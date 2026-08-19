# CLO-SKET — Methods

## 1. Study Design

This study investigates the quantitative geometric organization of
garment sketches using explicit image-derived morphology measurements
and an independently derived radial–angular representation.

The analysis is representation-focused rather than semantic.

The study is organized into two principal computational branches:

1. a canonical 135-dimensional morphology representation; and
2. an independently derived 28-dimensional radial–angular
   representation.

The two branches are subsequently compared using association,
cross-validated recovery, permutation-based correspondence testing,
downstream complementarity testing, dimension-matched controls, and
descriptor-level ablation.

No semantic category labels are used to construct either geometric
representation.

---

# 2. Dataset

The study uses 2,300 garment sketches from the Clo-Sket dataset.

The same population is used throughout the morphology and
radial–angular branches.

Row-level provenance between the two branches was explicitly verified
before cross-branch analyses were performed.

The provenance audit established that the image-path ordering of the
morphology branch exactly matched the image-path ordering of the
radial–angular branch.

Therefore, for every observation i:

    X_morphology[i]

and

    X_radial-angular[i]

refer to the same sketch.

No cross-branch association analysis was performed before this
provenance condition was satisfied.

---

# 3. Canonical Image Representation

The morphology branch begins from canonicalized grayscale sketch
images.

The frozen morphology artifact records:

- grayscale conversion;
- intensity normalization by division by 255;
- foreground threshold `< 0.8`;
- canonical spatial size of 64 × 64 pixels.

The resulting canonical image representation is used to construct
explicit morphology measurements.

The raw canonical morphology matrix contains:

    2300 observations × 135 features.

The frozen matrix is stored as a float32 artifact.

Its SHA-256 fingerprint is recorded in the corresponding provenance
metadata to ensure that subsequent analyses use the same canonical
matrix.

---

# 4. Explicit 135-D Morphology Representation

The canonical morphology representation contains three feature blocks.

## 4.1 Horizontal Occupancy

For each of the 64 canonical spatial columns, foreground occupancy is
measured.

This produces:

    64 horizontal occupancy features.

The resulting matrix has shape:

    2300 × 64.

---

## 4.2 Vertical Occupancy

For each of the 64 canonical spatial rows, foreground occupancy is
measured.

This produces:

    64 vertical occupancy features.

The resulting matrix has shape:

    2300 × 64.

---

## 4.3 Global Geometric Descriptors

Seven global descriptors are included as the final morphology block.

This produces:

    7 global geometric features.

---

## 4.4 Complete Morphology Representation

The complete representation is therefore:

    64 horizontal
    +
    64 vertical
    +
    7 global
    =
    135 dimensions.

The complete matrix is:

    X_raw ∈ R^(2300 × 135)

This representation is frozen before downstream morphology
organization analyses.

No semantic labels are used in constructing X_raw.

---

# 5. Preservation of the Frozen Morphology Representation

The 135-dimensional morphology matrix used in the present study is
treated as a frozen canonical artifact.

The radial–angular analysis does not modify:

- the morphology measurements;
- the canonical image representation;
- the morphology feature definitions; or
- the original 135-dimensional matrix.

This separation ensures that the radial–angular branch constitutes a
representation-sensitivity analysis rather than a modification of the
primary morphology representation.

---

# 6. Standardization and PCA

For geometric analyses requiring standardized morphology coordinates,
feature standardization is performed prior to PCA.

The morphology representation is subsequently projected into principal
component coordinates.

PCA is used as a dimensionality-reduction and coordinate
representation procedure.

It is not interpreted as a semantic decomposition.

The principal components are therefore not treated as:

- garment-part primitives;
- semantic categories;
- universal morphology axes; or
- learned semantic concepts.

The primary variance-retention criterion used in the morphology
analysis retains approximately 95% of standardized morphology
variance, resulting in a 73-dimensional PCA representation.

The phrase "73-dimensional PCA representation" is used rather than
"73-dimensional intrinsic manifold" because PCA variance retention
does not by itself establish mathematical intrinsic dimensionality.

---

# 7. Morphology-Space Organization Analyses

The morphology representation is evaluated as a quantitative geometric
space.

The analysis includes:

- spectral structure;
- local neighborhood organization;
- graph-geodesic relationships;
- transition structure;
- multiscale density organization;
- permutation-based neighborhood tests; and
- feature-order permutation analyses.

These analyses are used to determine whether morphology measurements
exhibit reproducible organization rather than behaving as an
unstructured collection of coordinates.

Density-defined regions are treated as regions of quantitative
morphological density.

They are not interpreted as discrete semantic categories.

Within-region dispersion is explicitly retained in the interpretation.

---

# 8. Independent Radial–Angular Representation

A separate radial–angular branch is constructed independently of the
frozen 135-dimensional morphology representation.

The purpose of this branch is to provide a different geometric
description of the same sketch population.

The final compact radial–angular representation contains 28 dimensions.

It is composed of five predefined descriptor blocks:

| Descriptor block | Dimensions |
|---|---:|
| F₂ radial | 9 |
| α₂ | 7 |
| observed circular | 3 |
| learned circular | 4 |
| relational | 5 |
| **Total** | **28** |

The representation is:

    X_RA ∈ R^(2300 × 28)

The 28-dimensional representation is not claimed to be uniquely
optimal or universally sufficient.

---

# 9. Radial–Angular Measurements

The radial–angular branch includes measurements derived from radial and
angular organization of the sketch representation.

The branch includes:

- F₂ radial descriptors;
- angular descriptors;
- observed circular descriptors;
- learned circular descriptors; and
- relational descriptors.

The underlying radial–angular measurements include radial magnitude,
radial location, circular/angular organization, and relationships
between observed and learned geometric quantities.

The present study evaluates these measurements as a geometric
representation.

It does not interpret them as semantic garment-part labels.

---

# 10. Domain Consistency and Shell Matching

Radial analyses use a locked radial domain:

    3.50 → 27.50

with:

    25 circular shells.

The F₂ peak location is matched to the corresponding circular shell
within this locked domain.

The analysis verifies:

    maximum F₂ ↔ circular-shell mismatch = 0

for all 2,300 observations.

This ensures that the radial and circular measurements used in
cross-branch comparisons are defined on the same locked radial
domain.

---

# 11. Row-Level Provenance Verification

Before any morphology ↔ radial–angular association analysis, the two
branches undergo an explicit provenance audit.

The audit checks:

- population size;
- image-reference count;
- uniqueness of image references;
- morphology-side image-path ordering;
- radial–angular image-path ordering; and
- exact row-level path correspondence.

The final audit established:

    2300 morphology observations
    2300 radial–angular observations
    2300 unique image references
    exact row-order path match.

The resulting provenance flag is:

    row_level_provenance_verified = True

Cross-branch analyses are permitted only after this condition is
satisfied.

---

# 12. Feature-Wise Cross-Branch Association

The first cross-branch analysis evaluates statistical associations
between individual morphology coordinates and radial–angular targets.

The primary association statistic is Spearman correlation.

Spearman correlation is used because the relationships need not be
linear.

The following radial–angular targets are evaluated:

1. F₂ peak magnitude;
2. F₂ peak radius;
3. observed R₂ at the matched F₂ peak shell; and
4. axial angular recovery error.

Multiple comparisons across the 135 morphology coordinates are
controlled using the Benjamini–Hochberg false-discovery-rate procedure,
performed separately for each target.

These analyses establish statistical association only.

They do not establish:

- causality;
- redundancy;
- complementarity;
- semantic meaning; or
- information-theoretic independence.

---

# 13. Cross-Validated Morphology → Radial–Angular Recovery

The second analysis evaluates whether the frozen morphology
representation can recover independently measured radial–angular
quantities.

The predictors are exclusively the 135 morphology coordinates.

The targets are independently derived radial–angular measurements.

Five-fold cross-validation is used with:

    shuffle = True
    random_state = 42

Performance is evaluated strictly out-of-sample.

The primary metric is cross-validated R².

MAE and RMSE are also recorded.

Prediction Pearson and Spearman correlations are retained as secondary
descriptive measures.

The analysis therefore distinguishes:

    morphology-encoded radial-angular structure

from:

    residual radial-angular variation.

A nonzero prediction performance does not by itself establish
complementarity.

---

# 14. Row-Permutation Correspondence Null

To test whether morphology ↔ radial–angular correspondence depends on
the actual sketch-level alignment, a row-permutation null is used.

The morphology representation remains fixed.

The radial–angular targets are randomly permuted across observations.

Thus:

    X_morphology[i]

is paired with:

    Y_radial-angular[π(i)]

where π is a random permutation.

The permutation preserves the marginal target distribution while
destroying the true sketch-level correspondence.

The observed cross-validated performance is compared with the empirical
null distribution.

For the reported correspondence analysis:

    permutations = 100
    random seed = 2026

The empirical p-value is calculated from the permutation distribution.

Because 100 permutations were used, the smallest attainable nonzero
empirical p-value under the +1 correction is:

    1 / 101 = 0.0099.

This should be reported explicitly rather than implying greater
numerical precision than the permutation design permits.

---

# 15. Downstream Complementarity Analysis

The next analysis asks whether radial–angular geometry contributes
useful information beyond morphology in a downstream discrimination
task.

The baseline representation contains:

    135-D morphology.

The augmented representation contains:

    135-D morphology
    +
    28-D radial–angular geometry.

The downstream task uses the predefined 23-category discrimination
setting.

The primary evaluation metrics are:

- macro-F1;
- balanced accuracy.

The evaluation is performed using cross-validation with out-of-sample
predictions.

The key comparison is:

    Δ metric =
        metric(morphology + RA)
        -
        metric(morphology only)

A positive Δ indicates improved downstream performance under the
tested representation and task.

This is interpreted as task-level complementary utility.

It is not interpreted as:

- semantic novelty;
- causal information;
- information-theoretic independence; or
- human-like understanding.

---

# 16. Dimension-Matched Control

A major alternative explanation for the downstream improvement is that
adding 28 additional dimensions could improve performance regardless
of their geometric meaning.

A dimension-matched row-permutation control is therefore used.

The control retains:

- the same morphology representation;
- the same number of added radial–angular dimensions;
- the same radial–angular marginal distribution.

The true sketch-level correspondence is destroyed by row permutation.

The purpose is to distinguish:

    correctly aligned geometric augmentation

from:

    generic dimensional expansion.

If the correctly aligned representation produces greater downstream
utility than the dimension-matched permuted representation, the result
provides evidence that the improvement depends on the actual
cross-branch correspondence.

This does not establish information-theoretic independence.

---

# 17. Descriptor-Level Ablation

The 28-dimensional radial–angular representation is decomposed into its
five predefined descriptor blocks.

Each block is separately added to the frozen morphology representation.

The blocks are:

- F₂ radial;
- α₂;
- observed circular;
- learned circular;
- relational.

The full 28-dimensional radial–angular representation is also tested.

The purpose is to determine whether the downstream effect is dominated
by one descriptor block.

The observed results show positive mean downstream gains for each
individual block, while the complete 28-dimensional representation
produces the largest gain.

The ablation does not establish that every block is independently
statistically significant.

---

# 18. Statistical and Computational Controls

The analysis uses the following controls:

### Representation freeze

The canonical 135-D morphology matrix is not modified during
radial–angular analysis.

### Provenance control

Row-level image correspondence is explicitly verified.

### Cross-validation

Downstream predictive analyses use out-of-sample evaluation.

### Training-fold preprocessing

Where PCA is used for predictive target construction, PCA fitting is
performed using training-fold data only.

### Permutation control

Row permutations destroy sketch-level correspondence while preserving
marginal representation structure.

### Dimension-matched control

The number of added radial–angular dimensions is preserved while
correspondence is destroyed.

### Descriptor ablation

Individual radial–angular blocks are evaluated separately.

---

# 19. Category-Label Separation

Semantic category labels are not used to construct:

- the 135-D morphology representation;
- the PCA morphology representation;
- the radial–angular representation;
- the feature-wise association analysis;
- the morphology → radial–angular recovery analysis; or
- the cross-branch permutation correspondence analysis.

Category labels enter only in the downstream discrimination analysis.

This separation is essential to the interpretation of the morphology
organization as non-semantic.

---

# 20. Reproducibility and Frozen Artifacts

The canonical morphology matrix is preserved as a frozen artifact.

The provenance metadata records:

- dataset;
- number of observations;
- number of features;
- image processing;
- representation;
- downstream processing state;
- source;
- data type; and
- SHA-256 matrix fingerprint.

The final radial–angular analysis was additionally checkpointed after
completion of the experimental phase.

The final checkpoint contains the principal representations and result
objects required to reproduce the cross-branch evidence ledger.

---

# 21. Experimental Sequence

The complete analysis follows this sequence:

    Clo-Sket sketches
            ↓
    canonical grayscale images
            ↓
    64 × 64 representation
            ↓
    ┌──────────────────────────────┐
    │ 135-D morphology             │
    │ 64 horizontal                │
    │ 64 vertical                  │
    │ 7 global descriptors         │
    └──────────────────────────────┘
            ↓
    standardization / PCA
            ↓
    morphology-space organization
            ↓
    independently derived
    radial–angular representation
            ↓
    28-D RA representation
            ↓
    provenance verification
            ↓
    feature association
            ↓
    cross-validated recovery
            ↓
    permutation correspondence
            ↓
    downstream complementarity
            ↓
    dimension-matched control
            ↓
    descriptor ablation
            ↓
    final evidence synthesis

---

# 22. Methodological Claim Boundary

The methods establish a framework for measuring and comparing
quantitative geometric representations of garment sketches.

They do not define a semantic language model.

They do not infer semantic garment parts.

They do not establish a universal morphology ontology.

They do not establish a mathematical manifold.

They do not establish causal relationships.

They do not establish information-theoretic independence.

---

# 23. Reproducibility Principle

The methodological principle of this study is:

> Freeze the primary representation, derive the secondary geometric
> representation independently, verify sketch-level provenance, and
> evaluate association, recovery, complementarity, and controls
> separately.

This prevents the radial–angular analysis from silently becoming a
modification of the primary morphology representation.

---

# 24. Summary of the Analytical Design

The study deliberately separates four levels of evidence:

### Level 1 — Representation

Can quantitative morphology be measured explicitly?

### Level 2 — Organization

Does the morphology representation exhibit reproducible geometric
organization?

### Level 3 — Cross-representation correspondence

Does independently derived radial–angular geometry correspond to the
morphology representation at the sketch level?

### Level 4 — Complementarity

Does radial–angular geometry provide additional downstream utility
beyond morphology under a controlled task?

These levels should not be conflated.

A result at one level does not automatically establish a stronger claim
at the next level.