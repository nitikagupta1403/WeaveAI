"""CLO-SKET Paper I — Experiment 06 corrective identity-map preflight.

This script is deliberately non-predictive. It applies only the authoritative
pre-outcome identity overrides already deposited by Experiment 08, validates
the corrected grouping/fold invariants, and writes provenance-locked identity
artifacts for the corrective Experiment 06 lineage.

It does NOT read feature matrices, fit classifiers, compute predictions, or
compute any Experiment-06 outcome.
"""

from __future__ import annotations

import csv
import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
HISTORICAL_ROW_MAP = (
    REPO_ROOT
    / "papers/CLO-SKET/evidence/Experiment_07/experiment07_row_map.csv"
)
OVERRIDES_JSON = (
    REPO_ROOT
    / "papers/CLO-SKET/Codes_paper_I/Experiment_08/experiment08_identity_overrides.json"
)
OUTPUT_DIR = REPO_ROOT / "papers/CLO-SKET/evidence/Experiment_06_Corrective"

CORRECTED_ROW_MAP = OUTPUT_DIR / "experiment06_corrected_identity_map.csv"
CORRECTED_IDENTITY_MAP = OUTPUT_DIR / "experiment06_corrected_identity_fold_map.csv"
CORRECTED_FOLD_SUMMARY = OUTPUT_DIR / "experiment06_corrected_fold_summary.csv"
PREFLIGHT_JSON = OUTPUT_DIR / "experiment06_identity_preflight.json"

EXPECTED_ROWS = 2300
EXPECTED_CATEGORIES = 23
EXPECTED_IDENTITIES = 230
EXPECTED_IDENTITIES_PER_CATEGORY = 10
EXPECTED_IDENTITIES_PER_CATEGORY_PER_FOLD = 2
EXPECTED_FOLDS = {0, 1, 2, 3, 4}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def fail(message: str) -> None:
    raise RuntimeError(message)


def relative_path_from_row(row: dict[str, str]) -> str:
    raw = row.get("image_path_resolved") or row.get("image_path_runtime") or ""
    parts = Path(raw).parts
    if len(parts) < 2:
        fail(f"Cannot derive category/filename relative path from: {raw!r}")
    return f"{parts[-2]}/{parts[-1]}"


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    for required in (HISTORICAL_ROW_MAP, OVERRIDES_JSON):
        if not required.is_file():
            fail(f"Required input missing: {required}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with HISTORICAL_ROW_MAP.open(newline="", encoding="utf-8") as f:
        historical_rows = list(csv.DictReader(f))

    with OVERRIDES_JSON.open(encoding="utf-8") as f:
        override_doc = json.load(f)

    if override_doc.get("stage") != "PRE_OUTCOME_IDENTITY_AUDIT":
        fail("Identity override file is not marked PRE_OUTCOME_IDENTITY_AUDIT")
    if override_doc.get("selection_used_learned_features") is not False:
        fail("Override selection must be independent of learned features")
    if override_doc.get("selection_used_classifier_outcomes") is not False:
        fail("Override selection must be independent of classifier outcomes")

    overrides = override_doc.get("overrides", [])
    if not overrides:
        fail("No authoritative identity overrides found")

    if len(historical_rows) != EXPECTED_ROWS:
        fail(f"Expected {EXPECTED_ROWS} historical rows; found {len(historical_rows)}")

    by_relative: dict[str, dict[str, str]] = {}
    row_indices: set[int] = set()
    for row in historical_rows:
        rel = relative_path_from_row(row)
        if rel in by_relative:
            fail(f"Duplicate relative path in historical map: {rel}")
        by_relative[rel] = row
        idx = int(row["row_index"])
        if idx in row_indices:
            fail(f"Duplicate row_index in historical map: {idx}")
        row_indices.add(idx)

    if row_indices != set(range(EXPECTED_ROWS)):
        fail("Historical row_index values are not exactly 0..2299")

    override_by_path: dict[str, dict] = {}
    for ov in overrides:
        rel = ov["relative_path"]
        if rel in override_by_path:
            fail(f"Duplicate override path: {rel}")
        if rel not in by_relative:
            fail(f"Override path not present in historical row map: {rel}")
        old = by_relative[rel]
        if old["garment_id"] != ov["historical_garment_id"]:
            fail(
                f"Historical garment mismatch for {rel}: "
                f"row map={old['garment_id']} override={ov['historical_garment_id']}"
            )
        if int(old["fold_id"]) != int(ov["historical_fold_id"]):
            fail(
                f"Historical fold mismatch for {rel}: "
                f"row map={old['fold_id']} override={ov['historical_fold_id']}"
            )
        corrected_id = ov["corrected_garment_id"]
        corrected_fold = int(ov["corrected_fold_id"])
        same_category_peers = [
            r
            for r in historical_rows
            if r["category"] == old["category"] and r["garment_id"] == corrected_id
        ]
        if not same_category_peers:
            fail(f"Corrected identity {corrected_id} has no historical peer rows for {rel}")
        peer_folds = {int(r["fold_id"]) for r in same_category_peers}
        if peer_folds != {corrected_fold}:
            fail(
                f"Corrected identity {corrected_id} peers do not uniquely occupy "
                f"declared corrected fold {corrected_fold}; observed {sorted(peer_folds)}"
            )
        override_by_path[rel] = ov

    corrected_rows: list[dict] = []
    for row in historical_rows:
        rel = relative_path_from_row(row)
        ov = override_by_path.get(rel)
        corrected_rows.append(
            {
                "row_index": int(row["row_index"]),
                "relative_path": rel,
                "category": row["category"],
                "historical_garment_id": row["garment_id"],
                "corrected_garment_id": (
                    ov["corrected_garment_id"] if ov else row["garment_id"]
                ),
                "historical_fold_id": int(row["fold_id"]),
                "corrected_fold_id": (
                    int(ov["corrected_fold_id"]) if ov else int(row["fold_id"])
                ),
                "override_applied": "yes" if ov else "no",
            }
        )

    corrected_rows.sort(key=lambda r: r["row_index"])

    categories = {r["category"] for r in corrected_rows}
    corrected_ids = {r["corrected_garment_id"] for r in corrected_rows}
    folds = {r["corrected_fold_id"] for r in corrected_rows}

    if len(categories) != EXPECTED_CATEGORIES:
        fail(f"Expected {EXPECTED_CATEGORIES} categories; found {len(categories)}")
    if len(corrected_ids) != EXPECTED_IDENTITIES:
        fail(f"Expected {EXPECTED_IDENTITIES} corrected identities; found {len(corrected_ids)}")
    if folds != EXPECTED_FOLDS:
        fail(f"Expected folds {sorted(EXPECTED_FOLDS)}; found {sorted(folds)}")

    identity_categories: dict[str, set[str]] = defaultdict(set)
    identity_folds: dict[str, set[int]] = defaultdict(set)
    identity_counts: Counter[str] = Counter()
    category_identities: dict[str, set[str]] = defaultdict(set)
    category_fold_identities: dict[tuple[str, int], set[str]] = defaultdict(set)

    for r in corrected_rows:
        gid = r["corrected_garment_id"]
        category = r["category"]
        fold = r["corrected_fold_id"]
        identity_categories[gid].add(category)
        identity_folds[gid].add(fold)
        identity_counts[gid] += 1
        category_identities[category].add(gid)
        category_fold_identities[(category, fold)].add(gid)

    bad_category_ids = {
        gid: sorted(vals) for gid, vals in identity_categories.items() if len(vals) != 1
    }
    if bad_category_ids:
        fail(f"Corrected identities span multiple categories: {bad_category_ids}")

    bad_fold_ids = {
        gid: sorted(vals) for gid, vals in identity_folds.items() if len(vals) != 1
    }
    if bad_fold_ids:
        fail(f"Corrected identities span multiple folds: {bad_fold_ids}")

    for category in sorted(categories):
        n_ids = len(category_identities[category])
        if n_ids != EXPECTED_IDENTITIES_PER_CATEGORY:
            fail(
                f"Category {category} has {n_ids} corrected identities; "
                f"expected {EXPECTED_IDENTITIES_PER_CATEGORY}"
            )
        for fold in sorted(EXPECTED_FOLDS):
            n_fold_ids = len(category_fold_identities[(category, fold)])
            if n_fold_ids != EXPECTED_IDENTITIES_PER_CATEGORY_PER_FOLD:
                fail(
                    f"Category {category}, fold {fold} has {n_fold_ids} corrected identities; "
                    f"expected {EXPECTED_IDENTITIES_PER_CATEGORY_PER_FOLD}"
                )

    preserved = override_doc.get("preserved_imbalance", {})
    for gid in ("Jumpsuit__G02", "Jumpsuit__G06"):
        if gid in preserved:
            expected = int(preserved[gid])
            observed = identity_counts[gid]
            if observed != expected:
                fail(f"Preserved imbalance mismatch for {gid}: expected {expected}, found {observed}")

    identity_rows: list[dict] = []
    for gid in sorted(corrected_ids):
        identity_rows.append(
            {
                "category": next(iter(identity_categories[gid])),
                "corrected_garment_id": gid,
                "fold_id": next(iter(identity_folds[gid])),
                "n_sketches": identity_counts[gid],
            }
        )
    identity_rows.sort(key=lambda r: (r["category"], r["corrected_garment_id"]))

    fold_summary: list[dict] = []
    all_ids = set(corrected_ids)
    for fold in sorted(EXPECTED_FOLDS):
        test_rows = [r for r in corrected_rows if r["corrected_fold_id"] == fold]
        train_rows = [r for r in corrected_rows if r["corrected_fold_id"] != fold]
        test_ids = {r["corrected_garment_id"] for r in test_rows}
        train_ids = {r["corrected_garment_id"] for r in train_rows}
        overlap = train_ids & test_ids
        if overlap:
            fail(f"Corrected train/test identity overlap in fold {fold}: {sorted(overlap)}")
        if test_ids | train_ids != all_ids:
            fail(f"Identity coverage failure in fold {fold}")
        fold_summary.append(
            {
                "fold": fold,
                "train_rows": len(train_rows),
                "test_rows": len(test_rows),
                "train_identities": len(train_ids),
                "test_identities": len(test_ids),
                "overlapping_corrected_identities": len(overlap),
            }
        )

    write_csv(
        CORRECTED_ROW_MAP,
        [
            "row_index",
            "relative_path",
            "category",
            "historical_garment_id",
            "corrected_garment_id",
            "historical_fold_id",
            "corrected_fold_id",
            "override_applied",
        ],
        corrected_rows,
    )
    write_csv(
        CORRECTED_IDENTITY_MAP,
        ["category", "corrected_garment_id", "fold_id", "n_sketches"],
        identity_rows,
    )
    write_csv(
        CORRECTED_FOLD_SUMMARY,
        [
            "fold",
            "train_rows",
            "test_rows",
            "train_identities",
            "test_identities",
            "overlapping_corrected_identities",
        ],
        fold_summary,
    )

    override_records = []
    for ov in overrides:
        override_records.append(
            {
                "relative_path": ov["relative_path"],
                "historical_garment_id": ov["historical_garment_id"],
                "corrected_garment_id": ov["corrected_garment_id"],
                "historical_fold_id": int(ov["historical_fold_id"]),
                "corrected_fold_id": int(ov["corrected_fold_id"]),
            }
        )

    report = {
        "schema_version": 1,
        "experiment": "CLO-SKET Experiment 06 corrective reanalysis",
        "stage": "PRE_OUTCOME_IDENTITY_PREFLIGHT",
        "preflight_passed": True,
        "predictive_outcome_computed": False,
        "classifier_fitted": False,
        "feature_matrix_generated": False,
        "source_candidate_commit": "60063623eedde05ed7c351c3c947a605f6be5344",
        "inputs": {
            "historical_row_map": str(HISTORICAL_ROW_MAP.relative_to(REPO_ROOT)),
            "historical_row_map_sha256": sha256_file(HISTORICAL_ROW_MAP),
            "identity_overrides": str(OVERRIDES_JSON.relative_to(REPO_ROOT)),
            "identity_overrides_sha256": sha256_file(OVERRIDES_JSON),
        },
        "counts": {
            "rows": len(corrected_rows),
            "categories": len(categories),
            "corrected_identities": len(corrected_ids),
            "folds": len(folds),
            "declared_overrides_applied": sum(
                r["override_applied"] == "yes" for r in corrected_rows
            ),
        },
        "authoritative_overrides": override_records,
        "fold_summary": fold_summary,
        "checks": {
            "row_indices_exactly_0_to_2299": True,
            "unique_relative_paths": True,
            "one_category_per_corrected_identity": True,
            "one_fold_per_corrected_identity": True,
            "ten_corrected_identities_per_category": True,
            "two_corrected_identities_per_category_per_fold": True,
            "zero_corrected_identity_train_test_overlap_all_folds": True,
            "declared_preserved_imbalance_verified": True,
            "no_predictive_analysis_performed": True,
        },
        "outputs": {
            "corrected_identity_map": str(CORRECTED_ROW_MAP.relative_to(REPO_ROOT)),
            "corrected_identity_map_sha256": sha256_file(CORRECTED_ROW_MAP),
            "corrected_identity_fold_map": str(CORRECTED_IDENTITY_MAP.relative_to(REPO_ROOT)),
            "corrected_identity_fold_map_sha256": sha256_file(CORRECTED_IDENTITY_MAP),
            "corrected_fold_summary": str(CORRECTED_FOLD_SUMMARY.relative_to(REPO_ROOT)),
            "corrected_fold_summary_sha256": sha256_file(CORRECTED_FOLD_SUMMARY),
        },
        "stop": (
            "PRE-OUTCOME STOP: identity/fold integrity only. No feature extraction, "
            "classifier fitting, prediction, metric, bootstrap, or permutation outcome computed."
        ),
    }

    PREFLIGHT_JSON.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    print("Experiment 06 corrective identity preflight: PASS")
    print(f"Rows: {len(corrected_rows)}")
    print(f"Categories: {len(categories)}")
    print(f"Corrected identities: {len(corrected_ids)}")
    print(f"Overrides applied: {len(overrides)}")
    for row in fold_summary:
        print(
            "Fold {fold}: train_rows={train_rows}, test_rows={test_rows}, "
            "train_ids={train_identities}, test_ids={test_identities}, overlap={overlapping_corrected_identities}".format(
                **row
            )
        )
    print(f"Preflight report: {PREFLIGHT_JSON.relative_to(REPO_ROOT)}")
    print("STOP — no predictive outcome was computed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Experiment 06 corrective identity preflight: FAIL — {exc}", file=sys.stderr)
        raise
