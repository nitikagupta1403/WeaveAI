# CLO-SKET — Introduction

## Title

# Understanding Garment Sketch Morphology

---

## Paragraph 1 — The Object of Study

Garment sketches are compact visual representations of garment form before it is physically realized. Their lines, silhouettes, proportions, and spatial arrangements convey substantial information about garment form, yet a sketch is not simply a reduced photograph of a garment: it is an abstract geometric representation in which design intent is expressed through shape and spatial structure. This makes garment sketches an important object for computational study—not only for recognizing or generating garments, but also for asking a more basic question: how is garment morphology quantitatively organized within a population of sketches?

---

## Paragraph 2 — The Representation Problem

Computational work involving garment sketches has addressed a range of task-oriented problems, including sketch-based garment modeling, transfer of garment style from sketches, shape analysis, recognition, and more recent sketch-to-fashion generation. These studies demonstrate that sketch geometry can support computational interpretation and downstream visual tasks. However, the question addressed here is narrower and more fundamental: rather than asking only what a sketch can be used to predict, model, or generate, can the morphology expressed in garment sketches itself be represented explicitly and studied as a quantitatively organized population?

---

## Paragraph 3 — From Individual Shape Cues to Population Structure

Individual geometric properties of fashion drawings can be measured and have been used to relate drawn form to garment dimensions or to support computational interpretation. What remains less clear is how such measurements behave when considered jointly across a population of sketches: whether they form reproducible patterns of variation, whether different geometric descriptions capture overlapping structure, and whether those descriptions contribute distinct information when evaluated together. This population-level view of garment morphology motivates the analysis developed in this study.

---

## Paragraph 4 — An Explicit Morphology Representation

To examine morphology as a population-level object, we represent each sketch using explicit image-derived measurements rather than beginning with a learned embedding. For sketch \(i\), the morphology representation is defined as

\[
\mathbf{x}_i =
\begin{bmatrix}
\mathbf{h}_i \\
\mathbf{v}_i \\
\mathbf{g}_i
\end{bmatrix}
\in \mathbb{R}^{135},
\]

where

\[
\mathbf{h}_i \in \mathbb{R}^{64},
\qquad
\mathbf{v}_i \in \mathbb{R}^{64},
\qquad
\mathbf{g}_i \in \mathbb{R}^{7}.
\]

Thus,

\[
64 + 64 + 7 = 135.
\]

The horizontal and vertical occupancy components describe how foreground structure is distributed along the two image axes, while the global descriptors capture broader geometric properties of the sketch. The coordinates therefore retain direct spatial meaning rather than representing an opaque learned embedding. The resulting matrix,

\[
\mathbf{X}
=
\begin{bmatrix}
\mathbf{x}_1^\top\\
\mathbf{x}_2^\top\\
\vdots\\
\mathbf{x}_{2300}^\top
\end{bmatrix}
\in \mathbb{R}^{2300\times135},
\]

provides an explicit quantitative space in which variation, neighborhood structure, and relationships between sketches can be measured directly.

---

## Paragraph 5 — An Independent Radial–Angular Description

Radial and angular coordinates provide an established way of describing geometric structure, and related coordinate systems have been used in clothing and garment analysis, including polar descriptions of garment patterns and distance–angle representations for clothing sketches. [CITATIONS — TO BE FINALIZED IN RELATED WORK] To examine whether the quantitative structure captured by the morphology representation depends on the particular coordinate system used, we construct a second geometric description of the same sketches using radial and angular measurements. For sketch \(i\), the radial–angular representation is defined as

\[
\mathbf{r}_i =
\begin{bmatrix}
\mathbf{f}_i \\
\boldsymbol{\alpha}_i \\
\mathbf{o}_i \\
\mathbf{l}_i \\
\mathbf{q}_i
\end{bmatrix}
\in \mathbb{R}^{28},
\]

where the predefined descriptor blocks have dimensions

\[
\mathbf{f}_i \in \mathbb{R}^{9},
\qquad
\boldsymbol{\alpha}_i \in \mathbb{R}^{7},
\qquad
\mathbf{o}_i \in \mathbb{R}^{3},
\qquad
\mathbf{l}_i \in \mathbb{R}^{4},
\qquad
\mathbf{q}_i \in \mathbb{R}^{5}.
\]

Consequently,

\[
9 + 7 + 3 + 4 + 5 = 28.
\]

The resulting radial–angular matrix is

\[
\mathbf{R}
=
\begin{bmatrix}
\mathbf{r}_1^\top\\
\mathbf{r}_2^\top\\
\vdots\\
\mathbf{r}_{2300}^\top
\end{bmatrix}
\in \mathbb{R}^{2300\times28}.
\]

The 28-dimensional representation is a predefined compact descriptor set used in this study, rather than an optimized or universal dimensionality for garment sketches. Its purpose is to provide an independently constructed geometric coordinate system whose relationship with the morphology representation can be evaluated empirically.

---

## Paragraph 6 — Testing Correspondence and Complementarity

The two representations are evaluated as alternative but potentially complementary descriptions of the same sketch population. For each sketch \(i\), the true cross-branch correspondence is

\[
\mathbf{x}_i
\longleftrightarrow
\mathbf{r}_i,
\]

whereas a row-permutation null replaces this correspondence with

\[
\mathbf{x}_i
\longleftrightarrow
\mathbf{r}_{\pi(i)},
\]

for a random permutation \(\pi\). We first examine whether individual morphology coordinates are associated with radial–angular measurements and whether radial–angular quantities can be recovered from morphology under cross-validation. We then test whether these relationships depend on the actual sketch-level correspondence between the two representations using row-permutation controls. Finally, we evaluate whether adding the radial–angular representation improves performance on an independent downstream discrimination task. If \(M(\cdot)\) denotes the downstream performance metric, the observed incremental utility is expressed as

\[
\Delta M
=
M(\mathbf{X},\mathbf{R})
-
M(\mathbf{X}).
\]

Dimension-matched and descriptor-level controls are then used to constrain the interpretation of any observed improvement.

---

## Paragraph 7 — Contributions

This study makes three main contributions. First, it provides an explicit quantitative representation of garment-sketch morphology and evaluates whether that representation exhibits reproducible population-level organization. Second, it introduces an independently constructed radial–angular description and evaluates its relationship with morphology through feature-wise association, cross-validated recovery, and permutation-based correspondence analysis. Third, it tests whether the radial–angular representation provides additional downstream utility beyond morphology and uses dimension-matched and descriptor-level controls to constrain the interpretation of that improvement. Together, these analyses provide an empirical framework for studying garment-sketch morphology as a quantitative geometric object without requiring claims of semantic interpretation.

---

# Introduction — Claim Boundary

The Introduction deliberately distinguishes between:

\[
\text{quantitative morphology}
\]

and

\[
\text{semantic interpretation}.
\]

The present study addresses the former.

It does not claim:

- semantic garment-part recognition;
- semantic novelty;
- a universal morphology vocabulary;
- a morphology grammar;
- a mathematical manifold;
- information-theoretic independence;
- causal mechanisms;
- human-like visual understanding.

The radial–angular representation is used as an independent geometric description for testing correspondence and downstream complementarity, not as evidence of semantic understanding by itself.

---

# Introduction — Scientific Logic

The complete argument is:

\[
\boxed{
\text{Garment Sketch}
\rightarrow
\text{Explicit Morphology}
\rightarrow
\text{Population Structure}
}
\]

followed by

\[
\boxed{
\text{Morphology}
\leftrightarrow
\text{Radial--Angular Geometry}
}
\]

and finally

\[
\boxed{
\text{Morphology}
+
\text{Radial--Angular Geometry}
\rightarrow
\text{Downstream Utility}
}
\]

with the corresponding controls:

\[
\text{Permutation Null}
\qquad
\text{Dimension-Matched Control}
\qquad
\text{Descriptor Ablation}.
\]

The manuscript therefore treats morphology as a measurable geometric object and evaluates the relationship between alternative representations empirically rather than assuming semantic structure in advance.