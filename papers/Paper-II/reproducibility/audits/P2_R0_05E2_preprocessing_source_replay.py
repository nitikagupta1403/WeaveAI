from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image


# =============================================================================
# P2-R0-05E2 — preprocessing-source ablation replay
#
# Variants:
#   RAW
#   V1_TEXT_ONLY
#   V2_LOCALIZE_ONLY
#   CLEAN
#
# Purpose:
# Determine which preprocessing intervention changes the Paper-II
# harmonic-band inference, especially high_25_36.
# =============================================================================


AUDIT_DIR = Path(__file__).resolve().parent

BASE_AUDIT = (
    AUDIT_DIR
    / "P2_R0_05_annotation_control_sensitivity.py"
)

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
}

EXPECTED_PREPROCESSING_MANIFEST_SHA256 = (
    "c464feafbb382c8e9d111433047298d8f42e1c661e018735e3df0b6016eaff4d"
)

EXPECTED_ROWS = 2300


# =============================================================================
# Load ONLY verified definitions from P2-R0-05D script.
#
# We deliberately do not import/execute its __main__ section.
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
        "sha256_file",
        "pixel_sha256",
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
        "P2-R0-05E2 VERIFIED D4 DEFINITIONS: PASS"
    )

    return namespace


# =============================================================================
# Variant provenance
# =============================================================================

def pixel_sha256(path: Path) -> str:
    with Image.open(path) as opened:
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
    root = config["root"]

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

    if report.get("variant") != label:
        raise RuntimeError(
            f"{label}: report variant mismatch"
        )

    if int(report.get("images", -1)) != EXPECTED_ROWS:
        raise RuntimeError(
            f"{label}: report image count mismatch"
        )

    if (
        report.get(
            "frozen_preprocessing_manifest_sha256"
        )
        !=
        EXPECTED_PREPROCESSING_MANIFEST_SHA256
    ):
        raise RuntimeError(
            f"{label}: frozen preprocessing "
            "manifest hash mismatch"
        )

    observed_manifest_sha = hashlib.sha256(
        manifest_path.read_bytes()
    ).hexdigest()

    if (
        observed_manifest_sha
        != config["manifest_sha256"]
    ):
        raise RuntimeError(
            f"{label}: materialized manifest "
            "SHA mismatch"
        )

    if (
        report.get("materialized_manifest_sha256")
        != config["manifest_sha256"]
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

    if len(manifest) != EXPECTED_ROWS:
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
            normalize_runtime_relative_path(x)
            for x in runtime["image_paths"]
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
        runtime["image_categories"],
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
                        runtime_categories[i]
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
        != config["ordered_pixel_sha256"]
    ):
        raise RuntimeError(
            f"{label}: ordered pixel SHA mismatch"
        )

    if (
        report.get("ordered_pixel_array_sha256")
        != config["ordered_pixel_sha256"]
    ):
        raise RuntimeError(
            f"{label}: report ordered-pixel "
            "SHA mismatch"
        )

    print(
        f"\nP2-R0-05E2 {label} PROVENANCE: PASS"
    )
    print(
        "Rows:",
        len(manifest),
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

    return manifest, rows


# =============================================================================
# Variant geometry + Fourier
# =============================================================================

def reconstruct_variant_geometry(
    label: str,
    rows,
    ra14_module,
):
    print(
        f"\nP2-R0-05E2 — reconstructing "
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
        f"\nP2-R0-05E2 {label} FOURIER FIELD: PASS"
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
# Compact comparison helper
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


# =============================================================================
# MAIN
# =============================================================================

def main():

    base = (
        load_verified_d4_definitions()
    )

    # -------------------------------------------------------------------------
    # Frozen CLEAN + runtime provenance
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
    # Verified RAW geometry implementation
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
        "\nP2-R0-05E2 VERIFIED RAW FOURIER: PASS"
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
    # V1 provenance + geometry
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
    # V2 provenance + geometry
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
    # Exact Cell-13 + Cell-13B replays
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

    # RAW

    (
        raw_selection,
        raw_effect_tables,
    ) = replay_selection(
        raw_fft,
        runtime[
            "radial_centers"
        ],
        G,
        C,
        folds,
        "RAW",
    )

    (
        raw_result,
        raw_paired,
        raw_category_effects,
    ) = replay_inference(
        raw_selection,
        raw_effect_tables,
        "RAW",
    )

    # V1 TEXT_ONLY

    (
        v1_selection,
        v1_effect_tables,
    ) = replay_selection(
        v1_fft,
        runtime[
            "radial_centers"
        ],
        G,
        C,
        folds,
        "V1_TEXT_ONLY",
    )

    (
        v1_result,
        v1_paired,
        v1_category_effects,
    ) = replay_inference(
        v1_selection,
        v1_effect_tables,
        "V1_TEXT_ONLY",
    )

    # V2 LOCALIZE_ONLY

    (
        v2_selection,
        v2_effect_tables,
    ) = replay_selection(
        v2_fft,
        runtime[
            "radial_centers"
        ],
        G,
        C,
        folds,
        "V2_LOCALIZE_ONLY",
    )

    (
        v2_result,
        v2_paired,
        v2_category_effects,
    ) = replay_inference(
        v2_selection,
        v2_effect_tables,
        "V2_LOCALIZE_ONLY",
    )

    # CLEAN

    (
        clean_selection,
        clean_effect_tables,
    ) = replay_selection(
        clean_fft,
        runtime[
            "radial_centers"
        ],
        G,
        C,
        folds,
        "CLEAN",
    )

    (
        clean_result,
        clean_paired,
        clean_category_effects,
    ) = replay_inference(
        clean_selection,
        clean_effect_tables,
        "CLEAN",
    )

    # -------------------------------------------------------------------------
    # Four-way comparison
    # -------------------------------------------------------------------------

    comparison = pd.concat(
        [
            compact_result(
                raw_result,
                "RAW",
            ),

            compact_result(
                v1_result,
                "V1_TEXT_ONLY",
            ),

            compact_result(
                v2_result,
                "V2_LOCALIZE_ONLY",
            ),

            compact_result(
                clean_result,
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
        + "=" * 120
    )
    print(
        "P2-R0-05E2 — FOUR-WAY PREPROCESSING-SOURCE COMPARISON"
    )
    print(
        "=" * 120
    )

    print(
        comparison.to_string(
            index=False
        )
    )

    # -------------------------------------------------------------------------
    # Focused high-band table
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
        + "=" * 120
    )
    print(
        "P2-R0-05E2 — HIGH_25_36 SOURCE DIAGNOSTIC"
    )
    print(
        "=" * 120
    )

    print(
        high.to_string(
            index=False
        )
    )

    print(
        "\nP2-R0-05E2 PREPROCESSING-SOURCE "
        "ABLATION REPLAY: COMPLETE"
    )


if __name__ == "__main__":
    main()