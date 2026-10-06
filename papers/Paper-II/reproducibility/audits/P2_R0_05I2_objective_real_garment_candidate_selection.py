from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd


# =============================================================================
# P2-R0-05I2 — OBJECTIVE REAL-GARMENT CANDIDATE SELECTION
#
# Goal
# ----
# Select exactly three garment identities for Canvas v0.4:
#
#   A) strongest RAW -> CROP_ONLY high-band loss
#   B) strongest RAW -> CROP_ONLY redistribution toward low+mid
#   C) most spectrally stable control
#
# Selection is based on per-image angular Fourier band fractions derived from
# the exact RAW and V3_CROP_ONLY conditional angular fields, then aggregated
# by garment identity using medians.
#
# Important
# ---------
# - This selects examples for visualization only.
# - It does NOT alter any Paper-II inference or model selection.
# - It does NOT cherry-pick by looking at Canvas appearance.
# - Selection criteria are frozen before viewing the chosen images.
# =============================================================================


AUDIT_DIR = Path(__file__).resolve().parent

BASE_AUDIT = (
    AUDIT_DIR
    / "P2_R0_05_annotation_control_sensitivity.py"
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

EXPECTED_CROP_ONLY_MANIFEST_SHA256 = (
    "19ab60c21c71de7918472142c36174ded9f8fae888eeb3320983ca2cc66a545e"
)

OUTPUT_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas"
)

PER_IMAGE_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05I2_per_image_band_fraction_change.csv"
)

IDENTITY_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05I2_identity_band_fraction_change.csv"
)

SELECTED_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05I2_selected_three_identities.csv"
)

REPORT_JSON = (
    OUTPUT_ROOT
    / "P2_R0_05I2_report.json"
)

EXPECTED_ROWS = 2300

BANDS = {
    "low_1_4": np.arange(1, 5, dtype=int),
    "mid_5_12": np.arange(5, 13, dtype=int),
    "highmid_13_24": np.arange(13, 25, dtype=int),
    "high_25_36": np.arange(25, 37, dtype=int),
}


# =============================================================================
# Helpers
# =============================================================================

def sha256_file(path: Path) -> str:
    import hashlib

    h = hashlib.sha256()

    with path.open("rb") as f:
        for chunk in iter(
            lambda: f.read(1024 * 1024),
            b"",
        ):
            h.update(chunk)

    return h.hexdigest()


def load_verified_definitions():

    if not BASE_AUDIT.is_file():
        raise RuntimeError(
            f"Base audit missing: {BASE_AUDIT}"
        )

    source = BASE_AUDIT.read_text(
        encoding="utf-8"
    )

    marker = 'if __name__ == "__main__":'

    if marker not in source:
        raise RuntimeError(
            "Could not locate __main__ boundary"
        )

    namespace = {
        "__file__": str(BASE_AUDIT),
        "__name__": "p2_r0_05_verified_definitions",
    }

    exec(
        compile(
            source.split(marker, 1)[0],
            str(BASE_AUDIT),
            "exec",
        ),
        namespace,
    )

    required = [
        "load_paper2_runtime",
        "validate_geometry_equivalence",
        "load_and_validate_fold_package",
        "normalize_runtime_relative_path",
    ]

    missing = [
        name
        for name in required
        if name not in namespace
    ]

    if missing:
        raise RuntimeError(
            f"Missing verified definitions: {missing}"
        )

    print(
        "P2-R0-05I2 VERIFIED DEFINITIONS: PASS"
    )

    return namespace


def reconstruct_crop(
    runtime: dict,
    ra14_module,
    normalize_runtime_relative_path,
):

    if not CROP_ONLY_MANIFEST.is_file():
        raise RuntimeError(
            "CROP_ONLY manifest missing"
        )

    if sha256_file(
        CROP_ONLY_MANIFEST
    ) != EXPECTED_CROP_ONLY_MANIFEST_SHA256:
        raise RuntimeError(
            "CROP_ONLY manifest SHA mismatch"
        )

    manifest = pd.read_csv(
        CROP_ONLY_MANIFEST,
        keep_default_na=False,
    ).sort_values(
        "row_index"
    ).reset_index(
        drop=True
    )

    runtime_paths = np.asarray(
        [
            normalize_runtime_relative_path(x)
            for x in runtime[
                "image_paths"
            ]
        ],
        dtype=str,
    )

    manifest_paths = manifest[
        "relative_path"
    ].astype(str).to_numpy()

    if not np.array_equal(
        runtime_paths,
        manifest_paths,
    ):
        raise RuntimeError(
            "CROP_ONLY/runtime order mismatch"
        )

    categories = np.asarray(
        runtime[
            "image_categories"
        ],
        dtype=str,
    )

    rows = []

    for i, rec in manifest.iterrows():

        p = (
            CROP_ONLY_ROOT
            / str(
                rec[
                    "output_relative_path"
                ]
            )
        )

        if not p.is_file():
            raise RuntimeError(
                f"Missing CROP_ONLY image: {p}"
            )

        rows.append(
            {
                "relative_path":
                    str(
                        rec[
                            "relative_path"
                        ]
                    ),

                "category":
                    str(
                        categories[
                            i
                        ]
                    ),

                "path":
                    p,
            }
        )

    (
        conditional,
        _nonempty,
        _radial_centers,
        mass_error,
        norm_error,
    ) = ra14_module.recover_geometry(
        rows
    )

    conditional = np.asarray(
        conditional,
        dtype=np.float64,
    )

    print(
        "P2-R0-05I2 CROP_ONLY RECONSTRUCTION: PASS"
    )

    print(
        "Max mass error:",
        mass_error,
    )

    print(
        "Max normalization error:",
        norm_error,
    )

    return conditional


def angular_band_fractions(
    conditional: np.ndarray,
) -> pd.DataFrame:
    """
    For each image:
      - angular rFFT over 72 angular samples
      - sum squared magnitude across radial shells
      - normalize non-DC energy across k=1..36
      - return band fractions
    """

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
            f"Unexpected field shape: {conditional.shape}"
        )

    F = np.fft.rfft(
        conditional,
        axis=2,
    )

    energy = np.abs(
        F
    ) ** 2

    # Sum over radial dimension, preserve image x harmonic.
    harmonic_energy = energy.sum(
        axis=1
    )

    non_dc_total = harmonic_energy[
        :,
        1:37,
    ].sum(
        axis=1
    )

    if np.any(
        non_dc_total
        <= 0
    ):
        raise RuntimeError(
            "Non-positive non-DC angular spectral energy"
        )

    rows = {}

    for name, ks in BANDS.items():

        e = harmonic_energy[
            :,
            ks,
        ].sum(
            axis=1
        )

        rows[
            name
        ] = (
            e
            / non_dc_total
        )

    df = pd.DataFrame(
        rows
    )

    # Sanity: fractions over the four disjoint bands should sum to 1.
    frac_sum = df.sum(
        axis=1
    ).to_numpy(
        dtype=float
    )

    if not np.allclose(
        frac_sum,
        1.0,
        atol=1e-12,
        rtol=0.0,
    ):
        raise RuntimeError(
            "Band fractions do not sum to 1"
        )

    return df


# =============================================================================
# Main
# =============================================================================

def main():

    OUTPUT_ROOT.mkdir(
        parents=True,
        exist_ok=True,
    )

    for path in (
        PER_IMAGE_CSV,
        IDENTITY_CSV,
        SELECTED_CSV,
        REPORT_JSON,
    ):
        if path.exists():
            raise RuntimeError(
                f"Refusing to overwrite: {path}"
            )

    base = load_verified_definitions()

    runtime = (
        base[
            "load_paper2_runtime"
        ]()
    )

    (
        ra14_module,
        raw_conditional,
    ) = (
        base[
            "validate_geometry_equivalence"
        ](
            runtime
        )
    )

    (
        G,
        C,
        folds,
        fold_sha,
    ) = (
        base[
            "load_and_validate_fold_package"
        ](
            runtime
        )
    )

    crop_conditional = reconstruct_crop(
        runtime,
        ra14_module,
        base[
            "normalize_runtime_relative_path"
        ],
    )

    raw_frac = angular_band_fractions(
        raw_conditional
    )

    crop_frac = angular_band_fractions(
        crop_conditional
    )

    relative_paths = np.asarray(
        [
            base[
                "normalize_runtime_relative_path"
            ](
                x
            )
            for x in runtime[
                "image_paths"
            ]
        ],
        dtype=str,
    )

    G = np.asarray(
        G,
        dtype=str,
    )

    C = np.asarray(
        C,
        dtype=str,
    )

    folds = np.asarray(
        folds,
        dtype=int,
    )

    per_image = pd.DataFrame(
        {
            "row_index":
                np.arange(
                    EXPECTED_ROWS,
                    dtype=int,
                ),

            "relative_path":
                relative_paths,

            "garment_identity":
                G,

            "category":
                C,

            "fold_id":
                folds,
        }
    )

    for band in BANDS:

        per_image[
            f"raw_{band}_fraction"
        ] = raw_frac[
            band
        ].to_numpy(
            dtype=float
        )

        per_image[
            f"crop_{band}_fraction"
        ] = crop_frac[
            band
        ].to_numpy(
            dtype=float
        )

        per_image[
            f"delta_{band}_fraction_crop_minus_raw"
        ] = (
            crop_frac[
                band
            ].to_numpy(
                dtype=float
            )
            -
            raw_frac[
                band
            ].to_numpy(
                dtype=float
            )
        )

    per_image[
        "delta_low_plus_mid_crop_minus_raw"
    ] = (
        per_image[
            "delta_low_1_4_fraction_crop_minus_raw"
        ]
        +
        per_image[
            "delta_mid_5_12_fraction_crop_minus_raw"
        ]
    )

    per_image[
        "band_fraction_l1_change"
    ] = (
        per_image[
            [
                f"delta_{band}_fraction_crop_minus_raw"
                for band in BANDS
            ]
        ]
        .abs()
        .sum(
            axis=1
        )
    )

    per_image.to_csv(
        PER_IMAGE_CSV,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Aggregate per garment identity using medians.
    # -------------------------------------------------------------------------

    agg_cols = [
        f"delta_{band}_fraction_crop_minus_raw"
        for band in BANDS
    ] + [
        "delta_low_plus_mid_crop_minus_raw",
        "band_fraction_l1_change",
    ]

    identity = (
        per_image
        .groupby(
            [
                "garment_identity",
                "category",
                "fold_id",
            ],
            as_index=False,
        )
        .agg(
            n_sketches=(
                "row_index",
                "size",
            ),

            **{
                f"median_{col}":
                    (
                        col,
                        "median",
                    )
                for col in agg_cols
            },
        )
    )

    if identity[
        "garment_identity"
    ].nunique() != 230:
        raise RuntimeError(
            "Expected exactly 230 garment identities"
        )

    identity.to_csv(
        IDENTITY_CSV,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Freeze objective selection.
    # -------------------------------------------------------------------------

    chosen_ids = set()
    selected_rows = []

    # A: strongest high-band loss.
    a = (
        identity
        .sort_values(
            "median_delta_high_25_36_fraction_crop_minus_raw",
            ascending=True,
        )
        .iloc[
            0
        ]
    )

    chosen_ids.add(
        str(
            a[
                "garment_identity"
            ]
        )
    )

    selected_rows.append(
        {
            "visual_role":
                "A_STRONG_HIGH_BAND_LOSS",

            **a.to_dict(),
        }
    )

    # B: strongest shift to low+mid, excluding A.
    b_pool = identity[
        ~identity[
            "garment_identity"
        ].astype(
            str
        ).isin(
            chosen_ids
        )
    ]

    b = (
        b_pool
        .sort_values(
            "median_delta_low_plus_mid_crop_minus_raw",
            ascending=False,
        )
        .iloc[
            0
        ]
    )

    chosen_ids.add(
        str(
            b[
                "garment_identity"
            ]
        )
    )

    selected_rows.append(
        {
            "visual_role":
                "B_STRONG_LOW_MID_REDISTRIBUTION",

            **b.to_dict(),
        }
    )

    # C: most stable control, excluding A/B.
    c_pool = identity[
        ~identity[
            "garment_identity"
        ].astype(
            str
        ).isin(
            chosen_ids
        )
    ]

    c = (
        c_pool
        .sort_values(
            "median_band_fraction_l1_change",
            ascending=True,
        )
        .iloc[
            0
        ]
    )

    selected_rows.append(
        {
            "visual_role":
                "C_STABLE_CONTROL",

            **c.to_dict(),
        }
    )

    selected = pd.DataFrame(
        selected_rows
    )

    selected.to_csv(
        SELECTED_CSV,
        index=False,
    )

    print(
        "\n"
        + "=" * 150
    )

    print(
        "P2-R0-05I2 — OBJECTIVE REAL-GARMENT CANDIDATES"
    )

    print(
        "=" * 150
    )

    display_cols = [
        "visual_role",
        "garment_identity",
        "category",
        "fold_id",
        "n_sketches",
        "median_delta_low_1_4_fraction_crop_minus_raw",
        "median_delta_mid_5_12_fraction_crop_minus_raw",
        "median_delta_highmid_13_24_fraction_crop_minus_raw",
        "median_delta_high_25_36_fraction_crop_minus_raw",
        "median_delta_low_plus_mid_crop_minus_raw",
        "median_band_fraction_l1_change",
    ]

    print(
        selected[
            display_cols
        ].to_string(
            index=False
        )
    )

    print(
        "\n"
        + "=" * 150
    )

    print(
        "P2-R0-05I2 — SELECTION RULES"
    )

    print(
        "=" * 150
    )

    print(
        "A = minimum identity-median Δ high_25_36 fraction (CROP - RAW)"
    )

    print(
        "B = maximum identity-median Δ(low + mid) fraction (CROP - RAW), excluding A"
    )

    print(
        "C = minimum identity-median L1 change across all 4 band fractions, excluding A/B"
    )

    report = {
        "stage":
            "P2_R0_05I2_OBJECTIVE_REAL_GARMENT_CANDIDATE_SELECTION",

        "status":
            "COMPLETE",

        "rows":
            EXPECTED_ROWS,

        "identities":
            230,

        "fold_package_sha256":
            fold_sha,

        "crop_manifest_sha256":
            EXPECTED_CROP_ONLY_MANIFEST_SHA256,

        "selection_rules":
            {
                "A":
                    "minimum median delta high_25_36 fraction crop-minus-raw",

                "B":
                    "maximum median delta low-plus-mid fraction crop-minus-raw excluding A",

                "C":
                    "minimum median L1 band-fraction change excluding A/B",
            },

        "selected":
            selected[
                [
                    "visual_role",
                    "garment_identity",
                    "category",
                    "fold_id",
                ]
            ].to_dict(
                orient="records"
            ),

        "interpretation_boundary":
            (
                "These identities are selected only as visualization exemplars "
                "using frozen, predeclared spectral criteria. They do not alter "
                "Paper-II inference and should not be presented as population-wide "
                "effect estimates."
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
        "\nP2-R0-05I2 CANDIDATE SELECTION: COMPLETE"
    )

    print(
        "Per-image:",
        PER_IMAGE_CSV,
    )

    print(
        "Identity summary:",
        IDENTITY_CSV,
    )

    print(
        "Selected three:",
        SELECTED_CSV,
    )

    print(
        "Report:",
        REPORT_JSON,
    )

    print(
        "\nSTOP — do not visually substitute different examples after selection."
    )


if __name__ == "__main__":
    main()