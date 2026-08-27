from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import subprocess
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, f1_score
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


# =============================================================================
# PATHS
# =============================================================================

E8 = Path(__file__).resolve().parent
PAPER_ROOT = E8.parent.parent
REPO_ROOT = E8.parents[3]

PREFLIGHT_PATH = E8 / "preflight.py"

RA14_PATH = E8 / "experiment08_ra14_features.npy"
RA14_ROW_MANIFEST = E8 / "experiment08_ra14_source_manifest.csv"
RA14_LOCK = E8 / "experiment08_ra14_manifest.json"

DINO_LOCK = E8 / "experiment08_dinov2_feature_lock.json"

DINO_PATH = Path(
    os.environ.get(
        "CLO_SKET_DINO_FEATURE_PATH",
        E8 / "experiment08_dinov2_vits14_embeddings.npy",
    )
)

DINO_ROWS = Path(
    os.environ.get(
        "CLO_SKET_DINO_ROW_PATH",
        E8 / "experiment08_dinov2_embedding_rows.csv",
    )
)

PRIMARY_POINT_ESTIMATE = (
    PAPER_ROOT
    / "evidence"
    / "Experiment_08"
    / "experiment08_primary_point_estimate.json"
)

EVIDENCE_DIR = (
    PAPER_ROOT
    / "evidence"
    / "Experiment_08"
)

RUNNER_PATH = Path(__file__).resolve()

AMENDMENT_REL = Path(
    "docs/experiment-08/"
    "post-outcome-predictive-controls-amendment.md"
)

CLARIFICATION_REL = Path(
    "docs/experiment-08/"
    "post-outcome-predictive-controls-clarification.md"
)


# =============================================================================
# PROVENANCE LOCKS
# =============================================================================

AMENDMENT_COMMIT = (
    "6e62d94d7a29088f92ec0c6d617bbf265d2810c1"
)

CLARIFICATION_COMMIT = (
    "7b4b283f0070b67817c71982526b3ed64034be4e"
)

STATUS = "POST_OUTCOME_EXPLORATORY_ONLY"


# =============================================================================
# FROZEN DATA / MODEL CONSTANTS
# =============================================================================

EXPECTED_ROWS = 2300
EXPECTED_IDENTITIES = 230
EXPECTED_CATEGORIES = 23

EXPECTED_RA14_DIM = 14
EXPECTED_DINO_DIM = 384

EXPECTED_RA14_FILE_SHA = (
    "2e9b7d6ddd144c6b85b66cd44ae60cbb72c84f0029e8f50afff77a833edbd033"
)

EXPECTED_DINO_FILE_SHA = (
    "6958b8b05eee66304ecda038cc5fedef33eecd139dccc20c12dc6d223c614d97"
)

EXPECTED_DINO_ROW_SHA = (
    "072f08ae9fb8328fe73a2566c1d5e812560cd4b007bf1c88550adbb082a6a4d9"
)

EXPECTED_CORRECTED_FOLD_SHA = (
    "e3fb0cf57b886bc303333795de42ecfc38cb1da9728d4d5cc365b47a91504c1f"
)

EXPECTED_TEST_ROWS = [459, 460, 461, 460, 460]

CLASSIFIER_SEED = 20260820

EXPECTED_PRIMARY_DELTA = 0.0009466521822523166
EXPECTED_PRIMARY_F1_L = 0.7380200305882273
EXPECTED_PRIMARY_F1_LG = 0.7389666827704796

PERMUTATION_MASTER_SEED = 20260822
N_PERMUTATIONS = 1000

REPEATED_PARTITION_SEEDS = tuple(
    range(20260823, 20260843)
)

EXPECTED_PERMUTATION_ELIGIBLE_IDENTITIES = 228
EXPECTED_STRUCTURALLY_FIXED_IDENTITIES = 2

EXPECTED_FIXED_IDENTITIES = {
    "Jumpsuit__G02",
    "Jumpsuit__G06",
}


# =============================================================================
# OUTPUT PATHS
# =============================================================================

CORRESPONDENCE_CSV = (
    EVIDENCE_DIR
    / "experiment08_correspondence_permutation.csv"
)

CORRESPONDENCE_SUMMARY = (
    EVIDENCE_DIR
    / "experiment08_correspondence_permutation_summary.json"
)

REPEATED_CSV = (
    EVIDENCE_DIR
    / "experiment08_repeated_grouped_partitions.csv"
)

REPEATED_SUMMARY = (
    EVIDENCE_DIR
    / "experiment08_repeated_grouped_partitions_summary.json"
)


# =============================================================================
# BASIC HELPERS
# =============================================================================

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as handle:
        for chunk in iter(
            lambda: handle.read(1024 * 1024),
            b"",
        ):
            digest.update(chunk)

    return digest.hexdigest()


def sha256_int_array(values: np.ndarray) -> str:
    arr = np.asarray(values, dtype=np.int64)

    return hashlib.sha256(
        arr.tobytes(order="C")
    ).hexdigest()


def git(
    *args: str,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:

    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=check,
    )


def load_preflight_module():
    spec = importlib.util.spec_from_file_location(
        "experiment08_preflight_controls",
        PREFLIGHT_PATH,
    )

    if spec is None or spec.loader is None:
        raise RuntimeError(
            "Could not construct preflight module specification."
        )

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def make_classifier() -> Pipeline:
    return Pipeline([
        (
            "scaler",
            StandardScaler(),
        ),
        (
            "classifier",
            LogisticRegression(
                penalty="l2",
                C=1.0,
                solver="lbfgs",
                max_iter=5000,
                random_state=CLASSIFIER_SEED,
            ),
        ),
    ])


def json_safe_float(value: float) -> float:
    return float(value)


# =============================================================================
# EXECUTION CHRONOLOGY GUARD
# =============================================================================

def verify_execution_chronology() -> dict:
    top = Path(
        git(
            "rev-parse",
            "--show-toplevel",
        ).stdout.strip()
    ).resolve()

    if top != REPO_ROOT.resolve():
        raise RuntimeError(
            "Repository-root mismatch."
        )

    for required_commit in [
        AMENDMENT_COMMIT,
        CLARIFICATION_COMMIT,
    ]:
        result = git(
            "merge-base",
            "--is-ancestor",
            required_commit,
            "HEAD",
            check=False,
        )

        if result.returncode != 0:
            raise RuntimeError(
                "Required prospective commit is not an "
                f"ancestor of HEAD: {required_commit}"
            )

    runner_rel = RUNNER_PATH.relative_to(
        REPO_ROOT
    ).as_posix()

    tracked = git(
        "ls-files",
        "--error-unmatch",
        runner_rel,
        check=False,
    )

    if tracked.returncode != 0:
        raise RuntimeError(
            "EXECUTION PROHIBITED: this runner has not "
            "yet been committed."
        )

    unstaged = git(
        "diff",
        "--quiet",
        "--",
        runner_rel,
        check=False,
    )

    staged = git(
        "diff",
        "--cached",
        "--quiet",
        "--",
        runner_rel,
        check=False,
    )

    if unstaged.returncode != 0:
        raise RuntimeError(
            "EXECUTION PROHIBITED: runner has uncommitted "
            "working-tree changes."
        )

    if staged.returncode != 0:
        raise RuntimeError(
            "EXECUTION PROHIBITED: runner has staged but "
            "uncommitted changes."
        )

    execution_head = git(
        "rev-parse",
        "HEAD",
    ).stdout.strip()

    source_commit = git(
        "log",
        "-1",
        "--format=%H",
        "--",
        runner_rel,
    ).stdout.strip()

    if not source_commit:
        raise RuntimeError(
            "Could not resolve committed runner source."
        )

    result = git(
        "merge-base",
        "--is-ancestor",
        CLARIFICATION_COMMIT,
        source_commit,
        check=False,
    )

    if result.returncode != 0:
        raise RuntimeError(
            "Runner implementation does not descend from "
            "the prospective structural clarification."
        )

    return {
        "execution_head_commit":
            execution_head,
        "runner_source_commit":
            source_commit,
        "runner_relative_path":
            runner_rel,
    }


# =============================================================================
# FROZEN INPUT LOADING AND STRUCTURAL VERIFICATION
# =============================================================================

def load_frozen_inputs() -> dict:
    required_paths = [
        PREFLIGHT_PATH,
        RA14_PATH,
        RA14_ROW_MANIFEST,
        RA14_LOCK,
        DINO_LOCK,
        DINO_PATH,
        DINO_ROWS,
        PRIMARY_POINT_ESTIMATE,
        REPO_ROOT / AMENDMENT_REL,
        REPO_ROOT / CLARIFICATION_REL,
    ]

    for path in required_paths:
        if not path.is_file():
            raise RuntimeError(
                f"Required frozen artifact missing: {path}"
            )

    ra14_sha = sha256_file(
        RA14_PATH
    )

    dino_sha = sha256_file(
        DINO_PATH
    )

    dino_rows_sha = sha256_file(
        DINO_ROWS
    )

    if ra14_sha != EXPECTED_RA14_FILE_SHA:
        raise RuntimeError(
            f"RA14 NPY hash mismatch: {ra14_sha}"
        )

    if dino_sha != EXPECTED_DINO_FILE_SHA:
        raise RuntimeError(
            f"DINO NPY hash mismatch: {dino_sha}"
        )

    if dino_rows_sha != EXPECTED_DINO_ROW_SHA:
        raise RuntimeError(
            f"DINO row-map hash mismatch: {dino_rows_sha}"
        )

    ra14_lock = json.loads(
        RA14_LOCK.read_text(
            encoding="utf-8"
        )
    )

    dino_lock = json.loads(
        DINO_LOCK.read_text(
            encoding="utf-8"
        )
    )

    for lock_name, lock in [
        ("RA14", ra14_lock),
        ("DINO", dino_lock),
    ]:
        if lock["classifier_fitted"] is not False:
            raise RuntimeError(
                f"{lock_name} lock does not preserve "
                "the original pre-outcome boundary."
            )

        if (
            lock["predictive_outcome_computed"]
            is not False
        ):
            raise RuntimeError(
                f"{lock_name} lock reports a predictive "
                "outcome inside the frozen feature lock."
            )

    G = np.load(
        RA14_PATH,
        allow_pickle=False,
    )

    L = np.load(
        DINO_PATH,
        allow_pickle=False,
    )

    if G.shape != (
        EXPECTED_ROWS,
        EXPECTED_RA14_DIM,
    ):
        raise RuntimeError(
            f"RA14 shape mismatch: {G.shape}"
        )

    if L.shape != (
        EXPECTED_ROWS,
        EXPECTED_DINO_DIM,
    ):
        raise RuntimeError(
            f"DINO shape mismatch: {L.shape}"
        )

    if not np.isfinite(G).all():
        raise RuntimeError(
            "RA14 contains non-finite values."
        )

    if not np.isfinite(L).all():
        raise RuntimeError(
            "DINO contains non-finite values."
        )

    pf = load_preflight_module()

    rows_historical, historical_audit = (
        pf.validate_public_maps(
            pf.DEFAULT_ROW_MAP,
            pf.DEFAULT_FOLD_MAP,
        )
    )

    rows, corrected_audit = (
        pf.apply_identity_overrides(
            rows_historical,
            pf.DEFAULT_IDENTITY_OVERRIDES,
            historical_audit,
        )
    )

    rows = rows.copy()

    observed_fold_sha = (
        corrected_audit[
            "experiment08_fold_array_sha256"
        ]
    )

    if (
        observed_fold_sha
        != EXPECTED_CORRECTED_FOLD_SHA
    ):
        raise RuntimeError(
            "Corrected Experiment-08 fold hash mismatch: "
            f"{observed_fold_sha}"
        )

    if len(rows) != EXPECTED_ROWS:
        raise RuntimeError(
            f"Expected {EXPECTED_ROWS} authoritative rows."
        )

    observed_test_rows = [
        int(
            (
                rows["fold_id"] == fold
            ).sum()
        )
        for fold in range(5)
    ]

    if observed_test_rows != EXPECTED_TEST_ROWS:
        raise RuntimeError(
            "Corrected fold-row counts differ from lock: "
            f"{observed_test_rows}"
        )

    ra14_rows = pd.read_csv(
        RA14_ROW_MANIFEST,
        keep_default_na=False,
    )

    dino_rows = pd.read_csv(
        DINO_ROWS,
        keep_default_na=False,
    )

    authoritative_paths = (
        rows["image_path_runtime"]
        .map(
            pf.normalized_relative_path
        )
        .tolist()
    )

    expected_row_index = list(
        range(EXPECTED_ROWS)
    )

    if (
        ra14_rows["row_index"].tolist()
        != expected_row_index
    ):
        raise RuntimeError(
            "RA14 row_index is not 0..2299."
        )

    if (
        dino_rows["row_index"].tolist()
        != expected_row_index
    ):
        raise RuntimeError(
            "DINO row_index is not 0..2299."
        )

    if (
        ra14_rows["relative_path"].tolist()
        != authoritative_paths
    ):
        raise RuntimeError(
            "RA14 rows differ from authoritative rows."
        )

    if (
        dino_rows["relative_path"].tolist()
        != authoritative_paths
    ):
        raise RuntimeError(
            "DINO rows differ from authoritative rows."
        )

    y = (
        rows["category"]
        .astype(str)
        .to_numpy()
    )

    groups = (
        rows["garment_id"]
        .astype(str)
        .to_numpy()
    )

    fold_id = rows[
        "fold_id"
    ].to_numpy(
        dtype=int
    )

    if (
        len(np.unique(y))
        != EXPECTED_CATEGORIES
    ):
        raise RuntimeError(
            "Expected exactly 23 categories."
        )

    if (
        len(np.unique(groups))
        != EXPECTED_IDENTITIES
    ):
        raise RuntimeError(
            "Expected exactly 230 garment identities."
        )

    # Every identity must remain category-homogeneous
    # and fold-homogeneous.
    identity_records = []

    for garment_id in sorted(
        np.unique(groups)
    ):
        idx = np.flatnonzero(
            groups == garment_id
        )

        categories = np.unique(
            y[idx]
        )

        folds = np.unique(
            fold_id[idx]
        )

        if len(categories) != 1:
            raise RuntimeError(
                f"{garment_id}: spans categories."
            )

        if len(folds) != 1:
            raise RuntimeError(
                f"{garment_id}: spans frozen folds."
            )

        identity_records.append({
            "garment_id":
                garment_id,
            "category":
                str(categories[0]),
            "n_rows":
                int(len(idx)),
            "fold_id":
                int(folds[0]),
        })

    identity_frame = pd.DataFrame(
        identity_records
    )

    size_distribution = (
        identity_frame[
            "n_rows"
        ]
        .value_counts()
        .sort_index()
        .to_dict()
    )

    expected_size_distribution = {
        9: 1,
        10: 228,
        11: 1,
    }

    if size_distribution != (
        expected_size_distribution
    ):
        raise RuntimeError(
            "Identity block-size structure differs "
            f"from clarification: {size_distribution}"
        )

    fixed_observed = set(
        identity_frame.loc[
            identity_frame["n_rows"].isin(
                [9, 11]
            ),
            "garment_id",
        ]
    )

    if fixed_observed != (
        EXPECTED_FIXED_IDENTITIES
    ):
        raise RuntimeError(
            "Unexpected non-modal identity set: "
            f"{sorted(fixed_observed)}"
        )

    # Frozen fold identity-disjointness.
    for fold in range(5):
        test_idx = np.flatnonzero(
            fold_id == fold
        )

        train_idx = np.flatnonzero(
            fold_id != fold
        )

        test_ids = set(
            groups[test_idx]
        )

        train_ids = set(
            groups[train_idx]
        )

        if train_ids & test_ids:
            raise RuntimeError(
                f"Fold {fold}: identity leakage."
            )

        if len(test_ids) != 46:
            raise RuntimeError(
                f"Fold {fold}: expected 46 "
                "test identities."
            )

        if len(train_ids) != 184:
            raise RuntimeError(
                f"Fold {fold}: expected 184 "
                "train identities."
            )

    primary = json.loads(
        PRIMARY_POINT_ESTIMATE.read_text(
            encoding="utf-8"
        )
    )

    if (
        primary[
            "fold_array_sha256"
        ]
        != EXPECTED_CORRECTED_FOLD_SHA
    ):
        raise RuntimeError(
            "Stored primary point estimate uses "
            "a different fold array."
        )

    if not np.isclose(
        float(
            primary[
                "delta_G_given_L"
            ]
        ),
        EXPECTED_PRIMARY_DELTA,
        rtol=0.0,
        atol=1e-15,
    ):
        raise RuntimeError(
            "Stored primary delta differs from "
            "the canonical exploratory value."
        )

    if not np.isclose(
        float(
            primary["macro_f1_L"]
        ),
        EXPECTED_PRIMARY_F1_L,
        rtol=0.0,
        atol=1e-15,
    ):
        raise RuntimeError(
            "Stored L macro-F1 differs from canonical."
        )

    if not np.isclose(
        float(
            primary[
                "macro_f1_L_plus_G"
            ]
        ),
        EXPECTED_PRIMARY_F1_LG,
        rtol=0.0,
        atol=1e-15,
    ):
        raise RuntimeError(
            "Stored L+G macro-F1 differs from canonical."
        )

    return {
        "G":
            G,
        "L":
            L,
        "rows":
            rows,
        "y":
            y,
        "groups":
            groups,
        "fold_id":
            fold_id,
        "identity_frame":
            identity_frame,
        "authoritative_paths":
            authoritative_paths,
        "ra14_sha256":
            ra14_sha,
        "dino_sha256":
            dino_sha,
        "dino_rows_sha256":
            dino_rows_sha,
        "fold_array_sha256":
            observed_fold_sha,
        "primary":
            primary,
    }


# =============================================================================
# OOF FITTING
# =============================================================================

def fit_oof(
    X: np.ndarray,
    y: np.ndarray,
    fold_assignment: np.ndarray,
) -> dict:

    fold_assignment = np.asarray(
        fold_assignment,
        dtype=int,
    )

    if fold_assignment.shape != (
        len(y),
    ):
        raise RuntimeError(
            "Fold-assignment shape mismatch."
        )

    if set(
        np.unique(
            fold_assignment
        ).tolist()
    ) != {
        0,
        1,
        2,
        3,
        4,
    }:
        raise RuntimeError(
            "OOF evaluation requires exactly "
            "fold labels 0..4."
        )

    predictions = np.empty(
        len(y),
        dtype=object,
    )

    max_iterations = 0
    all_converged = True

    for fold in range(5):
        test_idx = np.flatnonzero(
            fold_assignment == fold
        )

        train_idx = np.flatnonzero(
            fold_assignment != fold
        )

        if (
            len(test_idx) == 0
            or len(train_idx) == 0
        ):
            raise RuntimeError(
                f"Fold {fold}: empty train/test split."
            )

        model = make_classifier()

        model.fit(
            X[train_idx],
            y[train_idx],
        )

        pred = model.predict(
            X[test_idx]
        )

        predictions[
            test_idx
        ] = pred

        iterations = int(
            np.max(
                model.named_steps[
                    "classifier"
                ].n_iter_
            )
        )

        max_iterations = max(
            max_iterations,
            iterations,
        )

        if iterations >= 5000:
            all_converged = False

    if any(
        value is None
        for value in predictions
    ):
        raise RuntimeError(
            "OOF prediction vector was not fully filled."
        )

    return {
        "macro_f1":
            float(
                f1_score(
                    y,
                    predictions,
                    average="macro",
                )
            ),
        "balanced_accuracy":
            float(
                balanced_accuracy_score(
                    y,
                    predictions,
                )
            ),
        "max_iterations":
            int(max_iterations),
        "all_converged":
            bool(all_converged),
    }


# =============================================================================
# OUTPUT HELPERS
# =============================================================================

def ensure_output_absent(
    *paths: Path,
) -> None:

    for path in paths:
        if path.exists():
            raise RuntimeError(
                "Refusing to overwrite existing control "
                f"evidence: {path}"
            )


def write_evidence_pair(
    frame: pd.DataFrame,
    csv_path: Path,
    summary_path: Path,
    summary: dict,
) -> tuple[str, str]:

    ensure_output_absent(
        csv_path,
        summary_path,
    )

    EVIDENCE_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    csv_fd, csv_tmp_name = (
        tempfile.mkstemp(
            prefix=csv_path.name + ".",
            suffix=".tmp",
            dir=EVIDENCE_DIR,
        )
    )

    os.close(csv_fd)

    json_fd, json_tmp_name = (
        tempfile.mkstemp(
            prefix=summary_path.name + ".",
            suffix=".tmp",
            dir=EVIDENCE_DIR,
        )
    )

    os.close(json_fd)

    csv_tmp = Path(
        csv_tmp_name
    )

    json_tmp = Path(
        json_tmp_name
    )

    try:
        frame.to_csv(
            csv_tmp,
            index=False,
        )

        csv_sha = sha256_file(
            csv_tmp
        )

        summary = dict(
            summary
        )

        summary[
            "csv_output"
        ] = (
            csv_path.relative_to(
                REPO_ROOT
            ).as_posix()
        )

        summary[
            "csv_sha256"
        ] = csv_sha

        summary_path_rel = (
            summary_path.relative_to(
                REPO_ROOT
            ).as_posix()
        )

        summary[
            "summary_output"
        ] = summary_path_rel

        json_tmp.write_text(
            json.dumps(
                summary,
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )

        json_sha = sha256_file(
            json_tmp
        )

        os.replace(
            csv_tmp,
            csv_path,
        )

        os.replace(
            json_tmp,
            summary_path,
        )

    finally:
        if csv_tmp.exists():
            csv_tmp.unlink()

        if json_tmp.exists():
            json_tmp.unlink()

    return (
        csv_sha,
        json_sha,
    )


# =============================================================================
# CORRESPONDENCE PERMUTATION STRUCTURE
# =============================================================================

def build_identity_blocks(
    groups: np.ndarray,
    y: np.ndarray,
) -> tuple[
    dict[str, np.ndarray],
    dict[str, str],
    dict[str, int],
    dict[tuple[str, int], list[str]],
]:

    blocks: dict[
        str,
        np.ndarray,
    ] = {}

    identity_category: dict[
        str,
        str,
    ] = {}

    block_size: dict[
        str,
        int,
    ] = {}

    strata: dict[
        tuple[str, int],
        list[str],
    ] = {}

    for garment_id in sorted(
        np.unique(groups)
    ):
        idx = np.flatnonzero(
            groups == garment_id
        )

        # np.flatnonzero is ascending row-index order.
        if not np.all(
            np.diff(idx) > 0
        ):
            raise RuntimeError(
                f"{garment_id}: row order is not ascending."
            )

        categories = np.unique(
            y[idx]
        )

        if len(categories) != 1:
            raise RuntimeError(
                f"{garment_id}: category ambiguity."
            )

        category = str(
            categories[0]
        )

        size = int(
            len(idx)
        )

        blocks[
            garment_id
        ] = idx

        identity_category[
            garment_id
        ] = category

        block_size[
            garment_id
        ] = size

        strata.setdefault(
            (
                category,
                size,
            ),
            [],
        ).append(
            garment_id
        )

    for key in strata:
        strata[key] = sorted(
            strata[key]
        )

    return (
        blocks,
        identity_category,
        block_size,
        strata,
    )


def verify_permutation_strata(
    strata: dict[
        tuple[str, int],
        list[str],
    ],
) -> tuple[
    set[str],
    set[str],
]:

    eligible = set()
    structural_fixed = set()

    for ids in strata.values():
        if len(ids) == 1:
            structural_fixed.update(
                ids
            )
        else:
            eligible.update(
                ids
            )

    if len(eligible) != (
        EXPECTED_PERMUTATION_ELIGIBLE_IDENTITIES
    ):
        raise RuntimeError(
            "Permutation-eligible identity count differs "
            f"from clarification: {len(eligible)}"
        )

    if len(structural_fixed) != (
        EXPECTED_STRUCTURALLY_FIXED_IDENTITIES
    ):
        raise RuntimeError(
            "Structurally fixed identity count differs "
            f"from clarification: {len(structural_fixed)}"
        )

    if structural_fixed != (
        EXPECTED_FIXED_IDENTITIES
    ):
        raise RuntimeError(
            "Unexpected singleton permutation strata: "
            f"{sorted(structural_fixed)}"
        )

    if eligible & structural_fixed:
        raise RuntimeError(
            "Eligible/fixed identity sets overlap."
        )

    if len(
        eligible
        | structural_fixed
    ) != EXPECTED_IDENTITIES:
        raise RuntimeError(
            "Permutation strata do not cover all identities."
        )

    return (
        eligible,
        structural_fixed,
    )


def make_permuted_ra14(
    G: np.ndarray,
    rng: np.random.Generator,
    blocks: dict[str, np.ndarray],
    identity_category: dict[str, str],
    block_size: dict[str, int],
    strata: dict[
        tuple[str, int],
        list[str],
    ],
    structural_fixed: set[str],
) -> tuple[
    np.ndarray,
    dict,
]:

    G_permuted = np.empty_like(
        G
    )

    destination_filled = np.zeros(
        EXPECTED_ROWS,
        dtype=bool,
    )

    source_used = np.zeros(
        EXPECTED_ROWS,
        dtype=bool,
    )

    actual_reassigned = 0

    category_preserved = True
    block_size_preserved = True
    singleton_fixed = True

    for stratum in sorted(
        strata.keys(),
        key=lambda x: (
            x[0],
            x[1],
        ),
    ):
        destination_ids = list(
            strata[
                stratum
            ]
        )

        if len(
            destination_ids
        ) == 1:
            source_ids = list(
                destination_ids
            )
        else:
            source_ids = (
                rng.permutation(
                    destination_ids
                )
                .tolist()
            )

        if sorted(
            source_ids
        ) != sorted(
            destination_ids
        ):
            raise RuntimeError(
                "Permutation ceased to be a "
                "within-stratum bijection."
            )

        for (
            destination_id,
            source_id,
        ) in zip(
            destination_ids,
            source_ids,
            strict=True,
        ):
            destination_idx = blocks[
                destination_id
            ]

            source_idx = blocks[
                source_id
            ]

            if len(
                destination_idx
            ) != len(
                source_idx
            ):
                block_size_preserved = False
                raise RuntimeError(
                    "Attempted unequal-size block mapping."
                )

            if (
                identity_category[
                    destination_id
                ]
                != identity_category[
                    source_id
                ]
            ):
                category_preserved = False
                raise RuntimeError(
                    "Attempted cross-category block mapping."
                )

            if (
                block_size[
                    destination_id
                ]
                != block_size[
                    source_id
                ]
            ):
                block_size_preserved = False
                raise RuntimeError(
                    "Block-size stratum violation."
                )

            if destination_filled[
                destination_idx
            ].any():
                raise RuntimeError(
                    "Destination row filled more than once."
                )

            if source_used[
                source_idx
            ].any():
                raise RuntimeError(
                    "Source row used more than once."
                )

            G_permuted[
                destination_idx
            ] = G[
                source_idx
            ]

            destination_filled[
                destination_idx
            ] = True

            source_used[
                source_idx
            ] = True

            if (
                destination_id
                != source_id
            ):
                actual_reassigned += 1

            if (
                destination_id
                in structural_fixed
                and destination_id
                != source_id
            ):
                singleton_fixed = False

    all_destination_filled = bool(
        destination_filled.all()
    )

    all_source_used = bool(
        source_used.all()
    )

    if not all_destination_filled:
        raise RuntimeError(
            "Not all 2,300 destination rows were filled."
        )

    if not all_source_used:
        raise RuntimeError(
            "Not all 2,300 source rows were used exactly once."
        )

    if not category_preserved:
        raise RuntimeError(
            "Category preservation failed."
        )

    if not block_size_preserved:
        raise RuntimeError(
            "Block-size preservation failed."
        )

    if not singleton_fixed:
        raise RuntimeError(
            "Singleton permutation stratum moved."
        )

    if not np.isfinite(
        G_permuted
    ).all():
        raise RuntimeError(
            "Permuted RA14 contains non-finite values."
        )

    audit = {
        "permutation_eligible_identities":
            EXPECTED_PERMUTATION_ELIGIBLE_IDENTITIES,
        "structurally_fixed_identities":
            EXPECTED_STRUCTURALLY_FIXED_IDENTITIES,
        "actually_reassigned_identities":
            int(actual_reassigned),
        "all_2300_destination_rows_filled_once":
            all_destination_filled,
        "all_2300_source_rows_used_once":
            all_source_used,
        "category_preserved":
            category_preserved,
        "block_size_preserved":
            block_size_preserved,
        "singleton_strata_fixed":
            singleton_fixed,
    }

    return (
        G_permuted,
        audit,
    )


# =============================================================================
# CORRESPONDENCE PERMUTATION CONTROL
# =============================================================================

def run_correspondence_control(
    data: dict,
    chronology: dict,
) -> None:

    ensure_output_absent(
        CORRESPONDENCE_CSV,
        CORRESPONDENCE_SUMMARY,
    )

    G = data["G"]
    L = data["L"]
    y = data["y"]
    groups = data["groups"]
    fold_id = data["fold_id"]

    (
        blocks,
        identity_category,
        block_size,
        strata,
    ) = build_identity_blocks(
        groups,
        y,
    )

    (
        eligible,
        structural_fixed,
    ) = verify_permutation_strata(
        strata
    )

    print("=" * 88)
    print(
        "EXPERIMENT 08 — POST-OUTCOME "
        "CORRESPONDENCE PERMUTATION CONTROL"
    )
    print("=" * 88)
    print(
        "Status: POST_OUTCOME_EXPLORATORY_ONLY"
    )
    print(
        "Permutation-eligible identities:",
        len(eligible),
    )
    print(
        "Structurally fixed identities:",
        len(structural_fixed),
    )
    print(
        "No output has been computed yet."
    )

    # -------------------------------------------------------------------------
    # Canonical frozen-fold baseline / observed-result replay
    # -------------------------------------------------------------------------

    baseline_L = fit_oof(
        L,
        y,
        fold_id,
    )

    observed_LG = fit_oof(
        np.hstack([
            L,
            G,
        ]),
        y,
        fold_id,
    )

    observed_delta = (
        observed_LG[
            "macro_f1"
        ]
        - baseline_L[
            "macro_f1"
        ]
    )

    if not np.isclose(
        baseline_L[
            "macro_f1"
        ],
        EXPECTED_PRIMARY_F1_L,
        rtol=0.0,
        atol=1e-12,
    ):
        raise RuntimeError(
            "Frozen L replay does not reproduce the "
            "canonical exploratory macro-F1."
        )

    if not np.isclose(
        observed_LG[
            "macro_f1"
        ],
        EXPECTED_PRIMARY_F1_LG,
        rtol=0.0,
        atol=1e-12,
    ):
        raise RuntimeError(
            "Frozen L+G replay does not reproduce the "
            "canonical exploratory macro-F1."
        )

    if not np.isclose(
        observed_delta,
        EXPECTED_PRIMARY_DELTA,
        rtol=0.0,
        atol=1e-12,
    ):
        raise RuntimeError(
            "Frozen observed delta replay does not "
            "reproduce the canonical exploratory result."
        )

    # L is invariant to RA14 correspondence permutation.
    # Computing it once is algebraically identical to
    # refitting the same deterministic L model 1,000 times.
    baseline_f1 = float(
        baseline_L[
            "macro_f1"
        ]
    )

    baseline_ba = float(
        baseline_L[
            "balanced_accuracy"
        ]
    )

    rng = np.random.default_rng(
        PERMUTATION_MASTER_SEED
    )

    records = []

    for permutation_index in range(
        1,
        N_PERMUTATIONS + 1,
    ):
        (
            G_permuted,
            audit,
        ) = make_permuted_ra14(
            G=G,
            rng=rng,
            blocks=blocks,
            identity_category=identity_category,
            block_size=block_size,
            strata=strata,
            structural_fixed=structural_fixed,
        )

        permuted_LG = fit_oof(
            np.hstack([
                L,
                G_permuted,
            ]),
            y,
            fold_id,
        )

        permuted_delta = (
            permuted_LG[
                "macro_f1"
            ]
            - baseline_f1
        )

        permuted_ba_delta = (
            permuted_LG[
                "balanced_accuracy"
            ]
            - baseline_ba
        )

        records.append({
            "permutation_index":
                permutation_index,
            "master_seed":
                PERMUTATION_MASTER_SEED,
            "permutation_eligible_identities":
                audit[
                    "permutation_eligible_identities"
                ],
            "structurally_fixed_identities":
                audit[
                    "structurally_fixed_identities"
                ],
            "actually_reassigned_identities":
                audit[
                    "actually_reassigned_identities"
                ],
            "all_2300_destination_rows_filled_once":
                audit[
                    "all_2300_destination_rows_filled_once"
                ],
            "all_2300_source_rows_used_once":
                audit[
                    "all_2300_source_rows_used_once"
                ],
            "category_preserved":
                audit[
                    "category_preserved"
                ],
            "block_size_preserved":
                audit[
                    "block_size_preserved"
                ],
            "singleton_strata_fixed":
                audit[
                    "singleton_strata_fixed"
                ],
            "macro_f1_L":
                baseline_f1,
            "macro_f1_L_plus_G_permuted":
                permuted_LG[
                    "macro_f1"
                ],
            "delta_G_given_L":
                float(
                    permuted_delta
                ),
            "balanced_accuracy_L":
                baseline_ba,
            "balanced_accuracy_L_plus_G_permuted":
                permuted_LG[
                    "balanced_accuracy"
                ],
            "delta_balanced_accuracy":
                float(
                    permuted_ba_delta
                ),
            "max_iterations_L_plus_G":
                permuted_LG[
                    "max_iterations"
                ],
            "converged_L_plus_G":
                permuted_LG[
                    "all_converged"
                ],
        })

        if (
            permutation_index % 25
            == 0
        ):
            print(
                "Completed permutation",
                permutation_index,
                "of",
                N_PERMUTATIONS,
            )

    frame = pd.DataFrame(
        records
    )

    deltas = frame[
        "delta_G_given_L"
    ].to_numpy(
        dtype=float
    )

    if len(deltas) != (
        N_PERMUTATIONS
    ):
        raise RuntimeError(
            "Permutation count mismatch."
        )

    if not np.isfinite(
        deltas
    ).all():
        raise RuntimeError(
            "Permutation distribution contains "
            "non-finite values."
        )

    empirical_upper_tail = (
        1
        + int(
            np.sum(
                deltas
                >= observed_delta
            )
        )
    ) / (
        1
        + N_PERMUTATIONS
    )

    quantiles = np.quantile(
        deltas,
        [
            0.025,
            0.975,
        ],
    )

    summary = {
        "status":
            STATUS,
        "control":
            "correspondence_permutation",
        "interpretation":
            (
                "Conservative post-outcome correspondence "
                "control; unequal-size singleton identities "
                "remain structurally fixed."
            ),
        "amendment": {
            "path":
                AMENDMENT_REL.as_posix(),
            "commit":
                AMENDMENT_COMMIT,
        },
        "structural_clarification": {
            "path":
                CLARIFICATION_REL.as_posix(),
            "commit":
                CLARIFICATION_COMMIT,
        },
        "execution": chronology,
        "data": {
            "n_rows":
                EXPECTED_ROWS,
            "n_garment_identities":
                EXPECTED_IDENTITIES,
            "n_categories":
                EXPECTED_CATEGORIES,
            "ra14_dimension":
                EXPECTED_RA14_DIM,
            "dino_dimension":
                EXPECTED_DINO_DIM,
            "ra14_sha256":
                data[
                    "ra14_sha256"
                ],
            "dino_sha256":
                data[
                    "dino_sha256"
                ],
            "dino_row_map_sha256":
                data[
                    "dino_rows_sha256"
                ],
            "fold_array_sha256":
                data[
                    "fold_array_sha256"
                ],
        },
        "model": {
            "classifier":
                "LogisticRegression",
            "penalty":
                "l2",
            "C":
                1.0,
            "solver":
                "lbfgs",
            "max_iter":
                5000,
            "classifier_seed":
                CLASSIFIER_SEED,
            "scaler":
                "training-fold StandardScaler",
        },
        "representations": {
            "L":
                "frozen DINOv2 384-D representation",
            "G":
                "frozen RA14 14-D representation",
            "L_plus_G":
                "concatenated frozen DINOv2 + RA14",
        },
        "metric_definition": {
            "primary":
                (
                    "pooled out-of-fold macro-F1; "
                    "Delta_G|L = F1(L+G) - F1(L)"
                ),
            "secondary":
                (
                    "pooled out-of-fold balanced accuracy "
                    "difference"
                ),
        },
        "permutation_design": {
            "n_permutations":
                N_PERMUTATIONS,
            "master_seed":
                PERMUTATION_MASTER_SEED,
            "rng_scheme":
                (
                    "one numpy.random.default_rng(master_seed); "
                    "permutations consumed sequentially in "
                    "sorted (category, block_size) stratum order"
                ),
            "strata":
                "(category, identity_block_size)",
            "within_identity_row_order":
                "ascending authoritative row index",
            "permutation_eligible_identities":
                len(eligible),
            "structurally_fixed_identities":
                len(structural_fixed),
            "structurally_fixed_identity_ids":
                sorted(
                    structural_fixed
                ),
            "L_baseline_computed_once":
                True,
            "L_baseline_reason":
                (
                    "L and frozen folds are invariant to "
                    "RA14 correspondence permutation."
                ),
        },
        "observed_exploratory_result": {
            "macro_f1_L":
                json_safe_float(
                    baseline_f1
                ),
            "macro_f1_L_plus_G":
                json_safe_float(
                    observed_LG[
                        "macro_f1"
                    ]
                ),
            "delta_G_given_L":
                json_safe_float(
                    observed_delta
                ),
        },
        "permutation_distribution": {
            "mean":
                json_safe_float(
                    np.mean(
                        deltas
                    )
                ),
            "median":
                json_safe_float(
                    np.median(
                        deltas
                    )
                ),
            "quantile_0_025":
                json_safe_float(
                    quantiles[0]
                ),
            "quantile_0_975":
                json_safe_float(
                    quantiles[1]
                ),
            "quantile_method":
                "numpy default linear",
            "empirical_upper_tail_probability":
                json_safe_float(
                    empirical_upper_tail
                ),
            "empirical_probability_formula":
                (
                    "(1 + count(T_perm >= T_obs)) "
                    "/ (1 + B)"
                ),
        },
        "scientific_boundary": {
            "frozen_mechanical_gate":
                "FAIL",
            "experiment08_status":
                "EXPLORATORY / POST-OUTCOME",
            "confirmatory_claim_permitted":
                False,
            "mechanical_validity_restored":
                False,
        },
    }

    (
        csv_sha,
        summary_sha,
    ) = write_evidence_pair(
        frame,
        CORRESPONDENCE_CSV,
        CORRESPONDENCE_SUMMARY,
        summary,
    )

    print()
    print(
        "CORRESPONDENCE CONTROL COMPLETE"
    )
    print(
        "Evidence CSV SHA-256:",
        csv_sha,
    )
    print(
        "Summary JSON SHA-256:",
        summary_sha,
    )
    print(
        "STATUS:",
        STATUS,
    )


# =============================================================================
# REPEATED GROUPED PARTITIONS
# =============================================================================

def make_repeated_fold_assignment(
    y: np.ndarray,
    groups: np.ndarray,
    seed: int,
) -> tuple[
    np.ndarray,
    dict,
]:

    splitter = StratifiedGroupKFold(
        n_splits=5,
        shuffle=True,
        random_state=seed,
    )

    dummy_X = np.zeros(
        (
            len(y),
            1,
        ),
        dtype=np.uint8,
    )

    splits = list(
        splitter.split(
            dummy_X,
            y,
            groups,
        )
    )

    if len(splits) != 5:
        raise RuntimeError(
            f"Seed {seed}: expected exactly five folds."
        )

    assignment = np.full(
        len(y),
        -1,
        dtype=int,
    )

    fold_row_counts = []
    fold_identity_counts = []

    for (
        fold,
        (
            train_idx,
            test_idx,
        ),
    ) in enumerate(
        splits
    ):
        if (
            assignment[
                test_idx
            ]
            != -1
        ).any():
            raise RuntimeError(
                f"Seed {seed}: row assigned to "
                "multiple test folds."
            )

        train_ids = set(
            groups[
                train_idx
            ]
        )

        test_ids = set(
            groups[
                test_idx
            ]
        )

        if train_ids & test_ids:
            raise RuntimeError(
                f"Seed {seed}, fold {fold}: "
                "group leakage."
            )

        assignment[
            test_idx
        ] = fold

        fold_row_counts.append(
            int(
                len(
                    test_idx
                )
            )
        )

        fold_identity_counts.append(
            int(
                len(
                    test_ids
                )
            )
        )

    if (
        assignment == -1
    ).any():
        raise RuntimeError(
            f"Seed {seed}: not all rows received "
            "a test-fold assignment."
        )

    if set(
        np.unique(
            assignment
        ).tolist()
    ) != {
        0,
        1,
        2,
        3,
        4,
    }:
        raise RuntimeError(
            f"Seed {seed}: unexpected fold labels."
        )

    unique_groups = np.unique(
        groups
    )

    if len(
        unique_groups
    ) != EXPECTED_IDENTITIES:
        raise RuntimeError(
            "Unexpected garment identity count."
        )

    for garment_id in unique_groups:
        idx = np.flatnonzero(
            groups == garment_id
        )

        folds = np.unique(
            assignment[
                idx
            ]
        )

        if len(folds) != 1:
            raise RuntimeError(
                f"Seed {seed}: identity {garment_id} "
                "spans test folds."
            )

    if len(
        np.unique(
            y
        )
    ) != EXPECTED_CATEGORIES:
        raise RuntimeError(
            f"Seed {seed}: complete-dataset category "
            "count changed."
        )

    audit = {
        "seed":
            int(seed),
        "all_2300_rows_assigned_once":
            True,
        "all_230_identities_in_one_test_fold":
            True,
        "zero_group_overlap_each_fold":
            True,
        "n_folds":
            5,
        "n_categories_complete_dataset":
            EXPECTED_CATEGORIES,
        "fold_row_counts":
            fold_row_counts,
        "fold_identity_counts":
            fold_identity_counts,
        "fold_assignment_sha256":
            sha256_int_array(
                assignment
            ),
    }

    return (
        assignment,
        audit,
    )


def run_repeated_partition_control(
    data: dict,
    chronology: dict,
) -> None:

    ensure_output_absent(
        REPEATED_CSV,
        REPEATED_SUMMARY,
    )

    G = data["G"]
    L = data["L"]
    y = data["y"]
    groups = data["groups"]
    canonical_fold_id = data[
        "fold_id"
    ]

    representations = {
        "L":
            L,
        "G":
            G,
        "L_plus_G":
            np.hstack([
                L,
                G,
            ]),
    }

    print("=" * 88)
    print(
        "EXPERIMENT 08 — POST-OUTCOME "
        "REPEATED GROUPED-PARTITION CONTROL"
    )
    print("=" * 88)
    print(
        "Status: POST_OUTCOME_EXPLORATORY_ONLY"
    )
    print(
        "Partition seeds:",
        REPEATED_PARTITION_SEEDS[
            0
        ],
        "through",
        REPEATED_PARTITION_SEEDS[
            -1
        ],
    )
    print(
        "No partition will be accepted or rejected "
        "using predictive outcomes."
    )

    records = []

    for repeat_index, seed in enumerate(
        REPEATED_PARTITION_SEEDS,
        start=1,
    ):
        (
            fold_assignment,
            audit,
        ) = make_repeated_fold_assignment(
            y,
            groups,
            seed,
        )

        metrics = {}

        for (
            representation_name,
            X,
        ) in representations.items():
            metrics[
                representation_name
            ] = fit_oof(
                X,
                y,
                fold_assignment,
            )

        delta_f1 = (
            metrics[
                "L_plus_G"
            ][
                "macro_f1"
            ]
            - metrics[
                "L"
            ][
                "macro_f1"
            ]
        )

        delta_ba = (
            metrics[
                "L_plus_G"
            ][
                "balanced_accuracy"
            ]
            - metrics[
                "L"
            ][
                "balanced_accuracy"
            ]
        )

        records.append({
            "repeat_index":
                repeat_index,
            "seed":
                seed,
            "fold_assignment_sha256":
                audit[
                    "fold_assignment_sha256"
                ],
            "matches_canonical_fold_array_exactly":
                bool(
                    np.array_equal(
                        fold_assignment,
                        canonical_fold_id,
                    )
                ),
            "fold_row_counts":
                json.dumps(
                    audit[
                        "fold_row_counts"
                    ]
                ),
            "fold_identity_counts":
                json.dumps(
                    audit[
                        "fold_identity_counts"
                    ]
                ),
            "all_2300_rows_assigned_once":
                audit[
                    "all_2300_rows_assigned_once"
                ],
            "all_230_identities_in_one_test_fold":
                audit[
                    "all_230_identities_in_one_test_fold"
                ],
            "zero_group_overlap_each_fold":
                audit[
                    "zero_group_overlap_each_fold"
                ],
            "macro_f1_L":
                metrics[
                    "L"
                ][
                    "macro_f1"
                ],
            "macro_f1_G":
                metrics[
                    "G"
                ][
                    "macro_f1"
                ],
            "macro_f1_L_plus_G":
                metrics[
                    "L_plus_G"
                ][
                    "macro_f1"
                ],
            "delta_G_given_L":
                float(
                    delta_f1
                ),
            "balanced_accuracy_L":
                metrics[
                    "L"
                ][
                    "balanced_accuracy"
                ],
            "balanced_accuracy_G":
                metrics[
                    "G"
                ][
                    "balanced_accuracy"
                ],
            "balanced_accuracy_L_plus_G":
                metrics[
                    "L_plus_G"
                ][
                    "balanced_accuracy"
                ],
            "delta_balanced_accuracy":
                float(
                    delta_ba
                ),
            "max_iterations_L":
                metrics[
                    "L"
                ][
                    "max_iterations"
                ],
            "max_iterations_G":
                metrics[
                    "G"
                ][
                    "max_iterations"
                ],
            "max_iterations_L_plus_G":
                metrics[
                    "L_plus_G"
                ][
                    "max_iterations"
                ],
            "converged_L":
                metrics[
                    "L"
                ][
                    "all_converged"
                ],
            "converged_G":
                metrics[
                    "G"
                ][
                    "all_converged"
                ],
            "converged_L_plus_G":
                metrics[
                    "L_plus_G"
                ][
                    "all_converged"
                ],
        })

        print(
            "Completed repeated partition",
            repeat_index,
            "of",
            len(
                REPEATED_PARTITION_SEEDS
            ),
        )

    frame = pd.DataFrame(
        records
    )

    primary_deltas = frame[
        "delta_G_given_L"
    ].to_numpy(
        dtype=float
    )

    ba_deltas = frame[
        "delta_balanced_accuracy"
    ].to_numpy(
        dtype=float
    )

    if len(
        primary_deltas
    ) != 20:
        raise RuntimeError(
            "Repeated-partition result count "
            "is not 20."
        )

    if not np.isfinite(
        primary_deltas
    ).all():
        raise RuntimeError(
            "Repeated-partition primary results "
            "contain non-finite values."
        )

    if not np.isfinite(
        ba_deltas
    ).all():
        raise RuntimeError(
            "Repeated-partition BA results "
            "contain non-finite values."
        )

    primary_quantiles = np.quantile(
        primary_deltas,
        [
            0.025,
            0.975,
        ],
    )

    unique_partition_hashes = int(
        frame[
            "fold_assignment_sha256"
        ].nunique()
    )

    summary = {
        "status":
            STATUS,
        "control":
            "repeated_identity_grouped_partitions",
        "amendment": {
            "path":
                AMENDMENT_REL.as_posix(),
            "commit":
                AMENDMENT_COMMIT,
        },
        "structural_clarification": {
            "path":
                CLARIFICATION_REL.as_posix(),
            "commit":
                CLARIFICATION_COMMIT,
        },
        "execution":
            chronology,
        "data": {
            "n_rows":
                EXPECTED_ROWS,
            "n_garment_identities":
                EXPECTED_IDENTITIES,
            "n_categories":
                EXPECTED_CATEGORIES,
            "ra14_dimension":
                EXPECTED_RA14_DIM,
            "dino_dimension":
                EXPECTED_DINO_DIM,
            "ra14_sha256":
                data[
                    "ra14_sha256"
                ],
            "dino_sha256":
                data[
                    "dino_sha256"
                ],
            "dino_row_map_sha256":
                data[
                    "dino_rows_sha256"
                ],
            "canonical_fold_array_sha256":
                data[
                    "fold_array_sha256"
                ],
        },
        "partition_algorithm": {
            "class":
                "sklearn.model_selection.StratifiedGroupKFold",
            "n_splits":
                5,
            "shuffle":
                True,
            "random_state":
                "seed",
            "stratification_label":
                "category",
            "group":
                "garment_id",
            "seeds":
                list(
                    REPEATED_PARTITION_SEEDS
                ),
            "n_repeats":
                len(
                    REPEATED_PARTITION_SEEDS
                ),
            "outcome_dependent_partition_selection":
                False,
            "manual_posthoc_fold_repair":
                False,
            "unique_exact_partition_hashes":
                unique_partition_hashes,
        },
        "model": {
            "classifier":
                "LogisticRegression",
            "penalty":
                "l2",
            "C":
                1.0,
            "solver":
                "lbfgs",
            "max_iter":
                5000,
            "classifier_seed":
                CLASSIFIER_SEED,
            "scaler":
                "training-fold StandardScaler",
        },
        "representations": {
            "L":
                "frozen DINOv2 384-D representation",
            "G":
                "frozen RA14 14-D representation",
            "L_plus_G":
                "concatenated frozen DINOv2 + RA14",
        },
        "metric_definition": {
            "primary":
                (
                    "pooled out-of-fold macro-F1; "
                    "Delta_G|L = F1(L+G) - F1(L)"
                ),
            "secondary":
                (
                    "pooled out-of-fold balanced accuracy "
                    "difference"
                ),
        },
        "canonical_frozen_partition_result": {
            "reported_separately":
                True,
            "macro_f1_L":
                EXPECTED_PRIMARY_F1_L,
            "macro_f1_L_plus_G":
                EXPECTED_PRIMARY_F1_LG,
            "delta_G_given_L":
                EXPECTED_PRIMARY_DELTA,
        },
        "primary_delta_distribution": {
            "values":
                [
                    json_safe_float(
                        value
                    )
                    for value
                    in primary_deltas
                ],
            "mean":
                json_safe_float(
                    np.mean(
                        primary_deltas
                    )
                ),
            "median":
                json_safe_float(
                    np.median(
                        primary_deltas
                    )
                ),
            "minimum":
                json_safe_float(
                    np.min(
                        primary_deltas
                    )
                ),
            "maximum":
                json_safe_float(
                    np.max(
                        primary_deltas
                    )
                ),
            "standard_deviation":
                json_safe_float(
                    np.std(
                        primary_deltas,
                        ddof=1,
                    )
                ),
            "standard_deviation_ddof":
                1,
            "quantile_0_025":
                json_safe_float(
                    primary_quantiles[
                        0
                    ]
                ),
            "quantile_0_975":
                json_safe_float(
                    primary_quantiles[
                        1
                    ]
                ),
            "quantile_method":
                "numpy default linear",
            "n_positive":
                int(
                    np.sum(
                        primary_deltas
                        > 0.0
                    )
                ),
        },
        "balanced_accuracy_delta_values": [
            json_safe_float(
                value
            )
            for value
            in ba_deltas
        ],
        "scientific_boundary": {
            "frozen_mechanical_gate":
                "FAIL",
            "experiment08_status":
                "EXPLORATORY / POST-OUTCOME",
            "confirmatory_claim_permitted":
                False,
            "canonical_frozen_partition_replaced":
                False,
        },
    }

    (
        csv_sha,
        summary_sha,
    ) = write_evidence_pair(
        frame,
        REPEATED_CSV,
        REPEATED_SUMMARY,
        summary,
    )

    print()
    print(
        "REPEATED-PARTITION CONTROL COMPLETE"
    )
    print(
        "Evidence CSV SHA-256:",
        csv_sha,
    )
    print(
        "Summary JSON SHA-256:",
        summary_sha,
    )
    print(
        "STATUS:",
        STATUS,
    )


# =============================================================================
# MAIN
# =============================================================================

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run prospectively specified post-outcome "
            "Experiment 08 predictive controls."
        )
    )

    parser.add_argument(
        "--control",
        required=True,
        choices=[
            "correspondence",
            "repeated",
            "all",
        ],
        help=(
            "Control to execute. Execution is refused "
            "unless this runner is already committed."
        ),
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    chronology = verify_execution_chronology()

    data = load_frozen_inputs()

    print("=" * 88)
    print(
        "EXPERIMENT 08 POST-OUTCOME CONTROL "
        "PROVENANCE VERIFICATION"
    )
    print("=" * 88)
    print(
        "Amendment commit:",
        AMENDMENT_COMMIT,
    )
    print(
        "Clarification commit:",
        CLARIFICATION_COMMIT,
    )
    print(
        "Runner source commit:",
        chronology[
            "runner_source_commit"
        ],
    )
    print(
        "Execution HEAD:",
        chronology[
            "execution_head_commit"
        ],
    )
    print(
        "Rows:",
        EXPECTED_ROWS,
    )
    print(
        "Identities:",
        EXPECTED_IDENTITIES,
    )
    print(
        "Categories:",
        EXPECTED_CATEGORIES,
    )
    print(
        "STATUS:",
        STATUS,
    )

    if args.control in {
        "correspondence",
        "all",
    }:
        run_correspondence_control(
            data,
            chronology,
        )

    if args.control in {
        "repeated",
        "all",
    }:
        run_repeated_partition_control(
            data,
            chronology,
        )


if __name__ == "__main__":
    main()
