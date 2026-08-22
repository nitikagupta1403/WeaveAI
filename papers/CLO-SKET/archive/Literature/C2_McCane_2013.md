# C2 — McCane (2013)

## Shape Variation in Outline Shapes

**Cluster:** C — Quantitative Shape & Morphology  
**Role:** Population-level outline shape representation  
**FOMO Status:** Very Strong Methodological Bridge  
**Application domain:** Biological / morphological shape analysis

---

## 1. Purpose

McCane (2013) addresses the problem of representing and analysing **shape variation in populations of outlines**.

The central question is:

> How can variation among curved outlines be quantified without requiring the outline to be represented by a fixed set of discrete points?

The paper develops an outline-shape distance based on a Procrustes-style framework and uses the resulting distances to construct a low-dimensional Euclidean representation of outline shape variation.

The conceptual transition is:

\[
\boxed{
\text{individual outline}
\rightarrow
\text{shape distance}
\rightarrow
\text{population shape space}
}
\]

This makes the paper substantially closer to CLO-SKET than a method concerned only with extracting features from individual outlines.

---

# 2. Scientific Question

The paper asks how to represent **variation among outline shapes** in a way that permits statistical analysis and visualization.

Rather than asking:

> Which point on outline A corresponds to which point on outline B?

the approach asks:

> **How different are the two complete outlines as shapes?**

Thus the fundamental object becomes:

\[
\boxed{
d(A,B)
}
\]

where \(A\) and \(B\) are complete outlines.

The scientific objective is therefore to construct a meaningful geometry for a population of outlines.

---

# 3. Input

The input is a set of **closed outline shapes**.

For a population:

\[
S_1,S_2,\ldots,S_N
\]

each \(S_i\) represents one complete outline.

The method is designed to operate on the outlines themselves rather than requiring the user to identify a fixed set of biologically corresponding discrete points along every curve.

Therefore:

\[
\boxed{
\text{Input}=\text{population of outlines}
}
\]

---

# 4. The Core Problem

Traditional landmark-based morphometrics requires corresponding landmarks.

For an outline, however, there may be no obvious intrinsic landmarks.

A simple solution would be to sample the outline at a fixed number of points:

\[
S_i
\rightarrow
\{p_{i1},p_{i2},\ldots,p_{im}\}
\]

and compare the corresponding points.

But this introduces a discretisation/correspondence problem.

The sampled points are not necessarily meaningful morphological landmarks.

Therefore:

\[
\boxed{
\text{point correspondence}
\neq
\text{necessarily meaningful shape correspondence}
}
\]

McCane instead focuses on the distance between the **whole outlines**.

---

# 5. Continuous Outline → Shape Distance

Consider two continuous outlines:

\[
A(s),\qquad B(s)
\]

where

\[
s\in[0,1]
\]

parameterizes movement around the boundary.

Rather than immediately converting each curve into a fixed vector of sampled coordinates, the method defines a distance between the complete shapes.

Conceptually:

\[
\boxed{
A(s),B(s)
\rightarrow
d(A,B)
}
\]

The output is a scalar:

\[
d(A,B)\geq0
\]

representing their morphological difference under the chosen shape metric.

This is the key conceptual move.

---

# 6. Why This Is Different from Simple Discretisation

It is important not to describe the method as simply:

\[
\text{continuous outline}
\rightarrow
\text{sampled points}
\rightarrow
\text{distribution}
\]

That is not the central idea.

Instead:

\[
\boxed{
\text{continuous outline}
\rightarrow
\text{whole-outline distance}
}
\]

The method therefore shifts the representation from **individual boundary coordinates** toward **relationships between complete shapes**.

The important object becomes:

\[
\boxed{
d(S_i,S_j)
}
\]

rather than an individual boundary coordinate.

---

# 7. Pairwise Distance Matrix

For a population of \(N\) outlines, pairwise distances can be calculated:

\[
d_{ij}=d(S_i,S_j)
\]

giving the distance matrix:

\[
\boxed{
D=
\begin{bmatrix}
0 & d_{12} & d_{13} & \cdots\\
d_{21} & 0 & d_{23} & \cdots\\
\vdots & \vdots & \ddots & \vdots\\
d_{N1} & d_{N2} & \cdots & 0
\end{bmatrix}
}
\]

This matrix describes the **geometry of the population of outlines**.

For example:

\[
d_{12}=0.10
\]

means outlines 1 and 2 are relatively similar under the chosen metric.

While:

\[
d_{17}=0.85
\]

would indicate substantially greater shape difference.

The important point is that the representation is now population-level:

\[
\boxed{
\text{individual outlines}
\rightarrow
\text{pairwise shape relationships}
}
\]

---

# 8. From Distances to Shape Space

The pairwise distances can then be embedded into a low-dimensional Euclidean space.

Conceptually:

\[
D
\rightarrow
\boxed{
\text{Euclidean embedding}
}
\]

giving coordinates such as:

\[
S_i
\rightarrow
(z_{i1},z_{i2},\ldots,z_{ik})
\]

where \(k\) is much smaller than the original description of the outline.

Thus:

\[
\boxed{
\text{outline}
\rightarrow
\text{shape-space coordinates}
}
\]

The resulting coordinates provide a way to visualize and analyse the population's shape variation.

---

# 9. Mean Shape

Once the outlines have been represented in a common shape space, the population can be summarized.

A mean shape can be estimated conceptually as:

\[
\boxed{
\bar S
=
\text{central tendency of the outline population}
}
\]

The important idea is that the mean is defined in **shape space**, rather than simply averaging unrelated raw image pixels or arbitrary boundary coordinates.

This allows the population to be summarized in terms of its central morphology.

---

# 10. Principal Shape Variation

The low-dimensional representation also permits analysis of the dominant directions of shape variation.

Conceptually:

\[
\boxed{
\text{shape-space coordinates}
\rightarrow
\text{principal variation axes}
}
\]

The first principal direction describes the largest systematic pattern of variation.

The second describes the next largest independent pattern, and so on.

Thus a population can be interpreted as:

\[
\boxed{
\text{mean shape}
+
\text{major directions of shape variation}
}
\]

This is an important transition from simply comparing individual shapes to studying **morphological organization across a population**.

---

# 11. Relationship to Procrustes Analysis

McCane builds on the idea of Procrustes shape distance.

Classical Procrustes analysis seeks to separate shape from nuisance transformations such as:

- translation,
- rotation,
- scale.

The general conceptual goal is:

\[
\boxed{
\text{observed configuration}
\rightarrow
\text{remove non-shape transformations}
\rightarrow
\text{compare shape}
}
\]

McCane extends this idea to outline shapes without requiring a fixed set of discrete points sampled along the outline.

This is a major methodological distinction from conventional landmark-based approaches.

---

# 12. Relationship to Bookstein (1997)

The relationship between C1 and C2 is important.

### Bookstein

Bookstein addresses:

> How can an outline without conventional landmarks be represented through semi-landmarks and analysed morphometrically?

Conceptually:

\[
\boxed{
\text{outline}
\rightarrow
\text{semi-landmarks}
\rightarrow
\text{correspondence}
\rightarrow
\text{shape analysis}
}
\]

### McCane

McCane shifts the focus toward:

> How can complete outlines be compared directly and their population-level variation represented?

Conceptually:

\[
\boxed{
\text{outline}
\rightarrow
\text{outline distance}
\rightarrow
\text{shape space}
\rightarrow
\text{population variation}
}
\]

Therefore:

\[
\boxed{
\text{Bookstein}
=
\text{correspondence problem}
}
\]

while:

\[
\boxed{
\text{McCane}
=
\text{population outline-distance problem}
}
\]

This makes McCane a particularly important methodological bridge toward CLO-SKET.

---

# 13. What Is Actually Represented?

The central representation is not simply a list of boundary values.

It is the **geometry of relationships among complete outlines**.

For two shapes:

\[
A,B
\]

the representation asks:

\[
\boxed{
\text{How far apart are }A\text{ and }B\text{ in shape?}
}
\]

For a population:

\[
S_1,\ldots,S_N
\]

the collection of pairwise distances defines a shape-space geometry.

Thus:

\[
\boxed{
\text{boundary geometry}
\rightarrow
\text{pairwise shape relationships}
\rightarrow
\text{population geometry}
}
\]

---

# 14. Is This a Probability Distribution?

No.

This distinction is important.

The outline is not converted into a probability density over boundary values.

Instead, McCane constructs a **distance geometry**.

The central object is:

\[
\boxed{
d(S_i,S_j)
}
\]

not:

\[
p(x)
\]

Therefore:

\[
\boxed{
\text{shape distribution}
\neq
\text{probability distribution of boundary values}
}
\]

The population can certainly have a statistical distribution **within the resulting shape space**, but the underlying representation is geometric rather than probabilistic.

---

# 15. What Does the Method Learn?

The representation is not an end-to-end learned neural representation.

The outline distance is mathematically defined.

Then the population geometry is constructed from the pairwise distances.

Therefore:

\[
\boxed{
\text{analytic shape metric}
\rightarrow
\text{distance matrix}
\rightarrow
\text{shape-space representation}
}
\]

This is an example of:

\[
\boxed{
\text{mathematical representation}
+
\text{statistical analysis}
}
\]

rather than deep representation learning.

---

# 16. Comparison with Semilandmarks

A major motivation is avoiding some of the problems associated with discretizing an outline into a fixed set of semi-landmarks.

A semi-landmark method requires decisions about:

- number of points,
- point placement,
- correspondence,
- sliding.

McCane's approach instead works with the outline as a complete shape and derives distances between complete outlines.

Thus:

\[
\boxed{
\text{semi-landmark approach}
\rightarrow
\text{explicit point correspondence}
}
\]

versus:

\[
\boxed{
\text{McCane}
\rightarrow
\text{whole-outline distance}
}
\]

This does not mean that McCane eliminates all assumptions.

The chosen shape distance itself becomes a crucial modelling decision.

---

# 17. Critical Limitation

This is one of the most important findings for FOMO.

A mathematically valid distance between outlines does not automatically mean that the distance is **scientifically meaningful for the biological question**.

The suitability of an outline distance depends on whether it captures the aspects of shape that are actually relevant to the scientific problem.

Therefore:

\[
\boxed{
\text{mathematical distance}
\neq
\text{automatically meaningful morphology}
}
\]

This connects directly with the lesson from Bookstein:

\[
\boxed{
\text{representation validity}
\neq
\text{semantic/morphological validity}
}
\]

The metric must be evaluated in the context of the scientific question.

---

# 18. What McCane Establishes

The paper establishes an important general methodological capability:

\[
\boxed{
\text{population of outlines}
\rightarrow
\text{pairwise shape distances}
\rightarrow
\text{low-dimensional shape space}
\rightarrow
\text{shape variation}
}
\]

This demonstrates that a population of outlines can be analysed without requiring every outline to be represented by an explicitly corresponding set of discrete points.

The paper therefore provides a strong precedent for **population-level outline morphology**.

---

# 19. What McCane Does NOT Establish

McCane does not establish:

- garment-specific morphology,
- fashion-sketch semantics,
- garment primitives,
- garment construction relationships,
- fashion style ontology,
- semantic meaning of garment dimensions,
- an explicit garment measurement vector,
- independent garment representations,
- correspondence between two independently constructed garment representations.

The method is a general outline-shape framework applied in biological/morphological contexts.

Therefore:

\[
\boxed{
\text{McCane}
\neq
\text{fashion morphology}
}
\]

but:

\[
\boxed{
\text{McCane}
=
\text{strong population-outline morphology precedent}
}
\]

---

# 20. McCane vs. An & Li

The distinction between these papers is important.

### An & Li (2014)

\[
\boxed{
\text{fashion contour}
\rightarrow
\text{WFD}
\rightarrow
\text{classification}
}
\]

The objective is:

\[
\boxed{
\text{class discrimination}
}
\]

### McCane (2013)

\[
\boxed{
\text{outline population}
\rightarrow
\text{shape distance}
\rightarrow
\text{shape space}
\rightarrow
\text{variation}
}
\]

The objective is:

\[
\boxed{
\text{population shape analysis}
}
\]

Thus:

\[
\boxed{
\text{An \& Li}
=
\text{shape as classification feature}
}
\]

while:

\[
\boxed{
\text{McCane}
=
\text{shape as population object of study}
}
\]

---

# 21. McCane vs. CLO-SKET

This is the critical FOMO comparison.

### McCane

The representation is:

\[
\boxed{
d(S_i,S_j)
}
\]

between complete outlines.

The population is represented through:

\[
\boxed{
D_{ij}=d(S_i,S_j)
}
\]

and subsequently embedded into shape space.

### CLO-SKET

The primary representation is an explicit garment morphology vector:

\[
\boxed{
\mathbf{x}_i\in\mathbb{R}^{135}
}
\]

for each sketch.

Across the population:

\[
\boxed{
\mathbf X\in\mathbb{R}^{2300\times135}
}
\]

An independently constructed radial-angular representation provides:

\[
\boxed{
\mathbf r_i\in\mathbb{R}^{28}
}
\]

and:

\[
\boxed{
\mathbf R\in\mathbb{R}^{2300\times28}.
}
\]

The scientific question then includes whether corresponding sketches occupy related positions in the two representations.

Therefore:

\[
\boxed{
\text{McCane}
=
\text{population geometry of outlines}
}
\]

while:

\[
\boxed{
\text{CLO-SKET}
=
\text{interpretable garment morphology + independent representation correspondence}
}
\]

---

# 22. Scientific Positioning

McCane closes an important gap in the earlier literature chain.

The progression is now:

\[
\boxed{
\text{Bookstein 1997}
}
\]

Can an outline without landmarks become a quantitative shape object?

\[
\downarrow
\]

\[
\boxed{
\text{McCane 2013}
}
\]

Can a population of outlines be represented through pairwise shape distances and a low-dimensional shape space?

\[
\downarrow
\]

\[
\boxed{
\text{CLO-SKET}
}
\]

Can explicit garment-specific geometry provide an interpretable morphology representation whose population structure is independently supported?

This is the correct methodological lineage.

---

# 23. FOMO Takeaway

McCane prevents us from making another overly broad novelty claim.

We cannot claim:

> "CLO-SKET is the first work to study population-level variation in outline shapes."

That would be incorrect.

McCane already establishes a framework for:

\[
\boxed{
\text{outline population}
\rightarrow
\text{shape distances}
\rightarrow
\text{shape space}
\rightarrow
\text{variation}
}
\]

The defensible distinction is instead:

> **Prior outline-morphology research has developed methods for representing populations of outlines through pairwise shape distances and low-dimensional shape spaces. CLO-SKET applies a different representation philosophy to garment sketches by explicitly defining garment-specific geometric measurements and testing whether their population-level organization is supported by an independently constructed representation.**

Therefore the novelty cannot simply be:

\[
\boxed{
\text{"population shape space"}
}
\]

It must lie in the **garment-specific representation, interpretability, and evidence for correspondence between independent representations**.

---

# 24. Reviewer-Proof Classification

**Literature category**

\[
\boxed{
\text{Quantitative outline morphology / population shape analysis}
}
\]

**Primary input**

\[
\boxed{
\text{Population of outlines}
}
\]

**Primary representation**

\[
\boxed{
\text{Whole-outline shape distance}
}
\]

**Population representation**

\[
\boxed{
\text{Pairwise distance matrix}
}
\]

**Dimensionality reduction / embedding**

\[
\boxed{
\text{Low-dimensional Euclidean shape space}
}
\]

**Primary scientific objective**

\[
\boxed{
\text{Population-level outline shape variation}
}
\]

**Explicit garment-semantic coordinates**

\[
\boxed{
\text{No}
}
\]

**Fashion-specific**

\[
\boxed{
\text{No}
}
\]

**Independent-representation correspondence**

\[
\boxed{
\text{No}
}
\]

**Direct CLO-SKET competitor**

\[
\boxed{
\text{No}
}
\]

**Methodological relevance**

\[
\boxed{
\textbf{Very High}
}
\]

**FOMO role**

\[
\boxed{
\textbf{Strong population-morphology precedent}
}
\]

---

# 25. Final Finding

McCane (2013) extends quantitative outline analysis from the problem of representing individual curves toward the problem of characterizing **variation across populations of outlines**.

Its key conceptual contribution is to treat the complete outline as the object of comparison, construct pairwise outline-shape distances, and use those distances to obtain a low-dimensional representation of population shape variation.

Thus:

\[
\boxed{
\text{outline}
\rightarrow
\text{distance}
\rightarrow
\text{shape space}
\rightarrow
\text{population variation}
}
\]

For CLO-SKET, this is a major methodological precedent, but it does not provide a garment-specific or semantically interpretable representation.

---

# Final One-Sentence Understanding

> **McCane (2013) develops a framework for representing population-level variation in outline shapes by defining distances between complete outlines and embedding those distances into a low-dimensional shape space, thereby shifting analysis from arbitrary point correspondence toward whole-shape relationships; CLO-SKET differs by constructing explicit garment-specific morphology coordinates and testing whether their population structure is independently reflected in a second representation.**

---

## 🔒 C2 Status

**McCane (2013) — LOCKED**

\[
\boxed{
\textbf{C2 = Population outline-shape variation}
}
\]

\[
\boxed{
\textbf{FOMO relevance = VERY HIGH}
}
\]

\[
\boxed{
\textbf{Direct fashion precedent = NO}
}
\]

\[
\boxed{
\textbf{Methodological bridge to CLO-SKET = YES}
}