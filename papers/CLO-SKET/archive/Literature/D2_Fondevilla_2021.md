# D2 — Fondevilla et al. (2021)

## Fashion Transfer: Dressing 3D Characters from Stylized Fashion Sketches

**Authors:** A. Fondevilla, D. Rohmer, S. Hahmann, A. Bousseau, M.-P. Cani  
**Venue:** Computer Graphics Forum, 2021  
**Domain:** Computer Graphics / Fashion Sketch Understanding / Geometric Garment Representation

---

## 1. Purpose

The purpose of this paper is to extract geometrically meaningful garment-style information from a **single stylized fashion sketch** and use that information to generate a corresponding 3D garment on characters with different poses and morphologies.

The paper treats garment style as a set of geometric characteristics that can be extracted directly from a 2D sketch:

1. **Proportionality** — relative position of the garment with respect to the body and limbs.
2. **Fit** — whether the garment is tight or loose around the body.
3. **Overall shape** — represented through silhouette-derived surface-normal information.
4. **Fold patterns** — geometric representation of folds visible in the sketch.

The central idea is therefore:

\[
\boxed{
\text{2D fashion sketch}
\rightarrow
\text{geometric style features}
\rightarrow
\text{3D garment}
}
\]

The authors explicitly distinguish their work from conventional 3D style transfer: the source style is represented by a **2D drawing**, rather than by a complete 3D garment surface.

---

## 2. Design / Methodology / Approach

### 2.1 Input

The system takes:

- a stylized fashion sketch;
- user annotations of relevant garment structures.

The annotations include:

- garment silhouette;
- free borders of loose parts;
- skeletal bones of the character.

These annotations provide the geometric information required for reconstruction.

---

### 2.2 Geometric Style Representation

The paper decomposes garment style into four explicit geometric components:

\[
\boxed{
S =
\{
P,\;F,\;G,\;D
\}
}
\]

where:

- \(P\) = proportionality;
- \(F\) = fit;
- \(G\) = overall garment shape;
- \(D\) = fold structure.

This is an **explicit geometric representation**, rather than a learned neural embedding.

---

### 2.3 Proportionality

The skeletal annotations provide information about the relationship between the garment and the character's body.

The system therefore represents where garment boundaries occur relative to:

- limbs;
- body;
- skeletal directions.

This allows the garment representation to be transferred to characters with different morphologies.

---

### 2.4 Fit

Garment regions are annotated as **tight or loose**.

This affects how the garment surface is constructed around the body.

Conceptually:

\[
\text{sketch region}
\rightarrow
\text{tight/loose constraint}
\rightarrow
\text{surface behaviour}
\]

A loose region follows the silhouette information from the sketch, whereas a tight region follows the underlying body surface more closely.

---

### 2.5 Overall Shape / Silhouette

The silhouette provides information about the orientation of the garment surface.

The paper therefore does not treat the silhouette merely as a binary boundary.

Instead:

\[
\boxed{
\text{silhouette}
\rightarrow
\text{surface-normal information}
\rightarrow
\text{3D garment shape}
}
\]

Garment patches surrounding limbs are represented using **generalized cylinders**, incorporating proportions and silhouette-normal information extracted from the sketch.

---

### 2.6 Fold Representation

Fold patterns are separately extracted from the sketch.

The method reconstructs fold information while accounting for:

- perspective distortion;
- occlusion;
- garment geometry.

The fold representation is then normalized so that it can be transferred to garments of different sizes.

The paper allows different fold-transfer strategies, including:

- preserving the number of folds;
- preserving fold frequency and magnitude.

Thus:

\[
\text{2D fold pattern}
\rightarrow
\text{normalized fold representation}
\rightarrow
\text{transfer to target garment}
\]

---

### 2.7 3D Garment Construction

The geometric information extracted from the sketch is converted into a parametric garment representation.

Garment patches are represented using:

\[
\boxed{\text{parametric cubic Bézier patches}}
\]

These patches are parameterized along limb directions.

The resulting garment can then be adapted to target characters with different:

- poses;
- body morphologies;
- proportions.

---

### 2.8 Final Pipeline

The complete conceptual pipeline is:

```text
Stylized Fashion Sketch
        ↓
User Annotations
        ↓
────────────────────────────────
│                              │
├── Skeleton → proportionality │
├── Tight/loose → fit          │
├── Silhouette → surface shape │
└── Folds → fold representation│
────────────────────────────────
        ↓
Geometric garment representation
        ↓
Parametric 3D garment patches
        ↓
Adaptation to target morphology
        ↓
Fold transfer
        ↓
3D garment