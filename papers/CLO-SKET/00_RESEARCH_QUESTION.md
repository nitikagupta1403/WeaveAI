# CLO-SKET — Final Research Questions

## 1. Object of study

This study treats garment-sketch morphology as a measurable geometric property of a sketch population.

Each of the 2,300 CLO-SKET sketches is described using two explicit representations:

1. a 135-dimensional morphology vector containing horizontal occupancy, vertical occupancy, and global geometric descriptors; and
2. a separately constructed 28-dimensional radial–angular vector containing radial, circular, and relational descriptors.

Neither representation is constructed using garment-category labels. Category labels are used only in downstream evaluation, balanced partitioning, and category-stratified uncertainty analyses.

---

## 2. Primary research question

> **Can explicit image-derived measurements characterize garment sketches as a quantitatively organized morphological population, and does a separately constructed radial–angular description provide additional task-relevant structure under source-garment-identity-disjoint evaluation?**

This question is representation-focused. Classification is used as a controlled evaluation of task-level utility rather than as the sole scientific objective.

---

## 3. Research Question 1 — Quantitative morphology organization

> **Does the explicit 135-dimensional morphology representation exhibit reproducible population-level quantitative organization without using category labels in its construction?**

### Operational meaning

“Quantitative organization” refers to non-random and reproducible structure detected through complementary analyses of:

- standardized variance and PCA coordinates;
- local neighborhoods;
- graph and geodesic relationships;
- multiscale density organization;
- regional feature profiles;
- cross-scale stability; and
- corresponding permutation or null controls.

### Evidence required

Support requires convergence across multiple organization analyses rather than visual separation in a single PCA plot or statistical significance in isolated tests.

### Supported interpretation

> The examined CLO-SKET population exhibits measurable quantitative organization under the specified explicit morphology representation.

### Claim boundary

This question does not test or establish:

- discrete semantic garment states;
- semantic garment parts;
- a universal morphology vocabulary;
- morphology primitives;
- a compositional grammar;
- a mathematical manifold; or
- an intrinsic dimensionality of 73.

---

## 4. Research Question 2 — Cross-representation overlap and recoverability

> **Which radial–angular quantities are associated with explicit morphology and recoverable from morphology for source-garment identities not observed during model training?**

### Operational meaning

This question is evaluated at two levels:

1. feature-wise Spearman associations between the 135 morphology coordinates and predefined radial–angular targets; and
2. source-grouped out-of-fold prediction of those targets from morphology using a fixed Ridge-regression pipeline.

### Radial–angular targets

The four frozen targets are:

1. F2 peak magnitude;
2. F2 peak radius;
3. observed R2 at the matched F2 peak shell; and
4. axial-disagreement magnitude between observed and learned orientations at that shell.

The fourth target is a scalar disagreement magnitude on [0°, 90°]. It is not direct prediction of axial orientation.

### Evidence required

Primary evidence comes from source-identity-grouped out-of-fold predictions, summarized using:

- R²;
- mean absolute error;
- root-mean-square error;
- Spearman rank correlation; and
- identity-aware bootstrap intervals.

### Supported interpretation

> Several radial–angular quantities are partially recoverable from morphology across unseen source-garment identities, indicating heterogeneous representational overlap.

### Claim boundary

Recoverability does not establish:

- causality;
- equivalence of the two representations;
- complete redundancy;
- statistical independence;
- semantic interpretation; or
- that morphology directly generates radial–angular geometry.

---

## 5. Research Question 3 — Source-grouped downstream complementarity

> **Does adding the 28-dimensional radial–angular representation improve 23-category discrimination beyond the 135-dimensional morphology representation when complete source-garment identities are withheld from training?**

### Operational meaning

The primary comparison uses five exact category-balanced grouped folds:

- 230 complete source-garment identities;
- 10 identities per category;
- two test identities per category in every fold;
- all 23 categories represented in every fold;
- zero source-identity overlap between training and test;
- every identity and sketch tested exactly once.

Three inputs are compared under identical folds and a fixed classifier:

1. morphology alone;
2. radial–angular geometry alone; and
3. morphology plus radial–angular geometry.

### Primary metrics

- pooled out-of-fold Macro-F1;
- pooled out-of-fold balanced accuracy.

### Robustness evidence

The paired integration effect is additionally evaluated through:

- fold-level direction of effect;
- category-level F1 comparisons;
- a 5,000-replicate category-stratified source-identity bootstrap; and
- ten independently generated exact-balanced grouped partitions.

### Supported interpretation

> Under the tested classifier and source-grouped design, radial–angular geometry provides modest, reproducible task-level utility beyond morphology.

### Claim boundary

This question does not establish:

- universal classifier improvement;
- superiority across other tasks or datasets;
- model-family robustness;
- external generalization beyond CLO-SKET;
- information-theoretic independence; or
- the mechanism responsible for the improvement.

---

## 6. Control Question — Exact held-out alignment

> **Does the grouped integration advantage depend specifically on the exact morphology–radial–angular pairing of each held-out sketch, beyond garment-category membership and category-level radial–angular distributions?**

### Operational meaning

Within each grouped test fold, radial–angular rows are permuted within garment category. This preserves:

- the test categories;
- the number of observations per category;
- the category-level radial–angular distributions;
- the morphology rows;
- the trained fold-specific models; and
- the source-grouped partitions.

It disrupts only the exact pairing between held-out morphology and radial–angular rows.

### Interpretation rule

The control asks whether correct test-time pairing improves fixed-model predictions relative to a category-preserving misalignment distribution. It is not a model-refitting permutation test.

### Final evidentiary status

The aligned-minus-permuted advantages were:

- Macro-F1: +0.006153, empirical p = 0.141929;
- balanced accuracy: +0.006842, empirical p = 0.122939.

Therefore:

> **Exact sketch-pair-specific complementarity was not established under the specified alignment control.**

The supported downstream claim remains task-level complementarity. Category-conditioned or population-level radial–angular structure may account for part of the integrated advantage.

---

## 7. Supplementary sensitivity question — Direct axial orientation

> **Can morphology recover observed axial orientation more effectively than a category-conditioned mean-direction baseline when orientation is represented in an axially correct form?**

### Operational meaning

Morphology predicts:

\[
\cos(2\alpha)
\quad \text{and} \quad
\sin(2\alpha),
\]

after which the axial angle is reconstructed and evaluated using folded axial angular error.

### Evidentiary status

The results are mixed:

- morphology reduces mean angular error;
- morphology worsens median angular error;
- morphology performs worse within 10°;
- morphology performs slightly better within 30° and on axial agreement.

### Role in the paper

This question is supplementary. It demonstrates appropriate directional treatment but does not support a simple positive direct-orientation-recovery claim.

---

## 8. Historical reproduction question

> **Can the original image-level classification and morphology-to-radial–angular recovery results be reproduced exactly before applying stricter source-grouped validation?**

### Purpose

Historical reproduction verifies:

- frozen features and targets;
- estimator identity;
- split definitions;
- preprocessing placement;
- metric calculations; and
- row provenance.

### Interpretation boundary

Historical image-level classification evaluates unseen sketches of source garments represented during training. It is not the primary evidence for unseen-garment generalization.

---

## 9. Hypothesis structure

The study is primarily empirical and partly exploratory. The following hypotheses organize the tested evidence without implying preregistration.

### H1 — Morphology organization

The explicit morphology representation exhibits reproducible quantitative organization beyond the specified null structures.

### H2 — Partial cross-representation overlap

At least some predefined radial–angular quantities are recoverable from morphology across source-identity-disjoint folds.

### H3 — Grouped task-level complementarity

The integrated representation outperforms morphology alone under exact source-grouped evaluation.

### H4 — Split robustness

The direction of the integrated-minus-morphology effect remains positive across independently generated exact-balanced grouped partitions.

### Mechanistic control, not a confirmed hypothesis

The exact held-out morphology–radial–angular pairing may contribute beyond category-conditioned radial–angular structure. The completed alignment analysis did not resolve this effect and therefore does not support a positive mechanistic claim.

---

## 10. Evidence map

| Scientific question | Primary analysis | Control or uncertainty analysis | Supported conclusion |
|---|---|---|---|
| Is morphology quantitatively organized? | Population-level morphology analyses | Neighborhood, scale, density, and permutation nulls | Organization under the specified representation |
| Are the representations related? | Feature associations and grouped recovery | Identity-aware recovery bootstrap | Partial heterogeneous overlap |
| Does integration help unseen identities? | Exact grouped classification | Paired identity bootstrap | Modest task-level complementarity |
| Is the result partition-specific? | Ten exact-balanced grouped partitions | Fold-level direction audit | Positive across tested allocations |
| Does exact pairing explain the gain? | Within-category alignment perturbation | 2,000 fixed-model perturbations | Not established |
| Is direct axial orientation recovered? | Axial cos(2α)/sin(2α) regression | Paired identity bootstrap versus baseline | Mixed supplementary evidence |

---

## 11. Final answer to the research questions

The completed evidence supports the following integrated answer:

> The examined garment sketches exhibit reproducible quantitative organization under an explicit 135-dimensional morphology representation. Several radial–angular quantities are partially recoverable from morphology across unseen source-garment identities, demonstrating representational overlap. Under exact source-grouped evaluation, adding the 28-dimensional radial–angular representation yields a modest positive improvement over morphology alone, and this improvement is stable across identity-aware resampling and repeated grouped partitions. However, a category-preserving alignment control does not establish that the advantage depends on exact sketch-level pairing. The evidence therefore supports partial overlap and task-level complementarity within CLO-SKET, not statistical independence, semantic structure, or a proven pair-specific mechanism.

---

## 12. Claims explicitly outside scope

The study does not establish:

- semantic garment-part recognition;
- semantic novelty;
- universal morphology categories;
- semantic morphology primitives;
- a universal morphology vocabulary;
- a compositional morphology grammar;
- a mathematical morphology manifold;
- information-theoretic independence;
- causal mechanisms;
- external validity across sketch datasets;
- universal predictive superiority; or
- human-like visual understanding.

---

## 13. Claim-discipline rule

Every manuscript claim must follow:

```text
CLAIM
  ↓
ANALYSIS
  ↓
NUMERICAL EVIDENCE
  ↓
CONTROL OR UNCERTAINTY ESTIMATE
  ↓
CLAIM BOUNDARY
```

No claim should exceed the evaluation unit, model family, dataset, null hypothesis, or uncertainty design that produced its evidence.
