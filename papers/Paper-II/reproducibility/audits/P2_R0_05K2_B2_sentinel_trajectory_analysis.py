from pathlib import Path
import hashlib
import json

import numpy as np
import pandas as pd


# =============================================================================
# P2-R0-05K2-B2
# SENTINEL SUPPORT TRAJECTORY ANALYSIS
#
# INPUT:
#   frozen 05K2-B1 descriptor outputs
#
# PURPOSE:
#   descriptive evaluation of preregistered support-sweep trajectories
#
# IMPORTANT:
#   - sentinel experiment only
#   - no population inference
#   - no p-values
#   - no bootstrap
#   - no post-hoc threshold optimization
#   - no 0.005 "materiality" verdict
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

B1 = (
    FROZEN
    / "05K2_B1_Sentinel_Descriptor_Sweep_v1_0"
)

OUT = (
    AUDITS
    / "05K2_B2_sentinel_trajectory_analysis"
)

OUT.mkdir(
    parents=True,
    exist_ok=True,
)


# =============================================================================
# Frozen B1 artifacts
# =============================================================================

CONDITIONS_CSV = (
    B1
    / "P2_R0_05K2_B1_conditions_70.csv"
)

RASTER_CSV = (
    B1
    / "P2_R0_05K2_B1_raster_band_fractions_70.csv"
)

INTRINSIC_CSV = (
    B1
    / "P2_R0_05K2_B1_intrinsic_band_fractions_70.csv"
)

CONTROLS_CSV = (
    B1
    / "P2_R0_05K2_B1_numerical_controls_70.csv"
)

B1_REPORT = (
    B1
    / "P2_R0_05K2_B1_report.json"
)


EXPECTED_SHA = {
    "conditions":
        "e5ad03736a452ca7ac8a2093d15dcf1b9553bfb17af58afe4b10a41d51b2714e",

    "raster":
        "903a781bb802a1dd6211512b658d83db07dcc0e37d24b6d1069a293f24bc7d0b",

    "intrinsic":
        "0bd6c04b5cf50e787077b562f1fe05caf3ea2df2a4e6b8fb82e621b0718eb9de",

    "controls":
        "18873a418ca5795c0adfdcce534870f695b545a8da75f9ee60e903b9b05c0987",

    "report":
        "72889f50f6ce13bd9f883312e45164f91f828ec13a82998ec9c895c906bed212",
}


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


DIRECTION = {
    "low_1_4":
        +1,

    "mid_5_12":
        0,

    "highmid_13_24":
        -1,

    "high_25_36":
        -1,
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


def sign_with_zero(x, tol=1e-15):

    if x > tol:
        return 1

    if x < -tol:
        return -1

    return 0


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


# =============================================================================
# Header
# =============================================================================

print("=" * 108)
print(
    "P2-R0-05K2-B2 — "
    "SENTINEL SUPPORT TRAJECTORY ANALYSIS"
)
print("=" * 108)

print(
    "Sentinel diagnostic analysis : YES"
)

print(
    "Population inference          : NO"
)

print(
    "p-values / bootstrap          : NO"
)

print(
    "0.005 materiality rule        : NOT APPLIED"
)

print()


# =============================================================================
# 1. Validate frozen inputs
# =============================================================================

for label, path in [
    (
        "conditions",
        CONDITIONS_CSV,
    ),
    (
        "raster",
        RASTER_CSV,
    ),
    (
        "intrinsic",
        INTRINSIC_CSV,
    ),
    (
        "controls",
        CONTROLS_CSV,
    ),
    (
        "report",
        B1_REPORT,
    ),
]:

    require(
        path.is_file(),
        f"Missing B1 artifact: {path}",
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


b1_report = json.loads(
    B1_REPORT.read_text(
        encoding="utf-8"
    )
)


require(
    b1_report[
        "status"
    ]
    == "COMPLETE_DESCRIPTOR_EXECUTION_ONLY",
    "Unexpected B1 status",
)


require(
    b1_report[
        "analysis_boundary"
    ][
        "directional_hypotheses_tested"
    ]
    is False,
    "B1 already claims directional testing",
)


# =============================================================================
# 2. Load B1 tables
# =============================================================================

conditions = pd.read_csv(
    CONDITIONS_CSV,
    keep_default_na=False,
)

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
    (
        conditions,
        "conditions",
    ),
    (
        raster,
        "raster",
    ),
    (
        intrinsic,
        "intrinsic",
    ),
    (
        controls,
        "controls",
    ),
]:

    require(
        len(df) == 70,
        f"{label}: expected 70 rows",
    )


require(
    raster[
        "role"
    ].nunique()
    == 10,
    "Expected ten raster sentinel roles",
)


# =============================================================================
# 3. Build exact baseline-relative trajectories
# =============================================================================

trajectory_rows = []


for role, group in raster.groupby(
    "role",
    sort=True,
):

    group = group.sort_values(
        "support_factor"
    ).reset_index(
        drop=True
    )


    require(
        np.allclose(
            group[
                "support_factor"
            ].to_numpy(
                dtype=float
            ),
            SUPPORT_LEVELS,
            atol=1e-12,
            rtol=0.0,
        ),
        (
            f"{role}: support levels "
            "do not match frozen design"
        ),
    )


    intrinsic_group = (
        intrinsic.loc[
            intrinsic[
                "role"
            ]
            == role
        ]
        .sort_values(
            "support_factor"
        )
        .reset_index(
            drop=True
        )
    )


    require(
        len(
            intrinsic_group
        )
        == 7,
        f"{role}: intrinsic rows != 7",
    )


    raster_base = (
        group.iloc[
            0
        ][
            BANDS
        ]
        .to_numpy(
            dtype=float
        )
    )


    intrinsic_base = (
        intrinsic_group.iloc[
            0
        ][
            BANDS
        ]
        .to_numpy(
            dtype=float
        )
    )


    for j in range(
        len(
            SUPPORT_LEVELS
        )
    ):

        raster_vec = (
            group.iloc[
                j
            ][
                BANDS
            ]
            .to_numpy(
                dtype=float
            )
        )


        intrinsic_vec = (
            intrinsic_group.iloc[
                j
            ][
                BANDS
            ]
            .to_numpy(
                dtype=float
            )
        )


        dr = (
            raster_vec
            - raster_base
        )


        di = (
            intrinsic_vec
            - intrinsic_base
        )


        rec = {
            "role":
                role,

            "row_index":
                int(
                    group.iloc[
                        j
                    ][
                        "row_index"
                    ]
                ),

            "relative_path":
                str(
                    group.iloc[
                        j
                    ][
                        "relative_path"
                    ]
                ),

            "support_factor":
                float(
                    SUPPORT_LEVELS[
                        j
                    ]
                ),

            "raster_band_l1_from_s1":
                float(
                    np.sum(
                        np.abs(
                            dr
                        )
                    )
                ),

            "intrinsic_band_l1_from_s1":
                float(
                    np.sum(
                        np.abs(
                            di
                        )
                    )
                ),
        }


        for k, band in enumerate(
            BANDS
        ):

            rec[
                f"raster_{band}"
            ] = float(
                raster_vec[
                    k
                ]
            )

            rec[
                f"delta_raster_{band}"
            ] = float(
                dr[
                    k
                ]
            )

            rec[
                f"intrinsic_{band}"
            ] = float(
                intrinsic_vec[
                    k
                ]
            )

            rec[
                f"delta_intrinsic_{band}"
            ] = float(
                di[
                    k
                ]
            )


        trajectory_rows.append(
            rec
        )


trajectory = pd.DataFrame(
    trajectory_rows
).sort_values(
    [
        "role",
        "support_factor",
    ]
).reset_index(
    drop=True
)


require(
    len(
        trajectory
    )
    == 70,
    "Trajectory row count != 70",
)


# =============================================================================
# 4. Object-relative invariance control
# =============================================================================

intrinsic_delta_cols = [
    f"delta_intrinsic_{band}"
    for band in BANDS
]


intrinsic_max_abs_delta = float(
    np.max(
        np.abs(
            trajectory[
                intrinsic_delta_cols
            ].to_numpy(
                dtype=float
            )
        )
    )
)


intrinsic_l1_max = float(
    trajectory[
        "intrinsic_band_l1_from_s1"
    ].max()
)


intrinsic_exact_all = bool(
    intrinsic_max_abs_delta
    == 0.0
    and intrinsic_l1_max
    == 0.0
)


print()
print("=" * 108)
print("OBJECT-RELATIVE CONTROL")
print("=" * 108)

print(
    "All 70 conditions exactly invariant:",
    intrinsic_exact_all,
)

print(
    "Max absolute intrinsic band delta:",
    intrinsic_max_abs_delta,
)

print(
    "Max intrinsic four-band L1:",
    intrinsic_l1_max,
)


require(
    intrinsic_exact_all,
    (
        "Object-relative control is not "
        "exactly invariant"
    ),
)


# =============================================================================
# 5. Per-sentinel directional diagnostics
#
# No hypothesis winner/score.
# Record facts only.
# =============================================================================

sentinel_rows = []


for role, group in trajectory.groupby(
    "role",
    sort=True,
):

    group = group.sort_values(
        "support_factor"
    ).reset_index(
        drop=True
    )


    endpoint = group.iloc[
        -1
    ]


    rec = {
        "role":
            role,

        "row_index":
            int(
                endpoint[
                    "row_index"
                ]
            ),

        "relative_path":
            str(
                endpoint[
                    "relative_path"
                ]
            ),

        "raster_band_l1_s3_minus_s1":
            float(
                endpoint[
                    "raster_band_l1_from_s1"
                ]
            ),

        "raster_band_l1_nondecreasing":
            nondecreasing(
                group[
                    "raster_band_l1_from_s1"
                ].to_numpy(
                    dtype=float
                )
            ),
    }


    for band in BANDS:

        delta_values = group[
            f"delta_raster_{band}"
        ].to_numpy(
            dtype=float
        )


        endpoint_delta = float(
            delta_values[
                -1
            ]
        )


        direction = DIRECTION[
            band
        ]


        rec[
            f"{band}_delta_s3_minus_s1"
        ] = endpoint_delta


        rec[
            f"{band}_endpoint_sign"
        ] = sign_with_zero(
            endpoint_delta
        )


        if direction == +1:

            rec[
                f"{band}_endpoint_direction_concordant"
            ] = bool(
                endpoint_delta
                > 0
            )

            rec[
                f"{band}_trajectory_monotone_in_predicted_direction"
            ] = nondecreasing(
                delta_values
            )


        elif direction == -1:

            rec[
                f"{band}_endpoint_direction_concordant"
            ] = bool(
                endpoint_delta
                < 0
            )

            rec[
                f"{band}_trajectory_monotone_in_predicted_direction"
            ] = nonincreasing(
                delta_values
            )


        else:

            # mid band had no preregistered directional expectation
            rec[
                f"{band}_endpoint_direction_concordant"
            ] = None

            rec[
                f"{band}_trajectory_monotone_in_predicted_direction"
            ] = None


    sentinel_rows.append(
        rec
    )


sentinel = pd.DataFrame(
    sentinel_rows
)


require(
    len(
        sentinel
    )
    == 10,
    "Sentinel summary != 10 rows",
)


# =============================================================================
# 6. Aggregate descriptive trajectory summary
#
# Median/range across sentinel diagnostic cases.
# NOT inferential.
# =============================================================================

aggregate_rows = []


for level, group in trajectory.groupby(
    "support_factor",
    sort=True,
):

    rec = {
        "support_factor":
            float(
                level
            ),

        "sentinels":
            int(
                len(
                    group
                )
            ),

        "median_raster_band_l1_from_s1":
            float(
                np.median(
                    group[
                        "raster_band_l1_from_s1"
                    ]
                )
            ),

        "min_raster_band_l1_from_s1":
            float(
                np.min(
                    group[
                        "raster_band_l1_from_s1"
                    ]
                )
            ),

        "max_raster_band_l1_from_s1":
            float(
                np.max(
                    group[
                        "raster_band_l1_from_s1"
                    ]
                )
            ),
    }


    for band in BANDS:

        vals = group[
            f"delta_raster_{band}"
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
            f"min_delta_{band}"
        ] = float(
            np.min(
                vals
            )
        )

        rec[
            f"max_delta_{band}"
        ] = float(
            np.max(
                vals
            )
        )


        expected_direction = DIRECTION[
            band
        ]


        if expected_direction == +1:

            rec[
                f"n_positive_{band}"
            ] = int(
                np.sum(
                    vals > 0
                )
            )


        elif expected_direction == -1:

            rec[
                f"n_negative_{band}"
            ] = int(
                np.sum(
                    vals < 0
                )
            )


    aggregate_rows.append(
        rec
    )


aggregate = pd.DataFrame(
    aggregate_rows
)


# =============================================================================
# 7. Endpoint descriptive counts
# =============================================================================

endpoint_counts = {}


for band in [
    "low_1_4",
    "highmid_13_24",
    "high_25_36",
]:

    col = (
        f"{band}_"
        "endpoint_direction_concordant"
    )

    endpoint_counts[
        band
    ] = int(
        sentinel[
            col
        ].sum()
    )


monotone_counts = {}


for band in [
    "low_1_4",
    "highmid_13_24",
    "high_25_36",
]:

    col = (
        f"{band}_"
        "trajectory_monotone_in_predicted_direction"
    )

    monotone_counts[
        band
    ] = int(
        sentinel[
            col
        ].sum()
    )


l1_monotone_count = int(
    sentinel[
        "raster_band_l1_nondecreasing"
    ].sum()
)


# =============================================================================
# 8. Save outputs
# =============================================================================

TRAJECTORY_CSV = (
    OUT
    / "P2_R0_05K2_B2_per_condition_trajectories.csv"
)

SENTINEL_CSV = (
    OUT
    / "P2_R0_05K2_B2_per_sentinel_summary.csv"
)

AGGREGATE_CSV = (
    OUT
    / "P2_R0_05K2_B2_support_level_descriptive_summary.csv"
)


trajectory.to_csv(
    TRAJECTORY_CSV,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


sentinel.to_csv(
    SENTINEL_CSV,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


aggregate.to_csv(
    AGGREGATE_CSV,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


# =============================================================================
# 9. Report
# =============================================================================

REPORT_JSON = (
    OUT
    / "P2_R0_05K2_B2_report.json"
)


report = {
    "stage":
        "P2_R0_05K2_B2_SENTINEL_TRAJECTORY_ANALYSIS",

    "status":
        "COMPLETE_DESCRIPTIVE_SENTINEL_ANALYSIS",

    "sentinels":
        10,

    "support_levels":
        SUPPORT_LEVELS.tolist(),

    "population_inference":
        False,

    "object_relative_control": {
        "all_70_exactly_invariant":
            intrinsic_exact_all,

        "max_abs_band_delta":
            intrinsic_max_abs_delta,

        "max_four_band_l1":
            intrinsic_l1_max,
    },

    "raster_preregistered_direction": {
        "low_1_4":
            "increase with canvas support",

        "mid_5_12":
            "no directional requirement",

        "highmid_13_24":
            "decrease with canvas support",

        "high_25_36":
            "decrease with canvas support",
    },

    "endpoint_s3_direction_concordance_counts_of_10":
        endpoint_counts,

    "full_trajectory_monotone_in_predicted_direction_counts_of_10":
        monotone_counts,

    "four_band_l1_nondecreasing_counts_of_10":
        l1_monotone_count,

    "materiality": {
        "threshold_applied":
            False,

        "reason":
            (
                "A 0.005 band-fraction value at s=3 was discussed "
                "previously but was not frozen as an operational "
                "decision rule before descriptor results were opened."
            ),
    },

    "analysis_boundary": {
        "inferential_statistics":
            False,

        "population_generalization":
            False,

        "sentinel_selection_used_for_inference":
            False,

        "mechanism_proof_claim":
            False,
    },

    "interpretation_boundary":
        (
            "B2 describes the preregistered support trajectories of "
            "the ten frozen diagnostic sentinels. Directional and "
            "monotonicity summaries are descriptive controls, not "
            "population-level statistical inference."
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
# 10. Checksums
# =============================================================================

OUTPUTS = [
    TRAJECTORY_CSV,
    SENTINEL_CSV,
    AGGREGATE_CSV,
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

    for p in OUTPUTS:

        f.write(
            f"{sha256_file(p)}  "
            f"{p.name}\n"
        )


# =============================================================================
# 11. Final descriptive output
# =============================================================================

print()
print("=" * 108)
print("P2-R0-05K2-B2 — DESCRIPTIVE RESULTS")
print("=" * 108)

print()
print("OBJECT-RELATIVE CONTROL")
print(
    "70/70 exact band trajectories:",
    intrinsic_exact_all,
)

print(
    "Max intrinsic band delta:",
    intrinsic_max_abs_delta,
)

print()


print("RASTER ENDPOINT DIRECTION, s=3 vs s=1")

for band in [
    "low_1_4",
    "highmid_13_24",
    "high_25_36",
]:

    print(
        band,
        f"{endpoint_counts[band]}/10 concordant",
    )


print()
print("RASTER FULL-TRAJECTORY MONOTONICITY")

for band in [
    "low_1_4",
    "highmid_13_24",
    "high_25_36",
]:

    print(
        band,
        f"{monotone_counts[band]}/10",
    )


print()
print(
    "Four-band L1 nondecreasing:",
    f"{l1_monotone_count}/10",
)


print()
print("MEDIAN TRAJECTORIES")

display_cols = [
    "support_factor",
    "median_delta_low_1_4",
    "median_delta_mid_5_12",
    "median_delta_highmid_13_24",
    "median_delta_high_25_36",
    "median_raster_band_l1_from_s1",
]


print(
    aggregate[
        display_cols
    ].to_string(
        index=False
    )
)


print()
print("s=3 ENDPOINT VALUES BY SENTINEL")

endpoint_cols = [
    "role",
    "low_1_4_delta_s3_minus_s1",
    "mid_5_12_delta_s3_minus_s1",
    "highmid_13_24_delta_s3_minus_s1",
    "high_25_36_delta_s3_minus_s1",
    "raster_band_l1_s3_minus_s1",
]


print(
    sentinel[
        endpoint_cols
    ].to_string(
        index=False
    )
)


print()
print("OUTPUT HASHES")

for p in OUTPUTS:

    print(
        p.name,
        sha256_file(
            p
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
    "Population inference       : NO"
)

print(
    "Materiality threshold used : NO"
)

print(
    "Mechanism proof claimed    : NO"
)

print()
print("=" * 108)
print(
    "STOP — B2 DESCRIPTIVE TRAJECTORY ANALYSIS COMPLETE"
)
print("=" * 108)