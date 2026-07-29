# Design DNA Schema v0

## Towards a Computational Representation of Fashion Design

## Purpose

This document proposes the first conceptual schema for **Design DNA**, the computational representation at the core of the Weave AI research programme.

The objective is not to define a final database schema or implementation.

Instead, this document identifies the fundamental entities, attributes, and relationships that together describe a fashion design before it becomes a physical garment.

The schema will evolve as research progresses.

---

# Design Principles

The schema should satisfy the following principles.

- Human understandable
- Machine readable
- Explainable
- Extensible
- Modular
- Independent of any specific AI model
- Independent of any programming language
- Suitable for reasoning rather than only storage

---

# Core Entities

The current hypothesis is that every fashion design can be described through a set of interconnected entities.

## 1. Designer

Represents the creator and their evolving creative identity.

Possible attributes:

- Designer ID
- Experience
- Brand
- Design philosophy
- Signature style
- Preferred silhouettes
- Preferred materials
- Preferred construction techniques
- Creative influences

---

## 2. Design Intent

Represents the purpose behind a garment.

Possible attributes:

- Design objective
- Occasion
- Target audience
- Emotional expression
- Functional goals
- Cultural inspiration
- Historical inspiration
- Sustainability considerations

---

## 3. Garment

Represents the conceptual garment itself.

Possible attributes:

- Garment category
- Garment type
- Collection
- Season
- Gender
- Style classification

---

## 4. Silhouette

Represents the overall visual form.

Possible attributes:

- Shape
- Volume
- Proportion
- Length
- Fit
- Balance

---

## 5. Construction

Represents how the garment is assembled.

Possible attributes:

- Pattern type
- Seam construction
- Panels
- Layering
- Structural support
- Closures

---

## 6. Material

Represents physical materials.

Possible attributes:

- Fabric
- Fibre composition
- Weight
- Stretch
- Drape
- Texture
- Transparency
- Finish

---

## 7. Decorative Elements

Possible attributes:

- Embroidery
- Lace
- Prints
- Beads
- Sequins
- Appliqué
- Surface treatments

---

## 8. Colour

Possible attributes:

- Primary colours
- Secondary colours
- Palette
- Contrast
- Harmony

---

## 9. Body Representation

Represents the intended wearer.

Possible attributes:

- Body measurements
- Body morphology
- Posture
- Size
- Fit preferences
- Accessibility requirements

---

## 10. Personalisation

Represents customer-specific modifications.

Possible attributes:

- Colour preferences
- Fabric preferences
- Fit adjustments
- Functional requests
- Cultural preferences
- Budget constraints

---

## 11. Constraints

Represents practical limitations.

Possible attributes:

- Manufacturing
- Budget
- Material availability
- Delivery timeline
- Sustainability goals

---

# Relationships

The power of Design DNA lies not only in the entities but also in the relationships between them.

Examples include:

Designer
→ creates
→ Design Intent

Design Intent
→ defines
→ Garment

Garment
→ has
→ Silhouette

Garment
→ uses
→ Material

Garment
→ requires
→ Construction

Material
→ influences
→ Silhouette

Material
→ constrains
→ Construction

Construction
→ affects
→ Fit

Body Representation
→ influences
→ Personalisation

Personalisation
→ modifies
→ Garment

Constraints
→ limit
→ Material

Constraints
→ limit
→ Construction

---

# Design DNA Layers

The schema is organised into four conceptual layers.

Layer 1 — Creative Layer

- Designer
- Design Intent

Layer 2 — Design Layer

- Garment
- Silhouette
- Construction
- Decoration

Layer 3 — Physical Layer

- Material
- Body Representation

Layer 4 — Context Layer

- Personalisation
- Constraints

---

# Design DNA Graph

The current hypothesis is that Design DNA should be represented as a graph rather than a flat table.

Reasons include:

- Fashion concepts are highly interconnected.
- Relationships are often more important than individual attributes.
- Graph structures support reasoning and explainability.
- The representation can evolve without redesigning the entire schema.

---

# Open Questions

The following questions remain unresolved.

- Which entities are fundamental?
- Which attributes should be mandatory?
- Which relationships should carry weights?
- Can Design DNA evolve over time?
- How should uncertainty be represented?
- How should multiple designers collaborate?
- How should conflicting design constraints be handled?

These questions will guide future research.

---

# Future Work

Future versions of the schema will investigate:

- Fashion ontology
- Knowledge graphs
- Graph neural networks
- Multimodal embeddings
- Temporal evolution of Design DNA
- Designer memory
- Explainable reasoning
- Evaluation methodologies

---

# Version History

Version 0

Initial conceptual schema defining the core entities, relationships, and design principles of Design DNA.

This document is intended as a research foundation rather than a final implementation specification.
