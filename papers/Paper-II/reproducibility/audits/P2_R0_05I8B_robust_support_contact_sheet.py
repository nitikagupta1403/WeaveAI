from __future__ import annotations

from pathlib import Path

import pandas as pd
from PIL import Image, ImageOps, ImageDraw


# =============================================================================
# P2-R0-05I8B — VISUAL VALIDATION OF ROBUST SUPPORT TOP-12
#
# Purpose
# -------
# Create one frozen contact sheet from the already-ranked robust-support top-12.
# No re-ranking. No metric changes. No scientific inference in code.
#
# Human review questions:
#   1) Does robust support now correspond to substantial garment occupancy?
#   2) Are any cases still driven by stray marks / disconnected artifacts?
#   3) Are dominant-component bbox/area measures visually sensible?
# =============================================================================


BASE = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I6_highfreq_text_tightsupport/"
    "P2_R0_05I8_robust_support_metric_audit"
)

TOP_CSV = (
    BASE
    / "P2_R0_05I8_top_robust_support.csv"
)

OUT = (
    BASE
    / "P2_R0_05I8B_robust_support_contact_sheet.png"
)

RAW_ROOTS = [
    Path("/Users/nitikagupta/Desktop/Clo-Sket"),
    Path("/Users/nitikagupta/Research"),
    Path("/Users/nitikagupta/Desktop"),
]


def resolve_raw(relative_path: str) -> Path:
    rel = Path(relative_path)

    direct = [RAW_ROOTS[0] / rel]

    for root in RAW_ROOTS[1:]:
        direct += [
            root / rel,
            root / "WeaveAI" / rel,
            root / "FashionAI" / "datasets" / "Clo-Sket" / "Clo-Sket" / rel,
        ]

    hits = [p.resolve() for p in direct if p.is_file()]
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


def gray_thumb(
    path: Path,
    w: int = 300,
    h: int = 300,
) -> Image.Image:

    with Image.open(path) as im:
        im = ImageOps.exif_transpose(im).convert("L")
        im.thumbnail(
            (w, h),
            Image.Resampling.LANCZOS,
        )

        canvas = Image.new(
            "L",
            (w, h),
            255,
        )

        x = (
            w - im.width
        ) // 2

        y = (
            h - im.height
        ) // 2

        canvas.paste(
            im,
            (x, y),
        )

    return canvas.convert("RGB")


def main():

    if OUT.exists():
        raise RuntimeError(
            f"Refusing to overwrite: {OUT}"
        )

    df = pd.read_csv(
        TOP_CSV,
        keep_default_na=False,
    )

    if len(df) != 12:
        raise RuntimeError(
            f"Expected 12 robust-support exemplars, got {len(df)}"
        )

    df[
        "resolved_raw_path"
    ] = [
        str(
            resolve_raw(
                str(rel)
            )
        )
        for rel in df[
            "relative_path"
        ]
    ]

    cols = 4
    cell_w = 330
    image_h = 285
    label_h = 112
    cell_h = (
        image_h
        + label_h
    )
    rows = 3

    sheet = Image.new(
        "RGB",
        (
            cell_w * cols,
            44 + cell_h * rows,
        ),
        (
            246,
            242,
            234,
        ),
    )

    draw = ImageDraw.Draw(
        sheet
    )

    draw.text(
        (10, 12),
        "P2-R0-05I8B — ROBUST SUPPORT TOP-12 VISUAL VALIDATION",
        fill=(
            20,
            20,
            20,
        ),
    )

    for j, rec in df.iterrows():

        r = j // cols
        c = j % cols

        x0 = c * cell_w
        y0 = 44 + r * cell_h

        thumb = gray_thumb(
            Path(
                rec[
                    "resolved_raw_path"
                ]
            ),
            cell_w,
            image_h,
        )

        sheet.paste(
            thumb,
            (
                x0,
                y0 + label_h,
            ),
        )

        draw.text(
            (
                x0 + 6,
                y0 + 5,
            ),
            f"#{j+1}  {rec['relative_path']}",
            fill=(
                20,
                20,
                20,
            ),
        )

        draw.text(
            (
                x0 + 6,
                y0 + 24,
            ),
            (
                f"{rec['category']} | "
                f"{rec['garment_id']}"
            ),
            fill=(
                70,
                70,
                70,
            ),
        )

        draw.text(
            (
                x0 + 6,
                y0 + 44,
            ),
            (
                "robust="
                f"{float(rec['robust_support_score']):.4f} | "
                "q99="
                f"{float(rec['robust_q99_radius_to_grid']):.4f}"
            ),
            fill=(
                70,
                70,
                70,
            ),
        )

        draw.text(
            (
                x0 + 6,
                y0 + 62,
            ),
            (
                "bbox="
                f"{float(rec['dominant_component_bbox_area_fraction']):.4f} | "
                "area="
                f"{float(rec['dominant_component_area_fraction']):.4f}"
            ),
            fill=(
                70,
                70,
                70,
            ),
        )

        draw.text(
            (
                x0 + 6,
                y0 + 80,
            ),
            (
                "margin="
                f"{float(rec['dominant_component_min_border_margin_norm']):.4f} | "
                "high="
                f"{float(rec['raw_high_25_36_fraction']):.4f}"
            ),
            fill=(
                70,
                70,
                70,
            ),
        )

    sheet.save(
        OUT
    )

    print(
        "P2-R0-05I8B VISUAL VALIDATION SHEET: COMPLETE"
    )

    print(
        "Output:",
        OUT
    )

    print(
        "\nSTOP — visually inspect these frozen robust-support exemplars "
        "before 05J."
    )


if __name__ == "__main__":
    main()