#!/usr/bin/env python3
"""Verify deposited historical Experiment-06 evidence.

This script is intentionally read-only. It validates the frozen public
Experiment-06 evidence bundle: hash locks, structural facts, result values,
and claim-lock consistency. It does NOT reconstruct M/R/A from source TIFFs,
fit classifiers, regenerate OOF predictions, or recompute scientific outcomes.
It therefore does NOT establish end-to-end computational reproducibility of
historical Experiment 06.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "Experiment_06"
PUBLIC_MANIFEST = REPO_ROOT / "evidence" / "PUBLIC_EVIDENCE_MANIFEST.json"

REQUIRED_FILES = {
    "experiment06_primary_results.csv",
    "experiment06_provenance_hashes.json",
    "experiment06_repeated_grouped_cv.csv",
    "experiment06_alignment_permutation_summary.csv",
    "experiment06_claim_lock.json",
    "CLO_SKET_EXPERIMENT06_FINAL_MANIFEST.txt",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def assert_file(path: Path, label: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Missing required {label}: {path}")


def load_public_manifest() -> dict:
    assert_file(PUBLIC_MANIFEST, "public evidence manifest")
    return json.loads(PUBLIC_MANIFEST.read_text(encoding="utf-8"))


def validate_manifest_hashes() -> dict:
    manifest = load_public_manifest()
    expected = {
        item["file"]: item["sha256"]
        for item in manifest["files"]
        if item["experiment"] == "Experiment_06"
    }
    missing = sorted(REQUIRED_FILES.difference(expected.keys()))
    if missing:
        raise RuntimeError(f"Public manifest is missing required Experiment-06 hashes: {missing}")

    observed = {}
    for filename, expected_hash in expected.items():
        path = REPO_ROOT / "evidence" / "Experiment_06" / filename
        if filename == "CLO_SKET_EXPERIMENT06_FINAL_MANIFEST.txt":
            path = REPO_ROOT / "evidence" / "Experiment_06" / filename
        assert_file(path, filename)
        observed[filename] = sha256_file(path)
        if observed[filename] != expected_hash:
            raise RuntimeError(
                f"Hash mismatch for {filename}: observed {observed[filename]}, expected {expected_hash}"
            )
    return {"bundle": manifest["bundle"], "files": observed}


def validate_primary_results() -> dict:
    path = EVIDENCE_ROOT / "experiment06_primary_results.csv"
    df = pd.read_csv(path)
    expected = {
        "feature_set": ["R", "A", "R+A", "M", "M+R", "M+A", "M+R+A"],
        "dimensions": [8, 6, 14, 135, 143, 141, 149],
    }
    if list(df["feature_set"]) != expected["feature_set"]:
        raise RuntimeError(f"Unexpected primary-results ordering: {list(df['feature_set'])}")
    if list(df["dimensions"]) != expected["dimensions"]:
        raise RuntimeError(f"Unexpected dimensions ordering: {list(df['dimensions'])}")

    row = df[df["feature_set"] == "M+R+A"].iloc[0]
    summary = {
        "M_macro_f1": float(df.loc[df["feature_set"] == "M", "macro_f1"].iloc[0]),
        "M_plus_RA_macro_f1": float(row["macro_f1"]),
        "delta_macro_f1": float(row["macro_f1"]) - float(df.loc[df["feature_set"] == "M", "macro_f1"].iloc[0]),
        "M_plus_RA_balanced_accuracy": float(row["balanced_accuracy"]),
    }
    if abs(summary["delta_macro_f1"] - 0.03797663379050664) > 1e-12:
        raise RuntimeError(f"Unexpected primary delta: {summary['delta_macro_f1']}")
    return summary


def validate_hash_lock() -> dict:
    path = EVIDENCE_ROOT / "experiment06_provenance_hashes.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    expected = {
        "M": "aa31d0559f302f66633eff315b8c3db0e939958c47cc171cd7d2b75c531d33b7",
        "R": "bcae5739ad7cb62e28ac5305f819f62fcc8f3fdae816725c320b0aec1b540453",
        "A": "63164eb16b11b43d7d52ba7f29ca396f0432b4c65bd61cc79c45d333fa46ec18",
        "R+A": "ea660e0c53dc285d48635d9bdca74b7f7dd32eacd9cd225cd336d6147d5c7828",
        "garment": "8f54e0416dc8e598153464bf4caaf64d12c869f30de3b15a003cd715d4da7434",
        "category": "5f04a8c39e925e96c85d7175cb2c5b46ca37625d959a9134e5592a2946c45114",
        "fold": "abe2afb7e23d21b4bec63b45f2dd7c69bc8f8fcffe559e954cfd67228e0a1c22",
    }
    for key, value in expected.items():
        if payload.get(key) != value:
            raise RuntimeError(f"Unexpected provenance hash for {key}: {payload.get(key)} != {value}")
    return payload


def validate_alignment_control() -> dict:
    path = EVIDENCE_ROOT / "experiment06_alignment_permutation_summary.csv"
    summary = pd.read_csv(path)
    if summary.iloc[0].to_dict().get("empirical_p") != 0.7626186906546727:
        raise RuntimeError("Alignment-control p-value does not match the frozen value.")
    return summary.iloc[0].to_dict()


def validate_repeated_cv() -> dict:
    path = EVIDENCE_ROOT / "experiment06_repeated_grouped_cv.csv"
    df = pd.read_csv(path)
    if len(df) != 10:
        raise RuntimeError(f"Expected 10 repeated grouped-CV rows, found {len(df)}")
    observed = float(df["delta_full_macro_f1"].mean())
    expected = 0.03225279854129517
    if abs(observed - expected) > 1e-12:
        raise RuntimeError(f"Repeated grouped-CV mean delta mismatch: {observed} != {expected}")
    return {
        "mean_delta_macro_f1": observed,
        "first_row": df.iloc[0].to_dict(),
    }


def validate_claim_lock() -> dict:
    path = EVIDENCE_ROOT / "experiment06_claim_lock.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    required = {
        "PRIMARY_SUPPORTED_CLAIM",
        "SECONDARY_SUPPORTED_CLAIM",
        "ALIGNMENT_INTERPRETATION",
    }
    missing = required.difference(payload.keys())
    if missing:
        raise RuntimeError(f"Claim lock is missing required keys: {sorted(missing)}")
    return payload


def main() -> int:
    print("=" * 96)
    print("CLO-SKET — EXPERIMENT 06 — HISTORICAL EVIDENCE VERIFIER")
    print("=" * 96)

    manifest_status = validate_manifest_hashes()
    hash_lock = validate_hash_lock()
    primaries = validate_primary_results()
    alignment = validate_alignment_control()
    repeated = validate_repeated_cv()
    claim_lock = validate_claim_lock()

    print("Bundle                         :", manifest_status["bundle"])
    print("Public manifest files checked :", len(manifest_status["files"]))
    print("M hash                        :", hash_lock["M"])
    print("R+A hash                     :", hash_lock["R+A"])
    print("Fold hash                    :", hash_lock["fold"])
    print("Primary M macro-F1           :", primaries["M_macro_f1"])
    print("Primary M+R+A macro-F1       :", primaries["M_plus_RA_macro_f1"])
    print("Primary delta macro-F1       :", primaries["delta_macro_f1"])
    print("Alignment null empirical p   :", alignment["empirical_p"])
    print("Repeated CV delta mean       :", repeated["mean_delta_macro_f1"])
    print("Primary claim                :", claim_lock["PRIMARY_SUPPORTED_CLAIM"])
    print("Interpretation               :", claim_lock["ALIGNMENT_INTERPRETATION"])
    print("=" * 96)
    print("HISTORICAL EVIDENCE VERIFICATION: PASS")
    print("This verifier checks deposited historical evidence only.")
    print("It does not reconstruct M/R/A from source TIFFs, fit classifiers, regenerate OOF predictions, or recompute scientific outcomes.")
    print("It does not establish end-to-end computational reproducibility of historical Experiment 06.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
