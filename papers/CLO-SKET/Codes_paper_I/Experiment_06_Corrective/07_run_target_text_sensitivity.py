"""Post-outcome target-text sensitivity analysis for corrective Experiment 06.

This runner implements the protocol frozen in:

  papers/CLO-SKET/evidence/Experiment_06_Corrective/
  09_TARGET_TEXT_SENSITIVITY_PROTOCOL.md

The sensitivity intervention is fixed:
  exclude exactly Cardigan__G02 and Tunic__G02 at garment-identity level.

IMPORTANT
---------
Default invocation is validation-only and MUST NOT fit a classifier or compute
a predictive metric.

Real sensitivity execution requires BOTH:

  --execute-sensitivity
  --committed-protocol-sha256 <sha256>

This is a post-outcome sensitivity analysis. It is not a new confirmatory
Experiment 06 and cannot change the inferential status of the frozen corrective
Experiment-06 result.

Implementation principle
------------------------
The canonical corrective runner is reused for frozen estimator specification,
OOF fitting, pooled metrics, bootstrap summarization, alignment stratum
construction, and permutation construction.

Only adaptations forced by removal of two identities are implemented here:

1. Category-stratified identity bootstrap samples the retained number of
   identities within each category (9 for Cardigan/Tunic, 10 otherwise).

2. Repeated grouped folds are first generated on the original full 230-identity
   population using the canonical frozen algorithm and frozen seeds; the two
   excluded identities are then removed. Thus every retained identity preserves
   exactly the fold assignment it would have received in the canonical run.

3. Alignment-permutation self-mapped fraction uses the retained row count.

No model selection, tuning, feature reconstruction, fold re-optimization, or
outcome-contingent adaptation is permitted.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[4]
CORRECTIVE_DIR = Path(__file__).resolve().parent
EVIDENCE = REPO_ROOT / "papers/CLO-SKET/evidence/Experiment_06_Corrective"

CANONICAL_RUNNER = CORRECTIVE_DIR / "05_run_corrective_experiment06.py"
PROTOCOL = EVIDENCE / "09_TARGET_TEXT_SENSITIVITY_PROTOCOL.md"
LEAKAGE_SUMMARY = EVIDENCE / "experiment06_target_text_leakage_summary.json"
LEAKAGE_REVIEW = EVIDENCE / "experiment06_target_text_leakage_review.csv"

EXCLUDED_IDENTITIES = ("Cardigan__G02", "Tunic__G02")
EXPECTED_EXACT_ROWS = (320, 2020)
EXPECTED_EXACT_PATHS = ("Cardigan/2-1.tif", "Tunic/2_1.tif")

EXPECTED_FULL_ROWS = 2300
EXPECTED_FULL_IDENTITIES = 230
EXPECTED_RETAINED_IDENTITIES = 228
EXPECTED_CLASSES = 23

OUTPUT_PREFIX = "experiment06_target_text_sensitivity"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_canonical_runner():
    if not CANONICAL_RUNNER.is_file():
        raise RuntimeError(f"Missing canonical runner: {CANONICAL_RUNNER}")

    spec = importlib.util.spec_from_file_location(
        "experiment06_corrective_canonical",
        CANONICAL_RUNNER,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load canonical corrective runner")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--committed-protocol-sha256",
        type=str,
        default=None,
        help="Required only with --execute-sensitivity.",
    )
    p.add_argument(
        "--execute-sensitivity",
        action="store_true",
        help="Explicitly unlock the post-outcome target-text sensitivity analysis.",
    )
    p.add_argument(
        "--output-root",
        type=Path,
        default=EVIDENCE,
    )
    return p.parse_args()


def validate_protocol(expected_sha: str | None, execute: bool) -> str:
    if not PROTOCOL.is_file():
        raise RuntimeError(f"Missing frozen sensitivity protocol: {PROTOCOL}")

    observed = sha256_file(PROTOCOL)

    if execute:
        if not expected_sha:
            raise RuntimeError(
                "--execute-sensitivity requires --committed-protocol-sha256"
            )
        if observed != expected_sha:
            raise RuntimeError(
                "Sensitivity protocol SHA mismatch: "
                f"{observed} != {expected_sha}"
            )

    text = PROTOCOL.read_text(encoding="utf-8")
    for identity in EXCLUDED_IDENTITIES:
        if identity not in text:
            raise RuntimeError(
                f"Frozen sensitivity protocol does not name {identity}"
            )

    required_phrases = (
        "post-outcome sensitivity",
        "No new confirmatory claim",
        "No model selection, tuning",
        "The frozen CLEAN images themselves will not be edited or sanitized.",
    )
    for phrase in required_phrases:
        if phrase not in text:
            raise RuntimeError(
                f"Frozen protocol missing required phrase: {phrase}"
            )

    return observed


def validate_leakage_audit() -> dict:
    if not LEAKAGE_SUMMARY.is_file():
        raise RuntimeError(f"Missing leakage summary: {LEAKAGE_SUMMARY}")
    if not LEAKAGE_REVIEW.is_file():
        raise RuntimeError(f"Missing leakage review: {LEAKAGE_REVIEW}")

    summary = json.loads(LEAKAGE_SUMMARY.read_text(encoding="utf-8"))

    counts = summary.get("review_status_counts", {})
    if counts != {
        "AMBIGUOUS": 0,
        "EXACT": 2,
        "NONE": 2298,
        "PARTIAL_OR_ABBREVIATED": 0,
    }:
        raise RuntimeError(f"Unexpected leakage status counts: {counts}")

    if summary.get("target_text_leakage_cleared") is not False:
        raise RuntimeError("Leakage summary unexpectedly reports cleared=true")

    review_sha = sha256_file(LEAKAGE_REVIEW)
    if review_sha != summary.get("review_csv_sha256"):
        raise RuntimeError(
            "Leakage review SHA does not match frozen summary: "
            f"{review_sha} != {summary.get('review_csv_sha256')}"
        )

    review = pd.read_csv(LEAKAGE_REVIEW, keep_default_na=False)
    exact = (
        review.loc[review["target_text_status"].astype(str) == "EXACT"]
        .sort_values("row_index")
        .reset_index(drop=True)
    )

    observed_rows = tuple(exact["row_index"].astype(int).tolist())
    observed_paths = tuple(exact["relative_path"].astype(str).tolist())
    observed_ids = tuple(exact["corrected_garment_id"].astype(str).tolist())

    if observed_rows != EXPECTED_EXACT_ROWS:
        raise RuntimeError(
            f"Unexpected EXACT rows: {observed_rows}"
        )
    if observed_paths != EXPECTED_EXACT_PATHS:
        raise RuntimeError(
            f"Unexpected EXACT paths: {observed_paths}"
        )
    if observed_ids != EXCLUDED_IDENTITIES:
        raise RuntimeError(
            f"Unexpected EXACT identities: {observed_ids}"
        )

    return {
        "summary_sha256": sha256_file(LEAKAGE_SUMMARY),
        "review_sha256": review_sha,
        "exact_rows": list(observed_rows),
        "exact_paths": list(observed_paths),
        "exact_identities": list(observed_ids),
    }


def prepare_retained_inputs(canonical):
    # Canonical loader verifies all frozen source matrices and hashes before
    # anything is subsetted.
    full_status, full_arrays, input_hashes = canonical.load_inputs()

    if len(full_status) != EXPECTED_FULL_ROWS:
        raise RuntimeError("Canonical full-row count changed")
    if full_status["corrected_garment_id"].nunique() != EXPECTED_FULL_IDENTITIES:
        raise RuntimeError("Canonical full identity count changed")

    exclude_mask = full_status["corrected_garment_id"].astype(str).isin(
        EXCLUDED_IDENTITIES
    )

    excluded = full_status.loc[exclude_mask].copy()
    excluded_ids = set(excluded["corrected_garment_id"].astype(str))
    if excluded_ids != set(EXCLUDED_IDENTITIES):
        raise RuntimeError(
            f"Excluded identity set mismatch: {sorted(excluded_ids)}"
        )

    retained_positions = np.flatnonzero(~exclude_mask.to_numpy())

    retained = (
        full_status.loc[~exclude_mask]
        .copy()
        .reset_index(drop=True)
    )

    # Preserve original row_index for provenance, while replacing row_index
    # with a sensitivity-local contiguous index required by block resampling.
    retained.insert(
        retained.columns.get_loc("row_index"),
        "original_row_index",
        retained["row_index"].astype(int),
    )
    retained["row_index"] = np.arange(len(retained), dtype=int)

    arrays = {
        name: arr[retained_positions].copy()
        for name, arr in full_arrays.items()
    }

    if retained["corrected_garment_id"].nunique() != EXPECTED_RETAINED_IDENTITIES:
        raise RuntimeError(
            "Retained identity count is not 228 after predefined exclusion"
        )
    if retained["category"].nunique() != EXPECTED_CLASSES:
        raise RuntimeError("Class count changed after predefined exclusion")
    if retained["corrected_garment_id"].isin(EXCLUDED_IDENTITIES).any():
        raise RuntimeError("Excluded identity remains in retained status")

    category_identity_counts = (
        retained.groupby("category")["corrected_garment_id"]
        .nunique()
        .astype(int)
        .to_dict()
    )
    if category_identity_counts.get("Cardigan") != 9:
        raise RuntimeError("Cardigan retained identity count must be 9")
    if category_identity_counts.get("Tunic") != 9:
        raise RuntimeError("Tunic retained identity count must be 9")

    for category, n in category_identity_counts.items():
        expected = 9 if category in {"Cardigan", "Tunic"} else 10
        if n != expected:
            raise RuntimeError(
                f"Unexpected retained identity count for {category}: {n}"
            )

    return (
        full_status,
        retained,
        arrays,
        retained_positions,
        input_hashes,
        excluded,
        category_identity_counts,
    )


def sensitivity_identity_bootstrap(
    canonical,
    status: pd.DataFrame,
    y: np.ndarray,
    pred_m: np.ndarray,
    pred_aug: np.ndarray,
) -> pd.DataFrame:
    by_category = {}

    for category, cat_frame in status.groupby("category", sort=True):
        blocks = []
        for identity, block in cat_frame.groupby(
            "corrected_garment_id",
            sort=True,
        ):
            blocks.append(
                (
                    str(identity),
                    block["row_index"].to_numpy(dtype=int),
                )
            )

        expected = 9 if str(category) in {"Cardigan", "Tunic"} else 10
        if len(blocks) != expected:
            raise RuntimeError(
                f"Unexpected retained identity count in {category}: "
                f"{len(blocks)} != {expected}"
            )

        by_category[str(category)] = blocks

    rng = np.random.default_rng(canonical.RNG_SEED)
    out = []

    for b in range(canonical.BOOTSTRAP_REPLICATES):
        sampled_rows = []

        for category in sorted(by_category):
            blocks = by_category[category]

            # Same category-stratified identity bootstrap principle as the
            # canonical runner, sampling the retained number of blocks.
            chosen = rng.integers(
                0,
                len(blocks),
                size=len(blocks),
            )

            for idx in chosen:
                sampled_rows.extend(
                    blocks[int(idx)][1].tolist()
                )

        idx = np.asarray(sampled_rows, dtype=int)

        m = canonical.pooled_metrics(y[idx], pred_m[idx])
        a = canonical.pooled_metrics(y[idx], pred_aug[idx])

        out.append(
            {
                "replicate": b,
                "delta_macro_f1": (
                    a["macro_f1"] - m["macro_f1"]
                ),
                "delta_balanced_accuracy": (
                    a["balanced_accuracy"]
                    - m["balanced_accuracy"]
                ),
            }
        )

    return pd.DataFrame(out)


def canonical_full_repeated_fold_ids(
    canonical,
    full_status: pd.DataFrame,
    seed: int,
) -> np.ndarray:
    """Reproduce canonical full-population repeated folds exactly."""

    rng = np.random.default_rng(seed)
    assignment = {}

    for category, cat_frame in full_status.groupby("category", sort=True):
        identities = sorted(
            cat_frame["corrected_garment_id"]
            .astype(str)
            .unique()
            .tolist()
        )

        if len(identities) != 10:
            raise RuntimeError(
                f"Canonical full population no longer has 10 identities "
                f"in {category}"
            )

        permuted = np.asarray(
            identities,
            dtype=object,
        )[rng.permutation(10)]

        for fold in range(5):
            for identity in permuted[2 * fold : 2 * fold + 2]:
                assignment[str(identity)] = fold

    return (
        full_status["corrected_garment_id"]
        .astype(str)
        .map(assignment)
        .to_numpy(dtype=int)
    )


def sensitivity_repeated_grouped_robustness(
    canonical,
    full_status: pd.DataFrame,
    retained_positions: np.ndarray,
    retained_status: pd.DataFrame,
    clean_m135: np.ndarray,
    clean_ra14: np.ndarray,
    y: np.ndarray,
) -> pd.DataFrame:
    rows = []
    augmented = np.concatenate([clean_m135, clean_ra14], axis=1)

    for seed in canonical.REPEATED_SEEDS:
        full_fold_ids = canonical_full_repeated_fold_ids(
            canonical,
            full_status,
            seed,
        )
        fold_ids = full_fold_ids[retained_positions]

        # Verify retained folds are exactly the subset of the canonical
        # full-population seeded assignment.
        if fold_ids.shape[0] != len(retained_status):
            raise RuntimeError("Repeated-fold retained length mismatch")
        if set(np.unique(fold_ids)) != {0, 1, 2, 3, 4}:
            raise RuntimeError(
                f"Repeated-fold seed {seed} does not retain all five folds"
            )

        pred_m, fold_m = canonical.fit_oof(
            clean_m135,
            y,
            fold_ids,
        )
        pred_aug, fold_aug = canonical.fit_oof(
            augmented,
            y,
            fold_ids,
        )

        m = canonical.pooled_metrics(y, pred_m)
        a = canonical.pooled_metrics(y, pred_aug)

        rows.append(
            {
                "seed": seed,
                "delta_macro_f1": (
                    a["macro_f1"] - m["macro_f1"]
                ),
                "delta_balanced_accuracy": (
                    a["balanced_accuracy"]
                    - m["balanced_accuracy"]
                ),
                "positive_folds_macro_f1": int(
                    (
                        fold_aug["macro_f1"].to_numpy()
                        - fold_m["macro_f1"].to_numpy()
                        > 0
                    ).sum()
                ),
                "fold_0_rows": int(np.sum(fold_ids == 0)),
                "fold_1_rows": int(np.sum(fold_ids == 1)),
                "fold_2_rows": int(np.sum(fold_ids == 2)),
                "fold_3_rows": int(np.sum(fold_ids == 3)),
                "fold_4_rows": int(np.sum(fold_ids == 4)),
            }
        )

    return pd.DataFrame(rows)


def sensitivity_alignment_permutation(
    canonical,
    status: pd.DataFrame,
    clean_m135: np.ndarray,
    clean_ra14: np.ndarray,
    y: np.ndarray,
    fold_ids: np.ndarray,
    observed: dict,
):
    rng = np.random.default_rng(canonical.RNG_SEED)
    strata = canonical.build_alignment_strata(status)

    pred_m, _ = canonical.fit_oof(
        clean_m135,
        y,
        fold_ids,
    )
    m = canonical.pooled_metrics(y, pred_m)

    rows = []
    self_rows_ref = None

    for b in range(canonical.ALIGNMENT_PERMUTATIONS):
        perm_ra14, self_rows = canonical.permuted_ra14(
            clean_ra14,
            strata,
            rng,
        )

        if self_rows_ref is None:
            self_rows_ref = self_rows
        elif self_rows != self_rows_ref:
            raise RuntimeError(
                "Alignment self-mapped row count changed"
            )

        X = np.concatenate(
            [clean_m135, perm_ra14],
            axis=1,
        )
        pred_aug, _ = canonical.fit_oof(
            X,
            y,
            fold_ids,
        )
        a = canonical.pooled_metrics(y, pred_aug)

        rows.append(
            {
                "permutation": b,
                "delta_macro_f1": (
                    a["macro_f1"] - m["macro_f1"]
                ),
                "delta_balanced_accuracy": (
                    a["balanced_accuracy"]
                    - m["balanced_accuracy"]
                ),
                "self_mapped_rows": int(self_rows),
            }
        )

        if (b + 1) % 100 == 0:
            print(
                "Target-text sensitivity alignment permutation: "
                f"completed {b + 1}/"
                f"{canonical.ALIGNMENT_PERMUTATIONS}"
            )

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
                (
                    1 + np.sum(values >= obs)
                )
                / (
                    canonical.ALIGNMENT_PERMUTATIONS + 1
                )
            ),
        }

    retained_rows = len(status)

    summary["self_mapped_rows"] = int(
        self_rows_ref or 0
    )
    summary["self_mapped_fraction"] = float(
        (self_rows_ref or 0) / retained_rows
    )
    summary["fraction_denominator_rows"] = int(retained_rows)

    return frame, summary


def save_csv(path: Path, frame: pd.DataFrame) -> str:
    frame.to_csv(
        path,
        index=False,
        lineterminator="\n",
    )
    return sha256_file(path)


def main() -> None:
    args = parse_args()
    output_root = args.output_root.expanduser().resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    protocol_sha = validate_protocol(
        args.committed_protocol_sha256,
        args.execute_sensitivity,
    )
    audit = validate_leakage_audit()
    canonical = load_canonical_runner()

    (
        full_status,
        status,
        arrays,
        retained_positions,
        canonical_input_hashes,
        excluded,
        category_identity_counts,
    ) = prepare_retained_inputs(canonical)

    retained_rows = len(status)
    excluded_rows = len(excluded)

    fixed_fold_rows = (
        status.groupby("corrected_fold_id", sort=True)
        .size()
        .astype(int)
        .to_dict()
    )
    fixed_fold_identities = (
        status.groupby("corrected_fold_id", sort=True)
        ["corrected_garment_id"]
        .nunique()
        .astype(int)
        .to_dict()
    )

    print("Target-text sensitivity validation: PASS")
    print(f"Frozen protocol SHA-256: {protocol_sha}")
    print(
        "Excluded identities: "
        + ", ".join(EXCLUDED_IDENTITIES)
    )
    print(f"Excluded rows: {excluded_rows}")
    print(f"Retained rows: {retained_rows}")
    print(
        "Retained identities: "
        f"{status['corrected_garment_id'].nunique()}"
    )
    print(f"Retained classes: {status['category'].nunique()}")
    print(f"Fixed-fold retained rows: {fixed_fold_rows}")
    print(
        "Fixed-fold retained identities: "
        f"{fixed_fold_identities}"
    )
    print(
        "Cardigan identities retained: "
        f"{category_identity_counts['Cardigan']}"
    )
    print(
        "Tunic identities retained: "
        f"{category_identity_counts['Tunic']}"
    )
    print("Canonical frozen feature hashes: PASS")
    print("Leakage audit linkage: PASS")

    if not args.execute_sensitivity:
        print(
            "STOP — sensitivity outcome remains disabled. "
            "No classifier, prediction, predictive metric, "
            "bootstrap, repeated partition, or permutation "
            "was computed."
        )
        return

    y = status["category"].astype(str).to_numpy()
    fold_ids = (
        status["corrected_fold_id"]
        .astype(int)
        .to_numpy()
    )

    clean = canonical.primary_condition(
        "CLEAN_TARGET_TEXT_IDENTITY_EXCLUSION",
        arrays["clean_m135"],
        arrays["clean_ra14"],
        y,
        fold_ids,
    )

    bootstrap = sensitivity_identity_bootstrap(
        canonical,
        status,
        y,
        clean["pred_m"],
        clean["pred_aug"],
    )
    bootstrap_sum = canonical.bootstrap_summary(
        bootstrap,
        clean["pooled"],
    )

    repeated = sensitivity_repeated_grouped_robustness(
        canonical,
        full_status,
        retained_positions,
        status,
        arrays["clean_m135"],
        arrays["clean_ra14"],
        y,
    )

    alignment, alignment_sum = (
        sensitivity_alignment_permutation(
            canonical,
            status,
            arrays["clean_m135"],
            arrays["clean_ra14"],
            y,
            fold_ids,
            clean["pooled"],
        )
    )

    oof = status[
        [
            "row_index",
            "original_row_index",
            "relative_path",
            "category",
            "corrected_garment_id",
            "corrected_fold_id",
        ]
    ].copy()

    oof["clean_pred_m"] = clean["pred_m"]
    oof["clean_pred_m_ra14"] = clean["pred_aug"]

    pooled = pd.DataFrame([clean["pooled"]])
    fold_metrics = clean["fold_metrics"].copy()

    paths = {
        "oof_predictions":
            output_root
            / f"{OUTPUT_PREFIX}_oof_predictions.csv",
        "pooled_metrics":
            output_root
            / f"{OUTPUT_PREFIX}_pooled_metrics.csv",
        "fold_metrics":
            output_root
            / f"{OUTPUT_PREFIX}_fold_metrics.csv",
        "bootstrap":
            output_root
            / f"{OUTPUT_PREFIX}_identity_bootstrap.csv",
        "repeated":
            output_root
            / f"{OUTPUT_PREFIX}_repeated_partitions.csv",
        "alignment":
            output_root
            / f"{OUTPUT_PREFIX}_alignment_permutation.csv",
        "summary":
            output_root
            / f"{OUTPUT_PREFIX}_summary.json",
    }

    output_hashes = {
        "oof_predictions":
            save_csv(paths["oof_predictions"], oof),
        "pooled_metrics":
            save_csv(paths["pooled_metrics"], pooled),
        "fold_metrics":
            save_csv(paths["fold_metrics"], fold_metrics),
        "bootstrap":
            save_csv(paths["bootstrap"], bootstrap),
        "repeated":
            save_csv(paths["repeated"], repeated),
        "alignment":
            save_csv(paths["alignment"], alignment),
    }

    repeated_summary = {
        "macro_f1": {
            "mean": float(
                repeated["delta_macro_f1"].mean()
            ),
            "sd": float(
                repeated["delta_macro_f1"].std(ddof=1)
            ),
            "min": float(
                repeated["delta_macro_f1"].min()
            ),
            "max": float(
                repeated["delta_macro_f1"].max()
            ),
            "positive_repeats": int(
                (repeated["delta_macro_f1"] > 0).sum()
            ),
        },
        "balanced_accuracy": {
            "mean": float(
                repeated[
                    "delta_balanced_accuracy"
                ].mean()
            ),
            "sd": float(
                repeated[
                    "delta_balanced_accuracy"
                ].std(ddof=1)
            ),
            "min": float(
                repeated[
                    "delta_balanced_accuracy"
                ].min()
            ),
            "max": float(
                repeated[
                    "delta_balanced_accuracy"
                ].max()
            ),
            "positive_repeats": int(
                (
                    repeated[
                        "delta_balanced_accuracy"
                    ]
                    > 0
                ).sum()
            ),
        },
    }

    summary = {
        "schema_version": 1,
        "experiment":
            "CLO-SKET Experiment 06 corrective reanalysis",
        "analysis":
            "post-outcome target-text identity-exclusion sensitivity",
        "stage":
            "POST_OUTCOME_TARGET_TEXT_SENSITIVITY_COMPLETE",
        "confirmatory_status": "post_outcome_sensitivity_only",
        "excluded_identities": list(EXCLUDED_IDENTITIES),
        "excluded_rows": int(excluded_rows),
        "retained_rows": int(retained_rows),
        "retained_identities": int(
            status["corrected_garment_id"].nunique()
        ),
        "retained_classes": int(
            status["category"].nunique()
        ),
        "fixed_fold_rows": {
            str(k): int(v)
            for k, v in fixed_fold_rows.items()
        },
        "fixed_fold_identities": {
            str(k): int(v)
            for k, v in fixed_fold_identities.items()
        },
        "category_identity_counts": {
            str(k): int(v)
            for k, v in category_identity_counts.items()
        },
        "estimator": canonical.ESTIMATOR,
        "bootstrap_replicates":
            canonical.BOOTSTRAP_REPLICATES,
        "alignment_permutations":
            canonical.ALIGNMENT_PERMUTATIONS,
        "repeated_partition_seeds":
            canonical.REPEATED_SEEDS,
        "protocol_sha256": protocol_sha,
        "leakage_audit": audit,
        "canonical_input_hashes":
            canonical_input_hashes,
        "primary_results": clean["pooled"],
        "identity_bootstrap": bootstrap_sum,
        "repeated_partitions": repeated_summary,
        "alignment_permutation": alignment_sum,
        "output_sha256": output_hashes,
        "classifier_fitted": True,
        "prediction_computed": True,
        "predictive_metric_computed": True,
        "bootstrap_computed": True,
        "repeated_partitions_computed": True,
        "permutation_computed": True,
        "interpretation_gate":
            "descriptive_post_outcome_only_no_new_confirmatory_claim",
    }

    paths["summary"].write_text(
        json.dumps(
            summary,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    print(
        "\nExperiment 06 target-text sensitivity run: COMPLETE"
    )
    print(
        "Status: post-outcome sensitivity only; "
        "no new confirmatory claim."
    )
    print(f"Summary: {paths['summary']}")


if __name__ == "__main__":
    main()
