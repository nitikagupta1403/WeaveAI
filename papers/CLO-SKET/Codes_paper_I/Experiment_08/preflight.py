"""Experiment 08 preflight: validates provenance and mathematics without outcomes."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.metadata as metadata
import json
import math
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd


HERE = Path(__file__).resolve().parent
PAPER_ROOT = HERE.parent.parent
DEFAULT_ROW_MAP = PAPER_ROOT / "evidence/Experiment_07/experiment07_row_map.csv"
DEFAULT_FOLD_MAP = PAPER_ROOT / "evidence/Experiment_07/experiment07_fold_map.csv"
DEFAULT_IDENTITY_OVERRIDES = HERE / "experiment08_identity_overrides.json"

N_ROWS = 2300
N_CATEGORIES = 23
N_IDENTITIES = 230
HISTORICAL_EXPECTED_TEST_ROWS = [459, 460, 462, 460, 459]
CORRECTED_EXPECTED_TEST_ROWS = [459, 460, 461, 460, 460]
EXPECTED_ROW_MAP_SHA256 = "27d84a076afd69e96639388f6a1d576e0c8bc37169a915553e181b02a53f378f"
EXPECTED_FOLD_MAP_SHA256 = "f9d47f79829df94f9751fb11fd8cb16adf70fedee7d546efdfa470054346296c"
RECORDED_HISTORICAL_FOLD_ARRAY_HASH = "ccb6138e4bafb9f889c4c7dc92f3a0447c9d17ea870b34fc0f5c9d80ddf809b7"
ROTATIONS_DEG = [-90, -60, -45, -30, -15, 15, 30, 45, 60, 90]
ALGEBRA_TOLERANCE = 1e-12
EXPECTED_DINOV2_REPO = "https://github.com/facebookresearch/dinov2.git"
EXPECTED_DINOV2_COMMIT = "7764ea0f912e53c92e82eb78a2a1631e92725fc8"
EXPECTED_WEIGHT_BYTES = 88283115
EXPECTED_WEIGHT_SHA256 = "b938bf1bc15cd2ec0feacfe3a1bb553fe8ea9ca46a7e1d8d00217f29aef60cd9"
EXPECTED_FEATURE_ROWS = 2300
EXPECTED_FEATURE_DIMENSIONS = 384
EXPECTED_FEATURE_DTYPE = "float32"
EXPECTED_PYTHON_VERSION = "3.12.13"
REQUIRED_PACKAGES = {
    "numpy": "2.1.3",
    "pillow": "11.3.0",
    "pandas": "2.2.3",
    "scikit-learn": "1.6.1",
    "torch": "2.11.0",
    "torchvision": "0.26.0",
}


def sha256_file(path: Path, block_size: int = 1 << 20) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(block_size):
            digest.update(block)
    return digest.hexdigest()


def canonical_array_sha256(array: np.ndarray) -> str:
    """Experiment 08 canonical array hash: metadata plus contiguous little-endian bytes."""
    value = np.asarray(array)
    dtype = value.dtype.newbyteorder("<")
    canonical = np.ascontiguousarray(value.astype(dtype, copy=False))
    header = json.dumps(
        {"dtype": canonical.dtype.str, "shape": list(canonical.shape), "order": "C"},
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(header + b"\n" + canonical.tobytes(order="C")).hexdigest()


def normalized_relative_path(runtime_path: str) -> str:
    parts = Path(runtime_path.replace("\\", "/")).parts
    lowered = [part.casefold() for part in parts]
    for marker in ("clo-sket", "clo_sket"):
        matches = [index for index, part in enumerate(lowered) if part == marker]
        if matches:
            return Path(*parts[matches[-1] + 1 :]).as_posix()
    if len(parts) < 2:
        raise ValueError(f"Cannot recover category/filename from path: {runtime_path}")
    return Path(parts[-2], parts[-1]).as_posix()


def validate_public_maps(row_map_path: Path, fold_map_path: Path) -> tuple[pd.DataFrame, dict]:
    observed_row_hash = sha256_file(row_map_path)
    observed_fold_hash = sha256_file(fold_map_path)
    if observed_row_hash != EXPECTED_ROW_MAP_SHA256:
        raise RuntimeError(f"Authoritative row-map hash mismatch: {observed_row_hash}")
    if observed_fold_hash != EXPECTED_FOLD_MAP_SHA256:
        raise RuntimeError(f"Authoritative fold-map hash mismatch: {observed_fold_hash}")

    rows = pd.read_csv(row_map_path)
    required = {"row_index", "image_path_runtime", "category", "garment_id", "fold_id"}
    missing = required.difference(rows.columns)
    if missing:
        raise RuntimeError(f"Row map lacks required columns: {sorted(missing)}")
    if len(rows) != N_ROWS or rows["row_index"].tolist() != list(range(N_ROWS)):
        raise RuntimeError("Row map must contain the exact ordered row indices 0..2299")
    if rows["category"].nunique() != N_CATEGORIES:
        raise RuntimeError("Expected 23 categories")
    if rows["garment_id"].nunique() != N_IDENTITIES:
        raise RuntimeError("Expected 230 garment identities")
    if sorted(rows["fold_id"].unique().tolist()) != list(range(5)):
        raise RuntimeError("Expected fold IDs 0..4")

    structural = []
    for fold in range(5):
        test = rows[rows["fold_id"] == fold]
        train = rows[rows["fold_id"] != fold]
        test_ids = set(test["garment_id"])
        train_ids = set(train["garment_id"])
        record = {
            "fold": fold,
            "train_rows": len(train),
            "test_rows": len(test),
            "train_identities": len(train_ids),
            "test_identities": len(test_ids),
            "overlapping_identities": len(train_ids & test_ids),
        }
        if record["test_rows"] != HISTORICAL_EXPECTED_TEST_ROWS[fold]:
            raise RuntimeError(f"Fold {fold} test-row mismatch: {record}")
        if record["train_identities"] != 184 or record["test_identities"] != 46:
            raise RuntimeError(f"Fold {fold} identity-count mismatch: {record}")
        if record["overlapping_identities"] != 0:
            raise RuntimeError(f"Fold {fold} has identity leakage: {record}")
        structural.append(record)

    expected_summary = pd.read_csv(fold_map_path).to_dict(orient="records")
    if structural != expected_summary:
        raise RuntimeError("Recomputed fold structure does not match the public fold summary")

    return rows, {
        "row_map_sha256": observed_row_hash,
        "fold_map_sha256": observed_fold_hash,
        "historical_fold_array_hash_recorded_only": RECORDED_HISTORICAL_FOLD_ARRAY_HASH,
        "experiment08_fold_array_sha256": canonical_array_sha256(
            rows["fold_id"].to_numpy(dtype=np.int64)
        ),
        "folds": structural,
    }



def apply_identity_overrides(
    rows: pd.DataFrame, overrides_path: Path, historical_audit: dict
) -> tuple[pd.DataFrame, dict]:
    """Apply frozen, pre-outcome visual identity corrections without renaming files."""
    specification = json.loads(overrides_path.read_text(encoding="utf-8"))
    if specification.get("stage") != "PRE_OUTCOME_IDENTITY_AUDIT":
        raise RuntimeError("Identity overrides are not marked as pre-outcome")
    if specification.get("source_files_modified") is not False:
        raise RuntimeError("Identity override specification must preserve source files")
    if specification.get("selection_used_learned_features") is not False:
        raise RuntimeError("Identity overrides must not use learned features")
    if specification.get("selection_used_classifier_outcomes") is not False:
        raise RuntimeError("Identity overrides must not use classifier outcomes")

    corrected = rows.copy()
    corrected["relative_path"] = corrected["image_path_runtime"].map(
        normalized_relative_path
    )
    applied = []
    for override in specification["overrides"]:
        matches = corrected.index[
            corrected["relative_path"].str.casefold()
            == override["relative_path"].casefold()
        ].tolist()
        if len(matches) != 1:
            raise RuntimeError(
                f"Identity override must match exactly one row: {override}"
            )
        index = matches[0]
        observed_id = corrected.at[index, "garment_id"]
        observed_fold = int(corrected.at[index, "fold_id"])
        if observed_id != override["historical_garment_id"]:
            raise RuntimeError(
                f"Historical garment mismatch for {override['relative_path']}: "
                f"{observed_id}"
            )
        if observed_fold != int(override["historical_fold_id"]):
            raise RuntimeError(
                f"Historical fold mismatch for {override['relative_path']}: "
                f"{observed_fold}"
            )
        corrected.at[index, "garment_id"] = override["corrected_garment_id"]
        corrected.at[index, "fold_id"] = int(override["corrected_fold_id"])
        applied.append(override)

    counts = corrected.groupby("garment_id").size()
    distribution = {
        str(int(size)): int(number)
        for size, number in counts.value_counts().sort_index().items()
    }
    if distribution != {"9": 1, "10": 228, "11": 1}:
        raise RuntimeError(f"Unexpected corrected identity-size distribution: {distribution}")
    preserved = specification["preserved_imbalance"]
    for garment_id in ("Jumpsuit__G02", "Jumpsuit__G06"):
        if int(counts[garment_id]) != int(preserved[garment_id]):
            raise RuntimeError(f"Preserved Jumpsuit count mismatch: {garment_id}")

    structural = []
    for fold in range(5):
        test = corrected[corrected["fold_id"] == fold]
        train = corrected[corrected["fold_id"] != fold]
        test_ids = set(test["garment_id"])
        train_ids = set(train["garment_id"])
        record = {
            "fold": fold,
            "train_rows": len(train),
            "test_rows": len(test),
            "train_identities": len(train_ids),
            "test_identities": len(test_ids),
            "overlapping_identities": len(train_ids & test_ids),
        }
        if record["test_rows"] != CORRECTED_EXPECTED_TEST_ROWS[fold]:
            raise RuntimeError(f"Corrected fold {fold} row mismatch: {record}")
        if record["train_identities"] != 184 or record["test_identities"] != 46:
            raise RuntimeError(f"Corrected fold {fold} identity mismatch: {record}")
        if record["overlapping_identities"] != 0:
            raise RuntimeError(f"Corrected fold {fold} has identity leakage: {record}")
        structural.append(record)

    return corrected.drop(columns=["relative_path"]), {
        "row_map_sha256": historical_audit["row_map_sha256"],
        "fold_map_sha256": historical_audit["fold_map_sha256"],
        "historical_public_map_audit": historical_audit,
        "identity_overrides_path": str(overrides_path),
        "identity_overrides_sha256": sha256_file(overrides_path),
        "identity_override_count": len(applied),
        "identity_size_distribution": distribution,
        "experiment08_fold_array_sha256": canonical_array_sha256(
            corrected["fold_id"].to_numpy(dtype=np.int64)
        ),
        "folds": structural,
    }



def enumerate_dataset(data_root: Path) -> list[Path]:
    files = sorted(
        (path for path in data_root.rglob("*") if path.is_file() and path.suffix.casefold() in {".tif", ".tiff"}),
        key=lambda path: path.relative_to(data_root).as_posix(),
    )
    if len(files) != N_ROWS:
        raise RuntimeError(f"Expected {N_ROWS} TIFF files, found {len(files)}")
    relative = [path.relative_to(data_root).as_posix() for path in files]
    if len(relative) != len(set(relative)):
        raise RuntimeError("Duplicate normalized dataset paths detected")
    return files


def join_and_manifest(data_root: Path, files: list[Path], rows: pd.DataFrame) -> list[dict]:
    by_relative = {path.relative_to(data_root).as_posix().casefold(): path for path in files}
    authoritative = rows.copy()
    authoritative["relative_path"] = authoritative["image_path_runtime"].map(normalized_relative_path)
    if authoritative["relative_path"].str.casefold().duplicated().any():
        raise RuntimeError("Authoritative row map has duplicate normalized relative paths")

    manifest = []
    for record in authoritative.to_dict(orient="records"):
        key = record["relative_path"].casefold()
        path = by_relative.pop(key, None)
        if path is None:
            raise RuntimeError(f"Dataset file missing for authoritative row: {record['relative_path']}")
        manifest.append(
            {
                "row_index": int(record["row_index"]),
                "relative_path": path.relative_to(data_root).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
                "category": record["category"],
                "garment_id": record["garment_id"],
                "fold_id": int(record["fold_id"]),
            }
        )
    if by_relative:
        raise RuntimeError(f"Dataset contains {len(by_relative)} files absent from the row map")
    return manifest


def f2_from_angles(theta: np.ndarray, probability: np.ndarray) -> complex:
    return np.sum(probability * np.exp(-2j * theta))


def axial_angle(f2: complex) -> float:
    return (-0.5 * np.angle(f2)) % math.pi


def axial_distance(left: float, right: float) -> float:
    return 0.5 * abs(np.angle(np.exp(2j * (left - right))))


def analytic_rotation_tests() -> dict:
    theta = np.linspace(0.0, 2.0 * math.pi, 720, endpoint=False)
    probability = np.exp(3.0 * np.cos(2.0 * (theta - math.radians(17.0))))
    probability /= probability.sum()
    base = f2_from_angles(theta, probability)
    base_alpha = axial_angle(base)
    results = []
    for degrees in ROTATIONS_DEG:
        phi = math.radians(degrees)
        transformed = np.exp(-2j * phi) * base
        magnitude_error = abs(abs(transformed) - abs(base))
        expected_alpha = (base_alpha + phi) % math.pi
        angle_error = axial_distance(axial_angle(transformed), expected_alpha)
        vector_observed = np.array([math.cos(2 * axial_angle(transformed)), math.sin(2 * axial_angle(transformed))])
        rotation = np.array([[math.cos(2 * phi), -math.sin(2 * phi)], [math.sin(2 * phi), math.cos(2 * phi)]])
        vector_base = np.array([math.cos(2 * base_alpha), math.sin(2 * base_alpha)])
        vector_error = float(np.linalg.norm(vector_observed - rotation @ vector_base))
        if max(magnitude_error, angle_error, vector_error) >= ALGEBRA_TOLERANCE:
            raise RuntimeError(f"Analytic rotation test failed at {degrees} degrees")
        results.append({"rotation_degrees": degrees, "magnitude_error": magnitude_error, "axial_error_radians": angle_error, "vector_error": vector_error})

    horizontal = f2_from_angles(np.array([0.0, math.pi]), np.array([0.5, 0.5]))
    rotated = np.exp(-2j * math.radians(30.0)) * horizontal
    convention_error = axial_distance(axial_angle(rotated), math.radians(30.0))
    if convention_error >= ALGEBRA_TOLERANCE:
        raise RuntimeError("Synthetic +30-degree Cartesian convention test failed")
    return {"tolerance": ALGEBRA_TOLERANCE, "cartesian_plus_30_error_radians": convention_error, "rotations": results}


def write_manifest(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def get_version(name: str) -> str:
    try:
        return metadata.version(name)
    except metadata.PackageNotFoundError:
        raise RuntimeError(f"Required package not installed: {name}")


def git_output(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True).strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--row-map", type=Path, default=DEFAULT_ROW_MAP)
    parser.add_argument("--fold-map", type=Path, default=DEFAULT_FOLD_MAP)
    parser.add_argument("--identity-overrides", type=Path, default=DEFAULT_IDENTITY_OVERRIDES)
    parser.add_argument("--dinov2-root", type=Path, default=None)
    parser.add_argument("--weights", type=Path, default=None)
    parser.add_argument("--output-root", type=Path, required=True)
    return parser.parse_args()


def validate_environment() -> dict:
    observed_python = sys.version.split()[0]
    if observed_python != EXPECTED_PYTHON_VERSION:
        raise RuntimeError(f"Python version mismatch: {observed_python} != {EXPECTED_PYTHON_VERSION}")

    observed = {}
    for package, expected in REQUIRED_PACKAGES.items():
        version = get_version(package)
        observed[package] = version
        if version != expected:
            raise RuntimeError(f"Package version mismatch: {package}={version} != {expected}")

    return {"python": observed_python, "packages": observed}


def validate_dinov2_repo(repo: Path | None) -> dict:
    if repo is None:
        return {"status": "SKIPPED", "reason": "No --dinov2-root supplied; repo pin not checked in read-only preflight."}
    if not repo.exists():
        raise RuntimeError(f"DINOv2 repo path does not exist: {repo}")
    if not (repo / ".git").exists():
        raise RuntimeError(f"DINOv2 path is not a git repository: {repo}")
    commit = git_output(repo, "rev-parse", "HEAD")
    if commit != EXPECTED_DINOV2_COMMIT:
        raise RuntimeError(f"DINOv2 source commit mismatch: {commit} != {EXPECTED_DINOV2_COMMIT}")
    if git_output(repo, "status", "--short"):
        raise RuntimeError("DINOv2 source worktree is not clean")
    return {
        "status": "PASS",
        "repository": EXPECTED_DINOV2_REPO,
        "commit": commit,
        "clean_worktree": True,
    }


def validate_weight(path: Path | None) -> dict:
    if path is None:
        return {"status": "SKIPPED", "reason": "No --weights supplied; checkpoint hash not checked in read-only preflight."}
    if not path.exists():
        raise RuntimeError(f"Weight path does not exist: {path}")
    size = path.stat().st_size
    digest = sha256_file(path)
    if size != EXPECTED_WEIGHT_BYTES:
        raise RuntimeError(f"Weight byte count mismatch: {size} != {EXPECTED_WEIGHT_BYTES}")
    if digest != EXPECTED_WEIGHT_SHA256:
        raise RuntimeError(f"Weight SHA-256 mismatch: {digest} != {EXPECTED_WEIGHT_SHA256}")
    return {
        "status": "PASS",
        "path": str(path),
        "bytes": size,
        "sha256": digest,
        "model_identifier": "dinov2_vits14",
    }


def main() -> None:
    args = parse_args()
    environment = validate_environment()
    historical_rows, historical_audit = validate_public_maps(args.row_map, args.fold_map)
    rows, fold_audit = apply_identity_overrides(
        historical_rows, args.identity_overrides, historical_audit
    )
    files = enumerate_dataset(args.data_root)
    source_manifest = join_and_manifest(args.data_root, files, rows)
    math_audit = analytic_rotation_tests()
    dinov2_repo = validate_dinov2_repo(args.dinov2_root)
    weight = validate_weight(args.weights)
    args.output_root.mkdir(parents=True, exist_ok=True)
    manifest_path = args.output_root / "experiment08_source_manifest.csv"
    write_manifest(manifest_path, source_manifest)
    report = {
        "experiment": "CLO-SKET Experiment 08",
        "stage": "PRE_OUTCOME_PREFLIGHT_ONLY",
        "learned_features_extracted": False,
        "classifier_fitted": False,
        "predictive_outcome_computed": False,
        "environment": environment,
        "dinov2_repo": dinov2_repo,
        "pretrained_weight": weight,
        "expected_model": {
            "identifier": "dinov2_vits14",
            "repository": EXPECTED_DINOV2_REPO,
            "commit": EXPECTED_DINOV2_COMMIT,
            "weight_filename": "dinov2_vits14_pretrain.pth",
            "expected_weight_sha256": EXPECTED_WEIGHT_SHA256,
            "expected_weight_bytes": EXPECTED_WEIGHT_BYTES,
            "expected_feature_rows": EXPECTED_FEATURE_ROWS,
            "expected_feature_dimensions": EXPECTED_FEATURE_DIMENSIONS,
            "expected_dtype": EXPECTED_FEATURE_DTYPE,
            "pooling": "final normalized class token (x_norm_clstoken)",
            "preprocessing": "frozen Experiment-08 provenance lock",
        },
        "source_manifest": str(manifest_path),
        "source_manifest_sha256": sha256_file(manifest_path),
        "fold_audit": fold_audit,
        "analytic_rotation_audit": math_audit,
    }
    report_path = args.output_root / "experiment08_preflight.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"PASS: pre-outcome preflight completed; report={report_path}")
    print("STOP: no learned feature was extracted and no classifier was fitted")


if __name__ == "__main__":
    main()
