#!/usr/bin/env python3
"""
P2-R0-05K0
Gate A — PRE-05K provenance inventory

PURPOSE
-------
Recover authoritative historical sources/column names needed for
deterministic S01–S10 selection.

STRICT BOUNDARY
---------------
- PRE-05K historical artifacts only.
- NEVER read a path containing 05K.
- CSV schema/header inspection only; no 05K outcomes.
- Does NOT select sentinels.
- Does NOT compute support-sweep spectra.

OUTPUT
------
P2_R0_05K0_pre05k_provenance_inventory.csv
P2_R0_05K0_pre05k_provenance_inventory.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import pandas as pd


VERSION = "P2-R0-05K0-PROVENANCE-v1.0"

# Historical stages relevant to sentinel construction.
ALLOWED_STAGE_TOKENS = (
    "05e",
    "05f",
    "05h",
    "05i",
    "05j",
    "fold",
)

# Absolute guard: no 05K input may be opened.
FORBIDDEN_INPUT_TOKENS = (
    "05k",
    "support_sweep",
    "support-sweep",
)

# Terms useful for finding authoritative columns.
FIELD_HINTS = {
    "row_index": ("row_index",),
    "relative_path": ("relative_path", "rel_path"),
    "category": ("category",),
    "identity": ("identity", "garment_identity", "identity_id"),

    "fold": ("fold_id", "test_fold", "fold"),

    "crop_low": ("low",),
    "crop_high": ("high",),

    "q99": ("q99",),
    "rmax": ("rmax", "r_max", "max_radius"),
    "grid_radius": ("grid_radius", "r_grid", "rgrid"),

    "raw_crop_l1": (
        "raw_crop",
        "crop_raw",
        "band_l1",
        "l1",
    ),

    "raw_text_l1": (
        "raw_text",
        "text_raw",
        "text",
        "l1",
    ),

    "text_positive": (
        "text_positive",
        "text_present",
        "has_text",
    ),
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()

    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)

    return h.hexdigest()


def assert_pre05k(path: Path) -> None:
    p = str(path).lower()

    for token in FORBIDDEN_INPUT_TOKENS:
        if token in p:
            raise RuntimeError(
                f"REFUSING FORBIDDEN 05K INPUT:\n{path}"
            )


def relevant_historical_path(path: Path) -> bool:
    p = str(path).lower()

    if any(x in p for x in FORBIDDEN_INPUT_TOKENS):
        return False

    return any(x in p for x in ALLOWED_STAGE_TOKENS)


def find_hint_matches(columns):
    columns = [str(c) for c in columns]
    lower = {c: c.lower() for c in columns}

    result = {}

    for role, hints in FIELD_HINTS.items():
        hits = []

        for original, low in lower.items():
            if all(h in low for h in hints):
                hits.append(original)

        result[role] = sorted(hits)

    return result


def inspect_csv(path: Path) -> dict:
    assert_pre05k(path)

    # HEADER ONLY.
    header = pd.read_csv(path, nrows=0)
    columns = list(header.columns)

    return {
        "path": str(path.resolve()),
        "filename": path.name,
        "suffix": path.suffix.lower(),
        "size_bytes": path.stat().st_size,
        "sha256": sha256_file(path),
        "n_columns": len(columns),
        "columns": columns,
        "hint_matches": find_hint_matches(columns),
    }


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--root",
        required=True,
        help="Research root containing frozen PRE-05K artifacts.",
    )

    parser.add_argument(
        "--out",
        required=True,
        help="NEW output directory for 05K0 provenance inventory.",
    )

    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    out = Path(args.out).expanduser().resolve()

    if not root.exists():
        raise FileNotFoundError(root)

    out.mkdir(parents=True, exist_ok=True)

    # Input root itself must not be an 05K directory.
    assert_pre05k(root)

    candidates = []

    for path in root.rglob("*.csv"):
        if relevant_historical_path(path):
            candidates.append(path)

    candidates = sorted(
        candidates,
        key=lambda p: str(p).lower(),
    )

    print(f"\n{VERSION}")
    print("=" * 72)
    print(f"Historical root : {root}")
    print(f"CSV candidates  : {len(candidates)}")
    print("05K input access: FORBIDDEN")
    print("=" * 72)

    records = []

    for path in candidates:
        try:
            info = inspect_csv(path)
            info["status"] = "OK"
            info["error"] = None

        except Exception as exc:
            info = {
                "path": str(path),
                "filename": path.name,
                "status": "ERROR",
                "error": repr(exc),
            }

        records.append(info)

    # --------------------------------------------------------
    # Human-readable summary
    # --------------------------------------------------------

    rows = []

    for r in records:
        if r["status"] != "OK":
            rows.append({
                "path": r["path"],
                "sha256": None,
                "n_columns": None,
                "matched_roles": None,
                "status": "ERROR",
            })
            continue

        matched = [
            role
            for role, hits in r["hint_matches"].items()
            if hits
        ]

        rows.append({
            "path": r["path"],
            "sha256": r["sha256"],
            "n_columns": r["n_columns"],
            "matched_roles": ";".join(matched),
            "status": "OK",
        })

    summary = pd.DataFrame(rows)

    csv_out = out / "P2_R0_05K0_pre05k_provenance_inventory.csv"
    json_out = out / "P2_R0_05K0_pre05k_provenance_inventory.json"

    summary.to_csv(csv_out, index=False)

    payload = {
        "version": VERSION,
        "historical_root": str(root),
        "strict_pre05k_only": True,
        "n_candidate_csvs": len(candidates),
        "records": records,
    }

    json_text = json.dumps(
        payload,
        indent=2,
        sort_keys=True,
        ensure_ascii=False,
    ) + "\n"

    json_out.write_text(json_text, encoding="utf-8")

    print("\nWROTE")
    print(csv_out)
    print(json_out)

    print("\nSHA256")
    print(
        "CSV :",
        sha256_file(csv_out),
    )
    print(
        "JSON:",
        sha256_file(json_out),
    )

    print("\nCandidate files with useful fields:")
    print("-" * 72)

    for r in records:
        if r["status"] != "OK":
            continue

        matches = {
            k: v
            for k, v in r["hint_matches"].items()
            if v
        }

        if matches:
            print(f"\n{r['path']}")
            print(f"SHA256: {r['sha256']}")

            for role, cols in matches.items():
                print(f"  {role:16s}: {cols}")


if __name__ == "__main__":
    main()