from pathlib import Path
import hashlib
import json

import numpy as np
import pandas as pd


# =============================================================================
# P2-R0-05K3-D
# CALIBRATION TRAJECTORY ANALYSIS
#
# INPUT
#   Frozen 05K3-C descriptor outputs.
#
# PURPOSE
#   Descriptive analysis of the 230-case calibration support sweep.
#
# THIS STAGE DOES:
#   - compute Δband(s) = band(s) - band(1)
#   - summarize endpoint direction at s=3
#   - summarize full-trajectory monotonicity
#   - summarize four-band L1 displacement
#   - summarize support-level median / IQR trajectories
#   - summarize category-level endpoint behavior
#   - carry exact intrinsic invariance as a control
#
# THIS STAGE DOES NOT:
#   - perform p-values
#   - bootstrap
#   - apply a materiality threshold
#   - perform population inference
#   - claim a general mechanism
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
    / "05K3_D_calibration_trajectory_analysis"
)

OUT.mkdir(
    parents=True,
    exist_ok=True,
)


# =============================================================================
# Frozen 05K3-C package
# =============================================================================

C_DIR = (
    FROZEN
    / "05K3_C_Calibration_Descriptor_Execution_v1_0"
)

RASTER_CSV = (
    C_DIR
    / "P2_R0_05K3_C_raster_band_fractions_1610.csv"
)

INTRINSIC_CSV = (
    C_DIR
    / "P2_R0_05K3_C_intrinsic_band_fractions_1610.csv"
)

CONTROLS_CSV = (
    C_DIR
    / "P2_R0_05K3_C_numerical_controls_1610.csv"
)

C_REPORT = (
    C_DIR
    / "P2_R0_05K3_C_report.json"
)


EXPECTED_SHA = {
    "raster":
        "d5eb9487796e8c29994a1a0f596817ae0995e144e9dbde073d68f370ec016c7e",

    "intrinsic":
        "43bf4fe8bf4af073a15f362edd6597533172b72f891f4d17cb3694b5783a0960",

    "controls":
        "7dd1ce7f49ef43fdd6d1f9b8d3ae5d7232e17285058cf08201c83d0193b8485c",

    "report":
        "c924de04ac0531054e79944b1e1e5c2c16fe441e4acb234ac24020c052855712",
}


EXPECTED_CASES = 230
EXPECTED_CATEGORIES = 23
EXPECTED_ROWS = 1610

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

BANDS = [
    "low_1_4",
    "mid_5_12",
    "highmid_13_24",
    "high_25_36",
]


# Preregistered directional expectations for canvas enlargement.
DIRECTION = {
    "low_1_4": +1,
    "mid_5_12": 0,
    "highmid_13_24": -1,
    "high_25_36": -1,
}


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


def nondecreasing(values, tol=1e-15):
    values = np.asarray(
        values,
        dtype=float,
    )

    return bool(
        np.all(
            np.diff(values)
            >= -tol
        )
    )


def nonincreasing(values, tol=1e-15):
    values = np.asarray(
        values,
        dtype=float,
    )

    return bool(
        np.all(
            np.diff(values)
            <= tol
        )
    )


def quantile(values, q):
    return float(
        np.quantile(
            np.asarray(
                values,
                dtype=float,
            ),
            q,
        )
    )


# =============================================================================
# Header
# =============================================================================

print("=" * 112)
print(
    "P2-R0-05K3-D — "
    "230-CASE CALIBRATION TRAJECTORY ANALYSIS"
)
print("=" * 112)

print("Calibration layer          : YES")
print("Population inference       : NO")
print("p-values / bootstrap       : NO")
print("Materiality threshold      : NOT APPLIED")
print("Mechanism proof            : NO")
print()


# =============================================================================
# 1. Frozen-input verification
# =============================================================================

for label, path in [
    ("raster", RASTER_CSV),
    ("intrinsic", INTRINSIC_CSV),
    ("controls", CONTROLS_CSV),
    ("report", C_REPORT),
]:

    require(
        path.is_file(),
        f"Missing frozen input: {path}",
    )

    observed = sha256_file(
        path
    )

    expected = EXPECTED_SHA[
        label
    ]

    print(
        label,
        observed,
        "PASS"
        if observed == expected
        else "FAIL",
    )

    require(
        observed == expected,
        f"{label} SHA mismatch",
    )


c_report = json.loads(
    C_REPORT.read_text(
        encoding="utf-8"
    )
)


require(
    c_report[
        "status"
    ]
    == "COMPLETE_DESCRIPTOR_EXECUTION_ONLY",
    "Unexpected 05K3-C report status",
)


require(
    c_report[
        "analysis_boundary"
    ][
        "directional_hypotheses_tested"
    ]
    is False,
    "05K3-C already claims directional testing",
)


# =============================================================================
# 2. Load descriptor outputs
# =============================================================================

raster = pd.read_csv(
    RASTER_CSV,
    keep_default_na=False,
)

intrinsic = pd.read_csv(
    INTRINSIC_CSV,
    keep_default_na=False,
)

controls = pd.read_csv(
    CONTROLS_CSV,
    keep_default_na=False,
)


for df, label in [
    (raster, "raster"),
    (intrinsic, "intrinsic"),
    (controls, "controls"),
]:

    require(
        len(df) == EXPECTED_ROWS,
        f"{label}: expected {EXPECTED_ROWS} rows",
    )


require(
    raster[
        "row_index"
    ].nunique()
    == EXPECTED_CASES,
    "Raster case count != 230",
)


require(
    raster[
        "category"
    ].nunique()
    == EXPECTED_CATEGORIES,
    "Raster category count != 23",
)


category_case_counts = (
    raster[
        [
            "category",
            "row_index",
        ]
    ]
    .drop_duplicates()
    .groupby(
        "category"
    )
    .size()
)


require(
    category_case_counts.min() == 10
    and category_case_counts.max() == 10,
    "Expected exactly ten calibration cases/category",
)


# =============================================================================
# 3. Verify intrinsic invariance before interpreting raster behavior
# =============================================================================

intrinsic_max_field_diff = float(
    controls[
        "intrinsic_max_field_abs_diff_from_s1"
    ].max()
)

intrinsic_max_band_diff = float(
    controls[
        "intrinsic_max_band_abs_diff_from_s1"
    ].max()
)


intrinsic_field_exact = bool(
    controls[
        "intrinsic_field_exact_from_s1"
    ].astype(bool).all()
)


intrinsic_band_exact = bool(
    controls[
        "intrinsic_band_exact_from_s1"
    ].astype(bool).all()
)


require(
    intrinsic_field_exact
    and intrinsic_band_exact,
    "Intrinsic invariance control failed",
)


require(
    intrinsic_max_field_diff == 0.0
    and intrinsic_max_band_diff == 0.0,
    "Intrinsic invariance is not bit-exact",
)


print()
print("=" * 112)
print("OBJECT-RELATIVE CONTROL")
print("=" * 112)

print(
    "Intrinsic field exact:",
    f"{int(controls['intrinsic_field_exact_from_s1'].astype(bool).sum())}"
    f"/{len(controls)}",
)

print(
    "Intrinsic band exact:",
    f"{int(controls['intrinsic_band_exact_from_s1'].astype(bool).sum())}"
    f"/{len(controls)}",
)

print(
    "Max intrinsic field difference:",
    intrinsic_max_field_diff,
)

print(
    "Max intrinsic band difference:",
    intrinsic_max_band_diff,
)


# =============================================================================
# 4. Build baseline-relative trajectories
# =============================================================================

trajectory_rows = []


for row_index, group in raster.groupby(
    "row_index",
    sort=True,
):

    group = (
        group.sort_values(
            "support_factor"
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
            "support levels do not match frozen design"
        ),
    )


    base = (
        group.iloc[
            0
        ][
            BANDS
        ]
        .to_numpy(
            dtype=float
        )
    )


    for j, row in group.iterrows():

        current = (
            row[
                BANDS
            ]
            .to_numpy(
                dtype=float
            )
        )


        delta = current - base


        # Band fractions sum to 1, therefore their deltas should sum to 0.
        delta_sum = float(
            delta.sum()
        )


        require(
            abs(delta_sum)
            <= 5e-12,
            (
                f"Band-delta conservation failed for "
                f"row={row_index}, s={row['support_factor']}: "
                f"{delta_sum}"
            ),
        )


        rec = {
            "calibration_index":
                int(
                    row[
                        "calibration_index"
                    ]
                ),

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

            "four_band_l1_from_s1":
                float(
                    np.sum(
                        np.abs(
                            delta
                        )
                    )
                ),

            "delta_sum":
                delta_sum,
        }


        for k, band in enumerate(
            BANDS
        ):

            rec[
                f"raster_{band}"
            ] = float(
                current[
                    k
                ]
            )

            rec[
                f"delta_{band}"
            ] = float(
                delta[
                    k
                ]
            )


        trajectory_rows.append(
            rec
        )


trajectory = pd.DataFrame(
    trajectory_rows
)


require(
    len(trajectory)
    == EXPECTED_ROWS,
    "Trajectory output != 1610 rows",
)


# =============================================================================
# 5. Per-case endpoint and monotonicity summary
# =============================================================================

case_rows = []


for row_index, group in trajectory.groupby(
    "row_index",
    sort=True,
):

    group = (
        group.sort_values(
            "support_factor"
        )
        .reset_index(
            drop=True
        )
    )


    endpoint = group.iloc[
        -1
    ]


    rec = {
        "calibration_index":
            int(
                endpoint[
                    "calibration_index"
                ]
            ),

        "row_index":
            int(
                row_index
            ),

        "category":
            str(
                endpoint[
                    "category"
                ]
            ),

        "garment_identity":
            str(
                endpoint[
                    "garment_identity"
                ]
            ),

        "relative_path":
            str(
                endpoint[
                    "relative_path"
                ]
            ),

        "four_band_l1_s3_minus_s1":
            float(
                endpoint[
                    "four_band_l1_from_s1"
                ]
            ),

        "four_band_l1_nondecreasing":
            nondecreasing(
                group[
                    "four_band_l1_from_s1"
                ].to_numpy(
                    dtype=float
                )
            ),
    }


    for band in BANDS:

        deltas = group[
            f"delta_{band}"
        ].to_numpy(
            dtype=float
        )


        endpoint_delta = float(
            deltas[
                -1
            ]
        )


        rec[
            f"{band}_delta_s3_minus_s1"
        ] = endpoint_delta


        direction = DIRECTION[
            band
        ]


        if direction == +1:

            rec[
                f"{band}_endpoint_direction_concordant"
            ] = bool(
                endpoint_delta > 0.0
            )

            rec[
                f"{band}_trajectory_monotone_in_predicted_direction"
            ] = nondecreasing(
                deltas
            )


        elif direction == -1:

            rec[
                f"{band}_endpoint_direction_concordant"
            ] = bool(
                endpoint_delta < 0.0
            )

            rec[
                f"{band}_trajectory_monotone_in_predicted_direction"
            ] = nonincreasing(
                deltas
            )


        else:

            rec[
                f"{band}_endpoint_direction_concordant"
            ] = None

            rec[
                f"{band}_trajectory_monotone_in_predicted_direction"
            ] = None


    case_rows.append(
        rec
    )


case_summary = pd.DataFrame(
    case_rows
)


require(
    len(case_summary)
    == EXPECTED_CASES,
    "Per-case summary != 230 rows",
)


# =============================================================================
# 6. Overall descriptive support-level trajectory
# =============================================================================

support_rows = []


for s, group in trajectory.groupby(
    "support_factor",
    sort=True,
):

    rec = {
        "support_factor":
            float(
                s
            ),

        "cases":
            int(
                len(
                    group
                )
            ),

        "median_four_band_l1_from_s1":
            float(
                np.median(
                    group[
                        "four_band_l1_from_s1"
                    ]
                )
            ),

        "q25_four_band_l1_from_s1":
            quantile(
                group[
                    "four_band_l1_from_s1"
                ],
                0.25,
            ),

        "q75_four_band_l1_from_s1":
            quantile(
                group[
                    "four_band_l1_from_s1"
                ],
                0.75,
            ),
    }


    for band in BANDS:

        vals = group[
            f"delta_{band}"
        ].to_numpy(
            dtype=float
        )


        rec[
            f"median_delta_{band}"
        ] = float(
            np.median(
                vals
            )
        )

        rec[
            f"q25_delta_{band}"
        ] = quantile(
            vals,
            0.25,
        )

        rec[
            f"q75_delta_{band}"
        ] = quantile(
            vals,
            0.75,
        )


    support_rows.append(
        rec
    )


support_summary = pd.DataFrame(
    support_rows
)


# =============================================================================
# 7. Endpoint descriptive counts
# =============================================================================

endpoint_counts = {}
endpoint_percent = {}

monotone_counts = {}
monotone_percent = {}


for band in [
    "low_1_4",
    "highmid_13_24",
    "high_25_36",
]:

    endpoint_col = (
        f"{band}_"
        "endpoint_direction_concordant"
    )

    monotone_col = (
        f"{band}_"
        "trajectory_monotone_in_predicted_direction"
    )


    n_endpoint = int(
        case_summary[
            endpoint_col
        ].astype(bool).sum()
    )


    n_monotone = int(
        case_summary[
            monotone_col
        ].astype(bool).sum()
    )


    endpoint_counts[
        band
    ] = n_endpoint

    endpoint_percent[
        band
    ] = float(
        100.0
        * n_endpoint
        / EXPECTED_CASES
    )


    monotone_counts[
        band
    ] = n_monotone

    monotone_percent[
        band
    ] = float(
        100.0
        * n_monotone
        / EXPECTED_CASES
    )


l1_monotone_count = int(
    case_summary[
        "four_band_l1_nondecreasing"
    ].astype(bool).sum()
)


l1_monotone_percent = float(
    100.0
    * l1_monotone_count
    / EXPECTED_CASES
)


# =============================================================================
# 8. Category-level endpoint summaries
#
# Exactly ten calibration identities/category.
# Descriptive only.
# =============================================================================

category_rows = []


for category, group in case_summary.groupby(
    "category",
    sort=True,
):

    require(
        len(group) == 10,
        (
            f"{category}: expected exactly "
            "10 calibration identities"
        ),
    )


    rec = {
        "category":
            str(
                category
            ),

        "cases":
            int(
                len(
                    group
                )
            ),

        "median_four_band_l1_s3_minus_s1":
            float(
                np.median(
                    group[
                        "four_band_l1_s3_minus_s1"
                    ]
                )
            ),
    }


    for band in BANDS:

        delta_col = (
            f"{band}_delta_s3_minus_s1"
        )


        vals = group[
            delta_col
        ].to_numpy(
            dtype=float
        )


        rec[
            f"median_delta_{band}"
        ] = float(
            np.median(
                vals
            )
        )


        direction = DIRECTION[
            band
        ]


        if direction == +1:

            rec[
                f"n_endpoint_concordant_{band}"
            ] = int(
                np.sum(
                    vals > 0.0
                )
            )


        elif direction == -1:

            rec[
                f"n_endpoint_concordant_{band}"
            ] = int(
                np.sum(
                    vals < 0.0
                )
            )


    category_rows.append(
        rec
    )


category_summary = pd.DataFrame(
    category_rows
)


require(
    len(category_summary)
    == EXPECTED_CATEGORIES,
    "Category summary != 23 rows",
)


# =============================================================================
# 9. Median endpoint direction across categories
#
# Again: descriptive, not inferential.
# =============================================================================

category_median_direction_counts = {}


for band in [
    "low_1_4",
    "highmid_13_24",
    "high_25_36",
]:

    vals = category_summary[
        f"median_delta_{band}"
    ].to_numpy(
        dtype=float
    )


    direction = DIRECTION[
        band
    ]


    if direction == +1:

        count = int(
            np.sum(
                vals > 0.0
            )
        )

    else:

        count = int(
            np.sum(
                vals < 0.0
            )
        )


    category_median_direction_counts[
        band
    ] = count


# =============================================================================
# 10. Save outputs
# =============================================================================

TRAJECTORY_CSV = (
    OUT
    / "P2_R0_05K3_D_per_condition_trajectories_1610.csv"
)

CASE_CSV = (
    OUT
    / "P2_R0_05K3_D_per_case_summary_230.csv"
)

SUPPORT_CSV = (
    OUT
    / "P2_R0_05K3_D_support_level_summary.csv"
)

CATEGORY_CSV = (
    OUT
    / "P2_R0_05K3_D_category_endpoint_summary_23.csv"
)


trajectory.to_csv(
    TRAJECTORY_CSV,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


case_summary.to_csv(
    CASE_CSV,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


support_summary.to_csv(
    SUPPORT_CSV,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


category_summary.to_csv(
    CATEGORY_CSV,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


# =============================================================================
# 11. Report
# =============================================================================

REPORT_JSON = (
    OUT
    / "P2_R0_05K3_D_report.json"
)


report = {
    "stage":
        "P2_R0_05K3_D_CALIBRATION_TRAJECTORY_ANALYSIS",

    "status":
        "COMPLETE_DESCRIPTIVE_CALIBRATION_ANALYSIS",

    "calibration_cases":
        EXPECTED_CASES,

    "categories":
        EXPECTED_CATEGORIES,

    "support_levels":
        SUPPORT_LEVELS.tolist(),

    "object_relative_control": {
        "all_1610_fields_exact":
            intrinsic_field_exact,

        "all_1610_band_vectors_exact":
            intrinsic_band_exact,

        "max_field_difference":
            intrinsic_max_field_diff,

        "max_band_difference":
            intrinsic_max_band_diff,
    },

    "preregistered_canvas_enlargement_direction": {
        "low_1_4":
            "increase",

        "mid_5_12":
            "no directional prediction",

        "highmid_13_24":
            "decrease",

        "high_25_36":
            "decrease",
    },

    "s3_endpoint_concordance_counts_of_230":
        endpoint_counts,

    "s3_endpoint_concordance_percent":
        endpoint_percent,

    "full_trajectory_monotonicity_counts_of_230":
        monotone_counts,

    "full_trajectory_monotonicity_percent":
        monotone_percent,

    "four_band_l1_nondecreasing": {
        "count":
            l1_monotone_count,

        "percent":
            l1_monotone_percent,
    },

    "category_median_endpoint_direction_counts_of_23":
        category_median_direction_counts,

    "materiality": {
        "threshold_applied":
            False,

        "reason":
            (
                "No operational materiality threshold was frozen "
                "before descriptor outcomes were opened."
            ),
    },

    "analysis_boundary": {
        "p_values":
            False,

        "bootstrap":
            False,

        "population_inference":
            False,

        "full_2300_primary_experiment":
            False,

        "mechanism_proof_claim":
            False,
    },

    "interpretation_boundary":
        (
            "05K3-D is an intermediate calibration analysis over "
            "one deterministically selected sketch per canonical "
            "garment identity. Results describe calibration behavior "
            "and heterogeneity but do not constitute population-level "
            "inference."
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
# 12. Checksums
# =============================================================================

OUTPUTS = [
    TRAJECTORY_CSV,
    CASE_CSV,
    SUPPORT_CSV,
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
# 13. Final descriptive output
# =============================================================================

print()
print("=" * 112)
print(
    "P2-R0-05K3-D — DESCRIPTIVE CALIBRATION RESULTS"
)
print("=" * 112)

print()
print("OBJECT-RELATIVE CONTROL")

print(
    "Field exact:",
    f"{int(controls['intrinsic_field_exact_from_s1'].astype(bool).sum())}"
    f"/{len(controls)}",
)

print(
    "Band exact:",
    f"{int(controls['intrinsic_band_exact_from_s1'].astype(bool).sum())}"
    f"/{len(controls)}",
)


print()
print("RASTER ENDPOINT DIRECTION — s=3 vs s=1")

for band in [
    "low_1_4",
    "highmid_13_24",
    "high_25_36",
]:

    print(
        f"{band:17s}",
        f"{endpoint_counts[band]}/{EXPECTED_CASES}",
        f"({endpoint_percent[band]:.1f}%)",
    )


print()
print("RASTER FULL-TRAJECTORY MONOTONICITY")

for band in [
    "low_1_4",
    "highmid_13_24",
    "high_25_36",
]:

    print(
        f"{band:17s}",
        f"{monotone_counts[band]}/{EXPECTED_CASES}",
        f"({monotone_percent[band]:.1f}%)",
    )


print()
print(
    "Four-band L1 nondecreasing:",
    f"{l1_monotone_count}/{EXPECTED_CASES}",
    f"({l1_monotone_percent:.1f}%)",
)


print()
print("MEDIAN / IQR TRAJECTORIES")

display_cols = [
    "support_factor",

    "median_delta_low_1_4",
    "q25_delta_low_1_4",
    "q75_delta_low_1_4",

    "median_delta_mid_5_12",

    "median_delta_highmid_13_24",
    "q25_delta_highmid_13_24",
    "q75_delta_highmid_13_24",

    "median_delta_high_25_36",
    "q25_delta_high_25_36",
    "q75_delta_high_25_36",

    "median_four_band_l1_from_s1",
]


print(
    support_summary[
        display_cols
    ].to_string(
        index=False
    )
)


print()
print("CATEGORY-MEDIAN ENDPOINT DIRECTION")

for band in [
    "low_1_4",
    "highmid_13_24",
    "high_25_36",
]:

    print(
        f"{band:17s}",
        f"{category_median_direction_counts[band]}"
        f"/{EXPECTED_CATEGORIES} categories",
    )


print()
print("CATEGORY ENDPOINT TABLE")

category_display = [
    "category",
    "median_delta_low_1_4",
    "median_delta_mid_5_12",
    "median_delta_highmid_13_24",
    "median_delta_high_25_36",
    "median_four_band_l1_s3_minus_s1",
    "n_endpoint_concordant_low_1_4",
    "n_endpoint_concordant_highmid_13_24",
    "n_endpoint_concordant_high_25_36",
]


print(
    category_summary[
        category_display
    ].to_string(
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
print("Population inference      : NO")
print("p-values / bootstrap      : NO")
print("Materiality threshold     : NO")
print("Mechanism proof claimed   : NO")

print()
print("=" * 112)
print(
    "STOP — FREEZE 05K3-D BEFORE DESIGNING "
    "THE 2300-IMAGE PRIMARY SUPPORT INTERVENTION"
)
print("=" * 112)