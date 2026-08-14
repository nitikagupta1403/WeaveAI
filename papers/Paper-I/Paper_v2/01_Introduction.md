# 1. Introduction

Fashion sketches provide a compact representation of garment design in which a relatively small number of lines and geometric marks encode structural information about silhouette, proportion, and component organization. Unlike photographs or rendered garments, sketches abstract away much of the material and appearance information of a garment while retaining geometric structure. This makes them a useful setting for investigating how recurring visual structure can be identified and represented computationally.

A central challenge is that the structural organization of fashion sketches can be represented at several levels, but the source of that representation is not always the same. Prior work has demonstrated the usefulness of stroke-aware sketch representations, geometric descriptors, predefined fashion landmarks, semantic component segmentation, graph-based sketch representations, and primitive-based abstraction. Such approaches establish important prior art for representing geometric and semantic structure in sketches. However, they address different questions, including recognition, retrieval, segmentation, abstraction, or localization. A more fundamental question remains: **can recurring structural units themselves be induced from the geometry of a sketch corpus, before semantic component categories are introduced?** This distinction concerns the direction of representation construction rather than simply the choice of model or task.

This study investigates whether recurring geometric structure in fashion sketches can be learned directly from observed sketch geometry and organized into a reusable symbolic representation. We adopt a geometry-first approach in which continuous sketch geometry is transformed into a one-dimensional width signal, localized persistent geometric events are extracted, and the resulting events are represented as normalized local geometric curves. A corpus-derived vocabulary of recurring geometry primitives is then learned from these representations.

The learned vocabulary is first evaluated as a representation of recurring geometric structure. We test whether curves assigned to the same primitive exhibit greater morphological similarity than curves assigned to different primitives. This analysis asks whether the learned units correspond to reproducible regions of geometric variation rather than arbitrary partitions of the event space. The primitive vocabulary is subsequently characterized through positional distributions and local sequential neighborhoods, allowing individual primitives to be described not only by their morphology but also by their structural roles within complete garment sequences.

We next examine whether these learned units exhibit sequential organization. Garments are represented as ordered primitive sequences, enabling primitive-to-primitive transitions to be quantified across the corpus. Within-garment permutation tests assess whether observed transition frequencies differ from those expected when primitive composition is preserved but ordering is randomized. Predictive analyses further test whether immediate primitive context contains information about subsequent primitives and whether this predictive structure remains measurable for garments excluded from transition estimation. These analyses distinguish sequential organization from simple differences in marginal primitive frequency.

The representation is then examined at the level of complete garments. Individual garments are represented as ordered combinations of primitives drawn from the shared vocabulary, allowing the study to test whether a relatively small set of recurring units can be reused across different garment sequences. This provides an empirical test of compositional organization rather than assuming that compositionality follows from the existence of discrete primitives alone. In the primary corpus, the learned vocabulary contains 12 primitives, while individual garments typically instantiate only a subset of them.

The learned representation is finally evaluated on an independent benchmark rather than only on the corpus from which the vocabulary was derived. The CLO-SK evaluation population contains 2,299 sketch images representing 230 garment identities, 23 garment categories, and 12 sketchers. The primitive vocabulary is frozen before transfer to this benchmark, and the symbolic representation is evaluated alongside an independent continuous geometric representation. This design allows the study to distinguish properties learned within the discovery corpus from structural information that remains measurable in an external sketch population.

The external evaluation also provides an important boundary condition. Raw geometry substantially outperforms the symbolic representation for direct garment-identity retrieval, including under cross-sketcher evaluation, demonstrating that discretization into primitives does not preserve all fine-grained geometric information. At the same time, the frozen symbolic representation retains measurable identity-associated, category-associated, and geometry-associated structure on the independent benchmark. The symbolic representation is therefore investigated not as a lossless replacement for sketch geometry, but as an intermediate representational level that makes selected recurring structural properties explicit.

Taken together, the study addresses the following question:

> **Can recurring geometric organization in fashion sketches be learned from visual evidence and represented as a structured system of reusable components and their relationships?**

The resulting framework connects several levels of representation:

$$
\text{sketch geometry}
\rightarrow
\text{persistent geometric events}
\rightarrow
\text{learned primitives}
\rightarrow
\text{position and morphology}
\rightarrow
\text{sequential organization}
\rightarrow
\text{compositional representation}.
$$

The sequential regularities identified within this representation motivate a **grammar-like** interpretation in a computational and statistical sense. The study does not claim to recover a complete generative grammar of fashion design, nor does it establish that individual primitives correspond to human-defined garment concepts. Rather, the grammar-like interpretation refers to measurable context-dependent regularities among learned structural units.

Accordingly, the contribution of this work is deliberately narrower than a complete semantic theory of fashion design. It is a **geometry-first, A corpus-derived vocabulary of recurring geometry primitives is then induced from these representations.**. The resulting structural layer provides an empirical basis for investigating whether learned geometric organization can subsequently be connected to independently validated semantic concepts.