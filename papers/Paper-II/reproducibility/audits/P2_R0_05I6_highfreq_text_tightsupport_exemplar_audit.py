from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image, ImageOps


# =============================================================================
# P2-R0-05I6 — HIGH-FREQUENCY / TEXT-SENSITIVITY / TIGHT-SUPPORT EXEMPLAR AUDIT
#
# Purpose
# -------
# Freeze three descriptive exemplar cohorts BEFORE any further Canvas inspection:
#
#   A) HIGH_FREQUENCY:
#      sketches with the largest RAW high-band fraction (k=25..36)
#
#   B) TEXT_SENSITIVE:
#      text-positive sketches with the largest RAW -> TEXT_BLANKED
#      4-band L1 redistribution
#
#   C) TIGHT_SUPPORT:
#      sketches with little whitespace / strong object occupation
#
# Also report intersections among these cohorts.
#
# Important
# ---------
# - This is a visualization/exemplar audit only.
# - It does not alter Paper-II inference or model selection.
# - Geometry notes (lace, zip, button, pleat, ruffle, etc.) must be added
#   only AFTER ranking/selection, never used as ranking inputs.
# =============================================================================


AUDIT_DIR = Path(__file__).resolve().parent

BASE_AUDIT = (
    AUDIT_DIR
    / "P2_R0_05_annotation_control_sensitivity.py"
)

PREPROCESS_MANIFEST = Path(
    "/Users/nitikagupta/Research/"
    "experiment08_preprocessing_freeze/"
    "experiment08_preprocessing_manifest.csv"
)

V1_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05e_preprocessing_ablation/"
    "V1_TEXT_ONLY"
)

V1_MANIFEST = (
    V1_ROOT
    / "materialized_manifest.csv"
)

OUTPUT_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I6_highfreq_text_tightsupport"
)

PER_IMAGE_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05I6_per_image_metrics.csv"
)

TOP_HIGH_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05I6_top_high_frequency.csv"
)

TOP_TEXT_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05I6_top_text_sensitive.csv"
)

TOP_TIGHT_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05I6_top_tight_support.csv"
)

INTERSECTIONS_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05I6_intersections.csv"
)

REPORT_JSON = (
    OUTPUT_ROOT
    / "P2_R0_05I6_report.json"
)

EXPECTED_ROWS = 2300

TOP_K = 12

BANDS = {
    "low_1_4": np.arange(1, 5, dtype=int),
    "mid_5_12": np.arange(5, 13, dtype=int),
    "highmid_13_24": np.arange(13, 25, dtype=int),
    "high_25_36": np.arange(25, 37, dtype=int),
}


# =============================================================================
# Helpers
# =============================================================================

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()

    with path.open("rb") as f:
        for chunk in iter(
            lambda: f.read(1024 * 1024),
            b"",
        ):
            h.update(chunk)

    return h.hexdigest()


def load_verified_definitions():

    source = BASE_AUDIT.read_text(
        encoding="utf-8"
    )

    marker = 'if __name__ == "__main__":'

    namespace = {
        "__file__": str(BASE_AUDIT),
        "__name__": "p2_r0_05_verified_definitions",
    }

    exec(
        compile(
            source.split(marker, 1)[0],
            str(BASE_AUDIT),
            "exec",
        ),
        namespace,
    )

    required = [
        "load_paper2_runtime",
        "validate_geometry_equivalence",
        "normalize_runtime_relative_path",
    ]

    missing = [
        x
        for x in required
        if x not in namespace
    ]

    if missing:
        raise RuntimeError(
            f"Missing verified definitions: {missing}"
        )

    print(
        "P2-R0-05I6 VERIFIED DEFINITIONS: PASS"
    )

    return namespace


def resolve_raw_display_path(
    historical_runtime_path: Path,
    relative_path: str,
    expected_source_sha256: str,
) -> Path:

    expected_source_sha256 = str(
        expected_source_sha256
    ).strip()

    def verified(
        p: Path
    ) -> bool:
        return (
            p.is_file()
            and
            (
                not expected_source_sha256
                or sha256_file(
                    p
                )
                == expected_source_sha256
            )
        )

    if verified(
        historical_runtime_path
    ):
        return historical_runtime_path

    rel = Path(
        relative_path
    )

    roots = [
        Path(
            "/Users/nitikagupta/Desktop/Clo-Sket"
        ),
        Path(
            "/Users/nitikagupta/Research"
        ),
        Path(
            "/Users/nitikagupta/Desktop"
        ),
    ]

    direct = [
        roots[
            0
        ]
        / rel,
    ]

    for root in roots[
        1:
    ]:
        direct.extend(
            [
                root
                / rel,

                root
                / "WeaveAI"
                / rel,

                root
                / "FashionAI"
                / "datasets"
                / "Clo-Sket"
                / "Clo-Sket"
                / rel,
            ]
        )

    hits = [
        p.resolve()
        for p in direct
        if verified(
            p
        )
    ]

    hits = sorted(
        set(
            hits
        )
    )

    if hits:
        return Path(
            hits[
                0
            ]
        )

    suffix = str(
        rel
    ).replace(
        "\\",
        "/",
    )

    for root in roots:

        if not root.exists():
            continue

        for p in root.rglob(
            rel.name
        ):

            p_norm = str(
                p
            ).replace(
                "\\",
                "/",
            )

            if not p_norm.endswith(
                suffix
            ):
                continue

            if verified(
                p
            ):
                hits.append(
                    p.resolve()
                )

    hits = sorted(
        set(
            hits
        )
    )

    if not hits:
        raise RuntimeError(
            f"Could not resolve RAW raster for {relative_path}"
        )

    return Path(
        hits[
            0
        ]
    )


def reconstruct_full_variant(
    ra14_module,
    runtime_paths: np.ndarray,
    runtime_categories: np.ndarray,
    manifest_path: Path,
    root: Path,
    label: str,
) -> np.ndarray:

    manifest = pd.read_csv(
        manifest_path,
        keep_default_na=False,
    ).sort_values(
        "row_index"
    ).reset_index(
        drop=True
    )

    manifest_paths = manifest[
        "relative_path"
    ].astype(str).to_numpy()

    if not np.array_equal(
        runtime_paths,
        manifest_paths,
    ):
        raise RuntimeError(
            f"{label} manifest/runtime order mismatch"
        )

    rows = []

    for i, rec in manifest.iterrows():

        p = (
            root
            / str(
                rec[
                    "output_relative_path"
                ]
            )
        )

        if not p.is_file():
            raise RuntimeError(
                f"Missing {label} image: {p}"
            )

        rows.append(
            {
                "relative_path":
                    str(
                        rec[
                            "relative_path"
                        ]
                    ),

                "category":
                    str(
                        runtime_categories[
                            i
                        ]
                    ),

                "path":
                    p,
            }
        )

    print(
        f"\nP2-R0-05I6 — reconstructing full {label} geometry..."
    )

    (
        conditional,
        _nonempty,
        _radial_centers,
        mass_error,
        norm_error,
    ) = ra14_module.recover_geometry(
        rows
    )

    conditional = np.asarray(
        conditional,
        dtype=np.float64,
    )

    if conditional.shape != (
        EXPECTED_ROWS,
        72,
        72,
    ):
        raise RuntimeError(
            f"Unexpected {label} field shape: {conditional.shape}"
        )

    if not np.isfinite(
        conditional
    ).all():
        raise RuntimeError(
            f"{label} field contains non-finite values"
        )

    print(
        f"P2-R0-05I6 {label} FULL RECONSTRUCTION: PASS"
    )

    print(
        "Max mass error:",
        mass_error,
    )

    print(
        "Max normalization error:",
        norm_error,
    )

    return conditional


def band_fractions(
    conditional: np.ndarray,
) -> pd.DataFrame:

    F = np.fft.rfft(
        np.asarray(
            conditional,
            dtype=np.float64,
        ),
        axis=2,
    )

    harmonic_energy = (
        np.abs(
            F
        ) ** 2
    ).sum(
        axis=1
    )

    total = harmonic_energy[
        :,
        1:37,
    ].sum(
        axis=1
    )

    if np.any(
        total
        <= 0
    ):
        raise RuntimeError(
            "Non-positive non-DC energy"
        )

    out = {}

    for name, ks in BANDS.items():
        out[
            name
        ] = (
            harmonic_energy[
                :,
                ks,
            ].sum(
                axis=1
            )
            / total
        )

    return pd.DataFrame(
        out
    )


def support_metrics(
    path: Path,
):
    """
    Tight-support metrics from RAW grayscale darkness.

    Foreground definition for this descriptive audit:
        grayscale < 245

    Metrics:
      - foreground_fraction
      - foreground_radius_to_grid_radius
      - minimum border margin (pixels and normalized)
    """

    with Image.open(
        path
    ) as im:
        arr = np.asarray(
            ImageOps.exif_transpose(
                im
            ).convert(
                "L"
            ),
            dtype=np.uint8,
        )

    mask = arr < 245

    h, w = mask.shape

    if not np.any(
        mask
    ):
        raise RuntimeError(
            f"No foreground detected: {path}"
        )

    yy, xx = np.where(
        mask
    )

    fg_fraction = float(
        mask.mean()
    )

    weights = (
        255.0
        - arr.astype(
            np.float64
        )
    )

    mass = float(
        weights.sum()
    )

    gy, gx = np.indices(
        arr.shape
    )

    cx = float(
        (
            weights
            * gx
        ).sum()
        / mass
    )

    cy = float(
        (
            weights
            * gy
        ).sum()
        / mass
    )

    r_fg = np.sqrt(
        (
            xx
            - cx
        ) ** 2
        +
        (
            yy
            - cy
        ) ** 2
    ).max()

    corners = np.array(
        [
            [
                0,
                0,
            ],
            [
                w - 1,
                0,
            ],
            [
                0,
                h - 1,
            ],
            [
                w - 1,
                h - 1,
            ],
        ],
        dtype=np.float64,
    )

    r_grid = np.sqrt(
        (
            corners[
                :,
                0,
            ]
            - cx
        ) ** 2
        +
        (
            corners[
                :,
                1,
            ]
            - cy
        ) ** 2
    ).max()

    fg_grid_ratio = float(
        r_fg
        / r_grid
    )

    left = int(
        xx.min()
    )

    right = int(
        w - 1 - xx.max()
    )

    top = int(
        yy.min()
    )

    bottom = int(
        h - 1 - yy.max()
    )

    min_margin = int(
        min(
            left,
            right,
            top,
            bottom,
        )
    )

    min_margin_norm = float(
        min_margin
        / max(
            h,
            w,
        )
    )

    return {
        "raw_foreground_fraction":
            fg_fraction,

        "raw_foreground_radius_to_grid_radius":
            fg_grid_ratio,

        "raw_min_border_margin_px":
            min_margin,

        "raw_min_border_margin_norm":
            min_margin_norm,

        "raw_width":
            int(
                w
            ),

        "raw_height":
            int(
                h
            ),
    }


# =============================================================================
# Main
# =============================================================================

def main():

    OUTPUT_ROOT.mkdir(
        parents=True,
        exist_ok=True,
    )

    for p in (
        PER_IMAGE_CSV,
        TOP_HIGH_CSV,
        TOP_TEXT_CSV,
        TOP_TIGHT_CSV,
        INTERSECTIONS_CSV,
        REPORT_JSON,
    ):
        if p.exists():
            raise RuntimeError(
                f"Refusing to overwrite: {p}"
            )

    base = load_verified_definitions()

    runtime = base[
        "load_paper2_runtime"
    ]()

    (
        ra14_module,
        raw_conditional,
    ) = base[
        "validate_geometry_equivalence"
    ](
        runtime
    )

    runtime_paths = np.asarray(
        [
            base[
                "normalize_runtime_relative_path"
            ](
                x
            )
            for x in runtime[
                "image_paths"
            ]
        ],
        dtype=str,
    )

    runtime_categories = np.asarray(
        runtime[
            "image_categories"
        ],
        dtype=str,
    )

    runtime_raw_paths = [
        Path(
            x
        )
        for x in runtime[
            "image_paths"
        ]
    ]

    v1_df = pd.read_csv(
        V1_MANIFEST,
        keep_default_na=False,
    ).sort_values(
        "row_index"
    ).reset_index(
        drop=True
    )

    text_conditional = reconstruct_full_variant(
        ra14_module,
        runtime_paths,
        runtime_categories,
        V1_MANIFEST,
        V1_ROOT,
        "TEXT_BLANKED",
    )

    raw_frac = band_fractions(
        raw_conditional
    )

    text_frac = band_fractions(
        text_conditional
    )

    freeze = pd.read_csv(
        PREPROCESS_MANIFEST,
        keep_default_na=False,
    ).sort_values(
        "row_index"
    ).reset_index(
        drop=True
    )

    if len(
        freeze
    ) != EXPECTED_ROWS:
        raise RuntimeError(
            "Unexpected preprocessing manifest length"
        )

    if not np.array_equal(
        freeze[
            "relative_path"
        ].astype(
            str
        ).to_numpy(),
        runtime_paths,
    ):
        raise RuntimeError(
            "Preprocessing manifest/runtime order mismatch"
        )

    source_sha_map = {
        str(
            rec[
                "relative_path"
            ]
        ):
        str(
            rec[
                "source_sha256"
            ]
        )
        for _, rec in v1_df.iterrows()
    }

    rows = []

    for i in range(
        EXPECTED_ROWS
    ):

        rel = runtime_paths[
            i
        ]

        raw_path = resolve_raw_display_path(
            runtime_raw_paths[
                i
            ],
            rel,
            source_sha_map[
                rel
            ],
        )

        sm = support_metrics(
            raw_path
        )

        delta = (
            text_frac.iloc[
                i
            ].to_numpy(
                dtype=float
            )
            -
            raw_frac.iloc[
                i
            ].to_numpy(
                dtype=float
            )
        )

        text_l1 = float(
            np.abs(
                delta
            ).sum()
        )

        rec = freeze.iloc[
            i
        ]

        rows.append(
            {
                "row_index":
                    int(
                        i
                    ),

                "relative_path":
                    rel,

                "category":
                    str(
                        runtime_categories[
                            i
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

                "n_text_boxes":
                    int(
                        rec[
                            "text_boxes_json"
                        ]
                        not in (
                            "",
                            "[]",
                        )
                    ),

                "raw_low_1_4_fraction":
                    float(
                        raw_frac.iloc[
                            i
                        ][
                            "low_1_4"
                        ]
                    ),

                "raw_mid_5_12_fraction":
                    float(
                        raw_frac.iloc[
                            i
                        ][
                            "mid_5_12"
                        ]
                    ),

                "raw_highmid_13_24_fraction":
                    float(
                        raw_frac.iloc[
                            i
                        ][
                            "highmid_13_24"
                        ]
                    ),

                "raw_high_25_36_fraction":
                    float(
                        raw_frac.iloc[
                            i
                        ][
                            "high_25_36"
                        ]
                    ),

                "raw_to_text_band_l1_change":
                    text_l1,

                "delta_text_low_1_4":
                    float(
                        delta[
                            0
                        ]
                    ),

                "delta_text_mid_5_12":
                    float(
                        delta[
                            1
                        ]
                    ),

                "delta_text_highmid_13_24":
                    float(
                        delta[
                            2
                        ]
                    ),

                "delta_text_high_25_36":
                    float(
                        delta[
                            3
                        ]
                    ),

                **sm,
            }
        )

        if (
            i + 1
        ) % 250 == 0 or (
            i + 1
        ) == EXPECTED_ROWS:
            print(
                f"P2-R0-05I6 support metrics: {i + 1}/{EXPECTED_ROWS}"
            )

    df = pd.DataFrame(
        rows
    )

    # -------------------------------------------------------------------------
    # Tight-support composite ranking.
    #
    # We do not hide the definition:
    #   high foreground fraction  -> tighter
    #   high fg/grid radius ratio -> tighter
    #   low normalized min margin -> tighter
    #
    # Use within-dataset percentile ranks, equal weight.
    # -------------------------------------------------------------------------

    df[
        "tight_rank_fg_fraction"
    ] = df[
        "raw_foreground_fraction"
    ].rank(
        pct=True,
        method="average",
    )

    df[
        "tight_rank_fg_grid_ratio"
    ] = df[
        "raw_foreground_radius_to_grid_radius"
    ].rank(
        pct=True,
        method="average",
    )

    df[
        "tight_rank_margin"
    ] = (
        1.0
        -
        df[
            "raw_min_border_margin_norm"
        ].rank(
            pct=True,
            method="average",
        )
    )

    df[
        "tight_support_score"
    ] = (
        df[
            "tight_rank_fg_fraction"
        ]
        +
        df[
            "tight_rank_fg_grid_ratio"
        ]
        +
        df[
            "tight_rank_margin"
        ]
    ) / 3.0

    df.to_csv(
        PER_IMAGE_CSV,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Cohort A — highest RAW high-band fraction.
    # -------------------------------------------------------------------------

    top_high = (
        df
        .sort_values(
            [
                "raw_high_25_36_fraction",
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

    top_high[
        "selection_cohort"
    ] = "HIGH_FREQUENCY"

    top_high[
        "geometry_note_after_selection"
    ] = ""

    top_high.to_csv(
        TOP_HIGH_CSV,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Cohort B — strongest text sensitivity.
    # Require frozen text boxes / annotation control.
    # -------------------------------------------------------------------------

    text_positive = df[
        freeze[
            "text_blanking_approved"
        ].astype(
            str
        ).str.lower().isin(
            [
                "true",
                "1",
                "yes",
            ]
        )
    ].copy()

    top_text = (
        text_positive
        .sort_values(
            [
                "raw_to_text_band_l1_change",
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

    top_text[
        "selection_cohort"
    ] = "TEXT_SENSITIVE"

    top_text[
        "geometry_note_after_selection"
    ] = ""

    top_text.to_csv(
        TOP_TEXT_CSV,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Cohort C — tight support / minimal whitespace.
    # -------------------------------------------------------------------------

    top_tight = (
        df
        .sort_values(
            [
                "tight_support_score",
                "raw_foreground_fraction",
                "row_index",
            ],
            ascending=[
                False,
                False,
                True,
            ],
        )
        .head(
            TOP_K
        )
        .copy()
    )

    top_tight[
        "selection_cohort"
    ] = "TIGHT_SUPPORT"

    top_tight[
        "geometry_note_after_selection"
    ] = ""

    top_tight.to_csv(
        TOP_TIGHT_CSV,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Intersections.
    # -------------------------------------------------------------------------

    set_high = set(
        top_high[
            "row_index"
        ].astype(
            int
        )
    )

    set_text = set(
        top_text[
            "row_index"
        ].astype(
            int
        )
    )

    set_tight = set(
        top_tight[
            "row_index"
        ].astype(
            int
        )
    )

    intersection_rows = []

    for idx in sorted(
        set_high
        | set_text
        | set_tight
    ):

        memberships = []

        if idx in set_high:
            memberships.append(
                "HIGH_FREQUENCY"
            )

        if idx in set_text:
            memberships.append(
                "TEXT_SENSITIVE"
            )

        if idx in set_tight:
            memberships.append(
                "TIGHT_SUPPORT"
            )

        if len(
            memberships
        ) >= 2:

            rec = df.loc[
                df[
                    "row_index"
                ]
                == idx
            ].iloc[
                0
            ]

            intersection_rows.append(
                {
                    "row_index":
                        idx,

                    "relative_path":
                        rec[
                            "relative_path"
                        ],

                    "category":
                        rec[
                            "category"
                        ],

                    "memberships":
                        " + ".join(
                            memberships
                        ),

                    "raw_high_25_36_fraction":
                        rec[
                            "raw_high_25_36_fraction"
                        ],

                    "raw_to_text_band_l1_change":
                        rec[
                            "raw_to_text_band_l1_change"
                        ],

                    "tight_support_score":
                        rec[
                            "tight_support_score"
                        ],
                }
            )

    intersections = pd.DataFrame(
        intersection_rows
    )

    intersections.to_csv(
        INTERSECTIONS_CSV,
        index=False,
    )

    # -------------------------------------------------------------------------
    # Print concise selection tables.
    # -------------------------------------------------------------------------

    def show(
        title: str,
        data: pd.DataFrame,
        cols,
    ):
        print(
            "\n"
            + "=" * 150
        )

        print(
            title
        )

        print(
            "=" * 150
        )

        print(
            data[
                cols
            ].to_string(
                index=False
            )
        )

    show(
        "P2-R0-05I6 — TOP RAW HIGH-FREQUENCY SKETCHES",
        top_high,
        [
            "row_index",
            "relative_path",
            "category",
            "garment_id",
            "raw_high_25_36_fraction",
            "raw_highmid_13_24_fraction",
            "raw_foreground_fraction",
            "raw_foreground_radius_to_grid_radius",
        ],
    )

    show(
        "P2-R0-05I6 — TOP TEXT-SENSITIVE SKETCHES",
        top_text,
        [
            "row_index",
            "relative_path",
            "category",
            "garment_id",
            "raw_to_text_band_l1_change",
            "delta_text_high_25_36",
            "raw_high_25_36_fraction",
            "raw_foreground_fraction",
        ],
    )

    show(
        "P2-R0-05I6 — TOP TIGHT-SUPPORT / LOW-WHITESPACE SKETCHES",
        top_tight,
        [
            "row_index",
            "relative_path",
            "category",
            "garment_id",
            "tight_support_score",
            "raw_foreground_fraction",
            "raw_foreground_radius_to_grid_radius",
            "raw_min_border_margin_norm",
            "raw_high_25_36_fraction",
        ],
    )

    print(
        "\n"
        + "=" * 150
    )

    print(
        "P2-R0-05I6 — COHORT INTERSECTIONS"
    )

    print(
        "=" * 150
    )

    if len(
        intersections
    ) == 0:
        print(
            "No top-12 cross-cohort intersections."
        )
    else:
        print(
            intersections.to_string(
                index=False
            )
        )

    report = {
        "stage":
            "P2_R0_05I6_HIGHFREQ_TEXT_TIGHTSUPPORT_EXEMPLAR_AUDIT",

        "status":
            "COMPLETE",

        "rows":
            EXPECTED_ROWS,

        "top_k":
            TOP_K,

        "selection_rules":
            {
                "HIGH_FREQUENCY":
                    "descending RAW high_25_36 non-DC energy fraction",

                "TEXT_SENSITIVE":
                    "text-blanking-approved rows, descending RAW->TEXT_BLANKED four-band L1 change",

                "TIGHT_SUPPORT":
                    (
                        "equal-weight percentile composite: high RAW foreground fraction, "
                        "high foreground-radius/grid-radius ratio, low normalized minimum border margin"
                    ),
            },

        "post_selection_annotation_rule":
            (
                "Visible geometry notes such as lace, zip, button, pleat, ruffle, "
                "cascading hem, pocket detail, text annotation, simple contour, or mixed "
                "must be added only after selection and never used to rank candidates."
            ),

        "outputs":
            {
                "per_image":
                    str(
                        PER_IMAGE_CSV
                    ),

                "top_high":
                    str(
                        TOP_HIGH_CSV
                    ),

                "top_text":
                    str(
                        TOP_TEXT_CSV
                    ),

                "top_tight":
                    str(
                        TOP_TIGHT_CSV
                    ),

                "intersections":
                    str(
                        INTERSECTIONS_CSV
                    ),
            },

        "interpretation_boundary":
            (
                "05I6 freezes descriptive exemplars for visual audit. "
                "Population mechanism claims remain outside this stage."
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
        "\nP2-R0-05I6 EXEMPLAR AUDIT: COMPLETE"
    )

    print(
        "Per-image metrics:",
        PER_IMAGE_CSV,
    )

    print(
        "Top high-frequency:",
        TOP_HIGH_CSV,
    )

    print(
        "Top text-sensitive:",
        TOP_TEXT_CSV,
    )

    print(
        "Top tight-support:",
        TOP_TIGHT_CSV,
    )

    print(
        "Intersections:",
        INTERSECTIONS_CSV,
    )

    print(
        "Report:",
        REPORT_JSON,
    )

    print(
        "\nSTOP — visually annotate garment-detail type only AFTER these rankings are frozen."
    )


if __name__ == "__main__":
    main()