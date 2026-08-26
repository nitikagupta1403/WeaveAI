"""Materialize frozen Experiment 08 images without learned features or outcomes."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageOps

from preprocess_audit import sha256_file


EXPECTED_MANIFEST_SHA256 = (
    "c464feafbb382c8e9d111433047298d8f42e1c661e018735e3df0b6016eaff4d"
)
OUTPUT_SIZE = 224


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--preprocessing-manifest", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    return parser.parse_args()


def pixel_sha256(image: Image.Image) -> str:
    pixels = np.ascontiguousarray(np.asarray(image.convert("L"), dtype=np.uint8))
    return hashlib.sha256(pixels.tobytes()).hexdigest()


def border_median(image: Image.Image) -> float:
    pixels = np.asarray(image.convert("L"), dtype=np.uint8)
    border = np.concatenate(
        [pixels[0, :], pixels[-1, :], pixels[:, 0], pixels[:, -1]]
    )
    return float(np.median(border) / 255.0)


def validate_box(box: list[int], width: int, height: int, label: str) -> None:
    if len(box) != 4:
        raise RuntimeError(f"{label} must have four coordinates")
    left, top, right, bottom = map(int, box)
    if not (0 <= left < right <= width and 0 <= top < bottom <= height):
        raise RuntimeError(f"Invalid {label}: {box} for {width}x{height}")


def normalize_polarity(image: Image.Image) -> tuple[Image.Image, float, bool]:
    median = border_median(image)
    inverted = median < 0.5
    return (ImageOps.invert(image) if inverted else image), median, inverted


def localize(
    image: Image.Image,
    garment_box: list[int],
    text_boxes: list[list[int]],
) -> Image.Image:
    left, top, right, bottom = map(int, garment_box)
    output = Image.new("L", image.size, 255)
    output.paste(image.crop((left, top, right, bottom)), (left, top))
    draw = ImageDraw.Draw(output)
    for box in text_boxes:
        draw.rectangle(tuple(map(int, box)), fill=255)
    return output


def resize_and_pad(image: Image.Image) -> tuple[Image.Image, int, int, int, int]:
    width, height = image.size
    scale = OUTPUT_SIZE / max(width, height)
    resized_width = max(1, round(width * scale))
    resized_height = max(1, round(height * scale))
    resized = image.resize((resized_width, resized_height), Image.Resampling.BICUBIC)
    left = (OUTPUT_SIZE - resized_width) // 2
    top = (OUTPUT_SIZE - resized_height) // 2
    output = Image.new("L", (OUTPUT_SIZE, OUTPUT_SIZE), 255)
    output.paste(resized, (left, top))
    return output, resized_width, resized_height, left, top


def main() -> None:
    args = parse_args()
    observed_manifest_hash = sha256_file(args.preprocessing_manifest)
    if observed_manifest_hash != EXPECTED_MANIFEST_SHA256:
        raise RuntimeError(
            "Preprocessing manifest SHA-256 mismatch: "
            f"{observed_manifest_hash} != {EXPECTED_MANIFEST_SHA256}"
        )

    manifest = pd.read_csv(args.preprocessing_manifest, keep_default_na=False)
    if len(manifest) != 2300:
        raise RuntimeError(f"Expected 2300 rows, found {len(manifest)}")
    if manifest["relative_path"].duplicated().any():
        raise RuntimeError("Manifest paths are not unique")
    if manifest["row_index"].duplicated().any():
        raise RuntimeError("Manifest row indices are not unique")

    image_root = args.output_root / "images"
    if image_root.exists() and any(image_root.iterdir()):
        raise RuntimeError(f"Refusing to overwrite non-empty output: {image_root}")
    image_root.mkdir(parents=True, exist_ok=True)

    rows = []
    inverted_count = 0
    for record in manifest.sort_values("row_index").to_dict("records"):
        source_path = args.data_root / record["relative_path"]
        if sha256_file(source_path) != record["source_sha256"]:
            raise RuntimeError(f"Source SHA-256 mismatch: {record['relative_path']}")

        with Image.open(source_path) as opened:
            oriented = ImageOps.exif_transpose(opened).convert("L")
        width, height = oriented.size
        garment_box = [
            int(record["garment_left"]),
            int(record["garment_top"]),
            int(record["garment_right"]),
            int(record["garment_bottom"]),
        ]
        text_boxes = json.loads(record["text_boxes_json"])
        validate_box(garment_box, width, height, "garment_box")
        for index, box in enumerate(text_boxes):
            validate_box(box, width, height, f"text_box_{index}")

        normalized, median, inverted = normalize_polarity(oriented)
        localized = localize(normalized, garment_box, text_boxes)
        processed, resized_width, resized_height, pad_left, pad_top = resize_and_pad(
            localized
        )
        inverted_count += int(inverted)

        filename = f"{int(record['row_index']):04d}.png"
        output_path = image_root / filename
        processed.save(output_path, format="PNG", optimize=False, compress_level=9)
        rows.append(
            {
                "row_index": int(record["row_index"]),
                "relative_path": record["relative_path"],
                "source_sha256": record["source_sha256"],
                "output_relative_path": f"images/{filename}",
                "output_png_sha256": sha256_file(output_path),
                "output_pixel_sha256": pixel_sha256(processed),
                "source_width": width,
                "source_height": height,
                "border_median": median,
                "inverted": inverted,
                "resized_width": resized_width,
                "resized_height": resized_height,
                "pad_left": pad_left,
                "pad_top": pad_top,
                "selection_cohort": record["selection_cohort"],
                "localization_source": record["localization_source"],
                "ambiguous_overlap": bool(record["ambiguous_overlap"]),
            }
        )

    output_manifest = args.output_root / "experiment08_materialized_images.csv"
    with output_manifest.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    aggregate = hashlib.sha256()
    for row in rows:
        aggregate.update(f"{row['row_index']}\t{row['output_pixel_sha256']}\n".encode())
    report = {
        "stage": "PRE_OUTCOME_IMAGE_MATERIALIZATION",
        "learned_features_extracted": False,
        "classifier_fitted": False,
        "predictive_outcome_computed": False,
        "images": len(rows),
        "output_size": [OUTPUT_SIZE, OUTPUT_SIZE],
        "inverted_images": inverted_count,
        "preprocessing_manifest_sha256": observed_manifest_hash,
        "materialized_manifest_sha256": sha256_file(output_manifest),
        "ordered_pixel_array_sha256": aggregate.hexdigest(),
    }
    report_path = args.output_root / "experiment08_materialization_report.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"PASS: 2300 frozen images materialized; report={report_path}")
    print(f"Manifest: {output_manifest}")
    print("STOP: Torch and DINOv2 were not loaded; no learned outcome was computed")


if __name__ == "__main__":
    main()
