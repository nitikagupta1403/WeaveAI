from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, f1_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


# =============================================================================
# FROZEN CONSTANTS
# =============================================================================

E8 = Path(__file__).resolve().parent
PAPER_ROOT = E8.parent.parent

RA14_PATH = E8 / "experiment08_ra14_features.npy"
RA14_ROW_MANIFEST = E8 / "experiment08_ra14_source_manifest.csv"
RA14_LOCK = E8 / "experiment08_ra14_manifest.json"
DINO_LOCK = E8 / "experiment08_dinov2_feature_lock.json"
PREFLIGHT_PATH = E8 / "preflight.py"

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

EXPECTED_ROWS = 2300
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


# =============================================================================
# HELPERS
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


def load_preflight_module():
    spec = importlib.util.spec_from_file_location(
        "experiment08_preflight",
        PREFLIGHT_PATH,
    )

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def make_classifier():
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


# =============================================================================
# PRE-OUTCOME GATE
# =============================================================================

print("=" * 88)
print("EXPERIMENT 08 — PRIMARY COMPARISON")
print("=" * 88)

print("\nPRE-OUTCOME VERIFICATION")
print("-" * 88)

for required_path in [
    RA14_PATH,
    RA14_ROW_MANIFEST,
    RA14_LOCK,
    DINO_LOCK,
    DINO_PATH,
    DINO_ROWS,
    PREFLIGHT_PATH,
]:
    if not required_path.is_file():
        raise RuntimeError(
            f"Required frozen artifact missing: {required_path}"
        )

ra14_file_sha = sha256_file(RA14_PATH)
dino_file_sha = sha256_file(DINO_PATH)
dino_row_sha = sha256_file(DINO_ROWS)

if ra14_file_sha != EXPECTED_RA14_FILE_SHA:
    raise RuntimeError(
        f"RA14 NPY hash mismatch: {ra14_file_sha}"
    )

if dino_file_sha != EXPECTED_DINO_FILE_SHA:
    raise RuntimeError(
        f"DINO NPY hash mismatch: {dino_file_sha}"
    )

if dino_row_sha != EXPECTED_DINO_ROW_SHA:
    raise RuntimeError(
        f"DINO row-map hash mismatch: {dino_row_sha}"
    )

ra14_lock = json.loads(
    RA14_LOCK.read_text(encoding="utf-8")
)

dino_lock = json.loads(
    DINO_LOCK.read_text(encoding="utf-8")
)

if ra14_lock["classifier_fitted"] is not False:
    raise RuntimeError(
        "RA14 lock does not preserve pre-outcome boundary."
    )

if ra14_lock["predictive_outcome_computed"] is not False:
    raise RuntimeError(
        "RA14 lock already reports a predictive outcome."
    )

if dino_lock["classifier_fitted"] is not False:
    raise RuntimeError(
        "DINO lock does not preserve pre-outcome boundary."
    )

if dino_lock["predictive_outcome_computed"] is not False:
    raise RuntimeError(
        "DINO lock already reports a predictive outcome."
    )


# =============================================================================
# LOAD REPRESENTATIONS
# =============================================================================

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


# =============================================================================
# AUTHORITATIVE CORRECTED MAP
# =============================================================================

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

observed_fold_sha = (
    corrected_audit[
        "experiment08_fold_array_sha256"
    ]
)

if observed_fold_sha != EXPECTED_CORRECTED_FOLD_SHA:
    raise RuntimeError(
        "Corrected Experiment-08 fold hash mismatch: "
        f"{observed_fold_sha}"
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


# =============================================================================
# ROW CORRESPONDENCE
# =============================================================================

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
    .map(pf.normalized_relative_path)
    .tolist()
)

if ra14_rows["row_index"].tolist() != list(
    range(EXPECTED_ROWS)
):
    raise RuntimeError(
        "RA14 row_index is not 0..2299."
    )

if dino_rows["row_index"].tolist() != list(
    range(EXPECTED_ROWS)
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


# =============================================================================
# LABELS AND FOLDS
# =============================================================================

y = rows["category"].astype(str).to_numpy()
fold_id = rows["fold_id"].to_numpy(dtype=int)

if len(np.unique(y)) != 23:
    raise RuntimeError(
        "Expected exactly 23 categories."
    )

if rows["garment_id"].nunique() != 230:
    raise RuntimeError(
        "Expected exactly 230 garment identities."
    )

for fold in range(5):

    test_mask = fold_id == fold
    train_mask = ~test_mask

    test_ids = set(
        rows.loc[
            test_mask,
            "garment_id",
        ]
    )

    train_ids = set(
        rows.loc[
            train_mask,
            "garment_id",
        ]
    )

    if len(test_ids) != 46:
        raise RuntimeError(
            f"Fold {fold}: expected 46 test identities."
        )

    if len(train_ids) != 184:
        raise RuntimeError(
            f"Fold {fold}: expected 184 train identities."
        )

    if train_ids & test_ids:
        raise RuntimeError(
            f"Fold {fold}: identity leakage detected."
        )


# =============================================================================
# LOCKED PRIMARY REPRESENTATIONS
# =============================================================================

representations = {
    "L": L,
    "L_plus_G": np.hstack([
        L,
        G,
    ]),
}

oof_predictions = {
    name: np.empty(
        EXPECTED_ROWS,
        dtype=object,
    )
    for name in representations
}

fold_records = []


# =============================================================================
# FIRST OUTCOME-PRODUCING SECTION
# =============================================================================

print("\nALL PRE-OUTCOME GATES PASSED.")
print("-" * 88)

print(
    "Crossing predictive-outcome boundary now."
)

for fold in range(5):

    test_idx = np.flatnonzero(
        fold_id == fold
    )

    train_idx = np.flatnonzero(
        fold_id != fold
    )

    for representation_name, X in (
        representations.items()
    ):

        model = make_classifier()

        model.fit(
            X[train_idx],
            y[train_idx],
        )

        pred = model.predict(
            X[test_idx]
        )

        oof_predictions[
            representation_name
        ][test_idx] = pred

        fold_records.append({
            "fold":
                fold,

            "representation":
                representation_name,

            "train_rows":
                len(train_idx),

            "test_rows":
                len(test_idx),

            "n_features":
                X.shape[1],

            "macro_f1":
                f1_score(
                    y[test_idx],
                    pred,
                    average="macro",
                ),

            "balanced_accuracy":
                balanced_accuracy_score(
                    y[test_idx],
                    pred,
                ),

            "iterations":
                int(
                    np.max(
                        model.named_steps[
                            "classifier"
                        ].n_iter_
                    )
                ),

            "converged":
                bool(
                    np.max(
                        model.named_steps[
                            "classifier"
                        ].n_iter_
                    )
                    < 5000
                ),
        })


# =============================================================================
# POOLED OOF PRIMARY ESTIMAND
# =============================================================================

pooled_records = []

for name, prediction in (
    oof_predictions.items()
):

    pooled_records.append({
        "representation":
            name,

        "n_features":
            representations[name].shape[1],

        "macro_f1":
            f1_score(
                y,
                prediction,
                average="macro",
            ),

        "balanced_accuracy":
            balanced_accuracy_score(
                y,
                prediction,
            ),
    })

pooled = pd.DataFrame(
    pooled_records
)

fold_metrics = pd.DataFrame(
    fold_records
)

f1_L = float(
    pooled.loc[
        pooled["representation"] == "L",
        "macro_f1",
    ].iloc[0]
)

f1_LG = float(
    pooled.loc[
        pooled["representation"]
        == "L_plus_G",
        "macro_f1",
    ].iloc[0]
)

delta = f1_LG - f1_L


# =============================================================================
# SAVE PRIMARY OUTPUTS
# =============================================================================

evidence = (
    PAPER_ROOT
    / "evidence"
    / "Experiment_08"
)

evidence.mkdir(
    parents=True,
    exist_ok=True,
)

fold_metrics_path = (
    evidence
    / "experiment08_fold_metrics.csv"
)

primary_results_path = (
    evidence
    / "experiment08_primary_results.csv"
)

oof_path = (
    evidence
    / "experiment08_oof_predictions.csv"
)

decision_path = (
    evidence
    / "experiment08_primary_point_estimate.json"
)

fold_metrics.to_csv(
    fold_metrics_path,
    index=False,
)

pooled.to_csv(
    primary_results_path,
    index=False,
)

oof_frame = pd.DataFrame({
    "row_index":
        np.arange(EXPECTED_ROWS),

    "relative_path":
        authoritative_paths,

    "category":
        y,

    "garment_id":
        rows[
            "garment_id"
        ].astype(str).to_numpy(),

    "fold_id":
        fold_id,

    "prediction_L":
        oof_predictions["L"],

    "prediction_L_plus_G":
        oof_predictions[
            "L_plus_G"
        ],
})

oof_frame.to_csv(
    oof_path,
    index=False,
)

decision = {
    "stage":
        "PRIMARY_POINT_ESTIMATE",

    "primary_estimand":
        "macro_F1(L_plus_G) - macro_F1(L)",

    "macro_f1_L":
        f1_L,

    "macro_f1_L_plus_G":
        f1_LG,

    "delta_G_given_L":
        delta,

    "identity_bootstrap_completed":
        False,

    "inferential_claim_permitted":
        False,

    "classifier_seed":
        CLASSIFIER_SEED,

    "fold_array_sha256":
        observed_fold_sha,

    "classifier":
        {
            "scaler":
                "training-fold StandardScaler",

            "model":
                "multinomial logistic regression",

            "penalty":
                "l2",

            "C":
                1.0,

            "solver":
                "lbfgs",

            "max_iter":
                5000,
        },
}

decision_path.write_text(
    json.dumps(
        decision,
        indent=2,
        sort_keys=True,
    )
    + "\n",
    encoding="utf-8",
)


# =============================================================================
# DISPLAY
# =============================================================================

print("\n" + "=" * 88)
print("PRIMARY POINT ESTIMATE")
print("=" * 88)

print(
    pooled.to_string(
        index=False,
        float_format=lambda x: f"{x:.6f}",
    )
)

print(
    "\nDelta G|L = "
    f"{delta:+.6f} macro-F1"
)

print("\nCONVERGENCE")
print("-" * 88)

print(
    fold_metrics[
        [
            "fold",
            "representation",
            "iterations",
            "converged",
        ]
    ].to_string(
        index=False
    )
)

print("\nSaved:")
print(" ", primary_results_path)
print(" ", fold_metrics_path)
print(" ", oof_path)
print(" ", decision_path)

print("\nIMPORTANT")
print("-" * 88)
print(
    "This is the primary point estimate only."
)
print(
    "No inferential claim is permitted until the "
    "frozen category-stratified garment-identity "
    "bootstrap is completed."
)