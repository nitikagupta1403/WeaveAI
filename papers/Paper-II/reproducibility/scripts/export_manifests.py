#!/usr/bin/env python3
"""Export aligned sample/fold manifests from a trusted frozen pickle package."""

import argparse
import csv
import json
import pickle
from pathlib import Path


def aligned_optional(package, keys, n):
    for key in keys:
        value = package.get(key)
        if value is not None and len(value) == n:
            return key, [str(item) for item in value]
    return None, [""] * n


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trusted-pickle", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--i-understand-pickle-risk", action="store_true")
    args = parser.parse_args()
    if not args.i_understand_pickle_risk:
        parser.error("Refusing to unpickle without --i-understand-pickle-risk")

    with args.trusted_pickle.open("rb") as handle:
        package = pickle.load(handle)

    required = ("garment_identity_ids", "cell30m_fold_assignment")
    missing = [key for key in required if key not in package]
    if missing:
        raise RuntimeError(f"Missing required keys: {missing}")

    identities = [str(item) for item in package[required[0]]]
    folds = [int(item) for item in package[required[1]]]
    n = len(identities)
    if n != 2300 or len(folds) != n:
        raise RuntimeError(f"Expected two aligned 2300-row arrays; got {n} and {len(folds)}")
    if len(set(identities)) != 230:
        raise RuntimeError(f"Expected 230 identities; found {len(set(identities))}")
    if len(set(folds)) != 5:
        raise RuntimeError(f"Expected five folds; found {sorted(set(folds))}")

    identity_folds = {}
    for identity, fold in zip(identities, folds):
        identity_folds.setdefault(identity, set()).add(fold)
    leaking = sorted(key for key, value in identity_folds.items() if len(value) != 1)
    if leaking:
        raise RuntimeError(f"Identity leakage across folds: {leaking[:10]}")

    category_key, categories = aligned_optional(package, ("category_ids", "category_labels"), n)
    filename_key, filenames = aligned_optional(package, ("filenames", "image_filenames", "image_paths"), n)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    manifest = args.output_dir / "sample_fold_manifest.csv"
    with manifest.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(("row_index", "filename", "category", "garment_identity", "fold"))
        for index, values in enumerate(zip(filenames, categories, identities, folds)):
            filename, category, identity, fold = values
            writer.writerow((index, filename, category, identity, fold))

    summary = {
        "rows": n,
        "identities": len(set(identities)),
        "folds": sorted(set(folds)),
        "category_source_key": category_key,
        "filename_source_key": filename_key,
        "identity_leakage_count": 0,
    }
    (args.output_dir / "manifest_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
