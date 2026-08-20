# Kamat et al. (2025) — CloSE: A Compact Shape- and Orientation-Agnostic Cloth State Representation

## Citation

**Kamat, J., Borràs, J., & Torras, C. (2025)**

*CloSE: A Compact Shape- and Orientation-Agnostic Cloth State Representation*

### Role in CLO-SKET Literature Review

This paper represents a **geometric/topological cloth-state representation approach**.

Its central contribution is not to learn garment morphology from sketches, but to transform **physical cloth-boundary geometry and its dGLI measurements** into a compact, continuous representation of cloth folding state.

The paper explicitly builds on the dGLI work of Coltraro et al. and introduces a new organization of those measurements—the **dGLI disk**—followed by the **CloSE representation**.

---

# 1. Scientific Question

The central question is:

> **How can the deformation state of a non-rigid cloth be represented compactly and continuously in a way that is general across different cloth shapes, sizes, and poses?**

The overall direction is:

[
\boxed{
\text{Cloth boundary geometry}
\rightarrow
\text{dGLI disk}
\rightarrow
\text{CloSE}
\rightarrow
\text{cloth-state semantics / planning}
}
]

The paper therefore treats the **physical cloth state** as the object of representation, rather than treating a visual sketch as the object of morphological analysis.

---

# 2. Input

The input is the **boundary of a cloth mesh**.

The authors calculate dGLI values between segments along the cloth boundary and arrange these measurements on a circular grid.

The important information is therefore:

[
\boxed{
\text{cloth-border geometry}
}
]

rather than:

[
\boxed{
\text{fashion sketch pixels}
}
]

The representation is derived from the geometry/topology of the physical cloth border.

---

# 3. The Core Problem

Cloth has an extremely large configuration space because it can deform in many ways.

A complete mesh contains a large number of degrees of freedom, while a robot may only need a much smaller amount of information to reason about the cloth state.

Existing approaches can use:

* full cloth meshes,
* simplified geometric silhouettes,
* RGB/RGB-D observations,
* learned representations.

The problem is therefore:

> **How can the relevant structure of a deformable cloth state be represented using a small number of meaningful, shape-independent coordinates?**

The authors build on the earlier dGLI representation and observe that its pairwise measurements contain more structured information than is apparent in matrix form.

---

# 4. dGLI as the Starting Representation

Paper 3 introduced the directional derivative of the Gauss Linking Integral:

[
dGLI.
]

For boundary segments (S_i,S_j), the resulting pairwise measurements can be organized as:

[
dGLI(S_i,S_j).
]

CloSE does **not** replace this mathematical foundation.

Instead:

[
\boxed{
\text{Paper 3: dGLI}
\rightarrow
\text{Paper 4: new organization of dGLI}
}
]

The authors' first major step is therefore to reorganize these pairwise measurements into a circular structure.

---

# 5. The dGLI Disk

The first new representation proposed by CloSE is the:

[
\boxed{\text{dGLI disk}}
]

Instead of storing the dGLI values in an ordinary matrix, the values are arranged on a **circular grid**.

The resulting heat-map reveals patterns that correspond to meaningful characteristics of the cloth state.

In particular, the authors identify patterns associated with:

* cloth corners,
* fold locations,
* other state-dependent structures.

Importantly, these patterns remain recognizable across different cloth shapes, sizes, and positions.

Thus:

[
\boxed{
\text{dGLI matrix}
\rightarrow
\text{circular arrangement}
\rightarrow
\text{visible geometric structure}
}
]

is one of the principal contributions of the paper.

---

# 6. What the dGLI Disk Reveals

The dGLI disk contains information at more than one level.

### Persistent boundary structure

The disk contains patterns corresponding to the corners of the unfolded cloth.

These patterns are associated with the **shape of the cloth boundary**.

### State-dependent structure

Folding produces additional changes in the dGLI representation.

The difference between the dGLI disk before and after a folding action can therefore expose information about the fold.

Conceptually:

[
\boxed{
\text{dGLI disk}_{initial}
\rightarrow
\text{persistent structure}
}
]

and

[
\boxed{
\text{dGLI disk}_{final}
------------------------

\text{dGLI disk}_{initial}
\rightarrow
\text{fold structure}
}
]

The authors then extract these structures to construct the final CloSE representation.

---

# 7. From dGLI Disk to CloSE

The second representation is the:

[
\boxed{\text{Cloth StatE (CloSE)}}
]

The authors abstract the important geometric features of the dGLI disk onto a circle.

For a cloth with (n) corners, the representation is:

[
\boxed{
CloSE=((v_1,\ldots,v_n),(f_1,f_2))
}
]

where:

[
v_i\in[0,2\pi)
]

represent the ordered corner locations, and

[
f_1,f_2\in[0,2\pi)
]

represent the two locations where the fold intersects the cloth boundary.

Thus the representation explicitly stores:

[
\boxed{
\text{corner locations}
+
\text{fold locations}
}
]

and, through their ordering, information about fold orientation.

---

# 8. How the Fold Is Extracted

The authors use the difference between dGLI disks corresponding to the initial and folded configurations.

Conceptually:

[
\boxed{
D_{\Delta}
==========

## D_{\text{folded}}

D_{\text{initial}}
}
]

The changed region is then processed using simple computational methods including:

* clustering,
* curve fitting.

The resulting fitted structure provides the fold coordinates:

[
f_1,\ f_2.
]

The pipeline is therefore:

[
\boxed{
\text{dGLI disks}
\rightarrow
\text{difference}
\rightarrow
\text{selected points}
\rightarrow
\text{curve fitting}
\rightarrow
(f_1,f_2)
}
]

The key point is that the authors are **extracting interpretable geometric coordinates from the dGLI field**, rather than learning a latent representation from images.

---

# 9. Semantic Interpretation of CloSE

The representation has a direct geometric interpretation.

The corner coordinates are ordered around the cloth boundary:

[
v_1 < v_2 < \cdots < v_n.
]

Each fold defines an interval on the circle between:

[
f_1
\quad\text{and}\quad
f_2.
]

The corners lying inside that interval correspond to the folded corners.

Therefore:

[
\boxed{
\text{circular interval}
\rightarrow
\text{folded-corner identity}
}
]

Furthermore, each fold coordinate lies between two neighboring corner coordinates:

[
v_j < f_i < v_{j+1}.
]

Its position relative to those neighboring corners provides information about **where along the corresponding edge the fold occurs**.

---

# 10. What Semantic Information Can Be Derived?

The authors show that simple reasoning over the CloSE coordinates can identify properties such as:

* which corners are folded,
* which edges are involved,
* where the fold lies along an edge,
* whether a fold is symmetric,
* whether corresponding edges have been folded by similar proportions.

Thus the representation has a direct mapping:

[
\boxed{
\text{geometric coordinates}
\rightarrow
\text{semantic cloth state}
}
]

This is an important characteristic of the work.

The semantics are not discovered through a learned language model; they follow from the **known geometric interpretation of the coordinates**.

---

# 11. Is the Mathematics Invented by the Paper?

**Partly, but the distinction is important.**

The paper does **not** invent the Gauss Linking Integral or the dGLI.

Those come from the preceding mathematical framework.

Its contribution is instead the new representational organization:

[
\boxed{
dGLI
\rightarrow
\text{dGLI disk}
\rightarrow
\text{CloSE}
}
]

The paper's methodological contributions include:

* arranging dGLI values on a circular grid,
* identifying the hidden geometric patterns,
* extracting corner and fold information,
* mapping those features onto a compact circular representation,
* demonstrating semantic labeling and manipulation planning.

The authors explicitly describe the dGLI disk as an extension of the earlier work and CloSE as the compact representation derived from it.

Therefore:

[
\boxed{
\text{new mathematical invariant}
\neq
\text{new representation}
}
]

CloSE's principal novelty is **representational and methodological**.

---

# 12. What Is Learned?

The core CloSE representation is **not a neural-network latent representation**.

The principal operations are:

[
\boxed{
\text{geometric/topological measurement}
\rightarrow
\text{reorganization}
\rightarrow
\text{feature extraction}
\rightarrow
\text{interpretable coordinates}
}
]

The dGLI disk is constructed analytically from the cloth boundary.

The corner and fold coordinates are extracted using clustering and curve fitting.

Thus:

[
\boxed{
\text{CloSE is explicitly constructed}
}
]

rather than learned from a training population of cloth images.

This distinction matters for our literature positioning.

---

# 13. What the Paper Actually Represents

The final representation is:

[
\boxed{
CloSE=((v_1,\ldots,v_n),(f_1,f_2))
}
]

It represents the **deformation/folding state of physical cloth** through a small number of continuous angular coordinates.

Its information content can be viewed as:

[
\boxed{
\text{cloth boundary shape}
+
\text{fold location}
+
\text{fold orientation}
}
]

The representation is intended to be compact, continuous, and general across cloth shapes and poses.

This is fundamentally different from representing the morphology of a population of fashion sketches.

---

# 14. What They Demonstrate

The authors demonstrate two main applications.

### Semantic labeling

The CloSE coordinates can be interpreted to automatically determine the semantic folding state.

[
\boxed{
CloSE
\rightarrow
\text{semantic cloth state}
}
]

### Manipulation planning

The representation is also used for:

* high-level planning,
* low-level manipulation planning.

The representation can help determine which corners should be manipulated and where manipulation actions should occur.

Thus:

[
\boxed{
\text{CloSE}
\rightarrow
\text{semantic reasoning}
\rightarrow
\text{manipulation planning}
}
]

is demonstrated in the paper.

---

# 15. Important Limitation

The general representation is proposed as applicable to cloth states, but the **demonstrated results focus on single-fold configurations**.

The authors explicitly note that the dGLI disk contains additional information about:

* multiple folds,
* wrinkles,
* other cloth-state characteristics,

but these are not incorporated into the CloSE descriptor in the present work and are identified as future work.

Therefore we should not write:

[
\boxed{
\text{CloSE solves arbitrary cloth deformation}
}
]

A reviewer-proof statement is:

[
\boxed{
\text{CloSE demonstrates compact representation of single-fold cloth states}
}
]

while identifying multiple-fold generalization as future work.

---

# 16. What the Paper Does NOT Study

The paper does not primarily ask:

* How is garment morphology distributed across a population of fashion sketches?
* Can fashion sketches be represented explicitly in a morphology space?
* What population-level variation exists in garment-sketch geometry?
* Are different geometric measurements associated with garment morphology?
* Does a second geometric representation provide complementary information about sketch morphology?
* Does a morphology representation improve an independent garment-classification/discrimination task?
* Is there a semantic organization or grammar underlying fashion sketches?

These questions are outside its primary objective.

The paper concerns **physical cloth-state representation for robotic manipulation**, not population-level visual morphology.

---

# 17. CloSE vs. CLO-SKET

## CloSE

The central question is:

[
\boxed{
\text{How can physical cloth deformation be represented compactly and continuously?}
}
]

Pipeline:

[
\boxed{
\text{cloth boundary}
\rightarrow
dGLI
\rightarrow
\text{dGLI disk}
\rightarrow
CloSE
\rightarrow
\text{semantic state / planning}
}
]

## CLO-SKET

The central question is:

[
\boxed{
\text{How is garment morphology organized across a population of sketches?}
}
]

Our representation is:

[
\mathbf{x}_i\in\mathbb{R}^{135}
]

with population matrix:

[
\mathbf{X}\in\mathbb{R}^{2300\times135}.
]

Independent radial-angular representation:

[
\mathbf{r}_i\in\mathbb{R}^{28}
]

with:

[
\mathbf{R}\in\mathbb{R}^{2300\times28}.
]

We then test correspondence:

[
\mathbf{x}_i
\leftrightarrow
\mathbf{r}_i
]

against a row-permuted null:

[
\mathbf{x}*i
\leftrightarrow
\mathbf{r}*{\pi(i)}.
]

The scientific objectives are therefore fundamentally different.

---

# 18. Scientific Positioning

CloSE represents a **mathematically grounded, geometry-driven representation of physical cloth state**.

Its principal concern is:

[
\boxed{
\text{physical cloth geometry}
\rightarrow
\text{compact state representation}
}
]

CLO-SKET instead treats the **sketch population itself** as the object of quantitative study:

[
\boxed{
\text{garment-sketch population}
\rightarrow
\text{explicit morphology representation}
}
]

The distinction can therefore be summarized as:

[
\boxed{
\text{CloSE: physical cloth}
\rightarrow
\text{state representation}
}
]

versus

[
\boxed{
\text{CLO-SKET: sketch population}
\rightarrow
\text{morphology representation}
}
]

They therefore operate at different scientific levels rather than being direct methodological competitors.

---

# 19. FOMO Takeaway

### What this paper means for CLO-SKET

CloSE prevents us from making an overly broad claim such as:

> "Previous work has not constructed mathematically explicit representations of garment/cloth geometry."

That would be incorrect.

CloSE demonstrates that **topological/geometric relationships can be transformed into a compact representation with directly interpretable semantic coordinates**.

However, the semantic object in CloSE is **physical cloth state**, not fashion-sketch morphology.

A more defensible positioning is:

> Prior work has demonstrated that mathematically defined geometric relationships can be organized into compact, interpretable representations of physical cloth state, including corner and fold structure. CLO-SKET addresses a different level of analysis by asking whether explicit geometric measurements of 2D fashion sketches can characterize the organization of garment morphology across a population.

This distinction should guide the final Related Work wording.

---

# 20. Reviewer-Proof Classification

**Literature category:**

[
\boxed{
\text{Geometric/topological cloth-state representation}
}
]

**Primary task:**

[
\boxed{
\text{Cloth boundary}
\rightarrow
\text{CloSE}
\rightarrow
\text{semantic state / manipulation planning}
}
]

**Representation type:**

[
\boxed{
\text{Explicit continuous geometric/topological representation}
}
]

**Mathematical basis:**

[
\boxed{
\text{dGLI + circular geometric organization}
}
]

**Learning type:**

[
\boxed{
\text{No neural representation learning for the core CloSE construction}
}
]

**Population-level fashion-sketch morphology analysis:**

[
\boxed{\text{No}}
]

**Direct CLO-SKET competitor:**

[
\boxed{\text{No}}
]

**Relevance to CLO-SKET:**

[
\boxed{
\text{High — methodological precedent for explicit geometric representations with interpretable semantic structure}
}
]

---

# Final One-Sentence Understanding

> **Kamat et al. extend the earlier dGLI framework by reorganizing pairwise boundary measurements into a dGLI disk whose geometric patterns reveal cloth corners and fold structure, then abstracting these features into the compact continuous CloSE representation; while this demonstrates that mathematically defined geometric relationships can yield interpretable semantic coordinates for physical cloth state, CLO-SKET addresses a different problem by studying the quantitative organization of morphology across a population of 2D fashion sketches.**
