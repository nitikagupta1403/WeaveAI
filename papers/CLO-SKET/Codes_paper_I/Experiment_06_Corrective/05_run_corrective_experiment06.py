"""Corrective Experiment 06 outcome runner.

IMPORTANT
---------
This file is part of a pre-outcome implementation lock.

Default invocation performs validation only and exits BEFORE fitting any
classifier. Real outcome computation requires BOTH:

  --execute-outcome
  --committed-preflight-sha256 <sha256>

The supplied preflight file must be the frozen execution-lock preflight and
must report preflight_passed=true, predictive_outcome_computed=false, and
outcome_execution_unlocked=true. The caller must supply its SHA-256 explicitly.

The first real outcome run computes the complete frozen analysis bundle in one
invocation:
  * RAW diagnostic primary five-fold OOF comparison;
  * CLEAN confirmatory primary five-fold OOF comparison;
  * CLEAN category-stratified corrected-identity bootstrap, B=5000;
  * CLEAN repeated grouped five-fold robustness, seeds 20260820..20260829;
  * CLEAN category-preserving, block-size-matched alignment permutation, B=2000.

No hyperparameter search, feature selection, calibration, or adaptive analysis
is permitted.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler


REPO_ROOT = Path(__file__).resolve().parents[4]
EVIDENCE = REPO_ROOT / "papers/CLO-SKET/evidence/Experiment_06_Corrective"

EXPECTED_ROWS = 2300
EXPECTED_CLASSES = 23
EXPECTED_IDENTITIES = 230
EXPECTED_FOLDS = 5
EXPECTED_TEST_ROWS = [459, 460, 461, 460, 460]
EXPECTED_TEST_IDENTITIES = 46

EXPECTED_ARRAY_HASHES = {
    "raw_m135": "66ae04156ee3fbf3f2605f382a16fc41cf19af34b50e59dd43f6c9427d96b2ee",
    "raw_ra14": "01ea6937783792d0d9295ca92db863d932db4b57f5ad4b61ca78a2c97eb88a3c",
    "clean_m135": "eccc922726a433f95bd235f61a5f591034cd012b6b67b3acea575ad00c1b3a8d",
    "clean_ra14": "c233af755d9833c0a472490fd98b33a121083c647c0559e41bd5d673ce8ce9d4",
}

BOOTSTRAP_REPLICATES = 5000
ALIGNMENT_PERMUTATIONS = 2000
REPEATED_SEEDS = list(range(20260820, 20260830))
RNG_SEED = 20260820

ESTIMATOR = {
    "penalty": "l2",
    "C": 1.0,
    "solver": "lbfgs",
    "max_iter": 5000,
    "class_weight": None,
    "random_state": 20260820,
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_array(array: np.ndarray) -> str:
    arr = np.ascontiguousarray(array)
    return hashlib.sha256(arr.tobytes()).hexdigest()


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--preflight-report",
        type=Path,
        default=EVIDENCE / "experiment06_execution_lock_preflight.json",
    )
    p.add_argument(
        "--committed-preflight-sha256",
        type=str,
        default=None,
        help="Required only with --execute-outcome.",
    )
    p.add_argument(
        "--execute-outcome",
        action="store_true",
        help="Explicitly unlock the first corrected predictive outcome.",
    )
    p.add_argument("--output-root", type=Path, default=EVIDENCE)
    return p.parse_args()


def validate_preflight(path: Path, expected_sha: str | None, execute: bool) -> dict:
    if not path.is_file():
        raise RuntimeError(f"Missing execution preflight: {path}")

    observed_sha = sha256_file(path)

    if execute:
        if not expected_sha:
            raise RuntimeError(
                "--execute-outcome requires --committed-preflight-sha256"
            )
        if observed_sha != expected_sha:
            raise RuntimeError(
                "Execution preflight SHA mismatch: "
                f"{observed_sha} != {expected_sha}"
            )

    report = json.loads(path.read_text(encoding="utf-8"))

    if report.get("stage") != "PRE_OUTCOME_EXECUTION_IMPLEMENTATION_PREFLIGHT":
        raise RuntimeError("Execution preflight stage mismatch")
    if report.get("preflight_passed") is not True:
        raise RuntimeError("Execution preflight is not PASS")
    if report.get("predictive_outcome_computed") is not False:
        raise RuntimeError("Preflight indicates predictive outcome already computed")
    if report.get("outcome_execution_unlocked") is not True:
        raise RuntimeError("Preflight does not unlock outcome execution")

    return {"sha256": observed_sha, "report": report}


def load_inputs() -> tuple[pd.DataFrame, dict[str, np.ndarray], dict]:
    status_path = EVIDENCE / "experiment06_annotation_status.csv"
    manifest_path = EVIDENCE / "experiment06_corrective_feature_manifest.json"

    status = pd.read_csv(status_path, keep_default_na=False)
    if len(status) != EXPECTED_ROWS:
        raise RuntimeError(f"Status row count mismatch: {len(status)}")

    required = {
        "row_index",
        "relative_path",
        "category",
        "corrected_garment_id",
        "corrected_fold_id",
    }
    missing = required.difference(status.columns)
    if missing:
        raise RuntimeError(f"Status missing columns: {sorted(missing)}")

    status = status.sort_values("row_index").reset_index(drop=True)
    if not np.array_equal(status["row_index"].to_numpy(), np.arange(EXPECTED_ROWS)):
        raise RuntimeError("row_index must be exactly 0..2299")
    if status["category"].nunique() != EXPECTED_CLASSES:
        raise RuntimeError("Category count mismatch")
    if status["corrected_garment_id"].nunique() != EXPECTED_IDENTITIES:
        raise RuntimeError("Identity count mismatch")

    observed_test_rows = (
        status.groupby("corrected_fold_id", sort=True)
        .size()
        .astype(int)
        .tolist()
    )
    if observed_test_rows != EXPECTED_TEST_ROWS:
        raise RuntimeError(
            f"Corrected fold row counts mismatch: {observed_test_rows}"
        )

    per_fold_ids = (
        status.groupby("corrected_fold_id")["corrected_garment_id"]
        .nunique()
        .astype(int)
        .tolist()
    )
    if per_fold_ids != [EXPECTED_TEST_IDENTITIES] * EXPECTED_FOLDS:
        raise RuntimeError(f"Corrected fold identity counts mismatch: {per_fold_ids}")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    checks = manifest.get("historical_reproduction_checks", {})
    if checks.get("raw_m135_exact_match") is not True:
        raise RuntimeError("Feature manifest does not confirm RAW M135 reproduction")
    if checks.get("raw_ra14_exact_match") is not True:
        raise RuntimeError("Feature manifest does not confirm RAW RA14 reproduction")
    if manifest.get("classifier_fitted") is not False:
        raise RuntimeError("Feature manifest indicates classifier fitting")
    if manifest.get("predictive_metric_computed") is not False:
        raise RuntimeError("Feature manifest indicates predictive metrics")

    paths = {
        "raw_m135": EVIDENCE / "experiment06_corrective_raw_m135.npy",
        "raw_ra14": EVIDENCE / "experiment06_corrective_raw_ra14.npy",
        "clean_m135": EVIDENCE / "experiment06_corrective_clean_m135.npy",
        "clean_ra14": EVIDENCE / "experiment06_corrective_clean_ra14.npy",
    }

    arrays: dict[str, np.ndarray] = {}
    for name, path in paths.items():
        if not path.is_file():
            raise RuntimeError(f"Missing frozen feature matrix: {path}")
        arr = np.load(path, allow_pickle=False)
        expected_shape = (EXPECTED_ROWS, 135 if "m135" in name else 14)
        if arr.shape != expected_shape:
            raise RuntimeError(f"{name} shape mismatch: {arr.shape}")
        if not np.isfinite(arr).all():
            raise RuntimeError(f"{name} contains non-finite values")
        observed = sha256_array(arr)
        expected = EXPECTED_ARRAY_HASHES[name]
        if observed != expected:
            raise RuntimeError(f"{name} array SHA mismatch: {observed} != {expected}")
        arrays[name] = arr

    return status, arrays, {
        "annotation_status_sha256": sha256_file(status_path),
        "feature_manifest_sha256": sha256_file(manifest_path),
        "feature_array_sha256": EXPECTED_ARRAY_HASHES,
    }


def fit_oof(
    X: np.ndarray,
    y: np.ndarray,
    fold_ids: np.ndarray,
) -> tuple[np.ndarray, pd.DataFrame]:
    pred = np.empty(y.shape[0], dtype=object)
    rows = []

    for fold in range(EXPECTED_FOLDS):
        test = fold_ids == fold
        train = ~test

        scaler = StandardScaler()
        X_train = scaler.fit_transform(X[train])
        X_test = scaler.transform(X[test])

        model = LogisticRegression(**ESTIMATOR)
        model.fit(X_train, y[train])
        fold_pred = model.predict(X_test)
        pred[test] = fold_pred

        rows.append(
            {
                "fold": fold,
                "test_rows": int(test.sum()),
                "macro_f1": float(
                    f1_score(y[test], fold_pred, average="macro")
                ),
                "balanced_accuracy": float(
                    balanced_accuracy_score(y[test], fold_pred)
                ),
            }
        )

    if any(v is None for v in pred):
        raise RuntimeError("OOF prediction vector is incomplete")

    return pred.astype(str), pd.DataFrame(rows)


def pooled_metrics(y: np.ndarray, pred: np.ndarray) -> dict:
    return {
        "macro_f1": float(f1_score(y, pred, average="macro")),
        "balanced_accuracy": float(balanced_accuracy_score(y, pred)),
    }


def primary_condition(condition, m135, ra14, y, fold_ids) -> dict:
    augmented = np.concatenate([m135, ra14], axis=1)
    pred_m, fold_m = fit_oof(m135, y, fold_ids)
    pred_aug, fold_aug = fit_oof(augmented, y, fold_ids)
    pooled_m = pooled_metrics(y, pred_m)
    pooled_aug = pooled_metrics(y, pred_aug)

    fold = fold_m.rename(columns={
        "macro_f1": "m_macro_f1",
        "balanced_accuracy": "m_balanced_accuracy",
    }).merge(
        fold_aug.rename(columns={
            "macro_f1": "aug_macro_f1",
            "balanced_accuracy": "aug_balanced_accuracy",
        }),
        on=["fold", "test_rows"], validate="one_to_one",
    )
    fold["delta_macro_f1"] = fold["aug_macro_f1"] - fold["m_macro_f1"]
    fold["delta_balanced_accuracy"] = (
        fold["aug_balanced_accuracy"] - fold["m_balanced_accuracy"]
    )
    fold.insert(0, "condition", condition)

    return {
        "pred_m": pred_m,
        "pred_aug": pred_aug,
        "fold_metrics": fold,
        "pooled": {
            "condition": condition,
            "m_macro_f1": pooled_m["macro_f1"],
            "m_balanced_accuracy": pooled_m["balanced_accuracy"],
            "aug_macro_f1": pooled_aug["macro_f1"],
            "aug_balanced_accuracy": pooled_aug["balanced_accuracy"],
            "delta_macro_f1": pooled_aug["macro_f1"] - pooled_m["macro_f1"],
            "delta_balanced_accuracy": (
                pooled_aug["balanced_accuracy"] - pooled_m["balanced_accuracy"]
            ),
        },
    }


def identity_bootstrap(status, y, pred_m, pred_aug) -> pd.DataFrame:
    by_category = {}
    for category, cat_frame in status.groupby("category", sort=True):
        blocks = []
        for identity, block in cat_frame.groupby("corrected_garment_id", sort=True):
            blocks.append((str(identity), block["row_index"].to_numpy(dtype=int)))
        if len(blocks) != 10:
            raise RuntimeError(f"Expected 10 identities in {category}")
        by_category[str(category)] = blocks

    rng = np.random.default_rng(RNG_SEED)
    out = []
    for b in range(BOOTSTRAP_REPLICATES):
        sampled_rows = []
        for category in sorted(by_category):
            blocks = by_category[category]
            chosen = rng.integers(0, len(blocks), size=len(blocks))
            for idx in chosen:
                sampled_rows.extend(blocks[int(idx)][1].tolist())
        idx = np.asarray(sampled_rows, dtype=int)
        m = pooled_metrics(y[idx], pred_m[idx])
        a = pooled_metrics(y[idx], pred_aug[idx])
        out.append({
            "replicate": b,
            "delta_macro_f1": a["macro_f1"] - m["macro_f1"],
            "delta_balanced_accuracy": (
                a["balanced_accuracy"] - m["balanced_accuracy"]
            ),
        })
    return pd.DataFrame(out)


def bootstrap_summary(bootstrap, observed) -> dict:
    summary = {}
    for metric, observed_key in [
        ("macro_f1", "delta_macro_f1"),
        ("balanced_accuracy", "delta_balanced_accuracy"),
    ]:
        values = bootstrap[f"delta_{metric}"].to_numpy(dtype=float)
        summary[metric] = {
            "observed": float(observed[observed_key]),
            "bootstrap_mean": float(np.mean(values)),
            "percentile_2_5": float(np.percentile(values, 2.5)),
            "percentile_97_5": float(np.percentile(values, 97.5)),
            "positive_replicates": int(np.sum(values > 0)),
            "replicates": int(values.size),
        }
    return summary


def make_repeated_fold_ids(status, seed) -> np.ndarray:
    rng = np.random.default_rng(seed)
    assignment = {}
    for category, cat_frame in status.groupby("category", sort=True):
        identities = sorted(cat_frame["corrected_garment_id"].unique().tolist())
        permuted = np.asarray(identities, dtype=object)[rng.permutation(10)]
        for fold in range(5):
            for identity in permuted[2 * fold:2 * fold + 2]:
                assignment[str(identity)] = fold
    return status["corrected_garment_id"].astype(str).map(assignment).to_numpy(dtype=int)


def repeated_grouped_robustness(status, clean_m135, clean_ra14, y) -> pd.DataFrame:
    rows = []
    augmented = np.concatenate([clean_m135, clean_ra14], axis=1)
    for seed in REPEATED_SEEDS:
        fold_ids = make_repeated_fold_ids(status, seed)
        pred_m, fold_m = fit_oof(clean_m135, y, fold_ids)
        pred_aug, fold_aug = fit_oof(augmented, y, fold_ids)
        m = pooled_metrics(y, pred_m)
        a = pooled_metrics(y, pred_aug)
        rows.append({
            "seed": seed,
            "delta_macro_f1": a["macro_f1"] - m["macro_f1"],
            "delta_balanced_accuracy": a["balanced_accuracy"] - m["balanced_accuracy"],
            "positive_folds_macro_f1": int((
                fold_aug["macro_f1"].to_numpy()
                - fold_m["macro_f1"].to_numpy() > 0
            ).sum()),
        })
    return pd.DataFrame(rows)


def build_alignment_strata(status) -> list[dict]:
    identities = (
        status.groupby(["category", "corrected_garment_id"], sort=True)
        .agg(
            block_size=("row_index", "size"),
            row_indices=("row_index", lambda s: tuple(sorted(map(int, s)))),
        )
        .reset_index()
    )
    strata = []
    for (category, block_size), group in identities.groupby(
        ["category", "block_size"], sort=True
    ):
        items = [{
            "identity": str(r.corrected_garment_id),
            "rows": np.asarray(r.row_indices, dtype=int),
        } for r in group.itertuples(index=False)]
        strata.append({
            "category": str(category),
            "block_size": int(block_size),
            "items": items,
        })
    return strata


def permuted_ra14(ra14, strata, rng):
    out = np.empty_like(ra14)
    self_rows = 0
    for stratum in strata:
        items = stratum["items"]
        n = len(items)
        if n == 1:
            donor_order = np.array([0], dtype=int)
        else:
            donor_order = rng.permutation(n)
            attempts = 0
            while np.any(donor_order == np.arange(n)):
                donor_order = rng.permutation(n)
                attempts += 1
                if attempts > 10000:
                    raise RuntimeError("Could not construct alignment derangement")
        for recipient_idx, donor_idx in enumerate(donor_order):
            recipient = items[recipient_idx]
            donor = items[int(donor_idx)]
            out[recipient["rows"]] = ra14[donor["rows"]]
            if recipient_idx == int(donor_idx):
                self_rows += int(recipient["rows"].size)
    return out, self_rows


def alignment_permutation(status, clean_m135, clean_ra14, y, fold_ids, observed):
    rng = np.random.default_rng(RNG_SEED)
    strata = build_alignment_strata(status)
    pred_m, _ = fit_oof(clean_m135, y, fold_ids)
    m = pooled_metrics(y, pred_m)
    rows = []
    self_rows_ref = None

    for b in range(ALIGNMENT_PERMUTATIONS):
        perm_ra14, self_rows = permuted_ra14(clean_ra14, strata, rng)
        if self_rows_ref is None:
            self_rows_ref = self_rows
        elif self_rows != self_rows_ref:
            raise RuntimeError("Alignment self-mapped row count changed")
        X = np.concatenate([clean_m135, perm_ra14], axis=1)
        pred_aug, _ = fit_oof(X, y, fold_ids)
        a = pooled_metrics(y, pred_aug)
        rows.append({
            "permutation": b,
            "delta_macro_f1": a["macro_f1"] - m["macro_f1"],
            "delta_balanced_accuracy": a["balanced_accuracy"] - m["balanced_accuracy"],
            "self_mapped_rows": int(self_rows),
        })
        if (b + 1) % 100 == 0:
            print(f"Alignment permutation: completed {b + 1}/{ALIGNMENT_PERMUTATIONS}")

    frame = pd.DataFrame(rows)
    summary = {}
    for metric, observed_key in [
        ("macro_f1", "delta_macro_f1"),
        ("balanced_accuracy", "delta_balanced_accuracy"),
    ]:
        values = frame[f"delta_{metric}"].to_numpy(dtype=float)
        obs = float(observed[observed_key])
        summary[metric] = {
            "observed": obs,
            "null_mean": float(np.mean(values)),
            "null_sd": float(np.std(values, ddof=1)),
            "null_2_5": float(np.percentile(values, 2.5)),
            "null_97_5": float(np.percentile(values, 97.5)),
            "empirical_p_one_sided": float(
                (1 + np.sum(values >= obs)) / (ALIGNMENT_PERMUTATIONS + 1)
            ),
        }
    summary["self_mapped_rows"] = int(self_rows_ref or 0)
    summary["self_mapped_fraction"] = float((self_rows_ref or 0) / EXPECTED_ROWS)
    return frame, summary


def save_csv(path, frame) -> str:
    frame.to_csv(path, index=False, lineterminator="\n")
    return sha256_file(path)


def main() -> None:
    args = parse_args()
    output_root = args.output_root.expanduser().resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    preflight = validate_preflight(
        args.preflight_report.expanduser().resolve(),
        args.committed_preflight_sha256,
        args.execute_outcome,
    )
    status, arrays, input_hashes = load_inputs()

    print("Corrective Experiment 06 runner validation: PASS")
    print(f"Rows: {len(status)}")
    print("Frozen feature hashes: PASS")
    print(f"Execution preflight SHA-256: {preflight['sha256']}")

    if not args.execute_outcome:
        print(
            "STOP — outcome execution remains disabled. No classifier, prediction, "
            "metric, bootstrap, repeated partition, or permutation was computed."
        )
        return

    y = status["category"].astype(str).to_numpy()
    fold_ids = status["corrected_fold_id"].astype(int).to_numpy()

    raw = primary_condition("RAW", arrays["raw_m135"], arrays["raw_ra14"], y, fold_ids)
    clean = primary_condition("CLEAN", arrays["clean_m135"], arrays["clean_ra14"], y, fold_ids)
    bootstrap = identity_bootstrap(status, y, clean["pred_m"], clean["pred_aug"])
    bootstrap_sum = bootstrap_summary(bootstrap, clean["pooled"])
    repeated = repeated_grouped_robustness(
        status, arrays["clean_m135"], arrays["clean_ra14"], y
    )
    alignment, alignment_sum = alignment_permutation(
        status, arrays["clean_m135"], arrays["clean_ra14"], y, fold_ids, clean["pooled"]
    )

    oof = status[[
        "row_index", "relative_path", "category",
        "corrected_garment_id", "corrected_fold_id",
    ]].copy()
    oof["raw_pred_m"] = raw["pred_m"]
    oof["raw_pred_m_ra14"] = raw["pred_aug"]
    oof["clean_pred_m"] = clean["pred_m"]
    oof["clean_pred_m_ra14"] = clean["pred_aug"]

    pooled = pd.DataFrame([raw["pooled"], clean["pooled"]])
    fold_metrics = pd.concat([raw["fold_metrics"], clean["fold_metrics"]], ignore_index=True)
    annotation_impact = pd.DataFrame([
        {
            "metric": "macro_f1",
            "raw_m": raw["pooled"]["m_macro_f1"],
            "clean_m": clean["pooled"]["m_macro_f1"],
            "raw_aug": raw["pooled"]["aug_macro_f1"],
            "clean_aug": clean["pooled"]["aug_macro_f1"],
            "raw_increment": raw["pooled"]["delta_macro_f1"],
            "clean_increment": clean["pooled"]["delta_macro_f1"],
            "clean_minus_raw_increment": clean["pooled"]["delta_macro_f1"] - raw["pooled"]["delta_macro_f1"],
        },
        {
            "metric": "balanced_accuracy",
            "raw_m": raw["pooled"]["m_balanced_accuracy"],
            "clean_m": clean["pooled"]["m_balanced_accuracy"],
            "raw_aug": raw["pooled"]["aug_balanced_accuracy"],
            "clean_aug": clean["pooled"]["aug_balanced_accuracy"],
            "raw_increment": raw["pooled"]["delta_balanced_accuracy"],
            "clean_increment": clean["pooled"]["delta_balanced_accuracy"],
            "clean_minus_raw_increment": clean["pooled"]["delta_balanced_accuracy"] - raw["pooled"]["delta_balanced_accuracy"],
        },
    ])

    paths = {
        "oof_predictions": output_root / "experiment06_corrective_oof_predictions.csv",
        "pooled_metrics": output_root / "experiment06_corrective_pooled_metrics.csv",
        "fold_metrics": output_root / "experiment06_corrective_fold_metrics.csv",
        "annotation_impact": output_root / "experiment06_corrective_annotation_impact.csv",
        "bootstrap": output_root / "experiment06_corrective_clean_identity_bootstrap.csv",
        "repeated": output_root / "experiment06_corrective_clean_repeated_partitions.csv",
        "alignment": output_root / "experiment06_corrective_clean_alignment_permutation.csv",
        "summary": output_root / "experiment06_corrective_outcome_summary.json",
    }

    output_hashes = {
        "oof_predictions": save_csv(paths["oof_predictions"], oof),
        "pooled_metrics": save_csv(paths["pooled_metrics"], pooled),
        "fold_metrics": save_csv(paths["fold_metrics"], fold_metrics),
        "annotation_impact": save_csv(paths["annotation_impact"], annotation_impact),
        "bootstrap": save_csv(paths["bootstrap"], bootstrap),
        "repeated": save_csv(paths["repeated"], repeated),
        "alignment": save_csv(paths["alignment"], alignment),
    }

    repeated_summary = {
        "macro_f1": {
            "mean": float(repeated["delta_macro_f1"].mean()),
            "sd": float(repeated["delta_macro_f1"].std(ddof=1)),
            "min": float(repeated["delta_macro_f1"].min()),
            "max": float(repeated["delta_macro_f1"].max()),
            "positive_repeats": int((repeated["delta_macro_f1"] > 0).sum()),
        },
        "balanced_accuracy": {
            "mean": float(repeated["delta_balanced_accuracy"].mean()),
            "sd": float(repeated["delta_balanced_accuracy"].std(ddof=1)),
            "min": float(repeated["delta_balanced_accuracy"].min()),
            "max": float(repeated["delta_balanced_accuracy"].max()),
            "positive_repeats": int((repeated["delta_balanced_accuracy"] > 0).sum()),
        },
    }

    ci = bootstrap_sum["macro_f1"]
    if clean["pooled"]["delta_macro_f1"] > 0 and ci["percentile_2_5"] > 0:
        decision = "CONFIRMATORY_POSITIVE_INCREMENT_SUPPORTED"
    elif clean["pooled"]["delta_macro_f1"] > 0:
        decision = "POSITIVE_INCREMENT_UNCERTAIN_INTERVAL_INCLUDES_ZERO"
    else:
        decision = "POSITIVE_CONFIRMATORY_UTILITY_CLAIM_ABANDONED"

    summary = {
        "schema_version": 1,
        "experiment": "CLO-SKET Experiment 06 corrective reanalysis",
        "stage": "CORRECTIVE_OUTCOME_COMPLETE",
        "primary_condition": "CLEAN",
        "raw_condition_status": "diagnostic_only",
        "estimator": ESTIMATOR,
        "bootstrap_replicates": BOOTSTRAP_REPLICATES,
        "alignment_permutations": ALIGNMENT_PERMUTATIONS,
        "repeated_partition_seeds": REPEATED_SEEDS,
        "input_hashes": input_hashes,
        "committed_execution_preflight_sha256": preflight["sha256"],
        "primary_results": {"RAW": raw["pooled"], "CLEAN": clean["pooled"]},
        "clean_identity_bootstrap": bootstrap_sum,
        "clean_repeated_partitions": repeated_summary,
        "clean_alignment_permutation": alignment_sum,
        "decision_rule_result": decision,
        "output_sha256": output_hashes,
        "classifier_fitted": True,
        "prediction_computed": True,
        "predictive_metric_computed": True,
        "bootstrap_computed": True,
        "repeated_partitions_computed": True,
        "permutation_computed": True,
    }
    paths["summary"].write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print("\nExperiment 06 corrective outcome run: COMPLETE")
    print(f"Decision rule: {decision}")
    print(f"Summary: {paths['summary']}")


if __name__ == "__main__":
    main()
