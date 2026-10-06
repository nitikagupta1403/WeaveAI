# WeaveAI Geometry Sandbox v0.1

This bundle contains:

1. `weaveai_synthetic_geometry_bench_v0_1.py`
   - authoritative scientific backend
   - generates controlled synthetic geometry cases
   - computes centroid, object/grid radii, radial-angular fields,
     radial/angular histograms, Fourier harmonic magnitudes, and band energies
   - exports `weaveai_geometry_bench_v0_1.json`

2. `weaveai_geometry_sandbox_v0_1.html`
   - browser Canvas visual debugger
   - loads the JSON using a file picker
   - does not recompute the scientific metrics

## Run

```bash
cd /Users/nitikagupta/Research/WeaveAI/papers/Paper-II/reproducibility/audits/
python weaveai_synthetic_geometry_bench_v0_1.py
```

Then open `weaveai_geometry_sandbox_v0_1.html` in the browser and choose the generated JSON file.

## Core scientific comparisons

- `circle_base` vs `circle_extra_canvas`
  - object pixels unchanged, support changes
- `circle_base` vs `circle_tight_crop`
  - object pixels unchanged, support changes
- `circle_base` vs `circle_translated`
  - translation test
- `circle_base` vs `circle_scaled`
  - isotropic scale test
- `circle_base` vs `circle_rotated`
  - rotation test
- `circle_base` vs `circle_plus_concentric_ring`
  - centroid can remain approximately fixed while radial mass changes
- `circle_base` vs `circle_plus_asymmetric_detail`
  - local detail + centroid/spectral sensitivity test

## Interpretation discipline

This bench distinguishes:
- centroid movement
- coordinate-support normalization
- mass/intensity redistribution

It is not a model-selection experiment and modifies no frozen Paper-II artifact.
