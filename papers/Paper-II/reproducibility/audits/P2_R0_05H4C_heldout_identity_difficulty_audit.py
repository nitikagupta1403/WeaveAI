from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd


# =============================================================================
# P2-R0-05H4C — HELD-OUT IDENTITY DIFFICULTY AUDIT
#
# Scientific question:
#   Are the identities assigned to test fold 3 intrinsically harder/confusable
#   when they are PRESENT in training in the other four folds?
#
# Why this is the right test:
#   H4B2 showed that INTRINSIC fold 3 has a broad low/mid training-MRR uplift.
#   If the identities assigned to fold 3 are genuinely harder, then when those
#   identities appear in training in folds 0/1/2/4, their own retrieval MRR
#   should be systematically lower than identities assigned to other test folds.
#
# Inputs:
#   - frozen fold package / identity assignments
#   - exact H4B2 per-identity training summaries
#
# Key design:
#   Every garment identity is test in exactly one fold and train in the other
#   four folds. For each identity we therefore aggregate its retrieval behavior
#   ONLY across the four folds where it is present in training.
#
# Outputs:
#   - identity-level difficulty table
#   - category x assigned-test-fold summary
#   - assigned-test-fold global summary
#   - category-centered fold-3 contrast
#
# This is a diagnostic audit only:
#   no fold exclusion, no tuning, no representation change.
# =============================================================================


AUDIT_DIR = Path(__file__).resolve().parent

BASE_AUDIT = (
    AUDIT_DIR
    / "P2_R0_05_annotation_control_sensitivity.py"
)

H4B2_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05h_intrinsic_coordinate/"
    "P2_R0_05H4B2_training_decomposition"
)

H4B2_IDENTITY_CSV = (
    H4B2_ROOT
    / "P2_R0_05H4B2_training_identity_summary.csv"
)

H4B2_VALIDATION_CSV = (
    H4B2_ROOT
    / "P2_R0_05H4B2_exact_mrr_validation.csv"
)

OUTPUT_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05h_intrinsic_coordinate/"
    "P2_R0_05H4C_heldout_identity_difficulty"
)

IDENTITY_DIFFICULTY_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05H4C_identity_difficulty.csv"
)

CATEGORY_FOLD_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05H4C_category_by_assigned_test_fold.csv"
)

FOLD_SUMMARY_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05H4C_assigned_test_fold_summary.csv"
)

FOLD3_CONTRAST_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05H4C_fold3_category_centered_contrast.csv"
)

REPORT_JSON = (
    OUTPUT_ROOT
    / "P2_R0_05H4C_report.json"
)

FOCUS_DATASET = "INTRINSIC"

FOCUS_BANDS = [
    "low_1_4",
    "mid_5_12",
]

FOCUS_STATES = [
    "full",
    "selected",
]

EXPECTED_IDENTITIES = 230
EXPECTED_CATEGORIES = 23
EXPECTED_FOLDS = 5


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
        "load_and_validate_fold_package",
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
        "P2-R0-05H4C VERIFIED DEFINITIONS: PASS"
    )

    return namespace


def build_identity_fold_map(
    G,
    C,
    folds,
) -> pd.DataFrame:

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

    rows = []

    for garment_identity in np.unique(
        G
    ):

        idx = np.flatnonzero(
            G
            == garment_identity
        )

        categories = np.unique(
            C[
                idx
            ]
        )

        assigned_folds = np.unique(
            folds[
                idx
            ]
        )

        if len(
            categories
        ) != 1:
            raise RuntimeError(
                f"{garment_identity} spans multiple categories"
            )

        if len(
            assigned_folds
        ) != 1:
            raise RuntimeError(
                f"{garment_identity} spans multiple test folds"
            )

        rows.append(
            {
                "garment_identity":
                    garment_identity,

                "category":
                    str(
                        categories[
                            0
                        ]
                    ),

                "assigned_test_fold":
                    int(
                        assigned_folds[
                            0
                        ]
                    ),

                "n_sketches":
                    int(
                        len(
                            idx
                        )
                    ),
            }
        )

    table = pd.DataFrame(
        rows
    )

    if len(
        table
    ) != EXPECTED_IDENTITIES:
        raise RuntimeError(
            f"Expected {EXPECTED_IDENTITIES} identities, "
            f"got {len(table)}"
        )

    fold_counts = (
        table
        .groupby(
            [
                "category",
                "assigned_test_fold",
            ]
        )[
            "garment_identity"
        ]
        .nunique()
    )

    if not np.all(
        fold_counts.to_numpy()
        == 2
    ):
        raise RuntimeError(
            "Expected exactly 2 identities/category/test-fold"
        )

    return table


def aggregate_identity_training_difficulty(
    identity_summary: pd.DataFrame,
    identity_fold_map: pd.DataFrame,
) -> pd.DataFrame:

    focus = identity_summary[
        (
            identity_summary[
                "dataset"
            ]
            == FOCUS_DATASET
        )
        &
        (
            identity_summary[
                "harmonic_band"
            ].isin(
                FOCUS_BANDS
            )
        )
        &
        (
            identity_summary[
                "representation_state"
            ].isin(
                FOCUS_STATES
            )
        )
    ].copy()

    merged = focus.merge(
        identity_fold_map,
        on=[
            "garment_identity",
            "category",
        ],
        how="inner",
        validate="many_to_one",
    )

    # Critical structural gate:
    # An identity must appear in training in all folds except its assigned test fold.
    bad = merged[
        merged[
            "fold"
        ]
        == merged[
            "assigned_test_fold"
        ]
    ]

    if len(
        bad
    ) != 0:
        raise RuntimeError(
            "Found identity summary row in its own test fold"
        )

    fold_presence = (
        merged
        .groupby(
            [
                "garment_identity",
                "harmonic_band",
                "representation_state",
            ]
        )[
            "fold"
        ]
        .nunique()
    )

    if not np.all(
        fold_presence.to_numpy()
        == 4
    ):
        raise RuntimeError(
            "Each identity should be present in training in exactly 4 folds"
        )

    agg = (
        merged
        .groupby(
            [
                "garment_identity",
                "category",
                "assigned_test_fold",
                "n_sketches",
                "harmonic_band",
                "representation_state",
            ],
            as_index=False,
        )
        .agg(
            n_training_folds_observed=(
                "fold",
                "nunique",
            ),

            mean_training_mrr_when_present=(
                "mean_reciprocal_rank",
                "mean",
            ),

            median_training_mrr_when_present=(
                "mean_reciprocal_rank",
                "median",
            ),

            min_training_mrr_when_present=(
                "mean_reciprocal_rank",
                "min",
            ),

            max_training_mrr_when_present=(
                "mean_reciprocal_rank",
                "max",
            ),

            mean_training_top1_when_present=(
                "top1_accuracy",
                "mean",
            ),

            mean_own_distance_squared_when_present=(
                "mean_own_distance_squared",
                "mean",
            ),

            median_identity_rank_when_present=(
                "median_rank",
                "median",
            ),
        )
    )

    return agg


def build_category_fold_summary(
    identity_difficulty: pd.DataFrame,
) -> pd.DataFrame:

    return (
        identity_difficulty
        .groupby(
            [
                "harmonic_band",
                "representation_state",
                "category",
                "assigned_test_fold",
            ],
            as_index=False,
        )
        .agg(
            n_identities=(
                "garment_identity",
                "nunique",
            ),

            mean_identity_mrr_when_present=(
                "mean_training_mrr_when_present",
                "mean",
            ),

            median_identity_mrr_when_present=(
                "mean_training_mrr_when_present",
                "median",
            ),

            mean_identity_top1_when_present=(
                "mean_training_top1_when_present",
                "mean",
            ),

            mean_own_distance_squared_when_present=(
                "mean_own_distance_squared_when_present",
                "mean",
            ),
        )
    )


def build_fold_summary(
    category_fold: pd.DataFrame,
) -> pd.DataFrame:

    return (
        category_fold
        .groupby(
            [
                "harmonic_band",
                "representation_state",
                "assigned_test_fold",
            ],
            as_index=False,
        )
        .agg(
            categories=(
                "category",
                "nunique",
            ),

            category_balanced_mean_identity_mrr_when_present=(
                "mean_identity_mrr_when_present",
                "mean",
            ),

            category_median_identity_mrr_when_present=(
                "mean_identity_mrr_when_present",
                "median",
            ),

            category_balanced_mean_top1_when_present=(
                "mean_identity_top1_when_present",
                "mean",
            ),

            category_balanced_mean_own_distance_squared_when_present=(
                "mean_own_distance_squared_when_present",
                "mean",
            ),
        )
    )


def build_fold3_contrast(
    category_fold: pd.DataFrame,
) -> pd.DataFrame:

    rows = []

    for (
        band,
        state,
        category,
    ), group in category_fold.groupby(
        [
            "harmonic_band",
            "representation_state",
            "category",
        ],
        sort=True,
    ):

        f3 = group[
            group[
                "assigned_test_fold"
            ]
            == 3
        ]

        peers = group[
            group[
                "assigned_test_fold"
            ]
            != 3
        ]

        if len(
            f3
        ) != 1:
            raise RuntimeError(
                "Expected one category row for fold 3"
            )

        r3 = f3.iloc[
            0
        ]

        peer_median_mrr = float(
            peers[
                "mean_identity_mrr_when_present"
            ].median()
        )

        peer_median_top1 = float(
            peers[
                "mean_identity_top1_when_present"
            ].median()
        )

        peer_median_distance = float(
            peers[
                "mean_own_distance_squared_when_present"
            ].median()
        )

        rows.append(
            {
                "harmonic_band":
                    band,

                "representation_state":
                    state,

                "category":
                    category,

                "fold3_identity_mrr_when_present":
                    float(
                        r3[
                            "mean_identity_mrr_when_present"
                        ]
                    ),

                "peer_median_identity_mrr_when_present":
                    peer_median_mrr,

                "fold3_minus_peer_identity_mrr_when_present":
                    float(
                        r3[
                            "mean_identity_mrr_when_present"
                        ]
                    )
                    - peer_median_mrr,

                "fold3_identity_top1_when_present":
                    float(
                        r3[
                            "mean_identity_top1_when_present"
                        ]
                    ),

                "peer_median_identity_top1_when_present":
                    peer_median_top1,

                "fold3_minus_peer_identity_top1_when_present":
                    float(
                        r3[
                            "mean_identity_top1_when_present"
                        ]
                    )
                    - peer_median_top1,

                "fold3_own_distance_squared_when_present":
                    float(
                        r3[
                            "mean_own_distance_squared_when_present"
                        ]
                    ),

                "peer_median_own_distance_squared_when_present":
                    peer_median_distance,

                "fold3_minus_peer_own_distance_squared_when_present":
                    float(
                        r3[
                            "mean_own_distance_squared_when_present"
                        ]
                    )
                    - peer_median_distance,
            }
        )

    result = pd.DataFrame(
        rows
    )

    return result.sort_values(
        [
            "harmonic_band",
            "representation_state",
            "fold3_minus_peer_identity_mrr_when_present",
        ],
        ascending=[
            True,
            True,
            True,
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
        IDENTITY_DIFFICULTY_CSV,
        CATEGORY_FOLD_CSV,
        FOLD_SUMMARY_CSV,
        FOLD3_CONTRAST_CSV,
        REPORT_JSON,
    ):
        if path.exists():
            raise RuntimeError(
                f"Refusing to overwrite: {path}"
            )

    if not H4B2_IDENTITY_CSV.is_file():
        raise RuntimeError(
            f"Missing H4B2 identity summary: {H4B2_IDENTITY_CSV}"
        )

    if not H4B2_VALIDATION_CSV.is_file():
        raise RuntimeError(
            f"Missing H4B2 validation file: {H4B2_VALIDATION_CSV}"
        )

    validation = pd.read_csv(
        H4B2_VALIDATION_CSV
    )

    if not bool(
        validation[
            "exact_within_tolerance"
        ].astype(
            bool
        ).all()
    ):
        raise RuntimeError(
            "H4B2 exact MRR validation did not fully pass"
        )

    if float(
        validation[
            "absolute_difference"
        ].max()
    ) != 0.0:
        raise RuntimeError(
            "H4B2 MRR validation is not exact-zero"
        )

    base = load_verified_definitions()

    runtime = base[
        "load_paper2_runtime"
    ]()

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

    identity_fold_map = build_identity_fold_map(
        G,
        C,
        folds,
    )

    identity_summary = pd.read_csv(
        H4B2_IDENTITY_CSV
    )

    identity_difficulty = (
        aggregate_identity_training_difficulty(
            identity_summary,
            identity_fold_map,
        )
    )

    identity_difficulty.to_csv(
        IDENTITY_DIFFICULTY_CSV,
        index=False,
    )

    category_fold = build_category_fold_summary(
        identity_difficulty
    )

    category_fold.to_csv(
        CATEGORY_FOLD_CSV,
        index=False,
    )

    fold_summary = build_fold_summary(
        category_fold
    )

    fold_summary.to_csv(
        FOLD_SUMMARY_CSV,
        index=False,
    )

    fold3_contrast = build_fold3_contrast(
        category_fold
    )

    fold3_contrast.to_csv(
        FOLD3_CONTRAST_CSV,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Console output
    # -------------------------------------------------------------------------

    print(
        "\n"
        + "=" * 150
    )

    print(
        "P2-R0-05H4C — ASSIGNED TEST-FOLD IDENTITY DIFFICULTY"
    )

    print(
        "=" * 150
    )

    print(
        fold_summary.to_string(
            index=False
        )
    )

    print(
        "\n"
        + "=" * 150
    )

    print(
        "P2-R0-05H4C — FOLD-3 CATEGORY-CENTERED CONTRAST"
    )

    print(
        "=" * 150
    )

    contrast_print = fold3_contrast[
        [
            "harmonic_band",
            "representation_state",
            "category",
            "fold3_identity_mrr_when_present",
            "peer_median_identity_mrr_when_present",
            "fold3_minus_peer_identity_mrr_when_present",
            "fold3_identity_top1_when_present",
            "peer_median_identity_top1_when_present",
            "fold3_minus_peer_identity_top1_when_present",
        ]
    ]

    print(
        contrast_print.to_string(
            index=False
        )
    )

    print(
        "\n"
        + "=" * 150
    )

    print(
        "P2-R0-05H4C — FOLD-3 DIRECTION SUMMARY"
    )

    print(
        "=" * 150
    )

    direction_rows = []

    for (
        band,
        state,
    ), group in fold3_contrast.groupby(
        [
            "harmonic_band",
            "representation_state",
        ],
        sort=True,
    ):

        diff = group[
            "fold3_minus_peer_identity_mrr_when_present"
        ].to_numpy(
            dtype=float
        )

        direction_rows.append(
            {
                "harmonic_band":
                    band,

                "representation_state":
                    state,

                "categories_fold3_harder_lower_mrr":
                    int(
                        np.sum(
                            diff
                            < 0
                        )
                    ),

                "categories_fold3_easier_higher_mrr":
                    int(
                        np.sum(
                            diff
                            > 0
                        )
                    ),

                "categories_equal":
                    int(
                        np.sum(
                            diff
                            == 0
                        )
                    ),

                "median_fold3_minus_peer_mrr":
                    float(
                        np.median(
                            diff
                        )
                    ),

                "mean_fold3_minus_peer_mrr":
                    float(
                        np.mean(
                            diff
                        )
                    ),
            }
        )

    direction = pd.DataFrame(
        direction_rows
    )

    print(
        direction.to_string(
            index=False
        )
    )

    # -------------------------------------------------------------------------
    # Report / hashes
    # -------------------------------------------------------------------------

    report = {
        "stage":
            "P2_R0_05H4C_HELDOUT_IDENTITY_DIFFICULTY",

        "status":
            "COMPLETE",

        "focus_dataset":
            FOCUS_DATASET,

        "focus_bands":
            FOCUS_BANDS,

        "focus_states":
            FOCUS_STATES,

        "identities":
            int(
                identity_fold_map[
                    "garment_identity"
                ].nunique()
            ),

        "categories":
            int(
                identity_fold_map[
                    "category"
                ].nunique()
            ),

        "folds":
            sorted(
                identity_fold_map[
                    "assigned_test_fold"
                ].unique()
                .astype(
                    int
                )
                .tolist()
            ),

        "fold_package_sha256":
            fold_sha,

        "h4b2_identity_csv_sha256":
            sha256_file(
                H4B2_IDENTITY_CSV
            ),

        "h4b2_validation_csv_sha256":
            sha256_file(
                H4B2_VALIDATION_CSV
            ),

        "identity_difficulty_csv_sha256":
            sha256_file(
                IDENTITY_DIFFICULTY_CSV
            ),

        "category_fold_csv_sha256":
            sha256_file(
                CATEGORY_FOLD_CSV
            ),

        "fold_summary_csv_sha256":
            sha256_file(
                FOLD_SUMMARY_CSV
            ),

        "fold3_contrast_csv_sha256":
            sha256_file(
                FOLD3_CONTRAST_CSV
            ),

        "interpretation_boundary":
            (
                "This audit asks whether identities assigned to fold 3 are "
                "harder when they are present in training in the other four "
                "folds. It is descriptive and does not alter folds, selection, "
                "representation, or inferential conclusions."
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
        "\nP2-R0-05H4C HELD-OUT IDENTITY "
        "DIFFICULTY AUDIT: COMPLETE"
    )

    print(
        "Identity difficulty:",
        IDENTITY_DIFFICULTY_CSV,
    )

    print(
        "Category x fold:",
        CATEGORY_FOLD_CSV,
    )

    print(
        "Fold summary:",
        FOLD_SUMMARY_CSV,
    )

    print(
        "Fold-3 contrast:",
        FOLD3_CONTRAST_CSV,
    )

    print(
        "Report:",
        REPORT_JSON,
    )

    print(
        "\nSTOP — diagnostic complete. "
        "Do not exclude fold 3 or tune representation from this audit."
    )


if __name__ == "__main__":
    main()