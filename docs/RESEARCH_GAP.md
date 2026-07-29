# Research Gap

## Introduction

The preceding survey of academic research and commercial systems demonstrates remarkable progress in artificial intelligence for fashion. Recent advances have significantly improved image generation, virtual try-on, garment simulation, recommendation systems, and digital design workflows. These developments have made fashion technology more accessible and efficient than ever before.

Despite this progress, several fundamental challenges remain unresolved.

Most existing approaches optimise visual realism, automate specific tasks, or improve production workflows. Comparatively little attention has been given to representing the knowledge and reasoning that guide fashion design before a garment is created.

This chapter identifies the principal research gaps that motivate the Weave AI research programme.

---

# Gap 1: Absence of Computational Representation of Creative Intent

The earliest stages of fashion design begin with ideas rather than garments.

Designers reason about concepts such as proportion, silhouette, balance, emotion, craftsmanship, cultural context, functionality, and personal expression before making detailed technical decisions.

Current computational systems lack a structured representation capable of describing this creative intent.

As a result, AI systems primarily operate on images, text, or completed garments rather than the underlying reasoning that produced them.

This represents the most fundamental gap identified in the current state of the art.

---

# Gap 2: Lack of Reasoning Before Garment Creation

Most existing AI systems assume that a garment already exists.

Virtual try-on systems require completed garments.

Recommendation systems require existing products.

Generative image models produce visual concepts without maintaining explicit design knowledge.

Consequently, there is limited computational support during the earliest stages of fashion design, where many of the most important creative decisions are made.

---

# Gap 3: Fragmented Representation of Fashion Knowledge

Fashion design integrates knowledge from multiple domains, including:

- garment construction
- textiles
- material behaviour
- body morphology
- aesthetics
- craftsmanship
- historical influences
- cultural context
- personal style

Existing systems typically model only a subset of these domains.

There is currently no unified representation that captures these relationships within a single computational framework.

---

# Gap 4: Limited Explainability

Current generative AI systems frequently produce visually compelling results but provide limited explanation of how or why a particular design was generated.

For designers, understanding the reasoning behind design suggestions is often as important as the suggestions themselves.

The absence of explainable design reasoning limits trust, collaboration, and educational value.

---

# Gap 5: Personalisation as a Secondary Process

Most current systems personalise fashion after a design has already been created.

Personalisation is typically achieved through recommendation, retrieval, or virtual try-on.

Relatively little research investigates personalisation as an integral part of the creative design process itself.

This limits the ability of AI systems to support bespoke and couture workflows.

---

# Gap 6: Lack of Standardised Fashion Knowledge Representation

Many scientific disciplines benefit from canonical representations.

Examples include:

- molecular structures in chemistry
- anatomical models in medicine
- scene graphs in computer vision
- knowledge graphs on the Semantic Web

Fashion currently lacks an equally accepted computational representation capable of describing garments, creative intent, design decisions, materials, and their relationships in a unified manner.

This absence makes knowledge sharing, reasoning, and interoperability significantly more difficult.

---

# Gap 7: Evaluation Beyond Visual Quality

Most current benchmarks evaluate systems using metrics related to image quality, realism, similarity, or retrieval accuracy.

These measures provide limited insight into whether an AI system:

- preserves designer intent
- supports creative exploration
- improves communication
- assists decision-making
- produces meaningful explanations

New evaluation methodologies may therefore be required for AI systems designed to support creative collaboration.

---

# Summary of Identified Research Gaps

| Gap | Current Limitation | Research Opportunity |
|------|--------------------|----------------------|
| Creative Intent | No computational representation | Develop structured representations of designer intent |
| Early Design | Focus on completed garments | Support reasoning before garments exist |
| Fashion Knowledge | Fragmented representations | Integrate fashion knowledge into a unified framework |
| Explainability | Limited reasoning transparency | Explain AI-assisted design decisions |
| Personalisation | Applied after design | Integrate personalisation into the creative process |
| Knowledge Representation | No canonical model | Investigate computational representations for fashion |
| Evaluation | Image-centric metrics | Develop metrics for creative reasoning and collaboration |

---

# Research Opportunity

The identified gaps suggest that future progress in fashion AI may require a shift in emphasis.

Rather than focusing exclusively on generating increasingly realistic images, future systems may benefit from computational representations that enable reasoning about fashion throughout the creative process.

This observation motivates the central hypothesis of the Weave AI research programme: that representing creative intent as structured knowledge can enable AI systems to support design exploration, communication, personalisation, and informed decision-making before garments are physically realised.

The next chapter introduces the proposed research direction for investigating this hypothesis.
