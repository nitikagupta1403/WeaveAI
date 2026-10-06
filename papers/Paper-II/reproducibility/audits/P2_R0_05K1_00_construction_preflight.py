from pathlib import Path
import pandas as pd
import numpy as np
from PIL import Image
import hashlib
import json


# ============================================================================
# P2-R0-05K1 — SENTINEL SUPPORT-ONLY CONSTRUCTION PREFLIGHT
#
# Purpose
# -------
# Before materializing the 10 x 7 support-only intervention:
#
#   1. Verify the frozen sentinel manifest.
#   2. Resolve the exact frozen V3 CROP_ONLY raster for each sentinel.
#   3. Verify those rasters against the frozen V3 pixel SHA where available.
#   4. Inspect historical background evidence WITHOUT assuming 255.
#   5. Freeze the exact support-level integer dimensions/padding geometry.
#
# NO spectral descriptor is computed.
# NO 05K intervention trajectory is opened.
# NO H1/H2/H3 outcome is computed.
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

OUTDIR = (
    REPO
    / "papers/Paper-II/reproducibility/audits/"
      "05K1_construction_preflight"
)

OUTDIR.mkdir(
    parents=True,
    exist_ok=True,
)


EXPECTED_SHA = {
    V3_MANIFEST:
        "19ab60c21c71de7918472142c36174ded9f8fae888eeb3320983ca2cc66a545e",

    SENTINEL_MANIFEST:
        "b9a1978d8a98744ecc349b038f24a8aa0078b409a1789ce006dcb0d17e3b2384",
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
        f"Expected uint8 array; got {arr.dtype}",
    )

    require(
        arr.ndim == 2,
        f"Expected grayscale 2D array; got {arr.shape}",
    )

    return hashlib.sha256(
        np.ascontiguousarray(arr).tobytes()
    ).hexdigest()


def resolve_v3_image(manifest_dir, output_relative_path):
    """
    Frozen V3 manifest should resolve relative to its own directory.

    No recursive discovery and no alternative dataset search.
    """

    p = Path(str(output_relative_path))

    if p.is_absolute():
        candidate = p
    else:
        candidate = manifest_dir / p

    require(
        candidate.exists(),
        (
            "Could not resolve frozen V3 raster exactly from "
            f"output_relative_path:\n{candidate}"
        ),
    )

    return candidate


def load_gray_uint8(path):
    with Image.open(path) as im:

        require(
            im.mode in ("L", "P", "1"),
            (
                f"Unexpected image mode for {path}: {im.mode}. "
                "STOP rather than silently convert."
            ),
        )

        # Palette/1-bit image still needs literal raster values inspected.
        arr = np.asarray(im.convert("L"))

    require(
        arr.ndim == 2,
        f"Expected 2D grayscale raster: {path}",
    )

    require(
        arr.dtype == np.uint8,
        f"Expected uint8 raster: {path}",
    )

    return arr


def perimeter_pixels(arr):
    """
    Returns raster perimeter only.
    This is diagnostic evidence, NOT a foreground definition.
    """

    top = arr[0, :]
    bottom = arr[-1, :]

    if arr.shape[0] > 2:
        left = arr[1:-1, 0]
        right = arr[1:-1, -1]

        return np.concatenate(
            [top, bottom, left, right]
        )

    return np.concatenate(
        [top, bottom]
    )


def support_geometry(h, w, s):
    """
    Frozen proposed canvas rule:

        H_s = H + 2*ceil(((s-1)*H)/2)
        W_s = W + 2*ceil(((s-1)*W)/2)

    Gives exact symmetric integer padding.
    """

    pad_y = int(
        np.ceil(
            ((s - 1.0) * h) / 2.0
        )
    )

    pad_x = int(
        np.ceil(
            ((s - 1.0) * w) / 2.0
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
        "realized_scale_h": hs / h,
        "realized_scale_w": ws / w,
        "realized_scale_geom": np.sqrt(
            (hs / h) * (ws / w)
        ),
    }


# ============================================================================
# Start
# ============================================================================

print("=" * 84)
print("P2-R0-05K1 — SENTINEL SUPPORT-ONLY CONSTRUCTION PREFLIGHT")
print("=" * 84)

print("Sentinel IDs already frozen      : YES")
print("Support levels                   :", SUPPORT_LEVELS)
print("05K spectral trajectories opened : NO")
print("Descriptor computation performed : NO")
print("Images modified                  : NO")
print()


# ============================================================================
# 1. Frozen input verification
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
# 2. Load manifests
# ============================================================================

v3 = pd.read_csv(
    V3_MANIFEST
)

sent = pd.read_csv(
    SENTINEL_MANIFEST
)


require(
    len(v3) == 2300,
    f"Expected 2300 V3 rows; got {len(v3)}",
)

require(
    len(sent) == 10,
    f"Expected 10 frozen sentinels; got {len(sent)}",
)

require(
    sent["role"].nunique() == 10,
    "Sentinel roles are not unique",
)

require(
    sent["identity"].nunique() == 10,
    "Sentinel identities are not unique",
)


# ============================================================================
# 3. Join sentinel rows to exact V3 rows
# ============================================================================

KEY = [
    "row_index",
    "relative_path",
]

require(
    not v3.duplicated(KEY).any(),
    "Duplicate V3 provenance key",
)

require(
    not sent.duplicated(KEY).any(),
    "Duplicate sentinel provenance key",
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
    "At least one sentinel did not resolve into V3 manifest",
)


# ============================================================================
# 4. Resolve + inspect exact frozen V3 rasters
# ============================================================================

rows = []

for _, r in joined.iterrows():

    role = str(r["role"])

    image_path = resolve_v3_image(
        V3_MANIFEST.parent,
        r["output_relative_path"],
    )

    arr = load_gray_uint8(
        image_path
    )

    h, w = arr.shape

    require(
        h == int(r["crop_height"]),
        (
            f"{role}: raster height {h} != "
            f"manifest crop_height {r['crop_height']}"
        ),
    )

    require(
        w == int(r["crop_width"]),
        (
            f"{role}: raster width {w} != "
            f"manifest crop_width {r['crop_width']}"
        ),
    )


    observed_pixel_sha = sha256_array_uint8(
        arr
    )

    expected_pixel_sha = str(
        r["output_pixel_sha256"]
    )


    pixel_sha_match = (
        observed_pixel_sha
        == expected_pixel_sha
    )

    require(
        pixel_sha_match,
        (
            f"{role}: V3 pixel SHA mismatch\n"
            f"expected={expected_pixel_sha}\n"
            f"observed={observed_pixel_sha}"
        ),
    )


    perimeter = perimeter_pixels(
        arr
    )

    values, counts = np.unique(
        perimeter,
        return_counts=True,
    )

    order = np.argsort(
        -counts
    )

    values = values[order]
    counts = counts[order]


    perimeter_mode = int(
        values[0]
    )

    perimeter_mode_count = int(
        counts[0]
    )

    perimeter_n = int(
        len(perimeter)
    )

    perimeter_mode_fraction = (
        perimeter_mode_count
        / perimeter_n
    )


    corners = [
        int(arr[0, 0]),
        int(arr[0, -1]),
        int(arr[-1, 0]),
        int(arr[-1, -1]),
    ]

    corners_all_equal = (
        len(set(corners)) == 1
    )


    # --------------------------------------------------------
    # IMPORTANT
    #
    # These values are diagnostics only.
    #
    # We are NOT yet choosing padding_background_value from:
    #   - perimeter mode
    #   - corners
    #   - 255
    #   - border_median
    #
    # That choice must match frozen historical implementation.
    # --------------------------------------------------------

    rows.append({
        "role":
            role,

        "row_index":
            int(r["row_index"]),

        "relative_path":
            str(r["relative_path"]),

        "identity":
            str(r["identity"]),

        "v3_image_path":
            str(image_path),

        "height":
            h,

        "width":
            w,

        "output_pixel_sha256":
            expected_pixel_sha,

        "observed_pixel_sha256":
            observed_pixel_sha,

        "pixel_sha_match":
            pixel_sha_match,

        "manifest_border_median":
            float(r["border_median"]),

        "manifest_inverted":
            str(r["inverted"]),

        "corner_tl":
            corners[0],

        "corner_tr":
            corners[1],

        "corner_bl":
            corners[2],

        "corner_br":
            corners[3],

        "corners_all_equal":
            corners_all_equal,

        "perimeter_mode":
            perimeter_mode,

        "perimeter_mode_count":
            perimeter_mode_count,

        "perimeter_n":
            perimeter_n,

        "perimeter_mode_fraction":
            perimeter_mode_fraction,

        "perimeter_unique_values":
            int(len(values)),

        "array_min":
            int(arr.min()),

        "array_max":
            int(arr.max()),
    })


inspection = pd.DataFrame(
    rows
)


# ============================================================================
# 5. Freeze proposed support geometry only
#
# No canvas is materialized yet.
# ============================================================================

geometry_rows = []

for _, r in inspection.iterrows():

    h = int(r["height"])
    w = int(r["width"])

    for s in SUPPORT_LEVELS:

        g = support_geometry(
            h,
            w,
            s,
        )

        geometry_rows.append({
            "role":
                r["role"],

            "row_index":
                int(r["row_index"]),

            "relative_path":
                r["relative_path"],

            "identity":
                r["identity"],

            "nominal_support_factor":
                float(s),

            "source_height":
                h,

            "source_width":
                w,

            **g,
        })


geometry = pd.DataFrame(
    geometry_rows
)


require(
    len(geometry) == 70,
    f"Expected 70 support conditions; got {len(geometry)}",
)


# s = 1.00 must be exact original dimensions and zero padding.
baseline = geometry.loc[
    np.isclose(
        geometry["nominal_support_factor"],
        1.0,
    )
]

require(
    (
        baseline["pad_top"] == 0
    ).all(),
    "s=1.00 has non-zero vertical padding",
)

require(
    (
        baseline["pad_left"] == 0
    ).all(),
    "s=1.00 has non-zero horizontal padding",
)

require(
    (
        baseline["output_height"]
        == baseline["source_height"]
    ).all(),
    "s=1.00 height changed",
)

require(
    (
        baseline["output_width"]
        == baseline["source_width"]
    ).all(),
    "s=1.00 width changed",
)


# ============================================================================
# 6. Outputs
# ============================================================================

INSPECTION_OUT = (
    OUTDIR
    / "P2_R0_05K1_sentinel_v3_background_inspection.csv"
)

GEOMETRY_OUT = (
    OUTDIR
    / "P2_R0_05K1_support_geometry_preflight.csv"
)

META_OUT = (
    OUTDIR
    / "P2_R0_05K1_construction_preflight_metadata.json"
)


inspection.to_csv(
    INSPECTION_OUT,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)

geometry.to_csv(
    GEOMETRY_OUT,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


metadata = {
    "audit":
        "P2-R0-05K1 construction preflight",

    "status":
        "BACKGROUND_RULE_NOT_YET_ASSUMED",

    "frozen_inputs": {
        V3_MANIFEST.name:
            EXPECTED_SHA[V3_MANIFEST],

        SENTINEL_MANIFEST.name:
            EXPECTED_SHA[SENTINEL_MANIFEST],
    },

    "support_levels":
        SUPPORT_LEVELS,

    "canvas_dimension_rule": {
        "height":
            "H + 2*ceil(((s-1)*H)/2)",

        "width":
            "W + 2*ceil(((s-1)*W)/2)",

        "padding":
            "symmetric integer padding",
    },

    "background_rule": {
        "assumed_value":
            None,

        "status":
            "MUST_RECOVER_FROM_HISTORICAL_PREPROCESSING",

        "explicitly_not_assumed":
            [
                255,
                "perimeter_mode",
                "corner_value",
                "manifest_border_median",
            ],
    },

    "anti_peeking": {
        "spectral_descriptor_computed":
            False,

        "band_fraction_computed":
            False,

        "05k_intervention_trajectory_opened":
            False,

        "h1_h2_h3_tested":
            False,
    },

    "counts": {
        "sentinels":
            10,

        "support_levels":
            7,

        "planned_conditions":
            70,
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


print()
print("=" * 84)
print("V3 SENTINEL BACKGROUND INSPECTION")
print("=" * 84)

print(
    inspection[
        [
            "role",
            "relative_path",
            "height",
            "width",
            "manifest_border_median",
            "manifest_inverted",
            "corner_tl",
            "corner_tr",
            "corner_bl",
            "corner_br",
            "corners_all_equal",
            "perimeter_mode",
            "perimeter_mode_fraction",
            "perimeter_unique_values",
        ]
    ].to_string(
        index=False
    )
)


print()
print("=" * 84)
print("SUPPORT GEOMETRY PREFLIGHT")
print("=" * 84)

print("Sentinels             :", len(inspection))
print("Support levels        :", len(SUPPORT_LEVELS))
print("Planned conditions    :", len(geometry))
print("s=1 exact dimensions  : PASS")
print("All V3 pixel SHAs     : PASS")

print()
print("Padding background chosen : NO")
print("Canvas materialized        : NO")
print("Spectral descriptor run    : NO")
print("05K trajectories opened    : NO")

print()
print("OUTPUTS")
print(INSPECTION_OUT)
print(GEOMETRY_OUT)
print(META_OUT)

print()
print("=" * 84)
print("PREFLIGHT COMPLETE — STOP BEFORE MATERIALIZATION")
print("=" * 84)