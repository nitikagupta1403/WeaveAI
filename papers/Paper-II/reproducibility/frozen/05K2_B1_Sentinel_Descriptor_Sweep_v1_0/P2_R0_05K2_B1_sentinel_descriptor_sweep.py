from pathlib import Path
import hashlib
import importlib.util
import json

import numpy as np
import pandas as pd
from PIL import Image


# =============================================================================
# P2-R0-05K2-B1
# SENTINEL SUPPORT SWEEP — DESCRIPTOR EXECUTION + CONTROL DIAGNOSTICS ONLY
#
# 10 sentinels × 7 frozen support levels = 70 conditions.
#
# ALLOWED HERE
#   - exact frozen raster-relative descriptor replay
#   - exact frozen intrinsic/object-relative descriptor replay
#   - exact frozen band-fraction reduction
#   - raw descriptor outputs
#   - raw band fractions
#   - numerical invariance diagnostics
#   - provenance/integrity checks
#
# NOT ALLOWED HERE
#   - directional hypothesis verdicts
#   - monotonicity conclusions
#   - dose-response slopes
#   - materiality decision at 3x
#   - inferential statistics
#   - manuscript/mechanism conclusions
# =============================================================================


REPO = Path(
    "/Users/nitikagupta/Research/WeaveAI"
)

AUDIT_ROOT = (
    REPO
    / "papers/Paper-II/reproducibility/audits"
)

FROZEN_ROOT = (
    REPO
    / "papers/Paper-II/reproducibility/frozen"
)

OUTDIR = (
    AUDIT_ROOT
    / "05K2_B1_sentinel_descriptor_sweep"
)

OUTDIR.mkdir(
    parents=True,
    exist_ok=True,
)


# =============================================================================
# Frozen implementation sources
# =============================================================================

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


EXPECTED_SOURCE_SHA = {
    "RA14":
        "3b3dad8315616b4c8a0013cdcb4c3258b243b8fc2722b366ecc8a0e8743fdca9",

    "I2":
        "802325ae23b3896bd0bf51bed49fd0bf5218583d73f76d1bae69f6f70e9fa3e3",

    "H1":
        "1ce3c0dd7f34e75c806777bff9c5142814f179a0b6fef48f927fbfeb1b4d1642",
}


# =============================================================================
# Frozen A2 gate
# =============================================================================

A2_ROOT = (
    FROZEN_ROOT
    / "05K2_A2_S1_Exact_Replay_v1_0"
)

A2_REPORT = (
    A2_ROOT
    / "P2_R0_05K2_A2_s1_exact_replay_report.json"
)


# =============================================================================
# Frozen 05K1 materialization
# =============================================================================

MAT_ROOT = (
    FROZEN_ROOT
    / "05K1_Sentinel_Materialization_v1_0"
)

MAT_MANIFEST = (
    MAT_ROOT
    / "P2_R0_05K1_sentinel_materialization_integrity.csv"
)


# =============================================================================
# Historical V3 population
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

EXPECTED_V3_MANIFEST_SHA = (
    "19ab60c21c71de7918472142c36174ded9f8fae888eeb3320983ca2cc66a545e"
)


# =============================================================================
# Historical H1 field
# =============================================================================

H1_ARTIFACT_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05h_intrinsic_coordinate"
)

EXPECTED_H1_FIELD_SHA = (
    "aaa69c8a6a416979dc037ae6c0197d5c62f1959eb41cc0482c8b5a3bdde21c03"
)


# =============================================================================
# Frozen conditions
# =============================================================================

SUPPORT_LEVELS = [
    1.00,
    1.10,
    1.25,
    1.50,
    2.00,
    2.50,
    3.00,
]

BANDS = [
    "low_1_4",
    "mid_5_12",
    "highmid_13_24",
    "high_25_36",
]

EXPECTED_ROWS = 2300
EXPECTED_SENTINELS = 10
EXPECTED_CONDITIONS = 70


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
        f"Unable to import {path}",
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
        im.load()

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
            f"Expected exactly one artifact SHA={expected_sha}; "
            f"found {len(hits)}:\n"
            + "\n".join(
                str(x)
                for x in hits
            )
        ),
    )

    return hits[0]


def first_existing_column(
    df,
    candidates,
    label,
):

    for c in candidates:
        if c in df.columns:
            return c

    raise RuntimeError(
        f"Could not resolve {label}. "
        f"Candidates={candidates}; "
        f"columns={df.columns.tolist()}"
    )


def resolve_canvas_path(
    mat_root,
    record,
):

    # First use an explicitly stored path if available.
    for col in [
        "output_path",
        "saved_path",
        "canvas_path",
        "materialized_path",
    ]:

        if col not in record.index:
            continue

        raw = str(
            record[col]
        ).strip()

        if not raw:
            continue

        p = Path(raw)

        if p.is_file():
            return p

        q = mat_root / p

        if q.is_file():
            return q


    # Otherwise use output_relative_path.
    if "output_relative_path" in record.index:

        rel = Path(
            str(
                record[
                    "output_relative_path"
                ]
            )
        )

        direct = (
            mat_root
            / rel
        )

        if direct.is_file():
            return direct


        if "role" in record.index:

            role = str(
                record[
                    "role"
                ]
            )

            by_role = (
                mat_root
                / "canvases"
                / role
                / rel.name
            )

            if by_role.is_file():
                return by_role


    # Final deterministic filename search.
    role = str(
        record[
            "role"
        ]
    )

    factor = float(
        record[
            "_support_factor"
        ]
    )

    candidates = []

    role_root = (
        mat_root
        / "canvases"
        / role
    )

    if role_root.is_dir():

        for p in sorted(
            role_root.glob("*.png")
        ):

            name = p.name.lower()

            tokens = [
                f"{factor:.2f}",
                str(factor),
                f"{factor:g}",
            ]

            if any(
                token in name
                for token in tokens
            ):
                candidates.append(
                    p
                )

    require(
        len(candidates) == 1,
        (
            f"Could not uniquely resolve canvas "
            f"role={role}, factor={factor}; "
            f"found={candidates}"
        ),
    )

    return candidates[0]


# =============================================================================
# Header
# =============================================================================

print("=" * 104)
print(
    "P2-R0-05K2-B1 — "
    "SENTINEL SUPPORT SWEEP / DESCRIPTORS ONLY"
)
print("=" * 104)

print(
    "Support levels opened          :",
    SUPPORT_LEVELS,
)

print(
    "Directional hypotheses tested : NO"
)

print(
    "Monotonicity evaluated         : NO"
)

print(
    "Materiality decision           : NO"
)

print(
    "Inferential statistics         : NO"
)

print()


# =============================================================================
# 1. Verify prerequisite A2 gate
# =============================================================================

require(
    A2_REPORT.is_file(),
    f"Frozen A2 report missing: {A2_REPORT}",
)

a2 = json.loads(
    A2_REPORT.read_text(
        encoding="utf-8"
    )
)

require(
    a2.get("status") == "PASS",
    "Frozen A2 report is not PASS",
)

require(
    a2.get(
        "s_gt_1_images_loaded"
    ) is False,
    "A2 anti-peeking state invalid",
)

require(
    a2.get(
        "support_trajectory_computed"
    ) is False,
    "A2 trajectory state invalid",
)

print(
    "Frozen A2 baseline gate: PASS"
)


# =============================================================================
# 2. Verify implementation anchors
# =============================================================================

for label, path in [
    ("RA14", RA14_SOURCE),
    ("I2", I2_SOURCE),
    ("H1", H1_SOURCE),
]:

    require(
        path.is_file(),
        f"{label} source missing: {path}",
    )

    observed = sha256_file(
        path
    )

    expected = EXPECTED_SOURCE_SHA[
        label
    ]

    require(
        observed == expected,
        (
            f"{label} source SHA mismatch\n"
            f"observed={observed}\n"
            f"expected={expected}"
        ),
    )

    print(
        f"{label} source SHA: PASS"
    )


require(
    V3_MANIFEST.is_file(),
    f"V3 manifest missing: {V3_MANIFEST}",
)

require(
    sha256_file(
        V3_MANIFEST
    )
    == EXPECTED_V3_MANIFEST_SHA,
    "V3 manifest SHA mismatch",
)

print(
    "V3 manifest SHA: PASS"
)


# =============================================================================
# 3. Load exact implementations
# =============================================================================

ra14 = load_module(
    "p2_05k2_b1_ra14",
    RA14_SOURCE,
)

i2 = load_module(
    "p2_05k2_b1_i2",
    I2_SOURCE,
)

h1 = load_module(
    "p2_05k2_b1_h1",
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
# 4. Load V3 population
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
    len(v3) == EXPECTED_ROWS,
    (
        f"Expected {EXPECTED_ROWS} V3 rows, "
        f"got {len(v3)}"
    ),
)

require(
    np.array_equal(
        v3[
            "row_index"
        ].astype(
            int
        ).to_numpy(),
        np.arange(
            EXPECTED_ROWS
        ),
    ),
    "V3 row order is not exact 0..2299",
)


base_rows = []


for _, rec in v3.iterrows():

    rel = str(
        rec[
            "relative_path"
        ]
    )

    path = (
        V3_ROOT
        / str(
            rec[
                "output_relative_path"
            ]
        )
    )

    require(
        path.is_file(),
        f"Missing V3 image: {path}",
    )

    base_rows.append({
        "relative_path":
            rel,

        "category":
            Path(
                rel
            ).parts[0],

        "path":
            path,
    })


# =============================================================================
# 5. Load and normalize frozen 05K1 materialization manifest
# =============================================================================

require(
    MAT_MANIFEST.is_file(),
    (
        "Frozen materialization manifest missing: "
        f"{MAT_MANIFEST}"
    ),
)

mat = pd.read_csv(
    MAT_MANIFEST,
    keep_default_na=False,
)


factor_col = first_existing_column(
    mat,
    [
        "nominal_support_factor",
        "support_factor",
        "requested_support_factor",
        "nominal_s",
        "s",
    ],
    "support factor column",
)


mat[
    "_support_factor"
] = mat[
    factor_col
].astype(
    float
)


require(
    len(mat)
    == EXPECTED_CONDITIONS,
    (
        f"Expected {EXPECTED_CONDITIONS} "
        f"materialized conditions, got {len(mat)}"
    ),
)

require(
    "row_index"
    in mat.columns,
    "Materialization manifest lacks row_index",
)

require(
    "role"
    in mat.columns,
    "Materialization manifest lacks role",
)


observed_levels = sorted(
    mat[
        "_support_factor"
    ].unique()
)


require(
    len(
        observed_levels
    )
    == len(
        SUPPORT_LEVELS
    ),
    (
        "Unexpected support-level count: "
        f"{observed_levels}"
    ),
)


for expected in SUPPORT_LEVELS:

    require(
        np.any(
            np.isclose(
                observed_levels,
                expected,
                atol=1e-12,
                rtol=0.0,
            )
        ),
        (
            f"Missing support level "
            f"{expected}"
        ),
    )


require(
    mat[
        "role"
    ].nunique()
    == EXPECTED_SENTINELS,
    "Expected exactly ten sentinel roles",
)


condition_rows = []


for idx, rec in mat.iterrows():

    path = resolve_canvas_path(
        MAT_ROOT,
        rec,
    )

    require(
        path.is_file(),
        f"Canvas missing: {path}",
    )


    observed_png_sha = sha256_file(
        path
    )


    sha_col = None

    for candidate in [
        "saved_png_sha256",
        "output_png_sha256",
        "png_sha256",
        "file_sha256",
    ]:

        if candidate in mat.columns:
            sha_col = candidate
            break


    if sha_col is not None:

        expected_png_sha = str(
            rec[
                sha_col
            ]
        )

        require(
            observed_png_sha
            == expected_png_sha,
            (
                f"PNG SHA mismatch: "
                f"{path}"
            ),
        )


    gray = load_gray(
        path
    )


    condition_rows.append({
        "manifest_index":
            int(
                idx
            ),

        "role":
            str(
                rec[
                    "role"
                ]
            ),

        "row_index":
            int(
                rec[
                    "row_index"
                ]
            ),

        "relative_path":
            str(
                v3.iloc[
                    int(
                        rec[
                            "row_index"
                        ]
                    )
                ][
                    "relative_path"
                ]
            ),

        "support_factor":
            float(
                rec[
                    "_support_factor"
                ]
            ),

        "canvas_path":
            str(
                path
            ),

        "canvas_png_sha256":
            observed_png_sha,

        "canvas_pixel_sha256":
            sha256_array(
                gray
            ),

        "canvas_height":
            int(
                gray.shape[
                    0
                ]
            ),

        "canvas_width":
            int(
                gray.shape[
                    1
                ]
            ),
    })


conditions = pd.DataFrame(
    condition_rows
)


require(
    len(
        conditions
    )
    == EXPECTED_CONDITIONS,
    "Condition resolution failed",
)


counts = conditions.groupby(
    "support_factor"
).size()


require(
    np.all(
        counts.to_numpy()
        == EXPECTED_SENTINELS
    ),
    (
        "Each support level must contain "
        "exactly ten conditions"
    ),
)


print(
    "Frozen 05K1 conditions resolved: PASS"
)

print(
    "Conditions:",
    len(
        conditions
    ),
)

print()


# =============================================================================
# 6. Locate and validate historical H1 field
# =============================================================================

H1_FIELD_NPZ = locate_by_sha(
    H1_ARTIFACT_ROOT,
    EXPECTED_H1_FIELD_SHA,
    suffix=".npz",
)


artifact = np.load(
    H1_FIELD_NPZ,
    allow_pickle=False,
)


required_h1_keys = {
    "conditional_angular",
    "nonempty_shells",
    "radial_centers",
    "relative_paths",
    "categories",
    "representation_name",
}


require(
    required_h1_keys.issubset(
        set(
            artifact.files
        )
    ),
    "Historical H1 NPZ missing arrays",
)


h1_base_field = np.asarray(
    artifact[
        "conditional_angular"
    ],
    dtype=np.float64,
)


h1_base_paths = np.asarray(
    artifact[
        "relative_paths"
    ],
    dtype=str,
)


require(
    h1_base_field.shape
    == (
        EXPECTED_ROWS,
        72,
        72,
    ),
    (
        "Unexpected historical H1 shape: "
        f"{h1_base_field.shape}"
    ),
)


require(
    np.array_equal(
        h1_base_paths,
        v3[
            "relative_path"
        ].astype(
            str
        ).to_numpy(),
    ),
    "H1/V3 population order mismatch",
)


# =============================================================================
# 7. Allocate B1 result storage
# =============================================================================

# 70 condition fields, indexed in deterministic order.
conditions = conditions.sort_values(
    [
        "support_factor",
        "role",
    ]
).reset_index(
    drop=True
)


raster_fields = np.zeros(
    (
        EXPECTED_CONDITIONS,
        72,
        72,
    ),
    dtype=np.float64,
)


intrinsic_fields = np.zeros_like(
    raster_fields
)


raster_band_rows = []

intrinsic_band_rows = []

intrinsic_geometry_rows = []

execution_rows = []


# =============================================================================
# 8. Execute each support level
#
# RA14:
#   full 2300 population per level.
#
# Intrinsic:
#   exact H1 construction for each of the 10 condition canvases,
#   then insert those 10 fields into frozen 2300 H1 population before
#   calling exact I2 spectral reducer.
# =============================================================================

for level in SUPPORT_LEVELS:

    print()
    print("=" * 104)
    print(
        f"SUPPORT LEVEL s={level:.2f}"
    )
    print("=" * 104)


    level_mask = np.isclose(
        conditions[
            "support_factor"
        ].to_numpy(
            dtype=float
        ),
        level,
        atol=1e-12,
        rtol=0.0,
    )


    level_conditions = conditions.loc[
        level_mask
    ].copy()


    require(
        len(
            level_conditions
        )
        == EXPECTED_SENTINELS,
        (
            f"s={level}: expected ten "
            f"conditions"
        ),
    )


    # -------------------------------------------------------------------------
    # A. Raster-relative population
    # -------------------------------------------------------------------------

    raster_rows = [
        dict(
            row
        )
        for row
        in base_rows
    ]


    for condition_index, rec in (
        level_conditions.iterrows()
    ):

        row_index = int(
            rec[
                "row_index"
            ]
        )

        canvas_path = Path(
            rec[
                "canvas_path"
            ]
        )

        raster_rows[
            row_index
        ][
            "path"
        ] = canvas_path


    print(
        "RA14 full-population reconstruction..."
    )


    (
        raster_population,
        raster_nonempty,
        raster_radial_centers,
        raster_mass_error,
        raster_norm_error,
    ) = ra14.recover_geometry(
        raster_rows
    )


    raster_population = np.asarray(
        raster_population,
        dtype=np.float64,
    )


    require(
        raster_population.shape
        == (
            EXPECTED_ROWS,
            72,
            72,
        ),
        (
            f"s={level}: unexpected "
            f"RA14 field shape "
            f"{raster_population.shape}"
        ),
    )


    raster_bands_population = (
        i2.angular_band_fractions(
            raster_population
        )
    )


    require(
        list(
            raster_bands_population.columns
        )
        == BANDS,
        "Unexpected raster band columns",
    )


    # -------------------------------------------------------------------------
    # B. Object-relative exact H1 fields
    # -------------------------------------------------------------------------

    intrinsic_population = (
        h1_base_field.copy()
    )


    for condition_index, rec in (
        level_conditions.iterrows()
    ):

        row_index = int(
            rec[
                "row_index"
            ]
        )

        canvas_path = Path(
            rec[
                "canvas_path"
            ]
        )

        gray = load_gray(
            canvas_path
        )


        mask = h1.diagnostic_ink_mask(
            gray
        )


        (
            intrinsic_field,
            intrinsic_nonempty,
            cx,
            cy,
            max_radius,
            foreground_pixels,
            intrinsic_mass_error,
            intrinsic_norm_error,
        ) = h1.intrinsic_field_from_mask(
            mask
        )


        intrinsic_field = np.asarray(
            intrinsic_field,
            dtype=np.float64,
        )


        require(
            intrinsic_field.shape
            == (
                72,
                72,
            ),
            (
                f"{rec['role']} s={level}: "
                "intrinsic field shape invalid"
            ),
        )


        intrinsic_population[
            row_index
        ] = intrinsic_field


        raster_fields[
            condition_index
        ] = raster_population[
            row_index
        ]


        intrinsic_fields[
            condition_index
        ] = intrinsic_field


        intrinsic_geometry_rows.append({
            "condition_index":
                int(
                    condition_index
                ),

            "role":
                str(
                    rec[
                        "role"
                    ]
                ),

            "row_index":
                row_index,

            "relative_path":
                str(
                    rec[
                        "relative_path"
                    ]
                ),

            "support_factor":
                float(
                    level
                ),

            "foreground_pixels":
                int(
                    foreground_pixels
                ),

            "centroid_x_px":
                float(
                    cx
                ),

            "centroid_y_px":
                float(
                    cy
                ),

            "max_foreground_radius_px":
                float(
                    max_radius
                ),

            "nonempty_radial_shells":
                int(
                    np.sum(
                        intrinsic_nonempty
                    )
                ),

            "mass_error":
                float(
                    intrinsic_mass_error
                ),

            "conditional_normalization_error":
                float(
                    intrinsic_norm_error
                ),
        })


    intrinsic_bands_population = (
        i2.angular_band_fractions(
            intrinsic_population
        )
    )


    require(
        list(
            intrinsic_bands_population.columns
        )
        == BANDS,
        "Unexpected intrinsic band columns",
    )


    # -------------------------------------------------------------------------
    # C. Extract only the 10 sentinel conditions
    # -------------------------------------------------------------------------

    for condition_index, rec in (
        level_conditions.iterrows()
    ):

        row_index = int(
            rec[
                "row_index"
            ]
        )


        raster_record = {
            "condition_index":
                int(
                    condition_index
                ),

            "role":
                str(
                    rec[
                        "role"
                    ]
                ),

            "row_index":
                row_index,

            "relative_path":
                str(
                    rec[
                        "relative_path"
                    ]
                ),

            "support_factor":
                float(
                    level
                ),
        }


        intrinsic_record = dict(
            raster_record
        )


        for band in BANDS:

            raster_record[
                band
            ] = float(
                raster_bands_population.iloc[
                    row_index
                ][
                    band
                ]
            )


            intrinsic_record[
                band
            ] = float(
                intrinsic_bands_population.iloc[
                    row_index
                ][
                    band
                ]
            )


        raster_band_rows.append(
            raster_record
        )

        intrinsic_band_rows.append(
            intrinsic_record
        )


    execution_rows.append({
        "support_factor":
            float(
                level
            ),

        "conditions":
            int(
                len(
                    level_conditions
                )
            ),

        "raster_population_rows":
            EXPECTED_ROWS,

        "raster_mass_error":
            float(
                raster_mass_error
            ),

        "raster_conditional_normalization_error":
            float(
                raster_norm_error
            ),

        "raster_radial_centers_sha256":
            sha256_array(
                np.asarray(
                    raster_radial_centers,
                    dtype=np.float64,
                )
            ),
    })


# =============================================================================
# 9. Assemble raw descriptor/band outputs
# =============================================================================

raster_bands_df = pd.DataFrame(
    raster_band_rows
).sort_values(
    "condition_index"
).reset_index(
    drop=True
)


intrinsic_bands_df = pd.DataFrame(
    intrinsic_band_rows
).sort_values(
    "condition_index"
).reset_index(
    drop=True
)


intrinsic_geometry_df = pd.DataFrame(
    intrinsic_geometry_rows
).sort_values(
    "condition_index"
).reset_index(
    drop=True
)


execution_df = pd.DataFrame(
    execution_rows
)


require(
    len(
        raster_bands_df
    )
    == EXPECTED_CONDITIONS,
    "Raster band result count != 70",
)

require(
    len(
        intrinsic_bands_df
    )
    == EXPECTED_CONDITIONS,
    "Intrinsic band result count != 70",
)

require(
    len(
        intrinsic_geometry_df
    )
    == EXPECTED_CONDITIONS,
    "Intrinsic geometry count != 70",
)


for df, label in [
    (
        raster_bands_df,
        "raster",
    ),
    (
        intrinsic_bands_df,
        "intrinsic",
    ),
]:

    fraction_sum = (
        df[
            BANDS
        ]
        .sum(
            axis=1
        )
        .to_numpy(
            dtype=float
        )
    )

    require(
        np.allclose(
            fraction_sum,
            1.0,
            atol=1e-12,
            rtol=0.0,
        ),
        (
            f"{label} band fractions "
            "do not sum to one"
        ),
    )


# =============================================================================
# 10. Numerical controls only
#
# No direction/monotonicity interpretation.
# =============================================================================

control_rows = []


for role, group in (
    conditions.groupby(
        "role",
        sort=True,
    )
):

    group = group.sort_values(
        "support_factor"
    )


    baseline_rows = group.loc[
        np.isclose(
            group[
                "support_factor"
            ].to_numpy(
                dtype=float
            ),
            1.0,
            atol=1e-12,
            rtol=0.0,
        )
    ]


    require(
        len(
            baseline_rows
        )
        == 1,
        (
            f"{role}: no unique "
            "s=1 baseline"
        ),
    )


    baseline_index = int(
        baseline_rows.index[
            0
        ]
    )


    raster_base = raster_fields[
        baseline_index
    ]


    intrinsic_base = intrinsic_fields[
        baseline_index
    ]


    raster_band_base = (
        raster_bands_df.loc[
            raster_bands_df[
                "condition_index"
            ]
            == baseline_index,
            BANDS,
        ]
        .iloc[
            0
        ]
        .to_numpy(
            dtype=float
        )
    )


    intrinsic_band_base = (
        intrinsic_bands_df.loc[
            intrinsic_bands_df[
                "condition_index"
            ]
            == baseline_index,
            BANDS,
        ]
        .iloc[
            0
        ]
        .to_numpy(
            dtype=float
        )
    )


    for condition_index in group.index:

        condition_index = int(
            condition_index
        )


        level = float(
            conditions.loc[
                condition_index,
                "support_factor",
            ]
        )


        raster_field_diff = np.abs(
            raster_fields[
                condition_index
            ]
            - raster_base
        )


        intrinsic_field_diff = np.abs(
            intrinsic_fields[
                condition_index
            ]
            - intrinsic_base
        )


        raster_band_vec = (
            raster_bands_df.loc[
                raster_bands_df[
                    "condition_index"
                ]
                == condition_index,
                BANDS,
            ]
            .iloc[
                0
            ]
            .to_numpy(
                dtype=float
            )
        )


        intrinsic_band_vec = (
            intrinsic_bands_df.loc[
                intrinsic_bands_df[
                    "condition_index"
                ]
                == condition_index,
                BANDS,
            ]
            .iloc[
                0
            ]
            .to_numpy(
                dtype=float
            )
        )


        control_rows.append({
            "condition_index":
                condition_index,

            "role":
                role,

            "support_factor":
                level,

            "raster_field_max_abs_diff_from_s1":
                float(
                    np.max(
                        raster_field_diff
                    )
                ),

            "raster_field_l2_from_s1":
                float(
                    np.linalg.norm(
                        raster_fields[
                            condition_index
                        ]
                        - raster_base
                    )
                ),

            "raster_band_max_abs_diff_from_s1":
                float(
                    np.max(
                        np.abs(
                            raster_band_vec
                            - raster_band_base
                        )
                    )
                ),

            "raster_band_l1_from_s1":
                float(
                    np.sum(
                        np.abs(
                            raster_band_vec
                            - raster_band_base
                        )
                    )
                ),

            "intrinsic_field_exact_vs_s1":
                bool(
                    np.array_equal(
                        intrinsic_fields[
                            condition_index
                        ],
                        intrinsic_base,
                    )
                ),

            "intrinsic_field_max_abs_diff_from_s1":
                float(
                    np.max(
                        intrinsic_field_diff
                    )
                ),

            "intrinsic_field_l2_from_s1":
                float(
                    np.linalg.norm(
                        intrinsic_fields[
                            condition_index
                        ]
                        - intrinsic_base
                    )
                ),

            "intrinsic_band_exact_vs_s1":
                bool(
                    np.array_equal(
                        intrinsic_band_vec,
                        intrinsic_band_base,
                    )
                ),

            "intrinsic_band_max_abs_diff_from_s1":
                float(
                    np.max(
                        np.abs(
                            intrinsic_band_vec
                            - intrinsic_band_base
                        )
                    )
                ),

            "intrinsic_band_l1_from_s1":
                float(
                    np.sum(
                        np.abs(
                            intrinsic_band_vec
                            - intrinsic_band_base
                        )
                    )
                ),
        })


controls_df = pd.DataFrame(
    control_rows
).sort_values(
    "condition_index"
).reset_index(
    drop=True
)


require(
    len(
        controls_df
    )
    == EXPECTED_CONDITIONS,
    "Control diagnostic rows != 70",
)


# =============================================================================
# 11. s=1 regression gate carried forward from A2
# =============================================================================

s1_controls = controls_df.loc[
    np.isclose(
        controls_df[
            "support_factor"
        ].to_numpy(
            dtype=float
        ),
        1.0,
        atol=1e-12,
        rtol=0.0,
    )
]


require(
    len(
        s1_controls
    )
    == EXPECTED_SENTINELS,
    "Expected ten s=1 controls",
)


require(
    np.all(
        s1_controls[
            "raster_field_max_abs_diff_from_s1"
        ].to_numpy(
            dtype=float
        )
        == 0.0
    ),
    "Raster s=1 self-control failure",
)


require(
    np.all(
        s1_controls[
            "intrinsic_field_max_abs_diff_from_s1"
        ].to_numpy(
            dtype=float
        )
        == 0.0
    ),
    "Intrinsic s=1 self-control failure",
)


# =============================================================================
# 12. Save raw descriptor fields
# =============================================================================

RASTER_NPZ = (
    OUTDIR
    / "P2_R0_05K2_B1_raster_fields_70.npz"
)

INTRINSIC_NPZ = (
    OUTDIR
    / "P2_R0_05K2_B1_intrinsic_fields_70.npz"
)


np.savez_compressed(
    RASTER_NPZ,

    fields=
        raster_fields,

    condition_index=
        conditions.index.to_numpy(
            dtype=int
        ),

    roles=
        conditions[
            "role"
        ].astype(
            str
        ).to_numpy(),

    row_indices=
        conditions[
            "row_index"
        ].astype(
            int
        ).to_numpy(),

    relative_paths=
        conditions[
            "relative_path"
        ].astype(
            str
        ).to_numpy(),

    support_factors=
        conditions[
            "support_factor"
        ].to_numpy(
            dtype=float
        ),
)


np.savez_compressed(
    INTRINSIC_NPZ,

    fields=
        intrinsic_fields,

    condition_index=
        conditions.index.to_numpy(
            dtype=int
        ),

    roles=
        conditions[
            "role"
        ].astype(
            str
        ).to_numpy(),

    row_indices=
        conditions[
            "row_index"
        ].astype(
            int
        ).to_numpy(),

    relative_paths=
        conditions[
            "relative_path"
        ].astype(
            str
        ).to_numpy(),

    support_factors=
        conditions[
            "support_factor"
        ].to_numpy(
            dtype=float
        ),
)


# =============================================================================
# 13. Save tables
# =============================================================================

CONDITIONS_CSV = (
    OUTDIR
    / "P2_R0_05K2_B1_conditions_70.csv"
)

RASTER_BANDS_CSV = (
    OUTDIR
    / "P2_R0_05K2_B1_raster_band_fractions_70.csv"
)

INTRINSIC_BANDS_CSV = (
    OUTDIR
    / "P2_R0_05K2_B1_intrinsic_band_fractions_70.csv"
)

INTRINSIC_GEOMETRY_CSV = (
    OUTDIR
    / "P2_R0_05K2_B1_intrinsic_geometry_70.csv"
)

CONTROLS_CSV = (
    OUTDIR
    / "P2_R0_05K2_B1_numerical_controls_70.csv"
)

EXECUTION_CSV = (
    OUTDIR
    / "P2_R0_05K2_B1_execution_by_support_level.csv"
)


for df, path in [
    (
        conditions,
        CONDITIONS_CSV,
    ),
    (
        raster_bands_df,
        RASTER_BANDS_CSV,
    ),
    (
        intrinsic_bands_df,
        INTRINSIC_BANDS_CSV,
    ),
    (
        intrinsic_geometry_df,
        INTRINSIC_GEOMETRY_CSV,
    ),
    (
        controls_df,
        CONTROLS_CSV,
    ),
    (
        execution_df,
        EXECUTION_CSV,
    ),
]:

    df.to_csv(
        path,
        index=False,
        lineterminator="\n",
        float_format="%.17g",
    )


# =============================================================================
# 14. Descriptive numerical summary
#
# Still no directional evaluation.
# =============================================================================

intrinsic_field_max = float(
    controls_df[
        "intrinsic_field_max_abs_diff_from_s1"
    ].max()
)

intrinsic_band_max = float(
    controls_df[
        "intrinsic_band_max_abs_diff_from_s1"
    ].max()
)

raster_field_max = float(
    controls_df[
        "raster_field_max_abs_diff_from_s1"
    ].max()
)

raster_band_max = float(
    controls_df[
        "raster_band_max_abs_diff_from_s1"
    ].max()
)


intrinsic_exact_field_count = int(
    controls_df[
        "intrinsic_field_exact_vs_s1"
    ].sum()
)

intrinsic_exact_band_count = int(
    controls_df[
        "intrinsic_band_exact_vs_s1"
    ].sum()
)


# =============================================================================
# 15. Report
# =============================================================================

REPORT_JSON = (
    OUTDIR
    / "P2_R0_05K2_B1_report.json"
)


report = {
    "stage":
        "P2_R0_05K2_B1_SENTINEL_DESCRIPTOR_SWEEP",

    "status":
        "COMPLETE_DESCRIPTOR_EXECUTION_ONLY",

    "conditions":
        EXPECTED_CONDITIONS,

    "sentinels":
        EXPECTED_SENTINELS,

    "support_levels":
        SUPPORT_LEVELS,

    "implementation_sha256": {
        "RA14":
            EXPECTED_SOURCE_SHA[
                "RA14"
            ],

        "I2":
            EXPECTED_SOURCE_SHA[
                "I2"
            ],

        "H1":
            EXPECTED_SOURCE_SHA[
                "H1"
            ],

        "V3_manifest":
            EXPECTED_V3_MANIFEST_SHA,

        "H1_field":
            EXPECTED_H1_FIELD_SHA,
    },

    "execution": {
        "raster_full_population_runs":
            len(
                SUPPORT_LEVELS
            ),

        "raster_population_rows_per_run":
            EXPECTED_ROWS,

        "raster_total_population_rows_processed":
            EXPECTED_ROWS
            * len(
                SUPPORT_LEVELS
            ),

        "sentinel_conditions":
            EXPECTED_CONDITIONS,
    },

    "numerical_controls": {
        "raster_field_max_abs_diff_from_s1_any_condition":
            raster_field_max,

        "raster_band_max_abs_diff_from_s1_any_condition":
            raster_band_max,

        "intrinsic_field_exact_vs_s1_count":
            intrinsic_exact_field_count,

        "intrinsic_field_max_abs_diff_from_s1_any_condition":
            intrinsic_field_max,

        "intrinsic_band_exact_vs_s1_count":
            intrinsic_exact_band_count,

        "intrinsic_band_max_abs_diff_from_s1_any_condition":
            intrinsic_band_max,
    },

    "analysis_boundary": {
        "directional_hypotheses_tested":
            False,

        "monotonicity_evaluated":
            False,

        "dose_response_model_fit":
            False,

        "materiality_threshold_applied":
            False,

        "inferential_statistics_run":
            False,

        "mechanism_conclusion_made":
            False,
    },

    "interpretation_boundary":
        (
            "P2-R0-05K2-B1 executes the frozen raster-relative and "
            "object-relative descriptor systems over the 70 preregistered "
            "sentinel support conditions and records numerical controls. "
            "It does not evaluate directional hypotheses, monotonicity, "
            "materiality, statistical significance, or mechanism."
        ),
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

OUTPUTS = [
    CONDITIONS_CSV,
    RASTER_BANDS_CSV,
    INTRINSIC_BANDS_CSV,
    INTRINSIC_GEOMETRY_CSV,
    CONTROLS_CSV,
    EXECUTION_CSV,
    RASTER_NPZ,
    INTRINSIC_NPZ,
    REPORT_JSON,
]


SUMS = (
    OUTDIR
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
# 17. Final output
# =============================================================================

print()
print("=" * 104)
print("P2-R0-05K2-B1 — EXECUTION COMPLETE")
print("=" * 104)

print(
    "Conditions:",
    EXPECTED_CONDITIONS,
)

print(
    "Raster full-population runs:",
    len(
        SUPPORT_LEVELS
    ),
)

print(
    "Raster rows processed:",
    EXPECTED_ROWS
    * len(
        SUPPORT_LEVELS
    ),
)

print()

print(
    "Raster max field diff from s=1:",
    raster_field_max,
)

print(
    "Raster max band diff from s=1:",
    raster_band_max,
)

print()

print(
    "Intrinsic field exact-vs-s1 "
    "conditions:",
    f"{intrinsic_exact_field_count}/{EXPECTED_CONDITIONS}",
)

print(
    "Intrinsic max field diff from s=1:",
    intrinsic_field_max,
)

print(
    "Intrinsic band exact-vs-s1 "
    "conditions:",
    f"{intrinsic_exact_band_count}/{EXPECTED_CONDITIONS}",
)

print(
    "Intrinsic max band diff from s=1:",
    intrinsic_band_max,
)

print()

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
print(
    "Directional hypotheses tested : NO"
)

print(
    "Monotonicity evaluated         : NO"
)

print(
    "Materiality threshold applied  : NO"
)

print(
    "Inferential statistics         : NO"
)

print()
print("=" * 104)
print(
    "STOP — DESCRIPTORS RECORDED; "
    "DO NOT INTERPRET TRAJECTORIES YET"
)
print("=" * 104)