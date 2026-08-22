# An & Li (2014) — An Integrated Approach to Fashion Flat Sketches Classification

## Citation

**An, L., & Li, W. (2014)**  
*An Integrated Approach to Fashion Flat Sketches Classification*  
**International Journal of Clothing Science and Technology, 26(5), 346–366.**  
DOI: 10.1108/IJCST-05-2013-0054

### Role in CLO-SKET Literature Review

This paper represents a **fashion-flat-sketch shape-description and classification approach**.

Its central contribution is the **Wavelet Fourier Descriptor (WFD)**, a mathematically constructed shape descriptor designed to encode garment-contour information for multiclass classification.

The paper therefore establishes an important prior result:

> **Fashion flat-sketch contours can be transformed into quantitative shape descriptors that contain strongly discriminative information.**

However, the scientific objective is classification rather than population-level morphology.

The paper therefore operates primarily at:

\[
\boxed{
\text{fashion-flat-sketch shape description}
\rightarrow
\text{classification}
}
\]

rather than:

\[
\boxed{
\text{fashion-sketch population}
\rightarrow
\text{morphology space}
\rightarrow
\text{population structure}
}
\]

---

# 1. Scientific Question

The paper asks:

> **How can fashion flat sketches be classified efficiently and reliably using their shape information?**

The overall direction is:

\[
\boxed{
\text{Fashion flat sketch}
\rightarrow
\text{shape descriptor}
\rightarrow
\text{dimensionality reduction}
\rightarrow
\text{classification}
}
\]

The stated purpose is to develop a fast and reliable approach for **multiclass fashion-flat-sketch classification**, with the longer-term objective of supporting garment-style querying.

The paper is therefore concerned primarily with:

\[
\boxed{
\text{class discrimination}
}
\]

rather than with discovering or characterizing a continuous morphology space.

---

# 2. Input

The input consists of **fashion flat sketches**.

The authors explicitly distinguish fashion concept sketches/illustrations from flat sketches.

Concept sketches may communicate:

- overall style,
- visual feel,
- design impression,

but the authors argue that they do not necessarily provide sufficient information about the garment parts or sections.

For this reason, their study is restricted to:

\[
\boxed{
\text{fashion flat sketches}
}
\]

rather than general fashion illustrations.

The geometric information used for the proposed representation comes primarily from the **garment contour**.

---

# 3. The Core Problem

The paper needs a representation of garment shape that is:

- compact,
- discriminative,
- computationally efficient,
- robust to transformations such as translation, scale and rotation,
- useful for multiclass classification.

A conventional Fourier descriptor can encode contour shape in the frequency domain.

However, the authors seek a representation that combines:

\[
\boxed{
\text{global shape information}
+
\text{local/multiscale shape information}
}
\]

Their solution is the:

\[
\boxed{
\text{Wavelet Fourier Descriptor (WFD)}
}
\]

The key idea is to combine:

\[
\boxed{
\text{Discrete Wavelet Transform}
+
\text{Fourier Transform}
}
\]

so that the descriptor can capture multiscale contour structure while retaining the useful invariance properties of Fourier-based shape representations.

---

# 4. The WFD Pipeline

The complete conceptual pipeline is:

\[
\boxed{
\begin{aligned}
\text{garment contour}
&\rightarrow
\text{centroid-distance boundary function}\\
&\rightarrow
\text{DWT}\\
&\rightarrow
\text{wavelet approximation/detail signals}\\
&\rightarrow
\text{DFT}\\
&\rightarrow
|F(k)|\\
&\rightarrow
\frac{|F(k)|}{|F(0)|}\\
&\rightarrow
\text{WFD}
\end{aligned}
}
\]

The important point is that WFD is **not simply a Fourier descriptor**.

The wavelet stage first introduces multiscale/localized information, after which Fourier analysis is applied to the resulting signals.

---

# 5. Centroid-Distance Boundary Function

The garment contour is converted into a one-dimensional signal using a **centroid-distance boundary function**.

If the contour is:

\[
C(t)=(x(t),y(t))
\]

and the centroid is:

\[
(x_c,y_c),
\]

then the radial distance can be represented conceptually as:

\[
r(t)
=
\sqrt{
(x(t)-x_c)^2+
(y(t)-y_c)^2
}.
\]

Thus:

\[
\boxed{
\text{2-D garment contour}
\rightarrow
\text{1-D centroid-distance signal}
}
\]

This removes dependence on the absolute image position of the garment.

Therefore:

\[
\boxed{
\text{translation}
\rightarrow
\text{removed through centroid-based representation}
}
\]

The contour is now treated as a signal that can be analyzed using signal-processing methods.

---

# 6. Discrete Wavelet Transform

The centroid-distance boundary signal is processed using the:

\[
\boxed{
\text{Discrete Wavelet Transform (DWT)}
}
\]

The wavelet decomposition separates the signal into components associated with different scales.

Conceptually:

\[
r(t)
\rightarrow
\boxed{
\text{approximation}
+
\text{detail}
}
\]

The approximation components capture broader/coarser contour structure.

The detail components capture more localized changes.

Therefore:

\[
\boxed{
\text{DWT}
\rightarrow
\text{multiscale contour information}
}
\]

This is the central difference between the proposed WFD and a conventional Fourier descriptor applied directly to the contour.

---

# 7. Why Use Wavelets?

A Fourier representation is naturally expressed in terms of global frequency components.

Wavelets provide an additional localization property.

Conceptually:

\[
\boxed{
\text{Fourier}
\rightarrow
\text{frequency structure}
}
\]

while:

\[
\boxed{
\text{Wavelet}
\rightarrow
\text{frequency/scale + localization}
}
\]

The authors therefore combine them to obtain a shape representation containing both:

\[
\boxed{
\text{coarse/global contour structure}
}
\]

and:

\[
\boxed{
\text{local/detail contour structure}
}
\]

The WFD is consequently a **multiscale contour descriptor** rather than a purely global Fourier signature.

---

# 8. Fourier Transform of the Wavelet Components

The wavelet-derived signals are then transformed into the frequency domain using the discrete Fourier transform:

\[
F(k)
=
\sum_{n=0}^{N-1}
f(n)
e^{-i2\pi kn/N}.
\]

The representation uses the magnitude spectrum:

\[
\boxed{
|F(k)|
}
\]

rather than retaining the full complex Fourier coefficients.

The resulting representation captures the frequency characteristics of the wavelet-derived contour signals.

Conceptually:

\[
\boxed{
\text{wavelet components}
\rightarrow
\text{DFT}
\rightarrow
\text{magnitude spectrum}
}
\]

---

# 9. Scale Normalization

The magnitude spectrum is normalized using the DC component:

\[
\boxed{
\hat F(k)
=
\frac{|F(k)|}{|F(0)|}
}
\]

This removes the overall scale factor.

For example, suppose a contour produces:

\[
|F(k)|
=
[10,2,1].
\]

After normalization:

\[
\hat F(k)
=
\left[
1,
0.2,
0.1
\right].
\]

If the same contour is scaled by a factor of two, the spectrum may become:

\[
[20,4,2].
\]

Normalization gives:

\[
\left[
1,
0.2,
0.1
\right]
\]

again.

Therefore:

\[
\boxed{
\text{same shape at different scale}
\rightarrow
\text{same normalized descriptor}
}
\]

This provides **scale invariance**.

---

# 10. Rotation and Starting-Point Invariance

The Fourier representation is complex:

\[
F(k)
=
|F(k)|e^{i\phi_k}.
\]

The phase:

\[
\phi_k
\]

contains positional/phase information.

The proposed descriptor retains the magnitude:

\[
|F(k)|
\]

rather than the phase.

A rotation of the contour changes the phase of the complex representation but leaves its magnitude unchanged.

Similarly, changing the starting point when traversing a closed contour produces a cyclic shift that changes Fourier phase but not the magnitude spectrum.

Therefore:

\[
\boxed{
|F(k)|
\rightarrow
\text{reduced phase dependence}
}
\]

and the descriptor becomes invariant to:

\[
\boxed{
\text{rotation + starting-point choice}
}
\]

Together with the centroid-distance representation and scale normalization, the WFD is designed to provide robustness to:

\[
\boxed{
\text{translation}
+
\text{scale}
+
\text{rotation}
+
\text{starting point}
}
\]

---

# 11. What Does WFD Actually Represent?

This is the most important conceptual point for CLO-SKET.

WFD represents the **multiscale frequency characteristics of the garment contour**.

Its individual coordinates are not explicitly named garment measurements.

For example, a WFD coordinate does not directly mean:

\[
\text{shoulder width}
\]

or:

\[
\text{waist position}
\]

or:

\[
\text{sleeve length}.
\]

Instead:

\[
\boxed{
\text{WFD coordinate}
\approx
\text{frequency/multiscale characteristic of contour shape}
}
\]

Therefore:

\[
\boxed{
\text{WFD is mathematically defined}
}
\]

but:

\[
\boxed{
\text{WFD coordinates are not directly garment-semantic coordinates}
}
\]

This distinction is critical when comparing WFD with CLO-SKET.

---

# 12. WFD → LDA → ELM

WFD is the representation stage of a larger classification pipeline.

The complete approach is:

\[
\boxed{
\text{Fashion flat sketch}
\rightarrow
WFD
\rightarrow
LDA
\rightarrow
ELM
\rightarrow
\text{class}
}
\]

### WFD

Extracts the shape information.

### LDA

Linear Discriminant Analysis is used for dimensionality reduction in the multiclass classification pipeline.

### ELM

Extreme Learning Machine is used as the final classifier.

Therefore:

\[
\boxed{
\text{shape representation}
\rightarrow
\text{dimensionality reduction}
\rightarrow
\text{classification}
}
\]

---

# 13. Is WFD Learned?

No.

The WFD itself is analytically constructed.

Its core pipeline is:

\[
\boxed{
\text{contour}
\rightarrow
\text{centroid-distance signal}
\rightarrow
\text{DWT}
\rightarrow
\text{DFT}
\rightarrow
\text{spectral normalization}
}
\]

Machine learning enters downstream:

\[
\boxed{
WFD
\rightarrow
LDA
\rightarrow
ELM
}
\]

Thus the paper provides an example of:

\[
\boxed{
\text{hand-designed mathematical representation}
+
\text{machine-learning classifier}
}
\]

rather than end-to-end learned visual representation.

---

# 14. Is the Mathematics Invented by the Paper?

The paper's contribution should not be interpreted as inventing the underlying mathematics of wavelets, Fourier transforms, or discriminant analysis.

These are established mathematical/statistical tools.

The contribution is instead their **combination into a new shape descriptor for fashion flat sketches**:

\[
\boxed{
\text{DWT}
+
\text{Fourier representation}
+
\text{invariance normalization}
\rightarrow
\text{WFD}
}
\]

The authors specifically position WFD as a new shape descriptor and compare it against existing:

- Fourier Descriptor (FD),
- Multiscale Fourier Descriptor (MFD).

Therefore:

\[
\boxed{
\text{mathematical novelty}
\neq
\text{methodological/descriptor novelty}
}
\]

The principal contribution is the **WFD representation and its integration into the classification pipeline**.

---

# 15. Main Findings

The authors report classification accuracy of approximately:

\[
\boxed{
\sim100\%
}
\]

for their integrated approach.

They report that the method provides advantages in:

- classification accuracy,
- efficiency.

They compare WFD with conventional Fourier Descriptor (FD) and Multiscale Fourier Descriptor (MFD).

The reported findings indicate that:

- WFD achieves high classification accuracy compared with FD and MFD without dimensionality reduction;
- after LDA, WFD achieves classification accuracy close to that obtained using FD;
- MFD is reported to encounter a small-sample-size problem when dimensionality reduction with LDA is applied.

The authors therefore conclude that their integrated:

\[
\boxed{
WFD + LDA + ELM
}
\]

approach is effective for fashion-flat-sketch classification.

Important:

\[
\boxed{
\text{reported }\sim100\%\text{ accuracy}
\neq
\text{proof of universal/generalized classification performance}
}
\]

The result should be interpreted within the experimental dataset and evaluation protocol used by the paper.

---

# 16. What the Paper Establishes

The strongest supported conclusion is:

\[
\boxed{
\text{Fashion-flat-sketch contours contain quantitative shape information that can be encoded and used for strong class discrimination.}
}
\]

In other words:

\[
\boxed{
\text{fashion contour}
\rightarrow
\text{mathematical shape descriptor}
\rightarrow
\text{classification}
}
\]

is demonstrated.

This is a direct precedent for computational quantitative analysis of fashion-sketch shape.

---

# 17. What the Paper Does NOT Study

The paper does not primarily ask:

- How is garment morphology distributed across a population of sketches?
- Can fashion sketches be represented explicitly in a continuous morphology space?
- What population-level variation exists in sketch geometry?
- Which geometric dimensions explain morphological variation?
- Are independent geometric representations associated with the same morphology?
- Does a second representation provide complementary morphological information?
- Does a radial-angular representation capture corresponding structure?
- Does morphology representation improve an independent discrimination task?
- Is there a population-level semantic organization of garment sketches?

These questions are outside the paper's main objective.

The paper studies:

\[
\boxed{
\text{classification}
}
\]

rather than:

\[
\boxed{
\text{population morphology}
}
\]

---

# 18. An & Li vs. CLO-SKET

## An & Li

Central question:

\[
\boxed{
\text{Can fashion flat sketches be classified using quantitative shape information?}
}
\]

Pipeline:

\[
\boxed{
\text{flat sketch}
\rightarrow
\text{contour}
\rightarrow
WFD
\rightarrow
LDA
\rightarrow
ELM
\rightarrow
\text{class}
}
\]

The descriptor is primarily a **discriminative shape signature**.

---

## CLO-SKET

Central question:

\[
\boxed{
\text{How is garment morphology organized across a population of sketches?}
}
\]

Representation:

\[
\mathbf{x}_i\in\mathbb{R}^{135}
\]

with:

\[
\mathbf{X}\in\mathbb{R}^{2300\times135}.
\]

Independent radial-angular representation:

\[
\mathbf{r}_i\in\mathbb{R}^{28}
\]

with:

\[
\mathbf{R}\in\mathbb{R}^{2300\times28}.
\]

We then test:

\[
\mathbf{x}_i
\leftrightarrow
\mathbf{r}_i
\]

against row-permuted correspondence:

\[
\mathbf{x}_i
\leftrightarrow
\mathbf{r}_{\pi(i)}.
\]

The scientific objectives are therefore fundamentally different.

---

# 19. Scientific Positioning

An & Li represents a **fashion-flat-sketch shape-description and classification approach**.

Its principal concern is:

\[
\boxed{
\text{constructing a transformation-invariant shape signature}
}
\]

that can support classification.

CLO-SKET instead treats the sketches themselves as the object of quantitative study:

\[
\boxed{
\text{garment-sketch population}
\rightarrow
\text{explicit morphology representation}
}
\]

The distinction is therefore:

\[
\boxed{
\text{An \& Li}
=
\text{shape as a discriminative feature}
}
\]

versus:

\[
\boxed{
\text{CLO-SKET}
=
\text{shape as an object of morphological investigation}
}
\]

An & Li is therefore **highly relevant** to CLO-SKET, but it is not a direct methodological competitor to the population-level morphology analysis.

---

# 20. FOMO Takeaway

### What this paper means for CLO-SKET

This paper prevents us from making an incorrect literature claim such as:

> "Previous work has not quantitatively represented fashion sketches."

That would be incorrect.

An & Li clearly demonstrate that fashion-flat-sketch contours can be transformed into a mathematically defined shape descriptor and used for classification.

A more defensible positioning is:

> **Prior work has demonstrated that quantitative, transformation-invariant shape descriptors can be extracted from fashion flat sketches and used effectively for multiclass classification. CLO-SKET addresses a different level of analysis by treating explicit garment geometry as a morphology representation and investigating how that morphology is organized across a population of sketches.**

The distinction is therefore not:

\[
\text{previous work}
=
\text{no geometric representation}
\]

but:

\[
\boxed{
\text{previous work}
=
\text{geometric descriptor for classification}
}
\]

versus:

\[
\boxed{
\text{CLO-SKET}
=
\text{geometric representation for population-level morphology analysis}
}
\]

This distinction should guide the final Related Work wording.

---

# 21. Reviewer-Proof Classification

**Literature category**

\[
\boxed{
\text{Fashion-flat-sketch shape description / classification}
}
\]

**Primary task**

\[
\boxed{
\text{Fashion flat sketch}
\rightarrow
\text{WFD}
\rightarrow
\text{classification}
}
\]

**Representation**

\[
\boxed{
\text{Wavelet Fourier Descriptor (WFD)}
}
\]

**Mathematical basis**

\[
\boxed{
\text{centroid-distance contour}
+
\text{DWT}
+
\text{DFT}
+
\text{spectral normalization}
}
\]

**Learning**

\[
\boxed{
\text{LDA + ELM downstream of the analytic WFD representation}
}
\]

**Representation type**

\[
\boxed{
\text{Explicit mathematical contour descriptor}
}
\]

**Primary semantic role**

\[
\boxed{
\text{Discriminative shape signature}
}
\]

**Population-level morphology analysis**

\[
\boxed{\text{No}}
\]

**Explicit garment-semantic coordinates**

\[
\boxed{\text{No}}
\]

**Independent-representation correspondence**

\[
\boxed{\text{No}}
\]

**Direct CLO-SKET competitor**

\[
\boxed{\text{No}}
\]

**Relevance to CLO-SKET**

\[
\boxed{
\text{High — direct precedent for quantitative shape encoding of fashion flat sketches}
}
\]

---

# Final One-Sentence Understanding

> **An & Li (2014) develop the Wavelet Fourier Descriptor (WFD) by converting fashion-flat-sketch contours into centroid-distance signals, decomposing them into multiscale wavelet components, transforming those components into normalized Fourier-magnitude features, and using the resulting representation with LDA and ELM for multiclass classification; CLO-SKET differs by treating explicit garment geometry not primarily as a discriminative classification feature but as an interpretable morphology representation whose variation and internal organization are studied across a population of sketches.**