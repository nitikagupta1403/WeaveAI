# Literature Audit — Paper 1
## Sketch-a-Net

### Paper-level understanding

Sketch-a-Net is a sketch-recognition method that learns a visual
representation directly from sketch images using a CNN.

The central objective is **recognition**, not discovery of a
population-level morphology organization.

The method exploits two important properties of sketches:

1. visual appearance / spatial structure
2. stroke-order information

The representation is learned from image pixels rather than being
constructed explicitly from predefined morphology measurements.

---

## 1. What problem does the paper address?

The paper asks whether a CNN can be specifically designed to recognize
free-hand sketches effectively by exploiting properties that distinguish
sketches from natural photographs.

The focus is therefore:

    sketch
        ↓
    learned visual representation
        ↓
    recognition

The scientific objective is **sketch recognition**.

---

## 2. What representation do they use?

The primary representation is a **learned CNN representation**.

The network learns visual filters/features directly from the sketch
images through supervised training.

The authors also explicitly incorporate information about stroke order.

Therefore:

    image pixels
        ↓
    CNN
        ↓
    learned visual features
        ↓
    recognition

This differs from CLO-SKET, where morphology measurements are explicitly
constructed before the geometric analysis.

---

## 3. How is stroke-order information incorporated?

Stroke order is not learned using an RNN or a separate Bayesian
sequence-learning model.

Instead, the authors explicitly construct multiple input channels from
the drawing sequence.

The stroke sequence is divided into ordered portions, and combinations
of those portions are represented as separate channels.

Conceptually:

    stroke sequence
          ↓
    ┌──────┬──────┬──────┐
    │  P1  │  P2  │  P3  │
    └──────┴──────┴──────┘
          ↓
    multi-channel representation
          ↓
          CNN

The CNN then learns how useful these channels are for recognition.

Therefore the distinction is:

    human-designed temporal encoding
            +
    machine-learned visual representation

rather than:

    Bayesian sequence discovery.

---

## 4. What is the role of Bayesian fusion?

Bayesian fusion is used later to combine predictions from multiple
networks operating at different visual scales.

Conceptually:

    sketch
      ↓
    multiple image scales
      ↓
    separate CNNs
      ↓
    predictions
      ↓
    Bayesian fusion
      ↓
    final recognition

Therefore Bayesian fusion should NOT be described as the mechanism
that learns stroke sequences.

It is a mechanism for combining evidence from multiple visual scales.

The multi-scale design is better understood as an ensemble/fusion
strategy than as ordinary data augmentation.

---

## 5. What does the paper establish?

The paper establishes that:

- sketch-specific CNN architectures can learn useful visual
  representations;
- sketch recognition benefits from exploiting sketch-specific
  properties;
- stroke-order information can be incorporated into a CNN input
  representation;
- multiple visual scales can provide complementary recognition
  information;
- Bayesian fusion can combine predictions from multiple scales.

---

## 6. What does the paper NOT establish?

The paper does NOT establish:

- an explicit population-level morphology space;
- a canonical quantitative morphology representation;
- recurring morphology density regions;
- morphology-region associations;
- cross-scale reproducibility of quantitative morphology profiles;
- semantic morphology primitives discovered from an unlabeled
  morphology space;
- a morphology vocabulary;
- a morphology grammar;
- a mathematical morphology manifold.

Its learned representation is optimized for the downstream task of
sketch recognition.

---

# 7. Relationship to CLO-SKET

## Sketch-a-Net

    sketch pixels
          ↓
    CNN representation
          ↓
    recognition

Geometry is represented implicitly through learned visual features.

## CLO-SKET

    sketch image
          ↓
    explicit morphology measurements
          ↓
    135-dimensional morphology representation
          ↓
    intrinsic morphology space
          ↓
    geometric organization
          ↓
    density organization
          ↓
    regional morphology profiles

Geometry is explicitly represented and then studied as the scientific
object.

---

# 8. The key distinction

The important difference is NOT:

    Sketch-a-Net has no geometry
    vs.
    CLO-SKET has geometry

That would be incorrect.

Sketch-a-Net clearly learns useful geometry-related visual structure.

The defensible distinction is:

> Sketch-a-Net learns a task-oriented visual representation from image
> pixels for sketch recognition, whereas CLO-SKET constructs an explicit
> quantitative morphology representation and investigates its
> population-level geometric organization independently of a recognition
> objective.

This distinction concerns the **scientific object and objective**, not
whether either method contains geometric information.

---

# 9. Relationship to our scientific gap

Prior work such as Sketch-a-Net demonstrates that sketch images contain
learnable visual and sequential structure.

However, this does not answer our Paper I question:

> Does explicit morphology measurement of complete garment sketches
> exhibit reproducible population-level quantitative organization before
> semantic categories or downstream recognition objectives are imposed?

CLO-SKET addresses this different question.

---

# 10. Reviewer-2 threat

A reviewer could reasonably say:

> "Sketch-a-Net already demonstrates that sketches contain structured
> geometric information."

Our response:

Correct.

We therefore do NOT claim that CLO-SKET is the first demonstration that
sketches contain structure.

Our distinction is that CLO-SKET investigates the **organization of an
explicit morphology representation itself**, rather than learning a
representation primarily for recognition.

---

# 11. What we can safely say in the paper

### SAFE

> Previous work has demonstrated that sketch-specific visual
> representations can exploit spatial and stroke-order information for
> recognition.

### SAFE

> Learned sketch representations provide evidence that free-hand
> sketches contain structured visual information that can be captured
> computationally.

### SAFE

> Our approach differs by explicitly constructing quantitative
> morphology measurements and examining their population-level geometric
> organization without a semantic recognition objective.

### DO NOT SAY

> Sketch-a-Net did not study sketch structure.

### DO NOT SAY

> Sketch-a-Net did not use geometry.

### DO NOT SAY

> CLO-SKET is the first method to represent geometry in fashion sketches.

### DO NOT SAY

> Sketch-a-Net discovered no meaningful structure.

---

# 12. Literature Matrix Entry

| Dimension | Sketch-a-Net | CLO-SKET |
|---|---|---|
| Primary objective | Sketch recognition | Quantitative morphology characterization |
| Input | Sketch images | Garment sketch images |
| Representation | Learned CNN features | Explicit morphology measurements |
| Feature construction | Learned from pixels | Explicitly defined morphology measurements |
| Stroke order | Explicitly encoded | Not the primary representation mechanism |
| Multi-scale analysis | Multiple CNN scales | Empirical morphology density scales |
| Bayesian component | Prediction fusion | Not used |
| Semantic labels | Recognition supervision | Not used in morphology discovery |
| Population-level morphology geometry | Not the primary objective | Central objective |
| Density organization | Not established | Investigated |
| Regional morphology profiles | Not established | Investigated |
| Cross-scale profile reproducibility | Not established | Tested |
| Semantic primitives | Not established | Not established |
| Morphology categories | Not established | Not established |
| Morphology grammar | Not established | Not established |
| Mathematical manifold | Not established | Not established |

---

# 13. Final Scientific Position

### Sketch-a-Net establishes:

    sketches
        ↓
    contain learnable visual structure
        ↓
    useful for recognition

### CLO-SKET investigates:

    explicit morphology measurements
        ↓
    quantitative morphology space
        ↓
    geometric organization
        ↓
    recurring density organization
        ↓
    regional quantitative profiles
        ↓
    cross-scale reproducibility

Therefore:

> **Sketch-a-Net provides evidence that sketch structure can be learned
> from pixels; CLO-SKET investigates the quantitative organization of
> explicitly measured morphology itself.**

---

## STATUS

**Paper 1 — Sketch-a-Net**

- Literature understanding: **LOCKED**
- Representation distinction: **LOCKED**
- Scientific overlap: **ACKNOWLEDGED**
- Novelty claim: **NARROWED**
- Reviewer-2 threat: **ADDRESSED**
- Semantic primitive claim: **NOT MADE**
- Category claim: **NOT MADE**
- Grammar claim: **NOT MADE**
- Manifold claim: **NOT MADE**

🔒 **PAPER 1 FROZEN**

**Next: Paper 2 — Abstracting Sketches through Simple Primitives**