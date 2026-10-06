#!/usr/bin/env python3
"""
P2-R0-05K0 — Gate B
Historical sentinel-source table construction

Version: P2-R0-05K0-GATEB-v1.0

STRICT:
- PRE-05K historical data only.
- No 05K support-sweep outcomes.
- No sentinel selection.
- No ranking of S01-S10.
- No manual substitutions.

PURPOSE:
Construct and validate the exact 2300-row historical table that will
later feed the frozen deterministic sentinel selector.
"""

from pathlib import Path
import hashlib
import json
import numpy as np
import pandas as pd


ROOT = Path("/Users/nitikagupta/Research")

OUT = (
    ROOT /
    "P2_R0_05K0_sentinel_freeze"
)

OUT.mkdir(parents=True, exist_ok=True)

VERSION = "P2-R0-05K0-GATEB-v1.0"

KEY = [
    "row_index",
    "relative_path",
    "category",
]


SOURCES = {

    "V3": (
        ROOT /
        "paper2_r0_05f_crop_vs_resampling/V3_CROP_ONLY/"
        "materialized_manifest.csv",

        "19ab60c21c71de7918472142c36174ded9f8fae888eeb3320983ca2cc66a545e",
    ),

    "I2": (
        ROOT /
        "paper2_r0_05i_real_garment_canvas/"
        "P2_R0_05I2_per_image_band_fraction_change.csv",

        "a9a096b4aafe89be79b5d3c35fd3e4dc4e6de046c30326f108d0cbe3601c39e2",
    ),

    "I8": (
        ROOT /
        "paper2_r0_05i_real_garment_canvas/"
        "P2_R0_05I6_highfreq_text_tightsupport/"
        "P2_R0_05I8_robust_support_metric_audit/"
        "P2_R0_05I8_per_image_robust_support_metrics.csv",

        "4ac2cc2d5393f9e55effca81358ed147d772d581e630dbe4312ef0490f92e0a0",
    ),

    "J": (
        ROOT /
        "paper2_r0_05i_real_garment_canvas/"
        "P2_R0_05I6_highfreq_text_tightsupport/"
        "P2_R0_05J_population_support_spectral_audit_v2/"
        "P2_R0_05J_per_image_population_metrics.csv",

        "f667d8850c43001f1ee251bc2c14f18765a5289c0ebf8e8be42b972e03f6995a",
    ),

    "H3": (
        ROOT /
        "paper2_r0_05h_intrinsic_coordinate/"
        "P2_R0_05H3_identity_assignments.csv",

        "d67ad6daf2926727fa823651a63e4954a424ce20a8f83bf5c1632bef3a3b532c",
    ),

    "FOLD_CORRECTED": (
        ROOT /
        "WeaveAI/papers/CLO-SKET/evidence/"
        "Experiment_06_Corrective/"
        "experiment06_corrected_identity_fold_map.csv",

        "82cda5ce42be46cb939bf15b50171d21c2b62df3d3e065eb8a32bc4e587cca3b",
    ),

    "I4": (
        ROOT /
        "paper2_r0_05i_real_garment_canvas/"
        "P2_R0_05I4_text_positive_control/"
        "P2_R0_05I4_text_positive_candidates.csv",

        "a99081a2d8428ce923ac6131b253ac5c1a5cc4d403cbe1242ef5d3b76c571cc3",
    ),

    "I6": (
        ROOT /
        "paper2_r0_05i_real_garment_canvas/"
        "P2_R0_05I6_highfreq_text_tightsupport/"
        "P2_R0_05I6_per_image_metrics.csv",

        "7987569d0fd08361212d4cad32cf511799ac7538dcb54dfc5dc4104ee933ecfa",
    ),
}


def sha256(path):
    h = hashlib.sha256()

    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)

    return h.hexdigest()


def assert_pre05k(path):
    if "05k" in str(path).lower():
        raise RuntimeError(
            f"FORBIDDEN 05K INPUT: {path}"
        )


def load_verified(label):
    path, expected = SOURCES[label]

    assert_pre05k(path)

    if not path.exists():
        raise FileNotFoundError(path)

    actual = sha256(path)

    if actual != expected:
        raise RuntimeError(
            f"{label}: SHA mismatch\n"
            f"expected {expected}\n"
            f"actual   {actual}"
        )

    df = pd.read_csv(path)

    print(
        f"{label:15s} "
        f"rows={len(df):5d} "
        f"cols={len(df.columns):3d} "
        f"SHA PASS"
    )

    return df


def assert_unique(df, cols, label):
    ndup = df.duplicated(cols).sum()

    if ndup:
        raise RuntimeError(
            f"{label}: {ndup} duplicate keys on {cols}"
        )


def assert_same_keys(a, b, cols, la, lb):
    ka = set(map(tuple, a[cols].to_numpy()))
    kb = set(map(tuple, b[cols].to_numpy()))

    if ka != kb:
        only_a = len(ka - kb)
        only_b = len(kb - ka)

        raise RuntimeError(
            f"KEY MISMATCH {la} vs {lb}: "
            f"only_{la}={only_a}, "
            f"only_{lb}={only_b}"
        )


print("\nP2-R0-05K0 GATE B")
print("=" * 78)

v3 = load_verified("V3")
i2 = load_verified("I2")
i8 = load_verified("I8")
j = load_verified("J")
h3 = load_verified("H3")
foldcorr = load_verified("FOLD_CORRECTED")
i4 = load_verified("I4")
i6 = load_verified("I6")


# ------------------------------------------------------------
# 1. Establish canonical 2300-sketch universe
# ------------------------------------------------------------

# ------------------------------------------------------------
# 1. Establish canonical 2300-sketch universe
#
# V3 manifest does NOT contain category.
# Therefore:
#   V3 provenance key = row_index + relative_path
#
# Historical analytical tables contain category, so:
#   analytical key = row_index + relative_path + category
#
# We do NOT derive category from filenames/paths.
# ------------------------------------------------------------

V3_KEY = [
    "row_index",
    "relative_path",
]

ANALYTICAL_KEY = [
    "row_index",
    "relative_path",
    "category",
]


# ----- row-count assertions -----

for label, df in [
    ("V3", v3),
    ("I2", i2),
    ("I8", i8),
    ("J", j),
    ("I6", i6),
]:
    if len(df) != 2300:
        raise RuntimeError(
            f"{label}: expected 2300 rows, got {len(df)}"
        )


# ----- uniqueness assertions -----

assert_unique(
    v3,
    V3_KEY,
    "V3",
)

for label, df in [
    ("I2", i2),
    ("I8", i8),
    ("J", j),
    ("I6", i6),
]:
    assert_unique(
        df,
        ANALYTICAL_KEY,
        label,
    )


# ------------------------------------------------------------
# V3 provenance alignment
#
# Compare only fields actually present in V3.
# Category is NOT reconstructed or inferred.
# ------------------------------------------------------------

assert_same_keys(
    v3,
    i2,
    V3_KEY,
    "V3",
    "I2",
)

print(
    "\nV3 ↔ I2 provenance alignment "
    "(row_index + relative_path): PASS"
)


# ------------------------------------------------------------
# Analytical-table alignment
#
# I2 is the analytical reference table because it carries
# canonical garment_identity plus historical band fractions.
# ------------------------------------------------------------

assert_same_keys(
    i2,
    i8,
    ANALYTICAL_KEY,
    "I2",
    "I8",
)

assert_same_keys(
    i2,
    j,
    ANALYTICAL_KEY,
    "I2",
    "J",
)

assert_same_keys(
    i2,
    i6,
    ANALYTICAL_KEY,
    "I2",
    "I6",
)

print(
    "I2 ↔ I8/J/I6 analytical-key universe: PASS"
)

print(
    "2300-row historical sketch universe: PASS"
)
if len(df) != 2300:
    raise RuntimeError(
        f"{label}: expected 2300 rows, got {len(df)}"
    )

assert_unique(df, KEY, label)

print("\n2300-row stable-key universe: PASS")


# ------------------------------------------------------------
# 2. Identity agreement
# ------------------------------------------------------------

identity_audit = (
    i2[
        KEY + ["garment_identity"]
    ]
    .merge(
        j[
            KEY + ["garment_identity"]
        ],
        on=KEY,
        suffixes=("_i2", "_j"),
        validate="one_to_one",
    )
)

identity_match = (
    identity_audit["garment_identity_i2"].astype(str)
    ==
    identity_audit["garment_identity_j"].astype(str)
)

if not identity_match.all():
    raise RuntimeError(
        "I2/J garment_identity mismatch"
    )

print("I2/J canonical identity agreement: PASS")


# ------------------------------------------------------------
# 3. Construct base selection table
# ------------------------------------------------------------

base = i2[
    KEY + [
        "garment_identity",
        "crop_low_1_4_fraction",
        "crop_high_25_36_fraction",
        "band_fraction_l1_change",
    ]
].copy()

base = base.rename(
    columns={
        "band_fraction_l1_change":
            "raw_crop_band_l1",
    }
)


# ------------------------------------------------------------
# 4. Add CROP q99/Rgrid from 05J
# ------------------------------------------------------------

q99 = j[
    KEY + [
        "crop_q99_radius_to_grid",
    ]
].copy()

base = base.merge(
    q99,
    on=KEY,
    how="left",
    validate="one_to_one",
)

if base["crop_q99_radius_to_grid"].isna().any():
    raise RuntimeError(
        "Missing CROP q99/Rgrid after J merge"
    )

print("CROP q99/Rgrid merge: PASS")


# ------------------------------------------------------------
# 5. S09 historical outlier metric from 05I8
#
# fragile max/Rgrid - robust q99/Rgrid
# =
# (rmax - rq99)/Rgrid
# ------------------------------------------------------------

support = i8[
    KEY + [
        "garment_id",
        "fragile_max_radius_to_grid",
        "robust_q99_radius_to_grid",
    ]
].copy()

support["s09_outlier_score"] = (
    support["fragile_max_radius_to_grid"]
    -
    support["robust_q99_radius_to_grid"]
)

base = base.merge(
    support[
        KEY + [
            "s09_outlier_score",
        ]
    ],
    on=KEY,
    how="left",
    validate="one_to_one",
)

if base["s09_outlier_score"].isna().any():
    raise RuntimeError(
        "Missing S09 outlier score"
    )

print("S09 historical support metric: PASS")


# ------------------------------------------------------------
# 6. Text-positive membership + RAW->TEXT L1
# ------------------------------------------------------------

assert_unique(i4, KEY, "I4")

text_keys = set(
    map(
        tuple,
        i4[KEY].to_numpy()
    )
)

base["text_positive"] = [
    tuple(x) in text_keys
    for x in base[KEY].to_numpy()
]


text_metrics = i6[
    KEY + [
        "raw_to_text_band_l1_change",
        "n_text_boxes",
    ]
].copy()

base = base.merge(
    text_metrics,
    on=KEY,
    how="left",
    validate="one_to_one",
)

if base["raw_to_text_band_l1_change"].isna().any():
    raise RuntimeError(
        "Missing RAW->TEXT L1"
    )

print(
    "Text-positive membership: "
    f"{int(base['text_positive'].sum())} rows"
)
print("RAW->TEXT L1 merge: PASS")


# ------------------------------------------------------------
# 7. Canonical assigned test fold from frozen H3 package
# ------------------------------------------------------------

required_h3 = {
    "fold",
    "split",
    "category",
    "garment_identity",
}

if not required_h3.issubset(h3.columns):
    raise RuntimeError(
        "H3 missing required columns"
    )

test_assign = (
    h3.loc[
        h3["split"].astype(str).str.lower() == "test",
        [
            "category",
            "garment_identity",
            "fold",
        ],
    ]
    .copy()
)

assert_unique(
    test_assign,
    ["category", "garment_identity"],
    "H3 TEST ASSIGNMENTS",
)

test_assign = test_assign.rename(
    columns={
        "fold": "canonical_test_fold"
    }
)

n_identities = len(test_assign)

if n_identities != 230:
    raise RuntimeError(
        f"Expected 230 canonical identities, got {n_identities}"
    )

print(
    "Canonical H3 test-fold map: "
    f"{n_identities} identities PASS"
)


base = base.merge(
    test_assign,
    on=[
        "category",
        "garment_identity",
    ],
    how="left",
    validate="many_to_one",
)

if base["canonical_test_fold"].isna().any():
    raise RuntimeError(
        "Some sketches lack canonical test-fold assignment"
    )


# ------------------------------------------------------------
# 8. Audit corrected historical fold map
#    DO NOT silently substitute it.
# ------------------------------------------------------------

fc = foldcorr.rename(
    columns={
        "corrected_garment_id":
            "garment_identity",
        "fold_id":
            "corrected_fold_id",
    }
).copy()

assert_unique(
    fc,
    ["category", "garment_identity"],
    "CORRECTED FOLD MAP",
)

fold_audit = test_assign.merge(
    fc[
        [
            "category",
            "garment_identity",
            "corrected_fold_id",
            "n_sketches",
        ]
    ],
    on=[
        "category",
        "garment_identity",
    ],
    how="outer",
    indicator=True,
    validate="one_to_one",
)

fold_audit["fold_equal"] = (
    pd.to_numeric(
        fold_audit["canonical_test_fold"],
        errors="coerce",
    )
    ==
    pd.to_numeric(
        fold_audit["corrected_fold_id"],
        errors="coerce",
    )
)

print("\nFOLD MAP AUDIT")
print(
    "rows                 :",
    len(fold_audit)
)
print(
    "both sources         :",
    int((fold_audit["_merge"] == "both").sum())
)
print(
    "H3 only              :",
    int((fold_audit["_merge"] == "left_only").sum())
)
print(
    "corrected-map only   :",
    int((fold_audit["_merge"] == "right_only").sum())
)
print(
    "matching fold values :",
    int(
        (
            (fold_audit["_merge"] == "both")
            &
            fold_audit["fold_equal"]
        ).sum()
    )
)


# ------------------------------------------------------------
# 9. Final integrity
# ------------------------------------------------------------

if len(base) != 2300:
    raise RuntimeError(
        f"Final table has {len(base)} rows"
    )

assert_unique(base, KEY, "FINAL BASE")

required_numeric = [
    "crop_low_1_4_fraction",
    "crop_high_25_36_fraction",
    "raw_crop_band_l1",
    "crop_q99_radius_to_grid",
    "s09_outlier_score",
    "raw_to_text_band_l1_change",
]

for col in required_numeric:
    x = pd.to_numeric(
        base[col],
        errors="coerce",
    )

    n_bad = int((~np.isfinite(x)).sum())

    print(
        f"{col:32s} finite failures = {n_bad}"
    )

    if n_bad:
        raise RuntimeError(
            f"{col}: nonfinite values"
        )


# ------------------------------------------------------------
# 10. Write PRE-SELECTION artifacts
# ------------------------------------------------------------

base_out = (
    OUT /
    "P2_R0_05K0_historical_selection_base.csv"
)

fold_out = (
    OUT /
    "P2_R0_05K0_fold_map_audit.csv"
)

meta_out = (
    OUT /
    "P2_R0_05K0_gateB_metadata.json"
)

base.to_csv(
    base_out,
    index=False,
)

fold_audit.to_csv(
    fold_out,
    index=False,
)


metadata = {
    "version": VERSION,
    "n_sketches": len(base),
    "n_identities": n_identities,
    "join_key": KEY,

    "scientific_field_map": {
        "identity":
            "I2.garment_identity",

        "crop_low_fraction":
            "I2.crop_low_1_4_fraction",

        "crop_high_fraction":
            "I2.crop_high_25_36_fraction",

        "raw_crop_band_l1":
            "I2.band_fraction_l1_change",

        "crop_q99_over_Rgrid":
            "J.crop_q99_radius_to_grid",

        "s09_outlier_score":
            "I8.fragile_max_radius_to_grid "
            "- I8.robust_q99_radius_to_grid",

        "raw_text_band_l1":
            "I6.raw_to_text_band_l1_change",

        "text_positive":
            "membership in I4 frozen text-positive candidate table",

        "canonical_test_fold":
            "H3 rows where split == test",
    },

    "source_sha256": {
        k: v[1]
        for k, v in SOURCES.items()
    },

    "05k_spectral_outcomes_opened": False,
    "sentinel_selection_performed": False,
}


meta_out.write_text(
    json.dumps(
        metadata,
        indent=2,
        sort_keys=True,
    ) + "\n",
    encoding="utf-8",
)


print("\nOUTPUT SHA256")
for p in [
    base_out,
    fold_out,
    meta_out,
]:
    print(
        p.name,
        sha256(p),
    )


print("\n" + "=" * 78)
print("GATE B COMPLETE")
print("Sentinel selection performed: NO")
print("05K spectral outcomes opened: NO")