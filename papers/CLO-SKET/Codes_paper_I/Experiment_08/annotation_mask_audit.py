"""Compare label-blind annotation masks without loading a learned model."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
from scipy import ndimage

from preprocess_audit import (
    CANVAS,
    audit_record,
    load_polarity_normalized_grayscale,
    resize_and_pad,
    sha256_file,
)


INK_THRESHOLD = 0.95
MARGINS = (0.05, 0.10)
STRUCTURAL_MIN_HEIGHT_FRACTION = 0.125
STRUCTURAL_MIN_INK_FRACTION = 0.01
STRUCTURAL_MAX_CENTRE_DISTANCE = 0.45
EXPECTED_ROWS = 2300
EXPECTED_IDENTITIES = 230
EXPECTED_CATEGORIES = 23


def principal_structure_box(array: np.ndarray) -> tuple[int, int, int, int, dict]:
    """Return the label-blind principal-structure box as left, top, right, bottom."""
    ink = array < INK_THRESHOLD
    if not ink.any():
        raise RuntimeError("Image contains no ink under the frozen threshold")

    # One-pixel dilation joins small gaps in garment strokes without using labels or OCR.
    expanded = ndimage.binary_dilation(ink, structure=np.ones((3, 3), dtype=bool), iterations=1)
    labels, count = ndimage.label(expanded, structure=np.ones((3, 3), dtype=np.uint8))
    height, width = array.shape
    image_cx = (width - 1) / 2.0
    image_cy = (height - 1) / 2.0
    diagonal = math.hypot(width, height)
    candidates = []
    for label_id in range(1, count + 1):
        ys, xs = np.nonzero(labels == label_id)
        if len(xs) == 0:
            continue
        left, right = int(xs.min()), int(xs.max()) + 1
        top, bottom = int(ys.min()), int(ys.max()) + 1
        component_ink = int(np.sum(ink & (labels == label_id)))
        extent_bonus = 1.0 + (right - left) / width + (bottom - top) / height
        distance = math.hypot(float(xs.mean()) - image_cx, float(ys.mean()) - image_cy) / diagonal
        centre_weight = math.exp(-2.0 * distance * distance)
        score = component_ink * extent_bonus * centre_weight
        candidates.append(
            {
                "label_id": label_id,
                "score": score,
                "component_ink": component_ink,
                "left": left,
                "top": top,
                "right": right,
                "bottom": bottom,
                "distance": distance,
            }
        )
    if not candidates:
        raise RuntimeError("Connected-component analysis produced no candidate")
    best = max(candidates, key=lambda item: (item["score"], item["component_ink"]))
    return best["left"], best["top"], best["right"], best["bottom"], {
        "component_count": count,
        "principal_component_ink": best["component_ink"],
        "principal_component_score": best["score"],
        "principal_component_centre_distance": best["distance"],
    }


def expanded_box(box: tuple[int, int, int, int], shape: tuple[int, int], margin: float) -> tuple[int, int, int, int]:
    left, top, right, bottom = box
    height, width = shape
    x_margin = math.ceil((right - left) * margin)
    y_margin = math.ceil((bottom - top) * margin)
    return (
        max(0, left - x_margin),
        max(0, top - y_margin),
        min(width, right + x_margin),
        min(height, bottom + y_margin),
    )


def multi_structure_box(array: np.ndarray) -> tuple[int, int, int, int, dict]:
    """Union all substantial vertically extended, centrally plausible components."""
    ink = array < INK_THRESHOLD
    total_ink = int(ink.sum())
    if total_ink == 0:
        raise RuntimeError("Image contains no ink under the frozen threshold")
    expanded = ndimage.binary_dilation(ink, structure=np.ones((3, 3), dtype=bool), iterations=1)
    labels, count = ndimage.label(expanded, structure=np.ones((3, 3), dtype=np.uint8))
    height, width = array.shape
    image_cx = (width - 1) / 2.0
    image_cy = (height - 1) / 2.0
    diagonal = math.hypot(width, height)
    selected = []
    for label_id in range(1, count + 1):
        ys, xs = np.nonzero(labels == label_id)
        if len(xs) == 0:
            continue
        left, right = int(xs.min()), int(xs.max()) + 1
        top, bottom = int(ys.min()), int(ys.max()) + 1
        component_ink = int(np.sum(ink & (labels == label_id)))
        height_fraction = (bottom - top) / height
        ink_fraction = component_ink / total_ink
        centre_distance = math.hypot(float(xs.mean()) - image_cx, float(ys.mean()) - image_cy) / diagonal
        if (
            height_fraction >= STRUCTURAL_MIN_HEIGHT_FRACTION
            and ink_fraction >= STRUCTURAL_MIN_INK_FRACTION
            and centre_distance <= STRUCTURAL_MAX_CENTRE_DISTANCE
        ):
            selected.append(
                {
                    "left": left,
                    "top": top,
                    "right": right,
                    "bottom": bottom,
                    "component_ink": component_ink,
                    "height_fraction": height_fraction,
                    "ink_fraction": ink_fraction,
                    "centre_distance": centre_distance,
                }
            )
    fallback = False
    if not selected:
        left, top, right, bottom, _ = principal_structure_box(array)
        selected = [{"left": left, "top": top, "right": right, "bottom": bottom}]
        fallback = True
    return (
        min(item["left"] for item in selected),
        min(item["top"] for item in selected),
        max(item["right"] for item in selected),
        max(item["bottom"] for item in selected),
        {
            "multi_component_count_total": count,
            "multi_component_count_selected": len(selected),
            "multi_component_fallback": fallback,
        },
    )


def apply_box_mask(array: np.ndarray, box: tuple[int, int, int, int]) -> np.ndarray:
    left, top, right, bottom = box
    masked = np.ones_like(array)
    masked[top:bottom, left:right] = array[top:bottom, left:right]
    return masked


def ink_count(array: np.ndarray) -> int:
    return int(np.sum(array < INK_THRESHOLD))


def image_sha256(image: Image.Image) -> str:
    return hashlib.sha256(np.ascontiguousarray(np.asarray(image, dtype=np.uint8)).tobytes()).hexdigest()


def make_comparison_sheet(items: list[dict], output: Path) -> None:
    label_width = 155
    heading_height = 30
    row_height = CANVAS + 24
    variants = ("raw", "margin_10", "multi_10")
    sheet = Image.new("RGB", (label_width + len(variants) * CANVAS, heading_height + len(items) * row_height), "white")
    draw = ImageDraw.Draw(sheet)
    for column, variant in enumerate(variants):
        draw.text((label_width + column * CANVAS + 6, 8), variant, fill="black")
    for row_index, item in enumerate(items):
        y = heading_height + row_index * row_height
        draw.text((4, y + 8), item["label"][:24], fill="black")
        for column, variant in enumerate(variants):
            sheet.paste(item[variant].convert("RGB"), (label_width + column * CANVAS, y))
    sheet.save(output)


def audit_image(data_root: Path, row: dict) -> tuple[dict, dict[str, Image.Image]]:
    # Reuse source-integrity verification from the approved preprocessing audit.
    audit_record(data_root, row)
    path = data_root / row["relative_path"]
    array, _ = load_polarity_normalized_grayscale(path)
    left, top, right, bottom, component = principal_structure_box(array)
    base_box = (left, top, right, bottom)
    original_ink = ink_count(array)
    raw, _ = resize_and_pad(array)
    images = {"raw": Image.fromarray(np.round(raw * 255.0).astype(np.uint8))}
    record = {
        "row_index": int(row["row_index"]),
        "relative_path": row["relative_path"],
        "category": row["category"],
        "garment_id": row["garment_id"],
        "original_ink_pixels": original_ink,
        "principal_left": left,
        "principal_top": top,
        "principal_right": right,
        "principal_bottom": bottom,
        **component,
    }
    for margin in MARGINS:
        box = expanded_box(base_box, array.shape, margin)
        masked = apply_box_mask(array, box)
        retained = ink_count(masked)
        processed, _ = resize_and_pad(masked)
        key = f"margin_{int(margin * 100)}"
        images[key] = Image.fromarray(np.round(processed * 255.0).astype(np.uint8))
        record[f"{key}_left"] = box[0]
        record[f"{key}_top"] = box[1]
        record[f"{key}_right"] = box[2]
        record[f"{key}_bottom"] = box[3]
        record[f"{key}_retained_ink_fraction"] = retained / original_ink
        record[f"{key}_processed_sha256"] = image_sha256(images[key])
    multi_left, multi_top, multi_right, multi_bottom, multi_details = multi_structure_box(array)
    multi_box = expanded_box(
        (multi_left, multi_top, multi_right, multi_bottom), array.shape, 0.10
    )
    multi_masked = apply_box_mask(array, multi_box)
    multi_retained = ink_count(multi_masked)
    multi_processed, _ = resize_and_pad(multi_masked)
    images["multi_10"] = Image.fromarray(
        np.round(multi_processed * 255.0).astype(np.uint8)
    )
    record.update(
        {
            "multi_10_left": multi_box[0],
            "multi_10_top": multi_box[1],
            "multi_10_right": multi_box[2],
            "multi_10_bottom": multi_box[3],
            "multi_10_retained_ink_fraction": multi_retained / original_ink,
            "multi_10_processed_sha256": image_sha256(images["multi_10"]),
            **multi_details,
        }
    )
    return record, images


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--source-manifest", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    manifest = pd.read_csv(args.source_manifest, keep_default_na=False)
    if len(manifest) != EXPECTED_ROWS:
        raise RuntimeError(f"Expected {EXPECTED_ROWS} rows, got {len(manifest)}")
    if manifest["garment_id"].nunique() != EXPECTED_IDENTITIES or manifest["category"].nunique() != EXPECTED_CATEGORIES:
        raise RuntimeError("Dataset identity/category structure mismatch")
    identity_sample = manifest.sort_values("row_index").groupby("garment_id", sort=True).head(1)
    category_rows = set(manifest.sort_values("row_index").groupby("category", sort=True).head(1)["row_index"])

    records = []
    category_items = []
    identity_items = []
    for row in identity_sample.to_dict(orient="records"):
        record, images = audit_image(args.data_root, row)
        records.append(record)
        item = {"label": f"{row['category']} | {row['garment_id']}", **images}
        identity_items.append(item)
        if row["row_index"] in category_rows:
            category_items.append(item)

    args.output_root.mkdir(parents=True, exist_ok=True)
    csv_path = args.output_root / "experiment08_annotation_mask_identity_audit.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    category_sheet = args.output_root / "experiment08_annotation_mask_category_comparison.png"
    identity_sheet = args.output_root / "experiment08_annotation_mask_identity_comparison.png"
    make_comparison_sheet(category_items, category_sheet)
    make_comparison_sheet(identity_items, identity_sheet)

    report = {
        "experiment": "CLO-SKET Experiment 08",
        "stage": "ANNOTATION_MASK_AUDIT_ONLY",
        "learned_features_extracted": False,
        "classifier_fitted": False,
        "predictive_outcome_computed": False,
        "selection_basis": "geometry preservation and peripheral-annotation removal only",
        "identity_sample_rows": len(records),
        "ink_threshold": INK_THRESHOLD,
        "component_connectivity": 8,
        "dilation_iterations": 1,
        "multi_structure_rule": {
            "minimum_height_fraction": STRUCTURAL_MIN_HEIGHT_FRACTION,
            "minimum_ink_fraction": STRUCTURAL_MIN_INK_FRACTION,
            "maximum_centre_distance": STRUCTURAL_MAX_CENTRE_DISTANCE,
            "margin": 0.10,
        },
        "margin_results": {
            f"margin_{int(margin * 100)}": {
                "retained_ink_min": min(record[f"margin_{int(margin * 100)}_retained_ink_fraction"] for record in records),
                "retained_ink_median": float(np.median([record[f"margin_{int(margin * 100)}_retained_ink_fraction"] for record in records])),
                "retained_ink_max": max(record[f"margin_{int(margin * 100)}_retained_ink_fraction"] for record in records),
            }
            for margin in MARGINS
        },
        "multi_10_results": {
            "retained_ink_min": min(record["multi_10_retained_ink_fraction"] for record in records),
            "retained_ink_median": float(np.median([record["multi_10_retained_ink_fraction"] for record in records])),
            "retained_ink_max": max(record["multi_10_retained_ink_fraction"] for record in records),
            "selected_components_min": min(record["multi_component_count_selected"] for record in records),
            "selected_components_median": float(np.median([record["multi_component_count_selected"] for record in records])),
            "selected_components_max": max(record["multi_component_count_selected"] for record in records),
            "fallback_count": sum(bool(record["multi_component_fallback"]) for record in records),
        },
        "audit_csv": str(csv_path),
        "audit_csv_sha256": sha256_file(csv_path),
        "category_sheet": str(category_sheet),
        "category_sheet_sha256": sha256_file(category_sheet),
        "identity_sheet": str(identity_sheet),
        "identity_sheet_sha256": sha256_file(identity_sheet),
    }
    report_path = args.output_root / "experiment08_annotation_mask_audit.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"PASS: annotation-mask audit completed; report={report_path}")
    print(f"Category comparison: {category_sheet}")
    print(f"Identity comparison: {identity_sheet}")
    print("STOP: DINOv2 was not loaded; no learned feature or outcome was computed")


if __name__ == "__main__":
    main()
