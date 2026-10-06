from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image, ImageOps


# =============================================================================
# P2-R0-05F1 — CROP_ONLY materializer
#
# Purpose:
#   Isolate pure garment localization/cropping from resize/pad/resampling.
#
# Pipeline:
#   EXIF transpose
#   -> grayscale
#   -> frozen polarity normalization
#   -> frozen garment bounding-box crop
#   -> NO text whitening
#   -> NO resize
#   -> NO padding
#
# This script ONLY materializes the controlled CROP_ONLY population.
# It performs NO Paper-II geometry, Fourier analysis, selection, or inference.
# =============================================================================


DATA_ROOT = Path(
    "/Users/nitikagupta/Desktop/Clo-Sket"
)

FROZEN_PREPROCESSING_MANIFEST = Path(
    "/Users/nitikagupta/Research/"
    "experiment08_preprocessing_freeze/"
    "experiment08_preprocessing_manifest.csv"
)

EXPECTED_FROZEN_MANIFEST_SHA256 = (
    "c464feafbb382c8e9d111433047298d8f42e1c661e018735e3df0b6016eaff4d"
)

OUTPUT_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05f_crop_vs_resampling/"
    "V3_CROP_ONLY"
)

IMAGE_ROOT = OUTPUT_ROOT / "images"

EXPECTED_ROWS = 2300


# =============================================================================
# Hash helpers
# =============================================================================

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()

    with path.open("rb") as f:
        while True:
            chunk = f.read(1024 * 1024)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()


def pixel_sha256(image: Image.Image) -> str:
    pixels = np.ascontiguousarray(
        np.asarray(
            image.convert("L"),
            dtype=np.uint8,
        )
    )

    return hashlib.sha256(
        pixels.tobytes()
    ).hexdigest()


# =============================================================================
# Frozen preprocessing helpers
# =============================================================================

def border_median(image: Image.Image) -> float:
    pixels = np.asarray(
        image.convert("L"),
        dtype=np.uint8,
    )

    border = np.concatenate(
        [
            pixels[0, :],
            pixels[-1, :],
            pixels[:, 0],
            pixels[:, -1],
        ]
    )

    return float(
        np.median(border) / 255.0
    )


def normalize_polarity(
    image: Image.Image,
) -> tuple[Image.Image, float, bool]:

    median = border_median(image)

    inverted = median < 0.5

    normalized = (
        ImageOps.invert(image)
        if inverted
        else image
    )

    return normalized, median, inverted


def validate_box(
    box,
    width: int,
    height: int,
    label: str,
):
    if len(box) != 4:
        raise RuntimeError(
            f"{label} must have 4 coordinates"
        )

    left, top, right, bottom = map(
        int,
        box,
    )

    if not (
        0 <= left < right <= width
        and
        0 <= top < bottom <= height
    ):
        raise RuntimeError(
            f"Invalid {label}: {box} "
            f"for image size {width}x{height}"
        )


def crop_garment_only(
    image: Image.Image,
    garment_box,
) -> Image.Image:

    left, top, right, bottom = map(
        int,
        garment_box,
    )

    return image.crop(
        (
            left,
            top,
            right,
            bottom,
        )
    )


# =============================================================================
# Output manifest / provenance
# =============================================================================

def save_materialized_manifest(rows):
    OUTPUT_ROOT.mkdir(
        parents=True,
        exist_ok=True,
    )

    manifest_path = (
        OUTPUT_ROOT
        / "materialized_manifest.csv"
    )

    with manifest_path.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as stream:

        writer = csv.DictWriter(
            stream,
            fieldnames=list(
                rows[0].keys()
            ),
        )

        writer.writeheader()
        writer.writerows(rows)

    aggregate = hashlib.sha256()

    for row in rows:
        aggregate.update(
            (
                f"{row['row_index']}\t"
                f"{row['output_pixel_sha256']}\n"
            ).encode()
        )

    report = {
        "stage":
            "P2_R0_05F1_CROP_ONLY_MATERIALIZATION",

        "variant":
            "V3_CROP_ONLY",

        "images":
            len(rows),

        "frozen_preprocessing_manifest_sha256":
            sha256_file(
                FROZEN_PREPROCESSING_MANIFEST
            ),

        "materialized_manifest_sha256":
            sha256_file(
                manifest_path
            ),

        "ordered_pixel_array_sha256":
            aggregate.hexdigest(),

        "transform":
            (
                "EXIF transpose -> grayscale -> "
                "polarity normalization -> "
                "frozen garment crop only"
            ),

        "text_whitening":
            False,

        "resize":
            False,

        "padding":
            False,
    }

    report_path = (
        OUTPUT_ROOT
        / "report.json"
    )

    report_path.write_text(
        json.dumps(
            report,
            indent=2,
        ),
        encoding="utf-8",
    )

    return (
        manifest_path,
        report_path,
        report,
    )


# =============================================================================
# MAIN
# =============================================================================

def main():

    # -------------------------------------------------------------------------
    # Frozen source-manifest gate
    # -------------------------------------------------------------------------

    if not FROZEN_PREPROCESSING_MANIFEST.is_file():
        raise RuntimeError(
            "Frozen preprocessing manifest missing: "
            f"{FROZEN_PREPROCESSING_MANIFEST}"
        )

    observed_manifest_sha = sha256_file(
        FROZEN_PREPROCESSING_MANIFEST
    )

    if (
        observed_manifest_sha
        != EXPECTED_FROZEN_MANIFEST_SHA256
    ):
        raise RuntimeError(
            "Frozen preprocessing manifest SHA mismatch:\n"
            f"observed: {observed_manifest_sha}\n"
            f"expected: {EXPECTED_FROZEN_MANIFEST_SHA256}"
        )

    print(
        "P2-R0-05F1 FROZEN MANIFEST: PASS"
    )
    print(
        "Manifest SHA-256:",
        observed_manifest_sha,
    )

    manifest = pd.read_csv(
        FROZEN_PREPROCESSING_MANIFEST,
        keep_default_na=False,
    ).sort_values(
        "row_index"
    ).reset_index(
        drop=True
    )

    if len(manifest) != EXPECTED_ROWS:
        raise RuntimeError(
            f"Expected {EXPECTED_ROWS} rows, "
            f"found {len(manifest)}"
        )

    expected_indices = np.arange(
        EXPECTED_ROWS,
        dtype=int,
    )

    observed_indices = manifest[
        "row_index"
    ].to_numpy(
        dtype=int
    )

    if not np.array_equal(
        observed_indices,
        expected_indices,
    ):
        raise RuntimeError(
            "Frozen manifest row_index "
            "is not exactly 0..2299"
        )

    # -------------------------------------------------------------------------
    # Protect existing outputs
    # -------------------------------------------------------------------------

    if (
        IMAGE_ROOT.exists()
        and
        any(
            IMAGE_ROOT.iterdir()
        )
    ):
        raise RuntimeError(
            "Refusing to overwrite non-empty output: "
            f"{IMAGE_ROOT}"
        )

    IMAGE_ROOT.mkdir(
        parents=True,
        exist_ok=True,
    )

    # -------------------------------------------------------------------------
    # Materialize CROP_ONLY population
    # -------------------------------------------------------------------------

    rows = []

    inverted_count = 0

    crop_widths = []
    crop_heights = []

    for n, record in enumerate(
        manifest.to_dict(
            "records"
        ),
        start=1,
    ):

        relative_path = str(
            record[
                "relative_path"
            ]
        )

        source_path = (
            DATA_ROOT
            / relative_path
        )

        if not source_path.is_file():
            raise RuntimeError(
                "Source image missing: "
                f"{source_path}"
            )

        observed_source_sha = sha256_file(
            source_path
        )

        expected_source_sha = str(
            record[
                "source_sha256"
            ]
        )

        if (
            observed_source_sha
            != expected_source_sha
        ):
            raise RuntimeError(
                "Source SHA mismatch: "
                f"{relative_path}"
            )

        with Image.open(
            source_path
        ) as opened:

            oriented = (
                ImageOps
                .exif_transpose(
                    opened
                )
                .convert("L")
            )

        width, height = (
            oriented.size
        )

        garment_box = [
            int(
                record[
                    "garment_left"
                ]
            ),
            int(
                record[
                    "garment_top"
                ]
            ),
            int(
                record[
                    "garment_right"
                ]
            ),
            int(
                record[
                    "garment_bottom"
                ]
            ),
        ]

        validate_box(
            garment_box,
            width,
            height,
            "garment_box",
        )

        normalized, median, inverted = (
            normalize_polarity(
                oriented
            )
        )

        inverted_count += int(
            inverted
        )

        # ---------------------------------------------------------------------
        # V3 — CROP ONLY
        #
        # Same EXIF/grayscale/polarity normalization as frozen preprocessing.
        # Frozen garment crop.
        # NO text whitening.
        # NO resize.
        # NO pad.
        # ---------------------------------------------------------------------

        cropped = crop_garment_only(
            normalized,
            garment_box,
        )

        crop_width, crop_height = (
            cropped.size
        )

        crop_widths.append(
            crop_width
        )
        crop_heights.append(
            crop_height
        )

        filename = (
            f"{int(record['row_index']):04d}.png"
        )

        output_path = (
            IMAGE_ROOT
            / filename
        )

        cropped.save(
            output_path,
            format="PNG",
            optimize=False,
            compress_level=9,
        )

        rows.append(
            {
                "row_index":
                    int(
                        record[
                            "row_index"
                        ]
                    ),

                "relative_path":
                    relative_path,

                "source_sha256":
                    expected_source_sha,

                "output_relative_path":
                    f"images/{filename}",

                "output_png_sha256":
                    sha256_file(
                        output_path
                    ),

                "output_pixel_sha256":
                    pixel_sha256(
                        cropped
                    ),

                "source_width":
                    width,

                "source_height":
                    height,

                "garment_left":
                    garment_box[0],

                "garment_top":
                    garment_box[1],

                "garment_right":
                    garment_box[2],

                "garment_bottom":
                    garment_box[3],

                "crop_width":
                    crop_width,

                "crop_height":
                    crop_height,

                "border_median":
                    median,

                "inverted":
                    inverted,

                "n_text_boxes":
                    int(
                        len(
                            json.loads(
                                record[
                                    "text_boxes_json"
                                ]
                            )
                        )
                    ),

                "variant":
                    "V3_CROP_ONLY",
            }
        )

        if (
            n % 250 == 0
            or
            n == EXPECTED_ROWS
        ):
            print(
                f"Processed "
                f"{n}/{EXPECTED_ROWS}"
            )

    # -------------------------------------------------------------------------
    # Save provenance
    # -------------------------------------------------------------------------

    (
        materialized_manifest,
        report_path,
        report,
    ) = save_materialized_manifest(
        rows
    )

    print(
        "\nP2-R0-05F1 CROP_ONLY "
        "MATERIALIZATION: PASS"
    )

    print(
        "Images:",
        len(rows),
    )

    print(
        "Polarity-inverted images:",
        inverted_count,
    )

    print(
        "Crop width range:",
        (
            min(crop_widths),
            max(crop_widths),
        ),
    )

    print(
        "Crop height range:",
        (
            min(crop_heights),
            max(crop_heights),
        ),
    )

    print(
        "Manifest:",
        materialized_manifest,
    )

    print(
        "Manifest SHA-256:",
        report[
            "materialized_manifest_sha256"
        ],
    )

    print(
        "Ordered pixel SHA-256:",
        report[
            "ordered_pixel_array_sha256"
        ],
    )

    print(
        "Report:",
        report_path,
    )

    print(
        "\nSTOP — CROP_ONLY image set "
        "materialized; no Paper-II geometry "
        "or inference performed."
    )


if __name__ == "__main__":
    main()