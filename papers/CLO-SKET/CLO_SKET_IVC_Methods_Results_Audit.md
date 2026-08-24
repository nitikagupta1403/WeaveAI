# CLO-SKET IVC — Methods ↔ Results Reproducibility Audit

## Status

This audit checks whether each manuscript-facing result has a corresponding prespecified or explicitly labeled methodological definition, including unit of analysis, validation split, estimator, stochastic control, metric, and claim boundary.

## Confirmatory Experiment 06

| Result | Methods specification | Audit |
|---|---|---|
| Seven feature sets: R, A, R+A, M, M+R, M+A, M+R+A | §3.11 | PASS |
| Primary contrast: Macro-F1(M+R+A) − Macro-F1(M) | §3.11 | PASS |
| Secondary contrast: balanced accuracy | §3.11 | PASS |
| Fixed estimator: StandardScaler + L2 LogisticRegression, C=1.0, lbfgs, max_iter=5000 | §3.12 | PASS |
| Validation unit: complete recovered garment identity | §3.12 | PASS |
| Five category-balanced identity-disjoint folds; 46 test identities/fold | §3.12 | PASS |
| Pooled out-of-fold Macro-F1 and balanced accuracy | §3.12 | PASS |
| 5,000 paired garment-identity bootstrap replicates | §3.13 | PASS |
| Category-stratified robustness bootstrap preserves all 23 categories | §3.13 | PASS |
| 10 repeated grouped partitions, seeds 20260820–20260829 | §3.14 | PASS |
| Alignment null permutes complete R+A identity blocks within category with exact block-size matching | §3.15 | PASS |
| Alignment permutations: 2,000, corrected one-sided empirical probability | §3.15 | PASS |
| Structural null: 97.3913% row-level identity misalignment | §3.15 | PASS |
| Claim hierarchy separating predictive increment from garment-specific correspondence | §3.16 | PASS |

## Representation and diagnostic analyses

| Result family | Methods specification | Audit |
|---|---|---|
| 14-D representation = 8 radial + 6 axial coordinates | §§3.8–3.10 | PASS |
| 72 radial bins and 72 angular bins; 25-shell primary domain 3.5–27.5 | §§3.3, 3.7 | PASS |
| Rigid-image rotations at ±5°, ±10°, ±20° and 0° | §3.4 | PASS |
| Second-harmonic axial convention and doubled-angle encoding | §§3.5–3.6, 3.9 | PASS |
| Garment-identity-disjoint C2/S2 reconstruction | §3.17 | PASS |
| Analytic/global and identity-randomized rotation controls | §3.18 | PASS |
| Parameter/discretization sensitivity | subsequent Methods sensitivity sections | PASS |
| Low-order harmonic control m∈{1,2,3,4} | low-order harmonic control section | PASS |
| Phase-conditioning analysis | phase-conditioning section | PASS |
| Garment-level associations with identity-level reduction/resampling | association Methods sections | PASS |
| Outcome-defined error bands treated descriptively/sensitivity-tested | corresponding Methods section | PASS |
| Algebraically coupled ΔR2 diagnostic explicitly non-inferential | corresponding Methods section | PASS |

## One discrepancy requiring correction

### Primary-fold sketch-row counts

The current §3.12 text states:

> test-row counts were 459, 460, 462, 460, and 459.

This conflicts with the frozen validation-shield provenance and the Results description, which constrain primary test-fold sizes to **459–461 sketches** (and training-fold sizes to 1839–1841). A 462-row test fold would imply a 1838-row training fold and is therefore inconsistent with the frozen fold audit.

**Required manuscript correction:** do not assert the erroneous five-value sequence. Replace it with the provenance-safe statement:

> Every sketch appeared in exactly one test fold; test-fold sizes ranged from 459 to 461 sketches because identity block sizes varied slightly.

The same wording should be used in both `CLO_SKET_IVC_Methods.md` and the integrated `CLO_SKET_IVC_Manuscript.md`.

## Overall decision

**PASS with one clerical correction.** The inferential architecture is reproducible and one-to-one across Methods and Results: the estimator, folds, resampling unit, metrics, repeated-partition design, alignment-null construction, permutation count, random-state lineage, and claim hierarchy are all explicitly defined. The only discrepancy identified in this pass is the primary-fold row-count sequence above; it is a reporting inconsistency rather than an analysis-design inconsistency.
