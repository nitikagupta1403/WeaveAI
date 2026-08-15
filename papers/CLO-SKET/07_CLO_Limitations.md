# 7. Limitations and Future Scope

## 7.1 Limitations

The present study establishes quantitative morphology organization within
the Clo-Sket source dataset, but several limitations define the boundary
of the current evidence.

### 7.1.1 Dataset and external reproducibility

The analysis is based on 2,300 sketches from the Clo-Sket dataset.
Although quantitative morphology organization and regional profile
reproducibility were examined across multiple internal observational
scales, their reproducibility across other datasets, drawing styles,
designers, garment categories, and sketching conventions remains to be
established.

External replication on independently collected garment-sketch
datasets is therefore required before treating the observed organization
as dataset-independent morphology structure.

### 7.1.2 Dependence on the quantitative representation

The present morphology geometry is defined by the canonical
135-dimensional representation consisting of occupancy measurements and
global geometric descriptors.

Feature-block complementarity and perturbation analyses show that
multiple feature families contribute to the recovered geometry.
Nevertheless, the representation remains a designed quantitative
description of image morphology.

Alternative morphology representations may reveal additional structure
or modify the observed geometry. The present findings should therefore
be interpreted as evidence for quantitative structure within the defined
morphology representation rather than as proof that the representation
exhaustively captures garment morphology.

### 7.1.3 Density organization is not semantic validation

The recurring density regions identified in the morphology space are
quantitative structures discovered without semantic labels.

Their reproducibility and quantitative profile differences do not by
themselves establish that they correspond to human-recognizable
morphology concepts.

The present study therefore does not assign semantic names to density
regions or interpret individual regions as morphology categories.

### 7.1.4 No semantic primitive validation

Several quantitative morphology properties were found to participate in
morphology variation and regional organization.

However, statistical association with quantitative morphology geometry
does not establish semantic primitive status.

A morphology primitive would require independent evidence that a
quantitative property, or a combination of properties, corresponds
consistently to a recognizable morphological unit.

This semantic grounding has not yet been performed.

### 7.1.5 No compositional morphology grammar

The present study establishes quantitative organization among morphology
observations but does not establish rules governing how morphology units
combine.

In particular, the analyses do not demonstrate:

    morphology primitives
        +
    compositional rules
        =
    garment morphology grammar

The existence of recurring quantitative regions is therefore not
equivalent to discovering a grammar.

### 7.1.6 No causal interpretation

Feature perturbation demonstrates that different feature families
contribute to preservation of the observed quantitative geometry.

These perturbational results should not be interpreted as causal
relationships in garment construction or design.

Establishing causal morphology relationships would require controlled
interventions in which specific morphological properties are
systematically modified while other properties are held constant.

### 7.1.7 Intrinsic dimensionality remains unresolved

The 73-dimensional PCA representation and the approximately
10.55-dimensional participation-ratio effective dimensionality describe
variance structure within the observed representation.

Neither quantity establishes the exact dimensionality of an underlying
mathematical morphology manifold.

A more rigorous intrinsic-dimensionality investigation would require
comparison across multiple estimators, neighborhood scales,
representations, and independent datasets.

### 7.1.8 Density-scale dependence

The density regions are derived at multiple observational scales and
their exact number and membership vary with scale.

The present evidence therefore supports cross-scale reproducibility of
quantitative regional profiles rather than a single scale-independent
partition of the morphology space.

This distinction prevents the density regions from being interpreted as
fixed morphology categories.

### 7.1.9 Spatial locality does not imply semantic ordering

The feature-order analysis demonstrated reproducible local adjacency in
the ordered horizontal and vertical occupancy representations relative
to a coordinate-order permutation null.

This establishes quantitative spatial locality in the representation,
but does not establish that the ordering corresponds to semantic
ordering, morphology primitives, morphology categories, or a grammar.

The spatial structure should therefore be interpreted specifically as
local quantitative organization of ordered occupancy measurements.

---

# 7.2 Future Scope

The present work provides a quantitative foundation for several
successive research directions.

### 7.2.1 External replication

The first priority is to test whether the observed quantitative
morphology organization generalizes beyond Clo-Sket.

Future studies should evaluate independently collected garment sketches
using a frozen source representation and transformation pipeline where
appropriate.

The primary question is:

    Does the same structured quantitative morphology
    organization recur outside the source dataset?

Replication across datasets would substantially strengthen the
generality of the proposed morphology organization.

### 7.2.2 Human perceptual validation

The next major step is to connect quantitative morphology geometry with
human perception.

Independent observers could be asked to:

    • judge sketch similarity
    • identify recurring morphology configurations
    • group visually similar sketches
    • identify specific morphological properties
    • evaluate candidate morphology regions

These judgments could then be compared with the quantitative geometry
and density organization.

Such experiments would directly test whether computationally discovered
morphology structure corresponds to human-perceived morphology
organization.

### 7.2.3 Semantic grounding of candidate morphology primitives

Candidate quantitative morphology properties and recurring
configurations can next be evaluated as potential semantic morphology
primitives.

A stronger primitive hypothesis would require a reproducible mapping:

    quantitative morphology configuration
                ↓
    independently validated morphology unit

This mapping should be tested across multiple sketches, garment
contexts, and independent observers.

The goal would be to determine whether recurring quantitative structures
correspond to stable semantic units rather than merely statistical
regularities.

### 7.2.4 Investigation of morphology categories

If candidate morphology structures obtain independent perceptual or
semantic validation, a subsequent study could test whether recurring
quantitative regions correspond to stable morphology categories.

Such a claim would require evidence that:

    quantitative region
            ↓
    independently defined or
    human-recognized morphology concept

remains reproducible across sketches, observers, and datasets.

The present study does not perform this validation.

### 7.2.5 Investigation of compositional morphology structure

Only after candidate morphology units have been independently validated
should their relationships be investigated.

Future work can examine whether combinations of morphology units occur
according to reproducible structural relationships, such as:

    morphology unit A + morphology unit B
                ↓
    recurring garment configuration

and whether these relationships generalize across garment types and
sketch styles.

Such evidence would provide the empirical basis for investigating a
compositional morphology grammar.

### 7.2.6 Multiscale morphology representation

The present results indicate that quantitative regional organization can
be examined across multiple observational scales.

Future models could investigate whether morphology organization can be
represented across levels such as:

    local quantitative variation
            ↓
    recurring quantitative configurations
            ↓
    larger morphology structures
            ↓
    complete garment organization

This should be treated as a future representational hypothesis rather
than as evidence that a hierarchy or grammar already exists.

### 7.2.7 Cross-dataset morphology alignment

An important future direction is to determine whether quantitative
morphology profiles discovered independently in different datasets can
be aligned.

This would allow testing whether apparently recurring morphology
structures represent general properties of garment morphology rather
than dataset-specific configurations.

Such alignment should be performed without assuming that basin identities
or region labels correspond across datasets.

### 7.2.8 Out-of-distribution and held-out validation

Future studies should evaluate the frozen morphology representation on
held-out and out-of-distribution sketches.

A strong test would require:

    source-only fitting
          ↓
    frozen morphology representation
          ↓
    unseen sketches
          ↓
    morphology geometry
          ↓
    quantitative regional organization

without refitting the representation to the evaluation dataset.

This would provide a stronger test of reproducibility and external
validity.

### 7.2.9 Independent validation of regional structure

The present permutation analyses establish that observed regional
morphology associations exceed specific size-preserving null models.

Future work should test whether these regional structures remain
detectable under additional independently motivated null models and
alternative quantitative representations.

Such analyses would determine how robust the regional organization is to
different assumptions about morphology geometry and regional assignment.

### 7.2.10 Toward an empirically grounded morphology language

The long-term objective is to determine whether the quantitative
organization identified here can eventually be grounded as part of a
semantic morphology language.

The proposed progression is:

    quantitative morphology
            ↓
    structured quantitative geometry
            ↓
    recurring quantitative organization
            ↓
    independent perceptual validation
            ↓
    validated morphology units
            ↓
    semantic morphology interpretation
            ↓
    compositional relationships
            ↓
    possible morphology vocabulary
            ↓
    possible morphology grammar

The present study provides evidence for the first three quantitative
levels.

The subsequent levels require independent semantic, perceptual, and
compositional validation.

---

## 7.3 Overall Future Direction

The central future challenge is therefore not simply to discover more
regions or increase the number of morphology features.

The more important question is whether the quantitative structures
identified in this study correspond reliably to how humans perceive,
describe, and reason about garment form.

A successful next stage would establish a measurable correspondence
between:

    computational morphology structure
                ↕
    human morphological perception
                ↕
    independently validated morphology concepts
                ↕
    compositional garment structure

Such evidence would transform the present quantitative morphology
geometry from a descriptive computational representation into a
scientifically grounded basis for investigating the semantic
organization of garment sketches.

The present study therefore establishes the quantitative foundation,
while future work must establish its perceptual, semantic, and
compositional interpretation.