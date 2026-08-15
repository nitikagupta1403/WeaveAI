# 1. Introduction

A garment sketch is a compact visual representation of design. Within a relatively small number of marks, a sketch can express differences in proportion, spatial distribution, silhouette, symmetry, occupancy, and other measurable properties of form. These properties are visible in the sketch before any semantic category is assigned to it. A garment sketch can therefore be viewed not only as an image to be recognized, but also as a morphological object whose internal quantitative organization can be investigated directly.

Fashion sketches have long been used as computational interfaces for communicating and interpreting garment shape. Earlier sketch-based garment systems used drawn silhouettes and curves to infer garment geometry or construct three-dimensional garments, with subsequent work explicitly incorporating contextual factors that influence garment shape. More recent fashion-sketch research has increasingly addressed semantic representation, fine-grained visual-language associations, sketch editing, and sketch-to-image generation. These directions demonstrate that substantial information can be extracted from fashion sketches, but they also motivate a more fundamental question that precedes semantic interpretation:

> **What quantitative organization is already present in the morphology of the sketches themselves?**

This distinction is important. Recognition and semantic modeling ask what a sketch represents; generation asks what can be produced from it; geometric interpretation asks how its depicted garment shape can be reconstructed. The present study instead asks whether the morphology underlying such interpretations exhibits a **reproducible quantitative organization before semantic categories are imposed**.

This perspective motivates a fundamental question:

> **Does a collection of garment sketches exhibit reproducible quantitative morphology organization that can be discovered from explicit morphology measurements without using category labels, replication labels, target sketches, or supervised semantic representations?**

The question is deliberately posed at the level of morphology rather than semantics. If semantic concepts are introduced before the organization of morphology has been established, it becomes difficult to determine whether the observed structure originates from the sketches themselves or from the categories imposed during analysis. We therefore begin with a geometry-first formulation in which morphology is measured explicitly and its organization is examined without semantic supervision.

---

## 1.1 Scientific Gap and Hypothesis

### Scientific Gap

Prior computational work on fashion and sketch understanding has established multiple levels of structured representation, including semantic categories and attributes, geometric and shape descriptors, stroke- and point-based representations, graph and relational structures, and primitive- or part-based abstractions. These approaches demonstrate that fashion sketches can be treated as structured visual objects rather than merely as undifferentiated images.

A related line of work has also explored geometry-derived structural representations in which recurring visual units are identified from sketch geometry rather than being defined entirely through predefined semantic parts. Such work motivates the distinction between structural discovery and semantic interpretation: a geometric unit may be reproducible and structurally meaningful without yet possessing an independently validated human semantic label.

This distinction motivates the present study, but at a level preceding primitive discovery.

Rather than beginning by defining discrete structural units, we first ask whether the morphology of complete garment sketches contains a **reproducible quantitative organization** from which such higher-level interpretations could eventually be developed.

The scientific gap addressed here is therefore:

> **Can the quantitative morphology of fashion sketches be characterized as a reproducible geometric organization before discrete structural or semantic units are imposed?**

This question is narrower than asking whether sketch representations can be learned. It is also distinct from asking whether predefined garment parts or semantic categories can be recognized. The objective is to establish the **quantitative morphological layer itself**.

---

### Hypothesis

We hypothesize that:

> **Garment sketches exhibit reproducible quantitative morphology organization that can be discovered from explicit morphology measurements without semantic supervision.**

The hypothesis is evaluated through a sequence of increasingly specific tests.

#### H1 — Quantitative Morphology Representation

A fixed representation constructed from explicit morphology measurements provides a quantitative description of garment sketches in which morphology relationships can be measured directly.

#### H2 — Local Quantitative Geometric Organization

The resulting morphology representation exhibits reproducible global and local geometric structure rather than behaving as an arbitrary collection of observations.

#### H3 — Connected Morphology Geometry

Local morphology relationships form a connected and geometrically traversable structure in which observations remain related through local neighborhoods and graph paths.

#### H4 — Recurring Density Organization

The morphology space contains recurring regions of increased observational density that remain detectable across multiple observational scales.

#### H5 — Quantitative Regional Organization

Independently discovered density regions exhibit reproducible differences in measurable morphology properties.

#### H6 — Null Robustness

Observed regional morphology-feature associations exceed those expected from arbitrary assignment of observations to regions with the same size distribution, providing a size-preserving null test of morphology-region association.

#### H7 — Cross-Scale Reproducibility

Quantitative regional morphology-profile organization remains reproducible across observational density scales without requiring direct correspondence between basin identities.

---

## Interpretation Boundary

The hypotheses deliberately stop at the level of **quantitative morphology organization**.

A positive result is interpreted as evidence for:

> **structured quantitative morphology**

and not automatically as evidence for:

- discrete morphology categories
- semantic morphology primitives
- named garment concepts
- morphology grammar
- a mathematical manifold

In particular:

```text
recurring density region
        ≠
semantic category

