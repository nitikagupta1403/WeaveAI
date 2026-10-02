from pathlib import Path
import hashlib
import importlib.util
import json

import numpy as np
import pandas as pd
from PIL import Image


# =============================================================================
# P2-R0-05K2-A2
# s=1.00 EXACT REPLAY VALIDATION
#
# PURPOSE
#   Validate the frozen 05K descriptor implementation against historical
#   V3_CROP_ONLY / H1 behavior BEFORE any s>1 condition is processed.
#
# IMPORTANT
#   - Full 2300 population is used for historical RA14 execution context.
#   - Only the ten frozen s=1.00 sentinel canvases are substituted.
#   - NO s>1 image is loaded.
#   - NO support trajectory is computed.
#   - NO H1/H2/H3 hypothesis is tested.
# =============================================================================


REPO = Path(
    "/Users/nitikagupta/Research/WeaveAI"
)

AUDIT_ROOT = (
    REPO
    / "papers/Paper-II/reproducibility/audits"
)

OUTDIR = (
    AUDIT_ROOT
    / "05K2_A2_s1_exact_replay"
)

OUTDIR.mkdir(
    parents=True,
    exist_ok=True,
)


# -----------------------------------------------------------------------------
# Frozen implementation anchors
# -----------------------------------------------------------------------------

RA14_SOURCE = (
    REPO
    / "papers/CLO-SKET/Codes_paper_I/Experiment_08/"
      "extract_ra14_features.py"
)

I2_SOURCE = (
    AUDIT_ROOT
    / "P2_R0_05I2_objective_real_garment_candidate_selection.py"
)

H1_SOURCE = (
    AUDIT_ROOT
    / "P2_R0_05H1_intrinsic_coordinate_field.py"
)

SOURCE_LOCK = (
    REPO
    / "papers/Paper-II/reproducibility/frozen/"
      "05K2_Descriptor_Source_Lock_v1_0/"
      "P2_R0_05K2_descriptor_source_lock_v1_0.json"
)


# -----------------------------------------------------------------------------
# Frozen 05K materialization
# -----------------------------------------------------------------------------

MAT_ROOT = (
    REPO
    / "papers/Paper-II/reproducibility/frozen/"
      "05K1_Sentinel_Materialization_v1_0"
)

MAT_MANIFEST = (
    MAT_ROOT
    / "P2_R0_05K1_sentinel_materialization_integrity.csv"
)


# -----------------------------------------------------------------------------
# Historical V3 / I2
# -----------------------------------------------------------------------------

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


# -----------------------------------------------------------------------------
# Historical H1 artifact root
# -----------------------------------------------------------------------------

H1_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05h_intrinsic_coordinate"
)


EXPECTED = {
    "RA14_SOURCE":
        "3b3dad8315616b4c8a0013cdcb4c3258b243b8fc2722b366ecc8a0e8743fdca9",

    "I2_SOURCE":
        "802325ae23b3896bd0bf51bed49fd0bf5218583d73f76d1bae69f6f70e9fa3e3",

    "H1_SOURCE":
        "1ce3c0dd7f34e75c806777bff9c5142814f179a0b6fef48f927fbfeb1b4d1642",

    "V3_MANIFEST":
        "19ab60c21c71de7918472142c36174ded9f8fae888eeb3320983ca2cc66a545e",

    "I2_PER_IMAGE":
        "a9a096b4aafe89be79b5d3c35fd3e4dc4e6de046c30326f108d0cbe3601c39e2",

    "H1_FIELD":
        "aaa69c8a6a416979dc037ae6c0197d5c62f1959eb41cc0482c8b5a3bdde21c03",
}


BANDS = [
    "low_1_4",
    "mid_5_12",
    "highmid_13_24",
    "high_25_36",
]


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

    return hashlib.sha256(
        arr.tobytes()
    ).hexdigest()


def load_module(name, path):

    spec = importlib.util.spec_from_file_location(
        name,
        path,
    )

    require(
        spec is not None
        and spec.loader is not None,
        f"Cannot import: {path}",
    )

    module = importlib.util.module_from_spec(
        spec
    )

    spec.loader.exec_module(
        module
    )

    return module


def load_gray(path):

    with Image.open(path) as im:

        return np.asarray(
            im.convert("L"),
            dtype=np.uint8,
        )


def locate_by_sha(
    root,
    expected_sha,
    suffix=None,
):

    hits = []

    for p in root.rglob("*"):

        if not p.is_file():
            continue

        if (
            suffix is not None
            and p.suffix.lower()
            != suffix.lower()
        ):
            continue

        try:
            if sha256_file(p) == expected_sha:
                hits.append(p)

        except Exception:
            pass

    require(
        len(hits) == 1,
        (
            f"Expected exactly one artifact with SHA "
            f"{expected_sha}; found {len(hits)}:\n"
            + "\n".join(map(str, hits))
        ),
    )

    return hits[0]


def resolve_crop_fraction_column(
    df,
    band,
):

    candidates = [
        f"crop_{band}_fraction",
        f"crop_only_{band}_fraction",
        f"V3_CROP_ONLY_{band}_fraction",
        band,
    ]

    for c in candidates:

        if c in df.columns:
            return c

    raise RuntimeError(
        f"No historical CROP_ONLY column "
        f"found for band {band}"
    )


# =============================================================================
# Header
# =============================================================================

print("=" * 96)
print(
    "P2-R0-05K2-A2 — "
    "s=1.00 EXACT REPLAY VALIDATION"
)
print("=" * 96)

print("s>1 images loaded             : NO")
print("Support trajectory computed   : NO")
print("Hypotheses tested             : NO")
print()


# =============================================================================
# 1. Verify frozen sources
# =============================================================================

source_paths = {
    "RA14_SOURCE":
        RA14_SOURCE,

    "I2_SOURCE":
        I2_SOURCE,

    "H1_SOURCE":
        H1_SOURCE,

    "V3_MANIFEST":
        V3_MANIFEST,

    "I2_PER_IMAGE":
        I2_PER_IMAGE,
}


for name, path in source_paths.items():

    require(
        path.exists(),
        f"Missing source: {path}",
    )

    observed = sha256_file(
        path
    )

    expected = EXPECTED[name]

    print(name)
    print("PATH :", path)
    print("SHA  :", observed)
    print("PASS :", observed == expected)
    print()

    require(
        observed == expected,
        f"{name} SHA mismatch",
    )


require(
    SOURCE_LOCK.exists(),
    "Frozen 05K2 source lock missing",
)

require(
    MAT_MANIFEST.exists(),
    "Frozen materialization manifest missing",
)


# =============================================================================
# 2. Import exact frozen implementations
# =============================================================================

ra14 = load_module(
    "p2_05k2_ra14_exact",
    RA14_SOURCE,
)

i2 = load_module(
    "p2_05k2_i2_exact",
    I2_SOURCE,
)

h1 = load_module(
    "p2_05k2_h1_exact",
    H1_SOURCE,
)


require(
    hasattr(
        ra14,
        "recover_geometry",
    ),
    "RA14 recover_geometry missing",
)

require(
    hasattr(
        i2,
        "angular_band_fractions",
    ),
    "I2 angular_band_fractions missing",
)

require(
    hasattr(
        h1,
        "diagnostic_ink_mask",
    ),
    "H1 diagnostic_ink_mask missing",
)

require(
    hasattr(
        h1,
        "intrinsic_field_from_mask",
    ),
    "H1 intrinsic_field_from_mask missing",
)


# =============================================================================
# 3. Load V3 population
# =============================================================================

v3 = pd.read_csv(
    V3_MANIFEST,
    keep_default_na=False,
).sort_values(
    "row_index"
).reset_index(
    drop=True
)


require(
    len(v3) == 2300,
    f"Expected 2300 V3 rows; got {len(v3)}",
)

require(
    np.array_equal(
        v3["row_index"].to_numpy(),
        np.arange(2300),
    ),
    "V3 row_index is not exact 0..2299 order",
)


# =============================================================================
# 4. Resolve exactly ten s=1 frozen canvases
# =============================================================================

mat = pd.read_csv(
    MAT_MANIFEST,
    keep_default_na=False,
)

s1 = mat.loc[
    np.isclose(
        mat[
            "nominal_support_factor"
        ].astype(float),
        1.0,
    )
].copy()


require(
    len(s1) == 10,
    f"Expected 10 s=1 rows; got {len(s1)}",
)

require(
    s1["role"].nunique() == 10,
    "s=1 roles are not unique",
)


s1_paths = {}


for _, r in s1.iterrows():

    role = str(
        r["role"]
    )

    row_index = int(
        r["row_index"]
    )

    old_relative = Path(
        str(
            r[
                "output_relative_path"
            ]
        )
    )

    frozen_path = (
        MAT_ROOT
        / "canvases"
        / role
        / old_relative.name
    )

    require(
        frozen_path.exists(),
        f"Frozen s=1 PNG missing: {frozen_path}",
    )

    expected_png_sha = str(
        r["saved_png_sha256"]
    )

    observed_png_sha = sha256_file(
        frozen_path
    )

    require(
        observed_png_sha
        == expected_png_sha,
        f"{role}: frozen PNG SHA mismatch",
    )

    s1_paths[
        row_index
    ] = frozen_path


require(
    len(s1_paths) == 10,
    "Did not resolve ten unique s=1 paths",
)


# =============================================================================
# 5. Verify each s=1 image is still exactly its V3 source raster
# =============================================================================

pixel_rows = []


for row_index, s1_path in sorted(
    s1_paths.items()
):

    rec = v3.iloc[
        row_index
    ]

    v3_path = (
        V3_ROOT
        / str(
            rec[
                "output_relative_path"
            ]
        )
    )

    require(
        v3_path.exists(),
        f"V3 image missing: {v3_path}",
    )

    a = load_gray(
        v3_path
    )

    b = load_gray(
        s1_path
    )

    equal = np.array_equal(
        a,
        b,
    )

    max_diff = int(
        np.max(
            np.abs(
                a.astype(np.int16)
                - b.astype(np.int16)
            )
        )
    )

    require(
        equal,
        f"row {row_index}: s=1 != V3 pixels",
    )

    pixel_rows.append({
        "row_index":
            row_index,

        "role":
            str(
                s1.loc[
                    s1[
                        "row_index"
                    ].astype(int)
                    == row_index,
                    "role",
                ].iloc[0]
            ),

        "relative_path":
            str(
                rec[
                    "relative_path"
                ]
            ),

        "v3_vs_s1_array_equal":
            bool(equal),

        "v3_vs_s1_max_pixel_diff":
            max_diff,

        "v3_pixel_sha256":
            sha256_array(a),

        "s1_pixel_sha256":
            sha256_array(b),
    })


print("=" * 96)
print("S=1 PIXEL REPLAY")
print("=" * 96)
print("10/10 V3 ↔ frozen s=1 arrays exact: PASS")
print()


# =============================================================================
# 6. Build full-population RA14 input A:
#    original V3 population
# =============================================================================

original_rows = []


for _, r in v3.iterrows():

    rel = str(
        r["relative_path"]
    )

    path = (
        V3_ROOT
        / str(
            r[
                "output_relative_path"
            ]
        )
    )

    require(
        path.exists(),
        f"Missing V3 path: {path}",
    )

    original_rows.append({
        "relative_path":
            rel,

        "category":
            Path(rel).parts[0],

        "path":
            path,
    })


# =============================================================================
# 7. Build full-population RA14 input B:
#    replace ONLY ten sentinel rows with frozen s=1 copies
# =============================================================================

substituted_rows = []


for i, row in enumerate(
    original_rows
):

    row2 = dict(row)

    if i in s1_paths:

        row2[
            "path"
        ] = s1_paths[i]

    substituted_rows.append(
        row2
    )


# =============================================================================
# 8. Exact historical raster-relative replay
# =============================================================================

print("=" * 96)
print("RASTER-RELATIVE FULL-POPULATION REPLAY")
print("=" * 96)

print(
    "A: original frozen V3 population..."
)

(
    raster_A,
    nonempty_A,
    radial_A,
    mass_error_A,
    norm_error_A,
) = ra14.recover_geometry(
    original_rows
)


print(
    "\nB: same population with ten "
    "frozen s=1 copies substituted..."
)

(
    raster_B,
    nonempty_B,
    radial_B,
    mass_error_B,
    norm_error_B,
) = ra14.recover_geometry(
    substituted_rows
)


raster_A = np.asarray(
    raster_A,
    dtype=np.float64,
)

raster_B = np.asarray(
    raster_B,
    dtype=np.float64,
)


require(
    raster_A.shape
    == (2300, 72, 72),
    f"Unexpected raster A shape {raster_A.shape}",
)

require(
    raster_B.shape
    == (2300, 72, 72),
    f"Unexpected raster B shape {raster_B.shape}",
)


raster_exact_all = np.array_equal(
    raster_A,
    raster_B,
)

raster_max_diff_all = float(
    np.max(
        np.abs(
            raster_A
            - raster_B
        )
    )
)


sentinel_indices = np.asarray(
    sorted(
        s1_paths.keys()
    ),
    dtype=int,
)


raster_exact_10 = np.array_equal(
    raster_A[
        sentinel_indices
    ],
    raster_B[
        sentinel_indices
    ],
)

raster_max_diff_10 = float(
    np.max(
        np.abs(
            raster_A[
                sentinel_indices
            ]
            - raster_B[
                sentinel_indices
            ]
        )
    )
)


require(
    raster_exact_all,
    (
        "Raster replay not exactly equal. "
        f"max_abs_diff={raster_max_diff_all}"
    ),
)


require(
    np.array_equal(
        nonempty_A,
        nonempty_B,
    ),
    "Raster nonempty-shell masks differ",
)


require(
    np.array_equal(
        radial_A,
        radial_B,
    ),
    "Raster radial centers differ",
)


print(
    "Entire 2300 raster field exact:",
    raster_exact_all,
)

print(
    "Max absolute field diff:",
    raster_max_diff_all,
)

print(
    "10 sentinel raster fields exact:",
    raster_exact_10,
)

print()


# =============================================================================
# 9. Exact I2 spectral reduction on raster replay
# =============================================================================

bands_A = i2.angular_band_fractions(
    raster_A
)

bands_B = i2.angular_band_fractions(
    raster_B
)


require(
    list(bands_A.columns)
    == BANDS,
    f"Unexpected I2 bands: {bands_A.columns.tolist()}",
)

require(
    np.array_equal(
        bands_A.to_numpy(),
        bands_B.to_numpy(),
    ),
    "Raster band fractions differ after s=1 substitution",
)


# =============================================================================
# 10. Compare raster fractions against historical I2 CSV
# =============================================================================

hist_i2 = pd.read_csv(
    I2_PER_IMAGE,
    keep_default_na=False,
)


require(
    len(hist_i2) == 2300,
    f"Historical I2 rows != 2300: {len(hist_i2)}",
)


if "row_index" in hist_i2.columns:

    hist_i2 = hist_i2.sort_values(
        "row_index"
    ).reset_index(
        drop=True
    )


historical_crop_columns = {
    band:
        resolve_crop_fraction_column(
            hist_i2,
            band,
        )
    for band in BANDS
}


hist_crop = np.column_stack(
    [
        hist_i2[
            historical_crop_columns[
                band
            ]
        ].astype(float).to_numpy()

        for band
        in BANDS
    ]
)


observed_crop = (
    bands_A[
        BANDS
    ]
    .to_numpy(
        dtype=float
    )
)


require(
    hist_crop.shape
    == observed_crop.shape,
    "Historical/current band array shape mismatch",
)


hist_raster_diff = np.abs(
    hist_crop
    - observed_crop
)


hist_raster_max_all = float(
    np.max(
        hist_raster_diff
    )
)

hist_raster_max_10 = float(
    np.max(
        hist_raster_diff[
            sentinel_indices
        ]
    )
)


RASTER_HISTORY_TOL = 1e-12


require(
    hist_raster_max_10
    <= RASTER_HISTORY_TOL,
    (
        "s=1 raster fractions do not reproduce "
        "historical I2 values: "
        f"{hist_raster_max_10}"
    ),
)


print("=" * 96)
print("RASTER HISTORICAL BAND-FRACTION REPLAY")
print("=" * 96)

print(
    "Max abs diff, all 2300:",
    hist_raster_max_all,
)

print(
    "Max abs diff, 10 sentinels:",
    hist_raster_max_10,
)

print(
    "Tolerance:",
    RASTER_HISTORY_TOL,
)

print("PASS")
print()


# =============================================================================
# 11. Locate frozen H1 intrinsic field artifact by immutable SHA
# =============================================================================

print("=" * 96)
print("LOCATING FROZEN H1 INTRINSIC FIELD")
print("=" * 96)


require(
    H1_ROOT.exists(),
    f"H1 artifact root missing: {H1_ROOT}",
)


H1_FIELD_NPZ = locate_by_sha(
    H1_ROOT,
    EXPECTED[
        "H1_FIELD"
    ],
    suffix=".npz",
)


print("H1 FIELD:", H1_FIELD_NPZ)
print(
    "SHA:",
    sha256_file(
        H1_FIELD_NPZ
    )
)
print()


artifact = np.load(
    H1_FIELD_NPZ,
    allow_pickle=False,
)


required_keys = {
    "conditional_angular",
    "nonempty_shells",
    "radial_centers",
    "relative_paths",
    "categories",
    "representation_name",
}


require(
    required_keys.issubset(
        set(
            artifact.files
        )
    ),
    "H1 NPZ missing required arrays",
)


h1_field = np.asarray(
    artifact[
        "conditional_angular"
    ],
    dtype=np.float64,
)


h1_nonempty = np.asarray(
    artifact[
        "nonempty_shells"
    ],
    dtype=bool,
)


h1_paths = np.asarray(
    artifact[
        "relative_paths"
    ],
    dtype=str,
)


require(
    h1_field.shape
    == (2300, 72, 72),
    f"Unexpected H1 field shape: {h1_field.shape}",
)


v3_paths = v3[
    "relative_path"
].astype(
    str
).to_numpy()


require(
    np.array_equal(
        h1_paths,
        v3_paths,
    ),
    "H1 field ordering does not match V3 ordering",
)


# =============================================================================
# 12. Recompute exact H1 intrinsic field for the ten s=1 canvases
# =============================================================================

intrinsic_replay_rows = []

h1_replaced = h1_field.copy()


for row_index in sentinel_indices:

    path = s1_paths[
        int(row_index)
    ]

    gray = load_gray(
        path
    )

    mask = h1.diagnostic_ink_mask(
        gray
    )

    (
        field,
        nonempty,
        cx,
        cy,
        max_radius,
        foreground_pixels,
        mass_error,
        norm_error,
    ) = h1.intrinsic_field_from_mask(
        mask
    )


    historical_field = h1_field[
        row_index
    ]


    exact_field = np.array_equal(
        field,
        historical_field,
    )

    max_field_diff = float(
        np.max(
            np.abs(
                field
                - historical_field
            )
        )
    )


    exact_nonempty = np.array_equal(
        nonempty,
        h1_nonempty[
            row_index
        ],
    )


    require(
        exact_field,
        (
            f"H1 intrinsic field mismatch "
            f"row={row_index}, "
            f"maxdiff={max_field_diff}"
        ),
    )

    require(
        exact_nonempty,
        f"H1 nonempty-shell mismatch row={row_index}",
    )


    h1_replaced[
        row_index
    ] = field


    intrinsic_replay_rows.append({
        "row_index":
            int(row_index),

        "relative_path":
            str(
                v3.iloc[
                    row_index
                ][
                    "relative_path"
                ]
            ),

        "intrinsic_field_exact":
            bool(
                exact_field
            ),

        "intrinsic_field_max_abs_diff":
            max_field_diff,

        "nonempty_shell_exact":
            bool(
                exact_nonempty
            ),

        "foreground_pixels":
            int(
                foreground_pixels
            ),

        "centroid_x":
            float(
                cx
            ),

        "centroid_y":
            float(
                cy
            ),

        "max_foreground_radius_px":
            float(
                max_radius
            ),

        "mass_error":
            float(
                mass_error
            ),

        "conditional_normalization_error":
            float(
                norm_error
            ),
    })


require(
    np.array_equal(
        h1_field,
        h1_replaced,
    ),
    "Replacing the ten replayed H1 fields changed frozen H1 array",
)


print("=" * 96)
print("INTRINSIC s=1 FIELD REPLAY")
print("=" * 96)

print(
    "10/10 intrinsic fields exact: PASS"
)

print(
    "Maximum field difference:",
    max(
        r[
            "intrinsic_field_max_abs_diff"
        ]
        for r
        in intrinsic_replay_rows
    ),
)

print()


# =============================================================================
# 13. Exact I2 spectral reduction on H1 frozen vs replayed fields
# =============================================================================

intrinsic_bands_original = (
    i2.angular_band_fractions(
        h1_field
    )
)

intrinsic_bands_replayed = (
    i2.angular_band_fractions(
        h1_replaced
    )
)


intrinsic_band_exact = np.array_equal(
    intrinsic_bands_original.to_numpy(),
    intrinsic_bands_replayed.to_numpy(),
)


intrinsic_band_max_diff = float(
    np.max(
        np.abs(
            intrinsic_bands_original.to_numpy()
            - intrinsic_bands_replayed.to_numpy()
        )
    )
)


require(
    intrinsic_band_exact,
    (
        "Intrinsic band fractions changed after "
        f"s=1 replay; maxdiff={intrinsic_band_max_diff}"
    ),
)


print("=" * 96)
print("INTRINSIC BAND-FRACTION REPLAY")
print("=" * 96)

print(
    "Frozen H1 vs s=1 replay exact:",
    intrinsic_band_exact,
)

print(
    "Max absolute band-fraction diff:",
    intrinsic_band_max_diff,
)

print()


# =============================================================================
# 14. Per-sentinel audit table
# =============================================================================

pixel_df = pd.DataFrame(
    pixel_rows
)

intrinsic_df = pd.DataFrame(
    intrinsic_replay_rows
)


audit = pixel_df.merge(
    intrinsic_df,
    on=[
        "row_index",
        "relative_path",
    ],
    how="inner",
    validate="one_to_one",
)


for band in BANDS:

    audit[
        f"historical_raster_{band}"
    ] = hist_crop[
        audit[
            "row_index"
        ].to_numpy(
            dtype=int
        ),
        BANDS.index(
            band
        ),
    ]

    audit[
        f"replayed_raster_{band}"
    ] = observed_crop[
        audit[
            "row_index"
        ].to_numpy(
            dtype=int
        ),
        BANDS.index(
            band
        ),
    ]

    audit[
        f"raster_absdiff_{band}"
    ] = np.abs(
        audit[
            f"historical_raster_{band}"
        ]
        - audit[
            f"replayed_raster_{band}"
        ]
    )


AUDIT_CSV = (
    OUTDIR
    / "P2_R0_05K2_A2_s1_exact_replay.csv"
)


audit.to_csv(
    AUDIT_CSV,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


# =============================================================================
# 15. Metadata
# =============================================================================

REPORT_JSON = (
    OUTDIR
    / "P2_R0_05K2_A2_s1_exact_replay_report.json"
)


report = {
    "stage":
        "P2_R0_05K2_A2_S1_EXACT_REPLAY",

    "status":
        "PASS",

    "sentinels":
        10,

    "raster_execution_population":
        2300,

    "s_gt_1_images_loaded":
        False,

    "support_trajectory_computed":
        False,

    "source_sha256": {
        "RA14":
            EXPECTED[
                "RA14_SOURCE"
            ],

        "I2":
            EXPECTED[
                "I2_SOURCE"
            ],

        "H1":
            EXPECTED[
                "H1_SOURCE"
            ],

        "V3_manifest":
            EXPECTED[
                "V3_MANIFEST"
            ],

        "I2_per_image":
            EXPECTED[
                "I2_PER_IMAGE"
            ],

        "H1_field":
            EXPECTED[
                "H1_FIELD"
            ],
    },

    "raster": {
        "full_population_A_vs_B_exact":
            bool(
                raster_exact_all
            ),

        "full_population_max_abs_field_diff":
            raster_max_diff_all,

        "sentinel_field_exact":
            bool(
                raster_exact_10
            ),

        "sentinel_max_abs_field_diff":
            raster_max_diff_10,

        "historical_i2_max_abs_band_diff_all":
            hist_raster_max_all,

        "historical_i2_max_abs_band_diff_sentinels":
            hist_raster_max_10,

        "historical_i2_tolerance":
            RASTER_HISTORY_TOL,
    },

    "intrinsic": {
        "ten_fields_exact":
            bool(
                all(
                    x[
                        "intrinsic_field_exact"
                    ]
                    for x
                    in intrinsic_replay_rows
                )
            ),

        "max_abs_field_diff":
            float(
                max(
                    x[
                        "intrinsic_field_max_abs_diff"
                    ]
                    for x
                    in intrinsic_replay_rows
                )
            ),

        "band_fractions_exact":
            bool(
                intrinsic_band_exact
            ),

        "max_abs_band_fraction_diff":
            intrinsic_band_max_diff,
    },

    "anti_peeking": {
        "s_gt_1_descriptor_execution":
            False,

        "05k_support_trajectory_opened":
            False,

        "h1_h2_h3_tested":
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
# 16. Checksums
# =============================================================================

SUMS = (
    OUTDIR
    / "SHA256SUMS.txt"
)


with SUMS.open(
    "w",
    encoding="utf-8",
) as f:

    f.write(
        f"{sha256_file(AUDIT_CSV)}  "
        f"{AUDIT_CSV.name}\n"
    )

    f.write(
        f"{sha256_file(REPORT_JSON)}  "
        f"{REPORT_JSON.name}\n"
    )


# =============================================================================
# Final
# =============================================================================

print("=" * 96)
print("P2-R0-05K2-A2 — FINAL")
print("=" * 96)

print(
    "s=1 V3 pixel equality             : PASS"
)

print(
    "Raster field exact                : PASS"
)

print(
    "Raster historical fractions       : PASS"
)

print(
    "Intrinsic field exact             : PASS"
)

print(
    "Intrinsic band fractions exact    : PASS"
)

print()
print(
    "Raster max field diff:",
    raster_max_diff_all,
)

print(
    "Raster max historical band diff "
    "(10):",
    hist_raster_max_10,
)

print(
    "Intrinsic max field diff:",
    report[
        "intrinsic"
    ][
        "max_abs_field_diff"
    ],
)

print(
    "Intrinsic max band diff:",
    intrinsic_band_max_diff,
)

print()
print(
    "Audit CSV:",
    AUDIT_CSV,
)

print(
    "Audit CSV SHA256:",
    sha256_file(
        AUDIT_CSV
    ),
)

print(
    "Report:",
    REPORT_JSON,
)

print(
    "Report SHA256:",
    sha256_file(
        REPORT_JSON
    ),
)

print(
    "SHA256SUMS:",
    sha256_file(
        SUMS
    ),
)

print()
print("s>1 images loaded            : NO")
print("Support trajectory opened    : NO")
print("Hypotheses tested            : NO")

print()
print("=" * 96)
print("05K2-A2 s=1 EXACT REPLAY: PASS")
print("STOP — DO NOT RUN s>1 YET")
print("=" * 96)