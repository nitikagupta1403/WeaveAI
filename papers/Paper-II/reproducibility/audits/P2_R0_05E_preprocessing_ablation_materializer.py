from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageOps


# =============================================================================
# P2-R0-05E — preprocessing-source ablation materializer
# =============================================================================

DATA_ROOT = Path(
    "/Users/nitikagupta/Desktop/Clo-Sket"
)

MANIFEST = Path(
    "/Users/nitikagupta/Research/"
    "experiment08_preprocessing_freeze/"
    "experiment08_preprocessing_manifest.csv"
)

EXPECTED_MANIFEST_SHA256 = (
    "c464feafbb382c8e9d111433047298d8f42e1c661e018735e3df0b6016eaff4d"
)

OUTPUT_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05e_preprocessing_ablation"
)

TEXT_ONLY_ROOT = (
    OUTPUT_ROOT
    / "V1_TEXT_ONLY"
)

LOCALIZE_ONLY_ROOT = (
    OUTPUT_ROOT
    / "V2_LOCALIZE_ONLY"
)

OUTPUT_SIZE = 224
CONTENT_SIZE = 196

V1_TEXT_ONLY_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05e_preprocessing_ablation/"
    "V1_TEXT_ONLY"
)

V2_LOCALIZE_ONLY_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05e_preprocessing_ablation/"
    "V2_LOCALIZE_ONLY"
)

def reconstruct_variant_geometry_from_manifest(
    ra14_module,
    variant_root: Path,
    expected_relative_paths,
    label: str,
):
    manifest_path = (
        variant_root
        / "materialized_manifest.csv"
    )

    manifest = pd.read_csv(
        manifest_path,
        keep_default_na=False,
    ).sort_values(
        "row_index"
    ).reset_index(
        drop=True
    )

    if len(manifest) != EXPECTED_ROWS:
        raise RuntimeError(
            f"{label}: expected {EXPECTED_ROWS} rows, "
            f"found {len(manifest)}"
        )

    relative_paths = manifest[
        "relative_path"
    ].astype(str).to_numpy()

    if not np.array_equal(
        relative_paths,
        np.asarray(
            expected_relative_paths,
            dtype=str,
        ),
    ):
        raise RuntimeError(
            f"{label}: population/order mismatch"
        )

    image_paths = [
        variant_root
        / str(rel)
        for rel in manifest[
            "output_relative_path"
        ]
    ]

    print(
        f"\nP2-R0-05E2 — reconstructing {label} geometry..."
    )

    conditional = (
        ra14_module.recover_geometry(
            image_paths
        )
    )

    conditional = np.asarray(
        conditional,
        dtype=np.float64,
    )

    if conditional.shape != (
        EXPECTED_ROWS,
        72,
        72,
    ):
        raise RuntimeError(
            f"{label}: unexpected conditional shape "
            f"{conditional.shape}"
        )

    mass_error = float(
        np.max(
            np.abs(
                conditional.sum(
                    axis=(1, 2)
                )
                - 1.0
            )
        )
    )

    shell_sums = conditional.sum(
        axis=2
    )

    nonempty = shell_sums > 0

    norm_error = float(
        np.max(
            np.abs(
                shell_sums[
                    nonempty
                ]
                - 1.0
            )
        )
    )

    fft_field = np.fft.rfft(
        conditional,
        axis=2,
    )

    if fft_field.shape != (
        EXPECTED_ROWS,
        72,
        37,
    ):
        raise RuntimeError(
            f"{label}: unexpected FFT shape "
            f"{fft_field.shape}"
        )

    if not (
        np.isfinite(
            conditional
        ).all()
        and
        np.isfinite(
            fft_field.real
        ).all()
        and
        np.isfinite(
            fft_field.imag
        ).all()
    ):
        raise RuntimeError(
            f"{label}: NaN/Inf found"
        )

    nyquist_imag = float(
        np.max(
            np.abs(
                fft_field[
                    :,
                    :,
                    36,
                ].imag
            )
        )
    )

    print(
        f"{label} conditional shape:",
        conditional.shape,
    )

    print(
        f"{label} rFFT shape:",
        fft_field.shape,
    )

    print(
        f"{label} max mass error:",
        mass_error,
    )

    print(
        f"{label} max shell normalization error:",
        norm_error,
    )

    print(
        f"{label} non-empty shells:",
        int(
            np.count_nonzero(
                nonempty
            )
        ),
        "/",
        int(
            nonempty.size
        ),
    )

    print(
        f"{label} max |Im(k=36)|:",
        nyquist_imag,
    )

    print(
        f"P2-R0-05E2 {label} FOURIER FIELD: PASS"
    )

    return conditional, fft_field

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()

    with path.open("rb") as f:
        while True:
            chunk = f.read(
                1024 * 1024
            )

            if not chunk:
                break

            h.update(chunk)

    return h.hexdigest()


def pixel_sha256(
    image: Image.Image,
) -> str:

    pixels = np.ascontiguousarray(
        np.asarray(
            image.convert("L"),
            dtype=np.uint8,
        )
    )

    return hashlib.sha256(
        pixels.tobytes()
    ).hexdigest()


def border_median(
    image: Image.Image,
) -> float:

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
        np.median(border)
        / 255.0
    )


def normalize_polarity(
    image: Image.Image,
) -> tuple[
    Image.Image,
    float,
    bool,
]:

    median = border_median(
        image
    )

    inverted = (
        median < 0.5
    )

    normalized = (
        ImageOps.invert(image)
        if inverted
        else image
    )

    return (
        normalized,
        median,
        inverted,
    )


def validate_box(
    box,
    width,
    height,
    label,
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
            f"Invalid {label}: "
            f"{box} for {width}x{height}"
        )


def whiten_text_boxes_full_frame(
    image: Image.Image,
    text_boxes,
) -> Image.Image:

    output = image.copy()

    draw = ImageDraw.Draw(
        output
    )

    for box in text_boxes:

        left, top, right, bottom = map(
            int,
            box,
        )

        draw.rectangle(
            (
                left,
                top,
                right,
                bottom,
            ),
            fill=255,
        )

    return output


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


def resize_and_pad(
    image: Image.Image,
):

    width, height = (
        image.size
    )

    scale = (
        CONTENT_SIZE
        /
        max(
            width,
            height,
        )
    )

    resized_width = max(
        1,
        round(
            width * scale
        ),
    )

    resized_height = max(
        1,
        round(
            height * scale
        ),
    )

    resized = image.resize(
        (
            resized_width,
            resized_height,
        ),
        Image.Resampling.BICUBIC,
    )

    left = (
        OUTPUT_SIZE
        - resized_width
    ) // 2

    top = (
        OUTPUT_SIZE
        - resized_height
    ) // 2

    output = Image.new(
        "L",
        (
            OUTPUT_SIZE,
            OUTPUT_SIZE,
        ),
        255,
    )

    output.paste(
        resized,
        (
            left,
            top,
        ),
    )

    return (
        output,
        resized_width,
        resized_height,
        left,
        top,
    )


def save_variant_manifest(
    rows,
    output_root,
    variant_name,
):

    manifest_path = (
        output_root
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
        writer.writerows(
            rows
        )

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
            "P2_R0_05E_PREPROCESSING_ABLATION",

        "variant":
            variant_name,

        "images":
            len(rows),

        "frozen_preprocessing_manifest_sha256":
            sha256_file(
                MANIFEST
            ),

        "materialized_manifest_sha256":
            sha256_file(
                manifest_path
            ),

        "ordered_pixel_array_sha256":
            aggregate.hexdigest(),
    }

    report_path = (
        output_root
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


def main():

    observed_manifest_sha = (
        sha256_file(
            MANIFEST
        )
    )

    if (
        observed_manifest_sha
        != EXPECTED_MANIFEST_SHA256
    ):
        raise RuntimeError(
            "Frozen preprocessing manifest "
            "SHA mismatch:\n"
            f"{observed_manifest_sha}\n"
            f"{EXPECTED_MANIFEST_SHA256}"
        )

    print(
        "P2-R0-05E FROZEN MANIFEST: PASS"
    )

    print(
        "Manifest SHA-256:",
        observed_manifest_sha,
    )

    manifest = pd.read_csv(
        MANIFEST,
        keep_default_na=False,
    )

    if len(manifest) != 2300:
        raise RuntimeError(
            f"Expected 2300 rows, "
            f"found {len(manifest)}"
        )

    for root in [
        TEXT_ONLY_ROOT,
        LOCALIZE_ONLY_ROOT,
    ]:

        image_root = (
            root
            / "images"
        )

        if (
            image_root.exists()
            and
            any(
                image_root.iterdir()
            )
        ):
            raise RuntimeError(
                "Refusing to overwrite "
                f"non-empty output: "
                f"{image_root}"
            )

        image_root.mkdir(
            parents=True,
            exist_ok=True,
        )

    text_only_rows = []
    localize_only_rows = []

    inverted_count = 0
    text_box_count = 0

    for n, record in enumerate(
        manifest
        .sort_values(
            "row_index"
        )
        .to_dict(
            "records"
        ),
        start=1,
    ):

        source_path = (
            DATA_ROOT
            / record[
                "relative_path"
            ]
        )

        observed_source_sha = (
            sha256_file(
                source_path
            )
        )

        if (
            observed_source_sha
            != record[
                "source_sha256"
            ]
        ):
            raise RuntimeError(
                "Source SHA mismatch: "
                f"{record['relative_path']}"
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

        text_boxes = json.loads(
            record[
                "text_boxes_json"
            ]
        )

        validate_box(
            garment_box,
            width,
            height,
            "garment_box",
        )

        for j, box in enumerate(
            text_boxes
        ):

            validate_box(
                box,
                width,
                height,
                f"text_box_{j}",
            )

        text_box_count += len(
            text_boxes
        )

        normalized, median, inverted = (
            normalize_polarity(
                oriented
            )
        )

        inverted_count += int(
            inverted
        )

        # ==============================================================
        # V1 — TEXT ONLY
        #
        # Same original image frame.
        # Same EXIF/grayscale/polarity normalization.
        # Whiten frozen text boxes.
        # No crop.
        # No resize.
        # No pad.
        # ==============================================================

        text_only = (
            whiten_text_boxes_full_frame(
                normalized,
                text_boxes,
            )
        )

        filename = (
            f"{int(record['row_index']):04d}.png"
        )

        text_only_path = (
            TEXT_ONLY_ROOT
            / "images"
            / filename
        )

        text_only.save(
            text_only_path,
            format="PNG",
            optimize=False,
            compress_level=9,
        )

        text_only_rows.append(
            {
                "row_index":
                    int(
                        record[
                            "row_index"
                        ]
                    ),

                "relative_path":
                    record[
                        "relative_path"
                    ],

                "source_sha256":
                    record[
                        "source_sha256"
                    ],

                "output_relative_path":
                    f"images/{filename}",

                "output_png_sha256":
                    sha256_file(
                        text_only_path
                    ),

                "output_pixel_sha256":
                    pixel_sha256(
                        text_only
                    ),

                "source_width":
                    width,

                "source_height":
                    height,

                "output_width":
                    text_only.size[0],

                "output_height":
                    text_only.size[1],

                "border_median":
                    median,

                "inverted":
                    inverted,

                "n_text_boxes":
                    len(
                        text_boxes
                    ),

                "variant":
                    "V1_TEXT_ONLY",
            }
        )

        # ==============================================================
        # V2 — LOCALIZE ONLY
        #
        # Same EXIF/grayscale/polarity normalization.
        # Frozen garment crop.
        # NO text whitening.
        # Exact frozen bicubic resize/pad.
        # ==============================================================

        localized = (
            crop_garment_only(
                normalized,
                garment_box,
            )
        )

        (
            localized_processed,
            resized_width,
            resized_height,
            pad_left,
            pad_top,
        ) = resize_and_pad(
            localized
        )

        localize_path = (
            LOCALIZE_ONLY_ROOT
            / "images"
            / filename
        )

        localized_processed.save(
            localize_path,
            format="PNG",
            optimize=False,
            compress_level=9,
        )

        localize_only_rows.append(
            {
                "row_index":
                    int(
                        record[
                            "row_index"
                        ]
                    ),

                "relative_path":
                    record[
                        "relative_path"
                    ],

                "source_sha256":
                    record[
                        "source_sha256"
                    ],

                "output_relative_path":
                    f"images/{filename}",

                "output_png_sha256":
                    sha256_file(
                        localize_path
                    ),

                "output_pixel_sha256":
                    pixel_sha256(
                        localized_processed
                    ),

                "source_width":
                    width,

                "source_height":
                    height,

                "crop_width":
                    (
                        garment_box[2]
                        - garment_box[0]
                    ),

                "crop_height":
                    (
                        garment_box[3]
                        - garment_box[1]
                    ),

                "border_median":
                    median,

                "inverted":
                    inverted,

                "resized_width":
                    resized_width,

                "resized_height":
                    resized_height,

                "pad_left":
                    pad_left,

                "pad_top":
                    pad_top,

                "n_text_boxes":
                    len(
                        text_boxes
                    ),

                "variant":
                    "V2_LOCALIZE_ONLY",
            }
        )

        if (
            n % 250 == 0
            or
            n == 2300
        ):

            print(
                f"Processed "
                f"{n}/2300"
            )

    (
        text_manifest,
        text_report,
        text_info,
    ) = save_variant_manifest(
        text_only_rows,
        TEXT_ONLY_ROOT,
        "V1_TEXT_ONLY",
    )

    (
        loc_manifest,
        loc_report,
        loc_info,
    ) = save_variant_manifest(
        localize_only_rows,
        LOCALIZE_ONLY_ROOT,
        "V2_LOCALIZE_ONLY",
    )

    print(
        "\nP2-R0-05E ABLATION MATERIALIZATION: PASS"
    )

    print(
        "Images:",
        2300,
    )

    print(
        "Frozen text boxes:",
        text_box_count,
    )

    print(
        "Polarity-inverted images:",
        inverted_count,
    )

    print(
        "\nV1 TEXT_ONLY"
    )

    print(
        "Manifest:",
        text_manifest,
    )

    print(
        "Manifest SHA-256:",
        text_info[
            "materialized_manifest_sha256"
        ],
    )

    print(
        "Ordered pixel SHA-256:",
        text_info[
            "ordered_pixel_array_sha256"
        ],
    )

    print(
        "\nV2 LOCALIZE_ONLY"
    )

    print(
        "Manifest:",
        loc_manifest,
    )

    print(
        "Manifest SHA-256:",
        loc_info[
            "materialized_manifest_sha256"
        ],
    )

    print(
        "Ordered pixel SHA-256:",
        loc_info[
            "ordered_pixel_array_sha256"
        ],
    )

    print(
        "\nSTOP — ablation image sets materialized; "
        "no Paper-II geometry or inference performed."
    )


if __name__ == "__main__":
    main()