from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd


# =============================================================================
# P2-R0-05H4B2 — EXACT TRAINING-QUERY / IDENTITY / CATEGORY DECOMPOSITION
#
# Purpose:
#   Explain the INTRINSIC fold-3 low/mid training-MRR elevation using the
#   exact frozen Cell-13 retrieval geometry.
#
# Source-traced facts frozen by 05H4B1:
#   - train/test split is defined by frozen fold labels.
#   - band coefficients are converted with complex_band_to_vector_exact().
#   - robust median/IQR geometry is fit on TRAIN FULL vectors only.
#   - both full and selected representations use that same fitted geometry.
#   - training MRR uses leave-one-out identity prototypes within category.
#
# This audit adds only one transparent diagnostic wrapper:
#   prototype_retrieval_query_table_exact()
#
# It is line-for-line equivalent in ranking logic to
# prototype_retrieval_subset_exact(), but returns one row per training query
# so that the already-computed aggregate MRR can be decomposed by category
# and garment identity.
#
# Hard validation gate:
#   Mean reciprocal rank reconstructed from the per-query table MUST equal
#   the frozen replay Cell-13 train_full_mrr / train_selected_mrr for every
#   dataset x fold x band.
#
# No tuning. No new selection. No fold exclusion. No inferential claim.
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

OUTPUT_ROOT = (
    H1_ROOT
    / "P2_R0_05H4B2_training_decomposition"
)

QUERY_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05H4B2_training_query_table.csv"
)

IDENTITY_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05H4B2_training_identity_summary.csv"
)

CATEGORY_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05H4B2_training_category_summary.csv"
)

FOLD3_CATEGORY_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05H4B2_fold3_category_contrast.csv"
)

FOLD3_IDENTITY_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05H4B2_fold3_identity_detail.csv"
)

VALIDATION_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05H4B2_exact_mrr_validation.csv"
)

REPORT_JSON = (
    OUTPUT_ROOT
    / "P2_R0_05H4B2_report.json"
)

TARGET_BANDS = [
    "low_1_4",
    "mid_5_12",
    "highmid_13_24",
    "high_25_36",
]

FOCUS_BANDS = [
    "low_1_4",
    "mid_5_12",
]

TOL = 1e-12


# =============================================================================
# General helpers
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
        "__file__":
            str(
                BASE_AUDIT
            ),

        "__name__":
            "p2_r0_05_verified_definitions",
    }

    exec(
        compile(
            source.split(
                marker,
                1,
            )[0],
            str(
                BASE_AUDIT
            ),
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
        "complex_band_to_vector_exact",
        "fit_robust_geometry_exact",
        "apply_robust_geometry_exact",
        "raw_radial_reconstruct_exact",
        "dct_radial_reconstruct_exact",
        "wavelet_radial_reconstruct_exact",
        "HARMONIC_BANDS",
    ]

    missing = [
        name
        for name in required
        if name not in namespace
    ]

    if missing:
        raise RuntimeError(
            "Missing frozen definitions: "
            f"{missing}"
        )

    print(
        "P2-R0-05H4B2 VERIFIED DEFINITIONS: PASS"
    )

    return namespace


# =============================================================================
# Dataset reconstruction
# =============================================================================

def validate_intrinsic(
    runtime: dict,
    normalize_runtime_relative_path,
):

    if not H1_FIELD_NPZ.is_file():
        raise RuntimeError(
            "05H1 intrinsic field missing"
        )

    if sha256_file(
        H1_FIELD_NPZ
    ) != EXPECTED_H1_FIELD_SHA256:
        raise RuntimeError(
            "05H1 intrinsic field SHA mismatch"
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

    relative_paths = np.asarray(
        artifact[
            "relative_paths"
        ],
        dtype=str,
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

    if field.shape != (
        EXPECTED_ROWS,
        72,
        72,
    ):
        raise RuntimeError(
            f"Unexpected intrinsic shape: {field.shape}"
        )

    if not np.array_equal(
        relative_paths,
        runtime_paths,
    ):
        raise RuntimeError(
            "INTRINSIC/runtime order mismatch"
        )

    return {
        "conditional":
            field,

        "fft":
            np.fft.rfft(
                field,
                axis=2,
            ),

        "radial_centers":
            radial_centers,
    }


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
            normalize_runtime_relative_path(
                x
            )
            for x in runtime[
                "image_paths"
            ]
        ],
        dtype=str,
    )

    if not np.array_equal(
        runtime_paths,
        manifest[
            "relative_path"
        ].astype(
            str
        ).to_numpy(),
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

        path = (
            CROP_ONLY_ROOT
            / str(
                rec[
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
                    path,
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
        "P2-R0-05H4B2 CROP_ONLY RECONSTRUCTION: PASS"
    )

    print(
        "Max mass error:",
        mass_error,
    )

    print(
        "Max normalization error:",
        norm_error,
    )

    return {
        "conditional":
            conditional,

        "fft":
            np.fft.rfft(
                conditional,
                axis=2,
            ),
    }


# =============================================================================
# Exact per-query retrieval wrapper
# =============================================================================

def prototype_retrieval_query_table_exact(
    X,
    G_subset,
    C_subset,
    row_indices,
    relative_paths,
):
    """
    Exact ranking logic from prototype_retrieval_subset_exact(), extended only
    to return the rank / reciprocal rank for each query row.
    """

    X = np.asarray(
        X,
        dtype=np.float64,
    )

    G_subset = np.asarray(
        G_subset,
        dtype=str,
    )

    C_subset = np.asarray(
        C_subset,
        dtype=str,
    )

    row_indices = np.asarray(
        row_indices,
        dtype=int,
    )

    relative_paths = np.asarray(
        relative_paths,
        dtype=str,
    )

    if not (
        len(
            X
        )
        ==
        len(
            G_subset
        )
        ==
        len(
            C_subset
        )
        ==
        len(
            row_indices
        )
        ==
        len(
            relative_paths
        )
    ):
        raise RuntimeError(
            "Per-query retrieval inputs are misaligned"
        )

    rows = []

    for category in np.unique(
        C_subset
    ):

        idx_c = np.flatnonzero(
            C_subset
            == category
        )

        Xc = X[
            idx_c
        ]

        Gc = G_subset[
            idx_c
        ]

        garments, labels = np.unique(
            Gc,
            return_inverse=True,
        )

        n_garments = len(
            garments
        )

        if n_garments < 2:
            raise RuntimeError(
                f"Category {category} has <2 identities"
            )

        garment_sum = np.zeros(
            (
                n_garments,
                X.shape[
                    1
                ],
            ),
            dtype=np.float64,
        )

        garment_count = np.zeros(
            n_garments,
            dtype=int,
        )

        for gg in range(
            n_garments
        ):

            members = (
                labels
                == gg
            )

            garment_sum[
                gg
            ] = np.sum(
                Xc[
                    members
                ],
                axis=0,
            )

            garment_count[
                gg
            ] = int(
                np.sum(
                    members
                )
            )

        if np.any(
            garment_count
            < 2
        ):
            raise RuntimeError(
                "Identity has fewer than 2 sketches"
            )

        ordinary_proto = (
            garment_sum
            / garment_count[
                :,
                None,
            ]
        )

        diff = (
            Xc[
                :,
                None,
                :,
            ]
            -
            ordinary_proto[
                None,
                :,
                :,
            ]
        )

        d2 = np.sum(
            diff
            ** 2,
            axis=-1,
        )

        own_sum = garment_sum[
            labels
        ]

        own_count = garment_count[
            labels
        ]

        loo_proto = (
            own_sum
            - Xc
        ) / (
            own_count[
                :,
                None,
            ]
            - 1
        )

        own_d2 = np.sum(
            (
                Xc
                - loo_proto
            )
            ** 2,
            axis=1,
        )

        d2[
            np.arange(
                len(
                    idx_c
                )
            ),
            labels,
        ] = own_d2

        order = np.argsort(
            d2,
            axis=1,
            kind="stable",
        )

        for local_i in range(
            len(
                idx_c
            )
        ):

            rank = int(
                np.flatnonzero(
                    order[
                        local_i
                    ]
                    == labels[
                        local_i
                    ]
                )[
                    0
                ]
                + 1
            )

            subset_i = int(
                idx_c[
                    local_i
                ]
            )

            rows.append(
                {
                    "subset_row_index":
                        subset_i,

                    "global_row_index":
                        int(
                            row_indices[
                                subset_i
                            ]
                        ),

                    "relative_path":
                        str(
                            relative_paths[
                                subset_i
                            ]
                        ),

                    "garment_identity":
                        str(
                            G_subset[
                                subset_i
                            ]
                        ),

                    "category":
                        str(
                            category
                        ),

                    "n_candidate_identities_in_category":
                        int(
                            n_garments
                        ),

                    "own_identity_sketch_count":
                        int(
                            own_count[
                                local_i
                            ]
                        ),

                    "own_distance_squared":
                        float(
                            own_d2[
                                local_i
                            ]
                        ),

                    "rank":
                        rank,

                    "reciprocal_rank":
                        float(
                            1.0
                            / rank
                        ),

                    "top1":
                        bool(
                            rank
                            == 1
                        ),
                }
            )

    table = pd.DataFrame(
        rows
    ).sort_values(
        "global_row_index"
    ).reset_index(
        drop=True
    )

    if len(
        table
    ) != len(
        X
    ):
        raise RuntimeError(
            "Per-query retrieval table lost rows"
        )

    return table


# =============================================================================
# Decomposition helpers
# =============================================================================

def selected_reconstruction(
    base,
    representation_name: str,
    X_train_full: np.ndarray,
    budget: int,
    radial_centers: np.ndarray,
):

    if (
        representation_name
        == "raw_interpolation"
    ):
        return base[
            "raw_radial_reconstruct_exact"
        ](
            X_train_full,
            budget,
            radial_centers,
        )

    if representation_name == "dct":
        return base[
            "dct_radial_reconstruct_exact"
        ](
            X_train_full,
            budget,
        )

    if representation_name == "wavelet":
        return base[
            "wavelet_radial_reconstruct_exact"
        ](
            X_train_full,
            budget,
        )

    raise RuntimeError(
        "Unknown selected representation: "
        f"{representation_name}"
    )


def identity_summary(
    query_table: pd.DataFrame,
) -> pd.DataFrame:

    return (
        query_table
        .groupby(
            [
                "dataset",
                "fold",
                "harmonic_band",
                "representation_state",
                "garment_identity",
                "category",
            ],
            as_index=False,
        )
        .agg(
            n_queries=(
                "reciprocal_rank",
                "size",
            ),

            mean_reciprocal_rank=(
                "reciprocal_rank",
                "mean",
            ),

            median_rank=(
                "rank",
                "median",
            ),

            top1_accuracy=(
                "top1",
                "mean",
            ),

            mean_own_distance_squared=(
                "own_distance_squared",
                "mean",
            ),
        )
    )


def category_summary(
    query_table: pd.DataFrame,
    identity_table: pd.DataFrame,
) -> pd.DataFrame:

    query_weighted = (
        query_table
        .groupby(
            [
                "dataset",
                "fold",
                "harmonic_band",
                "representation_state",
                "category",
            ],
            as_index=False,
        )
        .agg(
            n_queries=(
                "reciprocal_rank",
                "size",
            ),

            n_identities=(
                "garment_identity",
                "nunique",
            ),

            query_weighted_mrr=(
                "reciprocal_rank",
                "mean",
            ),

            query_weighted_top1=(
                "top1",
                "mean",
            ),
        )
    )

    identity_balanced = (
        identity_table
        .groupby(
            [
                "dataset",
                "fold",
                "harmonic_band",
                "representation_state",
                "category",
            ],
            as_index=False,
        )
        .agg(
            identity_balanced_mrr=(
                "mean_reciprocal_rank",
                "mean",
            ),

            identity_balanced_top1=(
                "top1_accuracy",
                "mean",
            ),
        )
    )

    return query_weighted.merge(
        identity_balanced,
        on=[
            "dataset",
            "fold",
            "harmonic_band",
            "representation_state",
            "category",
        ],
        how="inner",
        validate="one_to_one",
    )


def fold3_category_contrast(
    category_table: pd.DataFrame,
) -> pd.DataFrame:

    focus = category_table[
        (
            category_table[
                "dataset"
            ]
            == "INTRINSIC"
        )
        &
        (
            category_table[
                "harmonic_band"
            ].isin(
                FOCUS_BANDS
            )
        )
    ].copy()

    rows = []

    for (
        band,
        state,
        category,
    ), group in focus.groupby(
        [
            "harmonic_band",
            "representation_state",
            "category",
        ],
        sort=True,
    ):

        fold3 = group[
            group[
                "fold"
            ]
            == 3
        ]

        peers = group[
            group[
                "fold"
            ]
            != 3
        ]

        if len(
            fold3
        ) != 1:
            raise RuntimeError(
                "Expected exactly one fold-3 category row"
            )

        r3 = fold3.iloc[
            0
        ]

        rows.append(
            {
                "harmonic_band":
                    band,

                "representation_state":
                    state,

                "category":
                    category,

                "fold3_n_queries":
                    int(
                        r3[
                            "n_queries"
                        ]
                    ),

                "fold3_query_weighted_mrr":
                    float(
                        r3[
                            "query_weighted_mrr"
                        ]
                    ),

                "peer_median_query_weighted_mrr":
                    float(
                        peers[
                            "query_weighted_mrr"
                        ].median()
                    ),

                "fold3_minus_peer_query_weighted_mrr":
                    float(
                        r3[
                            "query_weighted_mrr"
                        ]
                        -
                        peers[
                            "query_weighted_mrr"
                        ].median()
                    ),

                "fold3_identity_balanced_mrr":
                    float(
                        r3[
                            "identity_balanced_mrr"
                        ]
                    ),

                "peer_median_identity_balanced_mrr":
                    float(
                        peers[
                            "identity_balanced_mrr"
                        ].median()
                    ),

                "fold3_minus_peer_identity_balanced_mrr":
                    float(
                        r3[
                            "identity_balanced_mrr"
                        ]
                        -
                        peers[
                            "identity_balanced_mrr"
                        ].median()
                    ),
            }
        )

    result = pd.DataFrame(
        rows
    )

    result[
        "abs_fold3_minus_peer_query_weighted_mrr"
    ] = np.abs(
        result[
            "fold3_minus_peer_query_weighted_mrr"
        ]
    )

    return result.sort_values(
        [
            "harmonic_band",
            "representation_state",
            "abs_fold3_minus_peer_query_weighted_mrr",
        ],
        ascending=[
            True,
            True,
            False,
        ],
    ).reset_index(
        drop=True
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
        QUERY_CSV,
        IDENTITY_CSV,
        CATEGORY_CSV,
        FOLD3_CATEGORY_CSV,
        FOLD3_IDENTITY_CSV,
        VALIDATION_CSV,
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

    raw_radial_centers = np.asarray(
        runtime[
            "radial_centers"
        ],
        dtype=np.float64,
    )

    datasets = {
        "RAW": {
            "fft":
                np.fft.rfft(
                    raw_conditional,
                    axis=2,
                ),

            "radial_centers":
                raw_radial_centers,
        }
    }

    crop = reconstruct_crop(
        runtime,
        ra14_module,
        base[
            "normalize_runtime_relative_path"
        ],
    )

    datasets[
        "V3_CROP_ONLY"
    ] = {
        "fft":
            crop[
                "fft"
            ],

        "radial_centers":
            raw_radial_centers,
    }

    intrinsic = validate_intrinsic(
        runtime,
        base[
            "normalize_runtime_relative_path"
        ],
    )

    datasets[
        "INTRINSIC"
    ] = intrinsic

    # -------------------------------------------------------------------------
    # Frozen Cell-13 selection replay for each representation.
    # -------------------------------------------------------------------------

    replay_tables = {}

    for dataset, data in datasets.items():

        (
            replay,
            _effect_tables,
        ) = base[
            "replay_cell13_selection"
        ](
            data[
                "fft"
            ],
            data[
                "radial_centers"
            ],
            G,
            C,
            folds,
            f"{dataset}_H4B2",
        )

        replay_tables[
            dataset
        ] = replay.copy()

    # -------------------------------------------------------------------------
    # Exact query-level reconstruction and validation.
    # -------------------------------------------------------------------------

    query_tables = []
    validation_rows = []

    harmonic_bands = base[
        "HARMONIC_BANDS"
    ]

    for dataset, data in datasets.items():

        F = np.asarray(
            data[
                "fft"
            ],
            dtype=np.complex128,
        )

        radial_centers = np.asarray(
            data[
                "radial_centers"
            ],
            dtype=np.float64,
        )

        F_nonDC = F[
            ...,
            1:37,
        ].copy()

        replay = replay_tables[
            dataset
        ]

        for fold in np.sort(
            np.unique(
                folds
            )
        ):

            train_idx = np.flatnonzero(
                folds
                != fold
            )

            G_train = G[
                train_idx
            ]

            C_train = C[
                train_idx
            ]

            paths_train = relative_paths[
                train_idx
            ]

            for band_name in TARGET_BANDS:

                k_values = np.asarray(
                    harmonic_bands[
                        band_name
                    ]
                )

                k_idx = (
                    k_values
                    - 1
                )

                X_band_all = np.transpose(
                    F_nonDC[
                        :,
                        :,
                        k_idx,
                    ],
                    (
                        0,
                        2,
                        1,
                    ),
                )

                X_train_full = X_band_all[
                    train_idx
                ]

                train_full_vector = base[
                    "complex_band_to_vector_exact"
                ](
                    X_train_full
                )

                (
                    train_median,
                    train_scale,
                    _small,
                ) = base[
                    "fit_robust_geometry_exact"
                ](
                    train_full_vector
                )

                train_full_scaled = base[
                    "apply_robust_geometry_exact"
                ](
                    train_full_vector,
                    train_median,
                    train_scale,
                )

                selection_row = replay[
                    (
                        replay[
                            "fold"
                        ]
                        == int(
                            fold
                        )
                    )
                    &
                    (
                        replay[
                            "harmonic_band"
                        ]
                        == band_name
                    )
                ]

                if len(
                    selection_row
                ) != 1:
                    raise RuntimeError(
                        "Expected exactly one frozen selection row"
                    )

                selection_row = selection_row.iloc[
                    0
                ]

                selected_representation = str(
                    selection_row[
                        "selected_representation"
                    ]
                )

                selected_budget = int(
                    selection_row[
                        "selected_radial_budget"
                    ]
                )

                X_train_selected = selected_reconstruction(
                    base,
                    selected_representation,
                    X_train_full,
                    selected_budget,
                    radial_centers,
                )

                train_selected_vector = base[
                    "complex_band_to_vector_exact"
                ](
                    X_train_selected
                )

                # IMPORTANT: same FULL-fit robust geometry, matching frozen code.
                train_selected_scaled = base[
                    "apply_robust_geometry_exact"
                ](
                    train_selected_vector,
                    train_median,
                    train_scale,
                )

                for state, scaled in [
                    (
                        "full",
                        train_full_scaled,
                    ),
                    (
                        "selected",
                        train_selected_scaled,
                    ),
                ]:

                    query_table = (
                        prototype_retrieval_query_table_exact(
                            scaled,
                            G_train,
                            C_train,
                            train_idx,
                            paths_train,
                        )
                    )

                    query_table.insert(
                        0,
                        "dataset",
                        dataset,
                    )

                    query_table.insert(
                        1,
                        "fold",
                        int(
                            fold
                        ),
                    )

                    query_table.insert(
                        2,
                        "harmonic_band",
                        band_name,
                    )

                    query_table.insert(
                        3,
                        "representation_state",
                        state,
                    )

                    query_table.insert(
                        4,
                        "selected_representation",
                        selected_representation,
                    )

                    query_table.insert(
                        5,
                        "selected_radial_budget",
                        selected_budget,
                    )

                    observed_mrr = float(
                        query_table[
                            "reciprocal_rank"
                        ].mean()
                    )

                    frozen_mrr = float(
                        selection_row[
                            "train_full_mrr"
                            if state
                            == "full"
                            else
                            "train_selected_mrr"
                        ]
                    )

                    abs_diff = abs(
                        observed_mrr
                        - frozen_mrr
                    )

                    validation_rows.append(
                        {
                            "dataset":
                                dataset,

                            "fold":
                                int(
                                    fold
                                ),

                            "harmonic_band":
                                band_name,

                            "representation_state":
                                state,

                            "reconstructed_query_mrr":
                                observed_mrr,

                            "frozen_replay_mrr":
                                frozen_mrr,

                            "absolute_difference":
                                abs_diff,

                            "exact_within_tolerance":
                                bool(
                                    abs_diff
                                    <= TOL
                                ),
                        }
                    )

                    if abs_diff > TOL:
                        raise RuntimeError(
                            "Per-query reconstruction failed exact MRR gate: "
                            f"{dataset}, fold={fold}, band={band_name}, "
                            f"state={state}, diff={abs_diff}"
                        )

                    query_tables.append(
                        query_table
                    )

    query_all = pd.concat(
        query_tables,
        ignore_index=True,
    )

    validation = pd.DataFrame(
        validation_rows
    )

    if not bool(
        validation[
            "exact_within_tolerance"
        ].all()
    ):
        raise RuntimeError(
            "At least one exact MRR gate failed"
        )

    query_all.to_csv(
        QUERY_CSV,
        index=False,
    )

    validation.to_csv(
        VALIDATION_CSV,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Identity / category decomposition.
    # -------------------------------------------------------------------------

    identities = identity_summary(
        query_all
    )

    identities.to_csv(
        IDENTITY_CSV,
        index=False,
    )

    categories = category_summary(
        query_all,
        identities,
    )

    categories.to_csv(
        CATEGORY_CSV,
        index=False,
    )

    fold3_categories = fold3_category_contrast(
        categories
    )

    fold3_categories.to_csv(
        FOLD3_CATEGORY_CSV,
        index=False,
    )

    fold3_identity = identities[
        (
            identities[
                "dataset"
            ]
            == "INTRINSIC"
        )
        &
        (
            identities[
                "fold"
            ]
            == 3
        )
        &
        (
            identities[
                "harmonic_band"
            ].isin(
                FOCUS_BANDS
            )
        )
    ].copy()

    fold3_identity = fold3_identity.sort_values(
        [
            "harmonic_band",
            "representation_state",
            "category",
            "mean_reciprocal_rank",
        ],
        ascending=[
            True,
            True,
            True,
            False,
        ],
    ).reset_index(
        drop=True
    )

    fold3_identity.to_csv(
        FOLD3_IDENTITY_CSV,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Console summaries: exactly the diagnostic we need.
    # -------------------------------------------------------------------------

    print(
        "\n"
        + "=" * 150
    )

    print(
        "P2-R0-05H4B2 — EXACT MRR RECONSTRUCTION GATE"
    )

    print(
        "=" * 150
    )

    print(
        "Rows validated:",
        len(
            validation
        ),
    )

    print(
        "Maximum absolute MRR difference:",
        float(
            validation[
                "absolute_difference"
            ].max()
        ),
    )

    print(
        "All exact within tolerance:",
        bool(
            validation[
                "exact_within_tolerance"
            ].all()
        ),
    )

    print(
        "\n"
        + "=" * 150
    )

    print(
        "P2-R0-05H4B2 — INTRINSIC FOLD-3 LOW/MID "
        "CATEGORY CONTRAST"
    )

    print(
        "=" * 150
    )

    focus_print = fold3_categories[
        fold3_categories[
            "representation_state"
        ]
        == "full"
    ][
        [
            "harmonic_band",
            "category",
            "fold3_n_queries",
            "fold3_query_weighted_mrr",
            "peer_median_query_weighted_mrr",
            "fold3_minus_peer_query_weighted_mrr",
            "fold3_identity_balanced_mrr",
            "peer_median_identity_balanced_mrr",
            "fold3_minus_peer_identity_balanced_mrr",
        ]
    ]

    print(
        focus_print.to_string(
            index=False
        )
    )

    print(
        "\n"
        + "=" * 150
    )

    print(
        "P2-R0-05H4B2 — TOP POSITIVE FOLD-3 CATEGORY "
        "CONTRIBUTORS (FULL INTRINSIC)"
    )

    print(
        "=" * 150
    )

    top_positive = (
        fold3_categories[
            fold3_categories[
                "representation_state"
            ]
            == "full"
        ]
        .sort_values(
            "fold3_minus_peer_query_weighted_mrr",
            ascending=False,
        )
        .groupby(
            "harmonic_band",
            group_keys=False,
        )
        .head(
            8
        )
    )

    print(
        top_positive[
            [
                "harmonic_band",
                "category",
                "fold3_query_weighted_mrr",
                "peer_median_query_weighted_mrr",
                "fold3_minus_peer_query_weighted_mrr",
            ]
        ].to_string(
            index=False
        )
    )

    # -------------------------------------------------------------------------
    # Save hashes / report.
    # -------------------------------------------------------------------------

    hashes = {
        "query_csv_sha256":
            sha256_file(
                QUERY_CSV
            ),

        "identity_csv_sha256":
            sha256_file(
                IDENTITY_CSV
            ),

        "category_csv_sha256":
            sha256_file(
                CATEGORY_CSV
            ),

        "fold3_category_csv_sha256":
            sha256_file(
                FOLD3_CATEGORY_CSV
            ),

        "fold3_identity_csv_sha256":
            sha256_file(
                FOLD3_IDENTITY_CSV
            ),

        "validation_csv_sha256":
            sha256_file(
                VALIDATION_CSV
            ),
    }

    report = {
        "stage":
            "P2_R0_05H4B2_EXACT_TRAINING_DECOMPOSITION",

        "status":
            "COMPLETE",

        "rows":
            EXPECTED_ROWS,

        "fold_package_sha256":
            fold_sha,

        "h1_field_sha256":
            EXPECTED_H1_FIELD_SHA256,

        "mrr_validation_rows":
            int(
                len(
                    validation
                )
            ),

        "mrr_validation_max_abs_difference":
            float(
                validation[
                    "absolute_difference"
                ].max()
            ),

        "mrr_validation_all_exact_within_tolerance":
            bool(
                validation[
                    "exact_within_tolerance"
                ].all()
            ),

        **hashes,

        "interpretation_boundary":
            (
                "05H4B2 exactly decomposes the frozen training retrieval "
                "metric into query-, identity-, and category-level components. "
                "It does not alter selection, folds, representation, or "
                "inference, and category contrasts are descriptive."
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
        "\nP2-R0-05H4B2 EXACT TRAINING "
        "DECOMPOSITION: COMPLETE"
    )

    print(
        "Query table:",
        QUERY_CSV,
    )

    print(
        "Identity summary:",
        IDENTITY_CSV,
    )

    print(
        "Category summary:",
        CATEGORY_CSV,
    )

    print(
        "Fold-3 category contrast:",
        FOLD3_CATEGORY_CSV,
    )

    print(
        "Fold-3 identity detail:",
        FOLD3_IDENTITY_CSV,
    )

    print(
        "Validation:",
        VALIDATION_CSV,
    )

    print(
        "Report:",
        REPORT_JSON,
    )

    print(
        "\nSTOP — fold-3 training decomposition complete. "
        "No fold exclusion or tuning performed."
    )


if __name__ == "__main__":
    main()