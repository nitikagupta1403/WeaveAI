"""Pre-outcome implementation preflight for corrective Experiment 06.

This script verifies frozen corrective prerequisites, frozen feature artifacts,
and final implementation hashes/environment metadata. It MUST NOT fit a
classifier or compute a predictive outcome.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from importlib import metadata
from pathlib import Path

import pandas as pd


EXPECTED = {
    "rows": 2300,
    "categories": 23,
    "identities": 230,
    "identity_map_sha256": "c2510fb74b452da22d3b4e9badb46cfe4cbd2653c0ee99acb573942262c1ac2b",
    "identity_fold_map_sha256": "82cda5ce42be46cb939bf15b50171d21c2b62df3d3e065eb8a32bc4e587cca3b",
    "fold_summary_sha256": "7d0df33b09f9e47857877003e7d59705d87e9b922a8cf21a2c8a9c4889bef0d7",
    "annotation_status_sha256": "b83b74b6ff0f25fa8bb4474265d2f06c900bbcd3243b2cc332152e3c74cde55e",
    "annotation_preflight_stage": "PRE_OUTCOME_ANNOTATION_CONTROL_PREFLIGHT",
    "test_rows": [459, 460, 461, 460, 460],
    "test_identities": 46,
}
SOURCE_CANDIDATE_COMMIT = "60063623eedde05ed7c351c3c947a605f6be5344"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def package_version(name: str) -> str:
    try:
        return metadata.version(name)
    except metadata.PackageNotFoundError:
        return "NOT_INSTALLED"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--evidence-root",
        type=Path,
        default=Path("papers/CLO-SKET/evidence/Experiment_06_Corrective"),
    )
    p.add_argument(
        "--code-root",
        type=Path,
        default=Path("papers/CLO-SKET/Codes_paper_I"),
    )
    p.add_argument(
        "--output",
        type=Path,
        default=Path(
            "papers/CLO-SKET/evidence/Experiment_06_Corrective/"
            "experiment06_execution_lock_preflight.json"
        ),
    )
    return p.parse_args()


def require_hash(path: Path, expected: str, label: str) -> str:
    observed = sha256_file(path)
    if observed != expected:
        raise RuntimeError(f"{label} hash mismatch: {observed} != {expected}")
    return observed


def main() -> None:
    args = parse_args()
    evidence = args.evidence_root
    code = args.code_root
    corrective = code / "Experiment_06_Corrective"

    identity_map = evidence / "experiment06_corrected_identity_map.csv"
    identity_fold_map = evidence / "experiment06_corrected_identity_fold_map.csv"
    fold_summary = evidence / "experiment06_corrected_fold_summary.csv"
    annotation_status = evidence / "experiment06_annotation_status.csv"
    annotation_preflight = evidence / "experiment06_annotation_control_preflight.json"
    feature_manifest = evidence / "experiment06_corrective_feature_manifest.json"

    identity_hash = require_hash(
        identity_map, EXPECTED["identity_map_sha256"], "corrected identity map"
    )
    identity_fold_hash = require_hash(
        identity_fold_map,
        EXPECTED["identity_fold_map_sha256"],
        "corrected identity/fold map",
    )
    fold_summary_hash = require_hash(
        fold_summary, EXPECTED["fold_summary_sha256"], "corrected fold summary"
    )
    annotation_status_hash = require_hash(
        annotation_status,
        EXPECTED["annotation_status_sha256"],
        "annotation status",
    )

    annotation_report = json.loads(annotation_preflight.read_text(encoding="utf-8"))
    if annotation_report.get("stage") != EXPECTED["annotation_preflight_stage"]:
        raise RuntimeError("Annotation preflight stage mismatch")
    if annotation_report.get("preflight_passed") is not True:
        raise RuntimeError("Annotation-control preflight is not PASS")
    if annotation_report.get("predictive_outcome_computed") is not False:
        raise RuntimeError("Annotation-control report indicates an outcome was computed")

    identity = pd.read_csv(identity_map, keep_default_na=False)
    folds = pd.read_csv(fold_summary, keep_default_na=False)
    annotation = pd.read_csv(annotation_status, keep_default_na=False)

    if len(identity) != EXPECTED["rows"] or len(annotation) != EXPECTED["rows"]:
        raise RuntimeError("Corrective row count mismatch")
    if identity["category"].nunique() != EXPECTED["categories"]:
        raise RuntimeError("Category count mismatch")
    if identity["corrected_garment_id"].nunique() != EXPECTED["identities"]:
        raise RuntimeError("Corrected identity count mismatch")

    identity = identity.sort_values("row_index").reset_index(drop=True)
    annotation = annotation.sort_values("row_index").reset_index(drop=True)
    if identity["relative_path"].tolist() != annotation["relative_path"].tolist():
        raise RuntimeError("Identity and annotation path order mismatch")
    if identity["corrected_garment_id"].tolist() != annotation["corrected_garment_id"].tolist():
        raise RuntimeError("Identity and annotation garment IDs mismatch")
    if (
        identity["corrected_fold_id"].astype(int).tolist()
        != annotation["corrected_fold_id"].astype(int).tolist()
    ):
        raise RuntimeError("Identity and annotation fold IDs mismatch")

    folds = folds.sort_values("fold").reset_index(drop=True)
    observed_test_rows = folds["test_rows"].astype(int).tolist()
    if observed_test_rows != EXPECTED["test_rows"]:
        raise RuntimeError(
            f"Corrected primary test-row counts mismatch: {observed_test_rows}"
        )
    if not (
        folds["test_identities"].astype(int) == EXPECTED["test_identities"]
    ).all():
        raise RuntimeError("Corrected test-identity count mismatch")
    if not (
        folds["overlapping_corrected_identities"].astype(int) == 0
    ).all():
        raise RuntimeError("Corrected identity overlap is non-zero")

    required_implementation = {
        "core_ra14_notebook": code / "01_Core_Radial_Angular_14D_and_Reconstruction.ipynb",
        "historical_e06_evidence_record": code / "06_Experiment_06_Evidence_Record.md",
        "prospective_lock": code / "Experiment_06_Corrective_Reanalysis_PROSPECTIVE_LOCK.md",
        "execution_implementation_lock": corrective / "EXECUTION_IMPLEMENTATION_LOCK.md",
        "identity_builder": corrective / "01_build_corrected_identity_map.py",
        "annotation_preflight_code": corrective / "02_annotation_control_preflight.py",
        "execution_preflight_code": corrective / "03_execution_lock_preflight.py",
        "historical_m135_definition_lock": corrective / "M135_HISTORICAL_DEFINITION_LOCK.md",
        "raw_clean_feature_extractor": corrective / "04_extract_raw_clean_features.py",
        "corrective_outcome_runner": corrective / "05_run_corrective_experiment06.py",
    }
    missing_implementation = [
        name for name, path in required_implementation.items() if not path.is_file()
    ]

    feature_artifacts = {
        "feature_manifest": feature_manifest,
        "raw_m135": evidence / "experiment06_corrective_raw_m135.npy",
        "raw_ra14": evidence / "experiment06_corrective_raw_ra14.npy",
        "clean_m135": evidence / "experiment06_corrective_clean_m135.npy",
        "clean_ra14": evidence / "experiment06_corrective_clean_ra14.npy",
    }
    missing_features = [
        name for name, path in feature_artifacts.items() if not path.is_file()
    ]

    feature_checks = {
        "feature_manifest_present": not missing_features,
        "historical_raw_m135_exact_match": False,
        "historical_raw_ra14_exact_match": False,
        "feature_manifest_no_classifier": False,
        "feature_manifest_no_prediction": False,
        "feature_manifest_no_metric": False,
        "feature_manifest_outcome_locked": False,
    }

    if feature_manifest.is_file():
        feature_report = json.loads(feature_manifest.read_text(encoding="utf-8"))
        hist = feature_report.get("historical_reproduction_checks", {})
        feature_checks.update(
            {
                "historical_raw_m135_exact_match": hist.get("raw_m135_exact_match") is True,
                "historical_raw_ra14_exact_match": hist.get("raw_ra14_exact_match") is True,
                "feature_manifest_no_classifier": feature_report.get("classifier_fitted") is False,
                "feature_manifest_no_prediction": feature_report.get("prediction_computed") is False,
                "feature_manifest_no_metric": feature_report.get("predictive_metric_computed") is False,
                "feature_manifest_outcome_locked": feature_report.get("outcome_execution_unlocked") is False,
            }
        )

    implementation_hashes = {
        name: sha256_file(path)
        for name, path in required_implementation.items()
        if path.is_file()
    }
    feature_file_hashes = {
        name: sha256_file(path)
        for name, path in feature_artifacts.items()
        if path.is_file()
    }

    environment = {
        "python": platform.python_version(),
        "implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "numpy": package_version("numpy"),
        "pandas": package_version("pandas"),
        "scipy": package_version("scipy"),
        "scikit_learn": package_version("scikit-learn"),
        "pillow": package_version("Pillow"),
    }

    feature_gate_passed = not missing_features and all(feature_checks.values())
    preflight_passed = not missing_implementation and feature_gate_passed

    report = {
        "schema_version": 2,
        "experiment": "CLO-SKET Experiment 06 corrective reanalysis",
        "stage": "PRE_OUTCOME_EXECUTION_IMPLEMENTATION_PREFLIGHT",
        "source_candidate_commit": SOURCE_CANDIDATE_COMMIT,
        "prerequisite_checks": {
            "corrected_identity_map_hash_locked": True,
            "corrected_identity_fold_map_hash_locked": True,
            "corrected_fold_summary_hash_locked": True,
            "annotation_status_hash_locked": True,
            "annotation_control_preflight_passed": True,
            "row_order_consistent": True,
            "zero_corrected_identity_overlap": True,
            "corrected_test_row_counts_verified": True,
            **feature_checks,
        },
        "prerequisite_hashes": {
            "corrected_identity_map_sha256": identity_hash,
            "corrected_identity_fold_map_sha256": identity_fold_hash,
            "corrected_fold_summary_sha256": fold_summary_hash,
            "annotation_status_sha256": annotation_status_hash,
            "annotation_control_preflight_sha256": sha256_file(annotation_preflight),
        },
        "implementation_source_sha256": implementation_hashes,
        "feature_artifact_file_sha256": feature_file_hashes,
        "environment": environment,
        "missing_required_implementation": missing_implementation,
        "missing_feature_artifacts": missing_features,
        "feature_matrix_generated": True,
        "classifier_fitted": False,
        "predictive_outcome_computed": False,
        "outcome_execution_unlocked": preflight_passed,
        "preflight_passed": preflight_passed,
        "stop": (
            "PRE-OUTCOME STOP: implementation/provenance/hash inspection only. "
            "Frozen feature matrices already exist, but no classifier fitting, "
            "prediction, predictive metric, bootstrap, repeated partition, or "
            "alignment permutation was computed by this preflight."
        ),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    if preflight_passed:
        print("Experiment 06 execution implementation preflight: PASS")
        print(
            "All implementation and frozen-feature prerequisites are present. "
            "Outcome execution remains blocked until this PASS report is committed."
        )
    else:
        print("Experiment 06 execution implementation preflight: BLOCKED")
        if missing_implementation:
            print("Missing implementation:", ", ".join(missing_implementation))
        if missing_features:
            print("Missing feature artifacts:", ", ".join(missing_features))
        failed_feature_checks = [k for k, v in feature_checks.items() if not v]
        if failed_feature_checks:
            print("Failed feature checks:", ", ".join(failed_feature_checks))

    print(f"Report: {args.output}")
    print("STOP — no classifier or predictive outcome was computed.")


if __name__ == "__main__":
    main()
