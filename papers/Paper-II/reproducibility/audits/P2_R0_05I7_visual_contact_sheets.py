from __future__ import annotations

import hashlib
from pathlib import Path

import pandas as pd
from PIL import Image, ImageOps, ImageDraw


# =============================================================================
# P2-R0-05I7 — VISUAL CONTACT SHEETS FOR 05I6 FROZEN COHORTS
#
# Purpose
# -------
# Build visual contact sheets AFTER 05I6 rankings are frozen.
#
# Cohorts:
#   A) HIGH_FREQUENCY
#   B) TEXT_SENSITIVE  (RAW | TEXT_BLANKED paired)
#   C) TIGHT_SUPPORT
#
# No re-ranking.
# No scientific inference.
# Human geometry notes are added only after looking at these sheets.
# =============================================================================


BASE = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05i_real_garment_canvas/"
    "P2_R0_05I6_highfreq_text_tightsupport"
)

HIGH_CSV = BASE / "P2_R0_05I6_top_high_frequency.csv"
TEXT_CSV = BASE / "P2_R0_05I6_top_text_sensitive.csv"
TIGHT_CSV = BASE / "P2_R0_05I6_top_tight_support.csv"

V1_ROOT = Path(
    "/Users/nitikagupta/Research/"
    "paper2_r0_05e_preprocessing_ablation/"
    "V1_TEXT_ONLY"
)

V1_MANIFEST = V1_ROOT / "materialized_manifest.csv"

OUT = BASE / "P2_R0_05I7_contact_sheets"

RAW_ROOTS = [
    Path("/Users/nitikagupta/Desktop/Clo-Sket"),
    Path("/Users/nitikagupta/Research"),
    Path("/Users/nitikagupta/Desktop"),
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def resolve_raw(relative_path: str, expected_sha: str) -> Path:
    rel = Path(relative_path)

    direct = [RAW_ROOTS[0] / rel]

    for root in RAW_ROOTS[1:]:
        direct += [
            root / rel,
            root / "WeaveAI" / rel,
            root / "FashionAI" / "datasets" / "Clo-Sket" / "Clo-Sket" / rel,
        ]

    hits = []
    for p in direct:
        if p.is_file() and (not expected_sha or sha256_file(p) == expected_sha):
            hits.append(p.resolve())

    if hits:
        return Path(sorted(set(hits))[0])

    suffix = str(rel).replace("\\", "/")

    for root in RAW_ROOTS:
        if not root.exists():
            continue

        for p in root.rglob(rel.name):
            if not p.is_file():
                continue

            if not str(p).replace("\\", "/").endswith(suffix):
                continue

            if expected_sha and sha256_file(p) != expected_sha:
                continue

            hits.append(p.resolve())

    hits = sorted(set(hits))

    if not hits:
        raise RuntimeError(f"RAW raster not found: {relative_path}")

    return Path(hits[0])


def gray_thumb(path: Path, w=300, h=300) -> Image.Image:
    with Image.open(path) as im:
        im = ImageOps.exif_transpose(im).convert("L")
        im.thumbnail((w, h), Image.Resampling.LANCZOS)

        canvas = Image.new("L", (w, h), 255)

        x = (w - im.width) // 2
        y = (h - im.height) // 2

        canvas.paste(im, (x, y))

    return canvas.convert("RGB")


def make_single_sheet(df: pd.DataFrame, title: str, out_path: Path, metric_lines):
    cols = 4
    cell_w = 320
    image_h = 280
    label_h = 86
    cell_h = image_h + label_h
    rows = (len(df) + cols - 1) // cols

    sheet = Image.new(
        "RGB",
        (cell_w * cols, cell_h * rows + 38),
        (246, 242, 234),
    )

    draw = ImageDraw.Draw(sheet)
    draw.text((10, 10), title, fill=(20, 20, 20))

    for j, (_, rec) in enumerate(df.iterrows()):
        r = j // cols
        c = j % cols
        x0 = c * cell_w
        y0 = 38 + r * cell_h

        raw_path = Path(rec["resolved_raw_path"])
        thumb = gray_thumb(raw_path, cell_w, image_h)

        sheet.paste(thumb, (x0, y0 + label_h))

        draw.text(
            (x0 + 6, y0 + 5),
            f"#{j+1}  {rec['relative_path']}",
            fill=(20, 20, 20),
        )

        draw.text(
            (x0 + 6, y0 + 24),
            f"{rec['category']} | {rec['garment_id']}",
            fill=(70, 70, 70),
        )

        y = y0 + 43
        for line in metric_lines(rec):
            draw.text(
                (x0 + 6, y),
                line,
                fill=(70, 70, 70),
            )
            y += 16

    sheet.save(out_path)


def make_text_pair_sheet(df: pd.DataFrame, out_path: Path):
    cell_w = 300
    image_h = 250
    label_h = 70
    row_h = image_h + label_h
    pair_w = cell_w * 2

    sheet = Image.new(
        "RGB",
        (pair_w, row_h * len(df) + 38),
        (246, 242, 234),
    )

    draw = ImageDraw.Draw(sheet)
    draw.text(
        (10, 10),
        "P2-R0-05I7 — TEXT-SENSITIVE: RAW | TEXT_BLANKED",
        fill=(20, 20, 20),
    )

    for j, (_, rec) in enumerate(df.iterrows()):
        y0 = 38 + j * row_h

        raw = gray_thumb(
            Path(rec["resolved_raw_path"]),
            cell_w,
            image_h,
        )

        txt = gray_thumb(
            Path(rec["text_blanked_path"]),
            cell_w,
            image_h,
        )

        sheet.paste(raw, (0, y0 + label_h))
        sheet.paste(txt, (cell_w, y0 + label_h))

        draw.text(
            (6, y0 + 5),
            f"#{j+1} {rec['relative_path']} | L1={rec['raw_to_text_band_l1_change']:.4f}",
            fill=(20, 20, 20),
        )

        draw.text(
            (6, y0 + 25),
            f"RAW | high={rec['raw_high_25_36_fraction']:.4f} | Δhigh={rec['delta_text_high_25_36']:+.4f}",
            fill=(70, 70, 70),
        )

        draw.text(
            (cell_w + 6, y0 + 25),
            "TEXT_BLANKED",
            fill=(70, 70, 70),
        )

    sheet.save(out_path)


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    for p in [
        OUT / "P2_R0_05I7_high_frequency_contact_sheet.png",
        OUT / "P2_R0_05I7_text_sensitive_contact_sheet.png",
        OUT / "P2_R0_05I7_tight_support_contact_sheet.png",
        OUT / "P2_R0_05I7_visual_annotation_template.csv",
    ]:
        if p.exists():
            raise RuntimeError(f"Refusing to overwrite: {p}")

    high = pd.read_csv(HIGH_CSV, keep_default_na=False)
    text = pd.read_csv(TEXT_CSV, keep_default_na=False)
    tight = pd.read_csv(TIGHT_CSV, keep_default_na=False)

    v1 = pd.read_csv(V1_MANIFEST, keep_default_na=False)

    source_sha = {
        str(r["relative_path"]): str(r["source_sha256"])
        for _, r in v1.iterrows()
    }

    text_path = {
        str(r["relative_path"]):
            str(V1_ROOT / str(r["output_relative_path"]))
        for _, r in v1.iterrows()
    }

    for df in [high, text, tight]:
        df["resolved_raw_path"] = [
            str(resolve_raw(rel, source_sha[rel]))
            for rel in df["relative_path"].astype(str)
        ]

    text["text_blanked_path"] = [
        text_path[rel]
        for rel in text["relative_path"].astype(str)
    ]

    make_single_sheet(
        high,
        "P2-R0-05I7 — HIGH-FREQUENCY RAW COHORT",
        OUT / "P2_R0_05I7_high_frequency_contact_sheet.png",
        lambda r: [
            f"high={r['raw_high_25_36_fraction']:.4f}",
            f"highmid={r['raw_highmid_13_24_fraction']:.4f}",
            f"fg_frac={r['raw_foreground_fraction']:.4f}",
        ],
    )

    make_text_pair_sheet(
        text,
        OUT / "P2_R0_05I7_text_sensitive_contact_sheet.png",
    )

    make_single_sheet(
        tight,
        "P2-R0-05I7 — TIGHT-SUPPORT / LOW-WHITESPACE COHORT",
        OUT / "P2_R0_05I7_tight_support_contact_sheet.png",
        lambda r: [
            f"tight={r['tight_support_score']:.4f}",
            f"fg/grid={r['raw_foreground_radius_to_grid_radius']:.4f}",
            f"margin={r['raw_min_border_margin_norm']:.4f}",
        ],
    )

    annotation = pd.concat(
        [
            high.assign(cohort="HIGH_FREQUENCY"),
            text.assign(cohort="TEXT_SENSITIVE"),
            tight.assign(cohort="TIGHT_SUPPORT"),
        ],
        ignore_index=True,
    )[
        [
            "cohort",
            "row_index",
            "relative_path",
            "category",
            "garment_id",
        ]
    ].copy()

    annotation["visible_geometry_note"] = ""
    annotation["visible_text_or_annotation"] = ""
    annotation["garment_detail_examples"] = ""
    annotation["support_artifact_suspected"] = ""
    annotation["reviewer_note"] = ""

    annotation.to_csv(
        OUT / "P2_R0_05I7_visual_annotation_template.csv",
        index=False,
    )

    print("P2-R0-05I7 VISUAL CONTACT SHEETS: COMPLETE")
    print("High-frequency sheet:", OUT / "P2_R0_05I7_high_frequency_contact_sheet.png")
    print("Text-sensitive sheet:", OUT / "P2_R0_05I7_text_sensitive_contact_sheet.png")
    print("Tight-support sheet:", OUT / "P2_R0_05I7_tight_support_contact_sheet.png")
    print("Annotation template:", OUT / "P2_R0_05I7_visual_annotation_template.csv")
    print("\nSTOP — annotate visible garment detail only after viewing these frozen sheets.")


if __name__ == "__main__":
    main()