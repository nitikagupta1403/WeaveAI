from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import pandas as pd


EXPECTED_ROWS = 2300
EXPECTED_M135 = 135
EXPECTED_RA14 = 14

EXPECTED_RAW_M135_ARRAY_SHA256 = (
    "66ae04156ee3fbf3f2605f382a16fc41"
    "cf19af34b50e59dd43f6c9427d96b2ee"
)

EXPECTED_RAW_RA14_ARRAY_SHA256 = (
    "01ea6937783792d0d9295ca92db863d9"
    "32db4b57f5ad4b61ca78a2c97eb88a3c"
)

REPO_ROOT = Path(__file__).resolve().parents[4]
E8 = REPO_ROOT / "papers/CLO-SKET/Codes_paper_I/Experiment_08"
DEFAULT_STATUS = (
    REPO_ROOT
    / "papers/CLO-SKET/evidence/Experiment_06_Corrective/experiment06_annotation_status.csv"
)
DEFAULT_OUTPUT_ROOT = (
    REPO_ROOT
    / "papers/CLO-SKET/evidence/Experiment_06_Corrective"
)

MORPHOLOGY_SOURCE = E8 / "materialize_morphology.py"
RA14_SOURCE = E8 / "extract_ra14_features.py"


# -----------------------------------------------------------------------------
# Hash / import helpers
# -----------------------------------------------------------------------------

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_array(array: np.ndarray) -> str:
    arr = np.ascontiguousarray(array)
    return hashlib.sha256(arr.tobytes()).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# -----------------------------------------------------------------------------
# Input validation
# -----------------------------------------------------------------------------

def load_status(path: Path) -> pd.DataFrame:
    frame = pd.read_csv(path)

    required = {
        "row_index",
        "relative_path",
        "category",
        "corrected_garment_id",
        "corrected_fold_id",
        "clean_image_relative_path",
        "clean_png_sha256",
        "source_sha256",
    }
    missing = required.difference(frame.columns)
    if missing:
        raise RuntimeError(
            "Annotation-status table missing columns: "
            + ", ".join(sorted(missing))
        )

    if len(frame) != EXPECTED_ROWS:
        raise RuntimeError(
            f"Expected {EXPECTED_ROWS} rows, found {len(frame)}"
        )

    expected_index = np.arange(EXPECTED_ROWS)
    observed_index = frame["row_index"].to_numpy()
    if not np.array_equal(observed_index, expected_index):
        raise RuntimeError("Annotation-status row_index is not exactly 0..2299")

    if not frame["relative_path"].is_unique:
        raise RuntimeError("Duplicate relative_path values found")

    return frame


def resolve_paths(
    status: pd.DataFrame,
    dataset_root: Path,
    clean_root: Path,
):
    raw_rows = []
    clean_rows = []

    for row in status.itertuples(index=False):
        raw_path = dataset_root / row.relative_path
        clean_path = clean_root / row.clean_image_relative_path

        if not raw_path.is_file():
            raise RuntimeError(f"Missing RAW source: {raw_path}")
        if not clean_path.is_file():
            raise RuntimeError(f"Missing CLEAN source: {clean_path}")

        raw_hash = sha256_file(raw_path)
        if raw_hash != row.source_sha256:
            raise RuntimeError(
                f"RAW source hash mismatch for {row.relative_path}: "
                f"{raw_hash} != {row.source_sha256}"
            )

        clean_hash = sha256_file(clean_path)
        if clean_hash != row.clean_png_sha256:
            raise RuntimeError(
                f"CLEAN PNG hash mismatch for {row.relative_path}: "
                f"{clean_hash} != {row.clean_png_sha256}"
            )

        raw_rows.append(
            {
                "relative_path": row.relative_path,
                "category": row.category,
                "path": raw_path,
            }
        )
        clean_rows.append(
            {
                "relative_path": row.relative_path,
                "category": row.category,
                "path": clean_path,
            }
        )

    return raw_rows, clean_rows


# -----------------------------------------------------------------------------
# Exact frozen feature extraction
# -----------------------------------------------------------------------------

def extract_m135(rows, morphology_module) -> np.ndarray:
    matrix = np.vstack(
        [
            morphology_module.morphology_features(row["path"])
            for row in rows
        ]
    ).astype(np.float32, copy=False)

    if matrix.shape != (EXPECTED_ROWS, EXPECTED_M135):
        raise RuntimeError(f"Unexpected M135 shape: {matrix.shape}")
    if not np.isfinite(matrix).all():
        raise RuntimeError("M135 contains non-finite values")

    return matrix


def extract_ra14(rows, ra14_module):
    (
        conditional_angular,
        nonempty,
        normalized_radial_centers,
        max_mass_error,
        normalization_error,
    ) = ra14_module.recover_geometry(rows)

    f2_mag, alpha2_deg = ra14_module.recover_f2(
        conditional_angular
    )

    frame, matrix = ra14_module.build_ra14(
        f2_mag,
        alpha2_deg,
    )

    matrix = np.asarray(matrix, dtype=np.float64)

    if matrix.shape != (EXPECTED_ROWS, EXPECTED_RA14):
        raise RuntimeError(f"Unexpected RA14 shape: {matrix.shape}")
    if not np.isfinite(matrix).all():
        raise RuntimeError("RA14 contains non-finite values")

    diagnostics = {
        "max_relative_mass_error": float(max_mass_error),
        "max_conditional_normalization_error": float(normalization_error),
        "nonempty_shell_fraction": float(np.mean(nonempty)),
        "normalized_radial_centers_count": int(len(normalized_radial_centers)),
    }

    return frame, matrix, diagnostics


# -----------------------------------------------------------------------------
# Output
# -----------------------------------------------------------------------------

def save_npy(path: Path, array: np.ndarray) -> dict:
    np.save(path, array, allow_pickle=False)
    try:
        portable_path = path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except ValueError:
        portable_path = path.name

    return {
        "path": portable_path,
        "shape": list(array.shape),
        "dtype": str(array.dtype),
        "array_sha256": sha256_array(array),
        "saved_npy_sha256": sha256_file(path),
    }


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Materialize PRE-OUTCOME RAW and CLEAN M135 + RA14 feature matrices "
            "for the corrective Experiment 06. This script never fits a model, "
            "produces predictions, or computes predictive metrics."
        )
    )
    parser.add_argument(
        "--dataset-root",
        type=Path,
        required=True,
        help="Root containing the 2,300 native CLO-SKET TIFF sketches.",
    )
    parser.add_argument(
        "--clean-root",
        type=Path,
        required=True,
        help=(
            "Frozen Experiment-08 materialized-v4 root containing "
            "images/0000.png ... images/2299.png."
        ),
    )
    parser.add_argument(
        "--annotation-status",
        type=Path,
        default=DEFAULT_STATUS,
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
    )
    args = parser.parse_args()

    dataset_root = args.dataset_root.expanduser().resolve()
    clean_root = args.clean_root.expanduser().resolve()
    annotation_status = args.annotation_status.expanduser().resolve()
    output_root = args.output_root.expanduser().resolve()

    if not dataset_root.is_dir():
        raise RuntimeError(f"Dataset root does not exist: {dataset_root}")
    if not clean_root.is_dir():
        raise RuntimeError(f"Clean root does not exist: {clean_root}")
    if not annotation_status.is_file():
        raise RuntimeError(
            f"Annotation status does not exist: {annotation_status}"
        )

    output_root.mkdir(parents=True, exist_ok=True)

    status = load_status(annotation_status)
    raw_rows, clean_rows = resolve_paths(
        status,
        dataset_root,
        clean_root,
    )

    morphology_module = load_module(
        "clo_sket_frozen_m135",
        MORPHOLOGY_SOURCE,
    )
    ra14_module = load_module(
        "clo_sket_frozen_ra14",
        RA14_SOURCE,
    )

    print("Extracting RAW M135...")
    raw_m135 = extract_m135(raw_rows, morphology_module)
    raw_m135_hash = sha256_array(raw_m135)
    if raw_m135_hash != EXPECTED_RAW_M135_ARRAY_SHA256:
        raise RuntimeError(
            "RAW M135 historical reproduction failed: "
            f"{raw_m135_hash} != {EXPECTED_RAW_M135_ARRAY_SHA256}"
        )

    print("Extracting RAW RA14...")
    _, raw_ra14, raw_ra14_diag = extract_ra14(
        raw_rows,
        ra14_module,
    )
    raw_ra14_hash = sha256_array(raw_ra14)
    if raw_ra14_hash != EXPECTED_RAW_RA14_ARRAY_SHA256:
        raise RuntimeError(
            "RAW RA14 historical reproduction failed: "
            f"{raw_ra14_hash} != {EXPECTED_RAW_RA14_ARRAY_SHA256}"
        )

    print("Extracting CLEAN M135...")
    clean_m135 = extract_m135(clean_rows, morphology_module)

    print("Extracting CLEAN RA14...")
    _, clean_ra14, clean_ra14_diag = extract_ra14(
        clean_rows,
        ra14_module,
    )

    outputs = {
        "raw_m135": save_npy(
            output_root / "experiment06_corrective_raw_m135.npy",
            raw_m135,
        ),
        "clean_m135": save_npy(
            output_root / "experiment06_corrective_clean_m135.npy",
            clean_m135,
        ),
        "raw_ra14": save_npy(
            output_root / "experiment06_corrective_raw_ra14.npy",
            raw_ra14,
        ),
        "clean_ra14": save_npy(
            output_root / "experiment06_corrective_clean_ra14.npy",
            clean_ra14,
        ),
    }

    manifest = {
        "schema_version": 1,
        "experiment": "CLO-SKET Experiment 06 corrective reanalysis",
        "stage": "PRE_OUTCOME_FEATURE_MATERIALIZATION",
        "rows": EXPECTED_ROWS,
        "conditions": {
            "RAW": (
                "native source canvases + corrected true identity/fold map; "
                "diagnostic only"
            ),
            "CLEAN": (
                "frozen Experiment-08 annotation-controlled materialized-v4 "
                "field + corrected true identity/fold map; confirmatory condition"
            ),
        },
        "feature_definitions": {
            "M135": (
                "exact frozen 64 horizontal + 64 vertical + 7 global "
                "morphology implementation"
            ),
            "RA14": (
                "exact frozen shell-conditioned second-harmonic 14-D "
                "implementation"
            ),
        },
        "input_hashes": {
            "annotation_status_sha256": sha256_file(annotation_status),
            "m135_source_sha256": sha256_file(MORPHOLOGY_SOURCE),
            "ra14_source_sha256": sha256_file(RA14_SOURCE),
        },
        "historical_reproduction_checks": {
            "raw_m135_expected_array_sha256": EXPECTED_RAW_M135_ARRAY_SHA256,
            "raw_m135_observed_array_sha256": raw_m135_hash,
            "raw_m135_exact_match": True,
            "raw_ra14_expected_array_sha256": EXPECTED_RAW_RA14_ARRAY_SHA256,
            "raw_ra14_observed_array_sha256": raw_ra14_hash,
            "raw_ra14_exact_match": True,
        },
        "ra14_diagnostics": {
            "RAW": raw_ra14_diag,
            "CLEAN": clean_ra14_diag,
        },
        "outputs": outputs,
        "classifier_fitted": False,
        "prediction_computed": False,
        "predictive_metric_computed": False,
        "bootstrap_computed": False,
        "permutation_computed": False,
        "outcome_execution_unlocked": False,
        "stop": (
            "PRE-OUTCOME STOP: feature matrices and hashes only. "
            "Do not fit the corrective Experiment-06 classifier until the "
            "feature artifacts and execution implementation are frozen."
        ),
    }

    manifest_path = (
        output_root
        / "experiment06_corrective_feature_manifest.json"
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print("\nExperiment 06 corrective feature materialization: PASS")
    print(f"Rows: {EXPECTED_ROWS}")
    print(f"RAW M135 historical hash: {raw_m135_hash}")
    print(f"RAW RA14 historical hash: {raw_ra14_hash}")
    print(f"CLEAN M135 hash: {outputs['clean_m135']['array_sha256']}")
    print(f"CLEAN RA14 hash: {outputs['clean_ra14']['array_sha256']}")
    print(f"Manifest: {manifest_path}")
    print("STOP — no classifier or predictive outcome was computed.")


if __name__ == "__main__":
    main()
