from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image, ImageOps
from scipy import ndimage


DATA_ROOT = Path("/Users/nitikagupta/Desktop/Clo-Sket")
FROZEN_PREPROCESSING_MANIFEST = Path(
    "/Users/nitikagupta/Research/experiment08_preprocessing_freeze/"
    "experiment08_preprocessing_manifest.csv"
)
EXPECTED_FROZEN_MANIFEST_SHA256 = (
    "c464feafbb382c8e9d111433047298d8f42e1c661e018735e3df0b6016eaff4d"
)

CROP_ONLY_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05f_crop_vs_resampling/V3_CROP_ONLY"
)
CROP_ONLY_MANIFEST = CROP_ONLY_ROOT / "materialized_manifest.csv"
CROP_ONLY_REPORT = CROP_ONLY_ROOT / "report.json"

EXPECTED_CROP_ONLY_MANIFEST_SHA256 = (
    "19ab60c21c71de7918472142c36174ded9f8fae888eeb3320983ca2cc66a545e"
)
EXPECTED_CROP_ONLY_ORDERED_PIXEL_SHA256 = (
    "e44e5137fe301935551efd7e4a42a3246812849bfb874359a8b913a94fd3658c"
)

EXPECTED_ROWS = 2300

OUTPUT_ROOT = Path(
    "/Users/nitikagupta/Research/paper2_r0_05g_frame_border_gradient"
)
METRICS_CSV = OUTPUT_ROOT / "P2_R0_05G1_frame_border_gradient_metrics.csv"
REPORT_JSON = OUTPUT_ROOT / "P2_R0_05G1_report.json"

INK_THRESHOLD = 250
BORDER_BANDS_PX = (5, 10, 20)
GRADIENT_STRONG_QUANTILE = 0.90


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def pixel_sha256(image: Image.Image) -> str:
    pixels = np.ascontiguousarray(np.asarray(image.convert("L"), dtype=np.uint8))
    return hashlib.sha256(pixels.tobytes()).hexdigest()


def load_oriented_grayscale(path: Path) -> Image.Image:
    with Image.open(path) as opened:
        return ImageOps.exif_transpose(opened).convert("L")


def border_median(image: Image.Image) -> float:
    pixels = np.asarray(image, dtype=np.uint8)
    border = np.concatenate(
        [pixels[0, :], pixels[-1, :], pixels[:, 0], pixels[:, -1]]
    )
    return float(np.median(border) / 255.0)


def normalize_polarity(image: Image.Image):
    med = border_median(image)
    inverted = med < 0.5
    normalized = ImageOps.invert(image) if inverted else image
    return normalized, med, inverted


def diagnostic_ink_mask(gray: np.ndarray) -> np.ndarray:
    return np.asarray(gray, dtype=np.uint8) < INK_THRESHOLD


def sobel_magnitude(gray: np.ndarray) -> np.ndarray:
    x = np.asarray(gray, dtype=np.float64) / 255.0
    gx = ndimage.sobel(x, axis=1, mode="nearest")
    gy = ndimage.sobel(x, axis=0, mode="nearest")
    return np.hypot(gx, gy)


def border_band_mask(height: int, width: int, band: int) -> np.ndarray:
    band = int(min(band, max(1, min(height, width) // 2)))
    mask = np.zeros((height, width), dtype=bool)
    mask[:band, :] = True
    mask[-band:, :] = True
    mask[:, :band] = True
    mask[:, -band:] = True
    return mask


def foreground_geometry(mask: np.ndarray) -> dict:
    yy, xx = np.nonzero(mask)
    h, w = mask.shape

    if len(xx) == 0:
        return {
            "foreground_pixels": 0,
            "foreground_fraction": 0.0,
            "centroid_x": np.nan,
            "centroid_y": np.nan,
            "centroid_x_fraction": np.nan,
            "centroid_y_fraction": np.nan,
            "margin_left": np.nan,
            "margin_top": np.nan,
            "margin_right": np.nan,
            "margin_bottom": np.nan,
            "min_border_margin": np.nan,
            "max_foreground_radius": np.nan,
            "grid_max_radius_from_centroid": np.nan,
            "foreground_radius_to_grid_radius": np.nan,
        }

    cx = float(np.mean(xx))
    cy = float(np.mean(yy))

    left, right = int(np.min(xx)), int(np.max(xx))
    top, bottom = int(np.min(yy)), int(np.max(yy))

    margin_left = float(left)
    margin_top = float(top)
    margin_right = float(w - 1 - right)
    margin_bottom = float(h - 1 - bottom)

    fg_radius = np.hypot(xx.astype(float) - cx, yy.astype(float) - cy)
    max_fg_radius = float(np.max(fg_radius))

    corners = np.asarray(
        [[0.0, 0.0], [w - 1.0, 0.0], [0.0, h - 1.0], [w - 1.0, h - 1.0]]
    )
    grid_radius = float(
        np.max(np.hypot(corners[:, 0] - cx, corners[:, 1] - cy))
    )

    return {
        "foreground_pixels": int(len(xx)),
        "foreground_fraction": float(len(xx) / mask.size),
        "centroid_x": cx,
        "centroid_y": cy,
        "centroid_x_fraction": float(cx / max(w - 1, 1)),
        "centroid_y_fraction": float(cy / max(h - 1, 1)),
        "margin_left": margin_left,
        "margin_top": margin_top,
        "margin_right": margin_right,
        "margin_bottom": margin_bottom,
        "min_border_margin": float(
            min(margin_left, margin_top, margin_right, margin_bottom)
        ),
        "max_foreground_radius": max_fg_radius,
        "grid_max_radius_from_centroid": grid_radius,
        "foreground_radius_to_grid_radius": (
            float(max_fg_radius / grid_radius) if grid_radius > 0 else np.nan
        ),
    }


def foreground_border_metrics(mask: np.ndarray) -> dict:
    out = {}
    total = int(np.sum(mask))

    for band in BORDER_BANDS_PX:
        border = border_band_mask(mask.shape[0], mask.shape[1], band)
        near = int(np.sum(mask & border))
        out[f"foreground_near_border_{band}px"] = near
        out[f"foreground_near_border_{band}px_fraction"] = (
            float(near / total) if total > 0 else np.nan
        )

    return out


def gradient_metrics(gray: np.ndarray, foreground_mask: np.ndarray) -> dict:
    grad = sobel_magnitude(gray)

    if not np.isfinite(grad).all():
        raise RuntimeError("Gradient contains non-finite values")

    positive = grad[grad > 0]
    strong_threshold = (
        float(np.quantile(positive, GRADIENT_STRONG_QUANTILE))
        if positive.size
        else 0.0
    )
    strong = grad >= strong_threshold
    grad_sum = float(np.sum(grad))
    strong_total = int(np.sum(strong))

    out = {
        "gradient_mean_all": float(np.mean(grad)),
        "gradient_median_all": float(np.median(grad)),
        "gradient_max_all": float(np.max(grad)),
        "gradient_mean_foreground": (
            float(np.mean(grad[foreground_mask]))
            if np.any(foreground_mask)
            else np.nan
        ),
        "strong_gradient_threshold_q90_positive": strong_threshold,
        "strong_gradient_fraction_all": float(np.mean(strong)),
    }

    for band in BORDER_BANDS_PX:
        border = border_band_mask(gray.shape[0], gray.shape[1], band)
        out[f"gradient_mean_border_{band}px"] = float(np.mean(grad[border]))
        strong_border = int(np.sum(strong & border))
        out[f"strong_gradient_near_border_{band}px_fraction_of_strong"] = (
            float(strong_border / strong_total) if strong_total > 0 else np.nan
        )
        out[f"gradient_energy_border_{band}px_fraction"] = (
            float(np.sum(grad[border]) / grad_sum) if grad_sum > 0 else np.nan
        )

    return out


def prefix_dict(prefix: str, values: dict) -> dict:
    return {f"{prefix}_{k}": v for k, v in values.items()}


def validate_inputs():
    if sha256_file(FROZEN_PREPROCESSING_MANIFEST) != EXPECTED_FROZEN_MANIFEST_SHA256:
        raise RuntimeError("Frozen preprocessing manifest SHA mismatch")

    if sha256_file(CROP_ONLY_MANIFEST) != EXPECTED_CROP_ONLY_MANIFEST_SHA256:
        raise RuntimeError("CROP_ONLY manifest SHA mismatch")

    report = json.loads(CROP_ONLY_REPORT.read_text(encoding="utf-8"))

    if report["materialized_manifest_sha256"] != EXPECTED_CROP_ONLY_MANIFEST_SHA256:
        raise RuntimeError("CROP_ONLY report manifest SHA mismatch")

    if report["ordered_pixel_array_sha256"] != EXPECTED_CROP_ONLY_ORDERED_PIXEL_SHA256:
        raise RuntimeError("CROP_ONLY report ordered-pixel SHA mismatch")

    frozen = pd.read_csv(
        FROZEN_PREPROCESSING_MANIFEST, keep_default_na=False
    ).sort_values("row_index").reset_index(drop=True)

    crop = pd.read_csv(
        CROP_ONLY_MANIFEST, keep_default_na=False
    ).sort_values("row_index").reset_index(drop=True)

    if len(frozen) != EXPECTED_ROWS or len(crop) != EXPECTED_ROWS:
        raise RuntimeError("Expected 2300 rows in both manifests")

    expected_idx = np.arange(EXPECTED_ROWS, dtype=int)

    if not np.array_equal(frozen["row_index"].to_numpy(dtype=int), expected_idx):
        raise RuntimeError("Frozen row_index mismatch")

    if not np.array_equal(crop["row_index"].to_numpy(dtype=int), expected_idx):
        raise RuntimeError("CROP_ONLY row_index mismatch")

    if not np.array_equal(
        frozen["relative_path"].astype(str).to_numpy(),
        crop["relative_path"].astype(str).to_numpy(),
    ):
        raise RuntimeError("Frozen/CROP_ONLY population-order mismatch")

    print("P2-R0-05G1 INPUT PROVENANCE: PASS")
    print("Rows bound exactly:", EXPECTED_ROWS)

    return frozen, crop


def main():
    frozen, crop_manifest = validate_inputs()

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    if METRICS_CSV.exists():
        raise RuntimeError(f"Refusing to overwrite existing metrics file: {METRICS_CSV}")

    rows = []
    crop_pixel_aggregate = hashlib.sha256()
    max_centroid_mapback_error = 0.0

    for i in range(EXPECTED_ROWS):
        frozen_row = frozen.iloc[i]
        crop_row = crop_manifest.iloc[i]

        relative_path = str(frozen_row["relative_path"])
        raw_path = DATA_ROOT / relative_path
        crop_path = CROP_ONLY_ROOT / str(crop_row["output_relative_path"])

        if sha256_file(raw_path) != str(frozen_row["source_sha256"]):
            raise RuntimeError(f"RAW source SHA mismatch at row {i}")

        raw_oriented = load_oriented_grayscale(raw_path)
        raw_normalized, raw_border_med, raw_inverted = normalize_polarity(raw_oriented)
        raw_array = np.asarray(raw_normalized, dtype=np.uint8)

        left = int(frozen_row["garment_left"])
        top = int(frozen_row["garment_top"])
        right = int(frozen_row["garment_right"])
        bottom = int(frozen_row["garment_bottom"])

        raw_garment_array = raw_array[top:bottom, left:right]

        crop_image = load_oriented_grayscale(crop_path)
        crop_array = np.asarray(crop_image, dtype=np.uint8)

        observed_crop_pixel_sha = pixel_sha256(crop_image)
        expected_crop_pixel_sha = str(crop_row["output_pixel_sha256"])

        if observed_crop_pixel_sha != expected_crop_pixel_sha:
            raise RuntimeError(f"CROP_ONLY pixel SHA mismatch row {i}")

        crop_pixel_aggregate.update(
            f"{i}\t{expected_crop_pixel_sha}\n".encode()
        )

        if not np.array_equal(raw_garment_array, crop_array):
            max_diff = int(
                np.max(
                    np.abs(
                        raw_garment_array.astype(np.int16)
                        - crop_array.astype(np.int16)
                    )
                )
            )
            raise RuntimeError(
                f"CROP_ONLY != frozen RAW garment crop at row {i}; max_diff={max_diff}"
            )

        raw_mask = diagnostic_ink_mask(raw_array)
        crop_mask = diagnostic_ink_mask(crop_array)
        raw_crop_mask = diagnostic_ink_mask(raw_garment_array)

        raw_geom = foreground_geometry(raw_mask)
        crop_geom = foreground_geometry(crop_mask)
        raw_crop_geom = foreground_geometry(raw_crop_mask)

        raw_border = foreground_border_metrics(raw_mask)
        crop_border = foreground_border_metrics(crop_mask)

        raw_grad = gradient_metrics(raw_array, raw_mask)
        crop_grad = gradient_metrics(crop_array, crop_mask)
        raw_crop_grad = gradient_metrics(raw_garment_array, raw_crop_mask)

        crop_cx_raw = float(crop_geom["centroid_x"]) + left
        crop_cy_raw = float(crop_geom["centroid_y"]) + top
        raw_crop_cx_raw = float(raw_crop_geom["centroid_x"]) + left
        raw_crop_cy_raw = float(raw_crop_geom["centroid_y"]) + top

        mapback_error = float(
            np.hypot(crop_cx_raw - raw_crop_cx_raw, crop_cy_raw - raw_crop_cy_raw)
        )
        max_centroid_mapback_error = max(max_centroid_mapback_error, mapback_error)

        raw_h, raw_w = raw_array.shape
        crop_h, crop_w = crop_array.shape

        record = {
            "row_index": i,
            "relative_path": relative_path,
            "category": Path(relative_path).parts[0],
            "source_sha256": str(frozen_row["source_sha256"]),
            "crop_pixel_sha256": expected_crop_pixel_sha,
            "garment_left": left,
            "garment_top": top,
            "garment_right": right,
            "garment_bottom": bottom,
            "raw_width": raw_w,
            "raw_height": raw_h,
            "crop_width": crop_w,
            "crop_height": crop_h,
            "crop_area_fraction_of_raw": float((crop_h * crop_w) / (raw_h * raw_w)),
            "raw_border_median": raw_border_med,
            "raw_inverted": bool(raw_inverted),
            "crop_centroid_x_mapped_to_raw": crop_cx_raw,
            "crop_centroid_y_mapped_to_raw": crop_cy_raw,
            "raw_garment_box_centroid_x_mapped_to_raw": raw_crop_cx_raw,
            "raw_garment_box_centroid_y_mapped_to_raw": raw_crop_cy_raw,
            "centroid_mapback_error_px": mapback_error,
            "grid_radius_ratio_crop_to_raw": float(
                crop_geom["grid_max_radius_from_centroid"]
                / raw_geom["grid_max_radius_from_centroid"]
            ),
            "delta_foreground_fraction_crop_minus_raw": float(
                crop_geom["foreground_fraction"] - raw_geom["foreground_fraction"]
            ),
            "delta_min_border_margin_crop_minus_raw": float(
                crop_geom["min_border_margin"] - raw_geom["min_border_margin"]
            ),
            "delta_foreground_radius_to_grid_radius_crop_minus_raw": float(
                crop_geom["foreground_radius_to_grid_radius"]
                - raw_geom["foreground_radius_to_grid_radius"]
            ),
            "delta_gradient_mean_all_crop_minus_raw": float(
                crop_grad["gradient_mean_all"] - raw_grad["gradient_mean_all"]
            ),
        }

        record.update(prefix_dict("raw", raw_geom))
        record.update(prefix_dict("crop", crop_geom))
        record.update(prefix_dict("raw_garment_box", raw_crop_geom))
        record.update(prefix_dict("raw", raw_border))
        record.update(prefix_dict("crop", crop_border))
        record.update(prefix_dict("raw", raw_grad))
        record.update(prefix_dict("crop", crop_grad))
        record.update(prefix_dict("raw_garment_box", raw_crop_grad))

        for band in BORDER_BANDS_PX:
            record[
                f"delta_gradient_energy_border_{band}px_fraction_crop_minus_raw"
            ] = float(
                crop_grad[f"gradient_energy_border_{band}px_fraction"]
                - raw_grad[f"gradient_energy_border_{band}px_fraction"]
            )

            record[
                f"delta_strong_gradient_near_border_{band}px_fraction_crop_minus_raw"
            ] = float(
                crop_grad[
                    f"strong_gradient_near_border_{band}px_fraction_of_strong"
                ]
                - raw_grad[
                    f"strong_gradient_near_border_{band}px_fraction_of_strong"
                ]
            )

            record[
                f"delta_foreground_near_border_{band}px_fraction_crop_minus_raw"
            ] = float(
                crop_border[f"foreground_near_border_{band}px_fraction"]
                - raw_border[f"foreground_near_border_{band}px_fraction"]
            )

        rows.append(record)

        if (i + 1) % 250 == 0 or (i + 1) == EXPECTED_ROWS:
            print(f"Processed {i + 1}/{EXPECTED_ROWS}")

    if crop_pixel_aggregate.hexdigest() != EXPECTED_CROP_ONLY_ORDERED_PIXEL_SHA256:
        raise RuntimeError("CROP_ONLY ordered pixel aggregate mismatch")

    metrics = pd.DataFrame(rows)
    metrics.to_csv(METRICS_CSV, index=False, quoting=csv.QUOTE_MINIMAL)

    metrics_sha = sha256_file(METRICS_CSV)

    summary_columns = [
        "crop_area_fraction_of_raw",
        "raw_foreground_fraction",
        "crop_foreground_fraction",
        "raw_min_border_margin",
        "crop_min_border_margin",
        "raw_foreground_radius_to_grid_radius",
        "crop_foreground_radius_to_grid_radius",
        "raw_gradient_mean_all",
        "crop_gradient_mean_all",
        "raw_gradient_energy_border_10px_fraction",
        "crop_gradient_energy_border_10px_fraction",
        "raw_strong_gradient_near_border_10px_fraction_of_strong",
        "crop_strong_gradient_near_border_10px_fraction_of_strong",
    ]

    descriptive = {}

    for column in summary_columns:
        values = pd.to_numeric(metrics[column], errors="coerce").to_numpy(float)
        finite = values[np.isfinite(values)]
        descriptive[column] = {
            "mean": float(np.mean(finite)),
            "median": float(np.median(finite)),
            "q05": float(np.quantile(finite, 0.05)),
            "q95": float(np.quantile(finite, 0.95)),
        }

    report = {
        "stage": "P2_R0_05G1_FRAME_BORDER_GRADIENT_METRICS",
        "status": "PASS",
        "rows": int(len(metrics)),
        "diagnostic_mask_definition": f"grayscale intensity < {INK_THRESHOLD}",
        "gradient_operator": "scipy.ndimage.sobel, x/y magnitude",
        "gradient_strong_quantile": GRADIENT_STRONG_QUANTILE,
        "border_bands_px": list(BORDER_BANDS_PX),
        "frozen_preprocessing_manifest_sha256": EXPECTED_FROZEN_MANIFEST_SHA256,
        "crop_only_manifest_sha256": EXPECTED_CROP_ONLY_MANIFEST_SHA256,
        "crop_only_ordered_pixel_sha256": EXPECTED_CROP_ONLY_ORDERED_PIXEL_SHA256,
        "metrics_csv_sha256": metrics_sha,
        "max_centroid_mapback_error_px": float(max_centroid_mapback_error),
        "descriptive_summary": descriptive,
        "interpretation_boundary": (
            "05G1 materializes descriptive mechanism metrics only. "
            "It does not test association with Paper-II spectral effects "
            "and does not establish causality."
        ),
    }

    REPORT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print("\nP2-R0-05G1 FRAME / BORDER / GRADIENT METRICS: PASS")
    print("Rows:", len(metrics))
    print("Max centroid map-back error (px):", max_centroid_mapback_error)
    print("Metrics CSV:", METRICS_CSV)
    print("Metrics CSV SHA-256:", metrics_sha)
    print("Report:", REPORT_JSON)

    print("\nKey descriptive medians:")
    for column in summary_columns:
        print(f"{column}: {descriptive[column]['median']}")

    print(
        "\nSTOP — 05G1 metrics materialized. "
        "No mechanism association inference performed."
    )


if __name__ == "__main__":
    main()