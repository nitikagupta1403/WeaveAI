from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


# =============================================================================
# WeaveAI — Synthetic Geometry Invariance Bench v0.1
#
# Purpose
# -------
# Controlled unit tests for separating:
#   1) centroid movement
#   2) coordinate-support normalization effects
#   3) object mass/intensity redistribution
#
# Scientific backend:
#   Python is authoritative.
#
# Browser Canvas:
#   visualization/debugging only. It must not replace these calculations.
#
# Cases
# -----
#   circle_base
#   circle_extra_canvas
#   circle_tight_crop
#   circle_translated
#   circle_scaled
#   circle_rotated
#   circle_plus_concentric_ring
#   circle_plus_asymmetric_detail
#
# Outputs
# -------
#   weaveai_geometry_bench_v0_1.json
#
# Notes
# -----
# - No Paper-II frozen artifact is modified.
# - This is a synthetic diagnostic bench, not model selection.
# =============================================================================


OUT = Path(__file__).resolve().parent / "weaveai_geometry_bench_v0_1.json"

N_ANGLES = 72
N_RADIAL = 72

BANDS = {
    "low_1_4": (1, 4),
    "mid_5_12": (5, 12),
    "highmid_13_24": (13, 24),
    "high_25_36": (25, 36),
}


def make_canvas(h=256, w=256):
    return np.zeros((h, w), dtype=np.float64)


def draw_disk(img, cx, cy, radius, value=1.0):
    yy, xx = np.indices(img.shape)
    mask = (xx - cx) ** 2 + (yy - cy) ** 2 <= radius ** 2
    img[mask] = np.maximum(img[mask], value)
    return img


def draw_ring(img, cx, cy, radius, thickness, value=1.0):
    yy, xx = np.indices(img.shape)
    rr = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    mask = np.abs(rr - radius) <= thickness / 2.0
    img[mask] = np.maximum(img[mask], value)
    return img


def draw_asymmetric_detail(img, cx, cy, dx, dy, radius, value=1.0):
    return draw_disk(img, cx + dx, cy + dy, radius, value)


def foreground_centroid(img, eps=1e-12):
    mass = img.sum()
    if mass <= eps:
        raise ValueError("Empty image")
    yy, xx = np.indices(img.shape)
    cx = float((img * xx).sum() / mass)
    cy = float((img * yy).sum() / mass)
    return cx, cy


def max_foreground_radius(img, cx, cy, threshold=1e-12):
    yy, xx = np.nonzero(img > threshold)
    if len(xx) == 0:
        raise ValueError("Empty foreground")
    rr = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    return float(rr.max())


def grid_radius(img, cx, cy):
    h, w = img.shape
    corners = np.array([
        [0.0, 0.0],
        [w - 1.0, 0.0],
        [0.0, h - 1.0],
        [w - 1.0, h - 1.0],
    ])
    rr = np.sqrt((corners[:, 0] - cx) ** 2 + (corners[:, 1] - cy) ** 2)
    return float(rr.max())


def radial_angular_field(img, normalization="object"):
    """
    Build a 72x72 conditional angular field.

    For each foreground pixel:
      - radius is normalized either by max foreground radius (object)
        or max corner/grid radius (grid)
      - angle is quantized to 72 bins
      - pixel intensity contributes mass

    Rows are radial bins, columns are angular bins.
    Each non-empty radial shell is conditionally normalized to sum to 1.
    """
    cx, cy = foreground_centroid(img)

    if normalization == "object":
        denom = max_foreground_radius(img, cx, cy)
    elif normalization == "grid":
        denom = grid_radius(img, cx, cy)
    else:
        raise ValueError(normalization)

    yy, xx = np.nonzero(img > 0)
    vals = img[yy, xx]

    dx = xx.astype(np.float64) - cx
    dy = yy.astype(np.float64) - cy

    rr = np.sqrt(dx * dx + dy * dy) / max(denom, 1e-12)
    theta = np.mod(np.arctan2(dy, dx), 2.0 * np.pi)

    rbin = np.minimum((rr * N_RADIAL).astype(int), N_RADIAL - 1)
    abin = np.minimum((theta / (2.0 * np.pi) * N_ANGLES).astype(int), N_ANGLES - 1)

    field = np.zeros((N_RADIAL, N_ANGLES), dtype=np.float64)
    np.add.at(field, (rbin, abin), vals)

    shell_mass = field.sum(axis=1, keepdims=True)
    nonempty = shell_mass[:, 0] > 0
    field[nonempty] /= shell_mass[nonempty]

    return field, {
        "centroid_x": cx,
        "centroid_y": cy,
        "normalization_denominator": float(denom),
        "nonempty_radial_shells": int(nonempty.sum()),
    }


def summarize_field(field):
    fft = np.fft.rfft(field, axis=1)
    mag2 = np.abs(fft) ** 2

    radial_hist = field.sum(axis=1)
    angular_hist = field.sum(axis=0)

    total_non_dc = float(mag2[:, 1:].sum())

    band_energy = {}
    band_fraction = {}

    for name, (lo, hi) in BANDS.items():
        e = float(mag2[:, lo:hi+1].sum())
        band_energy[name] = e
        band_fraction[name] = (
            e / total_non_dc if total_non_dc > 0 else 0.0
        )

    return {
        "radial_histogram": radial_hist.tolist(),
        "angular_histogram": angular_hist.tolist(),
        "fft_magnitude_by_harmonic": np.sqrt(mag2).sum(axis=0).tolist(),
        "band_energy": band_energy,
        "band_fraction": band_fraction,
    }


def tight_crop(img):
    yy, xx = np.nonzero(img > 0)
    return img[yy.min():yy.max()+1, xx.min():xx.max()+1].copy()


def embed_center(img, out_h, out_w):
    out = np.zeros((out_h, out_w), dtype=np.float64)
    h, w = img.shape
    y0 = (out_h - h) // 2
    x0 = (out_w - w) // 2
    out[y0:y0+h, x0:x0+w] = img
    return out


def rotate_90(img):
    return np.rot90(img, k=1).copy()


def build_cases():
    base = make_canvas()
    draw_disk(base, 128, 128, 48, 1.0)

    extra_canvas = embed_center(base, 384, 384)
    crop = tight_crop(base)

    translated = make_canvas()
    draw_disk(translated, 164, 96, 48, 1.0)

    scaled = make_canvas()
    draw_disk(scaled, 128, 128, 70, 1.0)

    rotated = rotate_90(base)

    ring = base.copy()
    draw_ring(ring, 128, 128, radius=66, thickness=8, value=0.75)

    asymmetric = base.copy()
    draw_asymmetric_detail(
        asymmetric,
        128,
        128,
        dx=58,
        dy=-24,
        radius=12,
        value=1.0,
    )

    return {
        "circle_base": base,
        "circle_extra_canvas": extra_canvas,
        "circle_tight_crop": crop,
        "circle_translated": translated,
        "circle_scaled": scaled,
        "circle_rotated": rotated,
        "circle_plus_concentric_ring": ring,
        "circle_plus_asymmetric_detail": asymmetric,
    }


def image_to_sparse_preview(img, max_points=3500):
    yy, xx = np.nonzero(img > 0)
    vals = img[yy, xx]

    if len(xx) > max_points:
        idx = np.linspace(0, len(xx) - 1, max_points).astype(int)
        xx = xx[idx]
        yy = yy[idx]
        vals = vals[idx]

    return [
        [int(x), int(y), float(v)]
        for x, y, v in zip(xx, yy, vals)
    ]


def main():
    cases = build_cases()

    payload = {
        "version": "0.1",
        "purpose": (
            "Controlled synthetic invariance bench separating centroid, "
            "support normalization, and mass/intensity redistribution."
        ),
        "bands": BANDS,
        "cases": {},
        "pairwise": {},
    }

    computed = {}

    for name, img in cases.items():
        cx, cy = foreground_centroid(img)
        obj_radius = max_foreground_radius(img, cx, cy)
        grd_radius = grid_radius(img, cx, cy)

        entry = {
            "shape": [int(img.shape[0]), int(img.shape[1])],
            "mass": float(img.sum()),
            "foreground_pixels": int(np.count_nonzero(img)),
            "centroid": [cx, cy],
            "max_foreground_radius": obj_radius,
            "grid_radius": grd_radius,
            "foreground_radius_to_grid_radius": (
                obj_radius / grd_radius if grd_radius > 0 else None
            ),
            "preview_points": image_to_sparse_preview(img),
            "representations": {},
        }

        computed[name] = {}

        for norm in ("grid", "object"):
            field, meta = radial_angular_field(img, normalization=norm)
            summary = summarize_field(field)

            entry["representations"][norm] = {
                "meta": meta,
                **summary,
            }
            computed[name][norm] = field

        payload["cases"][name] = entry

    comparisons = [
        ("circle_base", "circle_extra_canvas"),
        ("circle_base", "circle_tight_crop"),
        ("circle_base", "circle_translated"),
        ("circle_base", "circle_scaled"),
        ("circle_base", "circle_rotated"),
        ("circle_base", "circle_plus_concentric_ring"),
        ("circle_base", "circle_plus_asymmetric_detail"),
    ]

    for a, b in comparisons:
        key = f"{a}__VS__{b}"
        payload["pairwise"][key] = {}

        for norm in ("grid", "object"):
            fa = computed[a][norm]
            fb = computed[b][norm]

            field_l2 = float(np.linalg.norm(fa - fb))
            max_abs = float(np.max(np.abs(fa - fb)))

            payload["pairwise"][key][norm] = {
                "field_l2": field_l2,
                "field_max_abs": max_abs,
                "exact_equal": bool(np.array_equal(fa, fb)),
            }

    OUT.write_text(
        json.dumps(payload, indent=2),
        encoding="utf-8",
    )

    print("=" * 110)
    print("WEAVEAI SYNTHETIC GEOMETRY INVARIANCE BENCH v0.1")
    print("=" * 110)
    print("Cases:", len(cases))
    print("Output:", OUT)
    print()
    print("KEY PAIRWISE CHECKS")
    print("-" * 110)

    for key, item in payload["pairwise"].items():
        print(key)
        for norm in ("grid", "object"):
            x = item[norm]
            print(
                f"  {norm:6s} "
                f"exact={str(x['exact_equal']):5s} "
                f"L2={x['field_l2']:.8f} "
                f"max={x['field_max_abs']:.8f}"
            )

    print()
    print("STOP — synthetic diagnostic only; no Paper-II artifact modified.")


if __name__ == "__main__":
    main()
