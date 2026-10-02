from pathlib import Path
import pandas as pd
import numpy as np
import hashlib
import json


# ============================================================================
# P2-R0-05K0 — DETERMINISTIC SENTINEL SELECTION v1.0a
#
# FIRST AUTHORIZED S01-S10 ID REVEAL
#
# Reads:
#   frozen Gate-B historical base
#   frozen Gate-B rules
#   frozen bookkeeping addendum
#
# Does NOT read:
#   any 05K support-sweep/intervention trajectory
#
# Selection order:
#   S01 -> S08 -> S02 -> S03 -> S04 ->
#   S05 -> S06 -> S07 -> S09 -> S10
#
# Global constraint:
#   no two sentinels from the same garment identity
# ============================================================================


REPO = Path("/Users/nitikagupta/Research/WeaveAI")

GATEB = (
    REPO
    / "papers/Paper-II/reproducibility/frozen/05K0_GateB_v1_0a"
)

OUTDIR = (
    REPO
    / "papers/Paper-II/reproducibility/frozen/"
      "05K0_Sentinel_Manifest_v1_0a"
)

OUTDIR.mkdir(parents=True, exist_ok=True)


BASE = (
    GATEB
    / "P2_R0_05K0_historical_selection_base_v1_0a.csv"
)

RULES = (
    GATEB
    / "P2_R0_05K0_sentinel_selection_rules_v1_0a.json"
)

GATEB_META = (
    GATEB
    / "P2_R0_05K0_gateB_final_metadata_v1_0a.json"
)

ADDENDUM = (
    GATEB
    / "P2_R0_05K0_manifest_bookkeeping_addendum_v1_0a.json"
)


EXPECTED_SHA = {
    BASE.name:
        "491f72796a2d0ce1794d88df7c9e1958dda27199069f87c3c0aea43ed36b017a",

    RULES.name:
        "f957f2afd81071374ec1eb1c3602e3feaa64093fa87c36bfe9dde59e6905a445",

    GATEB_META.name:
        "94ccb1e171d28cb66df29cac1b067c07bed17d419d467d00d2308028a6277e64",

    ADDENDUM.name:
        "84e42e67351f4a14a7e43991e404f6c4cb16af9888f4efff7b11241fd0d097ce",
}


VERSION = "P2-R0-05K0-SENTINEL-SELECTION-v1.0a"


SELECTION_ORDER = [
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
]


ROLE_SPEC = {

    "S01": {
        "name": "Fold-3 representative",
        "metric": "population_centre_distance",
        "ascending": True,
        "eligibility": "fold3",
    },

    "S02": {
        "name": "LOW extreme",
        "metric": "crop_low_1_4_fraction",
        "ascending": False,
        "eligibility": "all",
    },

    "S03": {
        "name": "HIGH extreme",
        "metric": "crop_high_25_36_fraction",
        "ascending": False,
        "eligibility": "all",
    },

    "S04": {
        "name": "Large robust support",
        "metric": "crop_q99_radius_to_grid",
        "ascending": False,
        "eligibility": "all",
    },

    "S05": {
        "name": "Small robust support",
        "metric": "crop_q99_radius_to_grid",
        "ascending": True,
        "eligibility": "all",
    },

    "S06": {
        "name": "Strong redistribution",
        "metric": "raw_crop_band_l1",
        "ascending": False,
        "eligibility": "all",
    },

    "S07": {
        "name": "Stable redistribution control",
        "metric": "raw_crop_band_l1",
        "ascending": True,
        "eligibility": "all",
    },

    "S08": {
        "name": "Text-sensitive case",
        "metric": "raw_to_text_band_l1_change",
        "ascending": False,
        "eligibility": "text_positive",
    },

    "S09": {
        "name": "Speck/outlier-sensitive support",
        "metric": "s09_outlier_score",
        "ascending": False,
        "eligibility": "all",
    },

    "S10": {
        "name": "Typical control",
        "metric": "population_centre_distance",
        "ascending": True,
        "eligibility": "all",
    },
}


# ============================================================================
# Helpers
# ============================================================================

def require(condition, message):
    if not condition:
        raise RuntimeError(message)


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
    Path(path).write_bytes(
        canonical_json_bytes(obj)
    )


def deterministic_sort(df, metric, ascending):
    """
    Frozen ordering:
        primary role metric in specified direction
        exact metric ties -> stable_tie_key ascending
    """

    return (
        df.sort_values(
            by=[metric, "stable_tie_key"],
            ascending=[ascending, True],
            kind="mergesort",
        )
        .reset_index(drop=True)
    )


# ============================================================================
# Start
# ============================================================================

print("=" * 82)
print("P2-R0-05K0 — DETERMINISTIC SENTINEL SELECTION v1.0a")
print("=" * 82)
print("THIS RUN WILL REVEAL S01-S10 IDs: YES")
print("05K intervention trajectories opened: NO")
print()


# ============================================================================
# 1. Verify frozen Gate-B inputs
# ============================================================================

for path in [
    BASE,
    RULES,
    GATEB_META,
    ADDENDUM,
]:

    require(
        path.exists(),
        f"Missing frozen input: {path}",
    )

    got = sha256_file(path)
    expected = EXPECTED_SHA[path.name]

    print(
        f"{path.name}\n"
        f"  SHA: {got}\n"
        f"  PASS: {got == expected}"
    )

    require(
        got == expected,
        f"Frozen input SHA mismatch: {path.name}",
    )


# ============================================================================
# 2. Read frozen definitions
# ============================================================================

base = pd.read_csv(BASE)

rules = json.loads(
    RULES.read_text(encoding="utf-8")
)

addendum = json.loads(
    ADDENDUM.read_text(encoding="utf-8")
)


require(
    rules["protocol_version"]
    == "P2-R0-05K0-SENTINEL-v1.0a",
    "Unexpected Gate-B rule version",
)

require(
    addendum["applies_to_rules_sha256"]
    == EXPECTED_SHA[RULES.name],
    "Bookkeeping addendum does not bind to frozen rules SHA",
)


# ============================================================================
# 3. Base integrity
# ============================================================================

require(
    len(base) == 2300,
    f"Historical base expected 2300 rows; found {len(base)}",
)

require(
    base["row_index"].nunique() == 2300,
    "row_index is not unique",
)

require(
    base["stable_tie_key"].nunique() == 2300,
    "stable_tie_key is not unique",
)

require(
    base["identity"].nunique() == 230,
    "Expected 230 identities",
)

require(
    base["category"].nunique() == 23,
    "Expected 23 categories",
)


required_cols = {
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

    "population_centre_distance",
    "stable_tie_key",
}

missing = required_cols - set(base.columns)

require(
    not missing,
    f"Missing required base columns: {sorted(missing)}",
)


# Boolean may deserialize cleanly, but normalize defensively.
if not pd.api.types.is_bool_dtype(
    base["s08_text_positive_eligible"]
):
    base["s08_text_positive_eligible"] = (
        base["s08_text_positive_eligible"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map({
            "true": True,
            "false": False,
        })
    )

require(
    base["s08_text_positive_eligible"].notna().all(),
    "Could not normalize S08 eligibility field",
)

require(
    int(base["s08_text_positive_eligible"].sum()) == 582,
    "S08 frozen eligible pool != 582",
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
    f"S01 Fold-3 identity pool != 46; got {fold3_identity_count}",
)


# ============================================================================
# 4. Role-specific eligibility
# ============================================================================

def eligible_pool(df, rule):

    if rule == "all":
        return df.copy()

    if rule == "fold3":
        return df.loc[
            df["canonical_test_fold"] == 3
        ].copy()

    if rule == "text_positive":
        return df.loc[
            df["s08_text_positive_eligible"]
        ].copy()

    raise RuntimeError(
        f"Unknown eligibility rule: {rule}"
    )


# ============================================================================
# 5. Precompute deterministic global + eligible ranks
#
# Important:
# - rank here is ordinal after metric direction + stable tie key.
# - collisions DO NOT change these ranks.
# ============================================================================

rank_tables = {}


for role in SELECTION_ORDER:

    spec = ROLE_SPEC[role]

    metric = spec["metric"]
    ascending = spec["ascending"]

    # Global metric must be finite over all 2300 sketches,
    # consistent with frozen bookkeeping definition.
    numeric = pd.to_numeric(
        base[metric],
        errors="coerce",
    )

    bad = int((~np.isfinite(numeric)).sum())

    require(
        bad == 0,
        f"{role}: global metric {metric} has "
        f"{bad} non-finite values",
    )

    work = base.copy()
    work[metric] = numeric.astype(float)

    global_sorted = deterministic_sort(
        work,
        metric,
        ascending,
    )

    global_sorted["global_metric_rank"] = (
        np.arange(1, len(global_sorted) + 1)
    )

    global_rank = global_sorted[
        ["stable_tie_key", "global_metric_rank"]
    ]


    eligible = eligible_pool(
        work,
        spec["eligibility"],
    )

    require(
        len(eligible) > 0,
        f"{role}: empty eligible pool",
    )

    eligible_sorted = deterministic_sort(
        eligible,
        metric,
        ascending,
    )

    eligible_sorted["eligible_pool_rank"] = (
        np.arange(1, len(eligible_sorted) + 1)
    )

    eligible_sorted = eligible_sorted.merge(
        global_rank,
        on="stable_tie_key",
        how="left",
        validate="one_to_one",
    )

    require(
        eligible_sorted["global_metric_rank"]
        .notna()
        .all(),
        f"{role}: missing global rank",
    )

    rank_tables[role] = eligible_sorted


# ============================================================================
# 6. Deterministic selection
# ============================================================================

selected_rows = []
skip_rows = []

used_identity = {}
# identity -> already-selected role


for role in SELECTION_ORDER:

    spec = ROLE_SPEC[role]

    candidates = rank_tables[role]

    chosen = None


    for _, row in candidates.iterrows():

        identity = str(row["identity"])

        if identity in used_identity:

            skip_rows.append({
                "role": role,
                "role_name": spec["name"],

                "skipped_row_index":
                    int(row["row_index"]),

                "skipped_relative_path":
                    str(row["relative_path"]),

                "skipped_category":
                    str(row["category"]),

                "skipped_identity":
                    identity,

                "metric":
                    spec["metric"],

                "metric_value":
                    float(row[spec["metric"]]),

                "global_metric_rank":
                    int(row["global_metric_rank"]),

                "eligible_pool_rank":
                    int(row["eligible_pool_rank"]),

                "stable_tie_key":
                    str(row["stable_tie_key"]),

                "reason":
                    "garment_identity_already_used",

                "conflicting_selected_role":
                    used_identity[identity],
            })

            continue


        chosen = row
        break


    require(
        chosen is not None,
        f"{role}: no eligible candidate remained "
        "after identity-collision exclusions",
    )


    selected_identity = str(
        chosen["identity"]
    )

    used_identity[selected_identity] = role


    selected_rows.append({

        "role":
            role,

        "role_name":
            spec["name"],

        "row_index":
            int(chosen["row_index"]),

        "relative_path":
            str(chosen["relative_path"]),

        "category":
            str(chosen["category"]),

        "identity":
            selected_identity,

        "canonical_test_fold":
            int(chosen["canonical_test_fold"]),

        "eligibility_rule":
            spec["eligibility"],

        "metric":
            spec["metric"],

        "metric_direction":
            "ascending"
            if spec["ascending"]
            else "descending",

        "metric_value":
            float(chosen[spec["metric"]]),

        "global_metric_rank":
            int(chosen["global_metric_rank"]),

        "eligible_pool_rank":
            int(chosen["eligible_pool_rank"]),

        "stable_tie_key":
            str(chosen["stable_tie_key"]),

        "identity_collision_skips_before_selection":
            int(
                sum(
                    1
                    for x in skip_rows
                    if x["role"] == role
                )
            ),

        "selection_algorithm_version":
            VERSION,
    })


# ============================================================================
# 7. Final selection invariants
# ============================================================================

manifest = pd.DataFrame(
    selected_rows
)

skip_log = pd.DataFrame(
    skip_rows
)


require(
    len(manifest) == 10,
    f"Expected 10 sentinels; found {len(manifest)}",
)

require(
    manifest["role"].tolist()
    == SELECTION_ORDER,
    "Manifest role order differs from frozen selection order",
)

require(
    manifest["identity"].nunique() == 10,
    "Identity collision survived final selection",
)

require(
    manifest["row_index"].nunique() == 10,
    "Duplicate sketch selected",
)


# Specific eligibility checks.

s01 = manifest.loc[
    manifest["role"] == "S01"
].iloc[0]

require(
    int(s01["canonical_test_fold"]) == 3,
    "S01 is not from canonical Fold 3",
)


s08_row = manifest.loc[
    manifest["role"] == "S08"
].iloc[0]

s08_source = base.loc[
    base["row_index"]
    == int(s08_row["row_index"])
].iloc[0]

require(
    bool(
        s08_source[
            "s08_text_positive_eligible"
        ]
    ),
    "S08 is not in frozen text-positive pool",
)


# ============================================================================
# 8. Output files
# ============================================================================

MANIFEST_OUT = (
    OUTDIR
    / "P2_R0_05K0_sentinel_manifest_v1_0a.csv"
)

SKIP_OUT = (
    OUTDIR
    / "P2_R0_05K0_sentinel_selection_log_v1_0a.csv"
)

META_OUT = (
    OUTDIR
    / "P2_R0_05K0_sentinel_manifest_metadata_v1_0a.json"
)

README_OUT = (
    OUTDIR
    / "README.md"
)

SUMS_OUT = (
    OUTDIR
    / "SHA256SUMS.txt"
)


manifest.to_csv(
    MANIFEST_OUT,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


# Preserve schema even when there are zero skips.
SKIP_COLUMNS = [
    "role",
    "role_name",
    "skipped_row_index",
    "skipped_relative_path",
    "skipped_category",
    "skipped_identity",
    "metric",
    "metric_value",
    "global_metric_rank",
    "eligible_pool_rank",
    "stable_tie_key",
    "reason",
    "conflicting_selected_role",
]

if len(skip_log) == 0:
    skip_log = pd.DataFrame(
        columns=SKIP_COLUMNS
    )
else:
    skip_log = skip_log[
        SKIP_COLUMNS
    ]


skip_log.to_csv(
    SKIP_OUT,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


# ============================================================================
# 9. Metadata
# ============================================================================

manifest_sha = sha256_file(
    MANIFEST_OUT
)

skip_sha = sha256_file(
    SKIP_OUT
)


metadata = {

    "selection_algorithm_version":
        VERSION,

    "status":
        "SENTINEL_SELECTION_COMPLETE",

    "selection_order":
        SELECTION_ORDER,

    "frozen_inputs": {
        BASE.name:
            EXPECTED_SHA[BASE.name],

        RULES.name:
            EXPECTED_SHA[RULES.name],

        GATEB_META.name:
            EXPECTED_SHA[GATEB_META.name],

        ADDENDUM.name:
            EXPECTED_SHA[ADDENDUM.name],
    },

    "counts": {
        "historical_sketches": 2300,
        "categories": 23,
        "identities": 230,

        "s01_fold3_identities": 46,
        "s08_text_positive_sketches": 582,

        "sentinels_selected": 10,

        "unique_selected_identities":
            int(manifest["identity"].nunique()),

        "identity_collision_skips":
            int(len(skip_log)),
    },

    "selection_constraints": {
        "no_two_sentinels_same_identity": True,
        "manual_replacement": False,
        "category_diversity_constraint": False,
        "metric_tie_break":
            "stable_tie_key lexicographic ascending",
        "collision_skips_change_ranks": False,
    },

    "rank_bookkeeping": {
        "global_metric_rank":
            (
                "Ordinal rank over all 2300 historical "
                "sketches for role metric and direction, "
                "with stable_tie_key resolving exact ties."
            ),

        "eligible_pool_rank":
            (
                "Ordinal rank after predeclared role "
                "eligibility restriction, using identical "
                "metric/tie ordering."
            ),
    },

    "anti_peeking": {
        "05k_intervention_trajectories_opened":
            False,

        "support_levels_1p10_to_3p00_opened":
            False,

        "selection_based_only_on_frozen_historical_data":
            True,
    },

    "outputs": {
        MANIFEST_OUT.name:
            manifest_sha,

        SKIP_OUT.name:
            skip_sha,
    },
}


write_canonical_json(
    META_OUT,
    metadata,
)

meta_sha = sha256_file(
    META_OUT
)


# ============================================================================
# 10. README
# ============================================================================

readme = f"""# P2-R0-05K0 Sentinel Manifest v1.0a

Status: FROZEN SELECTION OUTPUT — pending Git commit.

Selection algorithm:
- {VERSION}

Frozen Gate-B rules SHA256:
- {EXPECTED_SHA[RULES.name]}

Frozen historical base SHA256:
- {EXPECTED_SHA[BASE.name]}

Frozen bookkeeping addendum SHA256:
- {EXPECTED_SHA[ADDENDUM.name]}

Selection order:
- S01 → S08 → S02 → S03 → S04 → S05 → S06 → S07 → S09 → S10

Global constraint:
- no two sentinels from the same garment identity

At selection time:
- historical sketches: 2300
- categories: 23
- identities: 230
- S01 Fold-3 identities: 46
- S08 text-positive sketches: 582
- sentinels selected: 10
- identity-collision skips: {len(skip_log)}
- 05K intervention trajectories opened: NO

Output hashes are recorded in SHA256SUMS.txt.
"""

README_OUT.write_text(
    readme,
    encoding="utf-8",
)


readme_sha = sha256_file(
    README_OUT
)


# ============================================================================
# 11. SHA256SUMS
# ============================================================================

sum_entries = [
    (
        manifest_sha,
        MANIFEST_OUT.name,
    ),
    (
        skip_sha,
        SKIP_OUT.name,
    ),
    (
        meta_sha,
        META_OUT.name,
    ),
    (
        readme_sha,
        README_OUT.name,
    ),
]


SUMS_OUT.write_text(
    "".join(
        f"{sha}  {name}\n"
        for sha, name in sum_entries
    ),
    encoding="utf-8",
)

sums_sha = sha256_file(
    SUMS_OUT
)


# ============================================================================
# 12. FIRST AUTHORIZED ID REVEAL
# ============================================================================

print()
print("=" * 82)
print("S01-S10 DETERMINISTIC SENTINELS")
print("=" * 82)

display_cols = [
    "role",
    "role_name",
    "row_index",
    "relative_path",
    "category",
    "identity",
    "canonical_test_fold",
    "metric",
    "metric_value",
    "global_metric_rank",
    "eligible_pool_rank",
    "identity_collision_skips_before_selection",
]

print(
    manifest[
        display_cols
    ].to_string(
        index=False
    )
)


print()
print("=" * 82)
print("COLLISION SUMMARY")
print("=" * 82)

print(
    "Total identity-collision skips:",
    len(skip_log),
)

if len(skip_log):
    print()
    print(
        skip_log[
            [
                "role",
                "eligible_pool_rank",
                "skipped_relative_path",
                "skipped_identity",
                "conflicting_selected_role",
            ]
        ].to_string(
            index=False
        )
    )
else:
    print("No identity-collision skips occurred.")


print()
print("=" * 82)
print("OUTPUT SHA256")
print("=" * 82)

print(
    MANIFEST_OUT.name,
    manifest_sha,
)

print(
    SKIP_OUT.name,
    skip_sha,
)

print(
    META_OUT.name,
    meta_sha,
)

print(
    README_OUT.name,
    readme_sha,
)

print(
    SUMS_OUT.name,
    sums_sha,
)


print()
print("=" * 82)
print("SENTINEL SELECTION: PASS")
print("Sentinels selected             : 10")
print("Unique garment identities      : 10")
print("Manual replacement             : NO")
print("05K intervention trajectories  : NOT OPENED")
print("=" * 82)