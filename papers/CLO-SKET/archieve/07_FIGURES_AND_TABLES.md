# CLO-SKET — Final Figures and Tables Plan

## Purpose

This document defines the final visual evidence hierarchy for the CLO-SKET manuscript. It supersedes the pre-Validation-Shield figure plan.

The primary figures and tables must use **source-garment-identity-disjoint results**. Historical image-level results may appear only as explicitly labelled reproduction evidence. No visual may imply that exact sketch-level morphology–radial–angular alignment was established as the mechanism of improvement.

## Visual reporting rules

1. Use Macro-F1 as the primary downstream metric and balanced accuracy as a paired secondary metric.
2. Distinguish pooled out-of-fold metrics from fold means.
3. Label historical image-level folds as evaluation on unseen sketches of observed garment identities.
4. Label grouped folds as evaluation on unseen source-garment identities.
5. Show effect sizes and uncertainty intervals, not significance symbols alone.
6. State when intervals were computed from fixed out-of-fold predictions.
7. Keep bootstrap resampling, permutation controls, and repeated cross-validation conceptually separate.
8. Use “independently constructed” for the radial–angular branch; do not use “statistically independent.”
9. Do not use “semantic primitives,” “grammar,” “manifold,” or “intrinsic dimension” as established findings.
10. Do not describe the within-category alignment result as significant or mechanistically confirmatory.

---

# Main-text figures

## Figure 1 — Representations and validation design

### Purpose

Introduce the two representations, row-level provenance, source-identity structure, and the primary evaluation design in one compact schematic.

### Recommended panels

**Panel A — Explicit morphology**

- canonical 64 × 64 sketch;
- 64 horizontal occupancy coordinates;
- 64 vertical occupancy coordinates;
- seven global descriptors;
- final morphology vector: 135 dimensions.

**Panel B — Radial–angular geometry**

- centroid-referenced radial and angular construction;
- F2 radial: 9 dimensions;
- α2: 7 dimensions;
- observed circular: 3 dimensions;
- learned circular: 4 dimensions;
- relational: 5 dimensions;
- final radial–angular vector: 28 dimensions.

**Panel C — Identity-aware evaluation**

- 2,300 sketches;
- 23 categories;
- 230 source-garment identities;
- 10 identities per category;
- five grouped folds;
- two test identities per category per fold;
- zero source-identity overlap.

### Message

Two explicit geometric descriptions of the same sketches are evaluated under complete source-garment separation.

### Caption boundary

“Independently constructed” refers to the feature-construction branches, not to independent data or statistically independent information.

---

## Figure 2 — Quantitative organization of morphology space

### Purpose

Summarize the strongest label-free evidence that the explicit morphology representation exhibits reproducible population-level organization.

### Recommended panels

Select only the most interpretable analyses from the morphology notebook:

- standardized variance/PCA summary;
- local-neighborhood or graph-based organization;
- multiscale density organization;
- the corresponding null or permutation comparison.

### Message

The examined CLO-SKET population exhibits quantitative organization under the specified explicit morphology representation.

### Claim boundary

Density regions are not discrete garment states. Retaining 73 PCA coordinates at the selected variance threshold does not establish an intrinsic dimension or mathematical manifold.

---

## Figure 3 — Historical versus source-grouped integration

### Purpose

Make the validation correction transparent and show how source-identity separation changes the estimated integration effect.

### Recommended visualization

A paired dot or bar plot with two evaluation designs and two metrics:

| Evaluation | Morphology | Morphology + radial–angular | Increment |
|---|---:|---:|---:|
| Historical image-level Macro-F1 | 0.3411 | 0.4123 | +0.0712 |
| Grouped Macro-F1 | 0.306847 | 0.341445 | +0.034598 |
| Historical image-level balanced accuracy | 0.3422 | 0.4157 | +0.0735 |
| Grouped balanced accuracy | 0.307826 | 0.342174 | +0.034348 |

### Required annotation

- Historical: unseen sketches of source garments represented during training.
- Grouped: unseen source-garment identities; zero train–test identity overlap.

### Message

The integration advantage becomes smaller under source-identity separation but remains positive for both metrics.

### Important

The grouped comparison is the primary result. The historical comparison is included to document the effect of the evaluation correction, not to strengthen the final performance claim.

---

## Figure 4 — Primary grouped integration effect

### Purpose

Present the central result with fold-level consistency and identity-aware uncertainty.

### Recommended panels

**Panel A — Pooled grouped performance**

| Representation | Macro-F1 | Balanced accuracy |
|---|---:|---:|
| Morphology | 0.306847 | 0.307826 |
| Radial–angular | 0.265323 | 0.276087 |
| Morphology + radial–angular | **0.341445** | **0.342174** |

**Panel B — Paired fold effects**

Show morphology and integrated performance connected within each of the five grouped folds. Report that both metric increments were positive in all five folds.

**Panel C — Identity-bootstrap intervals**

| Metric increment | Observed | 95% percentile interval |
|---|---:|---:|
| Macro-F1 | +0.034598 | [0.015783, 0.053962] |
| Balanced accuracy | +0.034348 | [0.015612, 0.054268] |

### Message

Integration provides a modest, consistent task-level advantage under unseen-source-identity evaluation.

### Caption boundary

The 5,000 bootstrap replicates resampled complete source identities within category while holding grouped out-of-fold predictions fixed. The intervals do not include model-refitting variation.

---

## Figure 5 — Robustness across grouped partitions

### Purpose

Show that the primary effect is not specific to one identity-to-fold allocation.

### Recommended visualization

Plot the pooled integrated-minus-morphology increment for each of ten exact-balanced grouped partitions, with a horizontal line at zero and a summary mean ± SD.

| Metric | Mean increment | SD | Minimum | Maximum | Positive repeats |
|---|---:|---:|---:|---:|---:|
| Macro-F1 | 0.042304 | 0.007004 | 0.033574 | 0.052882 | 10/10 |
| Balanced accuracy | 0.040609 | 0.007127 | 0.031304 | 0.051739 | 10/10 |

Add the fold-level summary in the caption:

- positive Macro-F1 fold effects: 49/50;
- positive balanced-accuracy fold effects: 49/50;
- convergence warnings: 0.

### Message

The positive integration effect is robust to the tested identity-to-fold allocations.

### Claim boundary

Variation across repeated partitions is descriptive split-robustness evidence, not an independent confidence interval and not model-family robustness.

---

## Figure 6 — Within-category alignment control

### Purpose

Constrain the mechanism of the integration result.

### Recommended visualization

For each metric, plot the distribution of performance across 2,000 within-category held-out pairing perturbations and mark the aligned performance.

| Metric | Aligned | Permuted mean | Aligned minus permuted mean | Empirical p |
|---|---:|---:|---:|---:|
| Macro-F1 | 0.341445 | 0.335293 | +0.006153 | 0.141929 |
| Balanced accuracy | 0.342174 | 0.335332 | +0.006842 | 0.122939 |

Optional distribution intervals:

- Macro-F1 permuted 95% range: [0.324199, 0.345944];
- balanced-accuracy permuted 95% range: [0.323913, 0.346087].

### Message

Correct alignment was slightly better on average, but the effect was not resolved under the category-preserving null.

### Required caption language

The control preserves category membership and category-level radial–angular distributions while disrupting exact held-out sketch pairing. It tests fixed-model sensitivity to test-time alignment and is not a full model-refitting permutation test.

### Prohibited message

Do not state that the downstream improvement depends on true sketch-level correspondence.

---

## Figure 7 — Grouped recovery of radial–angular quantities

### Purpose

Quantify representational overlap across unseen source identities.

### Recommended visualization

Use observed-versus-out-of-fold-predicted panels or a compact coefficient/interval plot. Include R² and Spearman ρ together because the two metrics reveal different aspects of recovery.

| Target | R² | R² 95% identity-bootstrap interval | Spearman ρ |
|---|---:|---:|---:|
| F2 peak magnitude | 0.302221 | [0.266905, 0.333870] | 0.631055 |
| F2 peak radius | 0.014269 | [−0.042301, 0.066573] | 0.324874 |
| R2 at F2 peak | 0.190971 | [0.121399, 0.253892] | 0.521587 |
| Axial-disagreement magnitude | 0.206346 | [0.148195, 0.260074] | 0.442901 |

### Message

Morphology partially recovers several radial–angular quantities across unseen source identities, but recovery strength is heterogeneous and peak-radius variance recovery is weak.

### Claim boundary

Prediction establishes statistical recoverability, not causality or complete redundancy. “Axial-disagreement magnitude” is a scalar error magnitude, not direct prediction of axial orientation.

---

# Supplementary figures

## Supplementary Figure S1 — Source-identity reconstruction and grouped-fold audit

Show:

- 23 categories;
- 10 source identities per category;
- 9–11 images per identity;
- two identities per category in every test fold;
- fold sizes of 459–461;
- zero overlap;
- every row and identity tested exactly once.

This figure documents the filename irregularities without treating replicate identifiers as a perfectly balanced factorial design.

## Supplementary Figure S2 — Category-level classification effects

Show category-wise F1 for morphology, radial–angular, and integrated representations.

Report:

- integration improved 18 of 23 categories relative to morphology;
- integration improved 19 of 23 categories relative to radial–angular geometry.

Avoid ranking categories unless the manuscript has a category-specific hypothesis.

## Supplementary Figure S3 — Direct axial-orientation sensitivity analysis

Use paired summaries of morphology versus the category-conditioned mean-direction baseline.

Positive values should always denote a morphology advantage.

| Effect | Observed | 95% paired identity-bootstrap interval | Interpretation |
|---|---:|---:|---|
| Mean-error reduction, degrees | +1.447897 | [0.425764, 2.525118] | Morphology advantage |
| Median-error reduction, degrees | −1.348916 | [−1.811536, −0.889670] | Baseline advantage |
| R2-weighted mean-error reduction, degrees | +1.024246 | [−0.113484, 2.231822] | Interval includes zero |
| Increase within 10° | −0.051304 | [−0.069285, −0.033101] | Baseline advantage |
| Increase within 15° | −0.014348 | [−0.030435, 0.002606] | Interval includes zero |
| Increase within 30° | +0.017826 | [0.004778, 0.031767] | Morphology advantage |
| Axial-agreement increase | +0.048157 | [0.023101, 0.075019] | Morphology advantage |

### Message

Direct axial-orientation recovery is mixed and remains supplementary.

## Supplementary Figure S4 — Historical descriptor ablations

If retained, clearly label the analysis:

> Historical image-level exploratory ablation; source identities overlap between training and test.

The figure may document which radial–angular blocks contributed under the original setting, but it must not be presented as primary unseen-identity evidence or as proof that every block is independently significant.

## Supplementary Figure S5 — Historical recovery reproduction

Show exact reproduction of the original Ridge/KFold metrics before grouped validation. The purpose is estimator identification and provenance, not the final scientific claim.

---

# Main-text tables

## Table 1 — Study population and representations

| Item | Value |
|---|---:|
| Sketches | 2,300 |
| Categories | 23 |
| Sketches per category | 100 |
| Source-garment identities | 230 |
| Source identities per category | 10 |
| Images per source identity | 9–11 |
| Morphology dimensions | 135 |
| Radial–angular dimensions | 28 |
| Integrated dimensions | 163 |

## Table 2 — Cross-validation design audit

| Design | Folds | Test unit | Category balance | Source-identity overlap | Interpretation |
|---|---:|---|---|---:|---|
| Historical StratifiedKFold | 5 | Sketch | Preserved | Present in every fold | Unseen sketches of observed garments |
| Primary exact grouped | 5 | Complete source identity | Two identities/category/fold | 0 | Unseen source-garment identities |
| Repeated exact grouped | 10 × 5 | Complete source identity | Two identities/category/fold | 0 | Split-allocation robustness |

## Table 3 — Primary grouped classification results

| Representation | Macro-F1 | Balanced accuracy |
|---|---:|---:|
| Morphology | 0.306847 | 0.307826 |
| Radial–angular | 0.265323 | 0.276087 |
| Morphology + radial–angular | **0.341445** | **0.342174** |
| Integrated minus morphology | **+0.034598** | **+0.034348** |

## Table 4 — Identity-aware integration intervals

| Metric | Observed effect | 2.5th percentile | 97.5th percentile | Bootstrap replicates |
|---|---:|---:|---:|---:|
| Macro-F1 increment | +0.034598 | 0.015783 | 0.053962 | 5,000 |
| Balanced-accuracy increment | +0.034348 | 0.015612 | 0.054268 | 5,000 |

Caption must state that predictions were fixed and complete source identities were resampled within category.

## Table 5 — Grouped radial–angular recovery

| Target | R² | MAE | RMSE | Spearman ρ |
|---|---:|---:|---:|---:|
| F2 peak magnitude | 0.302221 | 0.013196 | 0.017027 | 0.631055 |
| F2 peak radius | 0.014269 | 4.080491 | 5.128389 | 0.324874 |
| R2 at F2 peak | 0.190971 | 0.127284 | 0.162518 | 0.521587 |
| Axial-disagreement magnitude | 0.206346 | 20.041103 | 26.323096 | 0.442901 |

## Table 6 — Alignment-control summary

| Metric | Observed aligned | Permuted mean | Aligned advantage | Empirical p | Perturbations |
|---|---:|---:|---:|---:|---:|
| Macro-F1 | 0.341445 | 0.335293 | +0.006153 | 0.141929 | 2,000 |
| Balanced accuracy | 0.342174 | 0.335332 | +0.006842 | 0.122939 | 2,000 |

## Table 7 — Evidence and claim boundary

| Question | Evidence | Supported conclusion | Boundary |
|---|---|---|---|
| Is morphology quantitatively organized? | Label-free population analyses and null controls | Organization under the specified representation | Not semantic states or a manifold |
| Are the branches related? | Feature associations and grouped recovery | Partial representational overlap | Not causality or equivalence |
| Does integration help unseen identities? | Exact grouped classification | Modest task-level complementarity | Task-, model-, and dataset-specific |
| Is the gain split-dependent? | Ten grouped partitions | Positive across tested allocations | Not model-family robustness |
| Does exact pairing explain the gain? | Within-category perturbations | Small positive aligned effect | Not resolved under the null |
| Does morphology directly recover orientation? | Proper axial sensitivity analysis | Mixed supplementary evidence | Not a primary claim |

---

# Visual priority for the main manuscript

If journal space is limited, retain the following four main figures:

1. Figure 1 — representations and grouped design;
2. Figure 2 — quantitative morphology organization;
3. Figure 4 — primary grouped integration with identity-bootstrap intervals;
4. Figure 6 or Figure 7 — alignment boundary or grouped recovery.

Use Figure 3 when transparency about the historical-to-grouped correction is especially important. Figure 5 can move to supplementary material if the repeated-partition summary is fully reported in text and table form.

---

# Final visual narrative

The figures and tables should communicate one evidence chain:

1. explicit morphology and radial–angular representations are constructed for the same 2,300 sketches;
2. morphology exhibits population-level quantitative organization;
3. the radial–angular branch is partially recoverable from morphology across unseen source identities;
4. integration modestly improves grouped discrimination over either representation alone;
5. the improvement is stable across identity-to-fold allocations;
6. exact sketch-level pairing is not established as the mechanism.

The final visual claim is therefore:

> The two explicit geometric representations exhibit partial overlap and modest, reproducible task-level complementarity under source-garment-disjoint evaluation, while category-preserving alignment controls prevent stronger pair-specific or independence claims.
