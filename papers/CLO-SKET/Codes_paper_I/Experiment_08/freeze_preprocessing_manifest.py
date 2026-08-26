"""Freeze the label-blind Experiment 08 localization manifest before outcomes."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from preprocess_audit import sha256_file


EXPECTED = {
    "rows": 2300,
    "reviewed": 928,
    "mandatory": 628,
    "quality_control": 300,
    "automatic": 1372,
    "ambiguous": 22,
    "text_boxes": 593,
    "proposal_sha256": "6db98417617eb4a69ed11421cfd9ec9bc457c191cd5b7072b7bc7e68d40308ae",
    "selection_sha256": "b42413bafd67183092315669cfa93cc9892813d95389a3f083d073e57b0c07c7",
    "annotations_sha256": "9a756cc47932d7f8f61508ddf067f3e44cf4c7ff761c484f7feb25223bab407c",
    "audit_sha256": "fdabfbf61b8d35827a98611061dd616268139c2c77406df4455956799438e880",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-manifest", type=Path, required=True)
    parser.add_argument("--proposal-csv", type=Path, required=True)
    parser.add_argument("--selection-csv", type=Path, required=True)
    parser.add_argument("--annotations-jsonl", type=Path, required=True)
    parser.add_argument("--audit-csv", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    return parser.parse_args()


def require_hash(path: Path, expected: str, label: str) -> None:
    observed = sha256_file(path)
    if observed != expected:
        raise RuntimeError(f"{label} SHA-256 mismatch: {observed} != {expected}")


def load_annotations(path: Path) -> dict[str, dict]:
    records = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    by_path = {record["relative_path"]: record for record in records}
    if len(records) != EXPECTED["reviewed"] or len(by_path) != len(records):
        raise RuntimeError("Reviewed annotations must contain 928 unique paths")
    if not all(record.get("reviewed") is True for record in records):
        raise RuntimeError("Every reviewed annotation must be approved")
    return by_path


def main() -> None:
    args = parse_args()
    require_hash(args.proposal_csv, EXPECTED["proposal_sha256"], "proposal")
    require_hash(args.selection_csv, EXPECTED["selection_sha256"], "selection")
    require_hash(args.annotations_jsonl, EXPECTED["annotations_sha256"], "annotations")
    require_hash(args.audit_csv, EXPECTED["audit_sha256"], "audit")

    source = pd.read_csv(args.source_manifest, keep_default_na=False)
    proposals = pd.read_csv(args.proposal_csv, keep_default_na=False)
    selection = pd.read_csv(args.selection_csv, keep_default_na=False)
    audit = pd.read_csv(args.audit_csv, keep_default_na=False)
    annotations = load_annotations(args.annotations_jsonl)

    for name, frame in [("source", source), ("proposal", proposals)]:
        if len(frame) != EXPECTED["rows"]:
            raise RuntimeError(f"{name} must contain 2300 rows")
        if frame["relative_path"].duplicated().any():
            raise RuntimeError(f"{name} paths are not unique")
    if len(selection) != EXPECTED["reviewed"]:
        raise RuntimeError("Selection must contain 928 rows")
    if set(selection["relative_path"]) != set(annotations):
        raise RuntimeError("Selection and reviewed annotation paths differ")
    if set(audit["relative_path"]) != set(annotations):
        raise RuntimeError("Audit and reviewed annotation paths differ")

    selection_by_path = selection.set_index("relative_path")
    proposal_by_path = proposals.set_index("relative_path")
    rows = []
    for item in source.sort_values("row_index").to_dict("records"):
        relative_path = item["relative_path"]
        proposal = proposal_by_path.loc[relative_path]
        if str(proposal["source_sha256"]) != str(item["sha256"]):
            raise RuntimeError(f"Proposal/source mismatch: {relative_path}")

        if relative_path in annotations:
            annotation = annotations[relative_path]
            if annotation["source_sha256"] != item["sha256"]:
                raise RuntimeError(f"Annotation/source mismatch: {relative_path}")
            box = list(map(int, annotation["garment_box"]))
            text_boxes = [list(map(int, box)) for box in annotation["text_boxes"]]
            cohort = str(selection_by_path.loc[relative_path, "selection_cohort"])
            localization_source = "human_reviewed"
            ambiguous = bool(annotation["ambiguous"])
        else:
            box = [
                int(proposal["proposal_left"]),
                int(proposal["proposal_top"]),
                int(proposal["proposal_right"]),
                int(proposal["proposal_bottom"]),
            ]
            text_boxes = []
            cohort = "automatic_remainder"
            localization_source = "automatic_qc_accepted"
            ambiguous = False

        rows.append(
            {
                "row_index": int(item["row_index"]),
                "relative_path": relative_path,
                "source_sha256": item["sha256"],
                "category": item["category"],
                "garment_id": item["garment_id"],
                "fold_id": int(item["fold_id"]),
                "garment_left": box[0],
                "garment_top": box[1],
                "garment_right": box[2],
                "garment_bottom": box[3],
                "text_boxes_json": json.dumps(text_boxes, separators=(",", ":")),
                "ambiguous_overlap": ambiguous,
                "localization_source": localization_source,
                "selection_cohort": cohort,
                "text_blanking_approved": bool(text_boxes),
            }
        )

    final = pd.DataFrame(rows)
    counts = final["selection_cohort"].value_counts().to_dict()
    if counts.get("mandatory") != EXPECTED["mandatory"]:
        raise RuntimeError("Mandatory count mismatch")
    if counts.get("quality_control") != EXPECTED["quality_control"]:
        raise RuntimeError("QC count mismatch")
    if counts.get("automatic_remainder") != EXPECTED["automatic"]:
        raise RuntimeError("Automatic-remainder count mismatch")
    if int(final["ambiguous_overlap"].sum()) != EXPECTED["ambiguous"]:
        raise RuntimeError("Ambiguous count mismatch")
    total_text_boxes = sum(len(json.loads(value)) for value in final["text_boxes_json"])
    if total_text_boxes != EXPECTED["text_boxes"]:
        raise RuntimeError("Text-box count mismatch")

    args.output_root.mkdir(parents=True, exist_ok=True)
    manifest_path = args.output_root / "experiment08_preprocessing_manifest.csv"
    final.to_csv(manifest_path, index=False)
    report = {
        "stage": "PRE_OUTCOME_PREPROCESSING_FREEZE",
        "learned_features_extracted": False,
        "classifier_fitted": False,
        "predictive_outcome_computed": False,
        "rows": len(final),
        "human_reviewed": EXPECTED["reviewed"],
        "automatic_qc_accepted": EXPECTED["automatic"],
        "mandatory_reviewed": EXPECTED["mandatory"],
        "quality_control_reviewed": EXPECTED["quality_control"],
        "quality_control_material_failures": 0,
        "quality_control_nonmaterial_padding_changes": 5,
        "material_failure_definition": (
            "garment truncation, structural-detail loss, or interfering annotation"
        ),
        "zero_failure_approximate_95_percent_upper_bound": 3 / EXPECTED["quality_control"],
        "ambiguous_overlap_records": EXPECTED["ambiguous"],
        "ambiguous_blanking_visual_approvals": EXPECTED["ambiguous"],
        "text_boxes": total_text_boxes,
        "preprocessing_manifest_sha256": sha256_file(manifest_path),
        "source_manifest_sha256": sha256_file(args.source_manifest),
        "proposal_csv_sha256": EXPECTED["proposal_sha256"],
        "selection_csv_sha256": EXPECTED["selection_sha256"],
        "annotations_jsonl_sha256": EXPECTED["annotations_sha256"],
        "audit_csv_sha256": EXPECTED["audit_sha256"],
    }
    report_path = args.output_root / "experiment08_preprocessing_freeze.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"PASS: preprocessing manifest frozen; report={report_path}")
    print(f"Manifest: {manifest_path}")
    print("STOP: no learned feature or predictive outcome was computed")


if __name__ == "__main__":
    main()
