from pathlib import Path
import pandas as pd
import numpy as np
from PIL import Image
import hashlib
import json
import shutil


# ============================================================================
# P2-R0-05K1 — SENTINEL SUPPORT-ONLY MATERIALIZATION + INTEGRITY
#
# 10 frozen sentinels x 7 frozen support levels = 70 conditions.
#
# This stage tests CONSTRUCTION ONLY.
#
# NO Fourier descriptor.
# NO band fractions.
# NO H1/H2/H3.
# NO 05K spectral trajectory.
# ============================================================================


REPO = Path("/Users/nitikagupta/Research/WeaveAI")

V3_MANIFEST = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05f_crop_vs_resampling/"
    "V3_CROP_ONLY/materialized_manifest.csv"
)

SENTINEL_MANIFEST = (
    REPO
    / "papers/Paper-II/reproducibility/frozen/"
      "05K0_Sentinel_Manifest_v1_0a/"
      "P2_R0_05K0_sentinel_manifest_v1_0a.csv"
)

CONSTRUCTION_RULE = (
    REPO
    / "papers/Paper-II/reproducibility/frozen/"
      "05K1_Construction_Rule_v1_0/"
      "P2_R0_05K1_support_only_construction_rule_v1_0.json"
)

WORKDIR = (
    REPO
    / "papers/Paper-II/reproducibility/audits/"
      "05K1_materialization"
)

CANVAS_DIR = WORKDIR / "canvases"

WORKDIR.mkdir(parents=True, exist_ok=True)
CANVAS_DIR.mkdir(parents=True, exist_ok=True)


EXPECTED_SHA = {
    V3_MANIFEST:
        "19ab60c21c71de7918472142c36174ded9f8fae888eeb3320983ca2cc66a545e",

    SENTINEL_MANIFEST:
        "b9a1978d8a98744ecc349b038f24a8aa0078b409a1789ce006dcb0d17e3b2384",

    CONSTRUCTION_RULE:
        "a2f38fbed518d7e9371bb5f517b39aaf6d97c34be4ea476ebc455a64d5a6101f",
}


SUPPORT_LEVELS = [
    1.00,
    1.10,
    1.25,
    1.50,
    2.00,
    2.50,
    3.00,
]


# ============================================================================
# Helpers
# ============================================================================

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


def sha256_array_uint8(arr):
    arr = np.asarray(arr)

    require(
        arr.dtype == np.uint8,
        f"Expected uint8; got {arr.dtype}",
    )

    require(
        arr.ndim == 2,
        f"Expected 2D grayscale; got {arr.shape}",
    )

    return hashlib.sha256(
        np.ascontiguousarray(arr).tobytes()
    ).hexdigest()


def load_gray_uint8(path):
    with Image.open(path) as im:

        require(
            im.mode in ("L", "P", "1"),
            f"Unexpected mode {im.mode}: {path}",
        )

        arr = np.asarray(
            im.convert("L")
        )

    require(
        arr.dtype == np.uint8,
        f"Unexpected dtype: {arr.dtype}",
    )

    require(
        arr.ndim == 2,
        f"Unexpected shape: {arr.shape}",
    )

    return arr


def resolve_v3_image(manifest_dir, output_relative_path):
    p = Path(str(output_relative_path))

    if p.is_absolute():
        candidate = p
    else:
        candidate = manifest_dir / p

    require(
        candidate.exists(),
        f"Frozen V3 image missing: {candidate}",
    )

    return candidate


def support_geometry(h, w, s):

    pad_y = int(
        np.ceil(
            ((float(s) - 1.0) * h) / 2.0
        )
    )

    pad_x = int(
        np.ceil(
            ((float(s) - 1.0) * w) / 2.0
        )
    )

    hs = h + 2 * pad_y
    ws = w + 2 * pad_x

    return {
        "pad_top": pad_y,
        "pad_bottom": pad_y,
        "pad_left": pad_x,
        "pad_right": pad_x,

        "output_height": hs,
        "output_width": ws,

        "realized_scale_h":
            hs / h,

        "realized_scale_w":
            ws / w,

        "realized_scale_geom":
            float(
                np.sqrt(
                    (hs / h)
                    * (ws / w)
                )
            ),
    }


def outside_padding_mask(
    out_h,
    out_w,
    top,
    left,
    src_h,
    src_w,
):
    mask = np.ones(
        (out_h, out_w),
        dtype=bool,
    )

    mask[
        top:top + src_h,
        left:left + src_w,
    ] = False

    return mask


def condition_label(s):
    return (
        f"{float(s):.2f}"
        .replace(".", "p")
    )


# ============================================================================
# Start
# ============================================================================

print("=" * 88)
print("P2-R0-05K1 — SENTINEL SUPPORT-ONLY MATERIALIZATION + INTEGRITY")
print("=" * 88)

print("Frozen sentinels                : 10")
print("Frozen support levels           :", SUPPORT_LEVELS)
print("Expected conditions             : 70")
print("Fourier descriptor computed     : NO")
print("Band fractions computed         : NO")
print("05K spectral trajectories opened: NO")
print()


# ============================================================================
# 1. Verify all frozen inputs
# ============================================================================

for p, expected in EXPECTED_SHA.items():

    require(
        p.exists(),
        f"Missing frozen input: {p}",
    )

    got = sha256_file(p)

    print("FILE:", p)
    print("SHA :", got)
    print("PASS:", got == expected)
    print()

    require(
        got == expected,
        f"Frozen SHA mismatch: {p}",
    )


# ============================================================================
# 2. Verify frozen construction rule
# ============================================================================

rule = json.loads(
    CONSTRUCTION_RULE.read_text(
        encoding="utf-8"
    )
)

require(
    rule["protocol"]
    == "P2-R0-05K1-SUPPORT-ONLY-CONSTRUCTION-v1.0",
    "Unexpected construction-rule version",
)

require(
    rule["status"]
    == "FROZEN_BEFORE_CANVAS_MATERIALIZATION",
    "Construction rule was not frozen pre-materialization",
)

require(
    rule["support_levels"]
    == SUPPORT_LEVELS,
    "Support-level mismatch against frozen construction rule",
)

require(
    rule["background_fill_rule"]["formula"]
    == "b_i = int(rint(255 * border_median_i))",
    "Unexpected frozen background formula",
)


# ============================================================================
# 3. Load manifests
# ============================================================================

v3 = pd.read_csv(
    V3_MANIFEST
)

sent = pd.read_csv(
    SENTINEL_MANIFEST
)


require(
    len(v3) == 2300,
    f"V3 rows != 2300: {len(v3)}",
)

require(
    len(sent) == 10,
    f"Sentinel rows != 10: {len(sent)}",
)

require(
    sent["role"].nunique() == 10,
    "Sentinel roles are not unique",
)

require(
    sent["identity"].nunique() == 10,
    "Sentinel identities are not unique",
)


KEY = [
    "row_index",
    "relative_path",
]

require(
    not v3.duplicated(KEY).any(),
    "Duplicate V3 provenance keys",
)

require(
    not sent.duplicated(KEY).any(),
    "Duplicate sentinel provenance keys",
)


joined = sent.merge(
    v3,
    on=KEY,
    how="left",
    validate="one_to_one",
    suffixes=("_sentinel", "_v3"),
)

require(
    joined["output_relative_path"]
    .notna()
    .all(),
    "Sentinel failed to resolve to V3 manifest",
)


# ============================================================================
# 4. Materialize all 70 conditions
# ============================================================================

integrity_rows = []


for _, r in joined.iterrows():

    role = str(r["role"])
    row_index = int(r["row_index"])
    rel = str(r["relative_path"])
    identity = str(r["identity"])

    source_path = resolve_v3_image(
        V3_MANIFEST.parent,
        r["output_relative_path"],
    )

    source = load_gray_uint8(
        source_path
    )

    h, w = source.shape


    # ------------------------------------------------------------------------
    # Frozen source integrity before intervention
    # ------------------------------------------------------------------------

    expected_source_pixel_sha = str(
        r["output_pixel_sha256"]
    )

    source_pixel_sha = sha256_array_uint8(
        source
    )

    require(
        source_pixel_sha
        == expected_source_pixel_sha,
        (
            f"{role}: source pixel SHA mismatch\n"
            f"expected={expected_source_pixel_sha}\n"
            f"observed={source_pixel_sha}"
        ),
    )

    require(
        h == int(r["crop_height"]),
        f"{role}: source height mismatch",
    )

    require(
        w == int(r["crop_width"]),
        f"{role}: source width mismatch",
    )


    # ------------------------------------------------------------------------
    # Frozen 05K1 background-fill rule
    # ------------------------------------------------------------------------

    border_median = float(
        r["border_median"]
    )

    require(
        np.isfinite(border_median),
        f"{role}: border_median non-finite",
    )

    require(
        0.0 <= border_median <= 1.0,
        f"{role}: border_median outside [0,1]",
    )

    background_value = int(
        np.rint(
            255.0 * border_median
        )
    )

    require(
        0 <= background_value <= 255,
        f"{role}: invalid background value",
    )


    # ------------------------------------------------------------------------
    # Seven support levels
    # ------------------------------------------------------------------------

    for s in SUPPORT_LEVELS:

        g = support_geometry(
            h,
            w,
            s,
        )

        top = g["pad_top"]
        bottom = g["pad_bottom"]
        left = g["pad_left"]
        right = g["pad_right"]

        out_h = g["output_height"]
        out_w = g["output_width"]


        # --------------------------------------------------------------------
        # Construct
        # --------------------------------------------------------------------

        if np.isclose(s, 1.0):

            # At baseline use an exact pixel-array copy.
            canvas = source.copy()

        else:

            canvas = np.full(
                (out_h, out_w),
                fill_value=background_value,
                dtype=np.uint8,
            )

            canvas[
                top:top + h,
                left:left + w,
            ] = source


        # --------------------------------------------------------------------
        # Direct array integrity checks BEFORE file output
        # --------------------------------------------------------------------

        require(
            canvas.shape
            == (out_h, out_w),
            f"{role} s={s}: output shape wrong",
        )


        recovered_patch = canvas[
            top:top + h,
            left:left + w,
        ]

        patch_array_equal = np.array_equal(
            recovered_patch,
            source,
        )

        require(
            patch_array_equal,
            f"{role} s={s}: inserted source patch changed",
        )


        recovered_patch_sha = sha256_array_uint8(
            recovered_patch
        )

        patch_sha_match = (
            recovered_patch_sha
            == expected_source_pixel_sha
        )

        require(
            patch_sha_match,
            f"{role} s={s}: recovered patch SHA changed",
        )


        padding_mask = outside_padding_mask(
            out_h,
            out_w,
            top,
            left,
            h,
            w,
        )

        padding_pixels = canvas[
            padding_mask
        ]

        if padding_pixels.size:

            padding_all_expected_value = bool(
                np.all(
                    padding_pixels
                    == background_value
                )
            )

            padding_unique_values = (
                np.unique(
                    padding_pixels
                )
            )

        else:

            padding_all_expected_value = True
            padding_unique_values = np.array(
                [],
                dtype=np.uint8,
            )


        require(
            padding_all_expected_value,
            (
                f"{role} s={s}: outside-source pixels "
                "do not all equal frozen background"
            ),
        )


        # --------------------------------------------------------------------
        # Algebraic geometry checks
        # --------------------------------------------------------------------

        require(
            top == bottom,
            f"{role} s={s}: vertical padding asymmetric",
        )

        require(
            left == right,
            f"{role} s={s}: horizontal padding asymmetric",
        )

        require(
            out_h == h + top + bottom,
            f"{role} s={s}: output height algebra failed",
        )

        require(
            out_w == w + left + right,
            f"{role} s={s}: output width algebra failed",
        )


        no_clipping = (
            top >= 0
            and left >= 0
            and top + h <= out_h
            and left + w <= out_w
        )

        require(
            no_clipping,
            f"{role} s={s}: source clipping detected",
        )


        # --------------------------------------------------------------------
        # Source patch multiset is unchanged
        # --------------------------------------------------------------------

        src_hist = np.bincount(
            source.ravel(),
            minlength=256,
        )

        patch_hist = np.bincount(
            recovered_patch.ravel(),
            minlength=256,
        )

        source_pixel_multiset_equal = np.array_equal(
            src_hist,
            patch_hist,
        )

        require(
            source_pixel_multiset_equal,
            f"{role} s={s}: source pixel multiset changed",
        )


        # --------------------------------------------------------------------
        # Baseline must equal original V3 raster exactly
        # --------------------------------------------------------------------

        baseline_pixel_equal = None
        baseline_pixel_sha_match = None

        if np.isclose(s, 1.0):

            baseline_pixel_equal = bool(
                np.array_equal(
                    canvas,
                    source,
                )
            )

            baseline_pixel_sha_match = (
                sha256_array_uint8(canvas)
                == expected_source_pixel_sha
            )

            require(
                baseline_pixel_equal,
                f"{role}: s=1 array != source",
            )

            require(
                baseline_pixel_sha_match,
                f"{role}: s=1 pixel SHA != source",
            )


        # --------------------------------------------------------------------
        # Save deterministic PNG artifact
        # --------------------------------------------------------------------

        role_dir = CANVAS_DIR / role

        role_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        outfile = (
            role_dir
            / (
                f"{role}"
                f"__row{row_index:04d}"
                f"__s{condition_label(s)}.png"
            )
        )


        Image.fromarray(
            canvas,
            mode="L",
        ).save(
            outfile,
            format="PNG",
            optimize=False,
        )


        # --------------------------------------------------------------------
        # Reload output and repeat critical integrity tests
        # --------------------------------------------------------------------

        reloaded = load_gray_uint8(
            outfile
        )

        file_pixel_equal = np.array_equal(
            reloaded,
            canvas,
        )

        require(
            file_pixel_equal,
            f"{role} s={s}: saved/reloaded pixels changed",
        )


        file_pixel_sha = sha256_array_uint8(
            reloaded
        )

        file_sha = sha256_file(
            outfile
        )


        reloaded_patch = reloaded[
            top:top + h,
            left:left + w,
        ]

        reloaded_patch_sha = sha256_array_uint8(
            reloaded_patch
        )

        require(
            reloaded_patch_sha
            == expected_source_pixel_sha,
            f"{role} s={s}: disk output patch SHA changed",
        )


        # --------------------------------------------------------------------
        # Record
        # --------------------------------------------------------------------

        integrity_rows.append({

            "role":
                role,

            "row_index":
                row_index,

            "relative_path":
                rel,

            "identity":
                identity,

            "nominal_support_factor":
                float(s),

            "source_height":
                h,

            "source_width":
                w,

            "pad_top":
                top,

            "pad_bottom":
                bottom,

            "pad_left":
                left,

            "pad_right":
                right,

            "output_height":
                out_h,

            "output_width":
                out_w,

            "realized_scale_h":
                g["realized_scale_h"],

            "realized_scale_w":
                g["realized_scale_w"],

            "realized_scale_geom":
                g["realized_scale_geom"],

            "frozen_border_median":
                border_median,

            "background_value":
                background_value,

            "expected_source_pixel_sha256":
                expected_source_pixel_sha,

            "observed_source_pixel_sha256":
                source_pixel_sha,

            "recovered_patch_pixel_sha256":
                recovered_patch_sha,

            "source_patch_array_equal":
                patch_array_equal,

            "source_patch_sha_match":
                patch_sha_match,

            "source_pixel_multiset_equal":
                source_pixel_multiset_equal,

            "padding_all_expected_value":
                padding_all_expected_value,

            "padding_unique_value_count":
                int(
                    len(
                        padding_unique_values
                    )
                ),

            "no_clipping":
                no_clipping,

            "baseline_pixel_equal":
                baseline_pixel_equal,

            "baseline_pixel_sha_match":
                baseline_pixel_sha_match,

            "saved_reloaded_pixel_equal":
                file_pixel_equal,

            "saved_canvas_pixel_sha256":
                file_pixel_sha,

            "saved_png_sha256":
                file_sha,

            "output_relative_path":
                str(
                    outfile.relative_to(
                        REPO
                    )
                ),
        })


# ============================================================================
# 5. Integrity manifest
# ============================================================================

integrity = pd.DataFrame(
    integrity_rows
)


require(
    len(integrity) == 70,
    f"Expected 70 rows; got {len(integrity)}",
)


require(
    integrity[
        [
            "role",
            "nominal_support_factor",
        ]
    ].drop_duplicates().shape[0]
    == 70,
    "Role/support combination not unique",
)


for role in sent["role"]:

    sub = integrity.loc[
        integrity["role"] == role
    ]

    require(
        len(sub) == 7,
        f"{role}: expected 7 conditions",
    )

    require(
        sorted(
            sub[
                "nominal_support_factor"
            ].tolist()
        )
        == SUPPORT_LEVELS,
        f"{role}: support levels differ from freeze",
    )


boolean_pass_cols = [
    "source_patch_array_equal",
    "source_patch_sha_match",
    "source_pixel_multiset_equal",
    "padding_all_expected_value",
    "no_clipping",
    "saved_reloaded_pixel_equal",
]

for c in boolean_pass_cols:

    require(
        integrity[c].astype(bool).all(),
        f"Integrity failure in {c}",
    )


baseline = integrity.loc[
    np.isclose(
        integrity[
            "nominal_support_factor"
        ],
        1.0,
    )
]

require(
    len(baseline) == 10,
    "Expected 10 s=1 baseline rows",
)

require(
    baseline[
        "baseline_pixel_equal"
    ].astype(bool).all(),
    "At least one s=1 canvas changed",
)

require(
    baseline[
        "baseline_pixel_sha_match"
    ].astype(bool).all(),
    "At least one s=1 pixel SHA changed",
)


# ============================================================================
# 6. Output audit files
# ============================================================================

MANIFEST_OUT = (
    WORKDIR
    / "P2_R0_05K1_sentinel_materialization_integrity.csv"
)

META_OUT = (
    WORKDIR
    / "P2_R0_05K1_sentinel_materialization_metadata.json"
)

SUMS_OUT = (
    WORKDIR
    / "SHA256SUMS.txt"
)


integrity.to_csv(
    MANIFEST_OUT,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


manifest_sha = sha256_file(
    MANIFEST_OUT
)


# ============================================================================
# 7. Aggregate diagnostics
# ============================================================================

background_summary = (
    integrity[
        [
            "role",
            "background_value",
        ]
    ]
    .drop_duplicates()
    .sort_values("role")
)


condition_file_hashes = (
    integrity[
        [
            "output_relative_path",
            "saved_png_sha256",
        ]
    ]
    .sort_values(
        "output_relative_path"
    )
)


metadata = {

    "protocol":
        "P2-R0-05K1-SENTINEL-MATERIALIZATION-v1.0",

    "status":
        "PASS",

    "frozen_inputs": {
        V3_MANIFEST.name:
            EXPECTED_SHA[V3_MANIFEST],

        SENTINEL_MANIFEST.name:
            EXPECTED_SHA[SENTINEL_MANIFEST],

        CONSTRUCTION_RULE.name:
            EXPECTED_SHA[CONSTRUCTION_RULE],
    },

    "counts": {
        "sentinels": 10,
        "support_levels": 7,
        "conditions": 70,
    },

    "support_levels":
        SUPPORT_LEVELS,

    "construction": {
        "resize":
            False,

        "interpolation":
            False,

        "antialias":
            False,

        "rethreshold":
            False,

        "crop_recomputation":
            False,

        "source_patch_modified":
            False,

        "background_rule":
            "int(rint(255 * frozen_V3_border_median))",
    },

    "integrity": {
        "all_source_patches_array_equal":
            bool(
                integrity[
                    "source_patch_array_equal"
                ].all()
            ),

        "all_source_patch_sha_match":
            bool(
                integrity[
                    "source_patch_sha_match"
                ].all()
            ),

        "all_source_multisets_equal":
            bool(
                integrity[
                    "source_pixel_multiset_equal"
                ].all()
            ),

        "all_padding_values_correct":
            bool(
                integrity[
                    "padding_all_expected_value"
                ].all()
            ),

        "all_conditions_no_clipping":
            bool(
                integrity[
                    "no_clipping"
                ].all()
            ),

        "all_saved_reloads_equal":
            bool(
                integrity[
                    "saved_reloaded_pixel_equal"
                ].all()
            ),

        "all_s1_exact":
            bool(
                baseline[
                    "baseline_pixel_equal"
                ].astype(bool)
                .all()
            ),

        "all_s1_sha_match":
            bool(
                baseline[
                    "baseline_pixel_sha_match"
                ].astype(bool)
                .all()
            ),
    },

    "explicitly_not_tested_here": [
        "foreground-mask invariance",
        "foreground centroid invariance",
        "q99 foreground-radius invariance",
        "max foreground-radius invariance",
        "Fourier descriptor invariance",
        "band-fraction behavior",
        "H1",
        "H2",
        "H3",
    ],

    "anti_peeking": {
        "spectral_descriptor_computed":
            False,

        "05k_spectral_trajectory_opened":
            False,

        "h1_h2_h3_tested":
            False,
    },

    "integrity_manifest": {
        "filename":
            MANIFEST_OUT.name,

        "sha256":
            manifest_sha,
    },

    "canvas_png_sha256": {
        row.output_relative_path:
            row.saved_png_sha256

        for row
        in condition_file_hashes.itertuples(
            index=False
        )
    },
}


META_OUT.write_text(
    json.dumps(
        metadata,
        indent=2,
        sort_keys=True,
    )
    + "\n",
    encoding="utf-8",
)


meta_sha = sha256_file(
    META_OUT
)


# ============================================================================
# 8. Work-directory checksums
# ============================================================================

with SUMS_OUT.open(
    "w",
    encoding="utf-8",
) as f:

    f.write(
        f"{manifest_sha}  {MANIFEST_OUT.name}\n"
    )

    f.write(
        f"{meta_sha}  {META_OUT.name}\n"
    )

    for row in condition_file_hashes.itertuples(
        index=False
    ):

        rel_from_workdir = Path(
            row.output_relative_path
        )

        # output_relative_path is repo-relative;
        # checksum manifest should be WORKDIR-relative.
        abs_file = REPO / rel_from_workdir

        relative = abs_file.relative_to(
            WORKDIR
        )

        f.write(
            f"{row.saved_png_sha256}  {relative}\n"
        )


sums_sha = sha256_file(
    SUMS_OUT
)


# ============================================================================
# 9. Final report
# ============================================================================

print()
print("=" * 88)
print("05K1 MATERIALIZATION INTEGRITY SUMMARY")
print("=" * 88)

print("Conditions materialized          :", len(integrity))
print("Unique sentinels                 :", integrity["role"].nunique())
print("Support levels/sentinel          : 7")

print()
print("Source patches array-identical   : PASS")
print("Source patch SHA256 preserved    : PASS")
print("Source pixel multisets preserved : PASS")
print("Padding values exact             : PASS")
print("Symmetric geometry               : PASS")
print("No clipping                      : PASS")
print("Saved/reloaded arrays exact      : PASS")
print("s=1 exact source pixels          : PASS")
print("s=1 source pixel SHA             : PASS")

print()
print("BACKGROUND VALUES")
print(
    background_summary.to_string(
        index=False
    )
)

print()
print("OUTPUT SHA256")
print(
    MANIFEST_OUT.name,
    manifest_sha,
)

print(
    META_OUT.name,
    meta_sha,
)

print(
    SUMS_OUT.name,
    sums_sha,
)

print()
print("WORKDIR")
print(WORKDIR)

print()
print("Fourier descriptor computed      : NO")
print("Band fractions computed          : NO")
print("05K spectral trajectories opened : NO")
print("H1/H2/H3 tested                  : NO")

print()
print("=" * 88)
print("P2-R0-05K1 MATERIALIZATION: PASS")
print("STOP — DO NOT RUN DESCRIPTORS YET")
print("=" * 88)