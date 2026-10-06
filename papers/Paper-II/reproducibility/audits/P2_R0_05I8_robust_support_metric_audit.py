from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image, ImageOps
from scipy import ndimage


# =============================================================================
# P2-R0-05I8 — ROBUST SUPPORT METRIC AUDIT
#
# Goal
# ----
# Repair the first "tight-support" metric after visual inspection showed that
# max-radius and minimum-border-margin can be dominated by stray/outlier pixels.
#
# Compare, per RAW sketch:
#
#   EXTREME / FRAGILE
#     - max foreground radius / grid radius
#     - minimum foreground border margin
#
#   ROBUST
#     - 99th percentile foreground radius / grid radius
#     - dominant connected-component bbox occupancy
#     - dominant connected-component area fraction
#     - dominant-component border margin
#
# Then report:
#   - population correlations
#   - top-12 examples under each definition
#   - rank overlap between fragile and robust definitions
#   - whether 05I6 "tight-support" exemplars survive robust ranking
#
# This is a descriptive support-definition audit only.
# No Paper-II inference or model selection is modified.
# =============================================================================


I6_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I6_highfreq_text_tightsupport"
)

I6_PER_IMAGE = (
    I6_ROOT
    / "P2_R0_05I6_per_image_metrics.csv"
)

I6_TOP_TIGHT = (
    I6_ROOT
    / "P2_R0_05I6_top_tight_support.csv"
)

OUTPUT_ROOT = (
    I6_ROOT
    / "P2_R0_05I8_robust_support_metric_audit"
)

PER_IMAGE_OUT = (
    OUTPUT_ROOT
    / "P2_R0_05I8_per_image_robust_support_metrics.csv"
)

TOP_FRAGILE_OUT = (
    OUTPUT_ROOT
    / "P2_R0_05I8_top_fragile_support.csv"
)

TOP_ROBUST_OUT = (
    OUTPUT_ROOT
    / "P2_R0_05I8_top_robust_support.csv"
)

SURVIVAL_OUT = (
    OUTPUT_ROOT
    / "P2_R0_05I8_05I6_tight_support_survival.csv"
)

SUMMARY_OUT = (
    OUTPUT_ROOT
    / "P2_R0_05I8_summary.csv"
)

REPORT_JSON = (
    OUTPUT_ROOT
    / "P2_R0_05I8_report.json"
)

RAW_ROOTS = [
    Path("/Users/nitikagupta/Desktop/Clo-Sket"),
    Path("/Users/nitikagupta/Research"),
    Path("/Users/nitikagupta/Desktop"),
]

TOP_K = 12


# =============================================================================
# Helpers
# =============================================================================

def resolve_raw(relative_path: str) -> Path:
    rel = Path(relative_path)

    direct = [
        RAW_ROOTS[0] / rel,
    ]

    for root in RAW_ROOTS[1:]:
        direct.extend(
            [
                root / rel,
                root / "WeaveAI" / rel,
                root / "FashionAI" / "datasets" / "Clo-Sket" / "Clo-Sket" / rel,
            ]
        )

    hits = [
        p.resolve()
        for p in direct
        if p.is_file()
    ]

    hits = sorted(set(hits))

    if hits:
        return Path(hits[0])

    suffix = str(rel).replace("\\", "/")

    for root in RAW_ROOTS:
        if not root.exists():
            continue

        for p in root.rglob(rel.name):
            if not p.is_file():
                continue

            if not str(p).replace("\\", "/").endswith(suffix):
                continue

            hits.append(p.resolve())

    hits = sorted(set(hits))

    if not hits:
        raise RuntimeError(
            f"Could not resolve RAW image: {relative_path}"
        )

    return Path(hits[0])


def load_gray(path: Path) -> np.ndarray:
    with Image.open(path) as im:
        return np.asarray(
            ImageOps.exif_transpose(im).convert("L"),
            dtype=np.uint8,
        )


def weighted_centroid(arr: np.ndarray):
    w = 255.0 - arr.astype(np.float64)
    mass = float(w.sum())

    if mass <= 0:
        raise RuntimeError("Zero grayscale mass")

    yy, xx = np.indices(arr.shape)

    cx = float((w * xx).sum() / mass)
    cy = float((w * yy).sum() / mass)

    return cx, cy


def dominant_component(mask: np.ndarray) -> np.ndarray:
    """
    Largest 8-connected foreground component.
    """
    structure = np.ones((3, 3), dtype=np.uint8)

    labels, n = ndimage.label(
        mask,
        structure=structure,
    )

    if n == 0:
        raise RuntimeError("No foreground component")

    counts = np.bincount(labels.ravel())
    counts[0] = 0

    lab = int(
        counts.argmax()
    )

    return labels == lab


def support_metrics(path: Path) -> dict:
    arr = load_gray(path)
    mask = arr < 245

    if not np.any(mask):
        raise RuntimeError(
            f"No foreground: {path}"
        )

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

    max_radius_ratio = float(
        radii.max()
        / grid_radius
    )

    q99_radius_ratio = float(
        np.quantile(
            radii,
            0.99,
        )
        / grid_radius
    )

    q995_radius_ratio = float(
        np.quantile(
            radii,
            0.995,
        )
        / grid_radius
    )

    left = int(xx.min())
    right = int(w - 1 - xx.max())
    top = int(yy.min())
    bottom = int(h - 1 - yy.max())

    fragile_min_margin = int(
        min(
            left,
            right,
            top,
            bottom,
        )
    )

    fragile_min_margin_norm = float(
        fragile_min_margin
        / max(h, w)
    )

    comp = dominant_component(
        mask
    )

    cyy, cxx = np.where(comp)

    c_left = int(cxx.min())
    c_right = int(w - 1 - cxx.max())
    c_top = int(cyy.min())
    c_bottom = int(h - 1 - cyy.max())

    comp_min_margin = int(
        min(
            c_left,
            c_right,
            c_top,
            c_bottom,
        )
    )

    comp_min_margin_norm = float(
        comp_min_margin
        / max(h, w)
    )

    comp_bbox_w = int(
        cxx.max()
        - cxx.min()
        + 1
    )

    comp_bbox_h = int(
        cyy.max()
        - cyy.min()
        + 1
    )

    comp_bbox_area_fraction = float(
        (
            comp_bbox_w
            * comp_bbox_h
        )
        / (
            w
            * h
        )
    )

    comp_area_fraction = float(
        comp.mean()
    )

    raw_fg_fraction = float(
        mask.mean()
    )

    return {
        "raw_width":
            int(w),

        "raw_height":
            int(h),

        "raw_foreground_fraction":
            raw_fg_fraction,

        "fragile_max_radius_to_grid":
            max_radius_ratio,

        "robust_q99_radius_to_grid":
            q99_radius_ratio,

        "robust_q995_radius_to_grid":
            q995_radius_ratio,

        "fragile_min_border_margin_norm":
            fragile_min_margin_norm,

        "dominant_component_min_border_margin_norm":
            comp_min_margin_norm,

        "dominant_component_bbox_area_fraction":
            comp_bbox_area_fraction,

        "dominant_component_area_fraction":
            comp_area_fraction,
    }


def percentile_rank(
    s: pd.Series,
    ascending_good: bool,
) -> pd.Series:
    """
    Convert to [0,1] rank where larger always means "tighter support".
    """
    r = s.rank(
        pct=True,
        method="average",
        ascending=True,
    )

    if ascending_good:
        return 1.0 - r

    return r


# =============================================================================
# Main
# =============================================================================

def main():

    OUTPUT_ROOT.mkdir(
        parents=True,
        exist_ok=True,
    )

    for p in (
        PER_IMAGE_OUT,
        TOP_FRAGILE_OUT,
        TOP_ROBUST_OUT,
        SURVIVAL_OUT,
        SUMMARY_OUT,
        REPORT_JSON,
    ):
        if p.exists():
            raise RuntimeError(
                f"Refusing to overwrite: {p}"
            )

    i6 = pd.read_csv(
        I6_PER_IMAGE,
        keep_default_na=False,
    )

    if len(i6) != 2300:
        raise RuntimeError(
            f"Expected 2300 rows, got {len(i6)}"
        )

    rows = []

    for j, rec in i6.iterrows():

        p = resolve_raw(
            str(
                rec[
                    "relative_path"
                ]
            )
        )

        metrics = support_metrics(
            p
        )

        rows.append(
            {
                "row_index":
                    int(
                        rec[
                            "row_index"
                        ]
                    ),

                "relative_path":
                    str(
                        rec[
                            "relative_path"
                        ]
                    ),

                "category":
                    str(
                        rec[
                            "category"
                        ]
                    ),

                "garment_id":
                    str(
                        rec[
                            "garment_id"
                        ]
                    ),

                "fold_id":
                    int(
                        rec[
                            "fold_id"
                        ]
                    ),

                "raw_high_25_36_fraction":
                    float(
                        rec[
                            "raw_high_25_36_fraction"
                        ]
                    ),

                **metrics,
            }
        )

        if (
            j + 1
        ) % 250 == 0 or (
            j + 1
        ) == len(i6):
            print(
                f"P2-R0-05I8 support metrics: {j + 1}/{len(i6)}"
            )

    df = pd.DataFrame(
        rows
    )

    # -------------------------------------------------------------------------
    # Fragile composite — mirrors the spirit of the original 05I6 definition.
    # -------------------------------------------------------------------------

    df[
        "fragile_rank_fg_fraction"
    ] = percentile_rank(
        df[
            "raw_foreground_fraction"
        ],
        ascending_good=False,
    )

    df[
        "fragile_rank_max_radius"
    ] = percentile_rank(
        df[
            "fragile_max_radius_to_grid"
        ],
        ascending_good=False,
    )

    df[
        "fragile_rank_min_margin"
    ] = percentile_rank(
        df[
            "fragile_min_border_margin_norm"
        ],
        ascending_good=True,
    )

    df[
        "fragile_support_score"
    ] = (
        df[
            "fragile_rank_fg_fraction"
        ]
        +
        df[
            "fragile_rank_max_radius"
        ]
        +
        df[
            "fragile_rank_min_margin"
        ]
    ) / 3.0

    # -------------------------------------------------------------------------
    # Robust composite.
    #
    # Equal weight:
    #   high q99 radius/grid
    #   high dominant-component bbox area fraction
    #   high dominant-component area fraction
    #   low dominant-component min border margin
    # -------------------------------------------------------------------------

    df[
        "robust_rank_q99_radius"
    ] = percentile_rank(
        df[
            "robust_q99_radius_to_grid"
        ],
        ascending_good=False,
    )

    df[
        "robust_rank_component_bbox"
    ] = percentile_rank(
        df[
            "dominant_component_bbox_area_fraction"
        ],
        ascending_good=False,
    )

    df[
        "robust_rank_component_area"
    ] = percentile_rank(
        df[
            "dominant_component_area_fraction"
        ],
        ascending_good=False,
    )

    df[
        "robust_rank_component_margin"
    ] = percentile_rank(
        df[
            "dominant_component_min_border_margin_norm"
        ],
        ascending_good=True,
    )

    df[
        "robust_support_score"
    ] = (
        df[
            "robust_rank_q99_radius"
        ]
        +
        df[
            "robust_rank_component_bbox"
        ]
        +
        df[
            "robust_rank_component_area"
        ]
        +
        df[
            "robust_rank_component_margin"
        ]
    ) / 4.0

    df.to_csv(
        PER_IMAGE_OUT,
        index=False,
    )

    top_fragile = (
        df
        .sort_values(
            [
                "fragile_support_score",
                "row_index",
            ],
            ascending=[
                False,
                True,
            ],
        )
        .head(
            TOP_K
        )
        .copy()
    )

    top_robust = (
        df
        .sort_values(
            [
                "robust_support_score",
                "row_index",
            ],
            ascending=[
                False,
                True,
            ],
        )
        .head(
            TOP_K
        )
        .copy()
    )

    top_fragile.to_csv(
        TOP_FRAGILE_OUT,
        index=False,
    )

    top_robust.to_csv(
        TOP_ROBUST_OUT,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Rank survival from original 05I6 top-tight cohort.
    # -------------------------------------------------------------------------

    old = pd.read_csv(
        I6_TOP_TIGHT,
        keep_default_na=False,
    )

    robust_rank_map = {
        int(row.row_index):
            rank
        for rank, row in enumerate(
            df.sort_values(
                "robust_support_score",
                ascending=False,
            ).itertuples(
                index=False
            ),
            start=1,
        )
    }

    old[
        "robust_population_rank"
    ] = [
        robust_rank_map[
            int(
                x
            )
        ]
        for x in old[
            "row_index"
        ]
    ]

    old[
        "survives_robust_top12"
    ] = (
        old[
            "robust_population_rank"
        ]
        <= TOP_K
    )

    old.to_csv(
        SURVIVAL_OUT,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Summary relationships.
    # -------------------------------------------------------------------------

    summary_rows = []

    metric_pairs = [
        (
            "fragile_max_radius_to_grid",
            "robust_q99_radius_to_grid",
        ),
        (
            "fragile_min_border_margin_norm",
            "dominant_component_min_border_margin_norm",
        ),
        (
            "fragile_support_score",
            "robust_support_score",
        ),
        (
            "robust_support_score",
            "raw_high_25_36_fraction",
        ),
        (
            "robust_q99_radius_to_grid",
            "raw_high_25_36_fraction",
        ),
        (
            "dominant_component_area_fraction",
            "raw_high_25_36_fraction",
        ),
    ]

    for a, b in metric_pairs:

        pearson = float(
            df[
                [
                    a,
                    b,
                ]
            ].corr(
                method="pearson"
            ).iloc[
                0,
                1,
            ]
        )

        spearman = float(
            df[
                [
                    a,
                    b,
                ]
            ].corr(
                method="spearman"
            ).iloc[
                0,
                1,
            ]
        )

        summary_rows.append(
            {
                "metric_a":
                    a,

                "metric_b":
                    b,

                "pearson_r":
                    pearson,

                "spearman_rho":
                    spearman,
            }
        )

    summary = pd.DataFrame(
        summary_rows
    )

    summary.to_csv(
        SUMMARY_OUT,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Print.
    # -------------------------------------------------------------------------

    print(
        "\n"
        + "=" * 150
    )

    print(
        "P2-R0-05I8 — TOP FRAGILE SUPPORT SCORE"
    )

    print(
        "=" * 150
    )

    print(
        top_fragile[
            [
                "row_index",
                "relative_path",
                "category",
                "fragile_support_score",
                "fragile_max_radius_to_grid",
                "fragile_min_border_margin_norm",
                "dominant_component_area_fraction",
                "raw_high_25_36_fraction",
            ]
        ].to_string(
            index=False
        )
    )

    print(
        "\n"
        + "=" * 150
    )

    print(
        "P2-R0-05I8 — TOP ROBUST SUPPORT SCORE"
    )

    print(
        "=" * 150
    )

    print(
        top_robust[
            [
                "row_index",
                "relative_path",
                "category",
                "robust_support_score",
                "robust_q99_radius_to_grid",
                "dominant_component_bbox_area_fraction",
                "dominant_component_area_fraction",
                "dominant_component_min_border_margin_norm",
                "raw_high_25_36_fraction",
            ]
        ].to_string(
            index=False
        )
    )

    print(
        "\n"
        + "=" * 150
    )

    print(
        "P2-R0-05I8 — ORIGINAL 05I6 TIGHT-SUPPORT SURVIVAL"
    )

    print(
        "=" * 150
    )

    print(
        old[
            [
                "row_index",
                "relative_path",
                "category",
                "robust_population_rank",
                "survives_robust_top12",
            ]
        ].to_string(
            index=False
        )
    )

    print(
        "\n"
        + "=" * 150
    )

    print(
        "P2-R0-05I8 — SUPPORT / HIGH-BAND RELATIONSHIPS"
    )

    print(
        "=" * 150
    )

    print(
        summary.to_string(
            index=False
        )
    )

    overlap = len(
        set(
            top_fragile[
                "row_index"
            ]
        )
        &
        set(
            top_robust[
                "row_index"
            ]
        )
    )

    print(
        f"\nTop-{TOP_K} fragile/robust overlap: {overlap}/{TOP_K}"
    )

    print(
        "Original 05I6 tight-support cases surviving robust top-12:",
        int(
            old[
                "survives_robust_top12"
            ].sum()
        ),
        "/",
        len(
            old
        ),
    )

    report = {
        "stage":
            "P2_R0_05I8_ROBUST_SUPPORT_METRIC_AUDIT",

        "status":
            "COMPLETE",

        "top_k":
            TOP_K,

        "robust_definition":
            (
                "equal-weight percentile composite of q99 foreground radius/grid radius, "
                "dominant-component bbox area fraction, dominant-component area fraction, "
                "and inverse dominant-component minimum border margin"
            ),

        "fragility_question":
            (
                "whether max-radius and minimum-margin support metrics are dominated by "
                "outlier foreground pixels"
            ),

        "outputs":
            {
                "per_image":
                    str(
                        PER_IMAGE_OUT
                    ),

                "top_fragile":
                    str(
                        TOP_FRAGILE_OUT
                    ),

                "top_robust":
                    str(
                        TOP_ROBUST_OUT
                    ),

                "survival":
                    str(
                        SURVIVAL_OUT
                    ),

                "summary":
                    str(
                        SUMMARY_OUT
                    ),
            },

        "interpretation_boundary":
            (
                "This audit evaluates support-measure robustness. "
                "It does not establish causal relationships with high-frequency energy."
            ),
    }

    REPORT_JSON.write_text(
        json.dumps(
            report,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        "\nP2-R0-05I8 ROBUST SUPPORT METRIC AUDIT: COMPLETE"
    )

    print(
        "Per-image:",
        PER_IMAGE_OUT,
    )

    print(
        "Top robust:",
        TOP_ROBUST_OUT,
    )

    print(
        "Survival:",
        SURVIVAL_OUT,
    )

    print(
        "Summary:",
        SUMMARY_OUT,
    )

    print(
        "Report:",
        REPORT_JSON,
    )

    print(
        "\nSTOP — inspect robust-support output before 05J."
    )


if __name__ == "__main__":
    main()
