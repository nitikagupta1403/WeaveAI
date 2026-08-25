# CLO-SKET Paper I — Reproducibility Package

This folder contains the curated computational materials supporting CLO-SKET Paper I.

## Intended execution structure

The primary computational lineage is:

```text
official CLO-SKET TIFF images
        ↓
01_Core_Radial_Angular_14D_and_Reconstruction.ipynb
        ↓
02_Parameter_Sensitivity.ipynb
03_Harmonic_Order_Control.ipynb
04_Phase_Conditioning.ipynb
05_Rotation_Controls.ipynb
```

Notebook 01 is the canonical source-to-measurement and reconstruction pipeline. Notebooks 02–05 contain targeted validation and sensitivity analyses built around the same Paper-I measurement lineage.

## Notebook roles

### 01_Core_Radial_Angular_14D_and_Reconstruction.ipynb

Primary Paper-I computational notebook. It rebuilds the radial–angular representation from the source CLO-SKET TIFF files, constructs the second-harmonic measurements and the final explicit descriptor representation, performs garment-identity-aware validation, and contains the canonical reconstruction analyses used by the manuscript.

### 02_Parameter_Sensitivity.ipynb

Sensitivity analyses for the prespecified measurement choices, including support/concentration settings, radial-domain sensitivity, angular-resolution sensitivity, radial-resolution sensitivity, and common-physical-domain controls.

### 03_Harmonic_Order_Control.ipynb

Harmonic-order diagnostics used to assess the second-harmonic focus relative to neighboring low-order harmonics. These analyses are geometric controls and are not semantic feature-selection experiments.

### 04_Phase_Conditioning.ipynb

Conditioning analysis for axial phase/orientation error, including garment-identity-aware association analyses and the perturbation-theoretic variables reported in the manuscript.

### 05_Rotation_Controls.ipynb

Contains two scientifically distinct rotation-control branches:

**Part A — Analytic and garment-identity-randomized rotation controls.** These analyses test coordinate-frame dependence of the magnitude-only reconstruction experiment using exact harmonic transformations.

**Part B — Rigid-image rotation invariance/equivariance control.** These analyses rerun the measurement pipeline after rigid raster rotation of the source sketches and test the intended transformation behavior of the final 14-dimensional representation over the evaluated rotations. The doubled-angle orientation pairs are assessed under the expected `R(2φ)` action, while the scalar/magnitude coordinates are assessed according to their intended invariant roles.

These two controls must not be collapsed into a generic claim of "rotation robustness": they answer different scientific questions.

### 06_Experiment_06_Evidence_Record.md

Public manuscript-facing evidence/provenance record for the locked compact-representation experiment. It records the exact feature sets, estimator, garment-identity-disjoint validation design, primary pooled results, identity-bootstrap uncertainty, repeated grouped-partition stability, category-preserving alignment-control result, historical-exposure disclosure, and claim boundary.

This is deliberately an evidence record rather than an executable notebook. The repository does **not** claim that a separate standalone rerunnable Experiment 06 notebook or frozen runtime bundle is present unless one is explicitly deposited.

### audit_Final_Validation_Shield.ipynb

Historical validation/provenance notebook retained for auditability. It records environment information, integrity checks, and reviewer-oriented validation of frozen result objects. It is **not** intended to be the primary source-to-result execution path and may depend on historical frozen runtime checkpoints.

### Experiment_08/

Prospective learned-baseline study governed by `../PAPER_I_FRESH_STUDY_MATHEMATICAL_DESIGN_LOCK.md`. Its current preflight validates public row/fold provenance, deterministic source-image mapping, and analytic angular/rotation conventions, then stops before DINOv2 extraction or classifier fitting. Outcome-capable execution remains locked until model-weight and environment provenance are complete.

## Data

The source image data are not redistributed in this repository. Obtain CLO-SKET from the official Mendeley Data record cited in the manuscript (Fitri Arnia, 2020, Version 1, doi:10.17632/jt533nkhsf.1).

Set the dataset root in the notebooks as documented in their runtime-configuration cells. The canonical source notebook supports a configurable CLO-SKET data root rather than requiring a particular local directory layout.

## Reproducibility policy

The intended public reproducibility chain is source-code driven. Large private/runtime-memory pickle snapshots are not part of the scientific source package and should not be treated as the canonical way to regenerate manuscript results.

Some historical validation cells retain references to frozen checkpoint files for provenance or recovery. Such cells should be interpreted as audit records unless the corresponding checkpoint is explicitly supplied. The manuscript-facing computational claims are governed by the source notebooks and the methods/results files in `papers/CLO-SKET/`.

## Randomness and grouped validation

Where stochastic procedures are used, seeds and resampling/permutation counts are declared in the relevant notebook cells. Grouped validation and inferential procedures use recovered garment identity as the dependency unit where specified in the manuscript. Users should preserve those units and seeds when reproducing the reported analyses.

## Scope

This folder supports **Paper I only**. Full-harmonic representation-selection, bandwise spectral compression, and latent-geometry analyses belong to Paper II and are intentionally excluded from this package.

For the formal ownership boundary, see:

```text
../P1_P2_CLAIM_FIREWALL.md
```

## Audit status

- Five curated Paper-I scientific notebooks are present.
- Rotation controls are consolidated into a single notebook while preserving the distinction between image-domain transformation validation and analytic reconstruction coordinate-frame controls.
- Experiment 06 now has a public evidence/provenance record with explicit non-executable status; no nonexistent standalone runtime bundle is claimed.
- The validation shield is retained as optional provenance material rather than the primary reproducibility entry point.
- Source image redistribution is intentionally avoided.
- Paper-II-only computational material is intentionally excluded.
