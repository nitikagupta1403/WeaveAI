# CLO-SKET — Research Question

## Working Scientific Question

Can garment sketches be characterized as occupying a structured
quantitative morphology space, using explicit image-derived
measurements without semantic supervision?

## Secondary Question

Does an independently derived radial–angular geometric
representation exhibit reproducible correspondence with the
quantitative morphology representation and provide complementary
information beyond it?

---

# Primary Research Question

Do garment sketches exhibit reproducible quantitative morphology
organization that can be characterized directly from explicit
image-derived morphology measurements without predefined semantic
categories?

---

# Secondary Research Question

Does an independently derived radial–angular representation capture
geometric structure that is:

1. reproducibly associated with the 135-D morphology representation;
2. recoverable from morphology at the sketch level; and
3. complementary to morphology in a downstream discrimination task?

---

# Scientific Scope

This study concerns:

- quantitative morphology of garment sketches;
- explicit image-derived morphology measurements;
- geometric organization of the resulting representation;
- radial–angular geometric representation;
- cross-representation correspondence;
- downstream complementary utility.

This study does NOT attempt to establish:

- semantic garment-part recognition;
- universal morphology categories;
- semantic morphology primitives;
- a compositional morphology grammar;
- a mathematical manifold;
- causal mechanisms;
- information-theoretic independence;
- human-like visual understanding.

---

# Primary Representation

The canonical morphology representation contains 135 dimensions:

- 64 horizontal occupancy measurements;
- 64 vertical occupancy measurements;
- 7 global geometric descriptors.

The representation is constructed directly from canonicalized
64 × 64 sketch images.

No semantic category labels are used in construction of the
representation.

---

# Radial–Angular Representation

An independently derived 28-dimensional radial–angular representation
is evaluated as a complementary geometric description.

The 28 dimensions comprise five descriptor blocks:

- F₂ radial descriptors: 9
- α₂ descriptors: 7
- observed circular descriptors: 3
- learned circular descriptors: 4
- relational descriptors: 5

Total:

9 + 7 + 3 + 4 + 5 = 28 dimensions.

The 28-D representation is not claimed to be uniquely optimal or
universally sufficient.

---

# Evidence Strategy

The study separates the following questions:

## 1. Morphology organization

Does the 135-D representation exhibit reproducible quantitative
organization?

## 2. Cross-branch association

Is the radial–angular representation statistically associated
with the morphology representation?

## 3. Cross-branch correspondence

Does morphology recover radial–angular measurements at the
individual-sketch level?

## 4. Complementarity

Does adding radial–angular geometry improve downstream
discrimination beyond morphology alone?

## 5. Dimensionality control

Can the downstream improvement be explained simply by adding
more dimensions?

## 6. Descriptor ablation

Is the observed utility confined to a single radial–angular
descriptor block?

---

# Core Scientific Claim

The study aims to establish an empirical quantitative geometric
layer for garment sketches.

The radial–angular branch is treated as an independently derived
geometric representation that provides complementary information
under the tested downstream task.

The study does not interpret either representation as a semantic
language by itself.

---

# Claim Discipline

Every manuscript claim must be traceable to:

    CLAIM
        ↓
    EXPERIMENT
        ↓
    NUMERICAL EVIDENCE
        ↓
    CONTROL
        ↓
    CLAIM BOUNDARY

No claim should exceed the evidence produced by the corresponding
analysis.