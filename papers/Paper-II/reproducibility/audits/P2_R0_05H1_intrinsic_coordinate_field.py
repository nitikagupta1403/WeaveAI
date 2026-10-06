from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image, ImageOps


# =============================================================================
# P2-R0-05H1 — ORACLE INTRINSIC-COORDINATE FIELD
#
# Purpose:
#   Test whether an object-centric coordinate system removes the raster-frame
#   dependence exposed by 05F/05G.
#
# This is NOT yet an object detector.
# We deliberately use the already-frozen garment bounding boxes as an ORACLE
# localization source so that only the coordinate system changes.
#
# Pipeline:
#   RAW page
#   -> exact frozen garment box
#   -> grayscale/polarity normalization
#   -> diagnostic garment-ink mask
#   -> foreground centroid
#   -> translate foreground coordinates to centroid
#   -> isotropic normalization by maximum foreground radius
#   -> 72 radial bins x 72 angular bins
#   -> conditional angular distribution per radial shell
#
# Critical invariance gate:
#   The intrinsic field reconstructed from the RAW garment-box pixels must be
#   identical to the intrinsic field reconstructed from the V3_CROP_ONLY image,
#   because those object pixels were already proven identical in 05G1.
#
# No Paper-II model selection or inference is performed here.
# =============================================================================


# -----------------------------------------------------------------------------
# Frozen inputs
# -----------------------------------------------------------------------------

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

CROP_ONLY_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05f_crop_vs_resampling/"
    "V3_CROP_ONLY"
)

CROP_ONLY_MANIFEST = (
    CROP_ONLY_ROOT
    / "materialized_manifest.csv"
)

CROP_ONLY_REPORT = (
    CROP_ONLY_ROOT
    / "report.json"
)

EXPECTED_CROP_ONLY_MANIFEST_SHA256 = (
    "19ab60c21c71de7918472142c36174ded9f8fae888eeb3320983ca2cc66a545e"
)

EXPECTED_CROP_ONLY_ORDERED_PIXEL_SHA256 = (
    "e44e5137fe301935551efd7e4a42a3246812849bfb874359a8b913a94fd3658c"
)

EXPECTED_ROWS = 2300


# -----------------------------------------------------------------------------
# Intrinsic representation settings
# -----------------------------------------------------------------------------

N_RADIAL = 72
N_ANGULAR = 72

INK_THRESHOLD = 250

RADIAL_EDGES = np.linspace(
    0.0,
    1.0,
    N_RADIAL + 1,
    dtype=np.float64,
)

ANGULAR_EDGES = np.linspace(
    0.0,
    2.0 * np.pi,
    N_ANGULAR + 1,
    dtype=np.float64,
)

RADIAL_CENTERS = (
    RADIAL_EDGES[:-1]
    + RADIAL_EDGES[1:]
) / 2.0


# -----------------------------------------------------------------------------
# Output
# -----------------------------------------------------------------------------

OUTPUT_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05h_intrinsic_coordinate"
)

FIELD_NPZ = (
    OUTPUT_ROOT
    / "P2_R0_05H1_intrinsic_coordinate_field.npz"
)

METRICS_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05H1_intrinsic_metrics.csv"
)

REPORT_JSON = (
    OUTPUT_ROOT
    / "P2_R0_05H1_report.json"
)


# =============================================================================
# Hash helpers
# =============================================================================

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()

    with path.open("rb") as f:
        for chunk in iter(
            lambda: f.read(1024 * 1024),
            b"",
        ):
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
# Image helpers
# =============================================================================

def load_oriented_grayscale(path: Path) -> Image.Image:
    with Image.open(path) as opened:
        return (
            ImageOps
            .exif_transpose(opened)
            .convert("L")
        )


def border_median(image: Image.Image) -> float:
    pixels = np.asarray(
        image,
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


def normalize_polarity(image: Image.Image):
    med = border_median(image)
    inverted = med < 0.5

    normalized = (
        ImageOps.invert(image)
        if inverted
        else image
    )

    return (
        normalized,
        med,
        inverted,
    )


def diagnostic_ink_mask(
    gray: np.ndarray,
) -> np.ndarray:

    return (
        np.asarray(
            gray,
            dtype=np.uint8,
        )
        < INK_THRESHOLD
    )


# =============================================================================
# Intrinsic coordinate representation
# =============================================================================

def intrinsic_field_from_mask(
    mask: np.ndarray,
):
    """
    Convert a binary object mask into a 72x72 radial-angular conditional field.

    Coordinates are intrinsic:
      - centroid translated to origin
      - isotropically normalized by maximum foreground radius

    Returns:
      conditional: (72,72)
      nonempty:    (72,)
      cx, cy
      max_radius_px
      foreground_pixels
      mass_error
      conditional_normalization_error
    """

    yy, xx = np.nonzero(mask)

    if len(xx) == 0:
        raise RuntimeError(
            "Intrinsic object mask contains no foreground pixels"
        )

    x = xx.astype(
        np.float64
    )

    y = yy.astype(
        np.float64
    )

    cx = float(
        np.mean(x)
    )

    cy = float(
        np.mean(y)
    )

    dx = x - cx
    dy = y - cy

    radius = np.hypot(
        dx,
        dy,
    )

    max_radius = float(
        np.max(radius)
    )

    if not np.isfinite(max_radius) or max_radius <= 0:
        raise RuntimeError(
            "Invalid intrinsic maximum foreground radius"
        )

    r_norm = np.clip(
        radius / max_radius,
        0.0,
        1.0,
    )

    theta = np.mod(
        np.arctan2(
            dy,
            dx,
        ),
        2.0 * np.pi,
    )

    # Histogram foreground mass in intrinsic polar coordinates.
    hist, _, _ = np.histogram2d(
        r_norm,
        theta,
        bins=(
            RADIAL_EDGES,
            ANGULAR_EDGES,
        ),
    )

    hist = hist.astype(
        np.float64
    )

    mass_error = float(
        abs(
            np.sum(hist)
            - len(xx)
        )
    )

    shell_mass = np.sum(
        hist,
        axis=1,
    )

    nonempty = (
        shell_mass > 0
    )

    conditional = np.zeros_like(
        hist,
        dtype=np.float64,
    )

    conditional[
        nonempty,
        :
    ] = (
        hist[
            nonempty,
            :
        ]
        /
        shell_mass[
            nonempty,
            None,
        ]
    )

    if np.any(nonempty):
        shell_sums = np.sum(
            conditional[
                nonempty,
                :
            ],
            axis=1,
        )

        normalization_error = float(
            np.max(
                np.abs(
                    shell_sums
                    - 1.0
                )
            )
        )

    else:
        normalization_error = np.nan

    return (
        conditional,
        nonempty,
        cx,
        cy,
        max_radius,
        int(len(xx)),
        mass_error,
        normalization_error,
    )


# =============================================================================
# Input validation
# =============================================================================

def validate_inputs():

    if not FROZEN_PREPROCESSING_MANIFEST.is_file():
        raise RuntimeError(
            "Frozen preprocessing manifest missing"
        )

    frozen_sha = sha256_file(
        FROZEN_PREPROCESSING_MANIFEST
    )

    if (
        frozen_sha
        != EXPECTED_FROZEN_MANIFEST_SHA256
    ):
        raise RuntimeError(
            "Frozen preprocessing manifest SHA mismatch"
        )

    if not CROP_ONLY_MANIFEST.is_file():
        raise RuntimeError(
            "CROP_ONLY manifest missing"
        )

    crop_manifest_sha = sha256_file(
        CROP_ONLY_MANIFEST
    )

    if (
        crop_manifest_sha
        != EXPECTED_CROP_ONLY_MANIFEST_SHA256
    ):
        raise RuntimeError(
            "CROP_ONLY manifest SHA mismatch"
        )

    report = json.loads(
        CROP_ONLY_REPORT.read_text(
            encoding="utf-8"
        )
    )

    if (
        report.get(
            "ordered_pixel_array_sha256"
        )
        != EXPECTED_CROP_ONLY_ORDERED_PIXEL_SHA256
    ):
        raise RuntimeError(
            "CROP_ONLY ordered pixel SHA mismatch"
        )

    frozen = pd.read_csv(
        FROZEN_PREPROCESSING_MANIFEST,
        keep_default_na=False,
    ).sort_values(
        "row_index"
    ).reset_index(
        drop=True
    )

    crop = pd.read_csv(
        CROP_ONLY_MANIFEST,
        keep_default_na=False,
    ).sort_values(
        "row_index"
    ).reset_index(
        drop=True
    )

    if (
        len(frozen) != EXPECTED_ROWS
        or
        len(crop) != EXPECTED_ROWS
    ):
        raise RuntimeError(
            "Expected exactly 2300 rows"
        )

    if not np.array_equal(
        frozen[
            "relative_path"
        ].astype(
            str
        ).to_numpy(),
        crop[
            "relative_path"
        ].astype(
            str
        ).to_numpy(),
    ):
        raise RuntimeError(
            "Frozen/CROP_ONLY population-order mismatch"
        )

    print(
        "P2-R0-05H1 INPUT PROVENANCE: PASS"
    )

    print(
        "Rows bound exactly:",
        EXPECTED_ROWS,
    )

    return (
        frozen,
        crop,
        frozen_sha,
        crop_manifest_sha,
    )


# =============================================================================
# MAIN
# =============================================================================

def main():

    (
        frozen,
        crop_manifest,
        frozen_sha,
        crop_manifest_sha,
    ) = validate_inputs()

    OUTPUT_ROOT.mkdir(
        parents=True,
        exist_ok=True,
    )

    for path in (
        FIELD_NPZ,
        METRICS_CSV,
        REPORT_JSON,
    ):
        if path.exists():
            raise RuntimeError(
                "Refusing to overwrite existing output: "
                f"{path}"
            )

    raw_box_fields = np.zeros(
        (
            EXPECTED_ROWS,
            N_RADIAL,
            N_ANGULAR,
        ),
        dtype=np.float64,
    )

    crop_fields = np.zeros_like(
        raw_box_fields
    )

    raw_box_nonempty = np.zeros(
        (
            EXPECTED_ROWS,
            N_RADIAL,
        ),
        dtype=bool,
    )

    crop_nonempty = np.zeros_like(
        raw_box_nonempty
    )

    rows = []

    max_pixel_diff = 0
    max_field_abs_diff = 0.0
    max_centroid_diff = 0.0
    max_scale_diff = 0.0

    crop_pixel_aggregate = hashlib.sha256()

    relative_paths = []
    categories = []

    for i in range(
        EXPECTED_ROWS
    ):

        frozen_row = frozen.iloc[
            i
        ]

        crop_row = crop_manifest.iloc[
            i
        ]

        relative_path = str(
            frozen_row[
                "relative_path"
            ]
        )

        category = Path(
            relative_path
        ).parts[0]

        relative_paths.append(
            relative_path
        )

        categories.append(
            category
        )

        raw_path = (
            DATA_ROOT
            / relative_path
        )

        crop_path = (
            CROP_ONLY_ROOT
            / str(
                crop_row[
                    "output_relative_path"
                ]
            )
        )

        # ---------------------------------------------------------------------
        # Exact RAW provenance
        # ---------------------------------------------------------------------

        if (
            sha256_file(
                raw_path
            )
            != str(
                frozen_row[
                    "source_sha256"
                ]
            )
        ):
            raise RuntimeError(
                f"RAW source SHA mismatch row {i}"
            )

        # ---------------------------------------------------------------------
        # RAW -> normalized -> frozen garment box
        # ---------------------------------------------------------------------

        raw_oriented = load_oriented_grayscale(
            raw_path
        )

        (
            raw_normalized,
            raw_border_med,
            raw_inverted,
        ) = normalize_polarity(
            raw_oriented
        )

        raw_array = np.asarray(
            raw_normalized,
            dtype=np.uint8,
        )

        left = int(
            frozen_row[
                "garment_left"
            ]
        )

        top = int(
            frozen_row[
                "garment_top"
            ]
        )

        right = int(
            frozen_row[
                "garment_right"
            ]
        )

        bottom = int(
            frozen_row[
                "garment_bottom"
            ]
        )

        raw_box_array = raw_array[
            top:bottom,
            left:right,
        ]

        # ---------------------------------------------------------------------
        # Exact CROP_ONLY artifact
        # ---------------------------------------------------------------------

        crop_image = load_oriented_grayscale(
            crop_path
        )

        crop_array = np.asarray(
            crop_image,
            dtype=np.uint8,
        )

        observed_crop_pixel_sha = pixel_sha256(
            crop_image
        )

        expected_crop_pixel_sha = str(
            crop_row[
                "output_pixel_sha256"
            ]
        )

        if (
            observed_crop_pixel_sha
            != expected_crop_pixel_sha
        ):
            raise RuntimeError(
                f"CROP_ONLY pixel SHA mismatch row {i}"
            )

        crop_pixel_aggregate.update(
            (
                f"{i}\t"
                f"{expected_crop_pixel_sha}\n"
            ).encode()
        )

        if (
            raw_box_array.shape
            != crop_array.shape
        ):
            raise RuntimeError(
                f"RAW-box/CROP shape mismatch row {i}"
            )

        pixel_diff = int(
            np.max(
                np.abs(
                    raw_box_array.astype(
                        np.int16
                    )
                    -
                    crop_array.astype(
                        np.int16
                    )
                )
            )
        )

        max_pixel_diff = max(
            max_pixel_diff,
            pixel_diff,
        )

        if pixel_diff != 0:
            raise RuntimeError(
                f"RAW-box/CROP pixel mismatch row {i}"
            )

        # ---------------------------------------------------------------------
        # Independent intrinsic reconstruction from both paths
        # ---------------------------------------------------------------------

        raw_box_mask = diagnostic_ink_mask(
            raw_box_array
        )

        crop_mask = diagnostic_ink_mask(
            crop_array
        )

        (
            raw_field,
            raw_nonempty,
            raw_cx,
            raw_cy,
            raw_scale,
            raw_fg_pixels,
            raw_mass_error,
            raw_norm_error,
        ) = intrinsic_field_from_mask(
            raw_box_mask
        )

        (
            crop_field,
            crop_nonempty_i,
            crop_cx,
            crop_cy,
            crop_scale,
            crop_fg_pixels,
            crop_mass_error,
            crop_norm_error,
        ) = intrinsic_field_from_mask(
            crop_mask
        )

        raw_box_fields[
            i
        ] = raw_field

        crop_fields[
            i
        ] = crop_field

        raw_box_nonempty[
            i
        ] = raw_nonempty

        crop_nonempty[
            i
        ] = crop_nonempty_i

        field_diff = float(
            np.max(
                np.abs(
                    raw_field
                    - crop_field
                )
            )
        )

        centroid_diff = float(
            np.hypot(
                raw_cx
                - crop_cx,
                raw_cy
                - crop_cy,
            )
        )

        scale_diff = float(
            abs(
                raw_scale
                - crop_scale
            )
        )

        max_field_abs_diff = max(
            max_field_abs_diff,
            field_diff,
        )

        max_centroid_diff = max(
            max_centroid_diff,
            centroid_diff,
        )

        max_scale_diff = max(
            max_scale_diff,
            scale_diff,
        )

        if field_diff > 1e-15:
            raise RuntimeError(
                "Intrinsic RAW-box/CROP field mismatch "
                f"row={i}, max_abs_diff={field_diff}"
            )

        if centroid_diff > 1e-15:
            raise RuntimeError(
                "Intrinsic centroid mismatch "
                f"row={i}, diff={centroid_diff}"
            )

        if scale_diff > 1e-15:
            raise RuntimeError(
                "Intrinsic scale mismatch "
                f"row={i}, diff={scale_diff}"
            )

        rows.append(
            {
                "row_index":
                    i,

                "relative_path":
                    relative_path,

                "category":
                    category,

                "raw_border_median":
                    raw_border_med,

                "raw_inverted":
                    bool(
                        raw_inverted
                    ),

                "crop_width":
                    int(
                        crop_array.shape[
                            1
                        ]
                    ),

                "crop_height":
                    int(
                        crop_array.shape[
                            0
                        ]
                    ),

                "foreground_pixels":
                    raw_fg_pixels,

                "intrinsic_centroid_x":
                    raw_cx,

                "intrinsic_centroid_y":
                    raw_cy,

                "intrinsic_scale_max_foreground_radius_px":
                    raw_scale,

                "nonempty_radial_shells":
                    int(
                        np.sum(
                            raw_nonempty
                        )
                    ),

                "raw_mass_error":
                    raw_mass_error,

                "crop_mass_error":
                    crop_mass_error,

                "raw_conditional_normalization_error":
                    raw_norm_error,

                "crop_conditional_normalization_error":
                    crop_norm_error,

                "raw_box_vs_crop_max_pixel_diff":
                    pixel_diff,

                "raw_box_vs_crop_intrinsic_field_max_abs_diff":
                    field_diff,

                "raw_box_vs_crop_centroid_diff_px":
                    centroid_diff,

                "raw_box_vs_crop_scale_diff_px":
                    scale_diff,
            }
        )

        if (
            (i + 1)
            % 250
            == 0
            or
            (i + 1)
            == EXPECTED_ROWS
        ):
            print(
                f"Processed "
                f"{i + 1}/{EXPECTED_ROWS}"
            )

    # -------------------------------------------------------------------------
    # Final provenance / invariance gates
    # -------------------------------------------------------------------------

    observed_crop_ordered_pixel_sha = (
        crop_pixel_aggregate.hexdigest()
    )

    if (
        observed_crop_ordered_pixel_sha
        != EXPECTED_CROP_ONLY_ORDERED_PIXEL_SHA256
    ):
        raise RuntimeError(
            "CROP_ONLY ordered pixel aggregate mismatch"
        )

    if not np.array_equal(
        raw_box_fields,
        crop_fields,
    ):
        raise RuntimeError(
            "Final intrinsic fields are not exactly equal"
        )

    if not np.array_equal(
        raw_box_nonempty,
        crop_nonempty,
    ):
        raise RuntimeError(
            "Final intrinsic nonempty-shell masks differ"
        )

    # -------------------------------------------------------------------------
    # Fourier validation of the new intrinsic field
    # -------------------------------------------------------------------------

    intrinsic_fft = np.fft.rfft(
        raw_box_fields,
        axis=2,
    )

    if intrinsic_fft.shape != (
        EXPECTED_ROWS,
        N_RADIAL,
        37,
    ):
        raise RuntimeError(
            f"Unexpected intrinsic rFFT shape: "
            f"{intrinsic_fft.shape}"
        )

    if not (
        np.isfinite(
            intrinsic_fft.real
        ).all()
        and
        np.isfinite(
            intrinsic_fft.imag
        ).all()
    ):
        raise RuntimeError(
            "Intrinsic Fourier field contains NaN/Inf"
        )

    nyquist_imag = float(
        np.max(
            np.abs(
                intrinsic_fft[
                    :,
                    :,
                    36,
                ].imag
            )
        )
    )

    if nyquist_imag > 1e-12:
        raise RuntimeError(
            "Intrinsic Nyquist imaginary component "
            f"unexpectedly non-zero: {nyquist_imag}"
        )

    # -------------------------------------------------------------------------
    # Save frozen intrinsic representation
    # -------------------------------------------------------------------------

    np.savez_compressed(
        FIELD_NPZ,

        conditional_angular=
            raw_box_fields,

        nonempty_shells=
            raw_box_nonempty,

        radial_centers=
            RADIAL_CENTERS,

        relative_paths=
            np.asarray(
                relative_paths,
                dtype=str,
            ),

        categories=
            np.asarray(
                categories,
                dtype=str,
            ),

        representation_name=
            np.asarray(
                [
                    "oracle_intrinsic_centroid_maxradius_v1"
                ],
                dtype=str,
            ),
    )

    metrics = pd.DataFrame(
        rows
    )

    metrics.to_csv(
        METRICS_CSV,
        index=False,
    )

    field_sha = sha256_file(
        FIELD_NPZ
    )

    metrics_sha = sha256_file(
        METRICS_CSV
    )

    nonempty_counts = np.sum(
        raw_box_nonempty,
        axis=1,
    )

    report = {
        "stage":
            "P2_R0_05H1_ORACLE_INTRINSIC_COORDINATE_FIELD",

        "status":
            "PASS",

        "rows":
            EXPECTED_ROWS,

        "representation":
            "oracle_intrinsic_centroid_maxradius_v1",

        "localization":
            "frozen garment bounding box (oracle; no detector)",

        "diagnostic_mask_definition":
            f"grayscale intensity < {INK_THRESHOLD}",

        "coordinate_transform":
            (
                "foreground pixels translated to their centroid; "
                "x/y coordinates isotropically divided by maximum "
                "foreground radius"
            ),

        "radial_bins":
            N_RADIAL,

        "angular_bins":
            N_ANGULAR,

        "frozen_preprocessing_manifest_sha256":
            frozen_sha,

        "crop_only_manifest_sha256":
            crop_manifest_sha,

        "crop_only_ordered_pixel_sha256":
            observed_crop_ordered_pixel_sha,

        "field_npz_sha256":
            field_sha,

        "metrics_csv_sha256":
            metrics_sha,

        "max_raw_box_vs_crop_pixel_diff":
            int(
                max_pixel_diff
            ),

        "max_raw_box_vs_crop_intrinsic_field_abs_diff":
            float(
                max_field_abs_diff
            ),

        "max_raw_box_vs_crop_centroid_diff_px":
            float(
                max_centroid_diff
            ),

        "max_raw_box_vs_crop_scale_diff_px":
            float(
                max_scale_diff
            ),

        "nonempty_radial_shells_median":
            float(
                np.median(
                    nonempty_counts
                )
            ),

        "nonempty_radial_shells_min":
            int(
                np.min(
                    nonempty_counts
                )
            ),

        "nonempty_radial_shells_max":
            int(
                np.max(
                    nonempty_counts
                )
            ),

        "nyquist_max_imag":
            nyquist_imag,

        "interpretation_boundary":
            (
                "05H1 establishes frame invariance of a new oracle-localized "
                "intrinsic coordinate representation. It does not establish "
                "retrieval utility, statistical support, or performance."
            ),
    }

    REPORT_JSON.write_text(
        json.dumps(
            report,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        "\nP2-R0-05H1 ORACLE INTRINSIC "
        "COORDINATE FIELD: PASS"
    )

    print(
        "Rows:",
        EXPECTED_ROWS,
    )

    print(
        "Intrinsic field shape:",
        raw_box_fields.shape,
    )

    print(
        "Intrinsic rFFT shape:",
        intrinsic_fft.shape,
    )

    print(
        "Max RAW-box vs CROP pixel diff:",
        max_pixel_diff,
    )

    print(
        "Max RAW-box vs CROP intrinsic field diff:",
        max_field_abs_diff,
    )

    print(
        "Max RAW-box vs CROP centroid diff (px):",
        max_centroid_diff,
    )

    print(
        "Max RAW-box vs CROP intrinsic scale diff (px):",
        max_scale_diff,
    )

    print(
        "Median non-empty radial shells:",
        float(
            np.median(
                nonempty_counts
            )
        ),
    )

    print(
        "Max |Im(k=36)|:",
        nyquist_imag,
    )

    print(
        "Field NPZ:",
        FIELD_NPZ,
    )

    print(
        "Field NPZ SHA-256:",
        field_sha,
    )

    print(
        "Metrics CSV:",
        METRICS_CSV,
    )

    print(
        "Metrics CSV SHA-256:",
        metrics_sha,
    )

    print(
        "Report:",
        REPORT_JSON,
    )

    print(
        "\nSTOP — intrinsic field frozen. "
        "No Paper-II selection or inference performed."
    )


if __name__ == "__main__":
    main()