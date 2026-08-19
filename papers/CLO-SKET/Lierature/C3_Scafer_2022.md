# C3 — Mitteroecker & Schaefer (2022)
## Thirty years of geometric morphometrics: Achievements, challenges, and the ongoing quest for biological meaningfulness

**Reference**

Mitteroecker, P., & Schaefer, K. (2022).  
*Thirty years of geometric morphometrics: Achievements, challenges, and the ongoing quest for biological meaningfulness.*  
Yearbook of Biological Anthropology, 178(Suppl. 74), 181–210.  
DOI: 10.1002/ajpa.24531

---

## 1. Why this paper matters

This is a methodological review of modern geometric morphometrics (GM).

Its central concern is not simply:

> How can morphology be represented mathematically?

but rather:

> **How can mathematical representations of morphology support biologically meaningful inference?**

The authors emphasize that geometric morphometrics connects:

\[
\text{biological theory}
+
\text{measurement}
+
\text{multivariate statistics}
+
\text{geometry}
\]

and that weaknesses in any one of these components can affect biological interpretation.

The paper reviews:

- landmarks and semilandmarks
- Procrustes superimposition
- shape and form
- sliding semilandmarks
- TPS/bending energy
- statistical analysis of shape space
- spatial scales of morphological variation
- landmark density
- high-dimensionality
- landmark-free approaches
- biological interpretation of morphometric results

**Key message:**

\[
\boxed{
\text{A mathematically valid shape representation}
\neq
\text{automatically a biologically meaningful representation}
}
\]

---

# 2. Landmarks and semilandmarks

Geometric morphometrics represents objects using corresponding landmark coordinates.

Semilandmarks are introduced when the morphology contains curves or surfaces for which discrete anatomical landmarks are insufficient.

For semilandmarks:

\[
\text{normal direction}
\]

contains the meaningful geometric information, whereas their position **along the curve or surface** is not considered anatomically meaningful.

Therefore, arbitrary initial placement can introduce artificial variation.

Bookstein's sliding landmark approach addresses this by allowing semilandmarks to move along the tangent direction:

\[
p_i' = p_i + u_i t_i
\]

where:

- \(p_i\) = initial semilandmark
- \(t_i\) = tangent direction
- \(u_i\) = sliding displacement

The purpose is to reduce artificial variation arising from arbitrary positional placement.

---

# 3. An important correction to our interpretation of Bookstein

Mitteroecker & Schaefer make an important clarification.

Sliding by **bending-energy minimization** does not necessarily minimize total shape variance.

Instead:

\[
\boxed{
\text{Bending-energy minimization}
\rightarrow
\text{smoothest TPS deformation}
}
\]

whereas:

\[
\boxed{
\text{Procrustes-distance minimization}
\rightarrow
\text{minimum total shape variance}
}
\]

These are not mathematically identical objectives.

Bending energy emphasizes localized/non-affine deformation.

Small-scale shape differences have relatively high bending energy.

Affine changes such as:

- uniform scaling
- shearing

are not captured by bending energy.

Therefore, reducing bending energy does not necessarily mean that the total Procrustes shape variance has been minimized.

---

# 4. Why this matters biologically

The paper makes a very important point:

Neither bending energy nor Procrustes distance is itself a biological model.

They are mathematical/statistical criteria.

Therefore:

\[
\boxed{
\text{geometric correspondence}
\neq
\text{universal biological homology}
}
\]

Sliding often improves correspondence and interpretability, but it cannot guarantee biological homology.

The biological interpretation must depend on:

- the research question
- the anatomical structure
- the measurement system
- the relevant concept of homology

This is one of the most important methodological warnings in the paper.

---

# 5. Sliding is an optimization problem

The sliding procedure is iterative.

At each iteration:

1. tangent directions/planes are estimated
2. semilandmarks are allowed to slide
3. the chosen criterion is minimized
4. the mean shape may be updated
5. tangent directions are recomputed

Thus:

\[
\boxed{
\text{initial correspondence}
\rightarrow
\text{optimization}
\rightarrow
\text{updated correspondence}
\rightarrow
\text{repeat}
}
\]

For strongly curved structures, sliding entirely along the estimated tangent can even move points away from the actual structure.

The authors therefore recommend carefully supervising the result and checking that slid semilandmarks:

- remain on the structure
- cover the relevant morphology
- maintain meaningful geometric/biological correspondence

---

# 6. Shape versus form

Geometric morphometrics distinguishes:

### Shape

Geometry after removing:

- translation
- rotation
- scale

### Form

Geometry retaining size information.

Generalized Procrustes Analysis (GPA) standardizes configurations by:

1. translating them to a common centroid
2. scaling them to common centroid size
3. rotating them to minimize squared differences

Thus:

\[
\text{raw coordinates}
\rightarrow
\text{GPA}
\rightarrow
\text{shape coordinates}
\]

But removing size is not automatically biologically justified.

The authors explicitly recommend that investigators consider **form**, not only shape, when there is no prior reason to discard size.

---

# 7. Important point for brain morphology

This paper is directly relevant to our brain work.

The authors discuss neurocranial/endocranial morphology and warn that centroid size can become geometrically associated with shape.

For example, centroid size can correlate with endocranial shape even when endocranial volume is identical.

Therefore:

\[
\boxed{
\text{centroid size}
\neq
\text{perfect biological measure of brain size}
}
\]

For subtle differences in brain size, the authors state that **endocranial volume can be safer than centroid size**, particularly when endocranial shape varies strongly.

This is extremely relevant to our study because it tells us not to casually interpret a morphometric "size" coordinate as biological brain size.

---

# 8. Spatial scale of morphology

One of the strongest concepts for our work is the distinction between:

\[
\text{large-scale shape variation}
\]

and

\[
\text{small-scale shape variation}
\]

Increasing landmark density introduces more small-scale shape information.

Bending energy provides a natural way of describing spatial scale:

\[
\text{high bending energy}
\rightarrow
\text{localized/small-scale deformation}
\]

\[
\text{low bending energy}
\rightarrow
\text{large-scale deformation}
\]

The authors discuss the use of relative warps and related approaches for examining different spatial scales.

This is important because morphology is not necessarily a single-scale phenomenon.

---

# 9. Landmark density is not automatically better

A major methodological point:

\[
\boxed{
\text{more landmarks}
\neq
\text{automatically better morphology}
}
\]

The appropriate number and spacing of landmarks depend on:

- the spatial scale of interest
- the biological question
- the expected variation
- whether important features are known beforehand

A dense landmark set is useful when small-scale features matter.

But increasing dimensionality also creates statistical challenges.

The authors note that shape coordinates are not full-rank and that covariance-matrix inversion generally requires dimension reduction or regularization.

Therefore:

\[
\text{spatial resolution}
\quad\text{vs}\quad
\text{statistical complexity}
\]

is an explicit methodological trade-off.

---

# 10. Biological interpretation is the real objective

The authors repeatedly return to the idea that morphometric analysis should not stop at a statistical result.

For example:

\[
\text{PCA}
\]

does not itself explain biology.

A useful morphometric analysis should connect statistical variation back to actual morphology.

Hence their emphasis on visualizing:

- reconstructed shapes
- deformation grids
- morphing
- meaningful anatomical structures

rather than relying exclusively on scalar statistics.

---

# 11. Landmark-free methods

The paper also discusses emerging "landmark-free" approaches.

These approaches can successfully detect morphological differences, particularly for:

- discrimination
- classification
- medical imaging

However, removing point homology creates a major interpretational problem.

If the same anatomical feature is not represented by corresponding points across specimens, then:

\[
\text{mean shape}
\]

may no longer correspond to a biologically meaningful specimen.

The authors give a useful conceptual example involving the nose:

If the nose occurs at different locations and there is no homologous landmark defining its tip, the computed average may effectively combine different anatomical regions.

Thus:

\[
\boxed{
\text{successful classification}
\neq
\text{successful morphological interpretation}
}
\]

The authors explicitly state that the usefulness of landmark-free approaches for biometric analyses beyond discrimination/classification remains to be fully explored.

---

# 12. The deeper mathematical lesson

This paper exposes a hierarchy that is extremely important for our work:

\[
\boxed{
\text{measurement}
\rightarrow
\text{representation}
\rightarrow
\text{geometry}
\rightarrow
\text{statistics}
\rightarrow
\text{biological interpretation}
}
\]

An error or assumption introduced at an earlier level can propagate through the entire pipeline.

For example:

\[
\text{arbitrary semilandmark placement}
\rightarrow
\text{artificial coordinate variation}
\rightarrow
\text{shape-space variation}
\rightarrow
\text{statistical signal}
\rightarrow
\text{potentially misleading biology}
\]

Sliding attempts to reduce the first problem.

But sliding itself introduces an optimization criterion.

Therefore the optimization criterion must also be understood biologically.

---

# 13. Relevance to our research

This paper strengthens the conceptual foundation of our approach.

It tells us that we should not ask only:

> Can we mathematically represent the morphology?

We should ask:

> **Does the representation preserve the biological information relevant to the question?**

This gives us a useful design principle:

\[
\boxed{
\text{Representation should be justified by the biological question}
}
\]

rather than:

\[
\text{Choose representation first}
\rightarrow
\text{interpret biology afterward}
\]

---

# 14. What this paper establishes

### Strongly supported

- Semilandmarks are useful for representing curves and surfaces.
- Their tangential position is generally not anatomically meaningful.
- Sliding reduces artificial variation caused by arbitrary placement.
- Bending-energy and Procrustes-distance sliding optimize different criteria.
- Bending energy emphasizes local/non-affine deformation.
- Geometric correspondence does not guarantee universal biological homology.
- Shape and size/form should be distinguished carefully.
- Centroid size is not a perfect biological size measure.
- Landmark density should be related to the spatial scale and biological question.
- High-dimensional morphometric data create statistical challenges.
- Landmark-free methods create substantial interpretational challenges.

---

# 15. What this paper does NOT establish

It does **not** establish that:

- sliding produces biologically true homology
- bending-energy minimization always gives the correct correspondence
- Procrustes minimization is universally superior
- more landmarks always improve inference
- landmark-free methods are invalid
- morphometric coordinates directly represent biological mechanisms

Instead, the paper argues for **context-dependent methodological justification**.

---

# 16. Contribution to our conceptual framework

The paper gives us the following principle:

\[
\boxed{
\text{Mathematical optimization}
\neq
\text{biological truth}
}
\]

More precisely:

\[
\boxed{
\text{Mathematical criterion}
\rightarrow
\text{geometric representation}
\rightarrow
\text{statistical inference}
}
\]

must ultimately be evaluated against:

\[
\boxed{
\text{biological meaning}
}
\]

---

# 17. Position in Cluster C

| Paper | Main contribution |
|---|---|
| **C1 — Bookstein** | Mathematical treatment of semilandmark sliding using TPS/bending energy |
| **C2 — McCane** | Formal treatment of shape representation/distance and correspondence |
| **C3 — Mitteroecker & Schaefer** | Biological interpretation, methodological limitations, and consequences of representation choices |

The progression is:

\[
\boxed{
\text{How do we optimize correspondence?}
\rightarrow
\text{How do we represent shape?}
\rightarrow
\text{Does that representation remain biologically meaningful?}
}
\]

---

# 18. Key takeaway for our brain study

The most important lesson is:

\[
\boxed{
\text{Do not equate a morphometric coordinate with a biological quantity
without validating the mapping.}
}
\]

For example:

\[
\text{centroid size}
\not\equiv
\text{brain size}
\]

when the biological question is specifically about brain volume.

Likewise:

\[
\text{sliding displacement}
\not\equiv
\text{biological movement/homology}
\]

It is an optimized geometric correspondence variable.

That distinction is fundamental.