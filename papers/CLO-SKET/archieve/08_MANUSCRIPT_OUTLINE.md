# CLO-SKET — Final Manuscript Outline

## 0. Manuscript identity

### Preferred title

**Quantitative Organization of Garment-Sketch Morphology through Complementary Geometric Representations**

### Alternative titles

1. **Explicit Morphology and Radial–Angular Geometry in Garment Sketches**
2. **Identity-Aware Evaluation of Complementary Geometric Representations for Garment Sketches**
3. **Quantitative Garment-Sketch Morphology under Source-Identity-Disjoint Evaluation**

### Title boundary

The title must not claim:

- semantic language;
- morphology primitives;
- a morphology grammar;
- a mathematical manifold;
- independent information; or
- universal garment morphology.

---

## 1. Central scientific question

> Can garment sketches be represented as a quantitatively organized population using explicit image-derived morphology measurements, and does a separately constructed radial–angular description provide additional task-relevant structure under source-garment-identity-disjoint evaluation?

This question contains three linked but distinct components:

1. **Organization:** Does the explicit morphology representation exhibit reproducible population-level quantitative structure?
2. **Overlap:** Which radial–angular quantities are associated with and recoverable from morphology across unseen source identities?
3. **Complementarity:** Does integrating radial–angular geometry improve downstream discrimination beyond morphology alone when complete source garments are withheld?

A fourth control question constrains the mechanism:

4. **Alignment:** Does the integrated advantage depend on the exact morphology–radial–angular pairing of each held-out sketch?

---

## 2. Central scientific claim

The strongest supported claim is:

> Across source-garment-identity-disjoint evaluation, an independently constructed radial–angular representation provides modest but reproducible task-level utility beyond explicit morphology for the examined 23-category CLO-SKET discrimination task.

The mandatory qualification is:

> A category-preserving alignment control did not establish that the improvement depends specifically on exact sketch-level morphology–radial–angular pairing.

The paper therefore supports **partial representational overlap and task-level complementarity**, not statistical independence or a proven pair-specific mechanism.

---

## 3. Contribution hierarchy

### Primary contribution

**Source-grouped task-level complementarity between explicit morphology and radial–angular geometry.**

Evidence:

- exact zero-overlap source-grouped folds;
- pooled paired performance comparison;
- positive effects in all five primary folds;
- identity-aware bootstrap intervals;
- positive effects across ten exact-balanced grouped partitions.

### Secondary contribution

**Explicit population-level morphology characterization and source-grouped cross-representation recovery.**

Evidence:

- transparent 135-dimensional morphology coordinates;
- label-free morphology-space analyses;
- feature-level associations;
- grouped recovery of four radial–angular targets.

### Supporting negative boundary

**Exact held-out sketch alignment was not established as the mechanism of the integrated gain.**

This result must be reported, not hidden, because it prevents the stronger complementarity claim from exceeding the evidence.

---

## 4. Paper logic

The manuscript should follow one evidence chain:

1. define explicit morphology;
2. characterize population-level organization;
3. construct a distinct radial–angular coordinate system;
4. establish exact row provenance;
5. quantify shared structure using association and grouped recovery;
6. expose leakage in the historical image-level evaluation;
7. evaluate integration using exact source-grouped folds;
8. quantify identity-sampling and split-allocation robustness;
9. test whether exact held-out pairing explains the gain;
10. constrain the final scientific claim.

The classification task is an evaluation instrument. It should not replace the representation-focused scientific question.

---

# Abstract

## Structure

The Abstract should contain six compact components.

### 1. Background

State that garment sketches encode form geometrically, but population-level explicit morphology and relationships between alternative geometric representations remain less established than task-specific recognition or generation.

### 2. Representations

Report:

- 2,300 CLO-SKET sketches;
- 23 garment categories;
- explicit 135-dimensional morphology representation;
- independently constructed 28-dimensional radial–angular representation.

### 3. Evaluation correction

State that filename provenance revealed 230 source-garment identities and that the primary analysis used exact category-balanced grouped folds with zero source-identity overlap.

### 4. Primary result

Report pooled grouped performance:

- morphology Macro-F1: 0.306847;
- integrated Macro-F1: 0.341445;
- increment: +0.034598;
- morphology balanced accuracy: 0.307826;
- integrated balanced accuracy: 0.342174;
- increment: +0.034348.

The Abstract may round these to four decimals if journal style requires:

- Macro-F1: 0.3068 → 0.3414, Δ = +0.0346;
- balanced accuracy: 0.3078 → 0.3422, Δ = +0.0343.

### 5. Robustness and mechanism

State:

- the improvements were positive in all five primary folds and all ten repeated grouped partitions;
- identity-bootstrap intervals excluded zero;
- within-category alignment perturbations did not establish an exact sketch-pair-specific mechanism (Macro-F1 p = 0.1419; balanced-accuracy p = 0.1229).

### 6. Conclusion

Conclude that the two explicit representations exhibit partial overlap and modest task-level complementarity under unseen-source-identity evaluation.

### Abstract exclusions

Do not include:

- the historical +0.071/+0.073 gains as the primary result;
- the phrase “reproducible sketch-level correspondence”;
- claims of independent information;
- semantic, primitive, grammar, or manifold terminology;
- supplementary direct-orientation results unless required by the journal.

---

# 1. Introduction

## Paragraph 1 — Object of study

Present garment sketches as abstract geometric representations of garment form rather than reduced photographs.

## Paragraph 2 — Representation problem

Position the gap relative to task-oriented garment modelling, recognition, retrieval, transfer, and generation.

## Paragraph 3 — Population-level morphology

Explain why jointly studying explicit geometric measurements across a sketch population is scientifically distinct from using them only as predictive inputs.

## Paragraph 4 — Explicit morphology representation

Introduce the 135-dimensional representation:

\[
\mathbf{x}_i = [\mathbf{h}_i,\mathbf{v}_i,\mathbf{g}_i]
\in \mathbb{R}^{135},
\]

with 64 horizontal, 64 vertical, and seven global descriptors.

## Paragraph 5 — Alternative radial–angular description

Introduce the 28-dimensional representation and its five blocks. Describe it as independently constructed, not statistically independent.

## Paragraph 6 — Evaluation problem

Explain why multiple sketches from one garment create a source-identity generalization problem. Introduce grouped evaluation without detailing the full algorithm.

## Paragraph 7 — Questions and controls

State the organization, overlap, complementarity, and alignment questions. Explain that the within-category control distinguishes general category-discriminative utility from exact pair-specific utility.

## Paragraph 8 — Contributions

End with three contributions:

1. explicit population-level morphology characterization;
2. grouped cross-representation recovery;
3. source-grouped downstream integration with uncertainty, robustness, and alignment controls.

### Introduction citation requirement

Replace the two `[CITATIONS]` placeholders using verified sources from Related Work before manuscript assembly.

---

# 2. Related Work

## 2.1 Computational geometry of garment sketches

Cover sketch-based garment modelling and geometry transfer:

- Yasseen et al.;
- Fondevilla et al.;
- Wang et al.

Use these studies to establish that sketches contain computationally recoverable garment geometry while distinguishing their task-oriented goals.

## 2.2 Fashion flats and silhouette descriptors

Cover:

- An and Li's wavelet Fourier descriptor work;
- Tsuru et al.'s quantitative silhouette analysis.

Explicitly state that geometric descriptors, Fourier operations, multivariate analysis, and PCA are not individually claimed as novel.

## 2.3 Geometric morphometrics and population-level shape

Use Bookstein and McCane to motivate explicit population-level shape analysis while clarifying that the current representation is not a conventional landmark morphometric model.

## 2.4 Alternative representations and cross-representation evidence

Distinguish association, recoverability, redundancy, and complementarity.

## 2.5 Identity-aware evaluation

Explain the inferential difference between:

- unseen sketches of observed garments; and
- unseen source-garment identities.

## 2.6 Research gap

End with the three principal research questions. Do not claim that no prior paper has ever examined fashion-sketch morphology unless a systematic search supports that absolute statement.

---

# 3. Methods

## 3.1 Study design

Summarize the representation-focused analytical sequence and distinguish primary from supplementary analyses.

## 3.2 Dataset and source-identity reconstruction

Report:

- 2,300 TIFF sketches;
- 23 categories;
- 100 sketches per category;
- 230 source-garment identities;
- 10 identities per category;
- 9–11 images per identity;
- filename separators `-`, `_`, and one `+`;
- irregular replicate identifiers and duplicated identity–replicate combinations;
- retention of all images.

Define garment identity as category plus the first numeric filename token.

## 3.3 Morphology representation

Describe:

- 64 × 64 grayscale canonicalization;
- intensity division by 255;
- foreground threshold below 0.8;
- 64 horizontal occupancy coordinates;
- 64 vertical occupancy coordinates;
- seven global descriptors;
- exact reconstructed SHA-256.

## 3.4 Morphology-space organization

Describe standardization, 95%-variance PCA retention, local-neighborhood, spectral, graph, density, transition, and null analyses. Do not interpret density regions semantically.

## 3.5 Radial–angular representation

Define the centroid-referenced construction and the five descriptor blocks. Report the locked 25-shell domain from 3.5 to 27.5 and exact peak-shell matching.

## 3.6 Provenance verification

State that both branches contained 2,300 unique paths and matched exactly in frozen row order.

## 3.7 Feature-level association

Describe Spearman correlation and target-wise Benjamini–Hochberg correction across 135 morphology coordinates.

## 3.8 Cross-validation designs

### Historical image-level folds

State that every test sketch had its source identity in training. Retain only for reproduction.

### Primary grouped folds

State:

- five folds;
- exactly two test identities per category;
- all 23 categories in every fold;
- 46 test identities per fold;
- 459–461 test images;
- zero source-identity overlap;
- every row and identity tested once.

### Repeated grouped folds

Report ten exact-balanced partitions using seeds 20260820–20260829.

## 3.9 Classification

Define the fixed within-fold `StandardScaler` plus multinomial L2 logistic-regression pipeline. State that no feature selection or hyperparameter search was performed.

## 3.10 Identity-aware uncertainty

Describe the category-stratified clustered bootstrap of complete source identities, 5,000 replicates, paired predictions, and percentile intervals. Explicitly state that models were not refitted.

## 3.11 Alignment control

Describe 2,000 within-category held-out radial–angular permutations using fixed fold-specific models. State the exact null question and distinguish it from a refitting permutation test.

## 3.12 Morphology-to-radial–angular recovery

Define the within-fold `StandardScaler` plus `Ridge(alpha=1.0)` pipeline, historical KFold reproduction, and grouped primary evaluation.

Name the fourth target “axial-disagreement magnitude,” not “axial orientation.”

## 3.13 Recovery uncertainty

Describe the 5,000-replicate category-stratified identity bootstrap with fixed grouped out-of-fold predictions.

## 3.14 Supplementary direct orientation

Describe prediction of cos(2α) and sin(2α), reconstruction of axial orientation, the category-conditioned mean-direction baseline, axial angular error, and paired identity bootstrap.

## 3.15 Reproducibility

Report software versions, fixed random states, frozen hashes, read-only arrays, result-package hashes, and the archived Validation Shield.

---

# 4. Results

## 4.1 Population and representation integrity

Report the exact population, identity structure, representation dimensions, finite-value checks, exact morphology hash, and row-level alignment.

Place:

- Figure 1;
- Table 1.

## 4.2 Morphology-space organization

Present the strongest convergent label-free evidence without enumerating every notebook result.

Place:

- Figure 2;
- morphology-evidence summary table if needed.

Avoid describing density regions as garment states.

## 4.3 Feature-level associations

Summarize association magnitudes, spatial patterns, and FDR results. Emphasize effect size rather than the number of significant coordinates.

## 4.4 Source-identity audit

Report that all historical test rows shared source identities with training and that grouped folds achieved exact zero overlap.

Place:

- Table 2;
- Supplementary Figure S1.

## 4.5 Historical integration reproduction

Report only as historical context:

- morphology fold-mean Macro-F1: 0.3411;
- integrated fold-mean Macro-F1: 0.4123;
- increment: +0.0712;
- morphology fold-mean balanced accuracy: 0.3422;
- integrated fold-mean balanced accuracy: 0.4157;
- increment: +0.0735.

Immediately state that this evaluates unseen sketches of observed source garments.

## 4.6 Primary grouped integration

Report pooled results:

| Representation | Macro-F1 | Balanced accuracy |
|---|---:|---:|
| Morphology | 0.306847 | 0.307826 |
| Radial–angular | 0.265323 | 0.276087 |
| Integrated | **0.341445** | **0.342174** |
| Integrated minus morphology | **+0.034598** | **+0.034348** |

State that both increments were positive in all five folds.

Place:

- Figure 3 or Figure 4;
- Table 3.

## 4.7 Identity uncertainty and split robustness

Report:

- Macro-F1 increment interval: [0.015783, 0.053962];
- balanced-accuracy increment interval: [0.015612, 0.054268];
- ten of ten repeated partition effects positive;
- mean repeated increments 0.042304 and 0.040609;
- 49/50 fold effects positive for each metric.

Place:

- Figure 4 Panel C;
- Figure 5;
- Table 4.

## 4.8 Alignment control

Report:

- Macro-F1 aligned-minus-permuted mean: +0.006153, p = 0.141929;
- balanced-accuracy aligned-minus-permuted mean: +0.006842, p = 0.122939.

State that exact sketch-level alignment was not established as the mechanism.

Place:

- Figure 6;
- Table 6.

## 4.9 Grouped recovery

Report all four targets:

| Target | R² | Spearman ρ |
|---|---:|---:|
| F2 peak magnitude | 0.302221 | 0.631055 |
| F2 peak radius | 0.014269 | 0.324874 |
| R2 at F2 peak | 0.190971 | 0.521587 |
| Axial-disagreement magnitude | 0.206346 | 0.442901 |

Interpret peak-radius recovery cautiously because its R² interval includes zero.

Place:

- Figure 7;
- Table 5.

## 4.10 Direct axial-orientation sensitivity

Present as supplementary and explicitly mixed:

- mean error improved;
- median error worsened;
- within 10° worsened;
- within 30° and axial agreement improved.

Do not convert this into a one-directional success claim.

## 4.11 Integrated claim boundary

Close Results with three statements:

1. the branches exhibit partial overlap;
2. integration yields modest reproducible grouped task-level utility;
3. exact pair-specific alignment was not established as the mechanism.

---

# 5. Discussion

## 5.1 Principal findings

Lead with the grouped result, not the historical result.

## 5.2 Morphology as a quantitative population

Explain the value and limitations of an explicit interpretable coordinate system. Avoid semantic interpretations.

## 5.3 Complementarity under unseen-source-identity evaluation

Discuss the reduction from the historical gain to the grouped gain as evidence that evaluation design matters. Emphasize that the grouped effect remains consistently positive.

## 5.4 Shared structure without a proven alignment mechanism

Integrate recovery and alignment results:

- recovery demonstrates partial shared structure;
- grouped integration demonstrates task-level complementarity;
- the alignment control does not prove exact pair dependence;
- category-conditioned or population-level radial–angular structure may contribute materially.

## 5.5 Recovery heterogeneity

Contrast F2 peak magnitude, R2, disagreement magnitude, and weak peak-radius variance recovery.

## 5.6 Scientific contribution

Position the contribution as empirical and validation-focused, not as a new descriptor or classifier.

## 5.7 Limitations

Include:

1. one dataset and no external replication;
2. handcrafted and preprocessing-dependent representations;
3. fixed classifier family;
4. fixed-prediction bootstrap intervals;
5. non-refitting alignment control;
6. mixed direct-orientation result;
7. no semantic validation;
8. incomplete robustness to alternative resolution and threshold choices.

## 5.8 Future work

Prioritize:

1. external dataset replication;
2. preprocessing/resolution sensitivity;
3. model-family robustness under identical grouped folds;
4. stronger conditional or refitting alignment tests if pair-specificity becomes a target claim;
5. expert semantic validation only if semantic interpretation is later pursued.

## 5.9 Conclusion

End with the narrow validated statement:

> Explicit morphology and radial–angular geometry provide partially overlapping descriptions of the examined garment-sketch population, and their integration yields modest, reproducible task-level utility under source-garment-disjoint evaluation. The evidence does not establish statistical independence, semantic structure, or an exact sketch-pair-specific mechanism.

---

# 6. Supplementary material

## Supplementary S1 — Complete feature definitions

- all 135 morphology coordinates;
- all 28 radial–angular descriptors;
- preprocessing definitions and units.

## Supplementary S2 — Identity reconstruction audit

- separator irregularities;
- identity and replicate distributions;
- duplicated identity–replicate records;
- fold assignments.

## Supplementary S3 — Full morphology-organization analyses

- all neighborhood, graph, density, scale, and null results.

## Supplementary S4 — Feature-level associations

- complete Spearman coefficients;
- raw and FDR-adjusted p-values;
- spatial-coordinate summaries.

## Supplementary S5 — Historical reproduction

- historical image-level classification;
- exact Ridge/KFold estimator reproduction;
- historical permutation controls;
- explicit seen-source-identity boundary.

## Supplementary S6 — Repeated grouped results

- all ten partitions;
- every fold-level metric;
- convergence audit.

## Supplementary S7 — Alignment perturbations

- full 2,000-replicate distributions;
- empirical calculation;
- fixed-model scope.

## Supplementary S8 — Grouped recovery bootstrap

- intervals for R², Spearman ρ, MAE, and RMSE;
- bootstrap design details.

## Supplementary S9 — Direct axial orientation

- cos(2α)/sin(2α) model;
- baseline definition;
- paired effects and intervals.

## Supplementary S10 — Reproducibility manifest

- software environment;
- random seeds;
- SHA-256 values;
- notebook-to-table mapping;
- final archive receipt.

---

# 7. Figure and table placement

| Manuscript location | Primary visual |
|---|---|
| Introduction | Figure 1, if journal permits an overview figure early |
| Results 4.2 | Figure 2 |
| Results 4.4–4.6 | Figure 3 and Table 2 |
| Results 4.6–4.7 | Figure 4 and Tables 3–4 |
| Results 4.7 | Figure 5 or supplementary equivalent |
| Results 4.8 | Figure 6 and Table 6 |
| Results 4.9 | Figure 7 and Table 5 |
| Results 4.10 | Supplementary Figure S3 |
| Discussion | Table 7 only if a compact evidence ledger is useful |

---

# 8. Numerical reporting conventions

1. Use six decimals in canonical result tables.
2. Use four decimals in prose unless additional precision is needed to reproduce an empirical probability.
3. Use leading zeros for decimal values.
4. Report absolute metric increments, not percentage improvements, unless both are explicitly distinguished.
5. Use “percentage points” only after multiplying a metric increment by 100.
6. Distinguish pooled out-of-fold metrics from fold-mean metrics.
7. Do not attach confidence-interval terminology to permutation distributions.
8. Do not call fixed-prediction bootstrap fractions independent p-values.

---

# 9. Terminology lock

## Use

- explicit morphology representation;
- independently constructed radial–angular representation;
- quantitative organization;
- partial representational overlap;
- cross-validated recoverability;
- task-level complementarity;
- source-garment-identity-disjoint evaluation;
- category-preserving alignment control;
- axial-disagreement magnitude;
- direct axial-orientation sensitivity analysis.

## Avoid or explicitly reject

- independent information;
- true sketch-level correspondence as an established mechanism;
- semantic language;
- morphology primitive;
- morphology grammar;
- morphology manifold;
- intrinsic dimensionality of 73;
- causal recovery;
- universal classification improvement;
- external validation.

---

# 10. Final manuscript architecture

```text
TITLE
ABSTRACT
1. INTRODUCTION
2. RELATED WORK
3. METHODS
   3.1 Study design
   3.2 Dataset and source identities
   3.3 Morphology representation
   3.4 Morphology organization
   3.5 Radial–angular representation
   3.6 Provenance
   3.7 Feature associations
   3.8 Cross-validation designs
   3.9 Classification
   3.10 Identity bootstrap
   3.11 Alignment control
   3.12 Grouped recovery
   3.13 Recovery uncertainty
   3.14 Direct axial orientation
   3.15 Reproducibility
4. RESULTS
   4.1 Population and integrity
   4.2 Morphology organization
   4.3 Feature associations
   4.4 Source-identity audit
   4.5 Historical reproduction
   4.6 Primary grouped integration
   4.7 Uncertainty and robustness
   4.8 Alignment control
   4.9 Grouped recovery
   4.10 Axial-orientation sensitivity
   4.11 Claim boundary
5. DISCUSSION
   5.1 Principal findings
   5.2 Quantitative morphology
   5.3 Grouped complementarity
   5.4 Alignment boundary
   5.5 Recovery heterogeneity
   5.6 Contribution
   5.7 Limitations
   5.8 Future work
   5.9 Conclusion
REFERENCES
SUPPLEMENTARY MATERIAL
```

---

# 11. Final manuscript narrative

The manuscript should tell one coherent story:

> Garment sketches can be represented using explicit, interpretable morphology coordinates and a separately constructed radial–angular coordinate system. The two representations share measurable structure, but neither fully substitutes for the other. When complete source-garment identities are withheld, integrating radial–angular geometry with morphology yields a modest positive improvement that is stable across folds, identity resampling, and repeated grouped partitions. A category-preserving alignment control does not establish that the gain depends on exact sketch pairing. The evidence therefore supports partial overlap and task-level complementarity within the examined CLO-SKET population, without requiring semantic, causal, independence, grammar, or manifold claims.
