# CLO-SKET — Scientific Contribution

## 1. Central Contribution

The central contribution of this study is an empirical characterization
of garment sketches as occupying a structured quantitative morphology
space that can be analyzed without imposing predefined semantic
categories.

The contribution is not the use of PCA itself, nor the introduction of
a particular handcrafted image descriptor.

Rather, the study establishes an evidence-based framework in which:

1. garment sketches are represented through explicit image-derived
   morphology measurements;
2. the resulting morphology representation exhibits reproducible
   quantitative organization;
3. an independently derived radial–angular geometric representation
   is reproducibly associated with that morphology;
4. the radial–angular representation provides complementary downstream
   information beyond the morphology representation under the tested
   discrimination task; and
5. this complementary utility survives a dimension-matched control and
   is not confined to a single radial–angular descriptor block.

---

# 2. What Is Novel

The novelty is therefore primarily at the level of the
**scientific characterization and validation framework**, rather than
the invention of a new individual mathematical operation.

The study asks a question that is distinct from conventional
task-oriented fashion image analysis:

> What quantitative geometric organization exists in garment sketches
> before semantic categories are imposed?

This separates the study from approaches whose primary objective is
classification, retrieval, recognition, generation, or semantic
annotation.

The resulting contribution is an empirical geometric description of
sketch morphology and a cross-representation validation of that
description.

---

# 3. Contribution 1 — Explicit Quantitative Morphology Representation

We construct a canonical 135-dimensional morphology representation
from 2300 garment sketches.

The representation contains:

- 64 horizontal occupancy coordinates;
- 64 vertical occupancy coordinates; and
- 7 global geometric descriptors.

The representation is intentionally explicit and image-derived.

It is not learned from semantic labels.

Its purpose is to provide a measurable coordinate system in which
quantitative morphology can be investigated independently of
predefined semantic categories.

The study does not claim that this representation is the unique,
optimal, or universal representation of garment morphology.

---

# 4. Contribution 2 — Empirical Characterization of Morphology Organization

The 135-dimensional representation is not treated merely as an input
feature matrix.

It is investigated as a geometric object.

The analysis evaluates:

- spectral organization;
- local neighborhood structure;
- graph-geodesic organization;
- transition structure;
- multiscale density organization; and
- permutation-based locality.

These analyses collectively test whether quantitative morphology
exhibits reproducible organization rather than behaving as an
unstructured collection of image measurements.

The resulting evidence supports quantitative morphology organization.

It does not establish discrete semantic morphology categories.

---

# 5. Contribution 3 — Independent Radial–Angular Geometric Description

A separate radial–angular representation is constructed independently
of the frozen 135-dimensional morphology representation.

The representation contains 28 dimensions distributed across five
descriptor blocks:

| Descriptor block | Dimensions |
|---|---:|
| F₂ radial | 9 |
| α₂ | 7 |
| observed circular | 3 |
| learned circular | 4 |
| relational | 5 |
| **Total** | **28** |

The radial–angular representation is not introduced as a replacement
for the morphology representation.

It provides a different geometric coordinate description of the same
sketch population.

The 28-dimensional representation is not claimed to be uniquely
optimal or universally sufficient.

---

# 6. Contribution 4 — Cross-Representation Correspondence

Row-level provenance was independently verified between the morphology
and radial–angular branches.

The two representations therefore refer to the same sketch for every
observation.

Feature-level associations demonstrate that multiple coordinates of
the morphology representation are statistically associated with
radial–angular measurements.

More importantly, cross-validated prediction shows that morphology
can recover independently measured radial–angular quantities at the
sketch level.

For the four tested radial–angular targets:

| Target | CV R² |
|---|---:|
| F₂ peak magnitude | 0.296 |
| F₂ peak radius | 0.059 |
| R₂ at F₂ peak | 0.217 |
| Axial angular error | 0.198 |

A row-permutation null further shows that the observed
morphology–radial-angular correspondence exceeds the correspondence
expected after destroying sketch-level alignment.

This establishes reproducible cross-representation correspondence.

It does not establish semantic interpretation or causality.

---

# 7. Contribution 5 — Complementary Downstream Information

The strongest evidence for the role of the radial–angular representation
comes from an independent downstream discrimination task.

The frozen 135-dimensional morphology representation is compared with
an augmented representation containing the 28-dimensional radial–
angular geometry.

Observed performance:

| Representation | Macro-F1 | Balanced Accuracy |
|---|---:|---:|
| Morphology only | 0.3413 | 0.3426 |
| Morphology + radial–angular | 0.4123 | 0.4157 |
| Improvement | +0.0710 | +0.0730 |

The observed improvement is evaluated using a row-permutation control
that preserves the radial–angular representation while destroying its
sketch-level correspondence with morphology.

The resulting evidence supports the interpretation that radial–
angular geometry provides reproducible complementary downstream
information under the tested 23-category discrimination task.

This is a task-level complementarity claim.

It is not a claim of information-theoretic independence.

---

# 8. Contribution 6 — Dimension-Matched Control

A potential alternative explanation is:

> The radial–angular representation improves performance simply
> because additional dimensions were added.

This explanation is explicitly tested using a dimension-matched
control.

The control preserves the dimensionality of the added representation
while destroying the true sketch-level correspondence.

The observed aligned representation produces substantially greater
downstream improvement than the corresponding row-permuted control.

Therefore the result cannot be adequately characterized as merely:

> "163 dimensions perform better than 135 dimensions."

Instead, the evidence supports the more specific conclusion that
the **correctly aligned radial–angular geometry** carries useful
information for the tested downstream task.

The control does not establish information-theoretic independence.

---

# 9. Contribution 7 — Descriptor-Level Ablation

The radial–angular representation is decomposed into its predefined
descriptor blocks.

The downstream gains relative to morphology alone are:

| Added representation | Δ Macro-F1 |
|---|---:|
| F₂ radial | +0.0331 |
| α₂ | +0.0150 |
| observed circular | +0.0172 |
| learned circular | +0.0254 |
| relational | +0.0208 |
| **full 28-D radial–angular** | **+0.0710** |

The complete radial–angular representation produces a larger gain than
any individual descriptor block.

This indicates that the observed downstream utility is not adequately
reduced to a single radial–angular component.

The ablation does not establish that every individual block is
independently statistically significant.

---

# 10. What Is NOT Claimed as Novel

The study does not claim novelty for:

- PCA as a mathematical technique;
- occupancy profiles as a generic image descriptor;
- radial statistics as mathematical operations;
- Fourier analysis as a mathematical operation;
- classification itself;
- permutation testing itself; or
- the existence of garment categories.

These are methodological components of the study.

The scientific contribution arises from their use in a controlled
framework to characterize quantitative morphology and test its
relationship with an independently derived geometric representation.

---

# 11. Distinction Between Methodological Novelty and Scientific Novelty

The study should not be presented as proposing a fundamentally new
machine-learning algorithm.

Its contribution is instead an empirical and analytical one.

The distinction is:

### Methodological novelty

Not claimed.

The individual mathematical operations used in the study are
established techniques.

### Scientific novelty

Claimed at the level of empirical characterization:

> garment sketches exhibit reproducible quantitative morphology
> organization that can be studied without predefined semantic
> categories, and an independently derived radial–angular geometric
> representation is reproducibly associated with that morphology and
> provides complementary downstream utility.

This distinction should be maintained throughout the manuscript.

---

# 12. Primary Contribution vs Secondary Contribution

## Primary contribution

**Quantitative characterization of garment-sketch morphology.**

The central result is that explicit image-derived morphology
measurements exhibit reproducible geometric organization.

## Secondary contribution

**Complementary radial–angular geometry.**

The radial–angular representation provides an independently derived
geometric description that is associated with the morphology
representation and provides additional downstream utility under the
tested task.

The secondary contribution should strengthen, rather than replace,
the primary morphology result.

---

# 13. Claim Boundary

The evidence supports:

- quantitative morphology organization;
- reproducible local and density-associated organization;
- sketch-level morphology ↔ radial-angular correspondence;
- cross-validated recovery of radial-angular measurements from
  morphology;
- downstream complementary utility of radial-angular geometry;
- dimension-matched evidence against a simple dimensional-expansion
  explanation; and
- distributed utility across multiple radial-angular descriptor
  blocks.

The evidence does NOT establish:

- semantic novelty;
- semantic garment-part recognition;
- universal morphology categories;
- semantic morphology primitives;
- a compositional morphology grammar;
- a mathematical manifold;
- causal relationships;
- information-theoretic independence; or
- human-like visual understanding.

---

# 14. One-Sentence Contribution

The study provides an empirical characterization of garment sketches
as occupying a structured quantitative morphology space and shows
that an independently derived radial–angular geometric representation
is reproducibly coupled to, and provides complementary downstream
information beyond, that morphology representation without semantic
supervision.

---

# 15. Reviewer-Defense Formulation

If a reviewer asks:

> "Is this simply feature engineering followed by PCA?"

The appropriate response is:

> No. The individual representation and dimensionality-reduction
> operations are not presented as algorithmic novelty. The scientific
> contribution is the empirical characterization of quantitative
> morphology organization and its independent geometric validation.
> The radial–angular branch provides a separate representation whose
> sketch-level correspondence, cross-validated recovery, downstream
> complementarity, dimension-matched control, and descriptor-level
> ablation are evaluated explicitly.

---

# 16. Contribution Statement for the Manuscript

A concise manuscript version is:

> **This study contributes an empirical framework for characterizing
> quantitative morphology in garment sketches without predefined
> semantic categories. Using an explicit 135-dimensional morphology
> representation, we identify reproducible geometric organization and
> subsequently evaluate an independently derived radial–angular
> representation. The two representations show reproducible
> sketch-level correspondence, while radial–angular geometry provides
> additional downstream utility beyond morphology under a controlled
> discrimination task. Dimension-matched and descriptor-level controls
> further constrain the interpretation of this complementarity. The
> contribution is therefore an empirical geometric characterization,
> rather than a claim of semantic morphology primitives or a new
> machine-learning algorithm.**