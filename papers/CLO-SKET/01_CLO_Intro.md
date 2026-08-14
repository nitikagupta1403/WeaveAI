# 1. Introduction

A garment sketch is a compact visual representation of design.
Within a relatively small number of marks, a sketch can express
differences in proportion, spatial distribution, silhouette,
symmetry, occupancy, and other measurable properties of form.
These properties are visible in the sketch before any semantic
category is assigned to it. A garment sketch can therefore be
viewed not only as an image to be recognized, but also as a
morphological object whose internal quantitative organization
can be investigated directly.

Fashion sketches have long been used as computational interfaces
for communicating and interpreting garment shape. Earlier
sketch-based garment systems used drawn silhouettes and curves to
infer garment geometry or construct three-dimensional garments,
with subsequent work explicitly incorporating contextual factors
that influence garment shape. :contentReference[oaicite:2]{index=2}
More recent fashion-sketch research has increasingly addressed
semantic representation, fine-grained visual-language associations,
sketch editing, and sketch-to-image generation. :contentReference[oaicite:3]{index=3}
These directions demonstrate that substantial information can be
extracted from fashion sketches, but they also motivate a more
fundamental question that precedes semantic interpretation:
**what quantitative organization is already present in the
morphology of the sketches themselves?**

This distinction is important. Recognition and semantic modeling
ask what a sketch represents; generation asks what can be produced
from it; geometric interpretation asks how its depicted garment
shape can be reconstructed. The present study instead asks whether
the morphology underlying such interpretations exhibits a
reproducible organization before semantic categories are imposed.

This perspective motivates a fundamental question:

> **Does a collection of garment sketches exhibit reproducible
> morphological organization that can be discovered from explicit
> morphology measurements without using category labels,
> replication labels, target sketches, or learned neural
> representations?**

The question is deliberately posed at the level of morphology
rather than semantics. If semantic concepts are introduced before
the organization of morphology has been established, it becomes
difficult to determine whether the observed structure originates
from the sketches themselves or from the categories imposed during
analysis. We therefore begin with a geometry-first formulation in
which morphology is measured explicitly and its organization is
examined without semantic supervision.

## 1.1 Scientific Gap and Hypothesis

### Scientific Gap

Prior computational work on fashion and sketch understanding
has established multiple levels of structured representation,
including semantic categories and attributes, geometric and
shape descriptors, stroke- and point-based representations,
graph and relational structures, and primitive- or part-based
abstractions. These approaches demonstrate that fashion sketches
can be treated as structured visual objects rather than merely as
undifferentiated images. :contentReference[oaicite:1]{index=1}

A related line of work has also explored geometry-derived
structural representations in which recurring visual units are
identified from sketch geometry rather than being defined
entirely through predefined semantic parts. Such work motivates
the distinction between structural discovery and semantic
interpretation: a geometric unit may be reproducible and
structurally meaningful without yet possessing an independently
validated human semantic label. :contentReference[oaicite:2]{index=2}
:contentReference[oaicite:3]{index=3}

This distinction motivates the present study, but at a level
preceding primitive discovery.

Rather than beginning by defining discrete structural units,
we first ask whether the morphology of complete garment sketches
contains a reproducible quantitative organization from which
such higher-level interpretations could eventually be developed.

The scientific gap addressed here is therefore:

> **Can the quantitative morphology of fashion sketches be
> characterized as a reproducible, continuous geometric
> organization before discrete structural or semantic units are
> imposed?**

This question is narrower than asking whether sketch
representations can be learned. It is also distinct from asking
whether predefined garment parts or semantic categories can be
recognized. The objective is to establish the quantitative
morphological layer itself.

---

### Hypothesis

We hypothesize that:

> **Garment sketches exhibit reproducible quantitative morphology
> organization that can be discovered from explicit morphology
> measurements without semantic supervision.**

The hypothesis is evaluated through a sequence of increasingly
specific tests.

#### H1 — Quantitative morphology representation

A fixed representation constructed from explicit morphology
measurements can provide a reproducible quantitative description
of garment sketches.

#### H2 — Continuous geometric organization

The resulting morphology representation contains reproducible
spectral and local geometric structure rather than behaving as an
arbitrary collection of observations.

#### H3 — Connected morphology geometry

Local morphology relationships form a connected and geometrically
traversable structure in which observations remain related through
local neighborhoods and graph paths.

#### H4 — Recurring density organization

The continuous morphology space contains recurring regions of
increased observational density that remain detectable across
multiple observational scales.

#### H5 — Quantitative regional organization

Independently discovered density regions exhibit reproducible
differences in measurable morphology properties.

#### H6 — Null robustness

Observed regional morphology-feature associations exceed those
expected from arbitrary assignment of observations to regions
with the same size distribution at multiple observational scales.

#### H7 — Cross-scale generalization

Quantitative regional morphology-profile organization remains
recognizable when the observational density scale changes,
without requiring direct correspondence between basin identities.

---

### Interpretation Boundary

The hypotheses deliberately stop at the level of quantitative
morphology organization.

A positive result is interpreted as evidence for:

    structured quantitative morphology

and not automatically as evidence for:

    discrete morphology categories
    semantic primitives
    named garment concepts
    morphology grammar

In particular:

    recurring density region
        ≠
    semantic category

and:

    discriminating morphology feature
        ≠
    semantic primitive

This distinction follows the broader methodological principle
that structural discovery and semantic interpretation are
separate empirical questions. :contentReference[oaicite:4]{index=4}

The present study therefore establishes the layer:

    explicit morphology measurements
        ↓
    reproducible quantitative geometry
        ↓
    local and connected organization
        ↓
    recurring density structure
        ↓
    measurable regional morphology properties

The subsequent question—whether these quantitative structures
correspond to meaningful design concepts—is deliberately left
open for independent investigation.