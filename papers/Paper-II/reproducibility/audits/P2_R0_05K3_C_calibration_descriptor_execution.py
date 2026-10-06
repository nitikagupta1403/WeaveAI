from pathlib import Path
import hashlib
import json
import importlib.util

import numpy as np
import pandas as pd
from PIL import Image


# =============================================================================
# P2-R0-05K3-C
# CALIBRATION DESCRIPTOR EXECUTION
#
# PURPOSE
#   Execute the frozen raster-relative RA14 representation and the frozen
#   intrinsic/object-relative H1 representation over the 1,610 05K3-B
#   calibration support conditions.
#
# THIS STAGE DOES:
#   - verify all frozen source hashes
#   - execute exact raster-relative descriptor construction
#   - execute exact intrinsic descriptor construction
#   - apply frozen I2 angular band reduction
#   - verify s=1 numerical replay
#   - verify intrinsic support invariance
#
# THIS STAGE DOES NOT:
#   - inspect directional hypotheses
#   - inspect monotonicity
#   - score "support" / "contradiction"
#   - run inferential statistics
#   - make population claims
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
    / "05K3_C_calibration_descriptor_execution"
)

OUT.mkdir(
    parents=True,
    exist_ok=True,
)


# =============================================================================
# Frozen 05K3-B materialization
# =============================================================================

B3 = (
    FROZEN
    / "05K3_B_Calibration_Support_Materialization_v1_0"
)

INTEGRITY_CSV = (
    B3
    / "P2_R0_05K3_B_integrity_1610.csv"
)

EXPECTED_INTEGRITY_SHA = (
    "3f1d913f70394abefd64eeb0a8a09f3cb194d723ee217b085b82abc053887ec9"
)


CANVAS_ROOT = (
    AUDITS
    / "05K3_B_calibration_support_materialization"
    / "canvases"
)


# =============================================================================
# Frozen source implementations
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


EXPECTED_ROWS = 1610
EXPECTED_CASES = 230

SUPPORT_LEVELS = np.asarray(
    [1.00, 1.10, 1.25, 1.50, 2.00, 2.50, 3.00],
    dtype=float,
)

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


def load_gray_uint8(path):
    with Image.open(path) as im:
        return np.asarray(
            im.convert("L"),
            dtype=np.uint8,
        )


# =============================================================================
# Exact frozen raster-relative implementation
# recovered from RA14 source
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
        "Zero total darkness mass",
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
# Exact frozen H1 object-relative implementation
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

    r = np.sqrt(
        dx ** 2
        + dy ** 2
    )

    scale = float(
        r.max()
    )

    require(
        scale > 0.0,
        "Intrinsic foreground scale is zero",
    )

    r_norm = r / scale

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
# Frozen I2 angular spectral reduction
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

    # Sum across radial shells.
    angular_energy = energy.sum(
        axis=0
    )

    non_dc = angular_energy[
        1:37
    ]

    denom = float(
        non_dc.sum()
    )

    require(
        denom > 0.0,
        "Zero non-DC angular spectral energy",
    )

    low = float(
        angular_energy[
            1:5
        ].sum()
        / denom
    )

    mid = float(
        angular_energy[
            5:13
        ].sum()
        / denom
    )

    highmid = float(
        angular_energy[
            13:25
        ].sum()
        / denom
    )

    high = float(
        angular_energy[
            25:37
        ].sum()
        / denom
    )

    values = np.asarray(
        [
            low,
            mid,
            highmid,
            high,
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

print("=" * 108)
print(
    "P2-R0-05K3-C — "
    "CALIBRATION DESCRIPTOR EXECUTION"
)
print("=" * 108)

print("Conditions expected        :", EXPECTED_ROWS)
print("Directional analysis       : NO")
print("Monotonicity analysis      : NO")
print("Hypothesis verdict         : NO")
print("Population inference       : NO")
print()


# =============================================================================
# 1. Verify frozen inputs
# =============================================================================

require(
    INTEGRITY_CSV.is_file(),
    f"Missing integrity CSV: {INTEGRITY_CSV}",
)

integrity_sha = sha256_file(
    INTEGRITY_CSV
)

print(
    "05K3-B integrity SHA:",
    integrity_sha,
    "PASS"
    if integrity_sha == EXPECTED_INTEGRITY_SHA
    else "FAIL",
)

require(
    integrity_sha
    == EXPECTED_INTEGRITY_SHA,
    "05K3-B integrity SHA mismatch",
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


# =============================================================================
# 2. Load materialization manifest
# =============================================================================

integrity = pd.read_csv(
    INTEGRITY_CSV,
    keep_default_na=False,
)


require(
    len(integrity) == EXPECTED_ROWS,
    f"Expected {EXPECTED_ROWS} rows",
)


require(
    integrity[
        "row_index"
    ].nunique()
    == EXPECTED_CASES,
    "Expected 230 unique calibration cases",
)


# =============================================================================
# 3. Execute descriptors
# =============================================================================

raster_records = []
intrinsic_records = []
geometry_records = []

raster_fields = {}
intrinsic_fields = {}


for n, row in integrity.iterrows():

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
        f"Missing canvas: {canvas_path}",
    )


    file_sha = sha256_file(
        canvas_path
    )

    require(
        file_sha
        == str(
            row[
                "output_file_sha256"
            ]
        ),
        (
            "Canvas file SHA mismatch: "
            f"{canvas_path}"
        ),
    )


    gray = load_gray_uint8(
        canvas_path
    )


    role_key = (
        f"{int(row['row_index']):04d}"
        f"__s{float(row['support_factor']):.2f}"
    )


    # -------------------------------------------------------------------------
    # Raster-relative RA14
    # -------------------------------------------------------------------------

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


    raster_fields[
        role_key
    ] = raster_field.astype(
        np.float64,
        copy=False,
    )


    raster_records.append({
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

        "support_factor":
            float(
                row[
                    "support_factor"
                ]
            ),

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


    # -------------------------------------------------------------------------
    # Intrinsic/object-relative H1
    # -------------------------------------------------------------------------

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


    intrinsic_fields[
        role_key
    ] = intrinsic_field.astype(
        np.float64,
        copy=False,
    )


    intrinsic_records.append({
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

        "support_factor":
            float(
                row[
                    "support_factor"
                ]
            ),

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

        "support_factor":
            float(
                row[
                    "support_factor"
                ]
            ),

        "intrinsic_centroid_x":
            intrinsic_cx,

        "intrinsic_centroid_y":
            intrinsic_cy,

        "intrinsic_max_foreground_radius":
            intrinsic_scale,
    })


# =============================================================================
# 4. Save descriptor tables
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


for df, label in [
    (raster_df, "raster"),
    (intrinsic_df, "intrinsic"),
    (geometry_df, "geometry"),
]:

    require(
        len(df) == EXPECTED_ROWS,
        f"{label} output row count != 1610",
    )


RASTER_CSV = (
    OUT
    / "P2_R0_05K3_C_raster_band_fractions_1610.csv"
)

INTRINSIC_CSV = (
    OUT
    / "P2_R0_05K3_C_intrinsic_band_fractions_1610.csv"
)

GEOMETRY_CSV = (
    OUT
    / "P2_R0_05K3_C_intrinsic_geometry_1610.csv"
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


# =============================================================================
# 5. Numerical controls
#
# We compare every intrinsic support condition to the s=1 condition for
# the same calibration case. This is a numerical invariance check only.
# =============================================================================

control_rows = []

raster_max_field_diff_from_s1 = 0.0
raster_max_band_diff_from_s1 = 0.0

intrinsic_max_field_diff_from_s1 = 0.0
intrinsic_max_band_diff_from_s1 = 0.0

intrinsic_exact_field_conditions = 0
intrinsic_exact_band_conditions = 0


for row_index, g in integrity.groupby(
    "row_index",
    sort=True,
):

    g = g.sort_values(
        "support_factor"
    )


    s1_row = g.iloc[
        0
    ]

    s1_key = (
        f"{int(row_index):04d}"
        f"__s{1.00:.2f}"
    )


    raster_s1 = raster_fields[
        s1_key
    ]

    intrinsic_s1 = intrinsic_fields[
        s1_key
    ]


    raster_band_s1 = (
        raster_df.loc[
            (raster_df["row_index"] == row_index)
            &
            np.isclose(
                raster_df["support_factor"],
                1.0,
            ),
            BANDS,
        ]
        .iloc[
            0
        ]
        .to_numpy(
            dtype=float
        )
    )


    intrinsic_band_s1 = (
        intrinsic_df.loc[
            (intrinsic_df["row_index"] == row_index)
            &
            np.isclose(
                intrinsic_df["support_factor"],
                1.0,
            ),
            BANDS,
        ]
        .iloc[
            0
        ]
        .to_numpy(
            dtype=float
        )
    )


    for _, rr in g.iterrows():

        s = float(
            rr[
                "support_factor"
            ]
        )

        key = (
            f"{int(row_index):04d}"
            f"__s{s:.2f}"
        )


        raster_field_diff = float(
            np.max(
                np.abs(
                    raster_fields[
                        key
                    ]
                    - raster_s1
                )
            )
        )


        intrinsic_field_diff = float(
            np.max(
                np.abs(
                    intrinsic_fields[
                        key
                    ]
                    - intrinsic_s1
                )
            )
        )


        raster_band_vec = (
            raster_df.loc[
                (raster_df["row_index"] == row_index)
                &
                np.isclose(
                    raster_df["support_factor"],
                    s,
                ),
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
            intrinsic_df.loc[
                (intrinsic_df["row_index"] == row_index)
                &
                np.isclose(
                    intrinsic_df["support_factor"],
                    s,
                ),
                BANDS,
            ]
            .iloc[
                0
            ]
            .to_numpy(
                dtype=float
            )
        )


        raster_band_diff = float(
            np.max(
                np.abs(
                    raster_band_vec
                    - raster_band_s1
                )
            )
        )


        intrinsic_band_diff = float(
            np.max(
                np.abs(
                    intrinsic_band_vec
                    - intrinsic_band_s1
                )
            )
        )


        raster_max_field_diff_from_s1 = max(
            raster_max_field_diff_from_s1,
            raster_field_diff,
        )

        raster_max_band_diff_from_s1 = max(
            raster_max_band_diff_from_s1,
            raster_band_diff,
        )

        intrinsic_max_field_diff_from_s1 = max(
            intrinsic_max_field_diff_from_s1,
            intrinsic_field_diff,
        )

        intrinsic_max_band_diff_from_s1 = max(
            intrinsic_max_band_diff_from_s1,
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


        control_rows.append({
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


controls_df = pd.DataFrame(
    control_rows
)


require(
    len(controls_df) == EXPECTED_ROWS,
    "Control rows != 1610",
)


require(
    intrinsic_exact_field_conditions
    == EXPECTED_ROWS,
    (
        "Intrinsic fields were not exact across "
        "all support conditions"
    ),
)


require(
    intrinsic_exact_band_conditions
    == EXPECTED_ROWS,
    (
        "Intrinsic band fractions were not exact across "
        "all support conditions"
    ),
)


CONTROLS_CSV = (
    OUT
    / "P2_R0_05K3_C_numerical_controls_1610.csv"
)


controls_df.to_csv(
    CONTROLS_CSV,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


# =============================================================================
# 6. Save fields
# =============================================================================

RASTER_NPZ = (
    OUT
    / "P2_R0_05K3_C_raster_fields_1610.npz"
)

INTRINSIC_NPZ = (
    OUT
    / "P2_R0_05K3_C_intrinsic_fields_1610.npz"
)


np.savez_compressed(
    RASTER_NPZ,
    **raster_fields,
)

np.savez_compressed(
    INTRINSIC_NPZ,
    **intrinsic_fields,
)


# =============================================================================
# 7. Execution summary only
# =============================================================================

EXECUTION_SUMMARY_CSV = (
    OUT
    / "P2_R0_05K3_C_execution_by_support_level.csv"
)


summary_rows = []


for s in SUPPORT_LEVELS:

    mask = np.isclose(
        raster_df[
            "support_factor"
        ].to_numpy(
            dtype=float
        ),
        s,
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

        "unique_cases":
            int(
                raster_df.loc[
                    mask,
                    "row_index"
                ].nunique()
            ),
    })


execution_summary = pd.DataFrame(
    summary_rows
)


execution_summary.to_csv(
    EXECUTION_SUMMARY_CSV,
    index=False,
    lineterminator="\n",
)


# =============================================================================
# 8. Report
# =============================================================================

REPORT_JSON = (
    OUT
    / "P2_R0_05K3_C_report.json"
)


report = {
    "stage":
        "P2_R0_05K3_C_CALIBRATION_DESCRIPTOR_EXECUTION",

    "status":
        "COMPLETE_DESCRIPTOR_EXECUTION_ONLY",

    "calibration_cases":
        EXPECTED_CASES,

    "conditions":
        EXPECTED_ROWS,

    "support_levels":
        SUPPORT_LEVELS.tolist(),

    "source_hashes": {
        "RA14":
            EXPECTED_SOURCE_SHA["RA14"],

        "I2":
            EXPECTED_SOURCE_SHA["I2"],

        "H1":
            EXPECTED_SOURCE_SHA["H1"],
    },

    "input_integrity_sha256":
        integrity_sha,

    "numerical_controls": {
        "raster_max_field_diff_from_s1":
            raster_max_field_diff_from_s1,

        "raster_max_band_diff_from_s1":
            raster_max_band_diff_from_s1,

        "intrinsic_exact_field_conditions":
            intrinsic_exact_field_conditions,

        "intrinsic_max_field_diff_from_s1":
            intrinsic_max_field_diff_from_s1,

        "intrinsic_exact_band_conditions":
            intrinsic_exact_band_conditions,

        "intrinsic_max_band_diff_from_s1":
            intrinsic_max_band_diff_from_s1,
    },

    "analysis_boundary": {
        "directional_hypotheses_tested":
            False,

        "monotonicity_tested":
            False,

        "materiality_threshold_applied":
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
# 9. Checksums
# =============================================================================

OUTPUTS = [
    RASTER_CSV,
    INTRINSIC_CSV,
    GEOMETRY_CSV,
    CONTROLS_CSV,
    EXECUTION_SUMMARY_CSV,
    RASTER_NPZ,
    INTRINSIC_NPZ,
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
# 10. Final
# =============================================================================

print()
print("=" * 108)
print(
    "P2-R0-05K3-C — EXECUTION COMPLETE"
)
print("=" * 108)

print(
    "Calibration cases:",
    EXPECTED_CASES,
)

print(
    "Conditions:",
    EXPECTED_ROWS,
)

print(
    "Raster conditions processed:",
    len(
        raster_df
    ),
)

print()

print(
    "Raster max field diff from s=1:",
    raster_max_field_diff_from_s1,
)

print(
    "Raster max band diff from s=1:",
    raster_max_band_diff_from_s1,
)

print()

print(
    "Intrinsic field exact-vs-s1 conditions:",
    f"{intrinsic_exact_field_conditions}/{EXPECTED_ROWS}",
)

print(
    "Intrinsic max field diff from s=1:",
    intrinsic_max_field_diff_from_s1,
)

print(
    "Intrinsic band exact-vs-s1 conditions:",
    f"{intrinsic_exact_band_conditions}/{EXPECTED_ROWS}",
)

print(
    "Intrinsic max band diff from s=1:",
    intrinsic_max_band_diff_from_s1,
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
print("Population inference           : NO")
print("Mechanism verdict              : NO")

print()
print("=" * 108)
print(
    "STOP — FREEZE 05K3-C BEFORE TRAJECTORY ANALYSIS"
)
print("=" * 108)