# Wang et al. (2017) — Learning a Shared Shape Space for Multimodal Garment Design

## Citation

Wang, T. Y., Ceylan, D., Popovic, J., & Mitra, N. J. (2017).
Learning a Shared Shape Space for Multimodal Garment Design.
ACM Transactions on Graphics, 36(4), Article 1.

arXiv: 1806.11335

---

## 1. Research Question

Can different garment-design representations be mapped into a common latent space so that a designer can move interactively between:

1. 2D garment sketches,
2. garment and body parameters,
3. 3D draped garment shapes?

The objective is to support interactive garment design, editing, and retargeting without requiring expensive cloth simulation at every design step.

---

## 2. Core Idea

The authors learn a shared latent representation linking three design domains:

    2D sketch
          ↓
    shared latent space
          ↕
    garment/body parameters
          ↕
    3D draped garment

The latent space acts as a common interface between different representations of the same garment-design instance.

This allows the system to:

- infer garment/body parameters from a sketch;
- predict a 3D draped garment;
- edit garment parameters;
- interpolate between designs;
- texture garments;
- retarget garments to different body shapes.

---

## 3. Representation

Each synthetic training example contains:

    (P, M, S)

where:

### P — Parameter representation

P contains:

- garment sewing-pattern parameters;
- material parameters;
- human body-shape parameters.

The experiments use:

- Shirt: 9 garment parameters + 3 material + 10 body parameters = 22 dimensions
- Skirt: 4 garment parameters + 3 material + 10 body parameters = 17 dimensions
- Kimono: 11 garment parameters + 3 material + 10 body parameters = 24 dimensions

The body is represented using the SMPL model.

---

### M — 3D draped garment representation

The authors generate simulated garments using a cloth simulator.

They then apply PCA to the simulated garment meshes.

The first:

    k = 200

PCA components are retained.

Therefore:

    3D garment mesh
          ↓
         PCA
          ↓
    200-dimensional representation

Important:

PCA here is primarily a compact representation of the simulated 3D garment geometry.

It is NOT being used to discover a population-level morphological taxonomy.

---

### S — Sketch representation

The simulated garment is rendered into a non-photorealistic 2D sketch.

The sketch is:

- centered;
- cropped to 224 × 224;
- augmented by removing small line segments, smoothing curves, Gaussian blur, etc.

DenseNet-161 features are then extracted.

The resulting sketch descriptor is:

    2208 dimensions

Therefore:

    sketch image
        ↓
    DenseNet-161
        ↓
    2208-D descriptor

---

## 4. Dataset Generation

The dataset is synthetic.

The authors use three garment families:

- shirt
- skirt
- kimono

Garment parameters are sampled.

Body shapes are sampled from a parametric body model.

Garments are then simulated on the bodies.

Each resulting 3D garment is rendered into a sketch.

Thus each training instance contains:

    sketch
    +
    garment/body parameters
    +
    3D draped garment

For each garment type approximately 8000 simulated combinations are generated.

The simulation of 8000 samples for one garment type takes approximately 60 hours.

---

## 5. Shared Latent Space

The authors learn a:

    K = 100

dimensional shared latent space.

Mappings include:

    S → L
    P → L
    L → P
    L → M

where:

- S = sketch descriptor
- P = garment/body parameters
- M = 3D draped garment
- L = shared latent space

The architecture consists of several encoder-decoder networks that share the same embedding.

---

## 6. Joint Loss

The loss jointly penalizes:

1. parameter prediction error from a sketch;
2. 3D garment prediction error from a sketch;
3. 3D garment prediction error from parameters;
4. parameter reconstruction error.

Conceptually:

    L =
        sketch → parameters error
      + sketch → garment error
      + parameters → garment error
      + parameter reconstruction error

The purpose of the additional cross-modal consistency terms is to regularize the learning problem.

---

## 7. Important Scientific Point

The shared latent space is not simply an arbitrary compression.

It is constrained by multiple mappings between the modalities.

The authors show that a direct:

    sketch → 3D garment

network can overfit.

Joint learning across the modalities improves generalization.

Thus the latent space functions as a form of multimodal regularization.

---

## 8. Retargeting

The authors additionally learn a Siamese embedding for 3D garments.

The goal is to make distances between 3D garments correspond to distances between their corresponding sketches.

The learned embedding is then used in an optimization procedure to retarget garments to new body shapes.

The optimization searches for new garment parameters that preserve the visual/style characteristics of the original garment.

---

## 9. Evaluation

Evaluation is primarily performed on synthetic data.

The dataset is split:

    95% training
    5% testing

with no garment/body parameter combinations shared between the splits.

The authors evaluate:

- garment reconstruction error;
- body-shape prediction error;
- garment-parameter prediction error;
- vertex-position error;
- PCA reconstruction error.

They also provide:

- qualitative comparisons;
- real-image examples;
- latent-space interpolation;
- retargeting experiments;
- user study;
- comparison against an alternative direct mapping.

---

## 10. User Study

The user study asks participants to match input sketches with generated draped garments.

There are:

    400 pairing queries per garment type
    13 Amazon Mechanical Turk participants

The purpose is to test whether the generated garment preserves fold characteristics represented in the input sketch.

---

## 11. Main Contributions

The paper's contributions can be summarized as:

1. A joint embedding of different garment-design spaces.
2. Inference of garment/body parameters from a single sketch.
3. Prediction of 3D draped garment configurations.
4. Interactive multimodal garment editing.
5. Fold-aware garment retargeting across body shapes.

---

## 12. What Wang DOES establish

Wang establishes that:

- sketches contain information useful for recovering garment/body parameters;
- sketch, parameter, and 3D garment representations can be aligned;
- a shared latent representation can support multimodal garment design;
- latent interpolation can produce smooth garment variations;
- sketch-derived representations can support garment reconstruction and retargeting.

---

## 13. What Wang DOES NOT establish

Wang does NOT establish that:

- a population of fashion sketches has an intrinsic morphological structure;
- garment morphology can be discovered from a population without predefined garment parameters;
- latent dimensions correspond to interpretable morphological variables;
- fashion sketches form a statistically validated morphological grammar;
- morphology can be independently recovered from multiple representations;
- morphological clusters correspond to human-recognizable semantic garment concepts;
- a common morphology exists across arbitrary garment categories;
- a sketch population can be treated as a biological-style or statistical shape population.

---

## 14. Critical Distinction for Our Work

Wang starts with a predefined generative parameterization:

    garment type
        ↓
    predefined garment parameters
        ↓
    simulated garment
        ↓
    sketch

The shared latent space is therefore learned from known correspondences.

Our research asks a different question:

    observed sketch population
        ↓
    geometric / morphological representation
        ↓
    statistical shape space
        ↓
    discover structure
        ↓
    test whether structure corresponds to meaningful garment concepts

The direction of scientific inference is therefore different.

Wang:

    known design variables → learned shared representation

Our problem:

    observed population → discover morphological organization

---

## 15. PCA Distinction

Wang uses PCA on simulated 3D garment meshes.

This is fundamentally different from using PCA/statistical shape analysis to investigate whether a population of 2D garment sketches contains low-dimensional morphological organization.

Therefore:

    Wang PCA
        =
    representation/compression of simulated 3D geometry

whereas our proposed analysis is closer to:

    Population shape analysis
        =
    discovery and characterization of morphological variation

These should not be conflated.

---

## 16. Limitations Relevant to Our Research

The authors explicitly state that:

- each garment type has a predefined set of 2D sewing parameters;
- shapes outside those parameterized families cannot be represented;
- pose variation is initially not handled;
- separate latent spaces are learned for shirt, skirt, and kimono;
- unifying garment-specific latent spaces remains difficult.

These limitations reinforce that the work is a multimodal garment-design model rather than a general morphological theory of fashion sketches.

---

## 17. Relationship to Our Paper

### Category

MAJOR PRIOR ART / METHODOLOGICAL BOUNDARY

### Relevance

High.

### Direct competition with our central hypothesis

Low-to-moderate.

### Why?

Wang demonstrates multimodal representation learning involving sketches, but the scientific objective is interactive garment design and reconstruction rather than discovery of population-level morphology.

---

## 18. One-Sentence Positioning

Wang et al. demonstrate that 2D garment sketches can be aligned with predefined garment/body parameters and simulated 3D garment shapes through a shared latent space, but they do not investigate whether a population of 2D fashion sketches itself exhibits an independently discoverable and statistically validated morphological organization.

---

## 19. Evidence Status

Evidence supporting:

    multimodal sketch ↔ garment representation
    YES

Evidence supporting:

    shared latent design space
    YES

Evidence supporting:

    sketch → garment parameter inference
    YES

Evidence supporting:

    sketch → 3D garment reconstruction
    YES

Evidence supporting:

    population-level morphological structure of sketches
    NO

Evidence supporting:

    statistically discovered morphology of 2D fashion sketches
    NO

Evidence supporting:

    semantic interpretation of discovered morphology
    NO

---

## 20. Relevance to FOMO / Research Gap

Wang should be cited as evidence that the field has already explored:

    sketch
        ↔
    latent representation
        ↔
    garment parameters
        ↔
    3D garment

Therefore our novelty should NOT be framed as:

    "learning a latent representation of fashion sketches"

Instead, the potentially novel question is:

    "Can the morphology of a population of 2D fashion sketches be
     quantitatively characterized and represented as a statistically
     structured shape space, independently of a predefined garment
     simulation parameterization?"

This is the distinction that should guide the next literature search.