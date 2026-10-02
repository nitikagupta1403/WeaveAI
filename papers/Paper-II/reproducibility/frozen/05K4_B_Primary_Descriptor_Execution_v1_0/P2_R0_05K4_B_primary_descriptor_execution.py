from pathlib import Path
import hashlib
import json

import numpy as np
import pandas as pd
from PIL import Image


# =============================================================================
# P2-R0-05K4-B
# FULL-POPULATION PRIMARY DESCRIPTOR EXECUTION
#
# 2300 source images × 7 support levels = 16,100 conditions
#
# PURPOSE
#   Execute the frozen raster-relative RA14 representation and frozen
#   intrinsic/object-relative H1 representation over all primary support
#   conditions, followed by the frozen I2 angular-band reduction.
#
# THIS STAGE DOES:
#   - verify frozen provenance hashes
#   - execute raster-relative descriptor
#   - execute intrinsic/object-relative descriptor
#   - compute frozen four-band fractions
#   - verify s=1 raster replay against historical frozen I2 CROP fractions
#   - verify intrinsic exact invariance across all support levels
#   - record numerical controls
#
# THIS STAGE DOES NOT:
#   - inspect endpoint direction
#   - inspect monotonicity
#   - apply a materiality threshold
#   - perform inferential statistics
#   - issue a mechanism verdict
#
# IMPORTANT IMPLEMENTATION NOTE
#   Full 72×72 fields are evaluated in memory one condition at a time.
#   They are not accumulated into large NPZ archives in this primary run.
#   This avoids unnecessary RAM/disk expansion while preserving exact
#   reproducibility through frozen inputs + frozen implementations.
# =============================================================================


REPO = Path(
    "/Users/nitikagupta/Research/WeaveAI"
)

FROZEN = (
    REPO
    / "papers/Paper-II/reproducibility/frozen"
)

AUDITS = (
    REPO
    / "papers/Paper-II/reproducibility/audits"
)

OUT = (
    AUDITS
    / "05K4_B_primary_descriptor_execution"
)

OUT.mkdir(
    parents=True,
    exist_ok=True,
)


# =============================================================================
# Frozen 05K4-A primary materialization
# =============================================================================

A_DIR = (
    FROZEN
    / "05K4_A_Primary_Support_Materialization_v1_0"
)

INTEGRITY_CSV = (
    A_DIR
    / "P2_R0_05K4_A_integrity_16100.csv"
)

EXPECTED_INTEGRITY_SHA = (
    "235991a193f5164a3fed3b0f2074a192601f5148b6fcaddb8ea5dc81d2b4fa80"
)


CANVAS_ROOT = (
    AUDITS
    / "05K4_A_primary_support_materialization"
    / "canvases"
)


# =============================================================================
# Frozen descriptor implementations
# =============================================================================

RA14_SOURCE = Path(
    "/Users/nitikagupta/Research/WeaveAI/"
    "papers/CLO-SKET/Codes_paper_I/Experiment_08/"
    "extract_ra14_features.py"
)

I2_SOURCE = (
    AUDITS
    / "P2_R0_05I2_objective_real_garment_candidate_selection.py"
)

H1_SOURCE = (
    AUDITS
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
# Historical frozen I2 per-image band table
#
# Used ONLY for s=1 exact numerical replay validation.
# Not used to select, tune, or interpret primary outcomes.
# =============================================================================

I2_PER_IMAGE = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I2_per_image_band_fraction_change.csv"
)

EXPECTED_I2_PER_IMAGE_SHA = (
    "a9a096b4aafe89be79b5d3c35fd3e4dc4e6de046c30326f108d0cbe3601c39e2"
)


EXPECTED_IMAGES = 2300
EXPECTED_CONDITIONS = 16100

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
    dtype=np.float64,
)

BANDS = [
    "low_1_4",
    "mid_5_12",
    "highmid_13_24",
    "high_25_36",
]

I2_CROP_COLUMNS = [
    "crop_low_1_4_fraction",
    "crop_mid_5_12_fraction",
    "crop_highmid_13_24_fraction",
    "crop_high_25_36_fraction",
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


def load_gray_uint8(path):
    with Image.open(path) as im:
        arr = np.asarray(
            im.convert("L"),
            dtype=np.uint8,
        )

    require(
        arr.ndim == 2,
        f"Expected 2-D grayscale image: {path}",
    )

    return arr


# =============================================================================
# Frozen raster-relative RA14 representation
# =============================================================================

def recover_geometry_raster_relative(gray):

    img = np.asarray(
        gray,
        dtype=np.float64,
    )

    require(
        img.ndim == 2,
        "Expected 2-D grayscale image",
    )

    w = 255.0 - img
    w = np.maximum(
        w,
        0.0,
    )

    mass = float(
        w.sum()
    )

    require(
        mass > 0.0,
        "Zero darkness mass",
    )

    H, W = img.shape

    S = float(
        max(
            W,
            H,
        )
    )

    x = (
        np.arange(
            W,
            dtype=np.float64,
        )
        - (W - 1.0) / 2.0
    ) / S

    y = (
        np.arange(
            H,
            dtype=np.float64,
        )
        - (H - 1.0) / 2.0
    ) / S

    X, Y = np.meshgrid(
        x,
        y,
    )

    cx = float(
        (X * w).sum()
        / mass
    )

    cy = float(
        (Y * w).sum()
        / mass
    )

    Xc = X - cx
    Yc = Y - cy

    R = np.sqrt(
        Xc ** 2
        + Yc ** 2
    )

    Theta = np.arctan2(
        Yc,
        Xc,
    )

    # Historical raster-grid normalization.
    Rmax = float(
        np.max(
            R
        )
    )

    require(
        Rmax > 0.0,
        "Raster-grid Rmax is zero",
    )

    Rn = R / Rmax

    radial_edges = np.linspace(
        0.0,
        1.0,
        73,
        dtype=np.float64,
    )

    angular_edges = np.linspace(
        -np.pi,
        np.pi,
        73,
        dtype=np.float64,
    )

    joint, _, _ = np.histogram2d(
        Rn.ravel(),
        Theta.ravel(),
        bins=[
            radial_edges,
            angular_edges,
        ],
        weights=w.ravel(),
    )

    shell_mass = joint.sum(
        axis=1,
        keepdims=True,
    )

    field = np.divide(
        joint,
        shell_mass,
        out=np.zeros_like(
            joint,
            dtype=np.float64,
        ),
        where=shell_mass > 0.0,
    )

    return field


# =============================================================================
# Frozen H1 intrinsic/object-relative representation
# =============================================================================

def intrinsic_field_from_mask(gray):

    gray = np.asarray(
        gray,
        dtype=np.uint8,
    )

    mask = (
        gray < 250
    )

    yy, xx = np.nonzero(
        mask
    )

    require(
        len(xx) > 0,
        "No foreground under <250 mask",
    )

    xx = xx.astype(
        np.float64
    )

    yy = yy.astype(
        np.float64
    )

    cx = float(
        xx.mean()
    )

    cy = float(
        yy.mean()
    )

    dx = xx - cx
    dy = yy - cy

    radius = np.sqrt(
        dx ** 2
        + dy ** 2
    )

    scale = float(
        radius.max()
    )

    require(
        scale > 0.0,
        "Intrinsic max foreground radius is zero",
    )

    r_norm = radius / scale

    theta = np.arctan2(
        dy,
        dx,
    )

    radial_edges = np.linspace(
        0.0,
        1.0,
        73,
        dtype=np.float64,
    )

    angular_edges = np.linspace(
        -np.pi,
        np.pi,
        73,
        dtype=np.float64,
    )

    joint, _, _ = np.histogram2d(
        r_norm,
        theta,
        bins=[
            radial_edges,
            angular_edges,
        ],
    )

    shell_mass = joint.sum(
        axis=1,
        keepdims=True,
    )

    field = np.divide(
        joint,
        shell_mass,
        out=np.zeros_like(
            joint,
            dtype=np.float64,
        ),
        where=shell_mass > 0.0,
    )

    return field, cx, cy, scale


# =============================================================================
# Frozen I2 angular band reduction
# =============================================================================

def angular_band_fractions(field):

    F = np.fft.rfft(
        field,
        axis=1,
    )

    energy = (
        np.abs(F)
        ** 2
    )

    angular_energy = energy.sum(
        axis=0
    )

    denominator = float(
        angular_energy[
            1:37
        ].sum()
    )

    require(
        denominator > 0.0,
        "Zero non-DC angular energy",
    )

    values = np.asarray(
        [
            angular_energy[1:5].sum()
            / denominator,

            angular_energy[5:13].sum()
            / denominator,

            angular_energy[13:25].sum()
            / denominator,

            angular_energy[25:37].sum()
            / denominator,
        ],
        dtype=np.float64,
    )

    require(
        abs(
            float(
                values.sum()
            )
            - 1.0
        )
        <= 1e-12,
        "Band fractions do not sum to one",
    )

    return values


# =============================================================================
# Header
# =============================================================================

print("=" * 112)
print(
    "P2-R0-05K4-B — "
    "FULL-POPULATION PRIMARY DESCRIPTOR EXECUTION"
)
print("=" * 112)

print(
    "Source images expected :",
    EXPECTED_IMAGES,
)

print(
    "Conditions expected    :",
    EXPECTED_CONDITIONS,
)

print()
print("Directional analysis    : NO")
print("Monotonicity analysis   : NO")
print("Materiality threshold   : NO")
print("Population inference    : NO")
print("Mechanism verdict       : NO")
print()


# =============================================================================
# 1. Verify frozen provenance
# =============================================================================

require(
    INTEGRITY_CSV.is_file(),
    f"Missing frozen 05K4-A integrity table: {INTEGRITY_CSV}",
)

integrity_sha = sha256_file(
    INTEGRITY_CSV
)

print(
    "05K4-A integrity SHA:",
    integrity_sha,
    "PASS"
    if integrity_sha == EXPECTED_INTEGRITY_SHA
    else "FAIL",
)

require(
    integrity_sha
    == EXPECTED_INTEGRITY_SHA,
    "05K4-A integrity SHA mismatch",
)


for label, path in [
    ("RA14", RA14_SOURCE),
    ("I2", I2_SOURCE),
    ("H1", H1_SOURCE),
]:

    require(
        path.is_file(),
        f"Missing frozen source: {path}",
    )

    observed = sha256_file(
        path
    )

    expected = EXPECTED_SOURCE_SHA[
        label
    ]

    print(
        f"{label} source SHA:",
        observed,
        "PASS"
        if observed == expected
        else "FAIL",
    )

    require(
        observed == expected,
        f"{label} source SHA mismatch",
    )


require(
    I2_PER_IMAGE.is_file(),
    f"Missing historical I2 table: {I2_PER_IMAGE}",
)

i2_table_sha = sha256_file(
    I2_PER_IMAGE
)

print(
    "Historical I2 per-image SHA:",
    i2_table_sha,
    "PASS"
    if i2_table_sha == EXPECTED_I2_PER_IMAGE_SHA
    else "FAIL",
)

require(
    i2_table_sha
    == EXPECTED_I2_PER_IMAGE_SHA,
    "Historical I2 table SHA mismatch",
)


# =============================================================================
# 2. Load primary integrity universe + historical I2 replay target
# =============================================================================

integrity = pd.read_csv(
    INTEGRITY_CSV,
    keep_default_na=False,
)

i2 = pd.read_csv(
    I2_PER_IMAGE,
    keep_default_na=False,
)


require(
    len(integrity)
    == EXPECTED_CONDITIONS,
    "Primary integrity rows != 16100",
)

require(
    integrity[
        "row_index"
    ].nunique()
    == EXPECTED_IMAGES,
    "Primary integrity image count != 2300",
)

require(
    len(i2)
    == EXPECTED_IMAGES,
    "Historical I2 rows != 2300",
)


for c in [
    "row_index",
    "relative_path",
] + I2_CROP_COLUMNS:

    require(
        c in i2.columns,
        f"Historical I2 missing column: {c}",
    )


i2[
    "row_index"
] = i2[
    "row_index"
].astype(int)


i2_replay = (
    i2[
        [
            "row_index",
            "relative_path",
        ]
        + I2_CROP_COLUMNS
    ]
    .copy()
    .sort_values(
        "row_index",
        kind="mergesort",
    )
    .reset_index(
        drop=True
    )
)


require(
    i2_replay[
        "row_index"
    ].nunique()
    == EXPECTED_IMAGES,
    "Historical I2 row_index is not unique",
)


# =============================================================================
# 3. Execute one source image at a time
#
# We intentionally group the seven support levels of each source image
# together so s=1 fields can serve immediately as exact controls.
# =============================================================================

raster_records = []
intrinsic_records = []
geometry_records = []
control_records = []


raster_global_max_field_diff = 0.0
raster_global_max_band_diff = 0.0

intrinsic_global_max_field_diff = 0.0
intrinsic_global_max_band_diff = 0.0

intrinsic_exact_field_conditions = 0
intrinsic_exact_band_conditions = 0

s1_historical_max_band_diff = 0.0
s1_historical_exact_within_1e12 = 0


grouped = integrity.groupby(
    "row_index",
    sort=True,
)


for image_counter, (
    row_index,
    group,
) in enumerate(
    grouped,
    start=1,
):

    if (
        image_counter == 1
        or image_counter % 100 == 0
        or image_counter == EXPECTED_IMAGES
    ):

        print(
            f"Processing source image "
            f"{image_counter}/{EXPECTED_IMAGES}"
        )


    group = (
        group.sort_values(
            "support_factor",
            kind="mergesort",
        )
        .reset_index(
            drop=True
        )
    )


    observed_levels = group[
        "support_factor"
    ].to_numpy(
        dtype=float
    )


    require(
        np.allclose(
            observed_levels,
            SUPPORT_LEVELS,
            atol=1e-12,
            rtol=0.0,
        ),
        (
            f"row_index={row_index}: "
            "support levels differ from frozen design"
        ),
    )


    raster_s1_field = None
    intrinsic_s1_field = None

    raster_s1_bands = None
    intrinsic_s1_bands = None

    intrinsic_s1_scale = None


    for j, row in group.iterrows():

        s = float(
            row[
                "support_factor"
            ]
        )


        canvas_path = (
            CANVAS_ROOT
            / str(
                row[
                    "output_relative_path"
                ]
            )
        )


        require(
            canvas_path.is_file(),
            f"Missing primary canvas: {canvas_path}",
        )


        observed_file_sha = sha256_file(
            canvas_path
        )


        require(
            observed_file_sha
            == str(
                row[
                    "output_file_sha256"
                ]
            ),
            (
                "Primary canvas SHA mismatch: "
                f"{canvas_path}"
            ),
        )


        gray = load_gray_uint8(
            canvas_path
        )


        # ---------------------------------------------------------------------
        # Raster-relative RA14
        # ---------------------------------------------------------------------

        raster_field = (
            recover_geometry_raster_relative(
                gray
            )
        )


        require(
            raster_field.shape
            == (72, 72),
            "Raster field shape != 72×72",
        )


        raster_bands = (
            angular_band_fractions(
                raster_field
            )
        )


        # ---------------------------------------------------------------------
        # Intrinsic/object-relative H1
        # ---------------------------------------------------------------------

        (
            intrinsic_field,
            intrinsic_cx,
            intrinsic_cy,
            intrinsic_scale,
        ) = intrinsic_field_from_mask(
            gray
        )


        require(
            intrinsic_field.shape
            == (72, 72),
            "Intrinsic field shape != 72×72",
        )


        intrinsic_bands = (
            angular_band_fractions(
                intrinsic_field
            )
        )


        # ---------------------------------------------------------------------
        # Establish s=1 control
        # ---------------------------------------------------------------------

        if j == 0:

            require(
                np.isclose(
                    s,
                    1.0,
                    atol=0.0,
                    rtol=0.0,
                ),
                (
                    f"row_index={row_index}: "
                    "first support condition is not s=1"
                ),
            )


            raster_s1_field = (
                raster_field.copy()
            )

            intrinsic_s1_field = (
                intrinsic_field.copy()
            )

            raster_s1_bands = (
                raster_bands.copy()
            )

            intrinsic_s1_bands = (
                intrinsic_bands.copy()
            )

            intrinsic_s1_scale = float(
                intrinsic_scale
            )


            # -----------------------------------------------------------------
            # Historical s=1 CROP band replay
            # -----------------------------------------------------------------

            historical = i2_replay.loc[
                i2_replay[
                    "row_index"
                ]
                == int(
                    row_index
                )
            ]


            require(
                len(historical) == 1,
                (
                    f"Historical I2 replay row missing/duplicated: "
                    f"{row_index}"
                ),
            )


            historical = historical.iloc[
                0
            ]


            require(
                str(
                    historical[
                        "relative_path"
                    ]
                )
                ==
                str(
                    row[
                        "relative_path"
                    ]
                ),
                (
                    "Historical I2 relative_path mismatch for "
                    f"row_index={row_index}"
                ),
            )


            historical_bands = (
                historical[
                    I2_CROP_COLUMNS
                ]
                .to_numpy(
                    dtype=float
                )
            )


            historical_diff = float(
                np.max(
                    np.abs(
                        raster_s1_bands
                        - historical_bands
                    )
                )
            )


            s1_historical_max_band_diff = max(
                s1_historical_max_band_diff,
                historical_diff,
            )


            if historical_diff <= 1e-12:
                s1_historical_exact_within_1e12 += 1


        # ---------------------------------------------------------------------
        # Numerical differences from s=1
        # ---------------------------------------------------------------------

        raster_field_diff = float(
            np.max(
                np.abs(
                    raster_field
                    - raster_s1_field
                )
            )
        )


        raster_band_diff = float(
            np.max(
                np.abs(
                    raster_bands
                    - raster_s1_bands
                )
            )
        )


        intrinsic_field_diff = float(
            np.max(
                np.abs(
                    intrinsic_field
                    - intrinsic_s1_field
                )
            )
        )


        intrinsic_band_diff = float(
            np.max(
                np.abs(
                    intrinsic_bands
                    - intrinsic_s1_bands
                )
            )
        )


        raster_global_max_field_diff = max(
            raster_global_max_field_diff,
            raster_field_diff,
        )


        raster_global_max_band_diff = max(
            raster_global_max_band_diff,
            raster_band_diff,
        )


        intrinsic_global_max_field_diff = max(
            intrinsic_global_max_field_diff,
            intrinsic_field_diff,
        )


        intrinsic_global_max_band_diff = max(
            intrinsic_global_max_band_diff,
            intrinsic_band_diff,
        )


        intrinsic_field_exact = bool(
            intrinsic_field_diff
            == 0.0
        )


        intrinsic_band_exact = bool(
            intrinsic_band_diff
            == 0.0
        )


        if intrinsic_field_exact:
            intrinsic_exact_field_conditions += 1


        if intrinsic_band_exact:
            intrinsic_exact_band_conditions += 1


        # ---------------------------------------------------------------------
        # Output records
        # ---------------------------------------------------------------------

        common = {
            "row_index":
                int(
                    row_index
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

            "support_factor":
                s,
        }


        raster_records.append({
            **common,

            "low_1_4":
                float(
                    raster_bands[
                        0
                    ]
                ),

            "mid_5_12":
                float(
                    raster_bands[
                        1
                    ]
                ),

            "highmid_13_24":
                float(
                    raster_bands[
                        2
                    ]
                ),

            "high_25_36":
                float(
                    raster_bands[
                        3
                    ]
                ),
        })


        intrinsic_records.append({
            **common,

            "low_1_4":
                float(
                    intrinsic_bands[
                        0
                    ]
                ),

            "mid_5_12":
                float(
                    intrinsic_bands[
                        1
                    ]
                ),

            "highmid_13_24":
                float(
                    intrinsic_bands[
                        2
                    ]
                ),

            "high_25_36":
                float(
                    intrinsic_bands[
                        3
                    ]
                ),
        })


        geometry_records.append({
            **common,

            "intrinsic_centroid_x":
                float(
                    intrinsic_cx
                ),

            "intrinsic_centroid_y":
                float(
                    intrinsic_cy
                ),

            "intrinsic_max_foreground_radius":
                float(
                    intrinsic_scale
                ),

            "intrinsic_scale_difference_from_s1":
                float(
                    intrinsic_scale
                    - intrinsic_s1_scale
                ),
        })


        control_records.append({
            "row_index":
                int(
                    row_index
                ),

            "support_factor":
                s,

            "raster_max_field_abs_diff_from_s1":
                raster_field_diff,

            "raster_max_band_abs_diff_from_s1":
                raster_band_diff,

            "intrinsic_max_field_abs_diff_from_s1":
                intrinsic_field_diff,

            "intrinsic_max_band_abs_diff_from_s1":
                intrinsic_band_diff,

            "intrinsic_field_exact_from_s1":
                intrinsic_field_exact,

            "intrinsic_band_exact_from_s1":
                intrinsic_band_exact,
        })


# =============================================================================
# 4. Assemble outputs
# =============================================================================

raster_df = pd.DataFrame(
    raster_records
)

intrinsic_df = pd.DataFrame(
    intrinsic_records
)

geometry_df = pd.DataFrame(
    geometry_records
)

controls_df = pd.DataFrame(
    control_records
)


for df, label in [
    (
        raster_df,
        "raster",
    ),
    (
        intrinsic_df,
        "intrinsic",
    ),
    (
        geometry_df,
        "geometry",
    ),
    (
        controls_df,
        "controls",
    ),
]:

    require(
        len(df)
        == EXPECTED_CONDITIONS,
        (
            f"{label}: expected "
            f"{EXPECTED_CONDITIONS} rows"
        ),
    )


# =============================================================================
# 5. Exact primary controls
# =============================================================================

require(
    intrinsic_exact_field_conditions
    == EXPECTED_CONDITIONS,
    (
        "Intrinsic field invariance failed: "
        f"{intrinsic_exact_field_conditions}/"
        f"{EXPECTED_CONDITIONS}"
    ),
)


require(
    intrinsic_exact_band_conditions
    == EXPECTED_CONDITIONS,
    (
        "Intrinsic band invariance failed: "
        f"{intrinsic_exact_band_conditions}/"
        f"{EXPECTED_CONDITIONS}"
    ),
)


require(
    intrinsic_global_max_field_diff
    == 0.0,
    "Intrinsic field max difference is nonzero",
)


require(
    intrinsic_global_max_band_diff
    == 0.0,
    "Intrinsic band max difference is nonzero",
)


require(
    s1_historical_exact_within_1e12
    == EXPECTED_IMAGES,
    (
        "Primary s=1 raster replay failed historical "
        f"I2 tolerance: {s1_historical_exact_within_1e12}/"
        f"{EXPECTED_IMAGES}"
    ),
)


require(
    s1_historical_max_band_diff
    <= 1e-12,
    (
        "Historical s=1 raster replay max error exceeds "
        f"1e-12: {s1_historical_max_band_diff}"
    ),
)


# =============================================================================
# 6. Save primary descriptor outputs
# =============================================================================

RASTER_CSV = (
    OUT
    / "P2_R0_05K4_B_raster_band_fractions_16100.csv"
)

INTRINSIC_CSV = (
    OUT
    / "P2_R0_05K4_B_intrinsic_band_fractions_16100.csv"
)

GEOMETRY_CSV = (
    OUT
    / "P2_R0_05K4_B_intrinsic_geometry_16100.csv"
)

CONTROLS_CSV = (
    OUT
    / "P2_R0_05K4_B_numerical_controls_16100.csv"
)


raster_df.to_csv(
    RASTER_CSV,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


intrinsic_df.to_csv(
    INTRINSIC_CSV,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


geometry_df.to_csv(
    GEOMETRY_CSV,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


controls_df.to_csv(
    CONTROLS_CSV,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


# =============================================================================
# 7. Execution-by-support summary
#
# Counts only. No band-direction statistics.
# =============================================================================

summary_rows = []


for s in SUPPORT_LEVELS:

    mask = np.isclose(
        raster_df[
            "support_factor"
        ].to_numpy(
            dtype=float
        ),
        s,
        atol=1e-12,
        rtol=0.0,
    )


    summary_rows.append({
        "support_factor":
            float(
                s
            ),

        "conditions":
            int(
                mask.sum()
            ),

        "unique_images":
            int(
                raster_df.loc[
                    mask,
                    "row_index"
                ].nunique()
            ),

        "categories":
            int(
                raster_df.loc[
                    mask,
                    "category"
                ].nunique()
            ),
    })


execution_summary = pd.DataFrame(
    summary_rows
)


EXECUTION_CSV = (
    OUT
    / "P2_R0_05K4_B_execution_by_support_level.csv"
)


execution_summary.to_csv(
    EXECUTION_CSV,
    index=False,
    lineterminator="\n",
)


# =============================================================================
# 8. Historical s=1 replay summary
# =============================================================================

S1_REPLAY_JSON = (
    OUT
    / "P2_R0_05K4_B_s1_historical_replay.json"
)


s1_replay = {
    "historical_source":
        str(
            I2_PER_IMAGE
        ),

    "historical_source_sha256":
        i2_table_sha,

    "images_checked":
        EXPECTED_IMAGES,

    "tolerance":
        1e-12,

    "images_within_tolerance":
        s1_historical_exact_within_1e12,

    "max_abs_band_difference":
        s1_historical_max_band_diff,

    "status":
        "PASS",
}


S1_REPLAY_JSON.write_text(
    json.dumps(
        s1_replay,
        indent=2,
        sort_keys=True,
    )
    + "\n",
    encoding="utf-8",
)


# =============================================================================
# 9. Primary execution report
# =============================================================================

REPORT_JSON = (
    OUT
    / "P2_R0_05K4_B_report.json"
)


report = {
    "stage":
        "P2_R0_05K4_B_PRIMARY_DESCRIPTOR_EXECUTION",

    "status":
        "COMPLETE_DESCRIPTOR_EXECUTION_ONLY",

    "source_images":
        EXPECTED_IMAGES,

    "conditions":
        EXPECTED_CONDITIONS,

    "support_levels":
        SUPPORT_LEVELS.tolist(),

    "input_integrity": {
        "path":
            str(
                INTEGRITY_CSV
            ),

        "sha256":
            integrity_sha,
    },

    "source_hashes": {
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
    },

    "historical_s1_replay": {
        "source_sha256":
            i2_table_sha,

        "images_within_1e12":
            s1_historical_exact_within_1e12,

        "max_abs_band_difference":
            s1_historical_max_band_diff,
    },

    "numerical_controls": {
        "raster_max_field_diff_from_s1":
            raster_global_max_field_diff,

        "raster_max_band_diff_from_s1":
            raster_global_max_band_diff,

        "intrinsic_exact_field_conditions":
            intrinsic_exact_field_conditions,

        "intrinsic_max_field_diff_from_s1":
            intrinsic_global_max_field_diff,

        "intrinsic_exact_band_conditions":
            intrinsic_exact_band_conditions,

        "intrinsic_max_band_diff_from_s1":
            intrinsic_global_max_band_diff,
    },

    "field_storage": {
        "full_fields_saved":
            False,

        "reason":
            (
                "Primary fields were executed exactly but not "
                "accumulated into large NPZ archives. Frozen input "
                "canvases, source implementations, band outputs, "
                "and numerical controls reproduce the computation."
            ),
    },

    "analysis_boundary": {
        "directional_hypotheses_tested":
            False,

        "monotonicity_tested":
            False,

        "materiality_threshold_applied":
            False,

        "inferential_statistics":
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
    RASTER_CSV,
    INTRINSIC_CSV,
    GEOMETRY_CSV,
    CONTROLS_CSV,
    EXECUTION_CSV,
    S1_REPLAY_JSON,
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
# 11. Final
# =============================================================================

print()
print("=" * 112)
print(
    "P2-R0-05K4-B — "
    "PRIMARY DESCRIPTOR EXECUTION COMPLETE"
)
print("=" * 112)

print(
    "Source images:",
    EXPECTED_IMAGES,
)

print(
    "Conditions:",
    EXPECTED_CONDITIONS,
)

print(
    "Raster rows:",
    len(
        raster_df
    ),
)

print(
    "Intrinsic rows:",
    len(
        intrinsic_df
    ),
)

print()

print("HISTORICAL s=1 RASTER REPLAY")

print(
    "Within 1e-12:",
    f"{s1_historical_exact_within_1e12}"
    f"/{EXPECTED_IMAGES}",
)

print(
    "Max abs band difference:",
    s1_historical_max_band_diff,
)

print()

print("RASTER NUMERICAL RANGE FROM s=1")

print(
    "Max field difference:",
    raster_global_max_field_diff,
)

print(
    "Max band difference:",
    raster_global_max_band_diff,
)

print()

print("OBJECT-RELATIVE CONTROL")

print(
    "Intrinsic field exact:",
    f"{intrinsic_exact_field_conditions}"
    f"/{EXPECTED_CONDITIONS}",
)

print(
    "Max intrinsic field difference:",
    intrinsic_global_max_field_diff,
)

print(
    "Intrinsic bands exact:",
    f"{intrinsic_exact_band_conditions}"
    f"/{EXPECTED_CONDITIONS}",
)

print(
    "Max intrinsic band difference:",
    intrinsic_global_max_band_diff,
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
print("Directional hypotheses tested : NO")
print("Monotonicity tested            : NO")
print("Materiality threshold applied  : NO")
print("Inferential statistics         : NO")
print("Population inference           : NO")
print("Mechanism verdict              : NO")

print()
print("=" * 112)
print(
    "STOP — FREEZE 05K4-B BEFORE PRIMARY TRAJECTORY / INFERENCE ANALYSIS"
)
print("=" * 112)