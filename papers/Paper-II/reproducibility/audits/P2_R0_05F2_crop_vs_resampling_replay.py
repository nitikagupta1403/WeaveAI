from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image


# =============================================================================
# P2-R0-05F2 — crop-vs-resampling replay
#
# Compare:
#   RAW
#   V1_TEXT_ONLY
#   V3_CROP_ONLY
#   V2_LOCALIZE_ONLY   (= crop + resize/pad)
#   CLEAN
#
# Purpose:
#   Determine whether the loss of the high_25_36 Paper-II effect is caused by
#   pure localization/cropping, or by the subsequent resize/pad/resampling step.
#
# IMPORTANT:
#   - Frozen historical artifacts are not modified.
#   - Verified D4 definitions are reused from the existing audit.
#   - This script performs replay/validation only.
# =============================================================================


AUDIT_DIR = Path(__file__).resolve().parent

BASE_AUDIT = (
    AUDIT_DIR
    / "P2_R0_05_annotation_control_sensitivity.py"
)


# -----------------------------------------------------------------------------
# Variant roots
# -----------------------------------------------------------------------------

V1_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05e_preprocessing_ablation/"
    "V1_TEXT_ONLY"
)

V2_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05e_preprocessing_ablation/"
    "V2_LOCALIZE_ONLY"
)

V3_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05f_crop_vs_resampling/"
    "V3_CROP_ONLY"
)


EXPECTED_ROWS = 2300

EXPECTED_PREPROCESSING_MANIFEST_SHA256 = (
    "c464feafbb382c8e9d111433047298d8f42e1c661e018735e3df0b6016eaff4d"
)


# -----------------------------------------------------------------------------
# Frozen variant provenance
# -----------------------------------------------------------------------------

EXPECTED_VARIANTS = {
    "V1_TEXT_ONLY": {
        "root": V1_ROOT,
        "manifest_sha256":
            "434d27e6ad1bbf69af3c2ba25ee792fc8676c384990e9c4d900a8969e21e784f",
        "ordered_pixel_sha256":
            "cf7f9940dd5b1ef0a0c6f60c7b165c4bd1f4a9df20a2e1c75e2374cfe0bd79f7",
    },

    "V2_LOCALIZE_ONLY": {
        "root": V2_ROOT,
        "manifest_sha256":
            "08d39bc98f113410850b80e30d8c38ed3515a22564cd0473c934f6cf2891e143",
        "ordered_pixel_sha256":
            "9e9fb9d88b98d5225a5bf12e72b3bc0487f1b69116d4f42f1bda74445fb7ef5f",
    },

    "V3_CROP_ONLY": {
        "root": V3_ROOT,
        "manifest_sha256":
            "19ab60c21c71de7918472142c36174ded9f8fae888eeb3320983ca2cc66a545e",
        "ordered_pixel_sha256":
            "e44e5137fe301935551efd7e4a42a3246812849bfb874359a8b913a94fd3658c",
    },
}


# =============================================================================
# Load verified D4 definitions without running its main block
# =============================================================================

def load_verified_d4_definitions():
    if not BASE_AUDIT.is_file():
        raise RuntimeError(
            f"Base D4 audit missing: {BASE_AUDIT}"
        )

    source = BASE_AUDIT.read_text(
        encoding="utf-8"
    )

    marker = 'if __name__ == "__main__":'

    if marker not in source:
        raise RuntimeError(
            "Could not locate __main__ boundary "
            "in verified D4 audit"
        )

    definitions_only = source.split(
        marker,
        1,
    )[0]

    namespace = {
        "__file__": str(BASE_AUDIT),
        "__name__": "p2_r0_05_verified_definitions",
    }

    exec(
        compile(
            definitions_only,
            str(BASE_AUDIT),
            "exec",
        ),
        namespace,
    )

    required = [
        "validate_clean_manifest",
        "load_paper2_runtime",
        "validate_raw_clean_binding",
        "validate_geometry_equivalence",
        "validate_clean_fourier",
        "load_and_validate_fold_package",
        "replay_cell13_selection",
        "run_cell13b_inference_exact",
        "normalize_runtime_relative_path",
    ]

    missing = [
        name
        for name in required
        if name not in namespace
    ]

    if missing:
        raise RuntimeError(
            "Verified D4 definitions missing: "
            f"{missing}"
        )

    print(
        "P2-R0-05F2 VERIFIED D4 DEFINITIONS: PASS"
    )

    return namespace


# =============================================================================
# Provenance helpers
# =============================================================================

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()

    with path.open("rb") as f:
        while True:
            chunk = f.read(
                1024 * 1024
            )

            if not chunk:
                break

            h.update(
                chunk
            )

    return h.hexdigest()


def pixel_sha256(path: Path) -> str:
    with Image.open(
        path
    ) as opened:

        pixels = np.ascontiguousarray(
            np.asarray(
                opened.convert("L"),
                dtype=np.uint8,
            )
        )

    return hashlib.sha256(
        pixels.tobytes()
    ).hexdigest()


def validate_variant_provenance(
    label: str,
    config: dict,
    runtime: dict,
    normalize_runtime_relative_path,
):
    root = config[
        "root"
    ]

    manifest_path = (
        root
        / "materialized_manifest.csv"
    )

    report_path = (
        root
        / "report.json"
    )

    if not manifest_path.is_file():
        raise RuntimeError(
            f"{label}: manifest missing: "
            f"{manifest_path}"
        )

    if not report_path.is_file():
        raise RuntimeError(
            f"{label}: report missing: "
            f"{report_path}"
        )

    report = json.loads(
        report_path.read_text(
            encoding="utf-8"
        )
    )

    if report.get(
        "variant"
    ) != label:
        raise RuntimeError(
            f"{label}: report variant mismatch"
        )

    if int(
        report.get(
            "images",
            -1,
        )
    ) != EXPECTED_ROWS:
        raise RuntimeError(
            f"{label}: report image count mismatch"
        )

    if (
        report.get(
            "frozen_preprocessing_manifest_sha256"
        )
        != EXPECTED_PREPROCESSING_MANIFEST_SHA256
    ):
        raise RuntimeError(
            f"{label}: frozen preprocessing "
            "manifest hash mismatch"
        )

    observed_manifest_sha = sha256_file(
        manifest_path
    )

    if (
        observed_manifest_sha
        != config[
            "manifest_sha256"
        ]
    ):
        raise RuntimeError(
            f"{label}: materialized manifest "
            "SHA mismatch"
        )

    if (
        report.get(
            "materialized_manifest_sha256"
        )
        != config[
            "manifest_sha256"
        ]
    ):
        raise RuntimeError(
            f"{label}: report manifest SHA mismatch"
        )

    manifest = pd.read_csv(
        manifest_path,
        keep_default_na=False,
    ).sort_values(
        "row_index"
    ).reset_index(
        drop=True
    )

    if len(
        manifest
    ) != EXPECTED_ROWS:
        raise RuntimeError(
            f"{label}: expected {EXPECTED_ROWS} rows, "
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
            f"{label}: row_index is not 0..2299"
        )

    runtime_relative = np.asarray(
        [
            normalize_runtime_relative_path(
                x
            )
            for x in runtime[
                "image_paths"
            ]
        ],
        dtype=str,
    )

    manifest_relative = manifest[
        "relative_path"
    ].astype(
        str
    ).to_numpy()

    if not np.array_equal(
        runtime_relative,
        manifest_relative,
    ):
        mismatch = np.flatnonzero(
            runtime_relative
            != manifest_relative
        )[0]

        raise RuntimeError(
            f"{label}: population/order mismatch "
            f"at row {int(mismatch)}\n"
            f"runtime={runtime_relative[mismatch]}\n"
            f"variant={manifest_relative[mismatch]}"
        )

    aggregate = hashlib.sha256()

    rows = []

    runtime_categories = np.asarray(
        runtime[
            "image_categories"
        ],
        dtype=str,
    )

    for i, record in manifest.iterrows():

        image_path = (
            root
            / str(
                record[
                    "output_relative_path"
                ]
            )
        )

        if not image_path.is_file():
            raise RuntimeError(
                f"{label}: missing image "
                f"{image_path}"
            )

        observed_pixel_sha = pixel_sha256(
            image_path
        )

        expected_pixel_sha = str(
            record[
                "output_pixel_sha256"
            ]
        )

        if (
            observed_pixel_sha
            != expected_pixel_sha
        ):
            raise RuntimeError(
                f"{label}: pixel SHA mismatch "
                f"row={i}"
            )

        aggregate.update(
            (
                f"{int(record['row_index'])}\t"
                f"{expected_pixel_sha}\n"
            ).encode()
        )

        rows.append(
            {
                "relative_path":
                    str(
                        record[
                            "relative_path"
                        ]
                    ),

                "category":
                    str(
                        runtime_categories[
                            i
                        ]
                    ),

                "path":
                    image_path,
            }
        )

    observed_ordered_pixel_sha = (
        aggregate.hexdigest()
    )

    if (
        observed_ordered_pixel_sha
        != config[
            "ordered_pixel_sha256"
        ]
    ):
        raise RuntimeError(
            f"{label}: ordered pixel SHA mismatch"
        )

    if (
        report.get(
            "ordered_pixel_array_sha256"
        )
        != config[
            "ordered_pixel_sha256"
        ]
    ):
        raise RuntimeError(
            f"{label}: report ordered-pixel "
            "SHA mismatch"
        )

    print(
        f"\nP2-R0-05F2 {label} PROVENANCE: PASS"
    )

    print(
        "Rows:",
        len(
            manifest
        ),
    )

    print(
        "Manifest SHA-256:",
        observed_manifest_sha,
    )

    print(
        "Ordered pixel SHA-256:",
        observed_ordered_pixel_sha,
    )

    print(
        "Population/order binding: PASS"
    )

    return (
        manifest,
        rows,
    )


# =============================================================================
# Geometry + Fourier reconstruction
# =============================================================================

def reconstruct_variant_geometry(
    label: str,
    rows,
    ra14_module,
):
    print(
        f"\nP2-R0-05F2 — reconstructing "
        f"{label} geometry..."
    )

    (
        conditional,
        nonempty,
        radial_centers,
        mass_error,
        normalization_error,
    ) = ra14_module.recover_geometry(
        rows
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
            f"{label}: unexpected conditional "
            f"shape {conditional.shape}"
        )

    if not np.isfinite(
        conditional
    ).all():
        raise RuntimeError(
            f"{label}: conditional contains "
            "NaN/Inf"
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
            f"{label}: unexpected rFFT shape "
            f"{fft_field.shape}"
        )

    if not (
        np.isfinite(
            fft_field.real
        ).all()
        and
        np.isfinite(
            fft_field.imag
        ).all()
    ):
        raise RuntimeError(
            f"{label}: FFT contains NaN/Inf"
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

    if nyquist_imag > 1e-12:
        raise RuntimeError(
            f"{label}: unexpected Nyquist "
            f"imaginary component "
            f"{nyquist_imag}"
        )

    print(
        f"\nP2-R0-05F2 {label} FOURIER FIELD: PASS"
    )

    print(
        "Conditional shape:",
        conditional.shape,
    )

    print(
        "rFFT shape:",
        fft_field.shape,
    )

    print(
        "Max mass error:",
        mass_error,
    )

    print(
        "Max conditional normalization error:",
        normalization_error,
    )

    print(
        "Non-empty shells:",
        int(
            np.sum(
                nonempty
            )
        ),
        "/",
        int(
            nonempty.size
        ),
    )

    print(
        "Max |Im(k=36)|:",
        nyquist_imag,
    )

    return (
        conditional,
        fft_field,
        radial_centers,
    )


# =============================================================================
# Result helpers
# =============================================================================

def compact_result(
    result: pd.DataFrame,
    dataset_label: str,
) -> pd.DataFrame:

    table = result[
        [
            "harmonic_band",
            "selected_representation",
            "selected_radial_budget",
            "observed_category_balanced_effect",
            "bootstrap_ci_low",
            "bootstrap_ci_high",
            "p_maxstat_FWER",
            "FWER_supported_0.05",
        ]
    ].copy()

    table.insert(
        0,
        "dataset",
        dataset_label,
    )

    return table


def run_replay(
    label: str,
    fft_field,
    radial_centers,
    G,
    C,
    folds,
    replay_selection,
    replay_inference,
):
    (
        selection,
        effect_tables,
    ) = replay_selection(
        fft_field,
        radial_centers,
        G,
        C,
        folds,
        label,
    )

    (
        result,
        paired,
        category_effects,
    ) = replay_inference(
        selection,
        effect_tables,
        label,
    )

    return {
        "selection":
            selection,

        "effect_tables":
            effect_tables,

        "result":
            result,

        "paired":
            paired,

        "category_effects":
            category_effects,
    }


# =============================================================================
# MAIN
# =============================================================================

def main():

    base = (
        load_verified_d4_definitions()
    )

    # -------------------------------------------------------------------------
    # Frozen CLEAN/runtime provenance
    # -------------------------------------------------------------------------

    clean_manifest = (
        base[
            "validate_clean_manifest"
        ]()
    )

    runtime = (
        base[
            "load_paper2_runtime"
        ]()
    )

    base[
        "validate_raw_clean_binding"
    ](
        runtime,
        clean_manifest,
    )

    # -------------------------------------------------------------------------
    # Verified RAW geometry
    # -------------------------------------------------------------------------

    (
        ra14_module,
        raw_conditional,
    ) = base[
        "validate_geometry_equivalence"
    ](
        runtime
    )

    raw_fft = np.fft.rfft(
        raw_conditional,
        axis=2,
    )

    if raw_fft.shape != (
        EXPECTED_ROWS,
        72,
        37,
    ):
        raise RuntimeError(
            "Unexpected RAW FFT shape"
        )

    print(
        "\nP2-R0-05F2 VERIFIED RAW FOURIER: PASS"
    )

    # -------------------------------------------------------------------------
    # CLEAN geometry
    # -------------------------------------------------------------------------

    (
        clean_conditional,
        clean_fft,
    ) = base[
        "validate_clean_fourier"
    ](
        clean_manifest,
        ra14_module,
    )

    # -------------------------------------------------------------------------
    # Frozen identity folds
    # -------------------------------------------------------------------------

    (
        G,
        C,
        folds,
        fold_sha,
    ) = base[
        "load_and_validate_fold_package"
    ](
        runtime
    )

    # -------------------------------------------------------------------------
    # V1 TEXT_ONLY
    # -------------------------------------------------------------------------

    (
        v1_manifest,
        v1_rows,
    ) = validate_variant_provenance(
        "V1_TEXT_ONLY",
        EXPECTED_VARIANTS[
            "V1_TEXT_ONLY"
        ],
        runtime,
        base[
            "normalize_runtime_relative_path"
        ],
    )

    (
        v1_conditional,
        v1_fft,
        v1_radial_centers,
    ) = reconstruct_variant_geometry(
        "V1_TEXT_ONLY",
        v1_rows,
        ra14_module,
    )

    # -------------------------------------------------------------------------
    # V3 CROP_ONLY
    # -------------------------------------------------------------------------

    (
        v3_manifest,
        v3_rows,
    ) = validate_variant_provenance(
        "V3_CROP_ONLY",
        EXPECTED_VARIANTS[
            "V3_CROP_ONLY"
        ],
        runtime,
        base[
            "normalize_runtime_relative_path"
        ],
    )

    (
        v3_conditional,
        v3_fft,
        v3_radial_centers,
    ) = reconstruct_variant_geometry(
        "V3_CROP_ONLY",
        v3_rows,
        ra14_module,
    )

    # -------------------------------------------------------------------------
    # V2 LOCALIZE_ONLY = crop + resize/pad
    # -------------------------------------------------------------------------

    (
        v2_manifest,
        v2_rows,
    ) = validate_variant_provenance(
        "V2_LOCALIZE_ONLY",
        EXPECTED_VARIANTS[
            "V2_LOCALIZE_ONLY"
        ],
        runtime,
        base[
            "normalize_runtime_relative_path"
        ],
    )

    (
        v2_conditional,
        v2_fft,
        v2_radial_centers,
    ) = reconstruct_variant_geometry(
        "V2_LOCALIZE_ONLY",
        v2_rows,
        ra14_module,
    )

    # -------------------------------------------------------------------------
    # Exact Cell-13 / Cell-13B replay functions
    # -------------------------------------------------------------------------

    replay_selection = (
        base[
            "replay_cell13_selection"
        ]
    )

    replay_inference = (
        base[
            "run_cell13b_inference_exact"
        ]
    )

    radial_centers = runtime[
        "radial_centers"
    ]

    # -------------------------------------------------------------------------
    # Run all five conditions
    # -------------------------------------------------------------------------

    raw = run_replay(
        "RAW",
        raw_fft,
        radial_centers,
        G,
        C,
        folds,
        replay_selection,
        replay_inference,
    )

    v1 = run_replay(
        "V1_TEXT_ONLY",
        v1_fft,
        radial_centers,
        G,
        C,
        folds,
        replay_selection,
        replay_inference,
    )

    v3 = run_replay(
        "V3_CROP_ONLY",
        v3_fft,
        radial_centers,
        G,
        C,
        folds,
        replay_selection,
        replay_inference,
    )

    v2 = run_replay(
        "V2_LOCALIZE_ONLY",
        v2_fft,
        radial_centers,
        G,
        C,
        folds,
        replay_selection,
        replay_inference,
    )

    clean = run_replay(
        "CLEAN",
        clean_fft,
        radial_centers,
        G,
        C,
        folds,
        replay_selection,
        replay_inference,
    )

    # -------------------------------------------------------------------------
    # Five-way compact comparison
    # -------------------------------------------------------------------------

    comparison = pd.concat(
        [
            compact_result(
                raw[
                    "result"
                ],
                "RAW",
            ),

            compact_result(
                v1[
                    "result"
                ],
                "V1_TEXT_ONLY",
            ),

            compact_result(
                v3[
                    "result"
                ],
                "V3_CROP_ONLY",
            ),

            compact_result(
                v2[
                    "result"
                ],
                "V2_LOCALIZE_ONLY",
            ),

            compact_result(
                clean[
                    "result"
                ],
                "CLEAN",
            ),
        ],
        ignore_index=True,
    )

    band_order = [
        "low_1_4",
        "mid_5_12",
        "highmid_13_24",
        "high_25_36",
    ]

    dataset_order = [
        "RAW",
        "V1_TEXT_ONLY",
        "V3_CROP_ONLY",
        "V2_LOCALIZE_ONLY",
        "CLEAN",
    ]

    comparison[
        "harmonic_band"
    ] = pd.Categorical(
        comparison[
            "harmonic_band"
        ],
        categories=band_order,
        ordered=True,
    )

    comparison[
        "dataset"
    ] = pd.Categorical(
        comparison[
            "dataset"
        ],
        categories=dataset_order,
        ordered=True,
    )

    comparison = comparison.sort_values(
        [
            "harmonic_band",
            "dataset",
        ]
    ).reset_index(
        drop=True
    )

    print(
        "\n"
        + "=" * 132
    )

    print(
        "P2-R0-05F2 — FIVE-WAY CROP-VS-RESAMPLING COMPARISON"
    )

    print(
        "=" * 132
    )

    print(
        comparison.to_string(
            index=False
        )
    )

    # -------------------------------------------------------------------------
    # High-band diagnostic
    # -------------------------------------------------------------------------

    high = (
        comparison
        .loc[
            comparison[
                "harmonic_band"
            ]
            == "high_25_36"
        ]
        .copy()
    )

    print(
        "\n"
        + "=" * 132
    )

    print(
        "P2-R0-05F2 — HIGH_25_36 CROP-VS-RESAMPLING DIAGNOSTIC"
    )

    print(
        "=" * 132
    )

    print(
        high.to_string(
            index=False
        )
    )

    # -------------------------------------------------------------------------
    # Explicit step-change summary
    # -------------------------------------------------------------------------

    high_idx = high.set_index(
        "dataset"
    )

    raw_effect = float(
        high_idx.loc[
            "RAW",
            "observed_category_balanced_effect",
        ]
    )

    text_effect = float(
        high_idx.loc[
            "V1_TEXT_ONLY",
            "observed_category_balanced_effect",
        ]
    )

    crop_effect = float(
        high_idx.loc[
            "V3_CROP_ONLY",
            "observed_category_balanced_effect",
        ]
    )

    localize_effect = float(
        high_idx.loc[
            "V2_LOCALIZE_ONLY",
            "observed_category_balanced_effect",
        ]
    )

    clean_effect = float(
        high_idx.loc[
            "CLEAN",
            "observed_category_balanced_effect",
        ]
    )

    print(
        "\nP2-R0-05F2 — HIGH-BAND EFFECT CHANGES"
    )

    print(
        "TEXT_ONLY - RAW:",
        text_effect - raw_effect,
    )

    print(
        "CROP_ONLY - RAW:",
        crop_effect - raw_effect,
    )

    print(
        "LOCALIZE_ONLY - CROP_ONLY:",
        localize_effect - crop_effect,
    )

    print(
        "CLEAN - LOCALIZE_ONLY:",
        clean_effect - localize_effect,
    )

    print(
        "\nP2-R0-05F2 CROP-VS-RESAMPLING "
        "REPLAY: COMPLETE"
    )


if __name__ == "__main__":
    main()