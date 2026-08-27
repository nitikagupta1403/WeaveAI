# Experiment 08 scientific-status amendment

**Status:** Post-outcome scientific-status lock  
**Date:** 2026-08-27  
**Scope:** Paper I Experiment 08 only  
**Authority:** This amendment governs interpretation of all Experiment 08 results whose claims depend on the RA14 representation.

## Decision

Experiment 08 has **not passed its prespecified mechanical-validity gate**. Consequently, no result whose interpretation depends on RA14 mechanical validity may be described as confirmatory.

The existing predictive outputs are retained for auditability, but they are **exploratory evidence only**. They must not be used to support a confirmatory claim, a non-inferiority claim, a primary conclusion, or a reviewer-facing statement that RA14 has established mechanical validity.

This decision is outcome-independent. It follows directly from the frozen mechanical audit.

## Evidence basis

Canonical evidence: `papers/CLO-SKET/evidence/Experiment_08/experiment08_mechanical_summary.json`.

| Gate or diagnostic | Frozen result | Interpretation |
|---|---:|---|
| Analytic transformation audit | pass | The symbolic/doubled-angle implementation satisfies the analytic tolerance. |
| Maximum doubled-angle vector error | `7.45 × 10^-16` | Within the frozen `1 × 10^-12` tolerance. |
| Raster axial gate | pass | Axial error alone meets its frozen raster criterion. |
| Median axial error | `0.286°` | Descriptive diagnostic. |
| 95th-percentile axial error | `4.208°` | Descriptive diagnostic. |
| Raster magnitude gate | **fail** | Magnitude stability does not meet the frozen raster criterion. |
| Magnitude failure rate | `0.08080` | 8.08% of supported observations fail the magnitude criterion. |
| Combined raster failure rate | `0.08188` | The overall raster gate fails. |
| Overall RA14 mechanical gate | **fail** | Confirmatory interpretation is blocked. |

The audit also records a coordinate-convention discrepancy: the synthetic raster test observes

`alpha_rot - alpha_ref ≈ -phi`

whereas the mathematical design lock states `+phi`. This may arise from mathematical Cartesian coordinates versus image coordinates with a downward-positive vertical axis, but it is not treated as resolved by assertion. The convention must be reconciled explicitly in code, equations, and documentation before any qualified mechanical claim is made.

## Chronology and inferential consequence

The canonical mechanical summary records `predictive_results_already_frozen: true`. Therefore:

1. the mechanical settings were not selected using predictive outcomes;
2. nevertheless, the required mechanical gate was not passed before predictive interpretation;
3. predictive results involving RA14 cannot inherit confirmatory status retroactively;
4. the failed gate must be reported even if a predictive result appears favorable.

Any existing RA14-versus-DINOv2, RA14 compactness, additive-value, ablation, or correspondence result is exploratory unless and until a prospectively locked qualified analysis is completed.

## Compactness-output invalidation

Commit `e9e4f220c9d036e05a0de88adad1bda94830c87f` corrected the paired identity-bootstrap implementation so that repeated garment-identity blocks sampled with replacement retain their multiplicity.

Any Experiment 08 compactness result generated before that correction is invalid and must not be cited, copied into the manuscript, or treated as a reproducible result. The correction authorizes no automatic rerun and does not restore confirmatory status.

## Rules for the next analysis

No revised predictive outcome may be computed until a separate, dated analysis amendment is committed that:

1. defines the exact mechanically qualified population or sensitivity strata without consulting revised predictive outcomes;
2. reconciles the rotation-sign convention between mathematical and raster coordinates;
3. fixes all thresholds, estimands, metrics, multiplicity handling, and reporting rules;
4. preserves the frozen identity-disjoint folds and train-only fitting of PCA, scaling, and classifiers;
5. requires the corrected paired bootstrap with replacement multiplicity preserved;
6. commits to reporting the original failed mechanical gate and all qualified sensitivity results, including null or adverse results;
7. distinguishes a sensitivity analysis from the original confirmatory study rather than relabeling it as confirmatory.

A permissible qualified analysis may stratify or filter using mechanical diagnostics only, provided the rule is frozen before revised predictive outcomes are inspected and the full-population exploratory result remains reported.

## Manuscript rule

Until the requirements above are met, the submission manuscript must do one of the following:

- omit Experiment 08 from confirmatory claims and primary conclusions; or
- present it in a clearly labelled exploratory/post-outcome section that discloses the failed raster magnitude gate, the sign-convention issue, and the invalidated pre-fix compactness bootstrap output.

The manuscript must not use “validated,” “mechanically verified,” “non-inferior,” or equivalent language for RA14 based on the current Experiment 08 evidence.

## Supersession boundary

This amendment does not alter the frozen dataset, representations, preprocessing artifacts, folds, feature hashes, or earlier Experiment 06/07 evidence. It changes only the scientific status and permitted interpretation of Experiment 08 outputs.
