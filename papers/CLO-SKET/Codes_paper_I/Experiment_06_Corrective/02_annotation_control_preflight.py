"""Freeze/verify the annotation-controlled measurement field for corrective Experiment 06.

This script performs PRE-OUTCOME preprocessing/provenance checks only. It does not
extract RA14 or morphology features, fit a classifier, compute predictions, or
calculate predictive metrics.

The clean measurement field is not redesigned here. It reuses the already-frozen
Experiment-08 preprocessing manifest and deterministic materialized images, whose
preprocessing choices were locked before the Experiment-08 learned baseline was
computed. The purpose here is to bind those same garment-only fields to the
corrected Experiment-06 row/identity map before any corrective Experiment-06
outcome is computed.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image

EXPECTED_ROWS = 2300
EXPECTED_CATEGORIES = 23
EXPECTED_IDENTITIES = 230
EXPECTED_REVIEWED_IMAGES = 928
EXPECTED_TEXT_BOXES = 593
EXPECTED_AMBIGUOUS_OVERLAPS = 22

EXPECTED_PREPROCESSING_MANIFEST_SHA256 = (
    "c464feafbb382c8e9d111433047298d8f42e1c661e018735e3df0b6016eaff4d"
)
EXPECTED_MATERIALIZED_MANIFEST_SHA256 = (
    "071ee7b6c535361951f9eb0044ff166c9a4d42b0ef55a3c0a72aab27af2af6a4"
)
EXPECTED_ORDERED_PIXEL_ARRAY_SHA256 = (
    "30006ee3661f18b4cc3925c753c2ada6e3eb6ea7bf7f56326e5edf7cb7be5703"
)
EXPECTED_IDENTITY_MAP_SHA256 = (
    "c2510fb74b452da22d3b4e9badb46cfe4cbd2653c0ee99acb573942262c1ac2b"
)
SOURCE_CANDIDATE_COMMIT = "60063623eedde05ed7c351c3c947a605f6be5344"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def pixel_sha256(path: Path) -> str:
    with Image.open(path) as opened:
        pixels = np.ascontiguousarray(np.asarray(opened.convert("L"), dtype=np.uint8))
    return hashlib.sha256(pixels.tobytes()).hexdigest()


def parse_text_boxes(value: object) -> list[list[int]]:
    if value is None:
        return []
    if isinstance(value, float) and np.isnan(value):
        return []
    text = str(value).strip()
    if not text:
        return []
    parsed = json.loads(text)
    if not isinstance(parsed, list):
        raise RuntimeError("text_boxes_json must decode to a list")
    return parsed


def as_bool(value: object) -> bool:
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    if text in {"true", "1", "yes"}:
        return True
    if text in {"false", "0", "no", ""}:
        return False
    raise RuntimeError(f"Cannot parse boolean value: {value!r}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--corrected-identity-map",
        type=Path,
        default=Path(
            "papers/CLO-SKET/evidence/Experiment_06_Corrective/"
            "experiment06_corrected_identity_map.csv"
        ),
    )
    parser.add_argument("--preprocessing-manifest", type=Path, required=True)
    parser.add_argument("--materialized-root", type=Path, required=True)
    parser.add_argument(
        "--materialized-manifest",
        type=Path,
        default=None,
        help=(
            "Defaults to <materialized-root>/experiment08_materialized_images.csv"
        ),
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path("papers/CLO-SKET/evidence/Experiment_06_Corrective"),
    )
    return parser.parse_args()


def require_columns(frame: pd.DataFrame, columns: set[str], label: str) -> None:
    missing = sorted(columns - set(frame.columns))
    if missing:
        raise RuntimeError(f"{label} missing columns: {missing}")


def main() -> None:
    args = parse_args()
    materialized_manifest_path = args.materialized_manifest or (
        args.materialized_root / "experiment08_materialized_images.csv"
    )

    identity_hash = sha256_file(args.corrected_identity_map)
    preprocessing_hash = sha256_file(args.preprocessing_manifest)
    materialized_manifest_hash = sha256_file(materialized_manifest_path)

    if identity_hash != EXPECTED_IDENTITY_MAP_SHA256:
        raise RuntimeError(
            "Corrected identity-map hash mismatch: "
            f"{identity_hash} != {EXPECTED_IDENTITY_MAP_SHA256}"
        )
    if preprocessing_hash != EXPECTED_PREPROCESSING_MANIFEST_SHA256:
        raise RuntimeError(
            "Frozen preprocessing-manifest hash mismatch: "
            f"{preprocessing_hash} != {EXPECTED_PREPROCESSING_MANIFEST_SHA256}"
        )
    if materialized_manifest_hash != EXPECTED_MATERIALIZED_MANIFEST_SHA256:
        raise RuntimeError(
            "Frozen materialized-manifest hash mismatch: "
            f"{materialized_manifest_hash} != {EXPECTED_MATERIALIZED_MANIFEST_SHA256}"
        )

    identity = pd.read_csv(args.corrected_identity_map, keep_default_na=False)
    preprocessing = pd.read_csv(args.preprocessing_manifest, keep_default_na=False)
    materialized = pd.read_csv(materialized_manifest_path, keep_default_na=False)

    require_columns(
        identity,
        {
            "row_index",
            "relative_path",
            "category",
            "corrected_garment_id",
            "corrected_fold_id",
        },
        "corrected identity map",
    )
    require_columns(
        preprocessing,
        {
            "row_index",
            "relative_path",
            "source_sha256",
            "text_boxes_json",
            "selection_cohort",
            "localization_source",
            "ambiguous_overlap",
        },
        "preprocessing manifest",
    )
    require_columns(
        materialized,
        {
            "row_index",
            "relative_path",
            "output_relative_path",
            "output_png_sha256",
            "output_pixel_sha256",
            "selection_cohort",
            "localization_source",
            "ambiguous_overlap",
        },
        "materialized manifest",
    )

    for label, frame in {
        "identity": identity,
        "preprocessing": preprocessing,
        "materialized": materialized,
    }.items():
        if len(frame) != EXPECTED_ROWS:
            raise RuntimeError(f"{label}: expected {EXPECTED_ROWS} rows, found {len(frame)}")
        if frame["row_index"].duplicated().any():
            raise RuntimeError(f"{label}: duplicate row_index")
        if frame["relative_path"].duplicated().any():
            raise RuntimeError(f"{label}: duplicate relative_path")

    identity = identity.sort_values("row_index").reset_index(drop=True)
    preprocessing = preprocessing.sort_values("row_index").reset_index(drop=True)
    materialized = materialized.sort_values("row_index").reset_index(drop=True)

    expected_indices = list(range(EXPECTED_ROWS))
    if identity["row_index"].astype(int).tolist() != expected_indices:
        raise RuntimeError("Corrected identity row indices are not exactly 0..2299")
    if preprocessing["row_index"].astype(int).tolist() != expected_indices:
        raise RuntimeError("Preprocessing row indices are not exactly 0..2299")
    if materialized["row_index"].astype(int).tolist() != expected_indices:
        raise RuntimeError("Materialized row indices are not exactly 0..2299")

    canonical_paths = identity["relative_path"].tolist()
    if preprocessing["relative_path"].tolist() != canonical_paths:
        raise RuntimeError("Preprocessing manifest path/order mismatch vs corrected identity map")
    if materialized["relative_path"].tolist() != canonical_paths:
        raise RuntimeError("Materialized manifest path/order mismatch vs corrected identity map")

    if identity["category"].nunique() != EXPECTED_CATEGORIES:
        raise RuntimeError("Corrected identity map category count mismatch")
    if identity["corrected_garment_id"].nunique() != EXPECTED_IDENTITIES:
        raise RuntimeError("Corrected identity count mismatch")

    text_boxes_by_row = [parse_text_boxes(v) for v in preprocessing["text_boxes_json"]]
    annotation_present = [bool(boxes) for boxes in text_boxes_by_row]
    text_box_count = sum(len(boxes) for boxes in text_boxes_by_row)
    overlap_flags = [as_bool(v) for v in preprocessing["ambiguous_overlap"]]
    overlap_count = sum(overlap_flags)

    # The frozen E08 review design contained 928 reviewed records. The remainder was
    # retained through the frozen automatic/QC localization path. We infer reviewer
    # status only from the already-frozen selection/localization metadata; no new
    # image-content decision is made here.
    reviewed_mask = preprocessing["selection_cohort"].astype(str).str.len() > 0
    reviewed_count = int(reviewed_mask.sum())

    if reviewed_count != EXPECTED_REVIEWED_IMAGES:
        raise RuntimeError(
            f"Reviewed-image count mismatch: {reviewed_count} != {EXPECTED_REVIEWED_IMAGES}"
        )
    if text_box_count != EXPECTED_TEXT_BOXES:
        raise RuntimeError(
            f"Frozen text-box count mismatch: {text_box_count} != {EXPECTED_TEXT_BOXES}"
        )
    if overlap_count != EXPECTED_AMBIGUOUS_OVERLAPS:
        raise RuntimeError(
            "Frozen ambiguous-overlap count mismatch: "
            f"{overlap_count} != {EXPECTED_AMBIGUOUS_OVERLAPS}"
        )

    aggregate = hashlib.sha256()
    status_rows: list[dict] = []
    missing_images: list[str] = []
    bad_png_hashes: list[str] = []
    bad_pixel_hashes: list[str] = []

    for idx in range(EXPECTED_ROWS):
        ident = identity.iloc[idx]
        prep = preprocessing.iloc[idx]
        mat = materialized.iloc[idx]
        image_path = args.materialized_root / str(mat["output_relative_path"])
        if not image_path.is_file():
            missing_images.append(str(mat["output_relative_path"]))
            continue

        observed_png_hash = sha256_file(image_path)
        observed_pixel_hash = pixel_sha256(image_path)
        expected_png_hash = str(mat["output_png_sha256"])
        expected_pixel_hash = str(mat["output_pixel_sha256"])
        if observed_png_hash != expected_png_hash:
            bad_png_hashes.append(str(mat["output_relative_path"]))
        if observed_pixel_hash != expected_pixel_hash:
            bad_pixel_hashes.append(str(mat["output_relative_path"]))

        aggregate.update(f"{idx}\t{expected_pixel_hash}\n".encode())
        status_rows.append(
            {
                "row_index": idx,
                "relative_path": ident["relative_path"],
                "category": ident["category"],
                "corrected_garment_id": ident["corrected_garment_id"],
                "corrected_fold_id": int(ident["corrected_fold_id"]),
                "annotation_present": annotation_present[idx],
                "annotation_box_count": len(text_boxes_by_row[idx]),
                "annotation_overlaps_or_touches_garment": overlap_flags[idx],
                "garment_only_field_source": "frozen_experiment08_preprocessing_v4",
                "selection_cohort": prep["selection_cohort"],
                "localization_source": prep["localization_source"],
                "reviewer_status": (
                    "human_reviewed" if bool(reviewed_mask.iloc[idx]) else "automatic_remainder_after_frozen_qc"
                ),
                "clean_image_relative_path": mat["output_relative_path"],
                "clean_png_sha256": expected_png_hash,
                "clean_pixel_sha256": expected_pixel_hash,
                "source_sha256": prep["source_sha256"],
            }
        )

    if missing_images:
        raise RuntimeError(f"Missing {len(missing_images)} frozen clean images; first={missing_images[0]}")
    if bad_png_hashes:
        raise RuntimeError(f"PNG-hash mismatch for {len(bad_png_hashes)} images; first={bad_png_hashes[0]}")
    if bad_pixel_hashes:
        raise RuntimeError(f"Pixel-hash mismatch for {len(bad_pixel_hashes)} images; first={bad_pixel_hashes[0]}")

    ordered_pixel_hash = aggregate.hexdigest()
    if ordered_pixel_hash != EXPECTED_ORDERED_PIXEL_ARRAY_SHA256:
        raise RuntimeError(
            "Ordered pixel-array hash mismatch: "
            f"{ordered_pixel_hash} != {EXPECTED_ORDERED_PIXEL_ARRAY_SHA256}"
        )

    args.output_root.mkdir(parents=True, exist_ok=True)
    status_path = args.output_root / "experiment06_annotation_status.csv"
    with status_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(status_rows[0]))
        writer.writeheader()
        writer.writerows(status_rows)

    report = {
        "schema_version": 1,
        "experiment": "CLO-SKET Experiment 06 corrective reanalysis",
        "stage": "PRE_OUTCOME_ANNOTATION_CONTROL_PREFLIGHT",
        "source_candidate_commit": SOURCE_CANDIDATE_COMMIT,
        "policy": (
            "Reuse the frozen Experiment-08 preprocessing/materialization v4 exactly; "
            "no new annotation-control choice is made after historical Experiment-06 outcomes."
        ),
        "counts": {
            "rows": EXPECTED_ROWS,
            "categories": EXPECTED_CATEGORIES,
            "corrected_identities": EXPECTED_IDENTITIES,
            "human_reviewed_images": reviewed_count,
            "automatic_remainder_after_frozen_qc": EXPECTED_ROWS - reviewed_count,
            "images_with_reviewed_annotation_boxes": int(sum(annotation_present)),
            "reviewed_text_boxes": text_box_count,
            "ambiguous_geometric_overlaps": overlap_count,
        },
        "checks": {
            "corrected_identity_map_hash_locked": True,
            "preprocessing_manifest_hash_locked": True,
            "materialized_manifest_hash_locked": True,
            "row_order_and_paths_identical": True,
            "all_2300_clean_images_present": True,
            "all_png_hashes_verified": True,
            "all_pixel_hashes_verified": True,
            "ordered_pixel_array_hash_verified": True,
            "no_feature_extraction_performed": True,
            "no_classifier_fitted": True,
            "no_predictive_outcome_computed": True,
        },
        "inputs": {
            "corrected_identity_map": str(args.corrected_identity_map),
            "corrected_identity_map_sha256": identity_hash,
            "preprocessing_manifest": str(args.preprocessing_manifest),
            "preprocessing_manifest_sha256": preprocessing_hash,
            "materialized_manifest": str(materialized_manifest_path),
            "materialized_manifest_sha256": materialized_manifest_hash,
            "ordered_pixel_array_sha256": ordered_pixel_hash,
        },
        "output": {
            "annotation_status": str(status_path),
            "annotation_status_sha256": sha256_file(status_path),
        },
        "feature_matrix_generated": False,
        "classifier_fitted": False,
        "predictive_outcome_computed": False,
        "preflight_passed": True,
        "stop": (
            "PRE-OUTCOME STOP: annotation-control provenance and clean-image integrity only. "
            "No RA14/morphology feature extraction, classifier fitting, prediction, metric, "
            "bootstrap, permutation, or annotation-sensitivity outcome computed."
        ),
    }
    report_path = args.output_root / "experiment06_annotation_control_preflight.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print("Experiment 06 annotation-control preflight: PASS")
    print(f"Rows: {EXPECTED_ROWS}")
    print(f"Human-reviewed images: {reviewed_count}")
    print(f"Reviewed text boxes: {text_box_count}")
    print(f"Ambiguous geometric overlaps: {overlap_count}")
    print(f"Ordered clean-pixel hash: {ordered_pixel_hash}")
    print(f"Annotation status: {status_path}")
    print(f"Preflight report: {report_path}")
    print("STOP — no feature extraction or predictive outcome was computed.")


if __name__ == "__main__":
    main()
