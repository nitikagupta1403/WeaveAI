# CLO-SKET — Literature Positioning

## 1. Purpose of This Document

This document defines how the CLO-SKET study is positioned relative to
existing literature.

The purpose is not to claim that no previous work has used similar
features or mathematical tools.

Instead, the objective is to distinguish:

1. established methodological components;
2. existing research questions;
3. closely related computational representations;
4. the specific gap addressed by this study; and
5. claims for which novelty remains provisional until a more exhaustive
   literature search is completed.

The manuscript should avoid absolute statements such as:

> "No previous work has studied this."

unless such a claim is supported by a sufficiently comprehensive
literature review.

---

# 2. Broad Fashion Computer-Vision Landscape

Fashion computer vision is a mature and broad research area.

A major survey of more than 200 fashion-related studies organized the
field into four broad areas:

- fashion detection;
- fashion analysis;
- fashion synthesis; and
- fashion recommendation.

Fashion detection includes tasks such as landmark detection, fashion
parsing, and item retrieval.

Fashion analysis includes attribute recognition, style learning, and
popularity prediction.

Fashion synthesis includes style transfer, pose transformation, and
physical simulation.

Fashion recommendation includes compatibility, outfit matching, and
related recommendation tasks.

This literature establishes that computational analysis of fashion
imagery is well developed.

However, these task-oriented formulations generally evaluate
representations according to downstream objectives rather than
treating quantitative garment morphology itself as the primary object
of investigation.

---

# 3. Position of the Present Study

The present study occupies a narrower research space:

> quantitative morphology of garment sketches independent of
> predefined semantic categories.

The distinction is important.

The study does not primarily ask:

- Can a sketch be classified?
- Can a sketch retrieve a photograph?
- Can a garment be generated from a sketch?
- Can garment parts be semantically parsed?
- Can a sketch be translated into text?
- Can a sketch be converted into a realistic garment image?

Instead, it asks:

> What measurable quantitative geometric organization exists within
> garment sketches before semantic categories are imposed?

This is therefore a representation-analysis question rather than a
conventional task-performance question.

---

# 4. Fashion Sketch Research

Sketch-based computer vision has an extensive literature involving
recognition, retrieval, cross-domain matching, and related tasks.

General sketch-recognition literature similarly emphasizes sketch
classification, sketch-based image retrieval, fine-grained retrieval,
and related recognition problems.

The present study differs in its primary object of analysis.

Rather than treating the sketch as a query or classifiable object, we
treat the sketch as an observation from which quantitative morphology
can be measured and its geometric organization investigated.

---

# 5. Clo-Sket and Its Original Role

Clo-Sket contains 2300 clothing sketches generated from six broad
clothing categories and 23 subcategories.

The dataset was designed for applications including:

- cross-domain photo/sketch matching;
- image retrieval;
- classification; and
- machine-learning/deep-learning evaluation.

The present study uses the same sketch population for a different
scientific purpose.

The sketches are treated as a population of morphological observations
rather than primarily as classification or retrieval examples.

This distinction should be stated explicitly.

The study therefore does not claim novelty for creating the Clo-Sket
dataset.

The contribution is the new analytical use of the dataset to
characterize quantitative morphology.

---

# 6. Explicit Image-Derived Morphology

## Existing methodological background

Explicit shape and image descriptors are well established throughout
computer vision.

Occupancy profiles, projections, geometric descriptors, Fourier
representations, moments, contour descriptors, and related shape
measurements are established methodological tools.

Therefore:

> the use of horizontal occupancy, vertical occupancy, and global
> geometric descriptors is not itself claimed as algorithmic novelty.

## Present contribution

The novelty question is instead whether these explicit measurements
can serve as a quantitative coordinate system for investigating the
organization of garment-sketch morphology independently of semantic
labels.

The study therefore treats the representation as an analytical
morphology space rather than merely as an input feature vector for a
classifier.

---

# 7. PCA and Dimensionality Reduction

PCA is an established dimensionality-reduction method.

The present study does not claim novelty for PCA.

PCA is used to:

- reduce the dimensionality of the standardized morphology
  representation;
- characterize variance structure; and
- provide a tractable coordinate system for subsequent geometric
  analyses.

Importantly:

> PCA is a methodological component, not the scientific hypothesis.

The study therefore should not state:

> "We propose PCA-based fashion morphology."

Instead:

> "PCA was used to obtain a variance-preserving coordinate
> representation for subsequent analysis of morphology organization."

---

# 8. Quantitative Morphology as an Object of Analysis

This is the central literature gap being investigated.

The relevant distinction is between:

### Task-oriented representation

A representation is constructed because it improves:

- classification;
- retrieval;
- recognition;
- generation;
- parsing; or
- another downstream task.

and:

### Morphology-oriented analysis

The representation itself becomes the object of study.

The present work belongs primarily to the second category.

The study asks whether the population of garment sketches exhibits
reproducible quantitative geometric organization independent of
predefined semantic categories.

This distinction should form a major part of the Introduction.

---

# 9. Semantic Representations vs Quantitative Morphology

Modern fashion datasets increasingly incorporate semantic,
multimodal, or textual annotations.

These representations are useful for:

- garment description;
- semantic retrieval;
- multimodal learning;
- generation;
- design assistance; and
- attribute recognition.

The present work intentionally operates at a different layer.

It does not attempt to infer semantic garment concepts from the
morphology representation.

Instead, it establishes a quantitative geometric layer that can
potentially serve as a substrate for later semantic investigations.

This distinction should be preserved throughout the manuscript.

---

# 10. Radial–Angular Representation

## Literature position

Radial and angular representations are established mathematical
descriptions of spatial structure.

Likewise, Fourier and frequency-domain representations are established
tools in image and shape analysis.

Therefore the present study does not claim novelty for:

- polar coordinates;
- radial sampling;
- angular sampling;
- Fourier transforms;
- radial spectra; or
- circular statistics as mathematical operations.

## What is being tested

The scientific question is whether an independently derived
radial–angular description provides a useful geometric representation
of garment sketches that is:

1. reproducibly associated with the explicit morphology
   representation;
2. recoverable from morphology at the sketch level; and
3. complementary to morphology in a downstream task.

The novelty is therefore empirical and analytical rather than
mathematical.

---

# 11. Relationship Between the Two Representations

The two representations are deliberately treated as distinct
coordinate descriptions.

### Morphology representation

The 135-D representation describes:

- horizontal occupancy;
- vertical occupancy; and
- global geometric descriptors.

It is fundamentally a canonical Cartesian/spatial occupancy
description.

### Radial–angular representation

The 28-D representation describes geometric organization using
radial, angular, circular, and relational quantities.

The study asks whether these coordinate systems:

> overlap in the information they encode while also exposing
> complementary structure.

This is tested rather than assumed.

---

# 12. Cross-Representation Correspondence

The study adds a specific validation step that is important for the
literature positioning.

The radial–angular representation is not simply appended to morphology
and evaluated once.

Instead, the study evaluates:

1. feature-wise association;
2. cross-validated morphology-to-radial-angular recovery;
3. row-permutation correspondence;
4. downstream complementarity;
5. dimension-matched control; and
6. descriptor-level ablation.

This creates an evidence chain from association to functional utility.

The study therefore avoids equating statistical correlation with
complementarity.

---

# 13. Complementarity vs Redundancy

A central literature-positioning distinction is:

> association is not the same as complementarity.

If morphology predicts radial–angular measurements, the two
representations may contain shared information.

That does not establish that radial–angular geometry contributes
something additional.

Conversely, if radial–angular descriptors improve a downstream task,
the improvement could potentially be caused simply by adding more
dimensions.

The present study therefore separates:

### Association

Cells 3–4.

### Sketch-level correspondence

Cell 6.

### Downstream complementarity

Cells 8–9.

### Dimensionality control

Cell 10.

### Descriptor ablation

Cell 11.

This layered structure is a methodological strength of the study.

---

# 14. Dimension-Matched Control

The most direct alternative explanation for the downstream improvement
is:

> additional features improve classification regardless of what they
> represent.

The dimension-matched control addresses this possibility by preserving
the dimensionality of the added representation while destroying its
true sketch-level correspondence.

Therefore the relevant comparison is not simply:

    135 dimensions
        vs
    163 dimensions

but:

    135-D morphology
        +
    correctly aligned 28-D radial-angular geometry

versus:

    135-D morphology
        +
    dimension-matched but misaligned radial-angular geometry.

This provides stronger evidence that the observed gain depends on the
geometric correspondence rather than dimensionality alone.

---

# 15. Descriptor Ablation

A second alternative explanation is:

> one particular radial-angular descriptor is responsible for the
> entire improvement.

The descriptor-level ablation addresses this possibility.

The full 28-D representation produces a larger downstream improvement
than any individual descriptor block.

Therefore the observed utility is not adequately reduced to a single
radial-angular component.

However, the ablation does not establish that every block is
independently significant.

---

# 16. What We Can Safely Claim About the Literature Gap

The safest current formulation is:

> Existing computational fashion and sketch research has extensively
> addressed recognition, retrieval, matching, semantic analysis,
> generation, and related downstream tasks. In contrast, the present
> study investigates quantitative morphology of garment sketches as an
> object of analysis independent of predefined semantic categories,
> and evaluates its relationship to an independently derived
> radial–angular geometric representation.

This is preferable to:

> "No previous work has studied fashion-sketch morphology."

The latter is an absolute negative claim and requires a much more
exhaustive literature search.

---

# 17. Provisional Novelty Matrix

| Research area | Established in literature? | Present study | Novelty status |
|---|---|---|---|
| Fashion image recognition | Yes | Not primary objective | Not claimed |
| Fashion retrieval | Yes | Not primary objective | Not claimed |
| Fashion parsing | Yes | Not primary objective | Not claimed |
| Fashion generation | Yes | Not primary objective | Not claimed |
| Sketch recognition | Yes | Used only as downstream context | Not claimed |
| Explicit image descriptors | Yes | Used for morphology representation | Not algorithmically novel |
| PCA | Yes | Used for dimensional reduction | Not novel |
| Radial/polar geometry | Yes | Used as independent representation | Not mathematically novel |
| Quantitative morphology organization of garment sketches | Less directly represented in the task literature identified so far | Primary objective | **Candidate contribution** |
| Cross-branch morphology ↔ radial-angular correspondence | No direct precedent established yet | Explicitly tested | **Candidate contribution** |
| Downstream complementarity between morphology and RA | No direct precedent established yet | Explicitly tested | **Candidate contribution** |
| Dimension-matched validation of that complementarity | No direct precedent established yet | Explicitly tested | **Candidate methodological contribution** |

The final three rows must remain labelled **candidate contributions**
until the dedicated systematic literature search is completed.

---

# 18. Literature Search Requirement Before Submission

Before making a definitive novelty claim, the literature review should
specifically search for studies involving combinations of:

### Fashion sketch morphology

- garment sketch shape representation;
- garment sketch morphology;
- fashion sketch shape analysis;
- fashion illustration shape analysis;
- quantitative fashion sketch descriptors.

### Explicit geometric representations

- fashion sketch occupancy profiles;
- garment silhouette descriptors;
- garment shape descriptors;
- garment contour representations;
- fashion sketch Fourier descriptors;
- fashion sketch radial descriptors;
- garment polar representations.

### Unsupervised morphology organization

- unsupervised garment shape spaces;
- garment morphology spaces;
- fashion shape manifolds;
- garment silhouette spaces;
- sketch morphology clustering;
- quantitative garment shape variation.

### Cross-representation geometry

- fashion sketch multi-representation;
- garment shape complementary representations;
- polar/cartesian garment representation;
- radial-angular fashion shape;
- complementary shape descriptors in fashion sketches.

The purpose of this search is not to find papers that use the same
mathematics.

The purpose is to determine whether the same **scientific question**
has already been answered.

---

# 19. Important Positioning Rule

Similarity of mathematical tools does not automatically invalidate
the contribution.

For example:

> Another paper using PCA does not invalidate this work.

Likewise:

> Another paper using Fourier descriptors does not invalidate this
> work.

The relevant question is whether prior work has already established
the same empirical claim:

> garment sketches exhibit reproducible quantitative morphology
> organization that can be characterized without semantic supervision
> and independently validated through complementary radial–angular
> geometry.

This should be the standard used when assessing novelty.

---

# 20. Current Literature-Based Position

Based on the literature reviewed so far:

### Established

- computational fashion vision is extensive;
- sketch recognition and retrieval are established;
- explicit image/shape descriptors are established;
- PCA and geometric transformations are established;
- radial/Fourier representations are established.

### Less directly addressed by the literature reviewed so far

- treating garment sketches themselves as a quantitative morphology
  population;
- characterizing their geometric organization independently of
  semantic labels;
- testing an independently derived radial–angular representation
  against that morphology space;
- evaluating representation complementarity rather than only
  downstream task accuracy.

These points are therefore the current candidate research gap.

They should be verified through a targeted systematic search before
being stated as definitive novelty claims.

---

# 21. Recommended Introduction Positioning

The Introduction should progress approximately as follows:

### Paragraph 1

Garment sketches are an important design representation.

### Paragraph 2

Computational fashion research has predominantly emphasized
recognition, retrieval, parsing, synthesis, recommendation, and
semantic/multimodal tasks.

### Paragraph 3

These approaches establish what can be predicted from fashion images
and sketches, but they do not necessarily characterize the quantitative
morphological organization of the sketch population itself.

### Paragraph 4

We therefore ask whether garment sketches occupy a structured
quantitative morphology space that can be characterized without
predefined semantic categories.

### Paragraph 5

We introduce an explicit morphology representation and evaluate its
geometric organization.

### Paragraph 6

We independently construct a radial–angular representation and test
whether it is associated with, recoverable from, and complementary to
the morphology representation.

### Paragraph 7

We state the contribution and explicitly limit the semantic claims.

---

# 22. Final Literature Positioning Statement

The paper should be positioned neither as:

> a new generic image descriptor,

nor as:

> a new fashion classifier,

nor as:

> a semantic understanding system.

It should be positioned as:

> **an empirical study of quantitative morphology organization in
> garment sketches, together with an independent geometric
> radial–angular validation and complementarity analysis.**

The novelty claim is therefore primarily about the **scientific object,
experimental framing, and evidence chain**, rather than the novelty of
individual mathematical operations.