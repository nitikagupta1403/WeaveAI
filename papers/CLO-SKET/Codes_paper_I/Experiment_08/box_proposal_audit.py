"""Generate dataset-wide garment-box proposals and review sheets pre-outcome."""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageOps

from annotation_mask_audit import multi_structure_box
from preprocess_audit import (
    load_polarity_normalized_grayscale,
    sha256_file,
)


INK_THRESHOLD = 0.95
TILE_WIDTH = 310
TILE_HEIGHT = 190
THUMB = 145
GRID_COLUMNS = 5
GRID_ROWS = 10
ITEMS_PER_PAGE = GRID_COLUMNS * GRID_ROWS
HEADER_HEIGHT = 34


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--source-manifest", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    return parser.parse_args()


def ink_count(array: np.ndarray) -> int:
    return int(np.sum(array < INK_THRESHOLD))


def crop_to_box(array: np.ndarray, box: tuple[int, int, int, int]) -> np.ndarray:
    left, top, right, bottom = box
    output = np.ones_like(array)
    output[top:bottom, left:right] = array[top:bottom, left:right]
    return output


def preview(array: np.ndarray) -> Image.Image:
    image = Image.fromarray(
        np.round(np.clip(array, 0.0, 1.0) * 255.0).astype(np.uint8)
    )
    image = ImageOps.autocontrast(image).convert("RGB")
    image.thumbnail((THUMB, THUMB))
    cell = Image.new("RGB", (THUMB, THUMB), "white")
    cell.paste(
        image,
        ((THUMB - image.width) // 2, (THUMB - image.height) // 2),
    )
    return cell


def render_page(items: list[dict], page_number: int, output: Path) -> None:
    sheet = Image.new(
        "RGB",
        (
            GRID_COLUMNS * TILE_WIDTH,
            HEADER_HEIGHT + GRID_ROWS * TILE_HEIGHT,
        ),
        "white",
    )
    draw = ImageDraw.Draw(sheet)
    draw.text(
        (8, 10),
        f"Experiment 08 proposal review | page {page_number} | raw / proposed",
        fill="black",
    )
    for position, item in enumerate(items):
        row, column = divmod(position, GRID_COLUMNS)
        x = column * TILE_WIDTH
        y = HEADER_HEIGHT + row * TILE_HEIGHT
        sheet.paste(preview(item["raw"]), (x + 4, y + 4))
        sheet.paste(preview(item["proposed"]), (x + THUMB + 10, y + 4))
        draw.text(
            (x + 4, y + THUMB + 7),
            item["relative_path"][:43],
            fill="black",
        )
        draw.text(
            (x + 4, y + THUMB + 23),
            (
                f"retain={item['retained_ink_fraction']:.4f} "
                f"area={item['box_area_fraction']:.4f} "
                f"components={item['selected_components']}"
            ),
            fill="black",
        )
    sheet.save(output)


def main() -> None:
    args = parse_args()
    manifest = pd.read_csv(args.source_manifest, keep_default_na=False)
    required = {
        "row_index",
        "relative_path",
        "sha256",
        "category",
        "garment_id",
        "fold_id",
    }
    missing = required.difference(manifest.columns)
    if missing:
        raise RuntimeError(f"Source manifest lacks columns: {sorted(missing)}")
    if len(manifest) != 2300:
        raise RuntimeError(f"Expected 2300 rows, found {len(manifest)}")

    records = []
    images = []
    for row in manifest.sort_values("row_index").to_dict(orient="records"):
        path = args.data_root / row["relative_path"]
        if sha256_file(path) != row["sha256"]:
            raise RuntimeError(f"Source hash mismatch: {row['relative_path']}")
        array, _ = load_polarity_normalized_grayscale(path)
        left, top, right, bottom, details = multi_structure_box(array)
        box = (left, top, right, bottom)
        proposed = crop_to_box(array, box)
        raw_ink = ink_count(array)
        retained_ink = ink_count(proposed)
        height, width = array.shape
        box_area_fraction = (
            (right - left) * (bottom - top) / (width * height)
        )
        touches_boundary = (
            left == 0 or top == 0 or right == width or bottom == height
        )
        retained_fraction = retained_ink / raw_ink
        record = {
            "row_index": int(row["row_index"]),
            "relative_path": row["relative_path"],
            "source_sha256": row["sha256"],
            "category": row["category"],
            "garment_id": row["garment_id"],
            "fold_id": int(row["fold_id"]),
            "image_width": width,
            "image_height": height,
            "proposal_left": left,
            "proposal_top": top,
            "proposal_right": right,
            "proposal_bottom": bottom,
            "raw_ink_pixels": raw_ink,
            "proposal_ink_pixels": retained_ink,
            "retained_ink_fraction": retained_fraction,
            "removed_ink_fraction": 1.0 - retained_fraction,
            "box_area_fraction": box_area_fraction,
            "touches_image_boundary": touches_boundary,
            "selected_components": int(
                details["multi_component_count_selected"]
            ),
            "component_fallback": bool(
                details["multi_component_fallback"]
            ),
        }
        records.append(record)
        images.append({"raw": array, "proposed": proposed, **record})

    order = sorted(
        range(len(records)),
        key=lambda index: (
            records[index]["retained_ink_fraction"],
            -records[index]["box_area_fraction"],
            records[index]["relative_path"],
        ),
    )
    ranked_records = []
    ranked_images = []
    for rank, index in enumerate(order, start=1):
        record = dict(records[index])
        record["review_priority_rank"] = rank
        ranked_records.append(record)
        item = dict(images[index])
        item["review_priority_rank"] = rank
        ranked_images.append(item)

    args.output_root.mkdir(parents=True, exist_ok=True)
    csv_path = args.output_root / "experiment08_box_proposals.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(ranked_records[0]))
        writer.writeheader()
        writer.writerows(ranked_records)

    page_paths = []
    page_count = math.ceil(len(ranked_images) / ITEMS_PER_PAGE)
    for page_index in range(page_count):
        start = page_index * ITEMS_PER_PAGE
        items = ranked_images[start : start + ITEMS_PER_PAGE]
        page_path = args.output_root / (
            f"experiment08_box_proposals_page_{page_index + 1:02d}.png"
        )
        render_page(items, page_index + 1, page_path)
        page_paths.append(page_path)
        print(f"Rendered page {page_index + 1}/{page_count}: {page_path}")

    retained = [record["retained_ink_fraction"] for record in records]
    areas = [record["box_area_fraction"] for record in records]
    report = {
        "experiment": "CLO-SKET Experiment 08",
        "stage": "PRE_OUTCOME_BOX_PROPOSAL_AUDIT_ONLY",
        "learned_features_extracted": False,
        "classifier_fitted": False,
        "predictive_outcome_computed": False,
        "proposal_basis": "label-blind multi-component garment geometry",
        "automatic_approval_performed": False,
        "rows": len(records),
        "retained_ink_min": min(retained),
        "retained_ink_median": float(np.median(retained)),
        "retained_ink_max": max(retained),
        "box_area_fraction_min": min(areas),
        "box_area_fraction_median": float(np.median(areas)),
        "box_area_fraction_max": max(areas),
        "boundary_touch_count": sum(
            record["touches_image_boundary"] for record in records
        ),
        "fallback_count": sum(
            record["component_fallback"] for record in records
        ),
        "proposal_csv_sha256": sha256_file(csv_path),
        "contact_sheet_pages": [
            {
                "path": str(path),
                "sha256": sha256_file(path),
            }
            for path in page_paths
        ],
    }
    report_path = args.output_root / "experiment08_box_proposal_report.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"PASS: proposal audit completed; report={report_path}")
    print("STOP: proposals are not approvals; no learned outcome was computed")


if __name__ == "__main__":
    main()
