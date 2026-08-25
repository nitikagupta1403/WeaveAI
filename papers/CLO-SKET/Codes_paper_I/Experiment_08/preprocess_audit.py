"""Preprocessing-only Experiment 08 audit; deliberately contains no DINOv2 code."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageOps


CANVAS = 224
BACKGROUND_THRESHOLD = 0.5
RESAMPLE = Image.Resampling.BICUBIC
EXPECTED_ROWS = 2300
EXPECTED_IDENTITIES = 230
EXPECTED_CATEGORIES = 23


def sha256_file(path: Path, block_size: int = 1 << 20) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(block_size):
            digest.update(block)
    return digest.hexdigest()


def border_values(array: np.ndarray) -> np.ndarray:
    if array.ndim != 2 or min(array.shape) < 2:
        raise ValueError(f"Expected a two-dimensional image at least 2x2, got {array.shape}")
    return np.concatenate((array[0, :], array[-1, :], array[1:-1, 0], array[1:-1, -1]))


def load_polarity_normalized_grayscale(path: Path) -> tuple[np.ndarray, dict]:
    with Image.open(path) as source:
        oriented = ImageOps.exif_transpose(source)
        original_mode = oriented.mode
        grayscale = oriented.convert("L")
        array = np.asarray(grayscale, dtype=np.float32) / 255.0
    background_before = float(np.median(border_values(array)))
    inverted = background_before < BACKGROUND_THRESHOLD
    if inverted:
        array = 1.0 - array
    background_after = float(np.median(border_values(array)))
    return array, {
        "original_mode": original_mode,
        "original_height": int(array.shape[0]),
        "original_width": int(array.shape[1]),
        "background_before": background_before,
        "inverted": inverted,
        "background_after": background_after,
    }


def resize_and_pad(array: np.ndarray) -> tuple[np.ndarray, dict]:
    height, width = array.shape
    scale = CANVAS / max(height, width)
    resized_width = max(1, min(CANVAS, round(width * scale)))
    resized_height = max(1, min(CANVAS, round(height * scale)))
    image = Image.fromarray(np.round(array * 255.0).astype(np.uint8))
    resized = image.resize((resized_width, resized_height), resample=RESAMPLE)
    left = (CANVAS - resized_width) // 2
    top = (CANVAS - resized_height) // 2
    canvas = Image.new("L", (CANVAS, CANVAS), color=255)
    canvas.paste(resized, (left, top))
    output = np.asarray(canvas, dtype=np.float32) / 255.0
    return output, {
        "resized_width": resized_width,
        "resized_height": resized_height,
        "pad_left": left,
        "pad_right": CANVAS - resized_width - left,
        "pad_top": top,
        "pad_bottom": CANVAS - resized_height - top,
    }


def processed_sha256(array: np.ndarray) -> str:
    uint8 = np.round(np.asarray(array) * 255.0).astype(np.uint8)
    return hashlib.sha256(np.ascontiguousarray(uint8).tobytes()).hexdigest()


def synthetic_tests() -> dict:
    cases = {
        "black_on_white": np.ones((80, 120), dtype=np.float32),
        "white_on_black": np.zeros((80, 120), dtype=np.float32),
    }
    cases["black_on_white"][20:60, 55:65] = 0.0
    cases["white_on_black"][20:60, 55:65] = 1.0
    outputs = {}
    for name, array in cases.items():
        before = float(np.median(border_values(array)))
        inverted = before < BACKGROUND_THRESHOLD
        normalized = 1.0 - array if inverted else array
        processed, geometry = resize_and_pad(normalized)
        if float(np.median(border_values(processed))) != 1.0:
            raise RuntimeError(f"Synthetic polarity/padding test failed for {name}")
        if processed.shape != (CANVAS, CANVAS):
            raise RuntimeError(f"Synthetic canvas test failed for {name}")
        outputs[name] = {"background_before": before, "inverted": inverted, **geometry}
    if not np.array_equal(
        np.round(resize_and_pad(cases["black_on_white"])[0] * 255),
        np.round(resize_and_pad(1.0 - cases["white_on_black"])[0] * 255),
    ):
        raise RuntimeError("Synthetic opposite-polarity images do not normalize identically")
    return outputs


def audit_record(data_root: Path, row: dict) -> tuple[dict, Image.Image]:
    path = data_root / row["relative_path"]
    if not path.is_file():
        raise FileNotFoundError(path)
    observed_source_hash = sha256_file(path)
    if observed_source_hash != row["sha256"]:
        raise RuntimeError(f"Source image hash changed: {row['relative_path']}")
    grayscale, source = load_polarity_normalized_grayscale(path)
    processed, geometry = resize_and_pad(grayscale)
    dark_fraction = float(np.mean(processed < 0.95))
    if not np.isfinite(processed).all() or processed.min() < 0.0 or processed.max() > 1.0:
        raise RuntimeError(f"Invalid processed values: {row['relative_path']}")
    record = {
        "row_index": int(row["row_index"]),
        "relative_path": row["relative_path"],
        "category": row["category"],
        "garment_id": row["garment_id"],
        "fold_id": int(row["fold_id"]),
        "source_sha256": observed_source_hash,
        "processed_sha256": processed_sha256(processed),
        "processed_min": float(processed.min()),
        "processed_max": float(processed.max()),
        "processed_mean": float(processed.mean()),
        "dark_pixel_fraction_lt_0_95": dark_fraction,
        **source,
        **geometry,
    }
    return record, Image.fromarray(np.round(processed * 255.0).astype(np.uint8))


def contact_sheet(items: list[tuple[str, Image.Image]], path: Path) -> None:
    columns = 5
    tile_width = CANVAS
    label_height = 28
    rows = math.ceil(len(items) / columns)
    sheet = Image.new("RGB", (columns * tile_width, rows * (CANVAS + label_height)), "white")
    draw = ImageDraw.Draw(sheet)
    for index, (label, image) in enumerate(items):
        x = (index % columns) * tile_width
        y = (index // columns) * (CANVAS + label_height)
        sheet.paste(image.convert("RGB"), (x, y))
        draw.text((x + 4, y + CANVAS + 4), label[:34], fill="black")
    sheet.save(path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--source-manifest", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    manifest = pd.read_csv(args.source_manifest, keep_default_na=False)
    required = {"row_index", "relative_path", "sha256", "category", "garment_id", "fold_id"}
    if missing := required.difference(manifest.columns):
        raise RuntimeError(f"Source manifest lacks columns: {sorted(missing)}")
    if len(manifest) != EXPECTED_ROWS:
        raise RuntimeError(f"Expected {EXPECTED_ROWS} source rows, got {len(manifest)}")
    if manifest["garment_id"].nunique() != EXPECTED_IDENTITIES:
        raise RuntimeError("Expected 230 garment identities")
    if manifest["category"].nunique() != EXPECTED_CATEGORIES:
        raise RuntimeError("Expected 23 categories")

    identity_sample = manifest.sort_values("row_index").groupby("garment_id", sort=True).head(1)
    category_sample = manifest.sort_values("row_index").groupby("category", sort=True).head(1)
    records = []
    category_images = {}
    for row in identity_sample.to_dict(orient="records"):
        record, image = audit_record(args.data_root, row)
        records.append(record)
        if row["row_index"] in set(category_sample["row_index"]):
            category_images[row["category"]] = image

    args.output_root.mkdir(parents=True, exist_ok=True)
    audit_csv = args.output_root / "experiment08_preprocessing_identity_audit.csv"
    with audit_csv.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    sheet_path = args.output_root / "experiment08_preprocessing_contact_sheet.png"
    contact_sheet(sorted(category_images.items()), sheet_path)
    inverted = sum(bool(record["inverted"]) for record in records)
    report = {
        "experiment": "CLO-SKET Experiment 08",
        "stage": "PREPROCESSING_AUDIT_ONLY",
        "learned_features_extracted": False,
        "classifier_fitted": False,
        "predictive_outcome_computed": False,
        "source_manifest_sha256": sha256_file(args.source_manifest),
        "identity_sample_rows": len(records),
        "category_contact_sheet_rows": len(category_images),
        "inverted_images": inverted,
        "dark_fraction_min": min(record["dark_pixel_fraction_lt_0_95"] for record in records),
        "dark_fraction_median": float(np.median([record["dark_pixel_fraction_lt_0_95"] for record in records])),
        "dark_fraction_max": max(record["dark_pixel_fraction_lt_0_95"] for record in records),
        "synthetic_tests": synthetic_tests(),
        "audit_csv": str(audit_csv),
        "audit_csv_sha256": sha256_file(audit_csv),
        "contact_sheet": str(sheet_path),
        "contact_sheet_sha256": sha256_file(sheet_path),
    }
    report_path = args.output_root / "experiment08_preprocessing_audit.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"PASS: preprocessing-only audit completed; report={report_path}")
    print(f"Contact sheet: {sheet_path}")
    print("STOP: DINOv2 was not loaded; no learned feature or outcome was computed")


if __name__ == "__main__":
    main()
