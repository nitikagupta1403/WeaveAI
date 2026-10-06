from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd


# =============================================================================
# P2-R0-05H3 — INTRINSIC FOLD-3 STRUCTURAL AUDIT
#
# Purpose:
#   Investigate the conspicuous INTRINSIC fold-3 training MRR elevation seen
#   in 05H2 without changing the representation, folds, band definitions,
#   selection rule, or inference.
#
# Questions:
#   1) Is fold 3 structurally valid?
#   2) Are identity/category counts exactly balanced as frozen?
#   3) Is the fold-3 elevation present in both full and selected MRR?
#   4) Is it isolated to particular harmonic bands?
#   5) Does the same fold behave unusually for RAW/CROP_ONLY?
#
# This is diagnostic only. No tuning, reselection, or exclusion is permitted.
# =============================================================================


AUDIT_DIR = Path(__file__).resolve().parent

BASE_AUDIT = (
    AUDIT_DIR
    / "P2_R0_05_annotation_control_sensitivity.py"
)

H1_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05h_intrinsic_coordinate"
)

H1_FIELD_NPZ = (
    H1_ROOT
    / "P2_R0_05H1_intrinsic_coordinate_field.npz"
)

EXPECTED_H1_FIELD_SHA256 = (
    "aaa69c8a6a416979dc037ae6c0197d5c62f1959eb41cc0482c8b5a3bdde21c03"
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

EXPECTED_ROWS = 2300

OUTPUT_ROOT = H1_ROOT

SELECTION_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05H3_selection_all_representations.csv"
)

FOLD_COMPOSITION_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05H3_fold_composition.csv"
)

IDENTITY_ASSIGNMENTS_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05H3_identity_assignments.csv"
)

FOLD_ANOMALY_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05H3_fold_anomaly_summary.csv"
)

REPORT_JSON = (
    OUTPUT_ROOT
    / "P2_R0_05H3_report.json"
)


# =============================================================================
# Helpers
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
        "replay_cell13_selection",
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
        "P2-R0-05H3 VERIFIED DEFINITIONS: PASS"
    )

    return namespace


def validate_intrinsic(
    runtime: dict,
    normalize_runtime_relative_path,
):

    if not H1_FIELD_NPZ.is_file():
        raise RuntimeError(
            "05H1 intrinsic NPZ missing"
        )

    if sha256_file(
        H1_FIELD_NPZ
    ) != EXPECTED_H1_FIELD_SHA256:
        raise RuntimeError(
            "05H1 intrinsic NPZ SHA mismatch"
        )

    artifact = np.load(
        H1_FIELD_NPZ,
        allow_pickle=False,
    )

    field = np.asarray(
        artifact[
            "conditional_angular"
        ],
        dtype=np.float64,
    )

    radial_centers = np.asarray(
        artifact[
            "radial_centers"
        ],
        dtype=np.float64,
    )

    paths = np.asarray(
        artifact[
            "relative_paths"
        ],
        dtype=str,
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

    if field.shape != (
        EXPECTED_ROWS,
        72,
        72,
    ):
        raise RuntimeError(
            f"Unexpected intrinsic field shape: {field.shape}"
        )

    if not np.array_equal(
        paths,
        runtime_paths,
    ):
        raise RuntimeError(
            "Intrinsic/runtime population-order mismatch"
        )

    fft = np.fft.rfft(
        field,
        axis=2,
    )

    print(
        "P2-R0-05H3 INTRINSIC ARTIFACT: PASS"
    )

    return (
        field,
        fft,
        radial_centers,
    )


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
            "CROP_ONLY population-order mismatch"
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
        "P2-R0-05H3 CROP_ONLY RECONSTRUCTION: PASS"
    )

    print(
        "Max mass error:",
        mass_error,
    )

    print(
        "Max normalization error:",
        norm_error,
    )

    return np.fft.rfft(
        conditional,
        axis=2,
    )


def median_abs_deviation(values: np.ndarray) -> float:

    values = np.asarray(
        values,
        dtype=float,
    )

    med = np.median(
        values
    )

    return float(
        np.median(
            np.abs(
                values
                - med
            )
        )
    )


def robust_fold_score(
    value: float,
    peer_values: np.ndarray,
):

    peer_values = np.asarray(
        peer_values,
        dtype=float,
    )

    med = float(
        np.median(
            peer_values
        )
    )

    mad = median_abs_deviation(
        peer_values
    )

    if mad == 0:
        return (
            med,
            mad,
            np.nan,
        )

    # Standard robust z conversion.
    rz = (
        0.67448975
        * (
            value
            - med
        )
        / mad
    )

    return (
        med,
        mad,
        float(rz),
    )


def attach_dataset(
    selection: pd.DataFrame,
    dataset: str,
) -> pd.DataFrame:

    out = selection.copy()

    out.insert(
        0,
        "dataset",
        dataset,
    )

    return out


def extract_fold_indices(
    fold_obj,
):

    """
    Tolerant extractor for the frozen fold package.
    Supports the common dict/object layouts used by the Paper-II audit.
    """

    if isinstance(
        fold_obj,
        dict,
    ):
        train_keys = [
            "train_idx",
            "train_indices",
            "train_rows",
            "train_index",
        ]

        test_keys = [
            "test_idx",
            "test_indices",
            "test_rows",
            "test_index",
        ]

        train = None
        test = None

        for key in train_keys:
            if key in fold_obj:
                train = fold_obj[key]
                break

        for key in test_keys:
            if key in fold_obj:
                test = fold_obj[key]
                break

        if (
            train is not None
            and
            test is not None
        ):
            return (
                np.asarray(
                    train,
                    dtype=int,
                ),
                np.asarray(
                    test,
                    dtype=int,
                ),
            )

    for train_name in [
        "train_idx",
        "train_indices",
        "train_rows",
        "train_index",
    ]:
        if hasattr(
            fold_obj,
            train_name,
        ):
            train = getattr(
                fold_obj,
                train_name,
            )
            break
    else:
        train = None

    for test_name in [
        "test_idx",
        "test_indices",
        "test_rows",
        "test_index",
    ]:
        if hasattr(
            fold_obj,
            test_name,
        ):
            test = getattr(
                fold_obj,
                test_name,
            )
            break
    else:
        test = None

    if (
        train is not None
        and
        test is not None
    ):
        return (
            np.asarray(
                train,
                dtype=int,
            ),
            np.asarray(
                test,
                dtype=int,
            ),
        )

    # Final attempt: two-element tuple/list.
    if (
        isinstance(
            fold_obj,
            (tuple, list),
        )
        and
        len(
            fold_obj
        )
        == 2
    ):
        return (
            np.asarray(
                fold_obj[0],
                dtype=int,
            ),
            np.asarray(
                fold_obj[1],
                dtype=int,
            ),
        )

    raise RuntimeError(
        f"Could not extract train/test indices "
        f"from fold object type {type(fold_obj)}"
    )


# =============================================================================
# Main
# =============================================================================

def main():

    OUTPUT_ROOT.mkdir(
        parents=True,
        exist_ok=True,
    )

    for path in (
        SELECTION_CSV,
        FOLD_COMPOSITION_CSV,
        IDENTITY_ASSIGNMENTS_CSV,
        FOLD_ANOMALY_CSV,
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

    raw_fft = np.fft.rfft(
        raw_conditional,
        axis=2,
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

    (
        _intrinsic_field,
        intrinsic_fft,
        intrinsic_radial_centers,
    ) = validate_intrinsic(
        runtime,
        base[
            "normalize_runtime_relative_path"
        ],
    )

    crop_fft = reconstruct_crop(
        runtime,
        ra14_module,
        base[
            "normalize_runtime_relative_path"
        ],
    )

    raw_radial_centers = np.asarray(
        runtime[
            "radial_centers"
        ],
        dtype=np.float64,
    )

    replay = (
        base[
            "replay_cell13_selection"
        ]
    )

    raw_selection, _ = replay(
        raw_fft,
        raw_radial_centers,
        G,
        C,
        folds,
        "RAW_H3",
    )

    crop_selection, _ = replay(
        crop_fft,
        raw_radial_centers,
        G,
        C,
        folds,
        "CROP_H3",
    )

    intrinsic_selection, _ = replay(
        intrinsic_fft,
        intrinsic_radial_centers,
        G,
        C,
        folds,
        "INTRINSIC_H3",
    )

    all_selection = pd.concat(
        [
            attach_dataset(
                raw_selection,
                "RAW",
            ),
            attach_dataset(
                crop_selection,
                "V3_CROP_ONLY",
            ),
            attach_dataset(
                intrinsic_selection,
                "INTRINSIC",
            ),
        ],
        ignore_index=True,
    )

    all_selection.to_csv(
        SELECTION_CSV,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Frozen fold composition audit
    # -------------------------------------------------------------------------

    G_arr = np.asarray(
        G
    ).astype(str)

    C_arr = np.asarray(
        C
    ).astype(str)

    fold_rows = []
    identity_rows = []

    # The verified fold package returns a per-row fold-assignment vector,
    # not a list of train/test fold objects.  Each row carries the held-out
    # fold ID (0..4).  Therefore, for fold k:
    #   test  = rows with fold_assignment == k
    #   train = all remaining rows.
    fold_assignments = np.asarray(
        folds,
        dtype=int,
    )

    if fold_assignments.shape != (
        EXPECTED_ROWS,
    ):
        raise RuntimeError(
            "Unexpected fold-assignment shape: "
            f"{fold_assignments.shape}"
        )

    unique_folds = np.unique(
        fold_assignments
    )

    if not np.array_equal(
        unique_folds,
        np.arange(
            5,
            dtype=int,
        ),
    ):
        raise RuntimeError(
            "Unexpected frozen fold IDs: "
            f"{unique_folds}"
        )

    for fold_id in unique_folds:

        test_idx = np.flatnonzero(
            fold_assignments
            == fold_id
        )

        train_idx = np.flatnonzero(
            fold_assignments
            != fold_id
        )

        overlap = np.intersect1d(
            np.unique(
                G_arr[
                    train_idx
                ]
            ),
            np.unique(
                G_arr[
                    test_idx
                ]
            ),
        )

        for split_name, idx in [
            (
                "train",
                train_idx,
            ),
            (
                "test",
                test_idx,
            ),
        ]:

            split_G = G_arr[
                idx
            ]

            split_C = C_arr[
                idx
            ]

            for category in np.unique(
                C_arr
            ):

                local = (
                    split_C
                    == category
                )

                ids = np.unique(
                    split_G[
                        local
                    ]
                )

                fold_rows.append(
                    {
                        "fold":
                            fold_id,

                        "split":
                            split_name,

                        "category":
                            category,

                        "rows":
                            int(
                                np.sum(
                                    local
                                )
                            ),

                        "identities":
                            int(
                                len(
                                    ids
                                )
                            ),

                        "identity_overlap_total_fold":
                            int(
                                len(
                                    overlap
                                )
                            ),
                    }
                )

                for garment_id in ids:
                    identity_rows.append(
                        {
                            "fold":
                                fold_id,

                            "split":
                                split_name,

                            "category":
                                category,

                            "garment_identity":
                                garment_id,
                        }
                    )

    fold_composition = pd.DataFrame(
        fold_rows
    )

    identity_assignments = pd.DataFrame(
        identity_rows
    )

    fold_composition.to_csv(
        FOLD_COMPOSITION_CSV,
        index=False,
    )

    identity_assignments.to_csv(
        IDENTITY_ASSIGNMENTS_CSV,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Fold-3 anomaly audit
    # -------------------------------------------------------------------------

    anomaly_rows = []

    required_mrr_columns = [
        "train_full_mrr",
        "train_selected_mrr",
        "train_mrr_retention",
        "train_reconstruction_energy_fraction",
    ]

    for col in required_mrr_columns:
        if col not in all_selection.columns:
            raise RuntimeError(
                f"Selection table missing required column: {col}"
            )

    for (
        dataset,
        band,
    ), group in all_selection.groupby(
        [
            "dataset",
            "harmonic_band",
        ],
        sort=True,
    ):

        group = group.sort_values(
            "fold"
        ).reset_index(
            drop=True
        )

        if not np.array_equal(
            group[
                "fold"
            ].to_numpy(
                dtype=int
            ),
            np.arange(
                5,
                dtype=int,
            ),
        ):
            raise RuntimeError(
                f"Unexpected folds for {dataset}/{band}"
            )

        fold3 = group[
            group[
                "fold"
            ]
            == 3
        ].iloc[0]

        peers = group[
            group[
                "fold"
            ]
            != 3
        ]

        row = {
            "dataset":
                dataset,

            "harmonic_band":
                band,

            "fold3_selected_representation":
                fold3[
                    "selected_representation"
                ],

            "fold3_selected_radial_budget":
                int(
                    fold3[
                        "selected_radial_budget"
                    ]
                ),
        }

        for metric in required_mrr_columns:

            fold3_value = float(
                fold3[
                    metric
                ]
            )

            peer_values = peers[
                metric
            ].to_numpy(
                dtype=float
            )

            (
                peer_median,
                peer_mad,
                robust_z,
            ) = robust_fold_score(
                fold3_value,
                peer_values,
            )

            row[
                f"{metric}_fold3"
            ] = fold3_value

            row[
                f"{metric}_peer_median"
            ] = peer_median

            row[
                f"{metric}_peer_mad"
            ] = peer_mad

            row[
                f"{metric}_fold3_minus_peer_median"
            ] = (
                fold3_value
                - peer_median
            )

            row[
                f"{metric}_fold3_over_peer_median"
            ] = (
                fold3_value
                / peer_median
                if peer_median != 0
                else np.nan
            )

            row[
                f"{metric}_fold3_robust_z"
            ] = robust_z

        anomaly_rows.append(
            row
        )

    anomaly = pd.DataFrame(
        anomaly_rows
    )

    anomaly.to_csv(
        FOLD_ANOMALY_CSV,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Print compact diagnostic
    # -------------------------------------------------------------------------

    compact_cols = [
        "dataset",
        "harmonic_band",
        "train_full_mrr_fold3",
        "train_full_mrr_peer_median",
        "train_full_mrr_fold3_minus_peer_median",
        "train_full_mrr_fold3_over_peer_median",
        "train_full_mrr_fold3_robust_z",
        "train_selected_mrr_fold3",
        "train_selected_mrr_peer_median",
        "train_selected_mrr_fold3_minus_peer_median",
        "train_selected_mrr_fold3_over_peer_median",
        "train_selected_mrr_fold3_robust_z",
    ]

    print(
        "\n"
        + "=" * 150
    )

    print(
        "P2-R0-05H3 — FOLD-3 MRR ANOMALY SUMMARY"
    )

    print(
        "=" * 150
    )

    print(
        anomaly[
            compact_cols
        ].to_string(
            index=False
        )
    )

    # -------------------------------------------------------------------------
    # Structural validity summary
    # -------------------------------------------------------------------------

    overlap_max = int(
        fold_composition[
            "identity_overlap_total_fold"
        ].max()
    )

    train_ids_per_category = (
        fold_composition[
            fold_composition[
                "split"
            ]
            == "train"
        ][
            "identities"
        ]
    )

    test_ids_per_category = (
        fold_composition[
            fold_composition[
                "split"
            ]
            == "test"
        ][
            "identities"
        ]
    )

    print(
        "\nP2-R0-05H3 — STRUCTURAL FOLD CHECK"
    )

    print(
        "Max identity overlap:",
        overlap_max,
    )

    print(
        "Train identities/category range:",
        (
            int(
                train_ids_per_category.min()
            ),
            int(
                train_ids_per_category.max()
            ),
        ),
    )

    print(
        "Test identities/category range:",
        (
            int(
                test_ids_per_category.min()
            ),
            int(
                test_ids_per_category.max()
            ),
        ),
    )

    # -------------------------------------------------------------------------
    # Output hashes / report
    # -------------------------------------------------------------------------

    selection_sha = sha256_file(
        SELECTION_CSV
    )

    composition_sha = sha256_file(
        FOLD_COMPOSITION_CSV
    )

    assignments_sha = sha256_file(
        IDENTITY_ASSIGNMENTS_CSV
    )

    anomaly_sha = sha256_file(
        FOLD_ANOMALY_CSV
    )

    report = {
        "stage":
            "P2_R0_05H3_INTRINSIC_FOLD3_STRUCTURAL_AUDIT",

        "status":
            "COMPLETE",

        "rows":
            EXPECTED_ROWS,

        "fold_package_sha256":
            fold_sha,

        "h1_field_sha256":
            EXPECTED_H1_FIELD_SHA256,

        "selection_csv_sha256":
            selection_sha,

        "fold_composition_csv_sha256":
            composition_sha,

        "identity_assignments_csv_sha256":
            assignments_sha,

        "fold_anomaly_csv_sha256":
            anomaly_sha,

        "max_identity_overlap":
            overlap_max,

        "train_identities_per_category_min":
            int(
                train_ids_per_category.min()
            ),

        "train_identities_per_category_max":
            int(
                train_ids_per_category.max()
            ),

        "test_identities_per_category_min":
            int(
                test_ids_per_category.min()
            ),

        "test_identities_per_category_max":
            int(
                test_ids_per_category.max()
            ),

        "interpretation_boundary":
            (
                "This audit only characterizes fold-3 structure and "
                "fold-level training-MRR behavior. It does not justify "
                "excluding fold 3, changing folds, tuning the intrinsic "
                "representation, or changing the inferential result."
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
        "\nP2-R0-05H3 INTRINSIC FOLD-3 "
        "STRUCTURAL AUDIT: COMPLETE"
    )

    print(
        "Selection CSV:",
        SELECTION_CSV,
    )

    print(
        "Fold composition CSV:",
        FOLD_COMPOSITION_CSV,
    )

    print(
        "Identity assignments CSV:",
        IDENTITY_ASSIGNMENTS_CSV,
    )

    print(
        "Fold anomaly CSV:",
        FOLD_ANOMALY_CSV,
    )

    print(
        "Report:",
        REPORT_JSON,
    )

    print(
        "\nSTOP — fold-3 diagnostic complete. "
        "No fold exclusion or tuning performed."
    )


if __name__ == "__main__":
    main()