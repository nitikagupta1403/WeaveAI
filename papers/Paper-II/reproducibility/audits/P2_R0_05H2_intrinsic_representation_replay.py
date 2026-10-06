from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd


# =============================================================================
# P2-R0-05H2 — INTRINSIC REPRESENTATION REPLAY
#
# Compare:
#   RAW               = original Paper-II frame-dependent geometry
#   V3_CROP_ONLY      = same old geometry after tight crop
#   INTRINSIC         = 05H1 object-centric centroid/max-radius geometry
#
# Purpose:
#   Test whether the new crop-invariant intrinsic field retains useful
#   band-wise retrieval/statistical evidence under the frozen Paper-II
#   Cell-13 / Cell-13B replay machinery.
#
# IMPORTANT:
#   - No historical artifact is modified.
#   - No band definitions are changed.
#   - No radial-budget grid is changed.
#   - No model selection rule is changed.
#   - The intrinsic representation is evaluated as frozen by 05H1.
# =============================================================================


AUDIT_DIR = Path(__file__).resolve().parent

BASE_AUDIT = (
    AUDIT_DIR
    / "P2_R0_05_annotation_control_sensitivity.py"
)


# -----------------------------------------------------------------------------
# 05H1 frozen intrinsic artifact
# -----------------------------------------------------------------------------

H1_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05h_intrinsic_coordinate"
)

H1_FIELD_NPZ = (
    H1_ROOT
    / "P2_R0_05H1_intrinsic_coordinate_field.npz"
)

H1_METRICS_CSV = (
    H1_ROOT
    / "P2_R0_05H1_intrinsic_metrics.csv"
)

H1_REPORT_JSON = (
    H1_ROOT
    / "P2_R0_05H1_report.json"
)

EXPECTED_H1_FIELD_SHA256 = (
    "aaa69c8a6a416979dc037ae6c0197d5c62f1959eb41cc0482c8b5a3bdde21c03"
)

EXPECTED_H1_METRICS_SHA256 = (
    "56741cec4d209a2200a177079207f457900d303d8dc7bf66c81757f4e78dc64b"
)


# -----------------------------------------------------------------------------
# Frozen CROP_ONLY artifact
# -----------------------------------------------------------------------------

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


# -----------------------------------------------------------------------------
# Output
# -----------------------------------------------------------------------------

OUTPUT_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05h_intrinsic_coordinate"
)

COMPARISON_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05H2_raw_crop_intrinsic_comparison.csv"
)

REPORT_JSON = (
    OUTPUT_ROOT
    / "P2_R0_05H2_report.json"
)

EXPECTED_ROWS = 2300


# =============================================================================
# Helpers
# =============================================================================

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


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
        "load_paper2_runtime",
        "validate_geometry_equivalence",
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
            f"Verified D4 definitions missing: {missing}"
        )

    print(
        "P2-R0-05H2 VERIFIED D4 DEFINITIONS: PASS"
    )

    return namespace


def validate_h1_artifact(runtime: dict, normalize_runtime_relative_path):

    if not H1_FIELD_NPZ.is_file():
        raise RuntimeError(
            f"05H1 field missing: {H1_FIELD_NPZ}"
        )

    if not H1_METRICS_CSV.is_file():
        raise RuntimeError(
            f"05H1 metrics missing: {H1_METRICS_CSV}"
        )

    if not H1_REPORT_JSON.is_file():
        raise RuntimeError(
            f"05H1 report missing: {H1_REPORT_JSON}"
        )

    field_sha = sha256_file(
        H1_FIELD_NPZ
    )

    metrics_sha = sha256_file(
        H1_METRICS_CSV
    )

    if field_sha != EXPECTED_H1_FIELD_SHA256:
        raise RuntimeError(
            "05H1 field SHA mismatch"
        )

    if metrics_sha != EXPECTED_H1_METRICS_SHA256:
        raise RuntimeError(
            "05H1 metrics SHA mismatch"
        )

    report = json.loads(
        H1_REPORT_JSON.read_text(
            encoding="utf-8"
        )
    )

    if report.get("status") != "PASS":
        raise RuntimeError(
            "05H1 report status is not PASS"
        )

    if report.get(
        "field_npz_sha256"
    ) != EXPECTED_H1_FIELD_SHA256:
        raise RuntimeError(
            "05H1 report field SHA mismatch"
        )

    if report.get(
        "metrics_csv_sha256"
    ) != EXPECTED_H1_METRICS_SHA256:
        raise RuntimeError(
            "05H1 report metrics SHA mismatch"
        )

    artifact = np.load(
        H1_FIELD_NPZ,
        allow_pickle=False,
    )

    required_keys = {
        "conditional_angular",
        "nonempty_shells",
        "radial_centers",
        "relative_paths",
        "categories",
        "representation_name",
    }

    if not required_keys.issubset(
        set(artifact.files)
    ):
        raise RuntimeError(
            "05H1 NPZ missing required arrays"
        )

    intrinsic = np.asarray(
        artifact[
            "conditional_angular"
        ],
        dtype=np.float64,
    )

    nonempty = np.asarray(
        artifact[
            "nonempty_shells"
        ],
        dtype=bool,
    )

    radial_centers = np.asarray(
        artifact[
            "radial_centers"
        ],
        dtype=np.float64,
    )

    relative_paths = np.asarray(
        artifact[
            "relative_paths"
        ],
        dtype=str,
    )

    categories = np.asarray(
        artifact[
            "categories"
        ],
        dtype=str,
    )

    representation_name = str(
        np.asarray(
            artifact[
                "representation_name"
            ]
        ).ravel()[0]
    )

    if intrinsic.shape != (
        EXPECTED_ROWS,
        72,
        72,
    ):
        raise RuntimeError(
            f"Unexpected intrinsic field shape: {intrinsic.shape}"
        )

    if nonempty.shape != (
        EXPECTED_ROWS,
        72,
    ):
        raise RuntimeError(
            f"Unexpected nonempty shape: {nonempty.shape}"
        )

    if radial_centers.shape != (
        72,
    ):
        raise RuntimeError(
            f"Unexpected radial_centers shape: {radial_centers.shape}"
        )

    runtime_paths = np.asarray(
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

    runtime_categories = np.asarray(
        runtime[
            "image_categories"
        ],
        dtype=str,
    )

    if not np.array_equal(
        relative_paths,
        runtime_paths,
    ):
        raise RuntimeError(
            "05H1 relative_paths do not match runtime order"
        )

    if not np.array_equal(
        categories,
        runtime_categories,
    ):
        raise RuntimeError(
            "05H1 categories do not match runtime order"
        )

    if not np.isfinite(
        intrinsic
    ).all():
        raise RuntimeError(
            "Intrinsic field contains NaN/Inf"
        )

    shell_sums = intrinsic.sum(
        axis=2
    )

    nonempty_sums = shell_sums[
        nonempty
    ]

    max_norm_error = float(
        np.max(
            np.abs(
                nonempty_sums
                - 1.0
            )
        )
    )

    if max_norm_error > 1e-12:
        raise RuntimeError(
            "Intrinsic conditional normalization invalid"
        )

    intrinsic_fft = np.fft.rfft(
        intrinsic,
        axis=2,
    )

    if intrinsic_fft.shape != (
        EXPECTED_ROWS,
        72,
        37,
    ):
        raise RuntimeError(
            f"Unexpected intrinsic FFT shape: "
            f"{intrinsic_fft.shape}"
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
            "Intrinsic Nyquist imaginary component invalid"
        )

    print(
        "\nP2-R0-05H2 05H1 INTRINSIC ARTIFACT: PASS"
    )

    print(
        "Representation:",
        representation_name,
    )

    print(
        "Field SHA-256:",
        field_sha,
    )

    print(
        "Field shape:",
        intrinsic.shape,
    )

    print(
        "rFFT shape:",
        intrinsic_fft.shape,
    )

    print(
        "Max conditional normalization error:",
        max_norm_error,
    )

    print(
        "Max |Im(k=36)|:",
        nyquist_imag,
    )

    return (
        intrinsic,
        intrinsic_fft,
        radial_centers,
        representation_name,
    )


def reconstruct_crop_only(
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

    if len(manifest) != EXPECTED_ROWS:
        raise RuntimeError(
            "CROP_ONLY row count mismatch"
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
    ].astype(
        str
    ).to_numpy()

    if not np.array_equal(
        runtime_paths,
        manifest_paths,
    ):
        raise RuntimeError(
            "CROP_ONLY population/order mismatch"
        )

    categories = np.asarray(
        runtime[
            "image_categories"
        ],
        dtype=str,
    )

    rows = []

    for i, record in manifest.iterrows():

        path = (
            CROP_ONLY_ROOT
            / str(
                record[
                    "output_relative_path"
                ]
            )
        )

        if not path.is_file():
            raise RuntimeError(
                f"Missing CROP_ONLY image: {path}"
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
                        categories[
                            i
                        ]
                    ),

                "path":
                    path,
            }
        )

    print(
        "\nP2-R0-05H2 — reconstructing "
        "V3_CROP_ONLY geometry..."
    )

    (
        conditional,
        nonempty,
        radial_centers,
        mass_error,
        norm_error,
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
            "Unexpected CROP_ONLY field shape"
        )

    fft = np.fft.rfft(
        conditional,
        axis=2,
    )

    if fft.shape != (
        EXPECTED_ROWS,
        72,
        37,
    ):
        raise RuntimeError(
            "Unexpected CROP_ONLY FFT shape"
        )

    print(
        "V3_CROP_ONLY reconstruction: PASS"
    )

    print(
        "Max mass error:",
        mass_error,
    )

    print(
        "Max normalization error:",
        norm_error,
    )

    return (
        conditional,
        fft,
    )


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

    OUTPUT_ROOT.mkdir(
        parents=True,
        exist_ok=True,
    )

    if COMPARISON_CSV.exists():
        raise RuntimeError(
            "Refusing to overwrite existing comparison: "
            f"{COMPARISON_CSV}"
        )

    if REPORT_JSON.exists():
        raise RuntimeError(
            "Refusing to overwrite existing report: "
            f"{REPORT_JSON}"
        )

    base = (
        load_verified_d4_definitions()
    )

    runtime = (
        base[
            "load_paper2_runtime"
        ]()
    )

    # -------------------------------------------------------------------------
    # RAW exact geometry
    # -------------------------------------------------------------------------

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

    raw_fft = np.fft.rfft(
        raw_conditional,
        axis=2,
    )

    # -------------------------------------------------------------------------
    # Frozen identity folds
    # -------------------------------------------------------------------------

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

    # -------------------------------------------------------------------------
    # CROP_ONLY old frame-dependent geometry
    # -------------------------------------------------------------------------

    (
        crop_conditional,
        crop_fft,
    ) = reconstruct_crop_only(
        runtime,
        ra14_module,
        base[
            "normalize_runtime_relative_path"
        ],
    )

    # -------------------------------------------------------------------------
    # New intrinsic geometry
    # -------------------------------------------------------------------------

    (
        intrinsic_conditional,
        intrinsic_fft,
        intrinsic_radial_centers,
        intrinsic_name,
    ) = validate_h1_artifact(
        runtime,
        base[
            "normalize_runtime_relative_path"
        ],
    )

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

    raw_radial_centers = np.asarray(
        runtime[
            "radial_centers"
        ],
        dtype=np.float64,
    )

    # -------------------------------------------------------------------------
    # Frozen replay
    # -------------------------------------------------------------------------

    raw = run_replay(
        "RAW",
        raw_fft,
        raw_radial_centers,
        G,
        C,
        folds,
        replay_selection,
        replay_inference,
    )

    crop = run_replay(
        "V3_CROP_ONLY",
        crop_fft,
        raw_radial_centers,
        G,
        C,
        folds,
        replay_selection,
        replay_inference,
    )

    intrinsic = run_replay(
        "INTRINSIC",
        intrinsic_fft,
        intrinsic_radial_centers,
        G,
        C,
        folds,
        replay_selection,
        replay_inference,
    )

    # -------------------------------------------------------------------------
    # Compact 3-way comparison
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
                crop[
                    "result"
                ],
                "V3_CROP_ONLY",
            ),

            compact_result(
                intrinsic[
                    "result"
                ],
                "INTRINSIC",
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
        "V3_CROP_ONLY",
        "INTRINSIC",
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

    comparison.to_csv(
        COMPARISON_CSV,
        index=False,
    )

    comparison_sha = sha256_file(
        COMPARISON_CSV
    )

    print(
        "\n"
        + "=" * 132
    )

    print(
        "P2-R0-05H2 — RAW / CROP_ONLY / "
        "INTRINSIC COMPARISON"
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
    # High-band focused diagnostic
    # -------------------------------------------------------------------------

    high = comparison[
        comparison[
            "harmonic_band"
        ]
        == "high_25_36"
    ].copy()

    print(
        "\n"
        + "=" * 132
    )

    print(
        "P2-R0-05H2 — HIGH_25_36 "
        "INTRINSIC RESCUE DIAGNOSTIC"
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
    # Stability fact from 05H1
    # -------------------------------------------------------------------------

    intrinsic_crop_exact = bool(
        np.array_equal(
            intrinsic_conditional,
            intrinsic_conditional,
        )
    )

    # The exact RAW-box == CROP_ONLY intrinsic equivalence was frozen by 05H1.
    h1_report = json.loads(
        H1_REPORT_JSON.read_text(
            encoding="utf-8"
        )
    )

    h1_exact_field_diff = float(
        h1_report[
            "max_raw_box_vs_crop_intrinsic_field_abs_diff"
        ]
    )

    # -------------------------------------------------------------------------
    # Report
    # -------------------------------------------------------------------------

    report = {
        "stage":
            "P2_R0_05H2_INTRINSIC_REPRESENTATION_REPLAY",

        "status":
            "COMPLETE",

        "rows":
            EXPECTED_ROWS,

        "representation":
            intrinsic_name,

        "h1_field_sha256":
            EXPECTED_H1_FIELD_SHA256,

        "h1_metrics_sha256":
            EXPECTED_H1_METRICS_SHA256,

        "comparison_csv_sha256":
            comparison_sha,

        "fold_package_sha256":
            fold_sha,

        "h1_raw_box_vs_crop_intrinsic_field_max_abs_diff":
            h1_exact_field_diff,

        "crop_invariant_by_05H1":
            bool(
                h1_exact_field_diff
                == 0.0
            ),

        "interpretation_boundary":
            (
                "05H2 evaluates the already-frozen intrinsic field "
                "with the frozen Paper-II selection/inference machinery. "
                "The intrinsic representation is new and must not be "
                "described as the historical Paper-II representation."
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
        "\nP2-R0-05H2 INTRINSIC "
        "REPRESENTATION REPLAY: COMPLETE"
    )

    print(
        "05H1 crop-invariant field diff:",
        h1_exact_field_diff,
    )

    print(
        "Comparison CSV:",
        COMPARISON_CSV,
    )

    print(
        "Comparison CSV SHA-256:",
        comparison_sha,
    )

    print(
        "Report:",
        REPORT_JSON,
    )

    print(
        "\nSTOP — frozen replay complete; "
        "no representation tuning performed."
    )


if __name__ == "__main__":
    main()