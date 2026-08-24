"""CLO-SKET IVC — low-mass shell support audit.

Purpose
-------
Audit whether shell conditioning can allow negligibly supported radial shells to
influence the frozen 14-D axial-radial representation. This is a sensitivity
analysis only. It does NOT redefine the frozen representation, optimize a new
threshold, or alter Experiment 06.

The audit recomputes the radial-angular mass directly from the 2,300 source TIFF
images using the manuscript's frozen 72 x 72 construction, then evaluates:
  1) shell-mass support over the primary 25-shell domain (r=3.5,...,27.5),
  2) mass support at the frozen R2 peak and at the two domain endpoints,
  3) radial-descriptor stability after audit-only minimum shell-mass filters.

If stage 1 shows material instability, predictive propagation into the frozen
identity-disjoint Experiment 06 should be performed as a separate stage. This
script intentionally does not perform that propagation.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image


# --------------------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------------------
N_RADIAL = 72
N_ANGULAR = 72
EPS_NONEMPTY = 1e-14
PRIMARY_SHELLS = np.arange(3.5, 28.0, 1.0)  # 3.5,...,27.5, exactly 25 shells
PRIMARY_INDEX = np.arange(3, 28)             # because r_j = j + 0.5

# Audit-only support thresholds: fraction of each sketch's total darkness mass.
# These are prespecified sensitivity perturbations, not candidate replacement rules.
SUPPORT_THRESHOLDS = np.array([
    0.0,
    1e-5,
    5e-5,
    1e-4,
    5e-4,
    1e-3,
    2e-3,
    5e-3,
], dtype=float)

DATA_ROOT = Path(os.environ.get(
    "CLO_SKET_DATA_ROOT",
    "/content/drive/MyDrive/FashionAI/datasets/Clo-Sket/Clo-Sket",
))
OUTPUT_ROOT = Path(os.environ.get(
    "CLO_SKET_SHELL_AUDIT_OUTPUT",
    "/content/drive/MyDrive/FashionAI/CLO_SKET_Low_Mass_Shell_Audit",
))
OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)


def _find_tiffs(root: Path) -> list[Path]:
    paths = [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in {".tif", ".tiff"}]
    return sorted(paths)


def _extract_mass_and_r2(path: Path):
    """Recompute the frozen radial x angular mass and second-harmonic magnitude."""
    img = np.asarray(Image.open(path).convert("L"), dtype=np.float64)
    h, w = img.shape
    darkness = np.maximum(255.0 - img, 0.0)
    total = float(darkness.sum())
    if not np.isfinite(total) or total <= 0:
        raise ValueError(f"No positive foreground darkness mass: {path}")

    yy, xx = np.indices((h, w), dtype=np.float64)
    scale = float(max(w, h))
    x = (xx - (w - 1) / 2.0) / scale
    y = (yy - (h - 1) / 2.0) / scale

    cx = float((darkness * x).sum() / total)
    cy = float((darkness * y).sum() / total)
    x = x - cx
    y = y - cy

    radius = np.sqrt(x * x + y * y)
    rmax = float(radius[darkness > 0].max())
    if not np.isfinite(rmax) or rmax <= 0:
        raise ValueError(f"Invalid maximum foreground radius: {path}")
    rho = radius / rmax
    theta = np.arctan2(y, x)

    # Histogram only positive-mass pixels. Explicitly retain rho == 1 in final radial bin.
    fg = darkness > 0
    rho_fg = np.minimum(rho[fg], np.nextafter(1.0, 0.0))
    theta_fg = theta[fg]
    weight_fg = darkness[fg]

    r_edges = np.linspace(0.0, 1.0, N_RADIAL + 1)
    t_edges = np.linspace(-np.pi, np.pi, N_ANGULAR + 1)
    H, _, _ = np.histogram2d(
        rho_fg,
        theta_fg,
        bins=(r_edges, t_edges),
        weights=weight_fg,
    )

    # Exact conservation check, matching the source extraction intent.
    err = abs(float(H.sum()) - total)
    if err > max(1e-8, 1e-12 * total):
        raise AssertionError(f"Mass conservation failure {err:g}: {path}")

    shell_mass = H.sum(axis=1)
    shell_fraction = shell_mass / total

    conditional = np.zeros_like(H)
    nonempty = shell_mass > EPS_NONEMPTY
    conditional[nonempty] = H[nonempty] / shell_mass[nonempty, None]

    F = np.fft.rfft(conditional, axis=1)
    R2 = np.abs(F[:, 2])
    return shell_mass, shell_fraction, R2


def _radial_features(r2_primary: np.ndarray) -> np.ndarray:
    """Frozen eight radial descriptors on the primary grid for one sketch.

    Audit filtering is represented by zeroing unsupported shells before calling
    this function. This preserves the fixed radial grid; it does not renormalize
    surviving shells across radius.
    """
    r = PRIMARY_SHELLS
    m = np.asarray(r2_primary, dtype=float)
    if m.shape != (25,):
        raise ValueError(m.shape)

    # np.trapezoid is preferred in NumPy 2; fall back for older runtimes.
    trapz = getattr(np, "trapezoid", np.trapz)
    I = float(trapz(m, r))
    if not np.isfinite(I) or I <= 0:
        return np.full(8, np.nan)

    rbar = float(trapz(r * m, r) / I)
    spread = float(np.sqrt(max(trapz(((r - rbar) ** 2) * m, r) / I, 0.0)))

    jstar = int(np.argmax(m))
    rstar = float(r[jstar])
    mstar = float(m[jstar])

    in_peak_window = np.abs(r - rstar) <= 4.0
    concentration = float(trapz(np.where(in_peak_window, m, 0.0), r) / I)

    tau = 0.10 * mstar
    support = np.flatnonzero(m >= tau)
    if support.size == 0:
        ron = np.nan
        roff = np.nan
    else:
        ron = float(r[support[0]])
        roff = float(r[support[-1]])

    return np.array([I, rbar, spread, concentration, ron, roff, rstar, mstar], dtype=float)


def _spearman(x: np.ndarray, y: np.ndarray) -> float:
    ok = np.isfinite(x) & np.isfinite(y)
    if ok.sum() < 3:
        return np.nan
    return float(pd.Series(x[ok]).corr(pd.Series(y[ok]), method="spearman"))


def main() -> None:
    print("=" * 112)
    print("CLO-SKET — LOW-MASS SHELL SUPPORT AUDIT — STAGE 1")
    print("=" * 112)
    print("DATA_ROOT   :", DATA_ROOT)
    print("OUTPUT_ROOT :", OUTPUT_ROOT)
    print("Frozen nonempty-shell epsilon :", EPS_NONEMPTY)
    print("Primary shells                : 3.5 ... 27.5 (25 shells)")
    print("Audit-only relative thresholds:", SUPPORT_THRESHOLDS.tolist())
    print()

    if not DATA_ROOT.exists():
        raise FileNotFoundError(
            f"Dataset root not found: {DATA_ROOT}\n"
            "Set CLO_SKET_DATA_ROOT or edit DATA_ROOT before running."
        )

    paths = _find_tiffs(DATA_ROOT)
    print("TIFF sketches found:", len(paths))
    if len(paths) != 2300:
        raise AssertionError(f"Expected 2300 TIFF sketches; found {len(paths)}")

    n = len(paths)
    shell_frac_primary = np.empty((n, 25), dtype=float)
    r2_primary = np.empty((n, 25), dtype=float)
    baseline_features = np.empty((n, 8), dtype=float)
    rows = []

    for i, path in enumerate(paths):
        shell_mass, shell_fraction, R2 = _extract_mass_and_r2(path)
        sf = shell_fraction[PRIMARY_INDEX]
        rr = R2[PRIMARY_INDEX]
        shell_frac_primary[i] = sf
        r2_primary[i] = rr
        baseline_features[i] = _radial_features(rr)

        jstar = int(np.argmax(rr))
        peak_frac = float(sf[jstar])
        # Rank 1 = highest supported shell mass in the primary domain.
        rank_desc = int(np.argsort(np.argsort(-sf))[jstar] + 1)
        rows.append({
            "path": str(path),
            "peak_shell": float(PRIMARY_SHELLS[jstar]),
            "peak_R2": float(rr[jstar]),
            "peak_shell_mass_fraction": peak_frac,
            "peak_shell_mass_rank_1_highest": rank_desc,
            "primary_min_shell_mass_fraction": float(sf.min()),
            "primary_q01_shell_mass_fraction": float(np.quantile(sf, 0.01)),
            "primary_q05_shell_mass_fraction": float(np.quantile(sf, 0.05)),
            "primary_median_shell_mass_fraction": float(np.median(sf)),
            "primary_max_shell_mass_fraction": float(sf.max()),
            "lower_endpoint_mass_fraction": float(sf[0]),
            "upper_endpoint_mass_fraction": float(sf[-1]),
        })

        if (i + 1) % 250 == 0 or i + 1 == n:
            print(f"processed {i + 1:4d} / {n}")

    per_sketch = pd.DataFrame(rows)
    per_sketch.to_csv(OUTPUT_ROOT / "shell_support_per_sketch.csv", index=False)

    print("\n" + "=" * 112)
    print("A. PRIMARY-DOMAIN SHELL SUPPORT")
    print("=" * 112)
    flat = shell_frac_primary.ravel()
    qs = [0, 0.001, 0.01, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99, 0.999, 1.0]
    for q in qs:
        print(f"q={q:>6.3f} : {np.quantile(flat, q):.10f}")

    print("\nPeak-shell mass fraction across 2,300 sketches")
    peak = per_sketch["peak_shell_mass_fraction"].to_numpy()
    for q in qs:
        print(f"q={q:>6.3f} : {np.quantile(peak, q):.10f}")

    print("\nPeak-shell mass-rank distribution (1 = highest-mass primary shell)")
    print(per_sketch["peak_shell_mass_rank_1_highest"].describe(percentiles=[.5,.9,.95,.99]).to_string())

    print("\n" + "=" * 112)
    print("B. AUDIT-ONLY MINIMUM SUPPORT THRESHOLDS")
    print("=" * 112)

    feature_names = ["I", "r_bar", "r_spread", "concentration", "r_on", "r_off", "r_peak", "R2_peak"]
    sensitivity_rows = []

    for t in SUPPORT_THRESHOLDS:
        keep = shell_frac_primary >= t
        counts = keep.sum(axis=1)
        filtered_features = np.empty_like(baseline_features)

        peak_shell_filtered = np.full(n, np.nan)
        peak_mag_filtered = np.full(n, np.nan)
        for i in range(n):
            mm = np.where(keep[i], r2_primary[i], 0.0)
            filtered_features[i] = _radial_features(mm)
            if np.any(keep[i]):
                j = int(np.argmax(mm))
                peak_shell_filtered[i] = PRIMARY_SHELLS[j]
                peak_mag_filtered[i] = mm[j]

        row = {
            "min_shell_mass_fraction": float(t),
            "mean_retained_shells": float(counts.mean()),
            "median_retained_shells": float(np.median(counts)),
            "min_retained_shells": int(counts.min()),
            "fraction_sketches_all_25_retained": float(np.mean(counts == 25)),
            "fraction_sketches_no_shell_retained": float(np.mean(counts == 0)),
            "exact_peak_radius_agreement": float(np.mean(peak_shell_filtered == baseline_features[:, 6])),
            "peak_radius_spearman": _spearman(baseline_features[:, 6], peak_shell_filtered),
            "peak_magnitude_spearman": _spearman(baseline_features[:, 7], peak_mag_filtered),
        }
        for j, name in enumerate(feature_names):
            row[f"spearman_{name}"] = _spearman(baseline_features[:, j], filtered_features[:, j])
            ok = np.isfinite(baseline_features[:, j]) & np.isfinite(filtered_features[:, j])
            row[f"exact_agreement_{name}"] = float(np.mean(
                np.isclose(baseline_features[ok, j], filtered_features[ok, j], rtol=0, atol=1e-12)
            )) if ok.any() else np.nan
        sensitivity_rows.append(row)

    sensitivity = pd.DataFrame(sensitivity_rows)
    sensitivity.to_csv(OUTPUT_ROOT / "threshold_sensitivity.csv", index=False)
    print(sensitivity.to_string(index=False))

    print("\n" + "=" * 112)
    print("C. DIRECT PEAK-SUPPORT COUNTS")
    print("=" * 112)
    count_rows = []
    for t in SUPPORT_THRESHOLDS[1:]:
        peak_below = peak < t
        lower_below = per_sketch["lower_endpoint_mass_fraction"].to_numpy() < t
        upper_below = per_sketch["upper_endpoint_mass_fraction"].to_numpy() < t
        count_rows.append({
            "threshold": float(t),
            "peak_below_n": int(peak_below.sum()),
            "peak_below_fraction": float(peak_below.mean()),
            "lower_endpoint_below_n": int(lower_below.sum()),
            "lower_endpoint_below_fraction": float(lower_below.mean()),
            "upper_endpoint_below_n": int(upper_below.sum()),
            "upper_endpoint_below_fraction": float(upper_below.mean()),
        })
    counts_df = pd.DataFrame(count_rows)
    counts_df.to_csv(OUTPUT_ROOT / "critical_shell_support_counts.csv", index=False)
    print(counts_df.to_string(index=False))

    summary = {
        "n_sketches": n,
        "n_primary_shells": 25,
        "nonempty_epsilon_frozen": EPS_NONEMPTY,
        "audit_thresholds_total_darkness_fraction": SUPPORT_THRESHOLDS.tolist(),
        "all_primary_shell_mass_fraction_quantiles": {str(q): float(np.quantile(flat, q)) for q in qs},
        "peak_shell_mass_fraction_quantiles": {str(q): float(np.quantile(peak, q)) for q in qs},
        "output_files": [
            "shell_support_per_sketch.csv",
            "threshold_sensitivity.csv",
            "critical_shell_support_counts.csv",
        ],
        "interpretation_lock": (
            "Audit-only sensitivity analysis. The frozen 14-D representation and Experiment 06 are unchanged. "
            "Do not select a new support threshold from these results. Escalate to predictive propagation only "
            "if stage-1 descriptor instability is material."
        ),
    }
    with open(OUTPUT_ROOT / "audit_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print("\n" + "=" * 112)
    print("STAGE-1 AUDIT COMPLETE")
    print("=" * 112)
    print("Saved:")
    for name in summary["output_files"] + ["audit_summary.json"]:
        print(" -", OUTPUT_ROOT / name)
    print("\nNO FEATURE DEFINITION OR EXPERIMENT-06 RESULT WAS MODIFIED.")
    print("Send the printed B/C tables here before any Stage-2 predictive propagation.")


if __name__ == "__main__":
    main()
