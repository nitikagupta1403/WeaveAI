"""
CLO-SKET — EXPERIMENT 07
Conventional image-descriptor baseline (HOG)

IMPORTANT
---------
This script is deliberately guard-railed.  By default it performs only
pre-run discovery and validation and then stops BEFORE fitting a classifier.

The experiment must use:
  * the exact frozen Experiment-06 garment-identity fold map; and
  * the exact frozen 2300 x 14 RA representation in identical row order.

Do not bypass these checks by silently rebuilding different folds or RA14.
See 08_HOG_External_Baseline_DESIGN_LOCK.md.
"""

from __future__ import annotations

from pathlib import Path
import json
import sys
import hashlib
import numpy as np
import pandas as pd

# -------------------------------------------------------------------------------------------------
# USER/RUNTIME PATHS
# -------------------------------------------------------------------------------------------------
DATA_ROOT = Path("/content/drive/MyDrive/FashionAI/datasets/Clo-Sket/Clo-Sket")
SEARCH_ROOTS = [
    Path("/content/drive/MyDrive/FashionAI"),
    Path("/content"),
]
OUTPUT_ROOT = Path("/content/drive/MyDrive/FashionAI/CLO_SKET_HOG_External_Baseline")

# This MUST remain False until we have inspected the discovery output together and supplied/verified
# the exact frozen Experiment-06 fold map and frozen RA14 artifact.
RUN_EXPERIMENT = False

# Paths may be filled only after discovery/verification.
FOLD_MAP_PATH: Path | None = None
RA14_PATH: Path | None = None
ROW_MANIFEST_PATH: Path | None = None

# -------------------------------------------------------------------------------------------------
# LOCKED EXPERIMENT SPECIFICATION
# -------------------------------------------------------------------------------------------------
RANDOM_STATE = 20260820
N_SKETCHES = 2300
N_IDENTITIES = 230
N_CATEGORIES = 23
N_FOLDS = 5
TEST_IDENTITIES_PER_FOLD = 46
TRAIN_IDENTITIES_PER_FOLD = 184
RA_DIM = 14

HOG_CANVAS = 256
HOG_ORIENTATIONS = 9
HOG_PIXELS_PER_CELL = (16, 16)
HOG_CELLS_PER_BLOCK = (2, 2)
HOG_BLOCK_NORM = "L2-Hys"
HOG_TRANSFORM_SQRT = False


def sha256_file(path: Path, block_size: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(block_size)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def print_lock() -> None:
    print("=" * 112)
    print("CLO-SKET — EXPERIMENT 07 — CONVENTIONAL IMAGE-DESCRIPTOR BASELINE")
    print("=" * 112)
    print("STATUS                       : DESIGN LOCKED; OUTCOME NOT YET COMPUTED")
    print("Purpose                      : secondary external standard-CV comparator only")
    print("Dataset                      : 2,300 sketches / 230 identities / 23 categories")
    print("Validation                   : SAME 5 frozen Experiment-06 identity-disjoint folds REQUIRED")
    print("RA input                     : SAME frozen 2,300 x 14 Experiment-06 RA matrix REQUIRED")
    print("Primary comparison           : HOG + RA14  minus  HOG")
    print("Primary metric               : pooled OOF Macro-F1")
    print("Secondary metric             : pooled OOF balanced accuracy")
    print("Estimator                    : StandardScaler(train fold) + LogisticRegression")
    print("LogisticRegression           : L2, C=1.0, lbfgs, max_iter=5000, class_weight=None")
    print("Random state                 : 20260820")
    print("HOG canvas                   : 256 x 256 white, aspect-ratio-preserving resize + centered pad")
    print("HOG                           : 9 orientations; 16x16 cells; 2x2 blocks; L2-Hys")
    print("HOG transform_sqrt           : False")
    print("Hyperparameter search        : NO")
    print("Feature selection / PCA      : NO")
    print("Augmentation                 : NO")
    print("RA modification              : NO")
    print("Experiment-06 modification   : NO")
    print("RUN_EXPERIMENT               :", RUN_EXPERIMENT)
    print("=" * 112)


def discover_candidates() -> dict[str, list[str]]:
    """Find plausible frozen artifacts without assuming filenames."""
    patterns = {
        "fold": ["*fold*.csv", "*fold*.npy", "*fold*.npz", "*fold*.pkl"],
        "ra14": ["*14D*.npy", "*14d*.npy", "*radial*angular*.npy", "*RA*.npy",
                 "*14D*.csv", "*14d*.csv", "*radial*angular*.csv"],
        "manifest": ["*manifest*.csv", "*metadata*.csv", "*paths*.csv", "*row*.csv"],
    }
    found: dict[str, list[str]] = {k: [] for k in patterns}
    for root in SEARCH_ROOTS:
        if not root.exists():
            continue
        for key, pats in patterns.items():
            for pat in pats:
                try:
                    for p in root.rglob(pat):
                        # Exclude huge irrelevant caches where possible.
                        s = str(p)
                        if "/.git/" in s or "/node_modules/" in s:
                            continue
                        if p.is_file():
                            found[key].append(s)
                except PermissionError:
                    pass
    for k in found:
        found[k] = sorted(set(found[k]))
    return found


def dataset_check() -> list[Path]:
    if not DATA_ROOT.exists():
        raise FileNotFoundError(f"DATA_ROOT does not exist: {DATA_ROOT}")
    files = sorted([*DATA_ROOT.rglob("*.tif"), *DATA_ROOT.rglob("*.tiff")])
    print(f"TIFF sketches found           : {len(files)}")
    if len(files) != N_SKETCHES:
        raise RuntimeError(f"Expected {N_SKETCHES} TIFF sketches, found {len(files)}")
    return files


def show_candidates(found: dict[str, list[str]]) -> None:
    print("\n" + "=" * 112)
    print("FROZEN-ARTIFACT DISCOVERY — NO MODEL FIT")
    print("=" * 112)
    for key in ["fold", "ra14", "manifest"]:
        print(f"\n[{key.upper()} candidates]  n={len(found[key])}")
        for p in found[key][:80]:
            try:
                size = Path(p).stat().st_size
                print(f"  {p}   ({size:,} bytes)")
            except Exception:
                print(" ", p)
        if len(found[key]) > 80:
            print(f"  ... {len(found[key]) - 80} additional candidates omitted")


def hard_stop_message() -> None:
    print("\n" + "=" * 112)
    print("PRE-RUN GATE — STOPPED AS INTENDED")
    print("=" * 112)
    print("No classifier has been fitted and no Experiment-07 outcome has been computed.")
    print("Before RUN_EXPERIMENT may be changed to True, we must verify:")
    print("  1. the exact frozen Experiment-06 fold assignment;")
    print("  2. the exact frozen 2300 x 14 RA matrix;")
    print("  3. row-order identity between TIFF files, RA14, labels, identities, and fold map;")
    print("  4. SHA-256 hashes / provenance of the selected artifacts.")
    print("Send the candidate lists printed above back for inspection.")
    print("DO NOT choose a candidate merely because its filename looks plausible.")
    print("=" * 112)


def main() -> None:
    print_lock()
    dataset_check()
    found = discover_candidates()
    show_candidates(found)

    # Save discovery only; this contains no predictive outcome.
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    payload = {
        "status": "PRE_RUN_DISCOVERY_ONLY",
        "run_experiment": RUN_EXPERIMENT,
        "data_root": str(DATA_ROOT),
        "n_sketches": N_SKETCHES,
        "candidates": found,
        "design_lock": {
            "hog_canvas": HOG_CANVAS,
            "orientations": HOG_ORIENTATIONS,
            "pixels_per_cell": HOG_PIXELS_PER_CELL,
            "cells_per_block": HOG_CELLS_PER_BLOCK,
            "block_norm": HOG_BLOCK_NORM,
            "transform_sqrt": HOG_TRANSFORM_SQRT,
            "random_state": RANDOM_STATE,
        },
    }
    discovery_json = OUTPUT_ROOT / "experiment07_pre_run_discovery.json"
    discovery_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"\nDiscovery record saved       : {discovery_json}")

    if not RUN_EXPERIMENT:
        hard_stop_message()
        return

    # Deliberate hard guard.  The fitting section will be activated only after the exact inputs have
    # been reviewed and pinned.  This prevents an outcome from being generated with guessed folds or
    # a merely plausible RA artifact.
    raise RuntimeError(
        "RUN_EXPERIMENT=True is not yet authorized in this script. "
        "Pin and verify the exact frozen fold map and RA14 artifact first."
    )


if __name__ == "__main__":
    main()
