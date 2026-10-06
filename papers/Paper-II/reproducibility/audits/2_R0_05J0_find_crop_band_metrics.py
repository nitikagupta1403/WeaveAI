from __future__ import annotations

from pathlib import Path
import pandas as pd


ROOTS = [
    Path("/Users/nitikagupta/Research/paper2_r0_05f_crop_only"),
    Path("/Users/nitikagupta/Research/paper2_r0_05g_mechanism"),
    Path("/Users/nitikagupta/Research/paper2_r0_05h_intrinsic"),
    Path("/Users/nitikagupta/Research/paper2_r0_05i_real_garment_canvas"),
]

TOKENS = [
    "low_1_4",
    "mid_5_12",
    "highmid_13_24",
    "high_25_36",
]

print("=" * 140)
print("P2-R0-05J0 — FIND FROZEN CROP-ONLY BAND METRICS")
print("=" * 140)

hits = []

for root in ROOTS:
    if not root.exists():
        continue

    for p in root.rglob("*.csv"):
        try:
            df = pd.read_csv(p, nrows=3, keep_default_na=False)
        except Exception:
            continue

        cols = [str(c) for c in df.columns]
        lowcols = [c.lower() for c in cols]

        band_hits = sum(
            any(tok in c for c in lowcols)
            for tok in TOKENS
        )

        has_rel = any(
            c.lower() == "relative_path"
            for c in cols
        )

        if band_hits >= 3:
            hits.append((p, has_rel, band_hits, cols))

if not hits:
    print("NO CANDIDATE CSV FOUND")
else:
    for i, (p, has_rel, n, cols) in enumerate(hits, start=1):
        print("\n" + "-" * 140)
        print(f"CANDIDATE #{i}")
        print("PATH:", p)
        print("relative_path column:", has_rel)
        print("band-token matches:", n)
        print("COLUMNS:")
        for c in cols:
            print("  ", c)

print("\nSTOP — send this output back before modifying 05J.")