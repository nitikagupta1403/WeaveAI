#!/usr/bin/env python3
"""
P2-R0-05K0 — Targeted PRE-05K schema recovery
Version: P2-R0-05K0-SCHEMA-v1.0

NO 05K spectral outcomes.
Reads headers only + verifies frozen SHA256.
"""

from pathlib import Path
import hashlib
import pandas as pd


ROOT = Path("/Users/nitikagupta/Research")

SOURCES = {
    "V3_CROP_MANIFEST": (
        ROOT / "paper2_r0_05f_crop_vs_resampling"
        / "V3_CROP_ONLY"
        / "materialized_manifest.csv",
        "19ab60c21c71de7918472142c36174ded9f8fae888eeb3320983ca2cc66a545e",
    ),

    "I2_BAND_FRACTIONS": (
        ROOT / "paper2_r0_05i_real_garment_canvas"
        / "P2_R0_05I2_per_image_band_fraction_change.csv",
        "a9a096b4aafe89be79b5d3c35fd3e4dc4e6de046c30326f108d0cbe3601c39e2",
    ),

    "I8_ROBUST_SUPPORT": (
        ROOT / "paper2_r0_05i_real_garment_canvas"
        / "P2_R0_05I6_highfreq_text_tightsupport"
        / "P2_R0_05I8_robust_support_metric_audit"
        / "P2_R0_05I8_per_image_robust_support_metrics.csv",
        "4ac2cc2d5393f9e55effca81358ed147d772d581e630dbe4312ef0490f92e0a0",
    ),

    "J_POPULATION_METRICS": (
        ROOT / "paper2_r0_05i_real_garment_canvas"
        / "P2_R0_05I6_highfreq_text_tightsupport"
        / "P2_R0_05J_population_support_spectral_audit_v2"
        / "P2_R0_05J_per_image_population_metrics.csv",
        "f667d8850c43001f1ee251bc2c14f18765a5289c0ebf8e8be42b972e03f6995a",
    ),

    "H3_IDENTITY_ASSIGNMENTS": (
        ROOT / "paper2_r0_05h_intrinsic_coordinate"
        / "P2_R0_05H3_identity_assignments.csv",
        "d67ad6daf2926727fa823651a63e4954a424ce20a8f83bf5c1632bef3a3b532c",
    ),

    "CORRECTED_FOLD_MAP": (
        ROOT / "WeaveAI/papers/CLO-SKET/evidence/Experiment_06_Corrective"
        / "experiment06_corrected_identity_fold_map.csv",
        "82cda5ce42be46cb939bf15b50171d21c2b62df3d3e065eb8a32bc4e587cca3b",
    ),

    "I4_TEXT_POSITIVE": (
        ROOT / "paper2_r0_05i_real_garment_canvas"
        / "P2_R0_05I4_text_positive_control"
        / "P2_R0_05I4_text_positive_candidates.csv",
        "a99081a2d8428ce923ac6131b253ac5c1a5cc4d403cbe1242ef5d3b76c571cc3",
    ),

    "I6_TEXT_METRICS": (
        ROOT / "paper2_r0_05i_real_garment_canvas"
        / "P2_R0_05I6_highfreq_text_tightsupport"
        / "P2_R0_05I6_per_image_metrics.csv",
        "7987569d0fd08361212d4cad32cf511799ac7538dcb54dfc5dc4104ee933ecfa",
    ),
}


def sha256(path):
    h = hashlib.sha256()

    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)

    return h.hexdigest()


def guard(path):
    # Historical source paths must not be 05K.
    if "05k" in str(path).lower():
        raise RuntimeError(f"FORBIDDEN 05K INPUT: {path}")


print("\nP2-R0-05K0 TARGETED SCHEMA RECOVERY")
print("=" * 78)

all_ok = True

for label, (path, expected_sha) in SOURCES.items():

    guard(path)

    print(f"\n[{label}]")
    print(path)

    if not path.exists():
        print("STATUS: MISSING")
        all_ok = False
        continue

    actual_sha = sha256(path)

    print("expected SHA :", expected_sha)
    print("actual SHA   :", actual_sha)

    if actual_sha != expected_sha:
        print("STATUS       : SHA MISMATCH — STOP FOR THIS SOURCE")
        all_ok = False
        continue

    # Header only. No scientific rows opened yet.
    cols = list(pd.read_csv(path, nrows=0).columns)

    print(f"STATUS       : SHA PASS")
    print(f"N columns    : {len(cols)}")
    print("COLUMNS:")

    for i, col in enumerate(cols):
        print(f"  {i:03d}  {col}")


print("\n" + "=" * 78)

if all_ok:
    print("TARGETED SOURCE HASH CHECK: PASS")
else:
    print("TARGETED SOURCE HASH CHECK: ATTENTION REQUIRED")

print("No 05K support-sweep outcomes were read.")