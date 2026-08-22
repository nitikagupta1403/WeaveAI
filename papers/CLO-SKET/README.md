# Understanding Garment Sketch Structure through Radial–Angular Geometry

This folder contains the manuscript components and supporting material for a geometric analysis of garment sketches using radial–angular structure and axial harmonics.

The study uses the existing CLO-SKET dataset and does **not** introduce or claim ownership of the dataset itself. The contribution is a mathematically explicit framework for characterizing garment-sketch geometry, together with garment-identity-aware validation, rotation controls, parameter-sensitivity analysis, harmonic-order justification, and phase-conditioning analysis.

## Manuscript files

- `CLO_SKET_Final_Abstract.md` — abstract and keywords
- `CLO_SKET_Final_Introduction.md` — motivation, research questions, and contribution
- `CLO_SKET_Final_Related_Work.md` — related literature through 2026
- `CLO_SKET_Final_Methods.md` — full mathematical and statistical methodology
- `CLO_SKET_Final_Results.md` — primary results, controls, and sensitivity analyses
- `CLO_SKET_Final_Discussion.md` — interpretation, limitations, and future work
- `CLO_SKET_References.bib` — **canonical machine-readable bibliography**

## Core representation

For each sketch, foreground intensity is expressed in centroid-relative polar coordinates and normalized within radial shells to form a conditional angular distribution

\[
p(\theta\mid r).
\]

The primary angular statistic is the second harmonic

\[
F_2(r)=\sum_k p(\theta_k\mid r)e^{-i2\theta_k}
      =C_2(r)-iS_2(r),
\]

with magnitude

\[
R_2(r)=|F_2(r)|
\]

and axial orientation

\[
\mu_2(r)=\frac12\operatorname{atan2}(S_2(r),C_2(r))\pmod{\pi}.
\]

The final representation contains 14 explicit descriptors: eight radial-magnitude features and six doubled-angle axial features.

## Validation principles

The analysis is designed around repeated sketches of common garment identities. Primary reconstruction therefore uses garment-identity-disjoint folds rather than image-level splits.

The paper additionally evaluates:

- common global rotation and garment-identity-randomized rotation;
- support-threshold and concentration-width sensitivity;
- angular and radial resolution sensitivity;
- radial-domain sensitivity and peak-boundary censoring;
- low-order harmonic controls for \(m=1,2,3,4\);
- perturbation-based phase conditioning; and
- garment-cluster bootstrap and category-stratified permutation inference.

## Scope

The paper studies explicit geometric structure in garment sketches. It does not claim semantic garment understanding, causal geometric laws, a universally optimal radial domain or harmonic order, prospective reliability classification, or complete angular-density reconstruction.

## Dataset

CLO-SKET is an external dataset originally published by Fitri Arnia (2020). Dataset citation details are provided in `CLO_SKET_References.bib`.

## Bibliography

`CLO_SKET_References.bib` is the single canonical bibliography for this paper. Any temporary or annotated literature notes should not be treated as authoritative citation sources.
