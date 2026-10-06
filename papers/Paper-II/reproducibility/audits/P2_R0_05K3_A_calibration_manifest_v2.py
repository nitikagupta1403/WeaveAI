from pathlib import Path
import hashlib
import json

import numpy as np
import pandas as pd


# =============================================================================
# P2-R0-05K3-A
# DETERMINISTIC 230-CASE CALIBRATION MANIFEST
#
# PURPOSE
#   Select exactly one sketch per frozen garment identity for the intermediate
#   230-case support-sweep calibration layer.
#
# SELECTION RULE
#   1. Bind frozen V3 provenance to frozen historical identity assignments.
#   2. Sort by:
#        category | garment_identity | relative_path | row_index
#   3. Within each garment identity choose the first relative_path.
#
# PROHIBITED
#   - spectral values in selection
#   - support metrics in selection
#   - fold difficulty in selection
#   - visual inspection in selection
#   - outcome-adaptive substitution
#   - descriptor execution
# =============================================================================


REPO = Path(
    "/Users/nitikagupta/Research/WeaveAI"
)

AUDITS = (
    REPO
    / "papers/Paper-II/reproducibility/audits"
)

OUT = (
    AUDITS
    / "05K3_A_calibration_manifest"
)

OUT.mkdir(
    parents=True,
    exist_ok=True,
)


# =============================================================================
# Frozen source artifacts
# =============================================================================

V3_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05f_crop_vs_resampling/"
    "V3_CROP_ONLY"
)

V3_MANIFEST = (
    V3_ROOT
    / "materialized_manifest.csv"
)

I2_PER_IMAGE = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I2_per_image_band_fraction_change.csv"
)


EXPECTED_SHA = {
    "V3":
        "19ab60c21c71de7918472142c36174ded9f8fae888eeb3320983ca2cc66a545e",

    "I2":
        "a9a096b4aafe89be79b5d3c35fd3e4dc4e6de046c30326f108d0cbe3601c39e2",
}


EXPECTED_ROWS = 2300
EXPECTED_IDENTITIES = 230
EXPECTED_CATEGORIES = 23
EXPECTED_IDENTITY_SIZE_DISTRIBUTION = {
    9: 3,
    10: 224,
    11: 3,
}
EXPECTED_IDENTITIES_PER_CATEGORY = 10


# =============================================================================
# Helpers
# =============================================================================

def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha256_file(path):
    h = hashlib.sha256()

    with Path(path).open("rb") as f:
        for chunk in iter(
            lambda: f.read(1024 * 1024),
            b"",
        ):
            h.update(chunk)

    return h.hexdigest()


# =============================================================================
# Header
# =============================================================================

print("=" * 100)
print(
    "P2-R0-05K3-A — "
    "DETERMINISTIC 230-CASE CALIBRATION MANIFEST"
)
print("=" * 100)

print("Descriptor execution       : NO")
print("Support canvases generated : NO")
print("Spectral metrics inspected : NO")
print("Visual selection            : NO")
print()


# =============================================================================
# 1. Verify immutable input hashes
# =============================================================================

for label, path in [
    ("V3", V3_MANIFEST),
    ("I2", I2_PER_IMAGE),
]:

    require(
        path.is_file(),
        f"Missing source: {path}",
    )

    observed = sha256_file(
        path
    )

    expected = EXPECTED_SHA[
        label
    ]

    print(
        f"{label} SHA:",
        observed,
        "PASS" if observed == expected else "FAIL",
    )

    require(
        observed == expected,
        f"{label} SHA mismatch",
    )


# =============================================================================
# 2. Load V3 universe
# =============================================================================

v3 = pd.read_csv(
    V3_MANIFEST,
    keep_default_na=False,
)


require(
    len(v3) == EXPECTED_ROWS,
    f"V3 rows != {EXPECTED_ROWS}",
)


required_v3 = {
    "row_index",
    "relative_path",
    "output_relative_path",
}


require(
    required_v3.issubset(
        set(v3.columns)
    ),
    (
        "V3 manifest missing columns: "
        f"{required_v3 - set(v3.columns)}"
    ),
)


v3["row_index"] = (
    v3[
        "row_index"
    ].astype(int)
)


v3["relative_path"] = (
    v3[
        "relative_path"
    ].astype(str)
)


v3["category"] = (
    v3[
        "relative_path"
    ]
    .map(
        lambda x:
            Path(x).parts[0]
    )
)


v3 = (
    v3.sort_values(
        "row_index"
    )
    .reset_index(
        drop=True
    )
)


require(
    np.array_equal(
        v3[
            "row_index"
        ].to_numpy(),
        np.arange(
            EXPECTED_ROWS
        ),
    ),
    "V3 row_index is not exact 0..2299",
)


require(
    v3[
        "relative_path"
    ].nunique()
    == EXPECTED_ROWS,
    "V3 relative_path is not unique",
)


# =============================================================================
# 3. Load historical I2 identity universe
# =============================================================================

i2 = pd.read_csv(
    I2_PER_IMAGE,
    keep_default_na=False,
)


require(
    len(i2) == EXPECTED_ROWS,
    f"I2 rows != {EXPECTED_ROWS}",
)


print()
print("I2 columns:")
print(i2.columns.tolist())
print()


# We require the historical identity assignment rather than reconstructing it.
identity_candidates = [
    "garment_identity",
    "identity",
    "identity_id",
]


identity_col = None


for c in identity_candidates:

    if c in i2.columns:
        identity_col = c
        break


require(
    identity_col is not None,
    (
        "No historical identity column found. "
        f"Looked for {identity_candidates}"
    ),
)


require(
    "relative_path"
    in i2.columns,
    "I2 lacks relative_path",
)


i2["relative_path"] = (
    i2[
        "relative_path"
    ].astype(str)
)


if "row_index" in i2.columns:

    i2[
        "row_index"
    ] = i2[
        "row_index"
    ].astype(int)


# =============================================================================
# 4. Stable provenance binding
#
# Prefer row_index + relative_path if both exist.
# Never use fold_id as a join key.
# =============================================================================

if "row_index" in i2.columns:

    binding = v3.merge(
        i2[
            [
                "row_index",
                "relative_path",
                identity_col,
            ]
        ],
        on=[
            "row_index",
            "relative_path",
        ],
        how="inner",
        validate="one_to_one",
    )

else:

    binding = v3.merge(
        i2[
            [
                "relative_path",
                identity_col,
            ]
        ],
        on="relative_path",
        how="inner",
        validate="one_to_one",
    )


require(
    len(binding)
    == EXPECTED_ROWS,
    (
        "V3/I2 binding did not recover "
        f"all {EXPECTED_ROWS} rows; "
        f"got {len(binding)}"
    ),
)


binding = binding.rename(
    columns={
        identity_col:
            "garment_identity"
    }
)


binding[
    "garment_identity"
] = binding[
    "garment_identity"
].astype(str)


# =============================================================================
# 5. Structural validation of frozen identity universe
# =============================================================================

n_identities = int(
    binding[
        "garment_identity"
    ].nunique()
)


n_categories = int(
    binding[
        "category"
    ].nunique()
)


require(
    n_identities
    == EXPECTED_IDENTITIES,
    (
        f"Expected {EXPECTED_IDENTITIES} identities; "
        f"got {n_identities}"
    ),
)


require(
    n_categories
    == EXPECTED_CATEGORIES,
    (
        f"Expected {EXPECTED_CATEGORIES} categories; "
        f"got {n_categories}"
    ),
)


rows_per_identity = (
    binding.groupby(
        "garment_identity"
    )
    .size()
)


identity_size_distribution = (
    rows_per_identity
    .value_counts()
    .sort_index()
    .to_dict()
)

identity_size_distribution = {
    int(k): int(v)
    for k, v
    in identity_size_distribution.items()
}

require(
    identity_size_distribution
    == EXPECTED_IDENTITY_SIZE_DISTRIBUTION,
    (
        "Unexpected frozen identity-size distribution: "
        f"{identity_size_distribution}"
    ),
)


# One garment identity must belong to exactly one category.
id_category_counts = (
    binding.groupby(
        "garment_identity"
    )[
        "category"
    ]
    .nunique()
)


require(
    id_category_counts.max()
    == 1,
    "At least one identity spans multiple categories",
)


identities_per_category = (
    binding[
        [
            "category",
            "garment_identity",
        ]
    ]
    .drop_duplicates()
    .groupby(
        "category"
    )
    .size()
)


require(
    identities_per_category.min()
    == EXPECTED_IDENTITIES_PER_CATEGORY
    and
    identities_per_category.max()
    == EXPECTED_IDENTITIES_PER_CATEGORY,
    (
        "Expected exactly "
        f"{EXPECTED_IDENTITIES_PER_CATEGORY} "
        "identities/category"
    ),
)


print("=" * 100)
print("FROZEN IDENTITY UNIVERSE")
print("=" * 100)

print(
    "Rows:",
    len(binding),
)

print(
    "Identities:",
    n_identities,
)

print(
    "Categories:",
    n_categories,
)

print(
    "Rows / identity:",
    f"{rows_per_identity.min()}.."
    f"{rows_per_identity.max()}",
)

print(
    "Identity-size distribution:",
    identity_size_distribution,
)

print(
    "Identities / category:",
    f"{identities_per_category.min()}.."
    f"{identities_per_category.max()}",
)

print()


# =============================================================================
# 6. Deterministic calibration selection
#
# Rule frozen here:
# sort category | identity | relative_path | row_index
# choose first path within identity.
# =============================================================================

ordered = (
    binding.sort_values(
        [
            "category",
            "garment_identity",
            "relative_path",
            "row_index",
        ],
        kind="mergesort",
    )
    .reset_index(
        drop=True
    )
)


selected = (
    ordered.groupby(
        "garment_identity",
        sort=False,
        as_index=False,
    )
    .first()
)


# Re-sort output canonically.
selected = (
    selected.sort_values(
        [
            "category",
            "garment_identity",
            "relative_path",
            "row_index",
        ],
        kind="mergesort",
    )
    .reset_index(
        drop=True
    )
)


selected.insert(
    0,
    "calibration_index",
    np.arange(
        len(selected),
        dtype=int,
    ),
)


require(
    len(selected)
    == EXPECTED_IDENTITIES,
    (
        "Calibration selection did not "
        f"produce {EXPECTED_IDENTITIES} rows"
    ),
)


require(
    selected[
        "garment_identity"
    ].nunique()
    == EXPECTED_IDENTITIES,
    "Selected identities are not unique",
)


require(
    selected[
        "relative_path"
    ].nunique()
    == EXPECTED_IDENTITIES,
    "Selected paths are not unique",
)


selected_counts = (
    selected.groupby(
        "category"
    )
    .size()
)


require(
    selected_counts.min()
    == EXPECTED_IDENTITIES_PER_CATEGORY
    and
    selected_counts.max()
    == EXPECTED_IDENTITIES_PER_CATEGORY,
    (
        "Calibration manifest does not have "
        "exactly 10 identities/category"
    ),
)


# =============================================================================
# 7. Independently verify each selected path is lexicographic minimum
# =============================================================================

lex_check_rows = []


for identity, group in (
    binding.groupby(
        "garment_identity",
        sort=False,
    )
):

    group = group.sort_values(
        [
            "relative_path",
            "row_index",
        ],
        kind="mergesort",
    )


    expected_row = group.iloc[
        0
    ]


    observed_row = selected.loc[
        selected[
            "garment_identity"
        ]
        == identity
    ].iloc[
        0
    ]


    path_equal = (
        str(
            observed_row[
                "relative_path"
            ]
        )
        ==
        str(
            expected_row[
                "relative_path"
            ]
        )
    )


    row_equal = (
        int(
            observed_row[
                "row_index"
            ]
        )
        ==
        int(
            expected_row[
                "row_index"
            ]
        )
    )


    require(
        path_equal
        and row_equal,
        (
            "Lexicographic selection verification "
            f"failed for identity {identity}"
        ),
    )


    lex_check_rows.append({
        "garment_identity":
            identity,

        "selected_relative_path":
            str(
                observed_row[
                    "relative_path"
                ]
            ),

        "selected_row_index":
            int(
                observed_row[
                    "row_index"
                ]
            ),

        "lexicographic_minimum_verified":
            True,
    })


lex_check = pd.DataFrame(
    lex_check_rows
)


# =============================================================================
# 8. Restrict manifest to stable provenance fields
#
# Preserve useful V3 integrity columns when available.
# =============================================================================

preferred_columns = [
    "calibration_index",
    "row_index",
    "category",
    "garment_identity",
    "relative_path",
    "output_relative_path",

    # Preserve these only if V3 actually contains them.
    "source_sha256",
    "output_pixel_sha256",
    "output_sha256",
    "crop_left",
    "crop_top",
    "crop_right",
    "crop_bottom",
    "crop_width",
    "crop_height",
]


manifest_columns = [
    c
    for c in preferred_columns
    if c in selected.columns
]


manifest = selected[
    manifest_columns
].copy()


# =============================================================================
# 9. Save
# =============================================================================

MANIFEST_CSV = (
    OUT
    / "P2_R0_05K3_A_calibration_manifest_230.csv"
)

LEX_CHECK_CSV = (
    OUT
    / "P2_R0_05K3_A_lexicographic_selection_check_230.csv"
)

REPORT_JSON = (
    OUT
    / "P2_R0_05K3_A_report.json"
)


manifest.to_csv(
    MANIFEST_CSV,
    index=False,
    lineterminator="\n",
)


lex_check.to_csv(
    LEX_CHECK_CSV,
    index=False,
    lineterminator="\n",
)


# =============================================================================
# 10. Report
# =============================================================================

report = {
    "stage":
        "P2_R0_05K3_A_DETERMINISTIC_CALIBRATION_MANIFEST",

    "status":
        "PASS",

    "source_population_rows":
        EXPECTED_ROWS,

    "categories":
        EXPECTED_CATEGORIES,

    "identities":
        EXPECTED_IDENTITIES,

    "identity_size_distribution":
        identity_size_distribution,

    "identity_size_min":
        int(rows_per_identity.min()),

    "identity_size_max":
        int(rows_per_identity.max()),

    "selected_rows":
        EXPECTED_IDENTITIES,

    "selected_rows_per_category":
        EXPECTED_IDENTITIES_PER_CATEGORY,

    "selection_rule":
        (
            "Within the frozen 2300-row V3/I2 identity universe, "
            "sort by category | garment_identity | relative_path | "
            "row_index using stable mergesort, then select the first "
            "row within each garment_identity."
        ),

    "identity_source":
        {
            "artifact":
                str(
                    I2_PER_IMAGE
                ),

            "sha256":
                EXPECTED_SHA[
                    "I2"
                ],

            "column_used":
                identity_col,
        },

    "v3_source":
        {
            "artifact":
                str(
                    V3_MANIFEST
                ),

            "sha256":
                EXPECTED_SHA[
                    "V3"
                ],
        },

    "selection_inputs_used": [
        "category",
        "garment_identity",
        "relative_path",
        "row_index",
    ],

    "selection_inputs_explicitly_not_used": [
        "spectral band fractions",
        "RAW-to-CROP spectral changes",
        "support geometry metrics",
        "fold difficulty",
        "retrieval performance",
        "visual judgment",
        "05K2 sentinel outcomes",
    ],

    "descriptor_execution":
        False,

    "support_canvas_generation":
        False,

    "population_inference":
        False,
}


REPORT_JSON.write_text(
    json.dumps(
        report,
        indent=2,
        sort_keys=True,
    )
    + "\n",
    encoding="utf-8",
)


# =============================================================================
# 11. Checksums
# =============================================================================

OUTPUTS = [
    MANIFEST_CSV,
    LEX_CHECK_CSV,
    REPORT_JSON,
]


SUMS = (
    OUT
    / "SHA256SUMS.txt"
)


with SUMS.open(
    "w",
    encoding="utf-8",
) as f:

    for path in OUTPUTS:

        f.write(
            f"{sha256_file(path)}  "
            f"{path.name}\n"
        )


# =============================================================================
# 12. Final
# =============================================================================

print("=" * 100)
print("P2-R0-05K3-A — CALIBRATION MANIFEST: PASS")
print("=" * 100)

print(
    "Selected rows:",
    len(manifest),
)

print(
    "Unique identities:",
    manifest[
        "garment_identity"
    ].nunique(),
)

print(
    "Categories:",
    manifest[
        "category"
    ].nunique(),
)

print(
    "Rows/category:",
    f"{selected_counts.min()}.."
    f"{selected_counts.max()}",
)

print(
    "Lexicographic checks:",
    f"{lex_check['lexicographic_minimum_verified'].sum()}"
    f"/{len(lex_check)}",
)

print()

print(
    manifest[
        [
            "calibration_index",
            "row_index",
            "category",
            "garment_identity",
            "relative_path",
        ]
    ]
    .head(
        25
    )
    .to_string(
        index=False
    )
)

print()
print("OUTPUT HASHES")

for path in OUTPUTS:

    print(
        path.name,
        sha256_file(
            path
        ),
    )

print(
    "SHA256SUMS.txt",
    sha256_file(
        SUMS
    ),
)

print()
print("Descriptor execution       : NO")
print("Support canvases generated : NO")
print("Spectral metrics inspected : NO")
print("Visual substitution         : NO")

print()
print("=" * 100)
print(
    "STOP — FREEZE 05K3-A BEFORE MATERIALIZING "
    "ANY 230-CASE SUPPORT CANVAS"
)
print("=" * 100)