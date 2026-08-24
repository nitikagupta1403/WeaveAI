# Garment Sketches: Axial–Radial Geometry and Identity-Aware Validation

This directory contains the Image and Vision Computing (IVC) submission sources and supporting provenance for the CLO-SKET axial–radial geometry study.

## Canonical IVC source of truth

Only the following files are canonical scientific sources for the active IVC manuscript:

- `CLO_SKET_IVC_Abstract.md`
- `CLO_SKET_IVC_Introduction.md`
- `CLO_SKET_IVC_Related_Work.md`
- `CLO_SKET_IVC_Methods.md`
- `CLO_SKET_IVC_Results.md`
- `CLO_SKET_IVC_Discussion.md`
- `CLO_SKET_IVC_Conclusion.md`
- `CLO_SKET_References.bib` — canonical bibliography

`assemble_ivc_manuscript.py` assembles these sources into `CLO_SKET_IVC_Manuscript.md`. The assembled manuscript is a generated artifact and must not be edited independently.

Legacy `CLO_SKET_Final_*` files, `CLO_SKET_IVC_Main.md`, archived manuscript versions, and files under `Reserve/` are retained for provenance only and must not be used as submission sources.

## Mathematical convention

The second harmonic uses the negative-exponential convention

\[
F_2(r)=\sum_k p(\theta_k\mid r)e^{-i2\theta_k}=C_2(r)-iS_2(r),
\]

so the associated axial orientation is

\[
\alpha_2(r)=-\frac12\arg F_2(r)=\frac12\operatorname{atan2}(S_2(r),C_2(r))\pmod{\pi}.
\]

The frozen implementation uses the 72-bin FFT/index reference. Because each angular bin spans 5 degrees, its absolute phase reference differs from geometric bin centres by a fixed 2.5-degree offset. This reference issue does not alter `R_2`, relative-angle quantities, or the frozen predictive results. See `CLO_SKET_IVC_Math_Convention_Correction.md`.

## Active figures

The active main-text figure assets are under `figures/`. In particular, `Figure_5_Garment_Identity_Inference.png` is the garment-level association/phase-conditioning figure and is distinct from `Figure_3_Rigid_Rotation_Control.png`. Figure numbering and captions must be taken from the canonical IVC Results source.

## Validation principles

The active study uses 2,300 CLO-SKET sketches from 23 categories and 230 recovered garment identities. Complete garment identity is the unit of train/test separation, resampling, and the category-preserving alignment permutation. The main inferential distinction is between incremental predictive utility and exact garment-level correspondence.

## Scope

The contribution is an explicit measurement-and-validation framework for garment-sketch geometry, not a claim of new Fourier mathematics, semantic garment understanding, causal structure, or information-theoretic independence.

## Data and code availability

Do not state that the Experiment 06 evidence bundle is publicly available until the corresponding frozen artifacts have been added to the public repository and verified from a clean checkout. Availability wording in the submission manuscript must match the repository state exactly.

## Dataset

CLO-SKET is an external dataset; this repository does not claim ownership of it. Dataset citation details are maintained in `CLO_SKET_References.bib`.
