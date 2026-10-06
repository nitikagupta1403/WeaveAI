from pathlib import Path
import hashlib
import json
import math

import numpy as np
import pandas as pd
from PIL import Image


# =============================================================================
# P2-R0-05K4-A
# FULL-POPULATION PRIMARY SUPPORT MATERIALIZATION
#
# 2300 frozen V3 images × 7 support levels = 16,100 conditions
#
# CONSTRUCTION / INTEGRITY ONLY.
#
# NO:
#   descriptor execution
#   Fourier analysis
#   trajectory analysis
#   directional testing
#   population inference
#   mechanism verdict
# =============================================================================


REPO = Path(
    "/Users/nitikagupta/Research/WeaveAI"
)

AUDITS = (
    REPO
    / "papers/Paper-II/reproducibility/audits"
)

FROZEN = (
    REPO
    / "papers/Paper-II/reproducibility/frozen"
)

OUT = (
    AUDITS
    / "05K4_A_primary_support_materialization"
)

CANVAS_ROOT = (
    OUT
    / "canvases"
)

OUT.mkdir(
    parents=True,
    exist_ok=True,
)

CANVAS_ROOT.mkdir(
    parents=True,
    exist_ok=True,
)


# =============================================================================
# Frozen V3 population
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

EXPECTED_V3_SHA = (
    "19ab60c21c71de7918472142c36174ded9f8fae888eeb3320983ca2cc66a545e"
)


# =============================================================================
# Frozen 05K1 construction rule
# =============================================================================

RULE_DIR = (
    FROZEN
    / "05K1_Construction_Rule_v1_0"
)

RULE_JSON = (
    RULE_DIR
    / "P2_R0_05K1_support_only_construction_rule_v1_0.json"
)

EXPECTED_RULE_SHA = (
    "a2f38fbed518d7e9371bb5f517b39aaf6d97c34be4ea476ebc455a64d5a6101f"
)


SUPPORT_LEVELS = np.asarray(
    [
        1.00,
        1.10,
        1.25,
        1.50,
        2.00,
        2.50,
        3.00,
    ],
    dtype=float,
)


EXPECTED_IMAGES = 2300
EXPECTED_CONDITIONS = 16100


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


def sha256_array(arr):
    arr = np.ascontiguousarray(
        arr
    )

    h = hashlib.sha256()

    h.update(
        str(arr.dtype).encode(
            "utf-8"
        )
    )

    h.update(
        np.asarray(
            arr.shape,
            dtype=np.int64,
        ).tobytes()
    )

    h.update(
        arr.tobytes(
            order="C"
        )
    )

    return h.hexdigest()


def load_gray_uint8(path):
    with Image.open(path) as im:
        arr = np.asarray(
            im.convert("L"),
            dtype=np.uint8,
        )

    require(
        arr.ndim == 2,
        f"Expected grayscale image: {path}",
    )

    return arr


def save_gray_uint8(path, arr):
    require(
        arr.dtype == np.uint8,
        "Canvas must be uint8",
    )

    require(
        arr.ndim == 2,
        "Canvas must be 2-D",
    )

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    Image.fromarray(
        arr,
        mode="L",
    ).save(
        path,
        format="PNG",
    )


def support_tag(s):
    return (
        f"s{s:.2f}"
        .replace(".", "p")
    )


def resolve_v3_image_path(row):

    candidates = []

    if "output_relative_path" in row.index:

        p = str(
            row[
                "output_relative_path"
            ]
        ).strip()

        if p:
            candidates.append(
                V3_ROOT / p
            )


    p = str(
        row[
            "relative_path"
        ]
    ).strip()

    if p:
        candidates.append(
            V3_ROOT / p
        )


    for candidate in candidates:

        if candidate.is_file():
            return candidate


    raise RuntimeError(
        "Unable to resolve frozen V3 image: "
        f"row_index={row['row_index']}, "
        f"relative_path={row['relative_path']}"
    )


# =============================================================================
# Header
# =============================================================================

print("=" * 112)
print(
    "P2-R0-05K4-A — "
    "FULL-POPULATION PRIMARY SUPPORT MATERIALIZATION"
)
print("=" * 112)

print(
    "Source images expected :",
    EXPECTED_IMAGES,
)

print(
    "Support levels         :",
    len(
        SUPPORT_LEVELS
    ),
)

print(
    "Conditions expected    :",
    EXPECTED_CONDITIONS,
)

print()

print("Descriptor execution   : NO")
print("Spectral analysis      : NO")
print("Hypothesis testing     : NO")
print("Population inference   : NO")
print()


# =============================================================================
# 1. Verify frozen provenance
# =============================================================================

require(
    V3_MANIFEST.is_file(),
    f"Missing V3 manifest: {V3_MANIFEST}",
)

v3_sha = sha256_file(
    V3_MANIFEST
)

print(
    "V3 manifest SHA:",
    v3_sha,
    "PASS"
    if v3_sha == EXPECTED_V3_SHA
    else "FAIL",
)

require(
    v3_sha == EXPECTED_V3_SHA,
    "V3 manifest SHA mismatch",
)


require(
    RULE_JSON.is_file(),
    f"Missing frozen construction rule: {RULE_JSON}",
)

rule_sha = sha256_file(
    RULE_JSON
)

print(
    "05K1 construction-rule SHA:",
    rule_sha,
    "PASS"
    if rule_sha == EXPECTED_RULE_SHA
    else "FAIL",
)

require(
    rule_sha == EXPECTED_RULE_SHA,
    "05K1 construction-rule SHA mismatch",
)


rule = json.loads(
    RULE_JSON.read_text(
        encoding="utf-8"
    )
)


# =============================================================================
# 2. Load complete V3 population
# =============================================================================

v3 = pd.read_csv(
    V3_MANIFEST,
    keep_default_na=False,
)


require(
    len(v3) == EXPECTED_IMAGES,
    (
        f"Expected {EXPECTED_IMAGES} V3 rows; "
        f"got {len(v3)}"
    ),
)


required = {
    "row_index",
    "relative_path",
    "border_median",
}


require(
    required.issubset(
        set(v3.columns)
    ),
    (
        "V3 manifest missing required columns: "
        f"{required - set(v3.columns)}"
    ),
)


v3[
    "row_index"
] = v3[
    "row_index"
].astype(int)


require(
    v3[
        "row_index"
    ].nunique()
    == EXPECTED_IMAGES,
    "V3 row_index is not unique",
)


require(
    v3[
        "relative_path"
    ].nunique()
    == EXPECTED_IMAGES,
    "V3 relative_path is not unique",
)


v3["category"] = (
    v3[
        "relative_path"
    ]
    .map(
        lambda p:
            Path(
                str(p)
            ).parts[
                0
            ]
    )
)


require(
    v3[
        "category"
    ].nunique()
    == 23,
    "Expected 23 categories",
)


v3 = (
    v3.sort_values(
        "row_index",
        kind="mergesort",
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
            EXPECTED_IMAGES
        ),
    ),
    "V3 row_index is not exact 0..2299",
)


# =============================================================================
# 3. Materialize 16,100 support conditions
# =============================================================================

records = []


for i, row in v3.iterrows():

    if (
        i == 0
        or (i + 1) % 100 == 0
        or (i + 1) == EXPECTED_IMAGES
    ):

        print(
            f"Processing source image "
            f"{i + 1}/{EXPECTED_IMAGES}"
        )


    source_path = resolve_v3_image_path(
        row
    )


    source = load_gray_uint8(
        source_path
    )


    H, W = source.shape


    border_median = float(
        row[
            "border_median"
        ]
    )


    require(
        np.isfinite(
            border_median
        ),
        (
            "Non-finite border_median: "
            f"{row['relative_path']}"
        ),
    )


    # -------------------------------------------------------------------------
    # Frozen padding-fill rule
    # -------------------------------------------------------------------------

    b_i = int(
        np.rint(
            255.0
            * border_median
        )
    )


    require(
        0 <= b_i <= 255,
        (
            "Padding value outside uint8 range: "
            f"{row['relative_path']} -> {b_i}"
        ),
    )


    # Historical H1 foreground diagnostic = gray < 250.
    require(
        b_i >= 250,
        (
            "Padding would create foreground under "
            "<250 mask: "
            f"{row['relative_path']} -> {b_i}"
        ),
    )


    source_array_sha = sha256_array(
        source
    )


    for s in SUPPORT_LEVELS:

        s = float(
            s
        )


        # ---------------------------------------------------------------------
        # Frozen support-dimension rule
        # ---------------------------------------------------------------------

        pad_y = int(
            math.ceil(
                ((s - 1.0) * H)
                / 2.0
            )
        )

        pad_x = int(
            math.ceil(
                ((s - 1.0) * W)
                / 2.0
            )
        )


        Hs = (
            H
            + 2 * pad_y
        )

        Ws = (
            W
            + 2 * pad_x
        )


        require(
            Hs
            ==
            H
            + 2
            * int(
                math.ceil(
                    ((s - 1.0) * H)
                    / 2.0
                )
            ),
            "Height rule mismatch",
        )


        require(
            Ws
            ==
            W
            + 2
            * int(
                math.ceil(
                    ((s - 1.0) * W)
                    / 2.0
                )
            ),
            "Width rule mismatch",
        )


        # ---------------------------------------------------------------------
        # Construct canvas
        # ---------------------------------------------------------------------

        canvas = np.full(
            (
                Hs,
                Ws,
            ),
            fill_value=b_i,
            dtype=np.uint8,
        )


        y0 = pad_y
        x0 = pad_x

        y1 = y0 + H
        x1 = x0 + W


        canvas[
            y0:y1,
            x0:x1,
        ] = source


        # ---------------------------------------------------------------------
        # Exact source-patch integrity
        # ---------------------------------------------------------------------

        embedded = canvas[
            y0:y1,
            x0:x1,
        ]


        patch_exact = bool(
            np.array_equal(
                embedded,
                source,
            )
        )


        require(
            patch_exact,
            (
                "Embedded patch changed: "
                f"{row['relative_path']} s={s}"
            ),
        )


        embedded_sha = sha256_array(
            embedded
        )


        require(
            embedded_sha
            == source_array_sha,
            (
                "Embedded patch SHA mismatch: "
                f"{row['relative_path']} s={s}"
            ),
        )


        # ---------------------------------------------------------------------
        # No clipping
        # ---------------------------------------------------------------------

        no_clipping = bool(
            y0 >= 0
            and x0 >= 0
            and y1 <= Hs
            and x1 <= Ws
            and embedded.shape
            == source.shape
        )


        require(
            no_clipping,
            (
                "Clipping detected: "
                f"{row['relative_path']} s={s}"
            ),
        )


        # ---------------------------------------------------------------------
        # Padding exactness
        # ---------------------------------------------------------------------

        pad_mask = np.ones(
            canvas.shape,
            dtype=bool,
        )


        pad_mask[
            y0:y1,
            x0:x1,
        ] = False


        padding_pixels = canvas[
            pad_mask
        ]


        if padding_pixels.size == 0:

            padding_exact = True

        else:

            padding_exact = bool(
                np.all(
                    padding_pixels
                    == b_i
                )
            )


        require(
            padding_exact,
            (
                "Padding mismatch: "
                f"{row['relative_path']} s={s}"
            ),
        )


        # ---------------------------------------------------------------------
        # s=1 exact source replay
        # ---------------------------------------------------------------------

        s1_exact = None


        if s == 1.0:

            s1_exact = bool(
                canvas.shape
                == source.shape
                and
                np.array_equal(
                    canvas,
                    source,
                )
            )


            require(
                s1_exact,
                (
                    "s=1 is not exact source replay: "
                    f"{row['relative_path']}"
                ),
            )


        # ---------------------------------------------------------------------
        # Deterministic output path
        # ---------------------------------------------------------------------

        tag = support_tag(
            s
        )


        out_relative = (
            Path(tag)
            / str(
                row[
                    "category"
                ]
            )
            / (
                f"{int(row['row_index']):04d}.png"
            )
        )


        out_path = (
            CANVAS_ROOT
            / out_relative
        )


        save_gray_uint8(
            out_path,
            canvas,
        )


        # ---------------------------------------------------------------------
        # Save/reload exactness
        # ---------------------------------------------------------------------

        reloaded = load_gray_uint8(
            out_path
        )


        reload_exact = bool(
            np.array_equal(
                reloaded,
                canvas,
            )
        )


        require(
            reload_exact,
            (
                "Save/reload mismatch: "
                f"{out_relative}"
            ),
        )


        records.append({
            "row_index":
                int(
                    row[
                        "row_index"
                    ]
                ),

            "category":
                str(
                    row[
                        "category"
                    ]
                ),

            "relative_path":
                str(
                    row[
                        "relative_path"
                    ]
                ),

            "source_path":
                str(
                    source_path
                ),

            "support_factor":
                s,

            "source_height":
                int(
                    H
                ),

            "source_width":
                int(
                    W
                ),

            "pad_top":
                int(
                    pad_y
                ),

            "pad_bottom":
                int(
                    pad_y
                ),

            "pad_left":
                int(
                    pad_x
                ),

            "pad_right":
                int(
                    pad_x
                ),

            "output_height":
                int(
                    Hs
                ),

            "output_width":
                int(
                    Ws
                ),

            "border_median":
                border_median,

            "padding_value_uint8":
                int(
                    b_i
                ),

            "source_array_sha256":
                source_array_sha,

            "embedded_patch_array_sha256":
                embedded_sha,

            "patch_array_equal":
                patch_exact,

            "padding_exact":
                padding_exact,

            "no_clipping":
                no_clipping,

            "s1_exact_source_replay":
                (
                    ""
                    if s1_exact is None
                    else bool(
                        s1_exact
                    )
                ),

            "save_reload_exact":
                reload_exact,

            "output_relative_path":
                str(
                    out_relative
                ),

            "output_file_sha256":
                sha256_file(
                    out_path
                ),
        })


# =============================================================================
# 4. Primary integrity table
# =============================================================================

integrity = pd.DataFrame(
    records
)


require(
    len(integrity)
    == EXPECTED_CONDITIONS,
    (
        f"Expected {EXPECTED_CONDITIONS} conditions; "
        f"got {len(integrity)}"
    ),
)


require(
    integrity[
        [
            "row_index",
            "support_factor",
        ]
    ]
    .drop_duplicates()
    .shape[
        0
    ]
    == EXPECTED_CONDITIONS,
    "row_index × support_factor is not unique",
)


require(
    integrity[
        "row_index"
    ].nunique()
    == EXPECTED_IMAGES,
    "Primary integrity table does not contain 2300 images",
)


require(
    bool(
        integrity[
            "patch_array_equal"
        ].all()
    ),
    "At least one embedded patch changed",
)


require(
    bool(
        (
            integrity[
                "source_array_sha256"
            ]
            ==
            integrity[
                "embedded_patch_array_sha256"
            ]
        ).all()
    ),
    "At least one embedded-patch SHA differs",
)


require(
    bool(
        integrity[
            "padding_exact"
        ].all()
    ),
    "At least one padding region differs",
)


require(
    bool(
        integrity[
            "no_clipping"
        ].all()
    ),
    "At least one condition clips source pixels",
)


require(
    bool(
        integrity[
            "save_reload_exact"
        ].all()
    ),
    "At least one save/reload differs",
)


# =============================================================================
# 5. s=1 exact replay
# =============================================================================

s1 = integrity.loc[
    np.isclose(
        integrity[
            "support_factor"
        ].to_numpy(
            dtype=float
        ),
        1.0,
        atol=0.0,
        rtol=0.0,
    )
].copy()


require(
    len(s1)
    == EXPECTED_IMAGES,
    "Expected 2300 s=1 rows",
)


require(
    bool(
        s1[
            "s1_exact_source_replay"
        ]
        .astype(bool)
        .all()
    ),
    "Not all s=1 conditions exactly replay source images",
)


# =============================================================================
# 6. Sort and save
# =============================================================================

integrity = (
    integrity.sort_values(
        [
            "row_index",
            "support_factor",
        ],
        kind="mergesort",
    )
    .reset_index(
        drop=True
    )
)


INTEGRITY_CSV = (
    OUT
    / "P2_R0_05K4_A_integrity_16100.csv"
)


integrity.to_csv(
    INTEGRITY_CSV,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


# =============================================================================
# 7. Support-level summary
# =============================================================================

summary_rows = []


for s, group in integrity.groupby(
    "support_factor",
    sort=True,
):

    summary_rows.append({
        "support_factor":
            float(
                s
            ),

        "conditions":
            int(
                len(
                    group
                )
            ),

        "unique_images":
            int(
                group[
                    "row_index"
                ].nunique()
            ),

        "categories":
            int(
                group[
                    "category"
                ].nunique()
            ),

        "all_patch_exact":
            bool(
                group[
                    "patch_array_equal"
                ].all()
            ),

        "all_padding_exact":
            bool(
                group[
                    "padding_exact"
                ].all()
            ),

        "all_no_clipping":
            bool(
                group[
                    "no_clipping"
                ].all()
            ),

        "all_save_reload_exact":
            bool(
                group[
                    "save_reload_exact"
                ].all()
            ),

        "min_padding_value":
            int(
                group[
                    "padding_value_uint8"
                ].min()
            ),

        "max_padding_value":
            int(
                group[
                    "padding_value_uint8"
                ].max()
            ),

        "min_output_height":
            int(
                group[
                    "output_height"
                ].min()
            ),

        "max_output_height":
            int(
                group[
                    "output_height"
                ].max()
            ),

        "min_output_width":
            int(
                group[
                    "output_width"
                ].min()
            ),

        "max_output_width":
            int(
                group[
                    "output_width"
                ].max()
            ),
    })


summary = pd.DataFrame(
    summary_rows
)


SUMMARY_CSV = (
    OUT
    / "P2_R0_05K4_A_support_level_summary.csv"
)


summary.to_csv(
    SUMMARY_CSV,
    index=False,
    lineterminator="\n",
)


# =============================================================================
# 8. Category counts
# =============================================================================

category_counts = (
    v3.groupby(
        "category",
        sort=True,
    )
    .size()
    .rename(
        "source_images"
    )
    .reset_index()
)


CATEGORY_CSV = (
    OUT
    / "P2_R0_05K4_A_category_source_counts.csv"
)


category_counts.to_csv(
    CATEGORY_CSV,
    index=False,
    lineterminator="\n",
)


# =============================================================================
# 9. Report
# =============================================================================

REPORT_JSON = (
    OUT
    / "P2_R0_05K4_A_report.json"
)


report = {
    "stage":
        "P2_R0_05K4_A_PRIMARY_SUPPORT_MATERIALIZATION",

    "status":
        "PASS_CONSTRUCTION_AND_INTEGRITY_ONLY",

    "source_images":
        EXPECTED_IMAGES,

    "categories":
        23,

    "support_levels":
        SUPPORT_LEVELS.tolist(),

    "conditions_materialized":
        EXPECTED_CONDITIONS,

    "v3_manifest": {
        "path":
            str(
                V3_MANIFEST
            ),

        "sha256":
            v3_sha,
    },

    "construction_rule": {
        "path":
            str(
                RULE_JSON
            ),

        "sha256":
            rule_sha,

        "dimension_rule":
            (
                "Hs = H + 2*ceil(((s-1)*H)/2); "
                "Ws = W + 2*ceil(((s-1)*W)/2)"
            ),

        "padding_rule":
            "b_i = int(rint(255 * border_median_i))",
    },

    "integrity": {
        "all_source_patches_array_equal":
            bool(
                integrity[
                    "patch_array_equal"
                ].all()
            ),

        "all_embedded_patch_array_sha_match":
            bool(
                (
                    integrity[
                        "source_array_sha256"
                    ]
                    ==
                    integrity[
                        "embedded_patch_array_sha256"
                    ]
                ).all()
            ),

        "all_padding_exact":
            bool(
                integrity[
                    "padding_exact"
                ].all()
            ),

        "all_no_clipping":
            bool(
                integrity[
                    "no_clipping"
                ].all()
            ),

        "all_saved_reloaded_exact":
            bool(
                integrity[
                    "save_reload_exact"
                ].all()
            ),

        "s1_exact_replay":
            bool(
                s1[
                    "s1_exact_source_replay"
                ]
                .astype(bool)
                .all()
            ),

        "minimum_padding_value":
            int(
                integrity[
                    "padding_value_uint8"
                ].min()
            ),

        "maximum_padding_value":
            int(
                integrity[
                    "padding_value_uint8"
                ].max()
            ),
    },

    "analysis_boundary": {
        "descriptor_execution":
            False,

        "spectral_analysis":
            False,

        "trajectory_analysis":
            False,

        "directional_hypotheses":
            False,

        "materiality_threshold":
            False,

        "population_inference":
            False,

        "mechanism_verdict":
            False,
    },
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
# 10. Checksums
# =============================================================================

OUTPUTS = [
    INTEGRITY_CSV,
    SUMMARY_CSV,
    CATEGORY_CSV,
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
# 11. Final output
# =============================================================================

print()
print("=" * 112)
print(
    "P2-R0-05K4-A — "
    "PRIMARY SUPPORT MATERIALIZATION: PASS"
)
print("=" * 112)

print(
    "Source images:",
    EXPECTED_IMAGES,
)

print(
    "Support levels:",
    len(
        SUPPORT_LEVELS
    ),
)

print(
    "Conditions:",
    len(
        integrity
    ),
)

print()

print(
    "Patch array exact:",
    f"{int(integrity['patch_array_equal'].sum())}"
    f"/{len(integrity)}",
)

print(
    "Patch SHA exact:",
    f"{int((integrity['source_array_sha256'] == integrity['embedded_patch_array_sha256']).sum())}"
    f"/{len(integrity)}",
)

print(
    "Padding exact:",
    f"{int(integrity['padding_exact'].sum())}"
    f"/{len(integrity)}",
)

print(
    "No clipping:",
    f"{int(integrity['no_clipping'].sum())}"
    f"/{len(integrity)}",
)

print(
    "Save/reload exact:",
    f"{int(integrity['save_reload_exact'].sum())}"
    f"/{len(integrity)}",
)

print(
    "s=1 exact replay:",
    f"{int(s1['s1_exact_source_replay'].astype(bool).sum())}"
    f"/{len(s1)}",
)

print(
    "Padding-value range:",
    int(
        integrity[
            "padding_value_uint8"
        ].min()
    ),
    "..",
    int(
        integrity[
            "padding_value_uint8"
        ].max()
    ),
)

print()
print("SUPPORT-LEVEL SUMMARY")

print(
    summary.to_string(
        index=False
    )
)

print()
print("CATEGORY SOURCE COUNTS")

print(
    category_counts.to_string(
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
print("Descriptor execution    : NO")
print("Spectral analysis       : NO")
print("Trajectory analysis     : NO")
print("Hypothesis verdict      : NO")
print("Population inference    : NO")
print("Mechanism verdict       : NO")

print()
print("=" * 112)
print(
    "STOP — FREEZE 05K4-A BEFORE PRIMARY DESCRIPTOR EXECUTION"
)
print("=" * 112)