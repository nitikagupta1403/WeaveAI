#!/usr/bin/env python3
"""Deterministic, label-blind CPU extraction of frozen DINOv2 ViT-S/14 features."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import platform
import subprocess
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image
import torch


EXPECTED_MATERIALIZED_MANIFEST_SHA256 = "071ee7b6c535361951f9eb0044ff166c9a4d42b0ef55a3c0a72aab27af2af6a4"
EXPECTED_DINOV2_COMMIT = "7764ea0f912e53c92e82eb78a2a1631e92725fc8"
EXPECTED_WEIGHT_BYTES = 88283115
EXPECTED_WEIGHT_SHA256 = "b938bf1bc15cd2ec0feacfe3a1bb553fe8ea9ca46a7e1d8d00217f29aef60cd9"
EXPECTED_ROWS = 2300
EXPECTED_DIMENSIONS = 384
MEAN = np.asarray([0.485, 0.456, 0.406], dtype=np.float32)[:, None, None]
STD = np.asarray([0.229, 0.224, 0.225], dtype=np.float32)[:, None, None]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_output(repo: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), *args],
        text=True,
    ).strip()


def resolve_image_path(root: Path, relative: str) -> Path:
    candidates = [root / relative, root / "images" / relative]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(f"Materialized image is missing: {relative}")


def load_batch(paths: list[Path]) -> torch.Tensor:
    rows = []
    for path in paths:
        with Image.open(path) as image:
            array = np.asarray(image.convert("L"), dtype=np.float32) / 255.0
        if array.shape != (224, 224):
            raise RuntimeError(f"Expected 224x224 image, got {array.shape}: {path}")
        rgb = np.repeat(array[None, :, :], 3, axis=0)
        rows.append((rgb - MEAN) / STD)
    return torch.from_numpy(np.stack(rows, axis=0))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--materialized-root", type=Path, required=True)
    parser.add_argument("--materialized-manifest", type=Path, required=True)
    parser.add_argument("--dinov2-repo", type=Path, required=True)
    parser.add_argument("--weight", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--threads", type=int, default=1)
    args = parser.parse_args()

    if args.batch_size < 1 or args.threads < 1:
        raise ValueError("batch-size and threads must be positive")

    manifest_sha = sha256_file(args.materialized_manifest)
    if manifest_sha != EXPECTED_MATERIALIZED_MANIFEST_SHA256:
        raise RuntimeError(
            f"Materialized manifest SHA-256 mismatch: {manifest_sha} != "
            f"{EXPECTED_MATERIALIZED_MANIFEST_SHA256}"
        )

    source_commit = git_output(args.dinov2_repo, "rev-parse", "HEAD")
    if source_commit != EXPECTED_DINOV2_COMMIT:
        raise RuntimeError(
            f"DINOv2 source commit mismatch: {source_commit} != {EXPECTED_DINOV2_COMMIT}"
        )
    if git_output(args.dinov2_repo, "status", "--short"):
        raise RuntimeError("DINOv2 source worktree is not clean")

    weight_bytes = args.weight.stat().st_size
    weight_sha = sha256_file(args.weight)
    if weight_bytes != EXPECTED_WEIGHT_BYTES or weight_sha != EXPECTED_WEIGHT_SHA256:
        raise RuntimeError("DINOv2 weight byte count or SHA-256 mismatch")

    manifest = pd.read_csv(args.materialized_manifest, keep_default_na=False)
    required = {"row_index", "relative_path", "output_relative_path", "output_png_sha256"}
    missing = required.difference(manifest.columns)
    if missing:
        raise RuntimeError(f"Materialized manifest columns missing: {sorted(missing)}")
    manifest = manifest.sort_values("row_index", kind="stable").reset_index(drop=True)
    if len(manifest) != EXPECTED_ROWS:
        raise RuntimeError(f"Expected {EXPECTED_ROWS} rows, found {len(manifest)}")
    if manifest["row_index"].tolist() != list(range(EXPECTED_ROWS)):
        raise RuntimeError("row_index is not the exact ordered range 0..2299")
    if manifest["relative_path"].nunique() != EXPECTED_ROWS:
        raise RuntimeError("Materialized manifest paths are not unique")

    paths = []
    for record in manifest.to_dict("records"):
        path = resolve_image_path(args.materialized_root, record["output_relative_path"])
        digest = sha256_file(path)
        if digest != record["output_png_sha256"]:
            raise RuntimeError(f"PNG SHA-256 mismatch: {record['relative_path']}")
        paths.append(path)

    os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
    torch.set_num_threads(args.threads)
    torch.set_num_interop_threads(1)
    torch.use_deterministic_algorithms(True)
    torch.manual_seed(0)

    model = torch.hub.load(
        str(args.dinov2_repo),
        "dinov2_vits14",
        source="local",
        pretrained=False,
    )
    state = torch.load(args.weight, map_location="cpu", weights_only=True)
    model.load_state_dict(state, strict=True)
    model.eval()
    model.requires_grad_(False)
    model.to("cpu")

    parameters = sum(parameter.numel() for parameter in model.parameters())
    if parameters != 22056576:
        raise RuntimeError(f"Unexpected model parameter count: {parameters}")

    embeddings = np.empty((EXPECTED_ROWS, EXPECTED_DIMENSIONS), dtype=np.float32)
    with torch.inference_mode():
        for start in range(0, EXPECTED_ROWS, args.batch_size):
            stop = min(start + args.batch_size, EXPECTED_ROWS)
            batch = load_batch(paths[start:stop]).to("cpu")
            features = model.forward_features(batch)["x_norm_clstoken"]
            values = features.detach().cpu().numpy().astype(np.float32, copy=False)
            if values.shape != (stop - start, EXPECTED_DIMENSIONS):
                raise RuntimeError(f"Unexpected feature shape: {values.shape}")
            if not np.isfinite(values).all():
                raise RuntimeError(f"Non-finite feature in rows {start}:{stop}")
            embeddings[start:stop] = values
            print(f"Extracted {stop}/{EXPECTED_ROWS}", flush=True)

    args.output_root.mkdir(parents=True, exist_ok=True)
    embedding_path = args.output_root / "experiment08_dinov2_vits14_embeddings.npy"
    row_path = args.output_root / "experiment08_dinov2_embedding_rows.csv"
    report_path = args.output_root / "experiment08_dinov2_extraction_report.json"

    np.save(embedding_path, embeddings, allow_pickle=False)
    with row_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["row_index", "relative_path"])
        writer.writerows(
            zip(manifest["row_index"].tolist(), manifest["relative_path"].tolist())
        )

    raw_embedding_sha = hashlib.sha256(
        np.ascontiguousarray(embeddings).tobytes(order="C")
    ).hexdigest()
    report = {
        "stage": "LABEL_BLIND_DINOV2_FEATURE_EXTRACTION",
        "learned_features_extracted": True,
        "classifier_fitted": False,
        "predictive_outcome_computed": False,
        "labels_used_during_extraction": False,
        "device": "cpu",
        "deterministic_algorithms": True,
        "torch_threads": args.threads,
        "torch_interop_threads": 1,
        "batch_size": args.batch_size,
        "platform": platform.platform(),
        "python": platform.python_version(),
        "torch": torch.__version__,
        "model": "dinov2_vits14",
        "source_commit": source_commit,
        "weight_bytes": weight_bytes,
        "weight_sha256": weight_sha,
        "rows": EXPECTED_ROWS,
        "dimensions": EXPECTED_DIMENSIONS,
        "dtype": "float32",
        "pooling": "x_norm_clstoken",
        "augmentation": "none",
        "materialized_manifest_sha256": manifest_sha,
        "embedding_npy_sha256": sha256_file(embedding_path),
        "embedding_raw_c_array_sha256": raw_embedding_sha,
        "row_csv_sha256": sha256_file(row_path),
    }
    report_path.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(f"PASS: {EXPECTED_ROWS} label-blind CPU embeddings extracted")
    print(f"Report: {report_path}")
    print("STOP: no classifier was fitted and no predictive outcome was computed")


if __name__ == "__main__":
    main()
