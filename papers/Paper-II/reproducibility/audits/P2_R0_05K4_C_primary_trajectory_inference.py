from pathlib import Path
import hashlib
import json
import math

import numpy as np
import pandas as pd


# =============================================================================
# P2-R0-05K4-C
# PRIMARY TRAJECTORY + CATEGORY-LEVEL INFERENTIAL ANALYSIS
#
# PRIMARY INTERVENTION:
#   2300 frozen images × 7 support levels
#
# DESCRIPTIVE:
#   Δband(s) = band(s) - band(1)
#   endpoint direction at s=3
#   image-level trajectory monotonicity
#   support-level median/IQR
#   category endpoint summaries
#
# PREREGISTERED DIRECTIONAL ENDPOINTS:
#   low_1_4       : increase
#   highmid_13_24 : decrease
#   high_25_36    : decrease
#
# MID BAND:
#   descriptive only
#
# INFERENCE:
#   - one endpoint effect per category = median across that category's 100 images
#   - 23 categories are the sign-flip units
#   - directionalize effects so all alternatives are > 0
#   - exact sign-flip enumeration over 2^23 configurations
#   - same sign vector applied jointly to all three bands
#   - one-sided raw p-values
#   - max-T FWER correction across the 3 preregistered bands
#
# IMPORTANT:
#   This does NOT treat 2300 image rows as independent inferential units.
#   No materiality threshold is applied.
#   No external-population generalization is claimed.
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
    / "05K4_C_primary_trajectory_inference"
)

OUT.mkdir(
    parents=True,
    exist_ok=True,
)


# =============================================================================
# Frozen 05K4-B package
# =============================================================================

B_DIR = (
    FROZEN
    / "05K4_B_Primary_Descriptor_Execution_v1_0"
)

RASTER_CSV = (
    B_DIR
    / "P2_R0_05K4_B_raster_band_fractions_16100.csv"
)

INTRINSIC_CSV = (
    B_DIR
    / "P2_R0_05K4_B_intrinsic_band_fractions_16100.csv"
)

CONTROLS_CSV = (
    B_DIR
    / "P2_R0_05K4_B_numerical_controls_16100.csv"
)

B_REPORT = (
    B_DIR
    / "P2_R0_05K4_B_report.json"
)


EXPECTED_SHA = {
    "raster":
        "ca96cbac776a9d7cf6466a98132c3817917b7720c5ab559be15f8bfe0ada531e",

    "intrinsic":
        "9c44242ea24eeef56f36e15552b4fe9e34c721d0ab8e893aecc6be8ae1a71253",

    "controls":
        "4d589e7dbd6131caa457444e9428c75f24a2b9feaa771365dfcc8aa91f68f798",

    "report":
        "be3cb72f645dfc3e5b618da5755b510bb6a09a0e0aef73ec414266f3c856290e",
}


EXPECTED_IMAGES = 2300
EXPECTED_CATEGORIES = 23
EXPECTED_IMAGES_PER_CATEGORY = 100
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


# Directionalized sign:
# +1 means original delta expected positive
# -1 means original delta expected negative
DIRECTION_SIGN = {
    "low_1_4":
        +1.0,

    "highmid_13_24":
        -1.0,

    "high_25_36":
        -1.0,
}


TESTED_BANDS = [
    "low_1_4",
    "highmid_13_24",
    "high_25_36",
]


# Exact sign-flip enumeration:
# 2^23 = 8,388,608 configurations.
SIGNFLIP_BATCH_SIZE = 131072


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


def quantile(values, q):
    return float(
        np.quantile(
            np.asarray(
                values,
                dtype=np.float64,
            ),
            q,
        )
    )


def nondecreasing(values, tol=1e-15):
    values = np.asarray(
        values,
        dtype=np.float64,
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
        dtype=np.float64,
    )

    return bool(
        np.all(
            np.diff(values)
            <= tol
        )
    )


def one_sample_t_stat(values):
    """
    Studentized location statistic across category effects.

    Alternative after directionalization: mean(values) > 0.
    """

    x = np.asarray(
        values,
        dtype=np.float64,
    )

    n = len(x)

    require(
        n >= 2,
        "Need >=2 category effects",
    )

    mean = float(
        x.mean()
    )

    sd = float(
        x.std(
            ddof=1
        )
    )

    require(
        sd > 0.0,
        "Zero category-effect standard deviation",
    )

    return float(
        mean
        / (
            sd
            / math.sqrt(
                n
            )
        )
    )


# =============================================================================
# Exact joint sign-flip max-T
# =============================================================================

def exact_joint_signflip_maxT(
    directional_category_effects,
    band_names,
    batch_size=131072,
):
    """
    directional_category_effects:
        array shape (n_categories, n_bands)

    All alternatives are positive after directionalization.

    Exact enumeration of every 2^n sign assignment.

    Same category sign vector is applied jointly to all tested bands,
    preserving cross-band dependence.

    Returns:
        observed_t
        raw one-sided exact p
        max-T FWER exact p
        number of sign configurations
    """

    X = np.asarray(
        directional_category_effects,
        dtype=np.float64,
    )

    require(
        X.ndim == 2,
        "Directional effect matrix must be 2-D",
    )

    n_categories, n_bands = X.shape

    require(
        n_categories == EXPECTED_CATEGORIES,
        (
            f"Expected {EXPECTED_CATEGORIES} categories; "
            f"got {n_categories}"
        ),
    )

    require(
        n_bands == len(
            band_names
        ),
        "Band-count mismatch",
    )


    # -------------------------------------------------------------------------
    # Observed studentized statistics
    # -------------------------------------------------------------------------

    observed_t = np.asarray(
        [
            one_sample_t_stat(
                X[
                    :,
                    j
                ]
            )
            for j in range(
                n_bands
            )
        ],
        dtype=np.float64,
    )


    # -------------------------------------------------------------------------
    # Exact sign-flip distribution
    #
    # For signed values z_i = sign_i * x_i:
    #
    # sum(z_i^2) is invariant under sign flips.
    #
    # Thus variance can be computed from:
    #   SS = sum(x_i^2)
    #   mean = sum(z_i)/n
    #   var = [SS - n*mean^2] / (n-1)
    # -------------------------------------------------------------------------

    sumsq = np.sum(
        X ** 2,
        axis=0,
    )


    total_configurations = (
        1 << n_categories
    )


    raw_exceed = np.zeros(
        n_bands,
        dtype=np.int64,
    )

    maxT_exceed = np.zeros(
        n_bands,
        dtype=np.int64,
    )


    bit_positions = np.arange(
        n_categories,
        dtype=np.uint64,
    )


    for start in range(
        0,
        total_configurations,
        batch_size,
    ):

        stop = min(
            start + batch_size,
            total_configurations,
        )


        ids = np.arange(
            start,
            stop,
            dtype=np.uint64,
        )


        # Bit 0 -> -1
        # Bit 1 -> +1
        bits = (
            (
                ids[
                    :,
                    None
                ]
                >> bit_positions[
                    None,
                    :
                ]
            )
            & np.uint64(
                1
            )
        )


        signs = (
            bits.astype(
                np.float64
            )
            * 2.0
            - 1.0
        )


        # shape:
        # batch × bands
        signed_sums = (
            signs
            @ X
        )


        means = (
            signed_sums
            / float(
                n_categories
            )
        )


        variance_numerator = (
            sumsq[
                None,
                :
            ]
            -
            float(
                n_categories
            )
            * means ** 2
        )


        # Guard tiny negative floating error.
        variance_numerator = np.maximum(
            variance_numerator,
            0.0,
        )


        variances = (
            variance_numerator
            / float(
                n_categories
                - 1
            )
        )


        standard_errors = (
            np.sqrt(
                variances
            )
            / math.sqrt(
                n_categories
            )
        )


        # If a rare configuration produces zero variance:
        # + mean -> +inf
        # - mean -> -inf
        # zero mean -> 0
        t_values = np.zeros_like(
            means,
            dtype=np.float64,
        )


        nonzero_se = (
            standard_errors
            > 0.0
        )


        t_values[
            nonzero_se
        ] = (
            means[
                nonzero_se
            ]
            /
            standard_errors[
                nonzero_se
            ]
        )


        zero_se = ~nonzero_se


        t_values[
            zero_se
            & (
                means > 0.0
            )
        ] = np.inf


        t_values[
            zero_se
            & (
                means < 0.0
            )
        ] = -np.inf


        # ---------------------------------------------------------------------
        # Raw one-sided exact p
        # ---------------------------------------------------------------------

        for j in range(
            n_bands
        ):

            raw_exceed[
                j
            ] += int(
                np.sum(
                    t_values[
                        :,
                        j
                    ]
                    >= observed_t[
                        j
                    ]
                    - 1e-15
                )
            )


        # ---------------------------------------------------------------------
        # max-T FWER
        #
        # For each sign configuration:
        #   M = max(T_low, T_highmid, T_high)
        #
        # Adjusted p_j =
        #   P(M >= T_observed_j)
        # ---------------------------------------------------------------------

        max_t = np.max(
            t_values,
            axis=1,
        )


        for j in range(
            n_bands
        ):

            maxT_exceed[
                j
            ] += int(
                np.sum(
                    max_t
                    >= observed_t[
                        j
                    ]
                    - 1e-15
                )
            )


    raw_p = (
        raw_exceed.astype(
            np.float64
        )
        / float(
            total_configurations
        )
    )


    fwer_p = (
        maxT_exceed.astype(
            np.float64
        )
        / float(
            total_configurations
        )
    )


    return {
        "observed_t":
            observed_t,

        "raw_p":
            raw_p,

        "fwer_p":
            fwer_p,

        "raw_exceed":
            raw_exceed,

        "maxT_exceed":
            maxT_exceed,

        "total_configurations":
            int(
                total_configurations
            ),
    }


# =============================================================================
# Header
# =============================================================================

print("=" * 116)
print(
    "P2-R0-05K4-C — "
    "PRIMARY TRAJECTORY + CATEGORY-LEVEL INFERENTIAL ANALYSIS"
)
print("=" * 116)

print("Images                    :", EXPECTED_IMAGES)
print("Categories                :", EXPECTED_CATEGORIES)
print("Images/category           :", EXPECTED_IMAGES_PER_CATEGORY)
print("Support levels            :", len(SUPPORT_LEVELS))
print()

print("Inferential unit          : category")
print("Sign-flip units           : 23 categories")
print(
    "Exact sign configurations:",
    1 << EXPECTED_CATEGORIES,
)
print("Tested directional bands  :", TESTED_BANDS)
print("Mid band inference        : NO")
print("Materiality threshold     : NOT APPLIED")
print("External generalization   : NO")
print()


# =============================================================================
# 1. Verify frozen inputs
# =============================================================================

for label, path in [
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
        B_REPORT,
    ),
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


b_report = json.loads(
    B_REPORT.read_text(
        encoding="utf-8"
    )
)


require(
    b_report[
        "status"
    ]
    == "COMPLETE_DESCRIPTOR_EXECUTION_ONLY",
    "Unexpected 05K4-B report status",
)


require(
    b_report[
        "analysis_boundary"
    ][
        "directional_hypotheses_tested"
    ]
    is False,
    "05K4-B already claims directional testing",
)


# =============================================================================
# 2. Load frozen descriptor outputs
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
        len(df)
        == EXPECTED_CONDITIONS,
        (
            f"{label}: expected "
            f"{EXPECTED_CONDITIONS} rows"
        ),
    )


require(
    raster[
        "row_index"
    ].nunique()
    == EXPECTED_IMAGES,
    "Raster unique image count != 2300",
)


require(
    raster[
        "category"
    ].nunique()
    == EXPECTED_CATEGORIES,
    "Raster category count != 23",
)


category_image_counts = (
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
    category_image_counts.min()
    == EXPECTED_IMAGES_PER_CATEGORY
    and
    category_image_counts.max()
    == EXPECTED_IMAGES_PER_CATEGORY,
    (
        "Expected exactly 100 "
        "source images/category"
    ),
)


# =============================================================================
# 3. Object-relative control gate
# =============================================================================

intrinsic_field_exact = bool(
    controls[
        "intrinsic_field_exact_from_s1"
    ]
    .astype(bool)
    .all()
)


intrinsic_band_exact = bool(
    controls[
        "intrinsic_band_exact_from_s1"
    ]
    .astype(bool)
    .all()
)


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


require(
    intrinsic_field_exact,
    "Intrinsic field control failed",
)


require(
    intrinsic_band_exact,
    "Intrinsic band control failed",
)


require(
    intrinsic_max_field_diff
    == 0.0,
    "Intrinsic field control is not exact",
)


require(
    intrinsic_max_band_diff
    == 0.0,
    "Intrinsic band control is not exact",
)


print()
print("=" * 116)
print("OBJECT-RELATIVE CONTROL")
print("=" * 116)

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

print(
    "Max field difference:",
    intrinsic_max_field_diff,
)

print(
    "Max band difference:",
    intrinsic_max_band_diff,
)


# =============================================================================
# 4. Build per-image baseline-relative trajectories
# =============================================================================

trajectory_rows = []


for row_index, group in raster.groupby(
    "row_index",
    sort=True,
):

    group = (
        group.sort_values(
            "support_factor",
            kind="mergesort",
        )
        .reset_index(
            drop=True
        )
    )


    observed_support = (
        group[
            "support_factor"
        ]
        .to_numpy(
            dtype=np.float64
        )
    )


    require(
        np.allclose(
            observed_support,
            SUPPORT_LEVELS,
            atol=1e-12,
            rtol=0.0,
        ),
        (
            f"row_index={row_index}: "
            "support levels differ from frozen design"
        ),
    )


    base = (
        group.iloc[
            0
        ][
            BANDS
        ]
        .to_numpy(
            dtype=np.float64
        )
    )


    for _, row in group.iterrows():

        current = (
            row[
                BANDS
            ]
            .to_numpy(
                dtype=np.float64
            )
        )


        delta = (
            current
            - base
        )


        # Four fractions sum to one, hence delta sum should be zero.
        delta_sum = float(
            delta.sum()
        )


        require(
            abs(
                delta_sum
            )
            <= 5e-12,
            (
                "Band-delta conservation failed: "
                f"row={row_index}, "
                f"s={row['support_factor']}, "
                f"sum={delta_sum}"
            ),
        )


        rec = {
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


        for j, band in enumerate(
            BANDS
        ):

            rec[
                f"raster_{band}"
            ] = float(
                current[
                    j
                ]
            )

            rec[
                f"delta_{band}"
            ] = float(
                delta[
                    j
                ]
            )


        trajectory_rows.append(
            rec
        )


trajectory = pd.DataFrame(
    trajectory_rows
)


require(
    len(
        trajectory
    )
    == EXPECTED_CONDITIONS,
    "Trajectory rows != 16100",
)


# =============================================================================
# 5. Per-image endpoint + monotonicity
# =============================================================================

image_rows = []


for row_index, group in trajectory.groupby(
    "row_index",
    sort=True,
):

    group = (
        group.sort_values(
            "support_factor",
            kind="mergesort",
        )
        .reset_index(
            drop=True
        )
    )


    endpoint = group.iloc[
        -1
    ]


    rec = {
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
                    dtype=np.float64
                )
            ),
    }


    for band in BANDS:

        deltas = (
            group[
                f"delta_{band}"
            ]
            .to_numpy(
                dtype=np.float64
            )
        )


        endpoint_delta = float(
            deltas[
                -1
            ]
        )


        rec[
            f"{band}_delta_s3_minus_s1"
        ] = endpoint_delta


        if band == "low_1_4":

            rec[
                f"{band}_endpoint_direction_concordant"
            ] = bool(
                endpoint_delta
                > 0.0
            )

            rec[
                f"{band}_trajectory_monotone_in_predicted_direction"
            ] = nondecreasing(
                deltas
            )


        elif band in [
            "highmid_13_24",
            "high_25_36",
        ]:

            rec[
                f"{band}_endpoint_direction_concordant"
            ] = bool(
                endpoint_delta
                < 0.0
            )

            rec[
                f"{band}_trajectory_monotone_in_predicted_direction"
            ] = nonincreasing(
                deltas
            )


        else:

            # Mid band had no directional prediction.
            rec[
                f"{band}_endpoint_direction_concordant"
            ] = None

            rec[
                f"{band}_trajectory_monotone_in_predicted_direction"
            ] = None


    image_rows.append(
        rec
    )


image_summary = pd.DataFrame(
    image_rows
)


require(
    len(
        image_summary
    )
    == EXPECTED_IMAGES,
    "Per-image endpoint summary != 2300",
)


# =============================================================================
# 6. Whole-dataset descriptive support trajectories
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

        "images":
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

        vals = (
            group[
                f"delta_{band}"
            ]
            .to_numpy(
                dtype=np.float64
            )
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
# 7. Image-level descriptive direction counts
#
# DESCRIPTIVE ONLY.
# These counts are NOT the inferential test.
# =============================================================================

image_endpoint_counts = {}
image_endpoint_percent = {}

image_monotone_counts = {}
image_monotone_percent = {}


for band in TESTED_BANDS:

    endpoint_col = (
        f"{band}_"
        "endpoint_direction_concordant"
    )

    monotone_col = (
        f"{band}_"
        "trajectory_monotone_in_predicted_direction"
    )


    endpoint_n = int(
        image_summary[
            endpoint_col
        ]
        .astype(bool)
        .sum()
    )


    monotone_n = int(
        image_summary[
            monotone_col
        ]
        .astype(bool)
        .sum()
    )


    image_endpoint_counts[
        band
    ] = endpoint_n


    image_endpoint_percent[
        band
    ] = float(
        100.0
        * endpoint_n
        / EXPECTED_IMAGES
    )


    image_monotone_counts[
        band
    ] = monotone_n


    image_monotone_percent[
        band
    ] = float(
        100.0
        * monotone_n
        / EXPECTED_IMAGES
    )


l1_monotone_n = int(
    image_summary[
        "four_band_l1_nondecreasing"
    ]
    .astype(bool)
    .sum()
)


l1_monotone_percent = float(
    100.0
    * l1_monotone_n
    / EXPECTED_IMAGES
)


# =============================================================================
# 8. Category-level endpoint effects
#
# PRIMARY INFERENTIAL EFFECT PER CATEGORY:
# median endpoint delta across the 100 images in that category.
# =============================================================================

category_rows = []


for category, group in image_summary.groupby(
    "category",
    sort=True,
):

    require(
        len(
            group
        )
        == EXPECTED_IMAGES_PER_CATEGORY,
        (
            f"{category}: expected 100 images; "
            f"got {len(group)}"
        ),
    )


    rec = {
        "category":
            str(
                category
            ),

        "images":
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

        vals = (
            group[
                f"{band}_delta_s3_minus_s1"
            ]
            .to_numpy(
                dtype=np.float64
            )
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


        if band == "low_1_4":

            rec[
                f"n_endpoint_concordant_{band}"
            ] = int(
                np.sum(
                    vals > 0.0
                )
            )


        elif band in [
            "highmid_13_24",
            "high_25_36",
        ]:

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
    len(
        category_summary
    )
    == EXPECTED_CATEGORIES,
    "Category endpoint summary != 23 rows",
)


# =============================================================================
# 9. Construct directionalized category effect matrix
#
# Columns:
#   low      = +median delta low
#   highmid  = -median delta highmid
#   high     = -median delta high
#
# Hence positive = preregistered direction for every tested band.
# =============================================================================

directional_matrix = np.column_stack(
    [
        category_summary[
            f"median_delta_{band}"
        ].to_numpy(
            dtype=np.float64
        )
        * DIRECTION_SIGN[
            band
        ]
        for band in TESTED_BANDS
    ]
)


require(
    directional_matrix.shape
    == (
        EXPECTED_CATEGORIES,
        len(
            TESTED_BANDS
        ),
    ),
    "Directional category matrix has wrong shape",
)


# =============================================================================
# 10. Exact joint sign-flip inference
# =============================================================================

print()
print("=" * 116)
print("EXACT CATEGORY-LEVEL SIGN-FLIP INFERENCE")
print("=" * 116)

print(
    "Enumerating",
    1 << EXPECTED_CATEGORIES,
    "joint sign configurations..."
)


signflip = exact_joint_signflip_maxT(
    directional_category_effects=directional_matrix,
    band_names=TESTED_BANDS,
    batch_size=SIGNFLIP_BATCH_SIZE,
)


print(
    "Exact enumeration complete."
)


# =============================================================================
# 11. Inferential result table
# =============================================================================

inference_rows = []


for j, band in enumerate(
    TESTED_BANDS
):

    original_category_effects = (
        category_summary[
            f"median_delta_{band}"
        ]
        .to_numpy(
            dtype=np.float64
        )
    )


    directional_effects = (
        directional_matrix[
            :,
            j
        ]
    )


    if DIRECTION_SIGN[
        band
    ] > 0:

        expected_direction = "increase"

        n_category_medians_concordant = int(
            np.sum(
                original_category_effects
                > 0.0
            )
        )

    else:

        expected_direction = "decrease"

        n_category_medians_concordant = int(
            np.sum(
                original_category_effects
                < 0.0
            )
        )


    inference_rows.append({
        "band":
            band,

        "expected_direction":
            expected_direction,

        "categories":
            EXPECTED_CATEGORIES,

        "category_medians_direction_concordant":
            n_category_medians_concordant,

        "median_original_category_effect":
            float(
                np.median(
                    original_category_effects
                )
            ),

        "mean_original_category_effect":
            float(
                np.mean(
                    original_category_effects
                )
            ),

        "median_directionalized_category_effect":
            float(
                np.median(
                    directional_effects
                )
            ),

        "mean_directionalized_category_effect":
            float(
                np.mean(
                    directional_effects
                )
            ),

        "observed_studentized_T":
            float(
                signflip[
                    "observed_t"
                ][
                    j
                ]
            ),

        "raw_one_sided_exact_p":
            float(
                signflip[
                    "raw_p"
                ][
                    j
                ]
            ),

        "maxT_FWER_exact_p":
            float(
                signflip[
                    "fwer_p"
                ][
                    j
                ]
            ),

        "raw_exceeding_configurations":
            int(
                signflip[
                    "raw_exceed"
                ][
                    j
                ]
            ),

        "maxT_exceeding_configurations":
            int(
                signflip[
                    "maxT_exceed"
                ][
                    j
                ]
            ),

        "total_sign_configurations":
            int(
                signflip[
                    "total_configurations"
                ]
            ),
    })


inference = pd.DataFrame(
    inference_rows
)


# =============================================================================
# 12. Save outputs
# =============================================================================

TRAJECTORY_CSV = (
    OUT
    / "P2_R0_05K4_C_per_condition_trajectories_16100.csv"
)

IMAGE_CSV = (
    OUT
    / "P2_R0_05K4_C_per_image_endpoint_summary_2300.csv"
)

SUPPORT_CSV = (
    OUT
    / "P2_R0_05K4_C_support_level_descriptive_summary.csv"
)

CATEGORY_CSV = (
    OUT
    / "P2_R0_05K4_C_category_endpoint_effects_23.csv"
)

INFERENCE_CSV = (
    OUT
    / "P2_R0_05K4_C_exact_category_signflip_inference.csv"
)


trajectory.to_csv(
    TRAJECTORY_CSV,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


image_summary.to_csv(
    IMAGE_CSV,
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


inference.to_csv(
    INFERENCE_CSV,
    index=False,
    lineterminator="\n",
    float_format="%.17g",
)


# =============================================================================
# 13. Report
# =============================================================================

REPORT_JSON = (
    OUT
    / "P2_R0_05K4_C_report.json"
)


report = {
    "stage":
        "P2_R0_05K4_C_PRIMARY_TRAJECTORY_AND_INFERENCE",

    "status":
        "COMPLETE_PRIMARY_ANALYSIS",

    "source_images":
        EXPECTED_IMAGES,

    "categories":
        EXPECTED_CATEGORIES,

    "images_per_category":
        EXPECTED_IMAGES_PER_CATEGORY,

    "support_levels":
        SUPPORT_LEVELS.tolist(),

    "primary_endpoint":
        "s=3.00 minus s=1.00 band-fraction change",

    "tested_directional_bands": {
        "low_1_4":
            "increase",

        "highmid_13_24":
            "decrease",

        "high_25_36":
            "decrease",
    },

    "mid_band":
        "descriptive only",

    "object_relative_control": {
        "all_16100_fields_exact":
            intrinsic_field_exact,

        "all_16100_band_vectors_exact":
            intrinsic_band_exact,

        "max_field_difference":
            intrinsic_max_field_diff,

        "max_band_difference":
            intrinsic_max_band_diff,
    },

    "image_level_descriptive_endpoint": {
        "direction_concordance_counts_of_2300":
            image_endpoint_counts,

        "direction_concordance_percent":
            image_endpoint_percent,

        "trajectory_monotonicity_counts_of_2300":
            image_monotone_counts,

        "trajectory_monotonicity_percent":
            image_monotone_percent,

        "four_band_l1_nondecreasing_count":
            l1_monotone_n,

        "four_band_l1_nondecreasing_percent":
            l1_monotone_percent,
    },

    "inference": {
        "unit":
            "category",

        "n_units":
            EXPECTED_CATEGORIES,

        "within_category_endpoint_estimator":
            "median across 100 images",

        "test":
            "exact joint sign-flip studentized max-T",

        "sign_configurations":
            int(
                signflip[
                    "total_configurations"
                ]
            ),

        "same_sign_vector_across_bands":
            True,

        "familywise_control":
            "max-T across the 3 preregistered directional bands",

        "one_sided":
            True,

        "results":
            inference.to_dict(
                orient="records"
            ),
    },

    "materiality": {
        "threshold_applied":
            False,

        "reason":
            (
                "No operational materiality threshold "
                "was frozen before outcomes were opened."
            ),
    },

    "scope_boundary": {
        "image_rows_treated_as_independent_inferential_units":
            False,

        "category_level_inference":
            True,

        "external_population_generalization":
            False,

        "universal_monotonic_mechanism_claim":
            False,

        "mechanism_wording":
            (
                "Any supported conclusion is limited to "
                "support dependence under the frozen "
                "raster-relative coordinate normalization."
            ),
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
# 14. Checksums
# =============================================================================

OUTPUTS = [
    TRAJECTORY_CSV,
    IMAGE_CSV,
    SUPPORT_CSV,
    CATEGORY_CSV,
    INFERENCE_CSV,
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
# 15. Final results
# =============================================================================

print()
print("=" * 116)
print(
    "P2-R0-05K4-C — PRIMARY RESULTS"
)
print("=" * 116)


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
print("IMAGE-LEVEL ENDPOINT DIRECTION — DESCRIPTIVE ONLY")

for band in TESTED_BANDS:

    print(
        f"{band:17s}",
        f"{image_endpoint_counts[band]}/{EXPECTED_IMAGES}",
        f"({image_endpoint_percent[band]:.1f}%)",
    )


print()
print("IMAGE-LEVEL FULL-TRAJECTORY MONOTONICITY — DESCRIPTIVE ONLY")

for band in TESTED_BANDS:

    print(
        f"{band:17s}",
        f"{image_monotone_counts[band]}/{EXPECTED_IMAGES}",
        f"({image_monotone_percent[band]:.1f}%)",
    )


print()

print(
    "Four-band L1 nondecreasing:",
    f"{l1_monotone_n}/{EXPECTED_IMAGES}",
    f"({l1_monotone_percent:.1f}%)",
)


print()
print("SUPPORT-LEVEL MEDIAN / IQR TRAJECTORIES")

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
print("CATEGORY MEDIAN ENDPOINT DIRECTION")

for band in TESTED_BANDS:

    row = inference.loc[
        inference[
            "band"
        ]
        == band
    ].iloc[
        0
    ]

    print(
        f"{band:17s}",
        f"{int(row['category_medians_direction_concordant'])}"
        f"/{EXPECTED_CATEGORIES}",
    )


print()
print("EXACT CATEGORY-LEVEL SIGN-FLIP INFERENCE")

print(
    inference[
        [
            "band",
            "expected_direction",
            "median_original_category_effect",
            "mean_original_category_effect",
            "observed_studentized_T",
            "raw_one_sided_exact_p",
            "maxT_FWER_exact_p",
        ]
    ]
    .to_string(
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
print("Inferential unit                 : CATEGORY")
print("Image rows independent?          : NO")
print("Exact sign-flip configurations   :", 1 << EXPECTED_CATEGORIES)
print("FWER correction                  : JOINT max-T")
print("Materiality threshold applied    : NO")
print("External-population claim        : NO")
print("Universal monotonicity claim     : NO")

print()
print("=" * 116)
print(
    "STOP — FREEZE 05K4-C BEFORE 05K SYNTHESIS"
)
print("=" * 116)