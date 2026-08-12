# 2. Related Work

Computational research on fashion and sketches has developed several forms of structured visual representation. These range from garment categories and attributes in fashion-image datasets to geometric, semantic, and relational representations of sketches. The approaches differ in whether their structural units are predefined, learned from visual data, or introduced for a particular downstream task.

## 2.1 Structured Representations of Fashion

Fashion-image datasets such as DeepFashion and DeepFashion2 established structured representations of garments through categories, attributes, landmarks, masks, and related annotations. Fashionpedia extends this approach through an expert-defined ontology of apparel categories, parts, and attributes, providing detailed semantic annotations for fashion images.

These resources demonstrate the value of structured representations for fashion understanding. However, their structural vocabularies are primarily defined through semantic categories, annotations, or task-specific labels rather than being derived directly from recurring geometric patterns in fashion sketches.

## 2.2 Computational Understanding of Sketches

Computational sketch research has explored representations based on strokes, points, geometry, and learned visual features, reflecting the importance of sketch-specific structure for recognition and interpretation. Sketch-a-Net demonstrated that sketch recognition benefits from representations designed for the distinctive visual properties of sketches, including their abstraction and deformation. Other sketch-understanding approaches have converted digital ink into symbolic representations and incorporated contextual or co-occurrence information among the resulting symbols.

These studies establish that sketches contain distinctive structural information that can be exploited computationally. They also motivate representations that preserve relationships among local sketch elements rather than treating a sketch solely as an undifferentiated image.

## 2.3 Fashion-Sketch Interpretation and Geometric Representation

Fashion-sketch research has represented garment structure through geometric descriptors, semantic component segmentation, and component-level relational or topological representations. These representations have supported tasks such as garment interpretation, modeling, matching, and retrieval.

Context-aware garment modeling has demonstrated that geometric properties and relationships among components can be used to infer or reconstruct garment structure from sketches. Graph-based and relational approaches similarly show that relationships among garment components provide useful information for computational interpretation.

These studies establish the importance of geometric and relational structure in fashion sketches, but they differ from the present work in how structural components are defined and in the objectives for which those representations are constructed. In particular, the present study does not begin by specifying garment components or semantic parts. Instead, it asks whether recurring geometric units can be learned directly from the observed sketch geometry.

## 2.4 Grammar and Compositional Representations

Grammar-based approaches provide another framework for representing structured visual organization, particularly through compositional relationships or production rules. Classical shape grammars represent design languages using predefined shapes and production rules. Such approaches demonstrate how recurring components and their relationships can provide a formal description of structured visual systems.

The present work adopts a related compositional perspective but differs in the direction from which the representation is constructed. Rather than defining a grammar or production system in advance, the study first identifies recurring geometric primitives from the sketch corpus and subsequently evaluates the sequential relationships that emerge among those primitives.

The resulting Visual Grammar is therefore corpus-derived and statistical. It describes observed regularities among learned geometric primitives rather than imposing a predefined rule system.

## 2.5 Recent Fashion-Sketch Resources and Multimodal Learning

Recent fashion-sketch resources have further established large-scale sketch collections for computational learning, including datasets that pair sketches with garment categories or textual descriptions. GarmentSketch, for example, provides a large-scale collection of fashion sketches paired with detailed textual descriptions for multimodal learning and sketch-to-fashion generation.

Such resources demonstrate the growing use of fashion sketches as computational inputs and provide increasingly rich supervision for multimodal learning. Their primary objectives, however, include downstream tasks such as generation, retrieval, or multimodal representation rather than discovering the internal structural organization of sketch geometry.

## 2.6 Positioning of the Present Study

Taken together, prior work provides several complementary approaches to representing fashion and sketches. Existing research demonstrates the value of semantic categories, geometric descriptors, component-level representations, relational structures, and predefined compositional grammars. However, comparatively less attention has been given to discovering a reusable structural vocabulary directly from recurring geometry in fashion sketches and then testing whether the learned units exhibit corpus-level organization.

The present study addresses this gap through a geometry-first representation. Persistent geometric events are extracted from sketch geometry and transformed into a learned vocabulary of recurring primitives. These primitives are then evaluated for morphological coherence, sequential enrichment, predictive organization, positional specialization, structural neighborhood, and compositional use across complete garments.

This distinction is central to the contribution of the present work: the structural vocabulary is not imposed at the beginning of the analysis. It is derived from recurring geometric evidence and subsequently examined for the organization that emerges within the learned representation.