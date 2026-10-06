from pathlib import Path
import pandas as pd
import numpy as np
import hashlib
import json
import math


# ============================================================================
# P2-R0-05K0 — FINAL GATE B
# Sentinel-selection historical base + frozen rules v1.0a
#
# IMPORTANT
# ---------
# - Historical/pre-05K inputs only.
# - NO 05K support-sweep spectral outcomes are read.
# - NO sentinel is selected.
# - NO S01-S10 winner/candidate ID is printed.
# - Experiment-06 corrected fold map is intentionally NOT used.
# ============================================================================


VERSION = "P2-R0-05K0-SENTINEL-v1.0a"

OUTDIR = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05k_support_only_intervention/"
    "P2_R0_05K0_gateB_final_v1_0a"
)

OUTDIR.mkdir(parents=True, exist_ok=True)


# ============================================================================
# 1. Frozen historical sources
# ============================================================================

V3 = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05f_crop_vs_resampling/"
    "V3_CROP_ONLY/materialized_manifest.csv"
)

I2 = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I2_per_image_band_fraction_change.csv"
)

I8 = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I6_highfreq_text_tightsupport/"
    "P2_R0_05I8_robust_support_metric_audit/"
    "P2_R0_05I8_per_image_robust_support_metrics.csv"
)

J = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I6_highfreq_text_tightsupport/"
    "P2_R0_05J_population_support_spectral_audit_v2/"
    "P2_R0_05J_per_image_population_metrics.csv"
)

H3 = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05h_intrinsic_coordinate/"
    "P2_R0_05H3_identity_assignments.csv"
)

I4 = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I4_text_positive_control/"
    "P2_R0_05I4_text_positive_candidates.csv"
)

I6 = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I6_highfreq_text_tightsupport/"
    "P2_R0_05I6_per_image_metrics.csv"
)


EXPECTED_SHA = {
    "V3": "19ab60c21c71de7918472142c36174ded9f8fae888eeb3320983ca2cc66a545e",
    "I2": "a9a096b4aafe89be79b5d3c35fd3e4dc4e6de046c30326f108d0cbe3601c39e2",
    "I8": "4ac2cc2d5393f9e55effca81358ed147d772d581e630dbe4312ef0490f92e0a0",
    "J": "f667d8850c43001f1ee251bc2c14f18765a5289c0ebf8e8be42b972e03f6995a",
    "H3": "d67ad6daf2926727fa823651a63e4954a424ce20a8f83bf5c1632bef3a3b532c",
    "I4": "a99081a2d8428ce923ac6131b253ac5c1a5cc4d403cbe1242ef5d3b76c571cc3",
    "I6": "7987569d0fd08361212d4cad32cf511799ac7538dcb54dfc5dc4104ee933ecfa",
}

SOURCES = {
    "V3": V3,
    "I2": I2,
    "I8": I8,
    "J": J,
    "H3": H3,
    "I4": I4,
    "I6": I6,
}


# ============================================================================
# 2. Helpers
# ============================================================================

def sha256_file(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_json_bytes(obj):
    return (
        json.dumps(
            obj,
            sort_keys=True,
            ensure_ascii=False,
            allow_nan=False,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def write_canonical_json(path, obj):
    Path(path).write_bytes(canonical_json_bytes(obj))


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def assert_unique(df, cols, label):
    require(
        not df.duplicated(cols).any(),
        f"{label}: duplicate key on {cols}",
    )


def finite_or_fail(series, label):
    x = pd.to_numeric(series, errors="coerce")
    bad = int((~np.isfinite(x)).sum())
    require(
        bad == 0,
        f"{label}: {bad} non-finite values",
    )
    return x.astype(float)


def normalize_bool(series):
    if pd.api.types.is_bool_dtype(series):
        return series.astype(bool)

    s = (
        series.astype(str)
        .str.strip()
        .str.lower()
    )

    mapping = {
        "true": True,
        "false": False,
        "1": True,
        "0": False,
        "yes": True,
        "no": False,
    }

    bad = sorted(set(s) - set(mapping))
    require(
        not bad,
        f"Unrecognized boolean values: {bad}",
    )

    return s.map(mapping).astype(bool)


def percentile_midrank(series):
    """
    Frozen v1.0a convention:

        R = average empirical rank, ascending
        P = (R - 0.5) / N

    Population = full valid 2300-sketch historical population.
    """
    x = finite_or_fail(series, series.name)

    n = len(x)

    require(
        n == 2300,
        f"{series.name}: percentile population must be 2300, got {n}",
    )

    r = x.rank(
        method="average",
        ascending=True,
    )

    p = (r - 0.5) / n

    require(
        ((p > 0) & (p < 1)).all(),
        f"{series.name}: percentile outside (0,1)",
    )

    return p.astype(float)


# ============================================================================
# 3. Start
# ============================================================================

print("=" * 78)
print("P2-R0-05K0 — FINAL GATE B v1.0a")
print("=" * 78)
print("Sentinel selection performed: NO")
print("05K spectral trajectories opened: NO")
print("Experiment-06 corrected fold map used: NO")
print()


# ============================================================================
# 4. Verify source hashes
# ============================================================================

observed_source_sha = {}

for name, path in SOURCES.items():

    require(
        path.exists(),
        f"Missing source: {path}",
    )

    # Defensive source-path check.
    # H3 contains "05h", etc.; only actual 05K inputs are forbidden.
    lower = str(path).lower()

    require(
        "05k" not in lower,
        f"Forbidden 05K source path: {path}",
    )

    got = sha256_file(path)
    observed_source_sha[name] = got

    ok = got == EXPECTED_SHA[name]

    print(
        f"{name:4s}",
        "SHA PASS" if ok else "SHA FAIL",
        got,
    )

    require(
        ok,
        f"{name}: SHA mismatch",
    )


# ============================================================================
# 5. Load
# ============================================================================

v3 = pd.read_csv(V3)
i2 = pd.read_csv(I2)
i8 = pd.read_csv(I8)
j = pd.read_csv(J)
h3 = pd.read_csv(H3)
i4 = pd.read_csv(I4)
i6 = pd.read_csv(I6)


V3_KEY = [
    "row_index",
    "relative_path",
]

KEY = [
    "row_index",
    "relative_path",
    "category",
]

IDENTITY_KEY = [
    "category",
    "garment_identity",
]


# ============================================================================
# 6. Basic historical-universe validation
# ============================================================================

for label, df in [
    ("V3", v3),
    ("I2", i2),
    ("I8", i8),
    ("J", j),
    ("I6", i6),
]:
    require(
        len(df) == 2300,
        f"{label}: expected 2300 rows; found {len(df)}",
    )


assert_unique(v3, V3_KEY, "V3")
assert_unique(i2, KEY, "I2")
assert_unique(i8, KEY, "I8")
assert_unique(j, KEY, "J")
assert_unique(i6, KEY, "I6")


# V3 has no category column.
v3_i2 = v3[V3_KEY].merge(
    i2[V3_KEY],
    on=V3_KEY,
    how="outer",
    indicator=True,
)

require(
    (v3_i2["_merge"] == "both").all(),
    "V3 ↔ I2 provenance universe mismatch",
)


for label, df in [
    ("I8", i8),
    ("J", j),
    ("I6", i6),
]:
    audit = i2[KEY].merge(
        df[KEY],
        on=KEY,
        how="outer",
        indicator=True,
    )

    require(
        (audit["_merge"] == "both").all(),
        f"I2 ↔ {label} analytical-key mismatch",
    )


require(
    i2["category"].nunique() == 23,
    "I2 category count != 23",
)

i2_ids = (
    i2[IDENTITY_KEY]
    .drop_duplicates()
)

require(
    len(i2_ids) == 230,
    f"I2 identity count != 230; found {len(i2_ids)}",
)


# ============================================================================
# 7. I2 ↔ J canonical identity agreement
# ============================================================================

identity_check = i2[
    KEY + ["garment_identity"]
].merge(
    j[
        KEY + ["garment_identity"]
    ],
    on=KEY,
    how="inner",
    validate="one_to_one",
    suffixes=("_i2", "_j"),
)

require(
    len(identity_check) == 2300,
    f"I2/J identity merge expected 2300 rows; found {len(identity_check)}",
)


# ============================================================================
# 8. Validate H3 as canonical Paper-II fold source
# ============================================================================

require(
    len(h3) == 1150,
    f"H3 expected 1150 rows; found {len(h3)}",
)

require(
    set(h3["fold"]) == {0, 1, 2, 3, 4},
    "H3 fold set is not exactly 0..4",
)

split_norm = (
    h3["split"]
    .astype(str)
    .str.strip()
    .str.lower()
)

require(
    set(split_norm) == {"train", "test"},
    "H3 split set is not exactly train/test",
)

h3_work = h3.copy()
h3_work["_split_norm"] = split_norm


h3_structure = (
    h3_work
    .groupby(
        ["category", "garment_identity"],
        sort=False,
    )
    .agg(
        n_rows=("fold", "size"),
        n_folds=("fold", "nunique"),
        n_test=(
            "_split_norm",
            lambda s: int((s == "test").sum()),
        ),
        n_train=(
            "_split_norm",
            lambda s: int((s == "train").sum()),
        ),
    )
    .reset_index()
)

require(
    len(h3_structure) == 230,
    "H3 identity count != 230",
)

require(
    (
        (h3_structure["n_rows"] == 5)
        & (h3_structure["n_folds"] == 5)
        & (h3_structure["n_test"] == 1)
        & (h3_structure["n_train"] == 4)
    ).all(),
    "H3 identity train/test structure failure",
)


h3_ids = (
    h3_work[
        ["category", "garment_identity"]
    ]
    .drop_duplicates()
)

id_audit = i2_ids.merge(
    h3_ids,
    on=IDENTITY_KEY,
    how="outer",
    indicator=True,
)

require(
    (id_audit["_merge"] == "both").all(),
    "I2/H3 identity universes differ",
)


h3_test = (
    h3_work.loc[
        h3_work["_split_norm"] == "test",
        [
            "category",
            "garment_identity",
            "fold",
        ],
    ]
    .drop_duplicates()
    .rename(
        columns={
            "fold": "canonical_test_fold",
        }
    )
)

require(
    len(h3_test) == 230,
    "H3 canonical test map != 230 identities",
)

assert_unique(
    h3_test,
    IDENTITY_KEY,
    "H3 canonical test map",
)


fold_counts = (
    h3_test
    .groupby("canonical_test_fold")
    .size()
)

require(
    len(fold_counts) == 5
    and (fold_counts == 46).all(),
    "H3 expected exactly 46 identities/fold",
)


cat_fold_counts = (
    h3_test
    .groupby(
        ["category", "canonical_test_fold"]
    )
    .size()
)

require(
    len(cat_fold_counts) == 23 * 5
    and (cat_fold_counts == 2).all(),
    "H3 expected exactly 2 identities/category/fold",
)


# ============================================================================
# 9. Validate S08 frozen text-positive pool
# ============================================================================

require(
    len(i4) == 582,
    f"I4 expected 582 rows; found {len(i4)}",
)

assert_unique(
    i4,
    V3_KEY,
    "I4",
)

cohort = (
    i4["selection_cohort"]
    .astype(str)
    .str.strip()
    .str.lower()
)

require(
    (cohort == "mandatory").all(),
    "I4 contains non-mandatory rows",
)

approved = normalize_bool(
    i4["text_blanking_approved"]
)

require(
    approved.all(),
    "I4 contains unapproved rows",
)

require(
    (pd.to_numeric(
        i4["n_text_boxes"],
        errors="coerce",
    ) > 0).all(),
    "I4 contains row with n_text_boxes <= 0",
)


v3_text = (
    v3.loc[
        pd.to_numeric(
            v3["n_text_boxes"],
            errors="coerce",
        ) > 0,
        V3_KEY,
    ]
    .drop_duplicates()
)

require(
    len(v3_text) == 582,
    f"V3 text-positive count != 582; found {len(v3_text)}",
)


text_membership_audit = v3_text.merge(
    i4[V3_KEY],
    on=V3_KEY,
    how="outer",
    indicator=True,
)

require(
    (text_membership_audit["_merge"] == "both").all(),
    "I4 != exact V3 n_text_boxes>0 membership",
)


# ============================================================================
# 10. Build historical selection base
# ============================================================================

base = i2[
    [
        "row_index",
        "relative_path",
        "category",
        "garment_identity",

        "crop_low_1_4_fraction",
        "crop_high_25_36_fraction",
        "band_fraction_l1_change",
    ]
].copy()


base = base.rename(
    columns={
        "garment_identity": "identity",
        "band_fraction_l1_change": "raw_crop_band_l1",
    }
)


# CROP q99/Rgrid from 05J.
j_q99 = j[
    KEY + [
        "crop_q99_radius_to_grid",
    ]
].copy()

base = base.merge(
    j_q99,
    on=KEY,
    how="left",
    validate="one_to_one",
)


# S09 historical speck/outlier-support metric:
#
#   (r_max - r_q99) / R_grid
#
# = fragile_max_radius_to_grid - robust_q99_radius_to_grid
#
i8_support = i8[
    KEY + [
        "fragile_max_radius_to_grid",
        "robust_q99_radius_to_grid",
    ]
].copy()

i8_support["s09_outlier_score"] = (
    pd.to_numeric(
        i8_support["fragile_max_radius_to_grid"],
        errors="coerce",
    )
    -
    pd.to_numeric(
        i8_support["robust_q99_radius_to_grid"],
        errors="coerce",
    )
)

base = base.merge(
    i8_support[
        KEY + [
            "s09_outlier_score",
        ]
    ],
    on=KEY,
    how="left",
    validate="one_to_one",
)


# H3 canonical test fold.
h3_for_base = h3_test.rename(
    columns={
        "garment_identity": "identity",
    }
)

base = base.merge(
    h3_for_base,
    on=[
        "category",
        "identity",
    ],
    how="left",
    validate="many_to_one",
)


# I4 text-positive membership.
i4_membership = (
    i4[V3_KEY]
    .drop_duplicates()
    .assign(
        s08_text_positive_eligible=True,
    )
)

base = base.merge(
    i4_membership,
    on=V3_KEY,
    how="left",
    validate="one_to_one",
)

base["s08_text_positive_eligible"] = (
    base["s08_text_positive_eligible"]
    .fillna(False)
    .astype(bool)
)


# I6 historical RAW -> TEXT_BLANKED L1.
i6_text = i6[
    KEY + [
        "raw_to_text_band_l1_change",
    ]
].copy()

base = base.merge(
    i6_text,
    on=KEY,
    how="left",
    validate="one_to_one",
)


# ============================================================================
# 11. Validate all role-source metrics
# ============================================================================

metric_cols = [
    "crop_low_1_4_fraction",
    "crop_high_25_36_fraction",
    "raw_crop_band_l1",
    "crop_q99_radius_to_grid",
    "s09_outlier_score",
]

for c in metric_cols:
    base[c] = finite_or_fail(
        base[c],
        c,
    )


# RAW->TEXT metric is required for all I4-eligible rows.
eligible_text_metric = pd.to_numeric(
    base.loc[
        base["s08_text_positive_eligible"],
        "raw_to_text_band_l1_change",
    ],
    errors="coerce",
)

require(
    np.isfinite(eligible_text_metric).all(),
    "S08 eligible pool contains missing/non-finite RAW->TEXT L1",
)

require(
    int(base["s08_text_positive_eligible"].sum()) == 582,
    "S08 eligible count != 582",
)


require(
    base["canonical_test_fold"].notna().all(),
    "Missing H3 canonical test fold",
)

base["canonical_test_fold"] = (
    base["canonical_test_fold"]
    .astype(int)
)


# ============================================================================
# 12. Frozen v1.0a percentile coordinates
#
# IMPORTANT:
# These are deterministic historical coordinates only.
# They DO NOT select S01 or S10.
# ============================================================================

base["P_crop_low"] = percentile_midrank(
    base["crop_low_1_4_fraction"]
)

base["P_crop_high"] = percentile_midrank(
    base["crop_high_25_36_fraction"]
)

base["P_crop_q99_grid"] = percentile_midrank(
    base["crop_q99_radius_to_grid"]
)

base["P_raw_crop_l1"] = percentile_midrank(
    base["raw_crop_band_l1"]
)


base["population_centre_distance"] = np.sqrt(
    (base["P_crop_low"] - 0.5) ** 2
    + (base["P_crop_high"] - 0.5) ** 2
    + (base["P_crop_q99_grid"] - 0.5) ** 2
    + (base["P_raw_crop_l1"] - 0.5) ** 2
)


finite_or_fail(
    base["population_centre_distance"],
    "population_centre_distance",
)


# ============================================================================
# 13. Stable tie key v1.0a
# ============================================================================

require(
    base["row_index"].between(0, 2299).all(),
    "row_index outside 0..2299",
)

base["stable_tie_key"] = (
    base["category"].astype(str)
    + "|"
    + base["identity"].astype(str)
    + "|"
    + base["relative_path"].astype(str)
    + "|"
    + base["row_index"].astype(int).map(
        lambda x: f"{x:06d}"
    )
)

require(
    base["stable_tie_key"].is_unique,
    "stable_tie_key is not unique",
)


# ============================================================================
# 14. Final base invariants
# ============================================================================

require(
    len(base) == 2300,
    "Final selection base != 2300 rows",
)

assert_unique(
    base,
    [
        "row_index",
        "relative_path",
        "category",
    ],
    "Final selection base",
)

require(
    base["identity"].nunique() == 230,
    "Final base identity count != 230",
)

require(
    base["category"].nunique() == 23,
    "Final base category count != 23",
)

require(
    int((base["canonical_test_fold"] == 3).sum()) > 0,
    "No Fold-3 sketches in final base",
)

fold3_identity_count = (
    base.loc[
        base["canonical_test_fold"] == 3,
        ["category", "identity"],
    ]
    .drop_duplicates()
    .shape[0]
)

require(
    fold3_identity_count == 46,
    f"Fold-3 identity count != 46; found {fold3_identity_count}",
)


# ============================================================================
# 15. Encode frozen sentinel rules v1.0a
#
# NO candidate sorting or selection is performed here.
# ============================================================================

rules = {
    "protocol_version": VERSION,

    "status": "FROZEN_BEFORE_SENTINEL_SELECTION",

    "historical_population": {
        "n_sketches": 2300,
        "n_categories": 23,
        "n_identities": 230,
        "selection_universe": (
            "Frozen V3 CROP_ONLY / Paper-II historical sketch universe"
        ),
    },

    "canonical_identity_source": {
        "source": "I2",
        "field": "garment_identity",
    },

    "canonical_fold_source": {
        "source": "H3",
        "definition": (
            "For each (category, garment_identity), canonical test fold "
            "is the unique H3 row with split == 'test'."
        ),
        "validated_identities": 230,
        "identities_per_fold": 46,
        "identities_per_category_per_fold": 2,
    },

    "explicitly_excluded_fold_source": {
        "source": (
            "Paper-I Experiment-06 corrected identity/fold map"
        ),
        "reason": (
            "Distinct corrective identity namespace; invalid for direct "
            "cross-namespace S01 fold assignment."
        ),
    },

    "percentile_convention": {
        "version": "v1.0a",
        "population_n": 2300,
        "ranking": "average empirical rank",
        "direction": "ascending",
        "formula": "P = (R - 0.5) / N",
        "ties": "average rank",
        "coordinates": [
            "crop_low_1_4_fraction",
            "crop_high_25_36_fraction",
            "crop_q99_radius_to_grid",
            "raw_crop_band_l1",
        ],
        "centre": [0.5, 0.5, 0.5, 0.5],
        "distance": (
            "sqrt(sum_j((P_ij - 0.5)^2))"
        ),
        "s01_rule": (
            "Compute percentile coordinates over full valid 2300-sketch "
            "population first; then restrict candidates to identities whose "
            "canonical H3 test fold is 3."
        ),
        "s10_rule": (
            "Minimum predefined four-coordinate population-centre distance."
        ),
    },

    "stable_tie_key": {
        "formula": (
            "category|identity|relative_path|row_index:06d"
        ),
        "row_index_width": 6,
        "ordering": "lexicographic ascending",
    },

    "global_selection_order": [
        "S01",
        "S08",
        "S02",
        "S03",
        "S04",
        "S05",
        "S06",
        "S07",
        "S09",
        "S10",
    ],

    "global_collision_rule": {
        "identity_constraint": (
            "No two sentinels may come from the same garment identity."
        ),
        "procedure": (
            "For each role in frozen selection order, sort by that role's "
            "primary metric and stable tie key; scan until the first candidate "
            "whose garment identity has not already been used."
        ),
        "category_diversity_constraint": False,
        "manual_replacement_allowed": False,
        "skips_logged": True,
    },

    "roles": {
        "S01": {
            "name": "Fold-3 representative",
            "eligible_pool": (
                "Sketches whose canonical H3 identity test fold == 3"
            ),
            "metric": "population_centre_distance",
            "direction": "ascending",
        },

        "S02": {
            "name": "LOW extreme",
            "metric": "crop_low_1_4_fraction",
            "direction": "descending",
        },

        "S03": {
            "name": "HIGH extreme",
            "metric": "crop_high_25_36_fraction",
            "direction": "descending",
        },

        "S04": {
            "name": "Large robust support",
            "metric": "crop_q99_radius_to_grid",
            "direction": "descending",
        },

        "S05": {
            "name": "Small robust support",
            "metric": "crop_q99_radius_to_grid",
            "direction": "ascending",
        },

        "S06": {
            "name": "Strong redistribution",
            "metric": "raw_crop_band_l1",
            "direction": "descending",
        },

        "S07": {
            "name": "Stable redistribution control",
            "metric": "raw_crop_band_l1",
            "direction": "ascending",
        },

        "S08": {
            "name": "Text-sensitive case",
            "eligible_pool": (
                "Exact frozen 582-row I4 text-positive pool"
            ),
            "metric": "raw_to_text_band_l1_change",
            "direction": "descending",
            "historical_pool_validation": {
                "n_rows": 582,
                "selection_cohort": "mandatory",
                "text_blanking_approved": True,
                "n_text_boxes": ">0",
                "equals_V3_n_text_boxes_gt_0": True,
            },
        },

        "S09": {
            "name": "Speck/outlier-sensitive support",
            "metric": "s09_outlier_score",
            "formula": (
                "fragile_max_radius_to_grid "
                "- robust_q99_radius_to_grid"
            ),
            "equivalent_formula": (
                "(r_max - r_q99) / R_grid"
            ),
            "direction": "descending",
        },

        "S10": {
            "name": "Typical control",
            "metric": "population_centre_distance",
            "direction": "ascending",
        },
    },

    "validity_rule": (
        "A sketch is valid only if it passed already-existing historical QA "
        "required to compute the role metric and all required values are finite. "
        "No new eligibility threshold may be invented during selection."
    ),

    "anti_peeking_rule": {
        "new_05k_raster_spectral_trajectories_allowed": False,
        "support_levels_1p10_to_3p00_may_be_opened": False,
        "sentinel_selection_before_05k_outcomes": True,
    },

    "selection_performed_by_this_gate": False,
}


# ============================================================================
# 16. Output paths
# ============================================================================

BASE_OUT = (
    OUTDIR
    / "P2_R0_05K0_historical_selection_base_v1_0a.csv"
)

RULES_OUT = (
    OUTDIR
    / "P2_R0_05K0_sentinel_selection_rules_v1_0a.json"
)

META_OUT = (
    OUTDIR
    / "P2_R0_05K0_gateB_final_metadata_v1_0a.json"
)


# ============================================================================
# 17. Write deterministic base
# ============================================================================

base = base.sort_values(
    "row_index",
    kind="stable",
).reset_index(drop=True)


OUTPUT_COLUMNS = [
    "row_index",
    "relative_path",
    "category",
    "identity",

    "canonical_test_fold",

    "crop_low_1_4_fraction",
    "crop_high_25_36_fraction",
    "crop_q99_radius_to_grid",
    "raw_crop_band_l1",

    "s09_outlier_score",

    "s08_text_positive_eligible",
    "raw_to_text_band_l1_change",

    "P_crop_low",
    "P_crop_high",
    "P_crop_q99_grid",
    "P_raw_crop_l1",

    "population_centre_distance",

    "stable_tie_key",
]


require(
    set(OUTPUT_COLUMNS).issubset(base.columns),
    "Missing final output column",
)


base[
    OUTPUT_COLUMNS
].to_csv(
    BASE_OUT,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


# ============================================================================
# 18. Write frozen rules
# ============================================================================

write_canonical_json(
    RULES_OUT,
    rules,
)


base_sha = sha256_file(BASE_OUT)
rules_sha = sha256_file(RULES_OUT)


# ============================================================================
# 19. Metadata
# ============================================================================

metadata = {
    "protocol_version": VERSION,

    "gate": "FINAL_GATE_B",

    "status": "PASS",

    "sentinel_selection_performed": False,

    "sentinel_ids_opened": False,

    "new_05k_spectral_outcomes_opened": False,

    "experiment06_cross_namespace_fold_comparison": {
        "performed": False,
        "status": "RETIRED",
        "reason": (
            "Paper-I Experiment-06 corrected IDs and Paper-II H3 IDs "
            "are distinct identity namespaces."
        ),
    },

    "source_sha256": {
        name: observed_source_sha[name]
        for name in sorted(observed_source_sha)
    },

    "validated_counts": {
        "sketches": 2300,
        "categories": 23,
        "identities": 230,
        "h3_rows": 1150,
        "h3_test_identities_per_fold": 46,
        "h3_test_identities_per_category_per_fold": 2,
        "fold3_eligible_identities_for_s01": 46,
        "s08_text_positive_sketches": 582,
    },

    "frozen_definitions": {
        "percentile_convention": (
            "P=(average_rank-0.5)/2300"
        ),
        "stable_tie_key": (
            "category|identity|relative_path|row_index:06d"
        ),
        "canonical_fold_source": "H3",
        "s08_pool": "exact frozen I4 582-row pool",
    },

    "outputs": {
        "historical_selection_base": {
            "filename": BASE_OUT.name,
            "sha256": base_sha,
        },
        "sentinel_selection_rules": {
            "filename": RULES_OUT.name,
            "sha256": rules_sha,
        },
    },
}


write_canonical_json(
    META_OUT,
    metadata,
)

meta_sha = sha256_file(META_OUT)


# ============================================================================
# 20. Final report — deliberately no candidate IDs
# ============================================================================

print()
print("=" * 78)
print("FINAL GATE B VALIDATION")
print("=" * 78)

print("Historical sketches                 :", len(base))
print("Categories                          :", base["category"].nunique())
print("Canonical identities                :", base["identity"].nunique())
print("H3 Fold-3 eligible identities       :", fold3_identity_count)
print(
    "S08 text-positive eligible sketches:",
    int(base["s08_text_positive_eligible"].sum()),
)

print()
print("Percentile convention               : P=(R-0.5)/N")
print("Percentile population N             : 2300")
print("Tie method                          : average rank")
print(
    "Stable tie key                     : "
    "category|identity|relative_path|row_index:06d"
)

print()
print("Experiment-06 fold comparison       : RETIRED / NOT USED")
print("Canonical S01 fold source           : H3")
print("Sentinel selection performed        : NO")
print("Sentinel IDs opened                 : NO")
print("05K spectral trajectories opened    : NO")


print()
print("=" * 78)
print("OUTPUT SHA256")
print("=" * 78)

print(
    BASE_OUT.name,
    base_sha,
)

print(
    RULES_OUT.name,
    rules_sha,
)

print(
    META_OUT.name,
    meta_sha,
)


print()
print("=" * 78)
print("FINAL GATE B v1.0a: PASS")
print("NEXT AUTHORIZED STEP: deterministic S01-S10 selection")
print("CURRENT STEP selected no sentinel.")