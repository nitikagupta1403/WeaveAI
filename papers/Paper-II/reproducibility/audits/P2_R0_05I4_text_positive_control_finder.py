from __future__ import annotations

import base64
import hashlib
import io
import json
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image, ImageOps


# =============================================================================
# P2-R0-05I4 — TEXT-POSITIVE CONTROL FINDER
#
# Goal
# ----
# Find real sketches where the frozen TEXT_ONLY preprocessing actually altered
# visible pixels, so we can add an explicit text-contamination control panel
# without disturbing the objectively selected crop/support exemplars.
#
# Selection logic
# ---------------
# 1) Use the frozen preprocessing manifest and V1_TEXT_ONLY manifest.
# 2) Require n_text_boxes > 0.
# 3) Require RAW and TEXT_ONLY rasters to differ.
# 4) Rank candidates by changed dark-pixel mass within the same-size raster.
# 5) Export a contact sheet of the top candidates for visual verification.
#
# No Paper-II inference changes.
# No exemplar substitution in 05I2/05I3.
# =============================================================================


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

LOCAL_RAW_ROOTS = [
    Path("/Users/nitikagupta/Desktop/Clo-Sket"),
    Path("/Users/nitikagupta/Research"),
]

OUTPUT_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I4_text_positive_control"
)

CANDIDATES_CSV = (
    OUTPUT_ROOT
    / "P2_R0_05I4_text_positive_candidates.csv"
)

CONTACT_SHEET = (
    OUTPUT_ROOT
    / "P2_R0_05I4_text_positive_contact_sheet.png"
)

REPORT_JSON = (
    OUTPUT_ROOT
    / "P2_R0_05I4_report.json"
)

TOP_K = 12


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def resolve_raw(relative_path: str, expected_sha: str) -> Path:
    rel = Path(relative_path)

    candidates = [
        LOCAL_RAW_ROOTS[0] / rel,
    ]

    for root in LOCAL_RAW_ROOTS[1:]:
        candidates.extend(
            [
                root / rel,
                root / "WeaveAI" / rel,
                root / "FashionAI" / rel,
                root / "datasets" / "Clo-Sket" / "Clo-Sket" / rel,
            ]
        )

    hits = []

    for p in candidates:
        if p.is_file():
            if not expected_sha or sha256_file(p) == expected_sha:
                hits.append(p.resolve())

    if hits:
        return Path(sorted(set(hits))[0])

    # Bounded fallback by basename + suffix + SHA.
    suffix = str(rel).replace("\\", "/")

    for root in LOCAL_RAW_ROOTS:
        if not root.exists():
            continue

        for p in root.rglob(rel.name):
            if not p.is_file():
                continue

            pnorm = str(p).replace("\\", "/")

            if not pnorm.endswith(suffix):
                continue

            if expected_sha and sha256_file(p) != expected_sha:
                continue

            hits.append(p.resolve())

    hits = sorted(set(hits))

    if not hits:
        raise FileNotFoundError(
            f"Could not resolve RAW raster for {relative_path}"
        )

    return Path(hits[0])


def load_gray(path: Path) -> np.ndarray:
    with Image.open(path) as im:
        im = ImageOps.exif_transpose(im).convert("L")
        return np.asarray(im, dtype=np.uint8)


def visible_difference_metrics(raw: np.ndarray, text: np.ndarray) -> dict:
    if raw.shape != text.shape:
        raise RuntimeError(
            f"RAW/TEXT_ONLY shape mismatch: {raw.shape} vs {text.shape}"
        )

    diff = text.astype(np.int16) - raw.astype(np.int16)

    changed = diff != 0

    # Positive values mean TEXT_ONLY became lighter.
    whiten = diff > 0

    # Restrict to pixels that were meaningfully dark in RAW.
    raw_dark = raw < 245
    changed_dark = whiten & raw_dark

    return {
        "changed_pixels":
            int(changed.sum()),

        "changed_fraction":
            float(changed.mean()),

        "whitened_pixels":
            int(whiten.sum()),

        "whitened_dark_pixels":
            int(changed_dark.sum()),

        "mean_positive_intensity_change":
            float(
                diff[whiten].mean()
                if np.any(whiten)
                else 0.0
            ),

        "total_positive_intensity_change":
            int(
                diff[whiten].sum()
                if np.any(whiten)
                else 0
            ),
    }


def fit_thumb(arr: np.ndarray, box_w=320, box_h=280) -> Image.Image:
    im = Image.fromarray(arr)
    im.thumbnail((box_w, box_h), Image.Resampling.LANCZOS)

    canvas = Image.new(
        "L",
        (box_w, box_h),
        255,
    )

    x = (box_w - im.width) // 2
    y = (box_h - im.height) // 2

    canvas.paste(im, (x, y))

    return canvas


def main():

    OUTPUT_ROOT.mkdir(
        parents=True,
        exist_ok=True,
    )

    for p in (
        CANDIDATES_CSV,
        CONTACT_SHEET,
        REPORT_JSON,
    ):
        if p.exists():
            raise RuntimeError(
                f"Refusing to overwrite: {p}"
            )

    freeze = pd.read_csv(
        PREPROCESS_MANIFEST,
        keep_default_na=False,
    )

    v1 = pd.read_csv(
        V1_MANIFEST,
        keep_default_na=False,
    )

    merged = freeze.merge(
        v1[
            [
                "row_index",
                "relative_path",
                "source_sha256",
                "output_relative_path",
                "n_text_boxes",
                "variant",
            ]
        ],
        on=[
            "row_index",
            "relative_path",
            "source_sha256",
        ],
        how="inner",
        validate="one_to_one",
    )

    if len(merged) != len(v1):
        raise RuntimeError(
            f"Freeze/V1 merge mismatch: {len(merged)} vs {len(v1)}"
        )

    candidates = merged[
        merged[
            "n_text_boxes"
        ].astype(int) > 0
    ].copy()

    rows = []

    for _, rec in candidates.iterrows():

        rel = str(
            rec[
                "relative_path"
            ]
        )

        raw_path = resolve_raw(
            rel,
            str(
                rec[
                    "source_sha256"
                ]
            ),
        )

        text_path = (
            V1_ROOT
            / str(
                rec[
                    "output_relative_path"
                ]
            )
        )

        if not text_path.is_file():
            raise RuntimeError(
                f"Missing TEXT_ONLY image: {text_path}"
            )

        raw = load_gray(
            raw_path
        )

        text = load_gray(
            text_path
        )

        metrics = visible_difference_metrics(
            raw,
            text,
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
                    rel,

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

                "n_text_boxes":
                    int(
                        rec[
                            "n_text_boxes"
                        ]
                    ),

                "selection_cohort":
                    str(
                        rec[
                            "selection_cohort"
                        ]
                    ),

                "text_blanking_approved":
                    str(
                        rec[
                            "text_blanking_approved"
                        ]
                    ),

                "raw_path":
                    str(
                        raw_path
                    ),

                "text_only_path":
                    str(
                        text_path
                    ),

                **metrics,
            }
        )

    result = pd.DataFrame(
        rows
    )

    # Require an actual raster change.
    result = result[
        result[
            "whitened_dark_pixels"
        ] > 0
    ].copy()

    result = result.sort_values(
        [
            "whitened_dark_pixels",
            "total_positive_intensity_change",
            "row_index",
        ],
        ascending=[
            False,
            False,
            True,
        ],
    ).reset_index(
        drop=True
    )

    result[
        "rank"
    ] = np.arange(
        1,
        len(result) + 1,
    )

    result.to_csv(
        CANDIDATES_CSV,
        index=False,
    )

    print(
        "=" * 150
    )

    print(
        "P2-R0-05I4 — TEXT-POSITIVE CANDIDATES"
    )

    print(
        "=" * 150
    )

    display_cols = [
        "rank",
        "row_index",
        "relative_path",
        "category",
        "garment_id",
        "n_text_boxes",
        "selection_cohort",
        "text_blanking_approved",
        "whitened_dark_pixels",
        "changed_fraction",
        "mean_positive_intensity_change",
    ]

    print(
        result[
            display_cols
        ].head(
            TOP_K
        ).to_string(
            index=False
        )
    )

    # -------------------------------------------------------------------------
    # Contact sheet: RAW | TEXT_ONLY for top candidates.
    # -------------------------------------------------------------------------

    top = result.head(
        TOP_K
    )

    cell_w = 320
    cell_h = 280
    label_h = 52
    pair_w = cell_w * 2
    row_h = cell_h + label_h

    sheet = Image.new(
        "RGB",
        (
            pair_w,
            row_h * len(top),
        ),
        (250, 247, 241),
    )

    from PIL import ImageDraw

    draw = ImageDraw.Draw(
        sheet
    )

    for i, (_, rec) in enumerate(
        top.iterrows()
    ):

        raw = load_gray(
            Path(
                rec[
                    "raw_path"
                ]
            )
        )

        text = load_gray(
            Path(
                rec[
                    "text_only_path"
                ]
            )
        )

        raw_thumb = fit_thumb(
            raw,
            cell_w,
            cell_h,
        ).convert(
            "RGB"
        )

        text_thumb = fit_thumb(
            text,
            cell_w,
            cell_h,
        ).convert(
            "RGB"
        )

        y = i * row_h

        sheet.paste(
            raw_thumb,
            (
                0,
                y + label_h,
            ),
        )

        sheet.paste(
            text_thumb,
            (
                cell_w,
                y + label_h,
            ),
        )

        label = (
            f"#{int(rec['rank'])}  {rec['relative_path']}  |  "
            f"boxes={int(rec['n_text_boxes'])}  |  "
            f"whitened-dark={int(rec['whitened_dark_pixels'])}"
        )

        draw.text(
            (
                8,
                y + 6,
            ),
            label,
            fill=(
                20,
                20,
                20,
            ),
        )

        draw.text(
            (
                8,
                y + 28,
            ),
            "RAW",
            fill=(
                80,
                80,
                80,
            ),
        )

        draw.text(
            (
                cell_w + 8,
                y + 28,
            ),
            "TEXT_ONLY",
            fill=(
                80,
                80,
                80,
            ),
        )

    sheet.save(
        CONTACT_SHEET
    )

    report = {
        "stage":
            "P2_R0_05I4_TEXT_POSITIVE_CONTROL_FINDER",

        "status":
            "COMPLETE",

        "candidate_count":
            int(
                len(
                    result
                )
            ),

        "ranking_rule":
            (
                "n_text_boxes > 0; actual RAW->TEXT_ONLY raster change; "
                "rank descending by whitened dark pixels, then total positive "
                "intensity change."
            ),

        "candidate_csv":
            str(
                CANDIDATES_CSV
            ),

        "contact_sheet":
            str(
                CONTACT_SHEET
            ),

        "interpretation_boundary":
            (
                "This stage identifies text-positive visualization controls. "
                "It does not modify the frozen 05I2 crop/support exemplars."
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
        "\nP2-R0-05I4 TEXT-POSITIVE CONTROL FINDER: COMPLETE"
    )

    print(
        "Candidate CSV:",
        CANDIDATES_CSV,
    )

    print(
        "Contact sheet:",
        CONTACT_SHEET,
    )

    print(
        "Report:",
        REPORT_JSON,
    )

    print(
        "\nSTOP — visually verify which candidates contain meaningful visible text "
        "before freezing the final text-control exemplar(s)."
    )


if __name__ == "__main__":
    main()