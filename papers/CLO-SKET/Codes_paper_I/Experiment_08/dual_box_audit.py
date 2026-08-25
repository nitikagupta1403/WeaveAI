"""Render and audit dual-box annotations without learned features or outcomes."""

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


INK_THRESHOLD = 242
THUMBNAIL = 300
LABEL_WIDTH = 190
ROW_HEIGHT = THUMBNAIL + 34
HEADING_HEIGHT = 34


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--source-manifest", type=Path, required=True)
    parser.add_argument("--annotations-jsonl", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    return parser.parse_args()


def load_annotations(path: Path) -> list[dict]:
    records = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if not records:
        raise RuntimeError("Annotation file is empty")
    paths = [record["relative_path"] for record in records]
    if len(paths) != len(set(paths)):
        raise RuntimeError("Duplicate annotation paths")
    if not all(record.get("reviewed") is True for record in records):
        raise RuntimeError("Every annotation must be reviewed")
    return sorted(records, key=lambda item: int(item["row_index"]))


def validate_box(box: list[int], width: int, height: int, name: str) -> None:
    if len(box) != 4:
        raise RuntimeError(f"{name} must contain four coordinates")
    left, top, right, bottom = map(int, box)
    if not (0 <= left < right <= width and 0 <= top < bottom <= height):
        raise RuntimeError(f"Invalid {name}: {box} for {width}x{height}")


def ink_count(image: Image.Image) -> int:
    return int(np.sum(np.asarray(image.convert("L")) < INK_THRESHOLD))


def garment_crop(image: Image.Image, box: list[int]) -> Image.Image:
    left, top, right, bottom = map(int, box)
    output = Image.new("L", image.size, 255)
    output.paste(image.crop((left, top, right, bottom)), (left, top))
    return output


def full_text_blank(image: Image.Image, boxes: list[list[int]]) -> Image.Image:
    output = image.copy()
    draw = ImageDraw.Draw(output)
    for box in boxes:
        draw.rectangle(tuple(map(int, box)), fill=255)
    return output


def overlap_area(left: list[int], right: list[int]) -> int:
    lx1, ly1, lx2, ly2 = map(int, left)
    rx1, ry1, rx2, ry2 = map(int, right)
    width = max(0, min(lx2, rx2) - max(lx1, rx1))
    height = max(0, min(ly2, ry2) - max(ly1, ry1))
    return width * height


def thumbnail(image: Image.Image) -> Image.Image:
    preview = ImageOps.autocontrast(image.convert("L")).convert("RGB")
    preview.thumbnail((THUMBNAIL - 8, THUMBNAIL - 8))
    cell = Image.new("RGB", (THUMBNAIL, THUMBNAIL), "white")
    cell.paste(
        preview,
        ((THUMBNAIL - preview.width) // 2, (THUMBNAIL - preview.height) // 2),
    )
    return cell


def image_pixel_sha256(image: Image.Image) -> str:
    array = np.ascontiguousarray(np.asarray(image.convert("L"), dtype=np.uint8))
    return hashlib.sha256(array.tobytes()).hexdigest()


def render_sheet(items: list[dict], path: Path) -> None:
    variants = ("raw", "safe_crop", "unsafe_blank")
    sheet = Image.new(
        "RGB",
        (
            LABEL_WIDTH + len(variants) * THUMBNAIL,
            HEADING_HEIGHT + len(items) * ROW_HEIGHT,
        ),
        "white",
    )
    draw = ImageDraw.Draw(sheet)
    for column, variant in enumerate(variants):
        draw.text(
            (LABEL_WIDTH + column * THUMBNAIL + 6, 9),
            variant,
            fill="black",
        )
    for row_number, item in enumerate(items):
        top = HEADING_HEIGHT + row_number * ROW_HEIGHT
        draw.text((5, top + 8), item["label"][:29], fill="black")
        draw.text(
            (5, top + 25),
            f"ambiguous={item['ambiguous']}",
            fill="black",
        )
        for column, variant in enumerate(variants):
            sheet.paste(
                thumbnail(item[variant]),
                (LABEL_WIDTH + column * THUMBNAIL, top),
            )
    sheet.save(path)


def main() -> None:
    args = parse_args()
    manifest = pd.read_csv(args.source_manifest, keep_default_na=False)
    by_path = manifest.set_index("relative_path")
    annotations = load_annotations(args.annotations_jsonl)
    audit_rows = []
    sheet_items = []

    for annotation in annotations:
        relative_path = annotation["relative_path"]
        if relative_path not in by_path.index:
            raise RuntimeError(f"Annotation path absent from manifest: {relative_path}")
        source = by_path.loc[relative_path]
        path = args.data_root / relative_path
        if sha256_file(path) != annotation["source_sha256"]:
            raise RuntimeError(f"Annotation/source hash mismatch: {relative_path}")
        if annotation["source_sha256"] != source["sha256"]:
            raise RuntimeError(f"Manifest/source hash mismatch: {relative_path}")

        raw = Image.open(path).convert("L")
        width, height = raw.size
        validate_box(annotation["garment_box"], width, height, "garment_box")
        for index, text_box in enumerate(annotation["text_boxes"]):
            validate_box(text_box, width, height, f"text_box_{index}")

        safe = garment_crop(raw, annotation["garment_box"])
        unsafe = full_text_blank(safe, annotation["text_boxes"])
        raw_ink = ink_count(raw)
        safe_ink = ink_count(safe)
        unsafe_ink = ink_count(unsafe)
        overlaps = [
            overlap_area(annotation["garment_box"], text_box)
            for text_box in annotation["text_boxes"]
        ]
        overlap_count = sum(area > 0 for area in overlaps)
        if bool(annotation["ambiguous"]) != (overlap_count > 0):
            raise RuntimeError(
                f"Ambiguity flag/box-overlap mismatch: {relative_path}"
            )

        audit_rows.append(
            {
                "row_index": int(annotation["row_index"]),
                "relative_path": relative_path,
                "garment_id": annotation["garment_id"],
                "raw_ink_pixels": raw_ink,
                "safe_crop_ink_pixels": safe_ink,
                "unsafe_blank_ink_pixels": unsafe_ink,
                "safe_crop_retained_ink_fraction": safe_ink / raw_ink,
                "unsafe_blank_retained_ink_fraction": unsafe_ink / raw_ink,
                "unsafe_incremental_removed_ink_fraction": (
                    safe_ink - unsafe_ink
                )
                / raw_ink,
                "text_box_count": len(annotation["text_boxes"]),
                "overlapping_text_box_count": overlap_count,
                "text_garment_box_overlap_area": sum(overlaps),
                "ambiguous": bool(annotation["ambiguous"]),
                "safe_crop_pixel_sha256": image_pixel_sha256(safe),
                "unsafe_blank_pixel_sha256": image_pixel_sha256(unsafe),
            }
        )
        sheet_items.append(
            {
                "label": f"{annotation['garment_id']} | {Path(relative_path).name}",
                "ambiguous": bool(annotation["ambiguous"]),
                "raw": raw,
                "safe_crop": safe,
                "unsafe_blank": unsafe,
            }
        )

    args.output_root.mkdir(parents=True, exist_ok=True)
    csv_path = args.output_root / "dual_box_pilot_audit.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(audit_rows[0]))
        writer.writeheader()
        writer.writerows(audit_rows)

    sheet_path = args.output_root / "dual_box_pilot_comparison.png"
    render_sheet(sheet_items, sheet_path)

    report = {
        "stage": "PRE_OUTCOME_DUAL_BOX_AUDIT_ONLY",
        "learned_features_extracted": False,
        "classifier_fitted": False,
        "predictive_outcome_computed": False,
        "annotation_records": len(annotations),
        "ambiguous_records": sum(row["ambiguous"] for row in audit_rows),
        "text_boxes": sum(row["text_box_count"] for row in audit_rows),
        "safe_crop_retained_ink_min": min(
            row["safe_crop_retained_ink_fraction"] for row in audit_rows
        ),
        "safe_crop_retained_ink_median": float(
            np.median(
                [
                    row["safe_crop_retained_ink_fraction"]
                    for row in audit_rows
                ]
            )
        ),
        "unsafe_incremental_removed_ink_max": max(
            row["unsafe_incremental_removed_ink_fraction"]
            for row in audit_rows
        ),
        "annotations_jsonl_sha256": sha256_file(args.annotations_jsonl),
        "audit_csv_sha256": sha256_file(csv_path),
        "comparison_sheet_sha256": sha256_file(sheet_path),
    }
    report_path = args.output_root / "dual_box_pilot_report.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"PASS: dual-box pilot rendered; report={report_path}")
    print(f"Comparison sheet: {sheet_path}")
    print("STOP: no learned feature or predictive outcome was computed")


if __name__ == "__main__":
    main()
