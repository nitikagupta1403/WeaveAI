# 7. Limitations and Future Scope

## 7.1 Limitations

The present study establishes the quantitative geometry of garment
sketch morphology within the Clo-Sket source dataset, but several
limitations define the boundary of the current evidence.

### 7.1.1 Dataset and generalization

The analysis is based on 2,300 sketches from the Clo-Sket dataset.
Although the geometry and regional organization are reproducible
across the internal observational scales examined here, their
generalization to other datasets, drawing styles, designers, garment
categories, and sketching conventions remains to be established.

External replication on independently collected garment-sketch
datasets is therefore required before treating the observed
organization as dataset-independent morphology structure.

### 7.1.2 Dependence on the quantitative representation

The present geometry is defined by the canonical 135-dimensional
morphology representation consisting of occupancy measurements and
global geometric descriptors.

The feature-block complementarity and perturbation analyses show that
multiple feature families contribute to the recovered geometry.
Nevertheless, the representation remains a designed quantitative
description of image morphology.

Alternative morphology representations may reveal additional
structure or modify the observed geometry. The present findings
should therefore be interpreted as evidence for structure within the
defined morphology representation rather than as proof that it
exhaustively captures garment morphology.

### 7.1.3 Density organization is not semantic validation

The recurring density regions identified in the morphology space are
quantitative structures discovered without semantic labels.

Their reproducibility and quantitative profile differences do not by
themselves establish that they correspond to human-recognizable
morphology concepts.

The present study therefore does not assign semantic names to
density regions or interpret individual regions as morphology
categories.

### 7.1.4 No semantic primitive validation

Several quantitative morphology properties were found to participate
in continuous variation and regional organization.

However, statistical association with morphology geometry does not
establish semantic primitive status.

A morphology primitive requires independent evidence that a
quantitative property, or a combination of properties, corresponds
consistently to a recognizable morphological unit.

This semantic grounding has not yet been performed.

### 7.1.5 No compositional grammar

The present study establishes organization among morphology
observations but does not establish rules governing how morphology
units combine.

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
contribute to preservation of the observed geometry.

These perturbational results should not be interpreted as causal
relationships in garment construction or design.

Establishing causal morphology relationships would require controlled
interventions in which specific morphological properties are
systematically modified while other properties are held constant.

### 7.1.7 Intrinsic dimensionality remains unresolved

The 73-dimensional PCA representation and the approximately
10.55-dimensional participation-ratio effective dimensionality
describe variance structure within the observed representation.

Neither quantity establishes the exact dimensionality of an
underlying mathematical morphology manifold.

A more rigorous intrinsic-dimensionality investigation would require
comparison across multiple estimators, neighborhood scales,
representations, and independent datasets.

---

# 7.2 Future Scope

The present work provides a quantitative foundation for several
successive research directions.

### 7.2.1 External replication

The first priority is to test whether the observed morphology
geometry generalizes beyond Clo-Sket.

Future studies should evaluate independently collected garment
sketches using the frozen source representation and transformation
pipeline.

The primary question is:

    Does the same structured morphology geometry
    recur outside the source dataset?

Replication across datasets would substantially strengthen the
generality of the proposed morphology organization.

### 7.2.2 Human perceptual validation

The next major step is to connect quantitative morphology geometry
with human perception.

Independent observers could be asked to:

    • judge sketch similarity
    • identify recurring morphology configurations
    • group visually similar sketches
    • identify specific morphological properties
    • evaluate candidate morphology regions

These judgments could then be compared with the quantitative
geometry and density organization.

Such experiments would directly test whether computationally
discovered morphology structure corresponds to human-perceived
morphology organization.

### 7.2.3 Semantic grounding of morphology primitives

Candidate morphology properties and recurring configurations can next
be evaluated as potential semantic morphology primitives.

A stronger primitive hypothesis would require a reproducible mapping:

    quantitative morphology configuration
                ↓
    human-recognizable morphology unit

This mapping should be tested across multiple sketches, garment
contexts, and independent observers.

The goal would be to determine whether recurring quantitative
structures correspond to stable semantic units rather than merely
statistical regularities.

### 7.2.4 Discovery of compositional morphology structure

Once candidate morphology primitives are independently validated,
their relationships can be investigated.

Future work can examine whether combinations of morphology units occur
according to reproducible structural rules, such as:

    primitive A + primitive B
        ↓
    recurring garment configuration

and whether these relationships generalize across garment types and
sketch styles.

This would provide the empirical basis for investigating a
compositional morphology grammar.

### 7.2.5 Hierarchical morphology representation

The present results suggest that morphology organization exists at
multiple observational scales.

Future models could therefore investigate hierarchical
representations in which:

    local morphology variation
            ↓
    recurring configurations
            ↓
    larger morphology structures
            ↓
    complete garment organization

Such a representation could preserve the continuous nature of the
morphology space while explicitly modelling recurring higher-level
structures.

### 7.2.6 Cross-dataset morphology alignment

An important future direction is to determine whether morphology
regions discovered independently in different datasets can be aligned
through their quantitative profiles.

This would allow testing whether apparently recurring morphology
structures represent general properties of garment morphology rather
than dataset-specific configurations.

### 7.2.7 Out-of-distribution and held-out validation

Future studies should evaluate the frozen morphology representation
on held-out and out-of-distribution sketches.

A strong test would require:

    source-only fitting
          ↓
    frozen morphology representation
          ↓
    unseen sketches
          ↓
    morphology geometry
          ↓
    regional organization

without refitting the representation to the evaluation dataset.

This would provide a stronger test of reproducibility and
generalization.

### 7.2.8 Toward an empirically grounded morphology language

The long-term objective is to determine whether the structured
quantitative organization identified here can be grounded as a
semantic morphology language.

The proposed progression is:

    quantitative morphology
            ↓
    structured morphology geometry
            ↓
    recurring morphology organization
            ↓
    perceptually validated morphology units
            ↓
    semantic morphology primitives
            ↓
    compositional relationships
            ↓
    morphology vocabulary
            ↓
    morphology grammar

The present study establishes evidence for the first three levels.

The subsequent levels require independent semantic and perceptual
validation.

---

## 7.3 Overall Future Direction

The central future challenge is therefore not simply to discover more
clusters or increase the number of morphology features.

The more important question is whether the quantitative structures
identified in this study can be connected reliably to how humans
perceive, describe, and construct garment form.

A successful next stage would establish a measurable correspondence
between:

    computational morphology structure
                ↕
    human morphological perception
                ↕
    semantic morphology concepts
                ↕
    compositional garment structure

Such evidence would transform the present quantitative morphology
geometry from a descriptive representation into a scientifically
grounded model of the semantic organization of garment sketches.

The present study therefore provides the geometric foundation, while
future work must establish its perceptual, semantic, and
compositional interpretation.