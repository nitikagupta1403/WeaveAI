# CLO-SKET — Final Reviewer-Risk Register

## 1. Purpose and evidentiary status

This document is an internal reviewer-risk register for the final CLO-SKET manuscript. It supersedes the pre-validation register and incorporates the completed Final Validation Shield.

The register distinguishes among:

- claims directly supported by source-identity-disjoint evaluation;
- descriptive or conditional evidence;
- unresolved questions; and
- claims that must not appear in the manuscript.

The central evidentiary distinction is between **task-level complementarity** and **exact sketch-level correspondence**. The former is supported under grouped evaluation; the latter was not established by the within-category alignment control.

## 2. Locked validation facts

The following facts define the final evidence base and should not be altered without rerunning the validated pipeline.

| Item | Locked result |
|---|---:|
| Sketches | 2,300 |
| Categories | 23 |
| Source-garment identities | 230 |
| Identities per category | 10 |
| Morphology representation | 135 dimensions |
| Radial–angular representation | 28 dimensions |
| Grouped folds | 5 exact category-balanced folds |
| Test identities per fold | 46; two per category |
| Source-identity overlap | 0 in every grouped fold |
| Morphology pooled Macro-F1 | 0.306847 |
| Combined pooled Macro-F1 | 0.341445 |
| Macro-F1 increment | +0.034598 |
| Morphology pooled balanced accuracy | 0.307826 |
| Combined pooled balanced accuracy | 0.342174 |
| Balanced-accuracy increment | +0.034348 |

The identity-aware bootstrap intervals for the paired combined-versus-morphology improvement were:

- Macro-F1: 95% interval [0.015783, 0.053962];
- balanced accuracy: 95% interval [0.015612, 0.054268].

Across ten exact-balanced grouped partitions, the mean increments were 0.042304 for Macro-F1 and 0.040609 for balanced accuracy. All ten partition-level effects were positive, and 49 of 50 individual fold effects were positive for each metric.

The within-category alignment control produced smaller aligned-versus-permuted advantages:

- Macro-F1: +0.006153, empirical p = 0.141929;
- balanced accuracy: +0.006842, empirical p = 0.122939.

These results do not establish that exact held-out morphology–radial–angular pairing is the mechanism responsible for the classification improvement.

## 3. Final central claim

The strongest defensible central claim is:

> Across source-identity-disjoint evaluation, an independently constructed radial–angular representation provided modest but reproducible task-level utility beyond explicit morphology for the examined 23-category CLO-SKET discrimination task.

The necessary qualification is:

> A within-category alignment control did not establish that this advantage depends specifically on exact sketch-level correspondence between the two representations.

## 4. Risk: source-identity leakage in the historical evaluation

### Reviewer objection

> Multiple sketches of the same source garment may occur in both training and test sets, inflating generalization performance.

### Assessment

This objection is valid for the original image-level StratifiedKFold analysis. Every historical test row had a source-garment identity represented in the corresponding training fold. That analysis evaluates unseen sketches of previously seen garment identities, not generalization to unseen garments.

### Evidence now available

The Final Validation Shield reconstructed 230 source-garment identities and created five exact category-balanced folds. Every fold tested two identities per category, no identity crossed training and test, and every row and identity was tested exactly once.

### Manuscript action

Use the grouped results as the primary downstream evidence. Historical image-level results may be retained only as a clearly labelled secondary comparison.

### Status

**Strongly addressed for the primary analysis.**

## 5. Risk: the improvement is caused merely by adding features

### Reviewer objection

> A 163-dimensional combined input may outperform a 135-dimensional input simply because it contains more predictors.

### Assessment

Dimension-matched and descriptor-level controls weaken this explanation. However, the interpretation must distinguish a feature-count control from a sketch-alignment test.

### Supported conclusion

The combined representation provides utility beyond morphology under the specified control framework and classifier.

### Prohibited conclusion

The analyses do not establish information-theoretic independence or prove that dimensionality can never contribute under another model.

### Status

**Addressed under the tested controls; not universal.**

## 6. Risk: exact cross-branch correspondence is overstated

### Reviewer objection

> Does the classifier benefit from the correct radial–angular vector for each individual held-out sketch, or merely from category-conditioned radial–angular structure?

### Assessment

This is the most important remaining mechanistic uncertainty. The 2,000 within-category perturbations preserved category membership while disrupting held-out morphology–radial–angular pairing. The aligned-minus-permuted effects were positive but not statistically resolved under this null.

### Required wording

Use:

> The representations were complementary at the task level under grouped evaluation.

Do not use:

> Exact sketch-level correspondence was demonstrated.

### Status

**Unresolved; claim narrowed.**

## 7. Risk: radial–angular information is redundant with morphology

### Reviewer objection

> If morphology predicts radial–angular quantities, the second representation may be only a re-expression of the first.

### Evidence

Grouped morphology-to-radial–angular recovery showed heterogeneous predictability:

| Target | Grouped R² | Grouped Spearman rho | Interpretation |
|---|---:|---:|---|
| F2 peak magnitude | 0.302221 | 0.631055 | Substantial recoverable ordering |
| F2 peak radius | 0.014269 | 0.324874 | Weak variance recovery; positive rank association |
| R2 at F2 peak | 0.190971 | 0.521587 | Partial recovery |
| Axial-disagreement magnitude | 0.206346 | 0.442901 | Partial recovery |

The combined classifier nevertheless exceeded morphology alone under grouped evaluation.

### Correct interpretation

The branches contain partially overlapping, task-complementary structure. This does not demonstrate statistically independent information.

### Status

**Addressed at the task level.**

## 8. Risk: handcrafted representations are presented as algorithmic novelty

### Reviewer objection

> The 135-dimensional morphology vector and 28-dimensional radial–angular vector use established geometric operations.

### Assessment

The objection is valid if the paper claims a fundamentally new descriptor. It should not.

### Manuscript position

The contribution is empirical and analytical: explicit geometric representations are used to test population organization, cross-representation recovery, and task-level complementarity under controlled validation.

### Status

**Managed through positioning.**

## 9. Risk: the 28-dimensional representation was chosen post hoc

### Reviewer objection

> Were descriptor blocks or dimensionality selected after observing downstream performance?

### Assessment

The 28 dimensions are a predefined compact descriptor set, not an optimized or universal dimensionality. Any exploratory influence on descriptor construction must be reported honestly; the manuscript must not imply preregistration.

### Required wording

> The 28-dimensional vector is the fixed descriptor configuration evaluated in this study.

### Status

**Partially resolved; provenance must remain explicit.**

## 10. Risk: labels create circularity

### Reviewer objection

> The same 23 categories may have been used to construct and evaluate the representation.

### Assessment

Category labels were not used to construct the morphology or radial–angular coordinates. They were used for supervised downstream evaluation and for category-balanced splitting and resampling.

The label-free construction claim and the supervised discrimination claim must remain separate.

### Status

**Managed, provided the manuscript preserves this distinction.**

## 11. Risk: grouped stratification itself leaks category information

### Reviewer objection

> Category-balanced grouped folds use labels during splitting.

### Response

Using labels to preserve class balance in cross-validation is not feature leakage. Labels are not supplied as predictors. The split construction ensures that every fold contains all categories while enforcing zero source-identity overlap.

### Status

**Not a leakage mechanism; explain clearly.**

## 12. Risk: uncertainty intervals are mischaracterized

### Reviewer objection

> Do the bootstrap intervals include model-fitting and fold-allocation uncertainty?

### Assessment

No. The 5,000-replicate identity-aware bootstrap resampled complete source identities within category while holding grouped out-of-fold predictions fixed.

### Correct interpretation

The intervals quantify sampling uncertainty across garment identities conditional on the fitted fold-specific models. Repeated grouped cross-validation separately describes sensitivity to identity-to-fold allocation.

### Prohibited interpretation

The bootstrap intervals are not model-refitting confidence intervals and the fractions at or below zero are not independent confirmatory p-values.

### Status

**Managed through explicit scope.**

## 13. Risk: permutation analyses are conflated

### Assessment

The manuscript contains different controls answering different questions. Their replicate counts and null hypotheses must not be pooled rhetorically.

| Analysis | Replicates | Question |
|---|---:|---|
| Historical permutation/control analysis | As reported in the originating experiment | Does the observed statistic exceed its specified historical null? |
| Within-category alignment perturbation | 2,000 | Does correct held-out sketch pairing improve fixed-model performance beyond category-preserving misalignment? |
| Identity-aware bootstrap | 5,000 | How uncertain is the observed effect across resampled source identities, conditional on fixed OOF predictions? |

### Status

**Requires precise reporting; no blanket “permutation test” statement.**

## 14. Risk: recovery analysis is interpreted causally

### Reviewer objection

> Predicting radial–angular variables from morphology proves that morphology generates them.

### Assessment

Cross-validated prediction demonstrates statistical recoverability, not causation or mechanistic derivation.

The historical Ridge/KFold estimator was reproduced exactly and then evaluated using source-grouped folds. This strengthens validity but does not convert association into causality.

### Status

**Managed through claim boundaries.**

## 15. Risk: axial variables are treated as ordinary linear outcomes

### Reviewer objection

> Orientation is axial and should respect its 180-degree periodicity.

### Assessment

The primary “axial error” recovery target is the scalar magnitude of disagreement between observed and learned orientations. It is not direct prediction of orientation and may be modeled as a scalar response.

A supplementary direct-orientation analysis predicted cos(2α) and sin(2α), reconstructed the axial angle, and evaluated axial angular error.

### Result boundary

The direct-orientation findings were mixed: morphology reduced mean angular error and improved broad agreement measures, but worsened median error and the fraction within 10 degrees relative to the category-conditioned mean-direction baseline.

### Status

**Methodological objection addressed; empirical result remains mixed and supplementary.**

## 16. Risk: the baseline for direct orientation is too weak

### Reviewer objection

> A category-conditioned mean direction may not represent the strongest directional baseline.

### Assessment

Valid. The paired comparison answers whether morphology improves upon this specified baseline, not whether it is optimal among all circular models.

### Manuscript action

Keep the analysis supplementary and describe the comparator exactly. Do not elevate it into the central claim.

### Status

**Open limitation.**

## 17. Risk: classifier-family dependence

### Reviewer objection

> Complementarity may be specific to the tested classifier and preprocessing pipeline.

### Assessment

The repeated grouped partitions demonstrate split robustness, not model-family robustness.

### Required wording

> Under the tested downstream classifier and evaluation design.

### Status

**Unresolved limitation.**

## 18. Risk: one dataset and no external replication

### Reviewer objection

> Results from CLO-SKET may not generalize to other sketch sources, drawing protocols, or populations.

### Assessment

Valid. The Validation Shield establishes stronger internal validity within CLO-SKET; it is not an external dataset replication.

### Required wording

> The conclusions concern the examined CLO-SKET population and require external replication.

### Status

**Unresolved limitation.**

## 19. Risk: preprocessing and resolution sensitivity

### Reviewer objection

> Occupancy and radial–angular descriptors may depend on binarization, centering, cropping, thresholding, or spatial resolution.

### Assessment

The frozen artifact and exact SHA reproduction establish computational reproducibility for the chosen pipeline, not robustness to alternative preprocessing choices.

### Status

**Unresolved limitation.**

## 20. Risk: dataset composition is mistaken for universal morphology

### Reviewer objection

> Observed organization may be induced by the 23 selected categories, garment frequencies, or acquisition protocol.

### Response

The analyses characterize the examined population. Category-balanced grouping prevents class imbalance across folds but does not establish invariance to a different category system or sampling frame.

### Status

**Unresolved beyond this dataset; constrain generalization.**

## 21. Risk: PCA is treated as the contribution or intrinsic dimension

### Assessment

PCA is a standard analytical transformation, not the central contribution. A variance-retention dimension is not an estimate of mathematical intrinsic dimensionality.

### Manuscript rule

Report the number of retained coordinates and variance criterion descriptively. Do not call it a garment-morphology manifold or intrinsic dimension.

### Status

**Managed through terminology.**

## 22. Risk: statistical significance is confused with importance

### Assessment

With 2,300 observations, modest associations can yield small p-values. Effect sizes, rank correlations, predictive metrics, paired increments, and uncertainty intervals must carry the interpretation.

The grouped downstream gain is modest in absolute magnitude even though it is reproducible across folds and partitions.

### Status

**Managed through quantitative reporting.**

## 23. Risk: semantic, primitive, grammar, or manifold claims

The present evidence does not establish:

- semantic garment-part recognition;
- semantic novelty;
- a universal morphology vocabulary;
- geometric primitives with validated compositional meaning;
- a morphology grammar;
- a mathematical manifold;
- human-like sketch understanding.

These terms must not be used as established findings.

### Status

**Explicitly excluded.**

## 24. Risk: “independent” is used ambiguously

The radial–angular representation is **independently constructed** in the sense that it is computed through a distinct geometric branch. This does not imply statistical independence, information-theoretic independence, causal independence, or an independent data source.

### Preferred phrase

> Independently constructed geometric representation.

### Status

**Managed through terminology.**

## 25. Risk: reproducibility is overstated

### Evidence

The final notebook records software versions, hashes frozen inputs and outputs, reconstructs the 135-dimensional morphology matrix exactly, reproduces the historical recovery estimator, freezes grouped splits, and archives final tables and predictions.

### Remaining requirement

Publication-quality reproducibility still requires a clean executable repository, environment specification, documented data access, and a mapping from manuscript tables to analysis outputs.

### Status

**Strong computational provenance; repository packaging still required.**

## 26. Consolidated reviewer-risk matrix

| Concern | Final evidence | Status |
|---|---|---|
| Source-identity leakage | Exact zero-overlap grouped folds | Strongly addressed for primary results |
| Added dimensions | Dimension-matched/descriptor controls | Addressed under tested controls |
| Exact sketch pairing | 2,000 category-preserving perturbations; p > 0.12 | Not established |
| RA redundancy | Partial grouped recovery plus downstream gain | Addressed at task level |
| Split dependence | 10 grouped partitions; 10/10 positive | Strongly addressed descriptively |
| Identity-sampling uncertainty | 5,000 clustered paired bootstraps | Addressed conditionally |
| Model-family dependence | One specified downstream family | Unresolved |
| External generalization | One dataset | Unresolved |
| Preprocessing sensitivity | Frozen exact artifact only | Unresolved |
| Direct orientation recovery | Proper axial model; mixed effects | Supplementary only |
| Semantic meaning | No semantic validation | Explicitly excluded |
| Manifold/grammar/primitives | Not tested | Explicitly excluded |
| Computational provenance | Frozen hashes, splits, predictions, archive | Strongly addressed |

## 27. Highest-value future experiments

If further experiments become necessary, priorities are:

1. external replication on a genuinely independent sketch dataset;
2. preprocessing and spatial-resolution sensitivity;
3. model-family robustness under the same source-grouped folds;
4. a stronger refitting-based alignment or conditional-null analysis, if exact pairing becomes a desired claim;
5. expert semantic validation only if the manuscript later advances semantic interpretations.

Additional experiments should be linked to a specific unresolved claim rather than added for volume.

## 28. Claims approved for the manuscript

The evidence supports the following statements:

1. Explicit morphology and radial–angular descriptors provide quantitative descriptions of the examined CLO-SKET population.
2. Under exact source-identity-disjoint evaluation, their combination modestly improves 23-category discrimination over morphology alone.
3. The positive increment is reproducible across the five primary folds and ten exact-balanced grouped partitions.
4. Several radial–angular targets are partially recoverable from morphology across unseen source identities, indicating representational overlap.
5. The combined task-level improvement and incomplete recovery are consistent with partial overlap and task-level complementarity.

## 29. Claims prohibited or requiring explicit qualification

Do not claim that:

- exact sketch-level alignment caused the downstream improvement;
- the representations contain statistically independent information;
- the results generalize beyond CLO-SKET;
- the classifier improvement is universal across models or tasks;
- the bootstrap intervals include model-refitting uncertainty;
- scalar axial-disagreement recovery is direct orientation prediction;
- the representation discovers semantic parts, primitives, grammar, or a manifold.

## 30. Internal decision

The evidence is sufficient for a focused representation-analysis paper whose primary empirical result is **source-grouped task-level complementarity**.

The manuscript should prioritize:

1. exact definition of both representations;
2. source-identity-disjoint validation as the primary evaluation;
3. separation of overlap, complementarity, and exact alignment;
4. effect sizes and identity-aware uncertainty;
5. explicit limitations on external, mechanistic, semantic, and model-family generalization.

The older statement that the study demonstrates “reproducible sketch-level correspondence” is retired. The validated replacement is “modest and reproducible task-level complementarity under source-grouped evaluation.”
