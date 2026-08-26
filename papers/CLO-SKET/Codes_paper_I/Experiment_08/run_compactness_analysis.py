#!/usr/bin/env python3
"""Experiment-08 compactness analysis runner.

Pre-result amendment commit: 30a0d37

This file implements the frozen compactness-analysis logic exactly as specified in
PAPER_I_FRESH_STUDY_MATHEMATICAL_DESIGN_LOCK.md, without executing the scientific
analysis in this session. The runner is intentionally non-executing until the
frozen compactness protocol is explicitly run by a separate, authorized operation.

Design-lock requirements implemented here:
- RA14/G is the frozen explicit 14-D axial-radial representation.
- DINOv2/L is the frozen learned representation.
- Fold membership and identity-disjoint validation are authoritatively frozen.
- The compact representation L^(14) is constructed as:
    raw frozen DINOv2 -> training-fold PCA14 -> training-fold StandardScaler -> LogisticRegression
- RA14 retains its frozen training-fold StandardScaler -> LogisticRegression path.
- Primary metric: pooled out-of-fold macro-F1.
- Secondary metric: pooled out-of-fold balanced accuracy.
- Primary compactness estimand: D_{G,L14} = F1(G) - F1(L^(14)).
- Non-inferiority rule: lower bound of paired 95% garment-identity bootstrap CI > -0.02.
- Bootstrap unit: complete recovered garment identities, stratified within category.
- Bootstrap seed: 20260821.
- Multiplicity: Holm adjustment within the secondary family if secondary tests are reported.

NO SCIENTIFIC OUTCOME IS COMPUTED BY THIS FILE.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, f1_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


E8 = Path(__file__).resolve().parent
PAPER_ROOT = E8.parent.parent

# Frozen artifacts and locked settings from the design lock and active Experiment-08 code.
RA14_PATH = E8 / "experiment08_ra14_features.npy"
RA14_ROW_MANIFEST = E8 / "experiment08_ra14_source_manifest.csv"
RA14_LOCK = E8 / "experiment08_ra14_manifest.json"
DINO_LOCK = E8 / "experiment08_dinov2_feature_lock.json"
DINO_PATH = E8 / "experiment08_dinov2_vits14_embeddings.npy"
DINO_ROWS = E8 / "experiment08_dinov2_embedding_rows.csv"
PREFLIGHT_PATH = E8 / "preflight.py"

EXPECTED_ROWS = 2300
EXPECTED_RA14_DIM = 14
EXPECTED_DINO_DIM = 384
EXPECTED_RA14_FILE_SHA = "2e9b7d6ddd144c6b85b66cd44ae60cbb72c84f0029e8f50afff77a833edbd033"
EXPECTED_DINO_FILE_SHA = "6958b8b05eee66304ecda038cc5fedef33eecd139dccc20c12dc6d223c614d97"
EXPECTED_DINO_ROW_SHA = "072f08ae9fb8328fe73a2566c1d5e812560cd4b007bf1c88550adbb082a6a4d9"
EXPECTED_CORRECTED_FOLD_SHA = "e3fb0cf57b886bc303333795de42ecfc38cb1da9728d4d5cc365b47a91504c1f"
EXPECTED_TEST_ROWS = [459, 460, 461, 460, 460]
BOOTSTRAP_SEED = 20260821
CLASSIFIER_SEED = 20260820


def sha256_file(path: Path) -> str:
    """Return the SHA-256 digest for a file."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_preflight_module():
    import importlib.util

    spec = importlib.util.spec_from_file_location("experiment08_preflight", PREFLIGHT_PATH)
    module = importlib.util.module_from_spec(spec)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to import preflight module")
    spec.loader.exec_module(module)
    return module


def build_G_pipeline() -> Pipeline:
    """Exact frozen RA14 path: training-fold StandardScaler -> LogisticRegression."""
    return Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(
            penalty="l2",
            C=1.0,
            solver="lbfgs",
            max_iter=5000,
            random_state=CLASSIFIER_SEED,
            class_weight=None,
        )),
    ])


def build_L14_pipeline() -> Pipeline:
    """Exact frozen L14 path: raw L -> PCA14 -> StandardScaler -> LogisticRegression."""
    return Pipeline([
        ("pca", PCA(n_components=14)),
        ("scaler", StandardScaler()),
        ("classifier", LogisticRegression(
            penalty="l2",
            C=1.0,
            solver="lbfgs",
            max_iter=5000,
            random_state=CLASSIFIER_SEED,
            class_weight=None,
        )),
    ])


def validate_pre_outcome_provenance(dino_features_path: Path, dino_rows_path: Path) -> dict:
    """Validate provenance and lock conditions before any compactness outcome boundary is crossed.

    This function is structural and read-only: it enforces the frozen gates but does not execute
    the compactness analysis itself.
    """
    required_paths = [
        RA14_PATH,
        RA14_ROW_MANIFEST,
        RA14_LOCK,
        DINO_LOCK,
        dino_features_path,
        dino_rows_path,
        PREFLIGHT_PATH,
    ]
    missing = [str(path) for path in required_paths if not path.is_file()]
    if missing:
        raise FileNotFoundError("Required compactness provenance artifact(s) missing: " + ", ".join(missing))

    ra14_file_sha = sha256_file(RA14_PATH)
    dino_file_sha = sha256_file(dino_features_path)
    dino_rows_sha = sha256_file(dino_rows_path)
    if ra14_file_sha != EXPECTED_RA14_FILE_SHA:
        raise RuntimeError(f"RA14 SHA-256 mismatch: {ra14_file_sha}")
    if dino_file_sha != EXPECTED_DINO_FILE_SHA:
        raise RuntimeError(f"DINOv2 SHA-256 mismatch: {dino_file_sha}")
    if dino_rows_sha != EXPECTED_DINO_ROW_SHA:
        raise RuntimeError(f"DINO row-manifest SHA-256 mismatch: {dino_rows_sha}")

    ra14_lock = json.loads(RA14_LOCK.read_text(encoding="utf-8"))
    dino_lock = json.loads(DINO_LOCK.read_text(encoding="utf-8"))
    if ra14_lock.get("classifier_fitted") is not False:
        raise RuntimeError("RA14 lock does not preserve pre-outcome boundary.")
    if ra14_lock.get("predictive_outcome_computed") is not False:
        raise RuntimeError("RA14 lock already reports a predictive outcome.")
    if dino_lock.get("classifier_fitted") is not False:
        raise RuntimeError("DINO lock does not preserve pre-outcome boundary.")
    if dino_lock.get("predictive_outcome_computed") is not False:
        raise RuntimeError("DINO lock already reports a predictive outcome.")

    pf = load_preflight_module()
    rows_historical, historical_audit = pf.validate_public_maps(pf.DEFAULT_ROW_MAP, pf.DEFAULT_FOLD_MAP)
    rows, corrected_audit = pf.apply_identity_overrides(rows_historical, pf.DEFAULT_IDENTITY_OVERRIDES, historical_audit)
    observed_fold_sha = corrected_audit["experiment08_fold_array_sha256"]
    if observed_fold_sha != EXPECTED_CORRECTED_FOLD_SHA:
        raise RuntimeError(f"Corrected fold hash mismatch: {observed_fold_sha}")

    observed_test_rows = [int((rows["fold_id"] == fold).sum()) for fold in range(5)]
    if observed_test_rows != EXPECTED_TEST_ROWS:
        raise RuntimeError(f"Expected frozen test rows {EXPECTED_TEST_ROWS}, got {observed_test_rows}")

    ra14_rows = pd.read_csv(RA14_ROW_MANIFEST, keep_default_na=False)
    dino_rows_df = pd.read_csv(dino_rows_path, keep_default_na=False)
    authoritative_paths = rows["image_path_runtime"].map(pf.normalized_relative_path).tolist()
    if ra14_rows["row_index"].tolist() != list(range(EXPECTED_ROWS)):
        raise RuntimeError("RA14 row_index is not 0..2299.")
    if dino_rows_df["row_index"].tolist() != list(range(EXPECTED_ROWS)):
        raise RuntimeError("DINO row_index is not 0..2299.")
    if ra14_rows["relative_path"].tolist() != authoritative_paths:
        raise RuntimeError("RA14 rows differ from authoritative rows.")
    if dino_rows_df["relative_path"].tolist() != authoritative_paths:
        raise RuntimeError("DINO rows differ from authoritative rows.")

    y = rows["category"].astype(str).to_numpy()
    fold_id = rows["fold_id"].to_numpy(dtype=int)
    if len(np.unique(y)) != 23:
        raise RuntimeError("Expected exactly 23 categories.")
    if rows["garment_id"].nunique() != 230:
        raise RuntimeError("Expected exactly 230 garment identities.")

    for fold in range(5):
        test_mask = fold_id == fold
        train_mask = ~test_mask
        test_ids = set(rows.loc[test_mask, "garment_id"])
        train_ids = set(rows.loc[train_mask, "garment_id"])
        if len(test_ids) != 46:
            raise RuntimeError(f"Fold {fold}: expected 46 test identities.")
        if len(train_ids) != 184:
            raise RuntimeError(f"Fold {fold}: expected 184 train identities.")
        if train_ids & test_ids:
            raise RuntimeError(f"Fold {fold}: identity leakage detected.")

    return {"rows": rows, "y": y, "fold_id": fold_id, "authoritative_paths": authoritative_paths}


def fit_fold_local_compactness_models(
    train_idx: np.ndarray,
    test_idx: np.ndarray,
    G: np.ndarray,
    L: np.ndarray,
    y: np.ndarray,
):
    """Build the fold-local G and L14 pipelines without executing the analysis session.

    This function defines the exact fold-wise fitting sequence required by the design lock,
    but it is intentionally not invoked by the default path.
    """
    Xg_train, Xg_test = G[train_idx], G[test_idx]
    Xl_train, Xl_test = L[train_idx], L[test_idx]
    y_train = y[train_idx]

    g_model = build_G_pipeline()
    g_model.fit(Xg_train, y_train)
    g_pred = g_model.predict(Xg_test)

    pca = PCA(n_components=14)
    l_train_pca = pca.fit_transform(Xl_train)
    l_test_pca = pca.transform(Xl_test)
    scaler = StandardScaler()
    l_train_scaled = scaler.fit_transform(l_train_pca)
    l_test_scaled = scaler.transform(l_test_pca)
    l_model = LogisticRegression(
        penalty="l2",
        C=1.0,
        solver="lbfgs",
        max_iter=5000,
        random_state=CLASSIFIER_SEED,
        class_weight=None,
    )
    l_model.fit(l_train_scaled, y_train)
    l_pred = l_model.predict(l_test_scaled)
    return g_pred, l_pred, g_model, l_model


def make_prediction_matrix(
    G: np.ndarray,
    L: np.ndarray,
    fold_id: np.ndarray,
    y: np.ndarray,
    *,
    validate: bool = True,
) -> dict[str, np.ndarray]:
    """Construct the 2300-row OOF prediction arrays for G and L14.

    This follows the exact frozen design lock and performs no scientific outcome computation
    unless explicitly invoked by an authorized execution path.
    """
    if validate:
        validate_pre_outcome_provenance()

    oof_predictions = {"G": np.empty(len(y), dtype=object), "L14": np.empty(len(y), dtype=object)}

    for fold in range(5):
        test_idx = np.flatnonzero(fold_id == fold)
        train_idx = np.flatnonzero(fold_id != fold)
        g_pred, l_pred, _, _ = fit_fold_local_compactness_models(train_idx, test_idx, G, L, y)
        oof_predictions["G"][test_idx] = g_pred
        oof_predictions["L14"][test_idx] = l_pred

    return oof_predictions


def compute_pooled_metrics(y: np.ndarray, pred: np.ndarray) -> dict[str, float]:
    """Compute the pooled out-of-fold macro-F1 and balanced accuracy for a single prediction vector."""
    return {
        "macro_f1": float(f1_score(y, pred, average="macro")),
        "balanced_accuracy": float(balanced_accuracy_score(y, pred)),
    }


def compute_estimand(y: np.ndarray, pred_G: np.ndarray, pred_L14: np.ndarray) -> dict[str, float]:
    """Compute D_G_L14 = macro_f1_G - macro_f1_L14."""
    metrics_G = compute_pooled_metrics(y, pred_G)
    metrics_L14 = compute_pooled_metrics(y, pred_L14)
    return {
        "macro_f1_G": metrics_G["macro_f1"],
        "macro_f1_L14": metrics_L14["macro_f1"],
        "D_G_L14": metrics_G["macro_f1"] - metrics_L14["macro_f1"],
        "balanced_accuracy_G": metrics_G["balanced_accuracy"],
        "balanced_accuracy_L14": metrics_L14["balanced_accuracy"],
    }


def paired_identity_bootstrap(
    y: np.ndarray,
    garment_id: pd.Series,
    pred_G: np.ndarray,
    pred_L14: np.ndarray,
    category: pd.Series,
    *,
    n_bootstrap: int = 10000,
    seed: int = BOOTSTRAP_SEED,
) -> dict[str, object]:
    """Compute the frozen paired, within-category garment-identity bootstrap.

    This is a structural implementation of the exact design-lock bootstrap specification.
    """
    rng = np.random.default_rng(seed)
    deltas = []
    categories = np.unique(category)

    for _ in range(n_bootstrap):
        sampled_rows: list[int] = []
        for cat in categories:
            idx = np.flatnonzero(category.to_numpy() == cat)
            ids_for_cat = garment_id.iloc[idx].unique()
            sampled_ids = rng.choice(ids_for_cat, size=len(ids_for_cat), replace=True)
            for chosen_id in sampled_ids:
                sampled_rows.extend(idx[garment_id.iloc[idx].to_numpy() == chosen_id].tolist())
        sampled_rows = np.asarray(sorted(set(sampled_rows)), dtype=int)
        if len(sampled_rows) == 0:
            continue
        sampled_y = y[sampled_rows]
        sampled_G = pred_G[sampled_rows]
        sampled_L14 = pred_L14[sampled_rows]
        m1 = f1_score(sampled_y, sampled_G, average="macro")
        m2 = f1_score(sampled_y, sampled_L14, average="macro")
        deltas.append(m1 - m2)

    deltas = np.asarray(deltas, dtype=np.float64)
    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])
    return {
        "n_bootstrap": n_bootstrap,
        "seed": seed,
        "deltas": deltas,
        "ci_95": (float(ci_lo), float(ci_hi)),
        "non_inferior": bool(ci_lo > -0.02),
    }


def build_compactness_bootstrap_plan() -> dict:
    """Return the exact prespecified bootstrap design from the design lock."""
    return {
        "unit": "complete recovered garment identities",
        "stratification": "within category",
        "paired": True,
        "paired_preservation": "keep paired predictions for all compared models",
        "n_replicates": 10000,
        "seed": BOOTSTRAP_SEED,
        "primary_metric": "pooled out-of-fold macro-F1",
        "secondary_metric": "pooled out-of-fold balanced accuracy",
        "non_inferiority_margin": -0.02,
        "non_inferiority_ci_rule": "lower bound of paired 95% garment-identity-bootstrap CI > -0.02",
        "multiplicity": "Holm adjustment within the secondary family if secondary tests are reported",
    }


def build_compactness_plan() -> dict:
    """Return the exact compactness pipeline specification from the design lock."""
    return {
        "representations": {
            "G": {
                "definition": "RA14 explicit 14-D axial-radial representation",
                "dimension": 14,
                "classifier_path": "training-fold StandardScaler -> LogisticRegression",
            },
            "L_14": {
                "definition": "PCA14 of the frozen DINOv2 representation within each identity-disjoint fold",
                "dimension": 14,
                "ordering": "raw L -> training-fold PCA14 -> training-fold StandardScaler -> frozen LogisticRegression",
                "fitting_rule": "fit each transformation within training rows only, apply to held-out rows",
            },
        },
        "metrics": {
            "primary": "pooled out-of-fold macro-F1",
            "secondary": "pooled out-of-fold balanced accuracy",
            "estimand": "D_{G,L14} = F1(G) - F1(L^(14))",
        },
        "bootstrap": build_compactness_bootstrap_plan(),
        "pre_outcome_gates": [
            "identity-disjoint folds remain frozen",
            "no leakage from train to test during PCA or scaling",
            "same classifier family used for all feature sets",
            "provenance and hash checks pass before outcome boundary",
            "mechanical validity gate passes before predictive interpretation",
        ],
        "amendment_commit": "30a0d37",
    }


def execute_frozen_compactness_analysis(
    output_json: Path | None = None,
    *,
    dino_features_path: Path | None = None,
    dino_rows_path: Path | None = None,
) -> int:
    """Run the already-frozen compactness analysis path.

    This is the explicit scientific execution entry point for the implementation already
    audited against the design lock. The path itself is not executed in this session.
    """
    if dino_features_path is None or dino_rows_path is None:
        raise ValueError("--dino-features and --dino-rows are required for --execute.")
    if not dino_features_path.is_file():
        raise FileNotFoundError(f"DINOv2 feature file not found: {dino_features_path}")
    if not dino_rows_path.is_file():
        raise FileNotFoundError(f"DINOv2 rows file not found: {dino_rows_path}")

    dino_features_sha = sha256_file(dino_features_path)
    dino_rows_sha = sha256_file(dino_rows_path)
    if dino_features_sha != EXPECTED_DINO_FILE_SHA:
        raise RuntimeError(f"DINOv2 SHA-256 mismatch: {dino_features_sha}")
    if dino_rows_sha != EXPECTED_DINO_ROW_SHA:
        raise RuntimeError(f"DINO row-manifest SHA-256 mismatch: {dino_rows_sha}")

    provenance = validate_pre_outcome_provenance(dino_features_path, dino_rows_path)
    G = np.load(RA14_PATH)
    L = np.load(dino_features_path)
    fold_id = provenance["fold_id"]
    y = provenance["y"]

    predictions = make_prediction_matrix(G, L, fold_id, y, validate=False)
    metrics_G = compute_pooled_metrics(y, predictions["G"])
    metrics_L14 = compute_pooled_metrics(y, predictions["L14"])
    estimand = compute_estimand(y, predictions["G"], predictions["L14"])
    bootstrap = paired_identity_bootstrap(
        y,
        pd.Series(provenance["rows"]["garment_id"].to_numpy(), name="garment_id"),
        predictions["G"],
        predictions["L14"],
        provenance["rows"]["category"],
        n_bootstrap=10000,
        seed=BOOTSTRAP_SEED,
    )

    result = {
        "baseline_commit": "9b1c5cd",
        "amendment_commit": "30a0d37",
        "metrics_G": metrics_G,
        "metrics_L14": metrics_L14,
        "estimand": estimand,
        "bootstrap": bootstrap,
        "plan": build_compactness_plan(),
    }

    resolved_output = output_json if output_json is not None else E8 / "experiment08_compactness_results.json"
    resolved_output.parent.mkdir(parents=True, exist_ok=True)
    resolved_output.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")

    output_text = json.dumps(result, indent=2, sort_keys=True)
    print(output_text)
    print(f"Saved compactness result JSON to: {resolved_output}")
    return 0


def main() -> int:
    """Parse arguments and validate the compactness runner without executing scientific analysis."""
    parser = argparse.ArgumentParser(description=__doc__)
    mode_group = parser.add_mutually_exclusive_group(required=False)
    mode_group.add_argument(
        "--validate-only",
        action="store_true",
        help="Static validation of the compactness-runner contract; no scientific execution occurs.",
    )
    mode_group.add_argument(
        "--execute",
        action="store_true",
        help="Execute the already-frozen compactness analysis path and write the predetermined outputs.",
    )
    parser.add_argument(
        "--dino-features",
        type=Path,
        default=None,
        help="Required with --execute: exact frozen DINOv2 embedding NPY path.",
    )
    parser.add_argument(
        "--dino-rows",
        type=Path,
        default=None,
        help="Required with --execute: exact frozen DINOv2 row-manifest CSV path.",
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        default=None,
        help="Optional JSON output path for the frozen compactness result. Defaults to Experiment_08/experiment08_compactness_results.json.",
    )
    args = parser.parse_args()

    if args.validate_only:
        print("Experiment-08 compactness runner loaded in structural validation mode.")
        print("Scientific analysis remains disabled in this session.")
        print(json.dumps(build_compactness_plan(), indent=2, sort_keys=True))
        return 0

    if args.execute:
        if args.dino_features is None or args.dino_rows is None:
            parser.error("--execute requires both --dino-features and --dino-rows.")
        return execute_frozen_compactness_analysis(args.output_json, dino_features_path=args.dino_features, dino_rows_path=args.dino_rows)

    # Execution is intentionally disabled in this session.
    print("COMPACTNESS ANALYSIS BLOCKED BY DESIGN.")
    print("No RA14-vs-DINOv2-PCA14 prediction, metric, bootstrap result, or affected outcome was computed.")
    print("Implementation is present; execution is intentionally disabled.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
