# 2. Related Work

Computational research on fashion and sketch understanding has developed
multiple approaches for representing visual structure, ranging from semantic
fashion ontologies and annotated garment datasets to geometric, stroke-based,
graph-based, and learned representations of sketches. These approaches differ
in the type of structural information they represent, the source of their
representational units, and the downstream objectives for which those
representations are constructed.

The present study is positioned at the intersection of these directions but
addresses a more specific representation question: whether recurring geometric
units in fashion sketches can be induced directly from sketch geometry and
subsequently characterized as a reusable corpus-level structural vocabulary.

## 2.1 Structured Representations of Fashion

Large-scale fashion datasets established structured representations of
garments through categories, attributes, landmarks, segmentation masks, and
other annotations. DeepFashion introduced large-scale fashion-image
annotations for clothing categories, attributes, and landmarks, while
DeepFashion2 extended structured garment representation through additional
annotations including categories, landmarks, masks, and clothing-instance
information. Fashionpedia further developed an expert-defined ontology of
fashion concepts, including apparel categories, parts, and attributes.

These resources demonstrate the importance of structured representations for
computational fashion understanding. They also provide increasingly rich
supervision for tasks such as detection, segmentation, recognition, retrieval,
and attribute prediction.

However, the structural vocabularies in these resources are primarily
defined through semantic categories, expert annotations, landmarks, or
task-specific labels. They therefore address a different level of the
representation problem from the one investigated here.

The present study does not attempt to replace semantic fashion ontologies.
Instead, it asks whether a lower-level structural vocabulary can first be
derived from recurring geometric patterns in fashion sketches, before
higher-level semantic interpretation is introduced.

This distinction is important because a semantic category system establishes
what concepts are represented, whereas a geometry-derived vocabulary asks what
recurring structural units emerge from the visual data itself.

## 2.2 Computational Understanding of Sketches

Computational sketch research has established that sketches require
representations that account for their sparse, abstract, and often highly
variable visual structure. Approaches have represented sketches using strokes,
points, trajectories, geometric descriptors, raster features, learned visual
embeddings, and relational structures.

Sketch recognition research has demonstrated that architectures designed
specifically for sketch characteristics can substantially improve recognition
performance. Other approaches have represented digital ink or sketch elements
through symbolic or graph-based structures, incorporating contextual,
co-occurrence, or relational information among local elements.

These studies establish two important principles relevant to the present work.

First, sketch structure cannot always be adequately described by treating the
input as an ordinary natural-image problem. Second, relationships among local
sketch elements can provide information beyond the isolated appearance of
individual elements.

The present study builds on this broader view of sketches but addresses a
different question. Rather than learning a representation primarily for
recognition or another downstream task, we investigate whether recurring
geometric units themselves can be discovered from a sketch corpus and then
examined for morphological and sequential organization.

Thus, the contribution is not the general idea of learning from sketches.
Learned sketch representations are well established. The distinction lies in
the explicit discovery and subsequent characterization of reusable
geometry-derived units.

## 2.3 Fashion-Sketch Interpretation and Geometric Representation

Research specifically concerned with fashion sketches has explored geometric
descriptors, garment landmarks, semantic component representations,
segmentation, relational structures, and topology-aware representations.
These approaches have supported tasks including garment interpretation,
component localization, reconstruction, matching, retrieval, and design
analysis.

Geometric representations are particularly relevant because fashion sketches
often encode garment structure through changes in silhouette, width,
proportion, boundaries, and component relationships rather than through
photorealistic appearance.

Context-aware approaches have shown that geometric properties and relationships
among garment components can be used to infer or reconstruct garment
structure from sketches. Graph-based approaches similarly demonstrate that
representing relationships among components can provide useful information
for computational interpretation.

Other work has investigated primitive-based abstraction of sketches, in which
complex visual structures are reduced to simpler geometric units for
representation, abstraction, or matching.

These studies provide important precedents for treating garment sketches as
structured geometric objects rather than undifferentiated images. They also
show that local geometric units and their relationships can be useful
representational elements.

The present work differs primarily in how the structural vocabulary is
constructed and what is subsequently tested.

Rather than beginning with predefined garment components, manually specified
semantic parts, or a representation optimized for a particular downstream
task, the present study derives primitive identities from recurring geometric
patterns observed in the target sketch corpus. The resulting primitives are
then evaluated independently for morphological coherence, positional
organization, sequential relationships, and compositional reuse.

The distinction is therefore not simply between learned and non-learned
representations. It concerns the level at which structural units are induced
and the scientific question used to evaluate them.

## 2.4 Primitive-Based and Part-Based Abstraction

Primitive-based representation has a long history in computer vision and
shape analysis. Representing complex visual objects through simpler recurring
units can provide advantages for abstraction, comparison, and structural
reasoning.

In fashion and sketch understanding, part-based approaches commonly represent
garments through components such as collars, sleeves, cuffs, bodices, skirts,
or other semantically defined regions. Such representations can be highly
useful when the semantic components are known in advance or when downstream
tasks require explicit part labels.

However, a predefined part vocabulary and a geometry-derived primitive
vocabulary answer different scientific questions.

A predefined component representation asks whether a known semantic component
can be detected or represented. A geometry-derived representation asks
whether recurring structure can be discovered without requiring those semantic
categories during primitive formation.

The present work therefore treats primitive discovery as a structural
identification problem. The learned primitive vocabulary is not assumed to
correspond one-to-one with conventional garment parts. Instead, its validity
at the structural level is evaluated through measurable geometric coherence
and its organization within complete garment sequences.

This distinction also provides a basis for separating structural discovery
from semantic interpretation. A primitive may be geometrically stable and
structurally meaningful without yet having an independently validated human
semantic label.

## 2.5 Grammar and Compositional Representations

Grammar-based approaches provide a complementary framework for representing
structured visual systems. Classical shape grammars describe design spaces
through reusable shapes, transformations, and production rules. More broadly,
compositional representations treat complex objects as combinations of
reusable elements and relationships.

These approaches motivate an important idea for fashion-sketch
representation: structural information may reside not only in individual
components but also in the relationships through which components are
combined.

The present work adopts this compositional perspective but reverses the usual
direction of construction.

Rather than specifying a grammar or production-rule system in advance, the
study first derives recurring geometric primitives from observed sketch
geometry. Sequential relationships among those primitives are then measured
empirically.

This distinction is fundamental.

The resulting representation is therefore **corpus-derived and statistical**.
It describes observed regularities among learned geometric units rather than
imposing a predefined grammar.

The term *grammar-like* is consequently used in a restricted computational
sense. It refers to measurable context-dependent sequential regularities,
including non-random transition structure and predictive information carried
by local primitive context.

It does not imply that the study has recovered a complete generative grammar,
a universal production-rule system, or a cognitive theory of fashion design.

## 2.6 Fashion-Sketch Resources and Multimodal Learning

The Clo-Sket dataset provides an important external resource for computational
fashion-sketch research. The dataset contains sketches derived from 230
clothing images spanning six broad clothing categories and 23 subcategories,
with ten sketch drawings produced for each source image. It was released as a
public dataset for applications including cross-domain image matching,
retrieval, and classification. [Clo-Sket citation]

Clo-Sket is particularly relevant to the present study because its repeated
sketches of the same underlying clothing image provide substantial
within-identity variation while preserving an underlying garment identity.
This makes it suitable for evaluating whether a learned structural
representation retains information associated with garment identity despite
variation in sketch production.

In the present study, Clo-Sket is used strictly as an independent evaluation
population. The primitive vocabulary is learned from the primary research
corpus and frozen before transfer to the Clo-Sket benchmark. Thus, the
benchmark is not used to define, tune, or rename the learned primitives.
Instead, it provides an external test of whether measurable structural
properties remain present when the frozen representation is applied to a
separate fashion-sketch population.

## 2.7 Fashion-Sketch Resources and Multimodal Learning

Recent fashion-sketch resources have expanded the scale and diversity of
available sketch data and have increasingly connected sketches with semantic,
textual, or multimodal information.

Datasets pairing fashion sketches with garment categories, attributes, or
textual descriptions support tasks such as sketch retrieval, multimodal
representation learning, text-conditioned generation, and sketch-to-fashion
translation.

These resources are important because they demonstrate that fashion sketches
can serve as meaningful computational representations of garment concepts and
can be connected to richer semantic and textual information.

However, their primary objectives generally concern downstream multimodal
learning, retrieval, recognition, or generation. They do not necessarily
address whether recurring geometric structure within sketches can itself be
discovered as a corpus-level vocabulary before semantic or textual supervision
is introduced.

The present study therefore occupies a complementary position. Rather than
using semantic or textual information to define the representation, it first
constructs a geometry-derived structural layer and subsequently investigates
how that layer is organized.

This separation allows the relationship between geometry and semantics to be
treated as an empirical question rather than being assumed during primitive
discovery.

## 2.8 The Representation Gap

Taken together, prior research establishes several important approaches to
structured fashion and sketch representation:

- semantic fashion categories and attributes;
- landmarks and component annotations;
- geometric and shape descriptors;
- stroke- and point-based sketch representations;
- graph and relational representations;
- predefined or learned primitive abstractions;
- part-based garment representations; and
- grammar-based or compositional models.

These approaches demonstrate that structure can be represented at multiple
levels. Nevertheless, they leave a more specific representation question open:

> **Can recurring geometric units in fashion sketches be induced directly from
> the observed geometry and then evaluated as a reusable corpus-level
> vocabulary before predefined semantic interpretation is imposed?**

This question is narrower than asking whether sketch representations can be
learned. Learned sketch representations are already well established.

The specific gap addressed here concerns the **discovery and structural
characterization of reusable geometry-derived units** and the examination of
whether those units exhibit systematic:

1. morphological organization;
2. positional specialization;
3. sequential relationships;
4. local contextual structure; and
5. compositional reuse.

The independent evaluation of a frozen representation further asks whether
such structural information remains measurable outside the corpus from which
the vocabulary was learned.

This framing deliberately avoids claiming that no previous work has used
learned primitives, geometric abstraction, or structured sketch
representations. The contribution instead lies in combining geometry-derived
primitive discovery with explicit corpus-level evaluation of the resulting
structural organization.

## 2.9 Positioning of the Present Study

The present study addresses this representation question through a
geometry-first pipeline.

Continuous fashion-sketch geometry is transformed into a one-dimensional
geometric representation from which persistent local events are extracted.
These events are represented using normalized local geometric curves, from
which a vocabulary of recurring geometry primitives is learned.

The learned primitives are then evaluated at several complementary levels.

### 2.9.1 Morphological Organization

We test whether curves assigned to the same learned primitive exhibit greater
geometric similarity than curves assigned to different primitives.

This evaluates whether primitive identities correspond to reproducible regions
of geometric variation rather than arbitrary partitions of the event space.

### 2.9.2 Positional Organization

We examine whether primitive identities exhibit characteristic locations
within complete garment sequences.

This tests whether learned primitives occupy structurally differentiated
positions rather than appearing uniformly throughout garment descriptions.

### 2.9.3 Sequential Organization

We evaluate whether primitive transitions deviate from within-garment
permutation expectations and whether immediate primitive context provides
predictive information about subsequent primitives.

This separates sequential organization from simple differences in marginal
primitive frequency.

### 2.9.4 Structural Roles

We characterize primitives through their local predecessor and successor
neighborhoods, together with their morphological and positional properties.

This provides a computational description of primitive structural roles without
requiring those roles to be assigned human semantic labels.

### 2.9.5 Compositional Organization

Complete garments are represented as ordered combinations of primitives drawn
from the shared vocabulary.

This allows reuse and variation of structural units to be evaluated directly
rather than assuming compositionality from the existence of discrete symbols.

### 2.9.6 Independent Evaluation

Finally, the frozen representation is evaluated on an independent CLO-SK
population.

This external evaluation distinguishes properties discovered in the primary
corpus from structural information that remains measurable after transfer to
a separate sketch population.

## 2.10 Scope of the Contribution

The contribution of the present study is therefore not the introduction of
another downstream classifier, retrieval system, or semantic ontology.

Instead, it is the construction and empirical characterization of a
**geometry-derived symbolic layer between continuous sketch geometry and
higher-level interpretation**.

The representation is deliberately evaluated at multiple levels because no
single analysis is sufficient to establish the existence of a useful
structural vocabulary.

Morphological analysis addresses whether the learned units are geometrically
coherent. Sequential analysis addresses whether the units participate in
non-random and predictive ordering. Positional and contextual analyses
characterize structural roles. Compositional analyses examine reuse across
complete garments. Independent benchmark evaluation tests whether measurable
structural information remains present beyond the discovery corpus.

This combination provides a more constrained interpretation than simply
claiming that the learned primitives are meaningful.

The study therefore treats **structural discovery** and **semantic
interpretation** as separate empirical questions.

Structural discovery is investigated in the present work through geometry,
morphology, sequence, and composition.

Human semantic interpretation remains a separate question requiring
independent evidence, such as expert annotation, inter-annotator agreement,
or explicit primitive-to-concept correspondence analysis.

The resulting positioning is consequently:

> **The present work investigates whether recurring geometric organization in
> fashion sketches can be discovered from visual evidence and represented as
> a reusable symbolic vocabulary whose morphology, positional behavior,
> sequential organization, and compositional reuse can be measured
> independently of predefined semantic labels.**

This provides a geometry-derived structural foundation on which future
semantic interpretation can be investigated without assuming semantic meaning
from geometric regularity alone.