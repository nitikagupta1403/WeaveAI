# 2. Related Work

## 2.1 Fashion Sketches as Structured Representations

Fashion sketches occupy a distinctive position in computational
fashion research because they provide a compact visual description
of garment design before physical realization. Unlike photographs,
which contain extensive appearance, texture, lighting, and
background information, sketches emphasize selected aspects of
garment form and design. This abstraction has motivated research
that treats sketches as structured visual representations rather
than simply as sparse natural images.

Early computational work demonstrated that garment sketches can
serve as geometric interfaces for garment interpretation and
three-dimensional modeling. Context-aware garment modeling, for
example, interpreted sketched garment silhouettes in relation to
factors such as garment cut, gravity, and body contact to construct
plausible three-dimensional garments. This work established that
geometric information expressed in a sketch can be computationally
interpreted beyond the literal drawing itself.

Subsequent research has explored increasingly structured
representations of sketches, including strokes, points,
trajectories, geometric descriptors, graphs, landmarks, semantic
components, and learned visual features. Sketch-a-Net established
the importance of sketch-specific representations for recognition,
including representations that preserve information associated
with the drawing process. Other structured-sketch approaches have
represented relationships among points and strokes explicitly,
demonstrating that sketch structure can provide information beyond
individual visual elements.

These studies establish an important premise for the present work:
fashion sketches contain structured information that can be
represented computationally. The question addressed here,
however, is not whether such information can support a downstream
task, but how the morphology expressed by a collection of sketches
is organized quantitatively before a downstream semantic task is
specified.

---

## 2.2 Semantic and Annotated Representations of Fashion

A major direction in computational fashion has been the construction
of explicit semantic representations. DeepFashion established
large-scale fashion recognition and retrieval resources using
fine-grained clothing categories, attributes, landmarks, and image
correspondences. Fashionpedia extended this paradigm through a
fine-grained fashion ontology containing apparel categories, parts,
attributes, and their spatial annotations.

These resources are foundational for computational fashion
understanding because they make garment concepts explicit and
provide structured targets for learning. Their representations,
however, begin with a predefined semantic or structural vocabulary.
The computational problem is consequently to recognize, localize,
or associate concepts that have already been specified.

Fashion-specific landmark detection follows a similar formulation.
Functional landmarks such as neckline, hemline, and cuff locations
are defined in advance and subsequently detected from fashion
images. Clothing-sketch component segmentation likewise uses
manually defined component categories and geometric descriptors to
assign semantic labels to sketch elements.

These approaches establish strong prior art for semantic and
geometric interpretation of fashion imagery and sketches. They also
clarify an important distinction for the present study:

    predefined semantic structure
        →
    localization / recognition / prediction

is different from:

    quantitative morphology
        →
    discovery of reproducible organization

The present study therefore does not attempt to reconstruct or
replace existing fashion ontologies. Instead, it investigates the
quantitative morphology that precedes such semantic interpretation.

---

## 2.3 Geometric and Morphological Representation of Garment Sketches

Several studies have demonstrated that garment sketches contain
explicit geometric information relevant to garment structure.
Geometric descriptors have been used to characterize local width,
tangential direction, shape context, distances, curvature-related
properties, and relationships between neighboring sketch elements.
Other work has represented garment silhouettes, folds, fit,
proportionality, and structural garment patches through
pose-independent geometric descriptors.

Research connecting fashion sketches to garment patterns has
similarly established mathematical relationships among body
dimensions, sketch dimensions, and garment-pattern dimensions.
Such work reinforces the view that sketch geometry is not merely
decorative: it can encode measurable information related to garment
construction.

These studies provide important methodological precedent for
quantitative morphology. They show that measurable geometric
properties can be extracted from garment sketches and that local
and global geometric relationships can carry useful information.

The present work differs in the scientific question being asked.
Rather than using geometric measurements to predict a predefined
component, reconstruct a garment, associate a sketch with a
pattern, or retrieve a corresponding image, we use explicit
morphology measurements to characterize the organization of the
sketch population itself.

The distinction is therefore between:

    geometry as an input to a downstream task

and:

    geometry as the object of scientific analysis.

---

## 2.4 Sketch Abstraction, Components, and Graph-Based Structure

Another line of research has explored abstraction and
decomposition of sketches into smaller structural units. Work on
primitive-based sketch abstraction, for example, uses a fixed
vocabulary of generic geometric primitives and learns to map sketch
strokes to those primitives. The primitive vocabulary is specified
before learning; semantic preservation is then evaluated through
downstream recognition and retrieval.

Graph-based approaches provide a complementary perspective.
SketchGNN represents sketches through point-, stroke-, and
sketch-level structures and uses graph-based learning for semantic
segmentation. Such methods demonstrate that relationships among
sketch elements can be important for computational understanding.

Fashion-sketch component segmentation provides another closely
related example. Sampled points and local geometric descriptors can
be combined with pairwise relationships to assign predefined
clothing-component labels and support retrieval.

These approaches establish that:

    local geometry
    +
    relationships among local elements

can provide a meaningful representation of sketches.

They do not, however, require the underlying quantitative geometry
to organize itself into recurring regions before semantic labels
are introduced. Their structural vocabulary is either predefined,
task-specific, or learned within a supervised downstream objective.

The present study therefore examines a preceding question:
whether quantitative morphology itself exhibits reproducible
organization independent of a predefined component vocabulary.

---

## 2.5 Learned Representations for Fashion-Sketch Understanding

Recent fashion-sketch research increasingly relies on learned
representations. Neural models have been used for sketch
recognition, semantic segmentation, attribute disentanglement,
retrieval, sketch-to-image generation, garment modeling, and
pattern reconstruction.

This trend has substantially expanded the computational utility of
fashion sketches. Recent systems demonstrate that learned sketch
representations can encode information useful for body-aware
three-dimensional garment generation, attribute editing, and
sketch-driven garment-pattern reconstruction.

However, the role of the learned representation differs across
these applications. In most cases, the representation is optimized
for a downstream objective such as classification, editing,
retrieval, image generation, garment reconstruction, or pattern
prediction. The internal feature space therefore need not provide
an explicit or interpretable description of how morphology varies
across the sketch corpus.

This distinction is particularly important as fashion-sketch
research becomes increasingly multimodal. Recent resources such as
GarmentSketch pair large numbers of fashion sketches with rich
textual descriptions and use these pairings for sketch-guided
generation and multimodal understanding. Other recent systems
combine sketches with text or body representations to generate
realistic garments or reconstruct garment patterns.

Such work demonstrates the increasing semantic and practical value
of fashion sketches. It also shifts the field toward a question of
how sketches can be connected to external semantic or generative
representations.

The present study approaches the problem from the opposite
direction. Rather than asking how semantic information can be
attached to a sketch, we first ask whether reproducible quantitative
morphology organization can be identified within the sketches
themselves.

---

## 2.6 From Semantic Interpretation to Quantitative Morphology

The literature therefore contains several established levels of
fashion-sketch representation:

    semantic categories and attributes
        ↓
    landmarks and component annotations
        ↓
    geometric and morphological descriptors
        ↓
    stroke- and point-based representations
        ↓
    graph and relational representations
        ↓
    learned visual representations
        ↓
    multimodal and generative representations

Each level has demonstrated value for a particular computational
objective.

What is less directly characterized is the organization that lies
between explicit morphology measurement and these higher-level
interpretations.

In particular, the following questions remain distinct from
recognition, segmentation, retrieval, editing, reconstruction, and
generation:

    • Do quantitative morphology measurements form a reproducible
      geometric organization?

    • Is that organization locally continuous?

    • Does it form a connected morphology structure?

    • Does it contain recurring density organization?

    • Do independently discovered density regions possess
      reproducible quantitative morphology profiles?

    • Are such profiles stable under changes in observational scale?

These questions do not require the introduction of semantic labels.
They instead concern whether morphology itself exhibits measurable
organization that could provide a foundation for subsequent
interpretation.

---

## 2.7 The Representation Gap

The literature reviewed above establishes that fashion sketches
contain computationally useful information and that this
information can be represented at multiple levels. Existing work
has successfully used sketches for recognition, semantic
segmentation, component localization, geometric interpretation,
retrieval, editing, multimodal learning, three-dimensional garment
generation, and pattern reconstruction.

The present study does not challenge these accomplishments.
Instead, it isolates a more foundational representation question:

> **Before semantic categories, component labels, or downstream
> prediction objectives are introduced, does the quantitative
> morphology of garment sketches exhibit reproducible organization
> in its own right?**

This question differs from the discovery of a semantic vocabulary.
It also differs from the discovery of discrete primitives. A
density-organized region of morphology space is not assumed to be a
garment category, and a morphology feature associated with such a
region is not assumed to represent a semantic primitive.

The intended progression is therefore:

    explicit morphology measurements
        ↓
    quantitative morphology space
        ↓
    local geometric organization
        ↓
    connected morphology structure
        ↓
    recurring density organization
        ↓
    quantitative regional morphology profiles
        ↓
    [future structural interpretation]
        ↓
    [future semantic interpretation]

The present work addresses the first part of this progression.

Its contribution is consequently not another classifier,
retrieval system, generative model, or predefined fashion ontology.
Rather, it is an empirical characterization of whether a
geometry-first morphology space exhibits reproducible organization
that survives complementary robustness and null analyses.

This establishes a quantitative layer beneath semantic
interpretation while deliberately leaving the mapping from
quantitative morphology to human-interpretable design concepts as
an open research question.