"""Freeze the pre-outcome manual-review cohort for Experiment 08 boxes."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import pandas as pd

from preprocess_audit import sha256_file


RETENTION_THRESHOLD = 0.98
QC_PER_CATEGORY = 13
QC_EXTRA_CATEGORY = "A-Line"
QC_EXTRA_COUNT = 1
QC_SALT = "CLO-SKET_EXPERIMENT08_BOX_QC_V1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--proposal-csv", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    return parser.parse_args()


def deterministic_score(relative_path: str) -> str:
    payload = f"{QC_SALT}\n{relative_path}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def main() -> None:
    args = parse_args()
    proposals = pd.read_csv(args.proposal_csv, keep_default_na=False)
    if len(proposals) != 2300:
        raise RuntimeError(f"Expected 2300 proposals, found {len(proposals)}")
    if proposals["relative_path"].duplicated().any():
        raise RuntimeError("Proposal paths are not unique")

    boundary = proposals["touches_image_boundary"].astype(bool)
    low_retention = proposals["retained_ink_fraction"] < RETENTION_THRESHOLD
    mandatory_mask = low_retention | boundary
    mandatory = proposals.loc[mandatory_mask].copy()
    mandatory["selection_reason"] = mandatory.apply(
        lambda row: "+".join(
            reason
            for active, reason in [
                (
                    row["retained_ink_fraction"] < RETENTION_THRESHOLD,
                    "retention_below_0.98",
                ),
                (
                    bool(row["touches_image_boundary"]),
                    "touches_image_boundary",
                ),
            ]
            if active
        ),
        axis=1,
    )
    mandatory["qc_score"] = ""

    remainder = proposals.loc[~mandatory_mask].copy()
    remainder["qc_score"] = remainder["relative_path"].map(
        deterministic_score
    )
    qc_parts = []
    categories = sorted(proposals["category"].unique().tolist())
    if len(categories) != 23:
        raise RuntimeError(f"Expected 23 categories, found {len(categories)}")
    for category in categories:
        count = QC_PER_CATEGORY + (
            QC_EXTRA_COUNT if category == QC_EXTRA_CATEGORY else 0
        )
        candidates = remainder[remainder["category"] == category].sort_values(
            ["qc_score", "relative_path"]
        )
        if len(candidates) < count:
            raise RuntimeError(
                f"Not enough QC candidates for {category}: {len(candidates)}"
            )
        selected = candidates.head(count).copy()
        selected["selection_reason"] = "deterministic_stratified_qc"
        qc_parts.append(selected)
    qc = pd.concat(qc_parts, ignore_index=True)

    if len(mandatory) != 628:
        raise RuntimeError(f"Frozen mandatory count mismatch: {len(mandatory)}")
    if len(qc) != 300:
        raise RuntimeError(f"Frozen QC count mismatch: {len(qc)}")
    if set(mandatory["relative_path"]) & set(qc["relative_path"]):
        raise RuntimeError("Mandatory and QC cohorts overlap")

    mandatory = mandatory.sort_values(
        ["review_priority_rank", "relative_path"]
    )
    qc = qc.sort_values(["category", "qc_score", "relative_path"])
    selection = pd.concat([mandatory, qc], ignore_index=True)
    selection.insert(0, "review_order", range(1, len(selection) + 1))
    selection["selection_cohort"] = [
        "mandatory" if index < len(mandatory) else "quality_control"
        for index in range(len(selection))
    ]

    args.output_root.mkdir(parents=True, exist_ok=True)
    selection_path = args.output_root / "experiment08_box_review_selection.csv"
    selection.to_csv(selection_path, index=False)

    report = {
        "stage": "PRE_OUTCOME_BOX_REVIEW_SELECTION",
        "learned_features_extracted": False,
        "classifier_fitted": False,
        "predictive_outcome_computed": False,
        "retention_threshold": RETENTION_THRESHOLD,
        "mandatory_rule": (
            "retained ink fraction below 0.98 OR proposal touches image boundary"
        ),
        "mandatory_count": len(mandatory),
        "quality_control_design": {
            "method": "deterministic SHA-256 ranking stratified by category",
            "salt": QC_SALT,
            "per_category": QC_PER_CATEGORY,
            "extra_category": QC_EXTRA_CATEGORY,
            "extra_count": QC_EXTRA_COUNT,
            "total": len(qc),
            "zero_failure_approximate_95_percent_upper_bound": 3 / len(qc),
        },
        "total_review_count": len(selection),
        "unreviewed_remainder_count": 2300 - len(selection),
        "proposal_csv_sha256": sha256_file(args.proposal_csv),
        "selection_csv_sha256": sha256_file(selection_path),
        "mandatory_by_category": {
            key: int(value)
            for key, value in mandatory.groupby("category").size().items()
        },
        "qc_by_category": {
            key: int(value)
            for key, value in qc.groupby("category").size().items()
        },
    }
    report_path = args.output_root / "experiment08_box_review_selection.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"PASS: frozen review selection written; report={report_path}")
    print(f"Selection: {selection_path}")
    print("STOP: selection used no learned feature or predictive outcome")


if __name__ == "__main__":
    main()
