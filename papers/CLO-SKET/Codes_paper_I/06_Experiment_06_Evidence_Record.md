# Experiment 06 — Public Evidence Record

## Purpose

This file is the manuscript-facing public evidence record for the locked compact-representation experiment described in Sections 3.11–3.16 and 4.2–4.6 of the IVC manuscript.

It exists to make the exact inferential design, primary numerical results, and claim boundary visible in the repository without implying that a separate fully rerunnable Experiment 06 notebook is presently included in the public package.

## Scientific question

Experiment 06 tested whether the frozen 14-dimensional axial–radial representation added garment-category predictive utility beyond the frozen 135-dimensional morphology representation when complete source-garment identities were withheld from validation.

The seven prespecified feature sets were:

- R: 8 radial descriptors;
- A: 6 axial descriptors;
- R+A: 14 descriptors;
- M: 135 morphology coordinates;
- M+R: 143 coordinates;
- M+A: 141 coordinates;
- M+R+A: 149 coordinates.

The prospectively locked primary contrast was

\[
\Delta F_1 = F_1^{\mathrm{macro}}(M+R+A)-F_1^{\mathrm{macro}}(M),
\]

with the analogous balanced-accuracy difference secondary.

## Validation lock

- Dataset rows: 2,300 sketches.
- Garment categories: 23.
- Recovered garment identities: 230, exactly 10 per category.
- Primary validation: five category-balanced garment-identity-disjoint folds.
- Test identities per fold: 46, exactly two from each category.
- Train identities per fold: 184.
- Train/test garment-identity overlap: 0.
- Primary metric: pooled out-of-fold macro-F1.
- Secondary metric: pooled out-of-fold balanced accuracy.

Every feature set used training-fold `StandardScaler` followed by `LogisticRegression` with L2 penalty, `C=1.0`, `solver="lbfgs"`, `max_iter=5000`, `class_weight=None`, and `random_state=20260820`. No hyperparameter search or feature-set-specific classifier change was used.

## Primary pooled results

| Feature set | Dimensions | Macro-F1 | Balanced accuracy |
|---|---:|---:|---:|
| R | 8 | 0.206831 | 0.224348 |
| A | 6 | 0.081165 | 0.106522 |
| R+A | 14 | 0.219993 | 0.231304 |
| M | 135 | 0.297788 | 0.298261 |
| M+R | 143 | 0.324540 | 0.325217 |
| M+A | 141 | 0.300087 | 0.300435 |
| M+R+A | 149 | 0.335765 | 0.336087 |

Primary observed increments:

- Macro-F1: +0.037977.
- Balanced accuracy: +0.037826.

The macro-F1 increment was positive in all five primary folds. Balanced-accuracy differences were also positive in all five folds.

## Identity-bootstrap uncertainty

A category-stratified paired bootstrap resampled complete garment identities within category while retaining paired frozen out-of-fold predictions.

- Replicates: 5,000.
- Macro-F1 observed increment: +0.037977.
- Macro-F1 bootstrap mean: +0.037909.
- Macro-F1 percentile 95% interval: [+0.020242, +0.055852].
- Positive Macro-F1 replicates: 5000 / 5000.
- Balanced-accuracy observed increment: +0.037826.
- Balanced-accuracy bootstrap mean: +0.037968.
- Balanced-accuracy percentile 95% interval: [+0.020000, +0.056239].
- Positive balanced-accuracy replicates: 5000 / 5000.

The fraction positive is descriptive and is not a permutation probability.

## Repeated grouped-partition stability

Ten category-balanced grouped five-fold repetitions used seeds 20260820 through 20260829.

| Quantity | Mean | SD | Minimum | Maximum | Positive repeats |
|---|---:|---:|---:|---:|---:|
| Full increment, Macro-F1 | +0.032253 | 0.006805 | +0.020620 | +0.043275 | 10 / 10 |
| Full increment, balanced accuracy | +0.031565 | 0.007362 | +0.019565 | +0.043913 | 10 / 10 |
| Radial increment, Macro-F1 | +0.028850 | — | — | — | 10 / 10 |

At the fold level, 44 of 50 macro-F1 differences were positive.

## Category-preserving alignment control

The alignment control asked a stronger question: whether the incremental utility required exact garment-level morphology–axial–radial pairing.

Complete R+A identity blocks were reassigned within garment category while also matching identity block size. This preserved category composition and repeated-measure block size while disrupting exact garment-level correspondence. Because six identities belonged to singleton category-by-size strata, 2.6087% of rows necessarily self-mapped; 97.3913% of rows were misaligned in every permutation.

- Permutations: 2,000.
- Same five frozen grouped folds.
- Same fold-local scaling and locked logistic-regression specification.
- One-sided corrected empirical probability:

\[
p = \frac{1+\sum_{b=1}^{B}\mathbf 1[\Delta_b^{\mathrm{null}}\geq\Delta_{\mathrm{obs}}]}{B+1},\qquad B=2000.
\]

| Metric | Observed increment | Null mean | Null SD | Null 2.5% | Null 97.5% | Empirical p |
|---|---:|---:|---:|---:|---:|---:|
| Macro-F1 | +0.037977 | +0.042896 | 0.007141 | +0.029088 | +0.056838 | 0.762619 |
| Balanced accuracy | +0.037826 | +0.042258 | 0.007145 | +0.028261 | +0.056522 | 0.729635 |

The correctly aligned effect did not exceed the category-preserving misalignment null.

## Supported conclusion

Experiment 06 supports reproducible incremental predictive utility of the compact axial–radial representation for the locked category-discrimination task under unseen-garment-identity evaluation.

It does **not** support the stronger claim that the utility requires exact garment-specific morphology–axial–radial correspondence. It also does not establish statistical independence, information-theoretic uniqueness, semantic understanding, or causality.

## Historical-exposure disclosure

The compact-representation experiment was not historically blind. Before its outcome was computed, frozen metadata had exposed a positive result for an earlier broader 28-dimensional radial–angular representation (macro-F1 increment +0.070984; balanced-accuracy increment +0.073043). The compact-representation feature definition, estimator, validation unit, primary contrast, bootstrap count, repeated-partition count, and alignment-permutation count were frozen before the compact outcome was computed. This distinction is retained explicitly in the manuscript.

## Public reproducibility status

This file is an evidence/provenance record, not a substitute for executable code. The public repository currently contains the Paper-I source measurement and validation notebooks listed in `README.md`, but it does **not** claim that a separate standalone rerunnable Experiment 06 notebook or frozen Experiment 06 runtime bundle is present unless such a file is explicitly deposited in this directory.

Accordingly, manuscript Code Availability language must not describe a nonexistent standalone Experiment 06 evidence bundle as publicly available.
