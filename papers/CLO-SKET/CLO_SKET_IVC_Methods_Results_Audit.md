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

## Resolved provenance discrepancy: primary-fold sketch-row counts

An earlier audit pass treated the five-value test-fold sequence

> 459, 460, 462, 460, and 459

as a clerical error because an older aggregate `grouped_fold_design.csv` summary reported test-fold counts of 461, 460, 459, 460, and 460 sketches (training counts 1839–1841). That interpretation has now been superseded by direct reproduction from the frozen Experiment 06 checkpoint.

The authoritative row-level `fold_id` stored in `CLO_SKET_EXPERIMENT06_FINAL_CHECKPOINT.pkl` gives test-fold sizes of **459, 460, 462, 460, and 459 sketches**, corresponding to training-fold sizes of **1841, 1840, 1838, 1840, and 1841 sketches**. Each fold contains 46 held-out garment identities, 184 training identities, and zero train/test garment-identity overlap.

Most importantly, using this checkpoint fold map with the frozen Experiment 06 feature matrices and locked classifier reproduces the primary pooled results to numerical precision:

- morphology: macro-F1 = 0.2977879716, balanced accuracy = 0.2982608696;
- morphology + R + A: macro-F1 = 0.3357646054, balanced accuracy = 0.3360869565;
- primary deltas: Δmacro-F1 = +0.0379766338 and Δbalanced accuracy = +0.0378260870.

The older aggregate fold-design summary therefore does not define the row-level partition that generated the frozen Experiment 06 primary results. It should be treated as a stale or earlier fold-design summary rather than as the authoritative Experiment 06 split. The manuscript's explicit sequence `459, 460, 462, 460, 459` is therefore retained.

The public repository does not currently track the stale `grouped_fold_design.csv` artifact itself; the remaining inconsistency was this audit note, which is corrected here.

## Experiment 07 provenance cross-check

The secondary HOG baseline reused the same authoritative Experiment 06 checkpoint `fold_id`. Before fitting either HOG model, the Experiment 06 morphology and morphology-plus-R+A results were reproduced exactly under that fold map. Experiment 07 therefore provides an independent execution-time confirmation that the checkpoint split, not the older aggregate summary, is the relevant frozen row-level assignment for the manuscript-facing primary experiment.

## Overall decision

**PASS.** The inferential architecture is reproducible and one-to-one across Methods and Results: the estimator, authoritative row-level folds, resampling unit, metrics, repeated-partition design, alignment-null construction, permutation count, random-state lineage, and claim hierarchy are explicitly defined. The earlier fold-count discrepancy is resolved in favor of the final Experiment 06 checkpoint because that row-level assignment exactly reproduces the locked primary results.
