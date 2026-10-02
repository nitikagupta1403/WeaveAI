from pathlib import Path
import hashlib
import json
import math

import numpy as np
import pandas as pd
from PIL import Image


# =============================================================================
# P2-R0-05K3-B
# MATERIALIZE 230 × 7 CALIBRATION SUPPORT CANVASES
#
# PURPOSE
#   Apply the already-frozen 05K1 support-only intervention to the
#   deterministic 230-case calibration manifest.
#
# THIS STAGE DOES:
#   - exact source image loading
#   - constant symmetric canvas enlargement
#   - exact source-patch preservation
#   - padding-fill verification
#   - save/reload exactness verification
#   - s=1 exact replay verification
#
# THIS STAGE DOES NOT:
#   - run RA14
#   - run H1
#   - compute Fourier bands
#   - inspect directional hypotheses
#   - inspect monotonicity
#   - perform population inference
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
    / "05K3_B_calibration_support_materialization"
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
# Frozen sources
# =============================================================================

CALIBRATION_MANIFEST = (
    FROZEN
    / "05K3_A_Calibration_Manifest_v1_0"
    / "P2_R0_05K3_A_calibration_manifest_230.csv"
)

EXPECTED_CALIBRATION_SHA = (
    "6cbbcb8a91390c906d9d255e0d0aed953d891fcfd70ca3833fa4f6ca065522f1"
)


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


# Frozen construction-rule artifact.
CONSTRUCTION_RULE_DIR = (
    FROZEN
    / "05K1_Construction_Rule_v1_0"
)

EXPECTED_CONSTRUCTION_RULE_SHA = (
    "a2f38f"
)

# Prefix is intentional here because the complete SHA was not carried
# into this script specification. We will print the complete observed
# SHA and freeze it in the B output metadata.
#
# IMPORTANT:
# If this directory or its unique JSON file is not found, STOP.
# Do not invent or regenerate the rule artifact.


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


EXPECTED_CASES = 230
EXPECTED_CONDITIONS = 230 * 7


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
    arr = np.ascontiguousarray(arr)

    h = hashlib.sha256()

    h.update(
        str(arr.dtype).encode("utf-8")
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
        f"Expected 2-D grayscale array: {path}",
    )

    return arr


def save_gray_uint8(path, arr):
    require(
        arr.dtype == np.uint8,
        "Output array must be uint8",
    )

    require(
        arr.ndim == 2,
        "Output array must be 2-D",
    )

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    # Lossless PNG is used only as storage.
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

    if "output_relative_path" in row:
        p = str(
            row[
                "output_relative_path"
            ]
        ).strip()

        if p:
            candidates.append(
                V3_ROOT / p
            )

    if "relative_path" in row:
        p = str(
            row[
                "relative_path"
            ]
        ).strip()

        if p:
            candidates.append(
                V3_ROOT / p
            )

    for path in candidates:
        if path.is_file():
            return path

    raise RuntimeError(
        "Could not resolve V3 image for "
        f"row_index={row['row_index']} "
        f"relative_path={row['relative_path']}"
    )


# =============================================================================
# Header
# =============================================================================

print("=" * 108)
print(
    "P2-R0-05K3-B — "
    "230 × 7 CALIBRATION SUPPORT MATERIALIZATION"
)
print("=" * 108)

print("Descriptor execution       : NO")
print("Spectral metrics inspected : NO")
print("Hypothesis testing         : NO")
print("Population inference       : NO")
print()


# =============================================================================
# 1. Verify frozen sources
# =============================================================================

require(
    CALIBRATION_MANIFEST.is_file(),
    f"Missing calibration manifest: {CALIBRATION_MANIFEST}",
)

calibration_sha = sha256_file(
    CALIBRATION_MANIFEST
)

print(
    "05K3-A calibration manifest SHA:",
    calibration_sha,
    "PASS"
    if calibration_sha == EXPECTED_CALIBRATION_SHA
    else "FAIL",
)

require(
    calibration_sha
    == EXPECTED_CALIBRATION_SHA,
    "Frozen 05K3-A manifest SHA mismatch",
)


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
    "Frozen V3 manifest SHA mismatch",
)


# =============================================================================
# 2. Locate and verify frozen 05K1 construction-rule artifact
# =============================================================================

require(
    CONSTRUCTION_RULE_DIR.is_dir(),
    (
        "Missing frozen 05K1 construction-rule directory: "
        f"{CONSTRUCTION_RULE_DIR}"
    ),
)


rule_jsons = sorted(
    CONSTRUCTION_RULE_DIR.glob("*.json")
)


require(
    len(rule_jsons) == 1,
    (
        "Expected exactly one JSON rule artifact in "
        f"{CONSTRUCTION_RULE_DIR}; found {len(rule_jsons)}"
    ),
)


CONSTRUCTION_RULE_JSON = rule_jsons[
    0
]


construction_rule_sha = sha256_file(
    CONSTRUCTION_RULE_JSON
)


print(
    "05K1 construction rule:",
    CONSTRUCTION_RULE_JSON,
)

print(
    "05K1 construction-rule SHA:",
    construction_rule_sha,
)


require(
    construction_rule_sha.startswith(
        EXPECTED_CONSTRUCTION_RULE_SHA
    ),
    (
        "05K1 construction-rule SHA does not match "
        "the frozen a2f38f... provenance"
    ),
)


# We preserve the artifact itself as provenance.
construction_rule = json.loads(
    CONSTRUCTION_RULE_JSON.read_text(
        encoding="utf-8"
    )
)


# =============================================================================
# 3. Load 230-case frozen manifest and V3 provenance
# =============================================================================

cal = pd.read_csv(
    CALIBRATION_MANIFEST,
    keep_default_na=False,
)

v3 = pd.read_csv(
    V3_MANIFEST,
    keep_default_na=False,
)


require(
    len(cal) == EXPECTED_CASES,
    f"Expected 230 calibration rows; got {len(cal)}",
)

require(
    cal["row_index"].nunique()
    == EXPECTED_CASES,
    "Calibration row_index not unique",
)

require(
    cal["garment_identity"].nunique()
    == EXPECTED_CASES,
    "Calibration identities not unique",
)


required_v3 = {
    "row_index",
    "relative_path",
    "border_median",
}


require(
    required_v3.issubset(
        set(v3.columns)
    ),
    (
        "V3 manifest is missing required columns: "
        f"{required_v3 - set(v3.columns)}"
    ),
)


cal["row_index"] = (
    cal["row_index"]
    .astype(int)
)

v3["row_index"] = (
    v3["row_index"]
    .astype(int)
)


# =============================================================================
# 4. Bind calibration manifest to frozen V3 provenance
# =============================================================================

join_cols = [
    "row_index",
    "relative_path",
]


extra_v3_cols = [
    c
    for c in [
        "output_relative_path",
        "border_median",
        "output_pixel_sha256",
        "output_sha256",
        "source_sha256",
    ]
    if c in v3.columns
]


bound = cal.merge(
    v3[
        join_cols
        + extra_v3_cols
    ],
    on=join_cols,
    how="inner",
    validate="one_to_one",
    suffixes=(
        "",
        "_v3",
    ),
)


require(
    len(bound)
    == EXPECTED_CASES,
    (
        "Calibration ↔ V3 binding did not recover "
        f"all 230 rows; got {len(bound)}"
    ),
)


# =============================================================================
# 5. Materialize support intervention
# =============================================================================

records = []


for idx, row in bound.iterrows():

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
            "Non-finite border_median for "
            f"{row['relative_path']}"
        ),
    )


    # Frozen 05K1 fill rule.
    b_i = int(
        np.rint(
            255.0
            * border_median
        )
    )


    require(
        0 <= b_i <= 255,
        (
            "Padding value outside uint8 range for "
            f"{row['relative_path']}: {b_i}"
        ),
    )


    # Historical foreground diagnostic uses <250.
    # Padding must not create new foreground support.
    require(
        b_i >= 250,
        (
            "Frozen padding rule would create foreground "
            f"under <250 mask for {row['relative_path']}: "
            f"b_i={b_i}"
        ),
    )


    source_array_sha = sha256_array(
        source
    )


    for s in SUPPORT_LEVELS:

        pad_y = int(
            math.ceil(
                ((float(s) - 1.0) * H)
                / 2.0
            )
        )

        pad_x = int(
            math.ceil(
                ((float(s) - 1.0) * W)
                / 2.0
            )
        )


        Hs = H + 2 * pad_y
        Ws = W + 2 * pad_x


        expected_Hs = (
            H
            + 2 * int(
                math.ceil(
                    ((float(s) - 1.0) * H)
                    / 2.0
                )
            )
        )

        expected_Ws = (
            W
            + 2 * int(
                math.ceil(
                    ((float(s) - 1.0) * W)
                    / 2.0
                )
            )
        )


        require(
            Hs == expected_Hs
            and Ws == expected_Ws,
            "Construction-rule dimension mismatch",
        )


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
        # Exact embedded-patch preservation
        # ---------------------------------------------------------------------

        embedded = canvas[
            y0:y1,
            x0:x1,
        ]


        patch_array_equal = bool(
            np.array_equal(
                embedded,
                source,
            )
        )


        require(
            patch_array_equal,
            (
                "Embedded source patch changed: "
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
                "Embedded patch array SHA mismatch: "
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
            and embedded.shape == source.shape
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
                "Padding fill mismatch: "
                f"{row['relative_path']} s={s}"
            ),
        )


        # ---------------------------------------------------------------------
        # s=1 exact replay
        # ---------------------------------------------------------------------

        s1_exact = None


        if np.isclose(
            s,
            1.0,
            atol=0.0,
            rtol=0.0,
        ):

            s1_exact = bool(
                canvas.shape
                == source.shape
                and np.array_equal(
                    canvas,
                    source,
                )
            )


            require(
                s1_exact,
                (
                    "s=1 condition is not exact source replay: "
                    f"{row['relative_path']}"
                ),
            )


        # ---------------------------------------------------------------------
        # Save deterministic lossless canvas
        # ---------------------------------------------------------------------

        tag = support_tag(
            float(s)
        )


        out_relative = (
            Path(tag)
            / str(
                row[
                    "category"
                ]
            )
            / (
                f"{int(row['row_index']):04d}"
                f"__{str(row['garment_identity']).replace('::', '__')}"
                ".png"
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


        save_reload_exact = bool(
            np.array_equal(
                reloaded,
                canvas,
            )
        )


        require(
            save_reload_exact,
            (
                "Saved/reloaded canvas differs: "
                f"{out_relative}"
            ),
        )


        # ---------------------------------------------------------------------
        # Centroid offset bookkeeping only
        #
        # This is canvas-placement geometry, not a descriptor calculation.
        # ---------------------------------------------------------------------

        expected_center_shift_y = float(
            pad_y
        )

        expected_center_shift_x = float(
            pad_x
        )


        records.append({
            "calibration_index":
                int(
                    row[
                        "calibration_index"
                    ]
                ),

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

            "garment_identity":
                str(
                    row[
                        "garment_identity"
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
                float(
                    s
                ),

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
                float(
                    border_median
                ),

            "padding_value_uint8":
                int(
                    b_i
                ),

            "source_array_sha256":
                source_array_sha,

            "embedded_patch_array_sha256":
                embedded_sha,

            "patch_array_equal":
                patch_array_equal,

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
                save_reload_exact,

            "expected_source_offset_y":
                expected_center_shift_y,

            "expected_source_offset_x":
                expected_center_shift_x,

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
# 6. Integrity table
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
    "row_index × support_factor not unique",
)


require(
    bool(
        integrity[
            "patch_array_equal"
        ].all()
    ),
    "Not all embedded patches are exact",
)


require(
    bool(
        integrity[
            "padding_exact"
        ].all()
    ),
    "Not all padding regions are exact",
)


require(
    bool(
        integrity[
            "no_clipping"
        ].all()
    ),
    "Clipping occurred",
)


require(
    bool(
        integrity[
            "save_reload_exact"
        ].all()
    ),
    "Save/reload mismatch occurred",
)


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
    len(s1) == EXPECTED_CASES,
    "Expected exactly 230 s=1 conditions",
)


require(
    bool(
        s1[
            "s1_exact_source_replay"
        ]
        .astype(bool)
        .all()
    ),
    "Not all s=1 canvases exactly replay source arrays",
)


# =============================================================================
# 7. Save manifest
# =============================================================================

INTEGRITY_CSV = (
    OUT
    / "P2_R0_05K3_B_integrity_1610.csv"
)


integrity = (
    integrity.sort_values(
        [
            "calibration_index",
            "support_factor",
        ],
        kind="mergesort",
    )
    .reset_index(
        drop=True
    )
)


integrity.to_csv(
    INTEGRITY_CSV,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


# =============================================================================
# 8. Support-level construction summary
# =============================================================================

summary_rows = []


for s, g in integrity.groupby(
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
                    g
                )
            ),

        "unique_cases":
            int(
                g[
                    "row_index"
                ].nunique()
            ),

        "all_patch_exact":
            bool(
                g[
                    "patch_array_equal"
                ].all()
            ),

        "all_padding_exact":
            bool(
                g[
                    "padding_exact"
                ].all()
            ),

        "all_no_clipping":
            bool(
                g[
                    "no_clipping"
                ].all()
            ),

        "all_save_reload_exact":
            bool(
                g[
                    "save_reload_exact"
                ].all()
            ),

        "min_padding_value":
            int(
                g[
                    "padding_value_uint8"
                ].min()
            ),

        "max_padding_value":
            int(
                g[
                    "padding_value_uint8"
                ].max()
            ),

        "min_output_height":
            int(
                g[
                    "output_height"
                ].min()
            ),

        "max_output_height":
            int(
                g[
                    "output_height"
                ].max()
            ),

        "min_output_width":
            int(
                g[
                    "output_width"
                ].min()
            ),

        "max_output_width":
            int(
                g[
                    "output_width"
                ].max()
            ),
    })


support_summary = pd.DataFrame(
    summary_rows
)


SUPPORT_SUMMARY_CSV = (
    OUT
    / "P2_R0_05K3_B_support_level_summary.csv"
)


support_summary.to_csv(
    SUPPORT_SUMMARY_CSV,
    index=False,
    lineterminator="\n",
)


# =============================================================================
# 9. Report
# =============================================================================

REPORT_JSON = (
    OUT
    / "P2_R0_05K3_B_report.json"
)


report = {
    "stage":
        "P2_R0_05K3_B_CALIBRATION_SUPPORT_MATERIALIZATION",

    "status":
        "PASS_CONSTRUCTION_AND_INTEGRITY_ONLY",

    "calibration_cases":
        EXPECTED_CASES,

    "support_levels":
        SUPPORT_LEVELS.tolist(),

    "conditions_materialized":
        EXPECTED_CONDITIONS,

    "calibration_manifest": {
        "path":
            str(
                CALIBRATION_MANIFEST
            ),

        "sha256":
            calibration_sha,
    },

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
                CONSTRUCTION_RULE_JSON
            ),

        "sha256":
            construction_rule_sha,

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

        "fourier_band_analysis":
            False,

        "directional_hypotheses":
            False,

        "monotonicity_analysis":
            False,

        "population_inference":
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
    SUPPORT_SUMMARY_CSV,
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
print("=" * 108)
print(
    "P2-R0-05K3-B — "
    "CALIBRATION SUPPORT MATERIALIZATION: PASS"
)
print("=" * 108)

print(
    "Calibration cases:",
    EXPECTED_CASES,
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
    support_summary.to_string(
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
print("Spectral metrics inspected : NO")
print("Hypothesis verdicts        : NO")
print("Population inference       : NO")

print()
print("=" * 108)
print(
    "STOP — FREEZE 05K3-B BEFORE DESCRIPTOR EXECUTION"
)
print("=" * 108)