from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image, ImageOps
from scipy import ndimage, stats


# =============================================================================
# P2-R0-05J — POPULATION SUPPORT–SPECTRAL MECHANISM AUDIT
#
# Scientific question
# -------------------
# Across all 2300 frozen sketches, does RAW→CROP spectral redistribution in
# the GRID-RELATIVE representation track changes in raster-relative support
# geometry?
#
# Important boundary
# ------------------
# This audit DOES NOT "re-prove" 05H1 intrinsic invariance.
#
# 05H1 already established, exactly, that when the same garment pixels are
# represented in centroid-centered / max-foreground-radius object coordinates,
# RAW-box and CROP produce identical intrinsic fields.
#
# Therefore 05J uses:
#   A) population RAW→CROP GRID-RELATIVE spectral shifts
#   B) population RAW→CROP robust support-geometry shifts
#   C) association / stratification analysis
#
# and treats 05H1 as the frozen object-relative control:
#
#   same object pixels + object-relative coordinates
#       => representation discrepancy = 0 by construction/oracle result.
#
# No model selection.
# No manuscript mechanism claim is made automatically.
# Association != causation.
# =============================================================================


ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I6_highfreq_text_tightsupport"
)

I6_PER_IMAGE = (
    ROOT
    / "P2_R0_05I6_per_image_metrics.csv"
)

I8_PER_IMAGE = (
    ROOT
    / "P2_R0_05I8_robust_support_metric_audit/"
    "P2_R0_05I8_per_image_robust_support_metrics.csv"
)

V3_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05f_crop_only/"
    "V3_CROP_ONLY"
)

V3_MANIFEST_CANDIDATES = [
    V3_ROOT / "materialized_manifest.csv",
    V3_ROOT / "manifest.csv",
    Path(
        "/Users/nitikagupta/Research/"
        "paper2_r0_05f_crop_only/"
        "V3_CROP_ONLY/materialized_manifest.csv"
    ),
]

OUT_ROOT = (
    ROOT
    / "P2_R0_05J_population_support_spectral_audit"
)

PER_IMAGE_OUT = (
    OUT_ROOT
    / "P2_R0_05J_per_image_population_metrics.csv"
)

ASSOC_OUT = (
    OUT_ROOT
    / "P2_R0_05J_associations.csv"
)

STRATA_OUT = (
    OUT_ROOT
    / "P2_R0_05J_support_change_strata.csv"
)

CATEGORY_OUT = (
    OUT_ROOT
    / "P2_R0_05J_category_summary.csv"
)

REPORT_OUT = (
    OUT_ROOT
    / "P2_R0_05J_report.json"
)

TOP_OUT = (
    OUT_ROOT
    / "P2_R0_05J_top_support_change_cases.csv"
)

N_EXPECTED = 2300
N_PERM = 10000
SEED = 20260909


# =============================================================================
# Column discovery
# =============================================================================

BAND_CANDIDATES = {
    "low": {
        "raw": [
            "raw_low_1_4_fraction",
            "raw_low_fraction",
        ],
        "crop": [
            "crop_low_1_4_fraction",
            "crop_low_fraction",
            "crop_only_low_1_4_fraction",
        ],
    },

    "mid": {
        "raw": [
            "raw_mid_5_12_fraction",
            "raw_mid_fraction",
        ],
        "crop": [
            "crop_mid_5_12_fraction",
            "crop_mid_fraction",
            "crop_only_mid_5_12_fraction",
        ],
    },

    "highmid": {
        "raw": [
            "raw_highmid_13_24_fraction",
            "raw_highmid_fraction",
        ],
        "crop": [
            "crop_highmid_13_24_fraction",
            "crop_highmid_fraction",
            "crop_only_highmid_13_24_fraction",
        ],
    },

    "high": {
        "raw": [
            "raw_high_25_36_fraction",
            "raw_high_fraction",
        ],
        "crop": [
            "crop_high_25_36_fraction",
            "crop_high_fraction",
            "crop_only_high_25_36_fraction",
        ],
    },
}


def first_existing(columns, candidates):
    for c in candidates:
        if c in columns:
            return c
    return None


# =============================================================================
# Support geometry
# =============================================================================

def load_gray(path: Path) -> np.ndarray:
    with Image.open(path) as im:
        return np.asarray(
            ImageOps.exif_transpose(im).convert("L"),
            dtype=np.uint8,
        )


def dominant_component(mask: np.ndarray) -> np.ndarray:
    labels, n = ndimage.label(
        mask,
        structure=np.ones((3, 3), dtype=np.uint8),
    )

    if n == 0:
        raise RuntimeError("No foreground component")

    counts = np.bincount(labels.ravel())
    counts[0] = 0

    return labels == int(counts.argmax())


def weighted_centroid(arr: np.ndarray):
    w = 255.0 - arr.astype(np.float64)
    mass = float(w.sum())

    if mass <= 0:
        raise RuntimeError("Zero grayscale mass")

    yy, xx = np.indices(arr.shape)

    cx = float((w * xx).sum() / mass)
    cy = float((w * yy).sum() / mass)

    return cx, cy


def robust_support_metrics(path: Path) -> dict:
    arr = load_gray(path)
    mask = arr < 245

    if not np.any(mask):
        raise RuntimeError(f"No foreground in {path}")

    h, w = arr.shape

    cx, cy = weighted_centroid(arr)

    yy, xx = np.where(mask)

    radii = np.sqrt(
        (xx - cx) ** 2
        + (yy - cy) ** 2
    )

    corners = np.array(
        [
            [0, 0],
            [w - 1, 0],
            [0, h - 1],
            [w - 1, h - 1],
        ],
        dtype=np.float64,
    )

    grid_radius = float(
        np.sqrt(
            (corners[:, 0] - cx) ** 2
            + (corners[:, 1] - cy) ** 2
        ).max()
    )

    q99 = float(
        np.quantile(radii, 0.99)
        / grid_radius
    )

    comp = dominant_component(mask)
    cyy, cxx = np.where(comp)

    bbox_w = int(cxx.max() - cxx.min() + 1)
    bbox_h = int(cyy.max() - cyy.min() + 1)

    bbox_frac = float(
        bbox_w * bbox_h
        / (w * h)
    )

    area_frac = float(comp.mean())

    min_margin = min(
        int(cxx.min()),
        int(w - 1 - cxx.max()),
        int(cyy.min()),
        int(h - 1 - cyy.max()),
    )

    margin_norm = float(
        min_margin
        / max(h, w)
    )

    return {
        "q99_radius_to_grid": q99,
        "component_bbox_area_fraction": bbox_frac,
        "component_area_fraction": area_frac,
        "component_min_border_margin_norm": margin_norm,
    }


# =============================================================================
# V3 manifest resolution
# =============================================================================

def find_v3_manifest() -> Path:
    for p in V3_MANIFEST_CANDIDATES:
        if p.is_file():
            return p

    raise RuntimeError(
        "Could not find V3_CROP_ONLY manifest. Tried:\n"
        + "\n".join(
            str(p)
            for p in V3_MANIFEST_CANDIDATES
        )
    )


def resolve_crop_path(
    rec: pd.Series,
    manifest_root: Path,
) -> Path:

    candidate_columns = [
        "output_path",
        "output_file",
        "materialized_path",
        "crop_path",
        "output_relative_path",
    ]

    for col in candidate_columns:
        if col not in rec.index:
            continue

        val = str(rec[col]).strip()

        if not val:
            continue

        p = Path(val)

        if p.is_file():
            return p.resolve()

        q = manifest_root / p

        if q.is_file():
            return q.resolve()

    raise RuntimeError(
        f"Unable to resolve crop output for {rec.get('relative_path', '<unknown>')}"
    )


# =============================================================================
# Statistics
# =============================================================================

def category_center(
    df: pd.DataFrame,
    col: str,
) -> pd.Series:
    return (
        df[col]
        - df.groupby("category")[col].transform("mean")
    )


def permutation_spearman(
    x: np.ndarray,
    y: np.ndarray,
    groups: np.ndarray,
    n_perm: int = N_PERM,
    seed: int = SEED,
):
    """
    Category-preserving permutation:
    shuffle y within category.
    Two-sided test on |rho|.
    """

    good = (
        np.isfinite(x)
        & np.isfinite(y)
    )

    x = x[good]
    y = y[good]
    groups = groups[good]

    observed = float(
        stats.spearmanr(
            x,
            y,
        ).statistic
    )

    rng = np.random.default_rng(seed)

    idx_by_group = {
        g: np.flatnonzero(groups == g)
        for g in np.unique(groups)
    }

    exceed = 0

    for _ in range(n_perm):
        yp = y.copy()

        for idx in idx_by_group.values():
            yp[idx] = rng.permutation(
                yp[idx]
            )

        rho = float(
            stats.spearmanr(
                x,
                yp,
            ).statistic
        )

        if abs(rho) >= abs(observed):
            exceed += 1

    p = (
        exceed + 1
    ) / (
        n_perm + 1
    )

    return observed, float(p)


def bh_fdr(pvals):
    pvals = np.asarray(
        pvals,
        dtype=float,
    )

    n = len(pvals)

    order = np.argsort(pvals)
    ranked = pvals[order]

    q = ranked * n / np.arange(
        1,
        n + 1,
    )

    q = np.minimum.accumulate(
        q[::-1]
    )[::-1]

    q = np.clip(
        q,
        0,
        1,
    )

    out = np.empty_like(q)
    out[order] = q

    return out


# =============================================================================
# Main
# =============================================================================

def main():

    OUT_ROOT.mkdir(
        parents=True,
        exist_ok=True,
    )

    for p in [
        PER_IMAGE_OUT,
        ASSOC_OUT,
        STRATA_OUT,
        CATEGORY_OUT,
        REPORT_OUT,
        TOP_OUT,
    ]:
        if p.exists():
            raise RuntimeError(
                f"Refusing to overwrite: {p}"
            )

    i6 = pd.read_csv(
        I6_PER_IMAGE,
        keep_default_na=False,
    )

    i8 = pd.read_csv(
        I8_PER_IMAGE,
        keep_default_na=False,
    )

    if len(i6) != N_EXPECTED:
        raise RuntimeError(
            f"05I6 expected {N_EXPECTED}, got {len(i6)}"
        )

    if len(i8) != N_EXPECTED:
        raise RuntimeError(
            f"05I8 expected {N_EXPECTED}, got {len(i8)}"
        )

    key = [
        "row_index",
        "relative_path",
        "category",
        "garment_id",
        "fold_id",
    ]

    base = i6.merge(
        i8[
            key
            + [
                "robust_q99_radius_to_grid",
                "dominant_component_bbox_area_fraction",
                "dominant_component_area_fraction",
                "dominant_component_min_border_margin_norm",
                "robust_support_score",
            ]
        ],
        on=key,
        how="inner",
        validate="one_to_one",
    )

    if len(base) != N_EXPECTED:
        raise RuntimeError(
            f"Merged population expected {N_EXPECTED}, got {len(base)}"
        )

    # -------------------------------------------------------------------------
    # Discover frozen RAW/CROP band columns.
    # -------------------------------------------------------------------------

    band_cols = {}

    for band, spec in BAND_CANDIDATES.items():

        raw_col = first_existing(
            base.columns,
            spec["raw"],
        )

        crop_col = first_existing(
            base.columns,
            spec["crop"],
        )

        if raw_col is None or crop_col is None:
            print("\nAVAILABLE 05I6 COLUMNS:")
            print("\n".join(base.columns))
            raise RuntimeError(
                f"Could not discover RAW/CROP columns for band={band}. "
                f"raw={raw_col}, crop={crop_col}"
            )

        band_cols[band] = {
            "raw": raw_col,
            "crop": crop_col,
        }

    # -------------------------------------------------------------------------
    # Resolve V3 crop images and compute ROBUST CROP support metrics.
    # -------------------------------------------------------------------------

    v3_manifest_path = find_v3_manifest()

    v3 = pd.read_csv(
        v3_manifest_path,
        keep_default_na=False,
    )

    if "relative_path" not in v3.columns:
        raise RuntimeError(
            "V3 manifest has no relative_path column.\n"
            f"Columns: {list(v3.columns)}"
        )

    v3_map = {
        str(rec["relative_path"]):
            resolve_crop_path(
                rec,
                v3_manifest_path.parent,
            )
        for _, rec in v3.iterrows()
    }

    crop_rows = []

    for j, rec in base.iterrows():

        rel = str(
            rec[
                "relative_path"
            ]
        )

        if rel not in v3_map:
            raise RuntimeError(
                f"Missing V3 crop for {rel}"
            )

        m = robust_support_metrics(
            v3_map[rel]
        )

        crop_rows.append(
            m
        )

        if (
            j + 1
        ) % 250 == 0 or (
            j + 1
        ) == len(base):
            print(
                f"P2-R0-05J crop support metrics: {j + 1}/{len(base)}"
            )

    crop_df = pd.DataFrame(
        crop_rows
    ).add_prefix(
        "crop_"
    )

    df = pd.concat(
        [
            base.reset_index(drop=True),
            crop_df.reset_index(drop=True),
        ],
        axis=1,
    )

    # -------------------------------------------------------------------------
    # RAW→CROP support changes.
    # -------------------------------------------------------------------------

    df[
        "delta_q99_radius_to_grid"
    ] = (
        df[
            "crop_q99_radius_to_grid"
        ]
        -
        df[
            "robust_q99_radius_to_grid"
        ]
    )

    df[
        "delta_component_bbox_area_fraction"
    ] = (
        df[
            "crop_component_bbox_area_fraction"
        ]
        -
        df[
            "dominant_component_bbox_area_fraction"
        ]
    )

    df[
        "delta_component_area_fraction"
    ] = (
        df[
            "crop_component_area_fraction"
        ]
        -
        df[
            "dominant_component_area_fraction"
        ]
    )

    df[
        "delta_component_min_border_margin_norm"
    ] = (
        df[
            "crop_component_min_border_margin_norm"
        ]
        -
        df[
            "dominant_component_min_border_margin_norm"
        ]
    )

    # -------------------------------------------------------------------------
    # RAW→CROP band redistribution.
    # -------------------------------------------------------------------------

    for band, cols in band_cols.items():

        df[
            f"raw_{band}_frozen"
        ] = pd.to_numeric(
            df[
                cols["raw"]
            ]
        )

        df[
            f"crop_{band}_frozen"
        ] = pd.to_numeric(
            df[
                cols["crop"]
            ]
        )

        df[
            f"delta_{band}_fraction"
        ] = (
            df[
                f"crop_{band}_frozen"
            ]
            -
            df[
                f"raw_{band}_frozen"
            ]
        )

    # L1 redistribution over four frozen bands.
    delta_band_cols = [
        f"delta_{b}_fraction"
        for b in [
            "low",
            "mid",
            "highmid",
            "high",
        ]
    ]

    df[
        "band_redistribution_l1"
    ] = (
        df[
            delta_band_cols
        ]
        .abs()
        .sum(
            axis=1
        )
    )

    df[
        "abs_delta_high_fraction"
    ] = (
        df[
            "delta_high_fraction"
        ].abs()
    )

    # -------------------------------------------------------------------------
    # Category-centered association tests.
    # -------------------------------------------------------------------------

    support_changes = [
        "delta_q99_radius_to_grid",
        "delta_component_bbox_area_fraction",
        "delta_component_area_fraction",
        "delta_component_min_border_margin_norm",
    ]

    spectral_targets = [
        "delta_low_fraction",
        "delta_mid_fraction",
        "delta_highmid_fraction",
        "delta_high_fraction",
        "abs_delta_high_fraction",
        "band_redistribution_l1",
    ]

    assoc_rows = []

    for xcol in support_changes:

        xcc = category_center(
            df,
            xcol,
        ).to_numpy(
            dtype=float
        )

        for ycol in spectral_targets:

            ycc = category_center(
                df,
                ycol,
            ).to_numpy(
                dtype=float
            )

            rho, p = permutation_spearman(
                xcc,
                ycc,
                df[
                    "category"
                ].astype(
                    str
                ).to_numpy(),
            )

            assoc_rows.append(
                {
                    "support_metric":
                        xcol,

                    "spectral_target":
                        ycol,

                    "category_centered_spearman_rho":
                        rho,

                    "permutation_p":
                        p,
                }
            )

    assoc = pd.DataFrame(
        assoc_rows
    )

    assoc[
        "bh_fdr_q"
    ] = bh_fdr(
        assoc[
            "permutation_p"
        ].to_numpy()
    )

    assoc.to_csv(
        ASSOC_OUT,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Support-change strata.
    #
    # Descriptive: quartiles of Δ q99 radius/grid.
    # -------------------------------------------------------------------------

    df[
        "delta_q99_quartile"
    ] = pd.qcut(
        df[
            "delta_q99_radius_to_grid"
        ],
        q=4,
        labels=[
            "Q1_smallest",
            "Q2",
            "Q3",
            "Q4_largest",
        ],
        duplicates="drop",
    )

    strata = (
        df.groupby(
            "delta_q99_quartile",
            observed=True,
        )
        .agg(
            n=(
                "row_index",
                "size",
            ),

            median_delta_q99=(
                "delta_q99_radius_to_grid",
                "median",
            ),

            median_delta_low=(
                "delta_low_fraction",
                "median",
            ),

            median_delta_mid=(
                "delta_mid_fraction",
                "median",
            ),

            median_delta_highmid=(
                "delta_highmid_fraction",
                "median",
            ),

            median_delta_high=(
                "delta_high_fraction",
                "median",
            ),

            median_abs_delta_high=(
                "abs_delta_high_fraction",
                "median",
            ),

            median_band_l1=(
                "band_redistribution_l1",
                "median",
            ),
        )
        .reset_index()
    )

    strata.to_csv(
        STRATA_OUT,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Category summary.
    # -------------------------------------------------------------------------

    category = (
        df.groupby(
            "category"
        )
        .agg(
            n=(
                "row_index",
                "size",
            ),

            median_delta_q99=(
                "delta_q99_radius_to_grid",
                "median",
            ),

            median_delta_high=(
                "delta_high_fraction",
                "median",
            ),

            median_abs_delta_high=(
                "abs_delta_high_fraction",
                "median",
            ),

            median_band_l1=(
                "band_redistribution_l1",
                "median",
            ),
        )
        .reset_index()
        .sort_values(
            "median_abs_delta_high",
            ascending=False,
        )
    )

    category.to_csv(
        CATEGORY_OUT,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Top support-change cases — frozen only after population computation.
    # -------------------------------------------------------------------------

    top = (
        df.assign(
            abs_delta_q99=
                df[
                    "delta_q99_radius_to_grid"
                ].abs()
        )
        .sort_values(
            [
                "abs_delta_q99",
                "row_index",
            ],
            ascending=[
                False,
                True,
            ],
        )
        .head(
            24
        )
    )

    top[
        [
            "row_index",
            "relative_path",
            "category",
            "garment_id",
            "fold_id",
            "robust_q99_radius_to_grid",
            "crop_q99_radius_to_grid",
            "delta_q99_radius_to_grid",
            "delta_low_fraction",
            "delta_mid_fraction",
            "delta_highmid_fraction",
            "delta_high_fraction",
            "band_redistribution_l1",
        ]
    ].to_csv(
        TOP_OUT,
        index=False,
    )

    df.to_csv(
        PER_IMAGE_OUT,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Console report.
    # -------------------------------------------------------------------------

    print(
        "\n"
        + "=" * 150
    )

    print(
        "P2-R0-05J — CATEGORY-CENTERED SUPPORT ↔ SPECTRAL ASSOCIATIONS"
    )

    print(
        "=" * 150
    )

    print(
        assoc.sort_values(
            [
                "bh_fdr_q",
                "permutation_p",
            ]
        ).to_string(
            index=False
        )
    )

    print(
        "\n"
        + "=" * 150
    )

    print(
        "P2-R0-05J — ΔQ99 SUPPORT-CHANGE QUARTILES"
    )

    print(
        "=" * 150
    )

    print(
        strata.to_string(
            index=False
        )
    )

    print(
        "\n"
        + "=" * 150
    )

    print(
        "P2-R0-05J — CATEGORIES WITH LARGEST MEDIAN |ΔHIGH|"
    )

    print(
        "=" * 150
    )

    print(
        category.head(
            23
        ).to_string(
            index=False
        )
    )

    print(
        "\n"
        + "=" * 150
    )

    print(
        "P2-R0-05J — INTERPRETATION BOUNDARY"
    )

    print(
        "=" * 150
    )

    print(
        "GRID-RELATIVE population question: "
        "does RAW→CROP support change covary with band redistribution?"
    )

    print(
        "OBJECT-RELATIVE control: 05H1 already established exact RAW-box↔CROP "
        "intrinsic-field equality for identical garment pixels."
    )

    print(
        "Therefore 05J must not be described as proving that support change "
        "'causes' spectral redistribution."
    )

    print(
        "It tests whether raster-relative support change is a population-level "
        "predictor/associate of GRID-RELATIVE redistribution."
    )

    report = {
        "stage":
            "P2_R0_05J_POPULATION_SUPPORT_SPECTRAL_MECHANISM_AUDIT",

        "status":
            "COMPLETE",

        "n":
            int(
                len(df)
            ),

        "question":
            (
                "Across all 2300 sketches, does RAW-to-CROP grid-relative "
                "spectral redistribution track robust raster-relative support change?"
            ),

        "object_relative_control":
            (
                "05H1 frozen oracle result: identical garment pixels represented "
                "in centroid-centered / max-foreground-radius intrinsic coordinates "
                "produce exact RAW-box vs CROP field equality."
            ),

        "statistical_design":
            {
                "association":
                    "category-centered Spearman",

                "permutation":
                    (
                        f"{N_PERM} category-preserving permutations, "
                        "two-sided"
                    ),

                "multiple_testing":
                    "Benjamini-Hochberg FDR over 24 association tests",
            },

        "support_metrics":
            support_changes,

        "spectral_targets":
            spectral_targets,

        "outputs":
            {
                "per_image":
                    str(
                        PER_IMAGE_OUT
                    ),

                "associations":
                    str(
                        ASSOC_OUT
                    ),

                "strata":
                    str(
                        STRATA_OUT
                    ),

                "category":
                    str(
                        CATEGORY_OUT
                    ),

                "top_cases":
                    str(
                        TOP_OUT
                    ),
            },

        "interpretation_boundary":
            (
                "Association does not establish causation. "
                "Intrinsic invariance is an already-frozen oracle representation fact, "
                "not a new 05J statistical finding."
            ),
    }

    REPORT_OUT.write_text(
        json.dumps(
            report,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        "\nP2-R0-05J POPULATION SUPPORT–SPECTRAL AUDIT: COMPLETE"
    )

    print(
        "Per-image:",
        PER_IMAGE_OUT,
    )

    print(
        "Associations:",
        ASSOC_OUT,
    )

    print(
        "Strata:",
        STRATA_OUT,
    )

    print(
        "Category summary:",
        CATEGORY_OUT,
    )

    print(
        "Top cases:",
        TOP_OUT,
    )

    print(
        "Report:",
        REPORT_OUT,
    )

    print(
        "\nSTOP — interpret 05J before any manuscript mechanism wording."
    )


if __name__ == "__main__":
    main()