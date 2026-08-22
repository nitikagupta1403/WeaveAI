# CLO-SKET — Final Scientific Contribution

## 1. Central contribution

The central contribution of this study is an evidence-based framework for representing and evaluating garment-sketch morphology using two explicit geometric descriptions of the same sketch population.

The study does not claim a new machine-learning algorithm or mathematical operator. Its contribution is empirical and analytical. It shows that:

1. garment sketches can be represented using an explicit 135-dimensional morphology vector with directly interpretable spatial coordinates;
2. a separately constructed 28-dimensional radial–angular vector provides an alternative geometric description of the same sketches;
3. several radial–angular quantities are partially recoverable from morphology across source-garment identities not observed during training; and
4. combining the two representations provides a modest but reproducible improvement over morphology alone in source-identity-disjoint 23-category discrimination.

The final validation also establishes an important boundary: a within-category alignment control did not show that the downstream advantage depends specifically on the exact morphology–radial–angular pairing of each held-out sketch. The supported conclusion is therefore **task-level complementarity**, not proven sketch-pair-specific correspondence.

## 2. What is novel

The novelty lies primarily in the **scientific characterization and validation design**, rather than in any individual feature operator.

The study asks:

> Can explicit geometric measurements be used to characterize garment-sketch morphology as a population-level quantitative object, and does a separately constructed radial–angular description contribute additional task-relevant structure under source-identity-disjoint evaluation?

This differs from work whose principal objective is garment generation, retrieval, recognition, or semantic annotation. Here, classification is used as a controlled evaluation setting rather than being presented as the paper's sole contribution.

The contribution combines:

- explicit and reproducible representation construction;
- population-level morphology analysis;
- cross-representation recovery;
- source-identity-aware validation;
- paired, identity-aware uncertainty analysis;
- category-preserving alignment controls; and
- downstream comparison of morphology, radial–angular geometry, and their integration.

## 3. Contribution 1 — Explicit quantitative morphology representation

The study constructs a fixed 135-dimensional morphology representation for 2,300 garment sketches:

| Component | Dimensions |
|---|---:|
| Horizontal occupancy | 64 |
| Vertical occupancy | 64 |
| Global geometric descriptors | 7 |
| **Total** | **135** |

The coordinates are explicit and image-derived rather than learned from category labels. They retain direct spatial or geometric meaning and therefore support inspection at the coordinate, descriptor, neighborhood, and population levels.

The representation is not claimed to be unique, optimal, or universal. Its contribution is to provide a transparent quantitative coordinate system in which the morphology of the examined sketch population can be studied.

## 4. Contribution 2 — Population-level characterization

The morphology matrix is treated as more than a classifier input. The associated analyses examine its variance structure, local relationships, graph-based organization, density organization, and feature-level behavior across the sketch population.

These analyses support a constrained conclusion:

> The examined CLO-SKET population exhibits reproducible quantitative organization under the specified morphology representation.

They do not establish semantic garment components, universal morphology categories, a compositional grammar, or a mathematical manifold.

## 5. Contribution 3 — A separately constructed radial–angular description

The second representation contains 28 predefined radial–angular descriptors:

| Descriptor block | Dimensions |
|---|---:|
| F2 radial | 9 |
| α2 descriptors | 7 |
| Observed circular | 3 |
| Learned circular | 4 |
| Relational | 5 |
| **Total** | **28** |

This representation is computed through a geometrically distinct analysis branch and is evaluated in the same frozen row order as morphology.

“Separately” or “independently constructed” refers to the construction process. It does not imply statistical independence, information-theoretic independence, causal independence, or an independent data source.

The 28-dimensional configuration is the fixed descriptor set evaluated in this study; it is not presented as a universally optimal dimensionality.

## 6. Contribution 4 — Source-grouped cross-representation recovery

The historical recovery estimator—within-fold standardization followed by Ridge regression with α = 1.0—was reproduced exactly before the stricter validation was performed.

The estimator was then evaluated using source-garment-disjoint folds. Grouped out-of-fold results were:

| Radial–angular target | R² | Spearman ρ | Identity-bootstrap R² interval |
|---|---:|---:|---:|
| F2 peak magnitude | 0.302221 | 0.631055 | [0.266905, 0.333870] |
| F2 peak radius | 0.014269 | 0.324874 | [-0.042301, 0.066573] |
| R2 at the F2 peak | 0.190971 | 0.521587 | [0.121399, 0.253892] |
| Axial-disagreement magnitude at the F2 peak | 0.206346 | 0.442901 | [0.148195, 0.260074] |

These results show heterogeneous but reproducible representational overlap. Morphology captures substantial ordering or variance for some radial–angular quantities, while F2 peak radius is only weakly recovered in variance terms.

The fourth target is the scalar magnitude of disagreement between observed and learned axial orientations. It is not direct orientation prediction.

The recovery analysis establishes statistical predictability across unseen source identities. It does not establish causality, semantic interpretation, or complete equivalence between the representations.

## 7. Contribution 5 — Source-grouped downstream complementarity

The primary downstream comparison evaluates unseen source-garment identities using five exact category-balanced grouped folds. Each fold tests 46 identities—two from every category—and no identity appears in both training and test.

Pooled grouped performance was:

| Representation | Macro-F1 | Balanced accuracy |
|---|---:|---:|
| Morphology only | 0.306847 | 0.307826 |
| Morphology + radial–angular | 0.341445 | 0.342174 |
| **Paired increment** | **+0.034598** | **+0.034348** |

The combined representation improved both metrics in all five primary folds.

Identity-aware paired bootstrap intervals were:

| Metric increment | Observed | 95% interval |
|---|---:|---:|
| Macro-F1 | +0.034598 | [0.015783, 0.053962] |
| Balanced accuracy | +0.034348 | [0.015612, 0.054268] |

These intervals resample complete source identities within categories while keeping grouped out-of-fold predictions fixed. They quantify identity-sampling uncertainty conditional on the fitted fold-specific models; they are not model-refitting confidence intervals.

The resulting contribution is precise:

> Under the tested classifier and source-grouped evaluation, radial–angular geometry provides modest additional task-level utility beyond morphology.

## 8. Contribution 6 — Robustness to identity-to-fold allocation

The grouped comparison was repeated across ten exact-balanced partitions.

| Metric | Mean increment | SD across partitions | Range | Positive partitions |
|---|---:|---:|---:|---:|
| Macro-F1 | 0.042304 | 0.007004 | 0.033574–0.052882 | 10/10 |
| Balanced accuracy | 0.040609 | 0.007127 | 0.031304–0.051739 | 10/10 |

Forty-nine of fifty fold-level comparisons were positive for each metric.

This analysis demonstrates that the combined advantage is not confined to one allocation of garment identities to folds. It is descriptive split-robustness evidence, not an independent confidence interval and not evidence of robustness across classifier families.

## 9. Contribution 7 — Constraining the mechanism with an alignment control

To determine whether the combined advantage depends on the correct held-out sketch pairing, the analysis performed 2,000 within-category perturbations. Category membership and the radial–angular distribution within each held-out category were preserved, while morphology–radial–angular pairing was disrupted.

| Metric | Aligned minus permuted mean | Empirical p |
|---|---:|---:|
| Macro-F1 | +0.006153 | 0.141929 |
| Balanced accuracy | +0.006842 | 0.122939 |

The aligned predictions were slightly better on average, but the effects were not resolved under the specified category-preserving null.

This control prevents an overextended interpretation of complementarity. The grouped classifier establishes that the radial–angular branch is useful at the task level; it does not establish that the benefit arises from the exact radial–angular vector paired with each test sketch.

This negative boundary is itself scientifically valuable because it distinguishes:

- **supported:** population- or category-conditioned task-level complementarity;
- **not established:** exact sketch-pair-specific complementarity.

## 10. Supporting representation comparisons

Under the primary grouped evaluation, radial–angular geometry alone produced pooled Macro-F1 of 0.265323 and balanced accuracy of 0.276087. The integrated representation exceeded both single-branch models.

At the category level, integration improved Macro-F1 for 18 of 23 categories relative to morphology and for 19 of 23 categories relative to radial–angular geometry.

These comparisons support the use of both branches together under the examined task. They do not imply that either representation is universally superior across datasets or downstream objectives.

## 11. Supplementary direct axial-orientation analysis

Because axial orientation has 180-degree periodicity, direct orientation was modeled using cos(2α) and sin(2α), followed by reconstruction and axial angular-error evaluation.

Relative to a category-conditioned mean-direction baseline, morphology reduced mean error by 1.447897 degrees, with a 95% paired identity-bootstrap interval of [0.425764, 2.525118]. However, it worsened median error and performance within 10 degrees, while improving broader measures such as performance within 30 degrees and axial agreement.

The evidence for direct orientation recovery is therefore mixed. This analysis demonstrates appropriate treatment of an axial target but is not a primary contribution claim.

## 12. What is not claimed as novel

The study does not claim novelty for:

- occupancy profiles as generic descriptors;
- PCA or other standard transformations;
- radial or Fourier operations;
- Ridge regression;
- classification;
- cross-validation;
- permutation testing; or
- clustered bootstrap resampling.

These are established tools used within a controlled empirical framework.

## 13. Methodological novelty versus scientific contribution

### Methodological novelty

A fundamentally new machine-learning algorithm is not claimed.

### Scientific contribution

The scientific contribution is the explicit, identity-aware evaluation of two geometric descriptions of garment-sketch morphology, including their partial recoverability, downstream integration, split robustness, identity-sampling uncertainty, and alignment-specific claim boundary.

The strongest result is not that a particular descriptor exists. It is that a modest integrated advantage survives exact source-identity separation and repeated grouped evaluation.

## 14. Primary and secondary contributions

### Primary contribution

**Source-grouped task-level complementarity between explicit morphology and radial–angular geometry.**

This is the most reviewer-defensible result because it is supported by exact zero-overlap folds, paired performance comparisons, identity-aware uncertainty intervals, and repeated grouped partitions.

### Secondary contribution

**Explicit population-level characterization and partial cross-representation recovery.**

The morphology representation provides a transparent coordinate system for population analysis, and the grouped recovery results quantify which radial–angular properties are shared with it.

### Supporting negative boundary

**Exact held-out sketch alignment was not established as the mechanism.**

This qualification should accompany the complementarity claim wherever mechanistic interpretation is discussed.

## 15. Final claim boundary

### Supported

- explicit quantitative characterization of the examined sketch population;
- partial recovery of several radial–angular targets from morphology across unseen source identities;
- modest downstream utility of radial–angular geometry beyond morphology under the tested grouped task;
- robustness of the positive downstream increment across ten identity-to-fold allocations;
- identity-aware uncertainty conditional on fixed grouped out-of-fold predictions;
- better performance of the integrated representation than either branch alone under the primary task.

### Not established

- dependence of the downstream gain on exact sketch-level morphology–radial–angular pairing;
- universal superiority across models, tasks, or datasets;
- external generalization beyond CLO-SKET;
- information-theoretic independence;
- causal relationships;
- semantic garment-part recognition;
- semantic primitives or a morphology vocabulary;
- a compositional grammar;
- a mathematical manifold; or
- human-like visual understanding.

## 16. One-sentence contribution

> Using source-garment-disjoint evaluation, this study shows that an independently constructed radial–angular description provides modest and reproducible task-level utility beyond an explicit morphology representation of garment sketches, while category-preserving alignment controls constrain this result from being interpreted as proven sketch-pair-specific correspondence.

## 17. Reviewer-defense formulation

If a reviewer asks, “Is this simply feature engineering followed by classification?”, the response is:

> The individual geometric operators and predictive models are not presented as algorithmic novelty. The contribution is the controlled empirical evaluation of explicit garment-sketch morphology through two separately constructed geometric coordinate systems. Their overlap is quantified through source-grouped recovery, and their task-level complementarity is evaluated using exact identity-disjoint folds, paired identity-aware uncertainty, repeated grouped partitions, and a category-preserving alignment control. The combined representation yields a modest reproducible gain, while the alignment analysis explicitly limits the mechanism that can be claimed.

## 18. Manuscript-ready contribution statement

> This study contributes an explicit and reproducible framework for analyzing garment-sketch morphology through two geometric representations. A 135-dimensional morphology vector describes horizontal and vertical occupancy together with global shape properties, while a separately constructed 28-dimensional radial–angular vector captures complementary radial, circular, and relational structure. Under exact source-garment-disjoint evaluation, several radial–angular quantities were partially recoverable from morphology, demonstrating representational overlap, while integrating the two representations improved pooled Macro-F1 by 0.0346 and balanced accuracy by 0.0343 relative to morphology alone. The improvements were positive across all primary folds and all ten repeated grouped partitions. A category-preserving alignment control did not establish that the benefit depends on exact sketch-level pairing; accordingly, the evidence supports modest task-level complementarity rather than statistical independence or proven pair-specific correspondence. The contribution is therefore an empirical geometric characterization and validation framework, not a claim of semantic primitives or a new learning algorithm.
