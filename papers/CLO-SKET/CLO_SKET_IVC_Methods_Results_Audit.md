# CLO-SKET IVC — Methods ↔ Results Reproducibility Audit

## Status

This audit checks whether each manuscript-facing result has a corresponding methodological definition, unit of analysis, validation split, estimator, stochastic control, metric, chronology, and claim boundary.

The manuscript-facing Experiment-06 primary result is now the separately frozen **corrective CLEAN analysis**. The earlier Experiment-06 package remains historical provenance and must not be treated as the current authoritative primary analysis.

## Corrective confirmatory Experiment 06

| Result | Methods specification | Audit |
|---|---|---|
| Primary comparison: \(M\) versus \(M+RA14\) | §3.11 | PASS |
| Primary metric: pooled OOF macro-F1 | §§3.11–3.12 | PASS |
| Secondary metric: balanced accuracy | §§3.11–3.12 | PASS |
| Fixed estimator: fold-local StandardScaler + L2 LogisticRegression, \(C=1.0\), `lbfgs`, `max_iter=5000` | §3.12 | PASS |
| Validation unit: complete corrected garment identity | §3.12 | PASS |
| 230 corrected identities; 10 per category | §§3.11–3.12 | PASS |
| Five corrected category-balanced identity-disjoint folds; 46 test identities/fold | §3.12 | PASS |
| Corrected test-row counts: 459, 460, 461, 460, 460 | §3.12 | PASS |
| CLEAN annotation-controlled condition governs the confirmatory claim | §3.11 | PASS |
| RAW condition is diagnostic only | §3.11 | PASS |
| 5,000 paired category-stratified corrected-identity bootstrap replicates | §3.13 | PASS |
| 10 repeated corrected grouped partitions, seeds 20260820–20260829 | §3.14 | PASS |
| 2,000 category-preserving, block-size-matched alignment permutations | §3.15 | PASS |
| Corrected structural null: 20 self-mapped rows; 99.1304% row-level misalignment | §3.15 | PASS |
| Claim hierarchy separates incremental predictive utility from garment-specific correspondence | §3.16 | PASS |
| Target-text identity-exclusion analysis explicitly post-outcome sensitivity only | §3.16 | PASS |

## Corrective primary numerical cross-check

The frozen CLEAN corrective result is:

- morphology macro-F1 = 0.2714293424;
- morphology balanced accuracy = 0.2730434783;
- morphology + RA14 macro-F1 = 0.3142559792;
- morphology + RA14 balanced accuracy = 0.3156521739;
- Δmacro-F1 = +0.0428266368;
- Δbalanced accuracy = +0.0426086957.

The category-stratified corrected-identity bootstrap used 5,000 paired replicates and remained positive in all 5,000 replicates for both metrics. The 10 corrected repeated grouped partitions produced positive pooled increments in all 10 repeats.

The corrected category-preserving alignment control did not support garment-specific correspondence:

- macro-F1 empirical one-sided \(p=0.722639\);
- balanced-accuracy empirical one-sided \(p=0.685657\).

The alignment result therefore limits interpretation without negating the primary incremental predictive-utility result.

## Post-outcome target-text sensitivity

A later complete review of all 2,300 frozen CLEAN images identified two exact target-text cases, corresponding to corrected identities `Cardigan__G02` and `Tunic__G02`.

A separate protocol was frozen before the sensitivity outcome was computed. Excluding those two complete identities retained 2,280 sketches and 228 garment identities. The resulting macro-F1 increment was +0.0364023058 and the balanced-accuracy increment was +0.0359903382.

This analysis is explicitly **post-outcome sensitivity only**. It is descriptive evidence of persistence with modest attenuation and cannot create, replace, or strengthen the confirmatory claim.

## Historical Experiment-06 provenance

The earlier Experiment-06 package used a different historical identity/fold lineage and produced the previously reported values:

- historical fold-row counts: 459, 460, 462, 460, 459;
- historical morphology macro-F1: 0.2977879716;
- historical morphology+RA14 macro-F1: 0.3357646054;
- historical Δmacro-F1: +0.0379766338.

Those values remain preserved for auditability but no longer define the manuscript-facing Experiment-06 primary result.

Historical standalone \(R\), \(A\), \(R+A\), \(M+R\), and \(M+A\) ablations were not rerun under the corrective CLEAN design. They therefore must not be used to localize the corrected increment to radial or axial sub-blocks.

## Experiment 07 provenance cross-check

Experiment 07 was prospectively frozen and executed before the later corrective Experiment-06 identity-map repair. It reused the **historical Experiment-06 checkpoint fold map**, with test-row counts 459, 460, 462, 460, and 459.

Those folds remain authoritative for Experiment 07 itself. They are not the corrected Experiment-06 primary folds.

Experiment 07 therefore remains a secondary conventional-descriptor comparator under its own frozen historical provenance. Its HOG and HOG+RA14 outcomes are retained unchanged, including bootstrap intervals crossing zero. It must not be described as a same-fold rerun of the corrected CLEAN Experiment-06 primary comparison.

## Representation and diagnostic analyses

Representation, reconstruction, rotation, discretization, harmonic, phase-conditioning, association, and related diagnostic analyses retain their own frozen provenance. Where a diagnostic analysis used a historical fold map, that historical design is not silently rewritten to the later corrective Experiment-06 map.

The corrective Experiment-06 analysis changes the manuscript-facing primary predictive claim; it does not retroactively redesign already frozen diagnostic or secondary experiments.

## Overall decision

**PASS, conditional on manuscript integration.**

The corrected Methods and Results now have a one-to-one inferential architecture for the manuscript-facing Experiment-06 primary claim. Historical Experiment-06 evidence, Experiment-07 evidence, the post-outcome target-text sensitivity, and Experiment-08 exploratory evidence retain distinct chronology and inferential status.

Remaining editorial projections must preserve these boundaries and must not reintroduce the historical Experiment-06 result as the current primary outcome.
