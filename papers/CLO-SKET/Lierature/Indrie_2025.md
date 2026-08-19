# Indrie et al. (2025) — A Study of Types of Silhouettes in Women’s Clothing

## Citation

**Indrie, L., Kazlacheva, Z., Ilieva, J., Zlatev, Z., Dineva, P., & Sturza, A. (2025).**

*A study of types of silhouettes in women’s clothing.*

**Industria Textila, 76(1), 19–30.**

DOI: 10.35530/IT.076.01.2024139

---

# 1. Why This Paper Matters

This paper is **important prior art for quantitative fashion morphology**.

The authors explicitly move beyond purely subjective silhouette classification and analyze collections of garment silhouettes using quantitative shape descriptors, feature selection, and PCA.

Their dataset contains:

- **29 dress silhouettes**
- **40 skirt silhouettes**
- **19 necklines**

The silhouettes are collected from existing literature rather than being treated as photographs or a large-scale naturally occurring sketch corpus.

The study therefore establishes that a population of garment silhouettes can be converted into quantitative shape vectors and analyzed statistically.

---

# 2. Scientific Question

The paper asks whether women's clothing silhouettes can be classified and organized more systematically using quantitative shape analysis.

The motivation is that traditional silhouette classification depends heavily on visual/subjective assessment, with limited connection between subjective labels and objective measurements.

The authors therefore seek a more quantitative classification system that can identify groups of dress and skirt silhouettes.

---

# 3. Dataset / Population

The study analyzes:

\[
N_{dress}=29
\]

dress silhouettes and

\[
N_{skirt}=40
\]

skirt silhouettes.

The paper also includes 19 neckline silhouettes.

Importantly, these are **pre-existing silhouette representations collected from literature**.

They are not presented as a large dataset of independently created fashion sketches.

The dress silhouettes include examples such as:

- Body-con
- Shift
- Sheath
- Strapless
- Bouffant
- A-line
- Tent
- Blouson
- Halter
- Shirt
- Wrap
- Peplum
- Drop waist
- Ball gown
- Empire
- Balloon
- Princess
- Trapezoid
- V-line

The skirt population similarly contains 40 named silhouette types.

---

# 4. What Is Actually Represented?

This is the critical part.

The authors do **not** feed raw sketch pixels directly into PCA.

Instead, they convert each isolated silhouette into a set of quantitative shape descriptors.

The paper defines:

\[
24
\]

shape/form coefficients:

\[
K_1,K_2,\ldots,K_{24}
\]

These coefficients are based on geometric quantities such as:

- major axis \(D\)
- minor axis \(d\)
- perimeter \(P\)
- area \(A\)
- ideal area
- enclosing rectangle area
- volume

The paper explicitly defines these geometric quantities as the basis for the form factors.

---

# 5. Image Processing Pipeline

The silhouette image undergoes a simple image-analysis pipeline:

\[
\boxed{
RGB
\rightarrow
HSV
\rightarrow
S\text{-channel}
\rightarrow
normalization
\rightarrow
binarization
\rightarrow
silhouette isolation
\rightarrow
geometric measurements
}
\]

The binary silhouette is then analyzed using region properties to obtain quantities such as:

\[
D,\ d,\ P,\ A
\]

These are subsequently used to calculate the 24 form coefficients.

The paper's Figure 3 explicitly illustrates this pipeline from the original RGB silhouette through HSV processing, binary segmentation, region properties, and calculated coefficients.

---

# 6. Important Scientific Point

Therefore the representation is:

\[
\boxed{
\text{silhouette image}
\rightarrow
\text{explicit geometric measurements}
\rightarrow
\text{24 form coefficients}
}
\]

NOT:

\[
\text{silhouette image}
\rightarrow
\text{learned neural embedding}
\]

and NOT:

\[
\text{raw pixel population}
\rightarrow
\text{PCA}
\]

The authors deliberately construct the geometric representation before performing statistical analysis.

---

# 7. Feature Selection

The 24 coefficients are not all used directly.

The authors apply **ReliefF** to identify informative shape indices.

A coefficient with a weighting value greater than:

\[
0.6
\]

is considered meaningful.

This produces:

### Dresses

\[
FVD=[K_5,K_6,K_{13},K_{14},K_{19}]
\]

### Skirts

\[
FVS=[K_5,K_6,K_{14},K_{22}]
\]

Thus:

\[
\boxed{
24\text{ descriptors}
\rightarrow
5\text{ informative dress descriptors}
}
\]

and

\[
\boxed{
24\text{ descriptors}
\rightarrow
4\text{ informative skirt descriptors}
}
\]

The paper explicitly notes that skirts can be described using fewer informative features than dresses.

---

# 8. PCA

PCA is then applied to these selected feature vectors.

The authors standardize the features, calculate the covariance matrix, obtain eigenvalues/eigenvectors, and project the observations into a lower-dimensional principal-component space.

Conceptually:

\[
X
\rightarrow
\text{standardization}
\rightarrow
\Sigma
\rightarrow
\{\lambda_i,v_i\}
\rightarrow
PC\ space
\]

The paper describes PCA as a transformation into a new coordinate system that reduces dimensionality while preserving important variation.

---

# 9. The Important "Rotation" Clarification

This is where our earlier conversation needs to be precise.

Yes, PCA mathematically **rotates/re-expresses the coordinate system of the feature data**.

But this is NOT what Indrie et al. are doing when they geometrically process the garment.

They are **not rotating a garment relative to a body part**.

There are two completely different operations:

### Geometric garment alignment

\[
\text{garment}
\rightarrow
\text{translation/rotation/scale}
\]

This is what the modular flat-sketch alignment paper we discussed earlier does.

### PCA coordinate transformation

\[
\text{feature vector}
\rightarrow
\text{new PC coordinate system}
\]

This is what Indrie et al. do.

So:

\[
\boxed{
\text{PCA rotation}
\neq
\text{garment alignment}
}
\]

Very important distinction for our literature map.

---

# 10. PCA Variance

The selected feature vectors are reduced to two principal components.

The paper reports that:

\[
PC_1 + PC_2 >95\%
\]

of the variance is explained in the analyzed cases.

Thus the high-dimensional geometric representation can be visualized approximately in a two-dimensional shape space.

This is probably the most interesting part for CLO-SKET.

---

# 11. Dress Shape Space

The 29 dress silhouettes are projected into:

\[
(PC_1,PC_2)
\]

space.

Four groups are identified.

The paper interprets these groups according to the quadrants of the PCA plot:

### Group 1

\[
(+PC_1,+PC_2)
\]

Primarily X-shaped silhouettes.

### Group 2

\[
(-PC_1,+PC_2)
\]

Primarily A- and I-shaped silhouettes.

### Group 3

\[
(-PC_1,-PC_2)
\]

Again primarily A- and I-shaped silhouettes.

### Group 4

\[
(+PC_1,-PC_2)
\]

X- and Y-shaped silhouettes.

Therefore:

\[
\boxed{
29\text{ dress silhouettes}
\rightarrow
5D\ geometric representation
\rightarrow
2D\ PCA
\rightarrow
4\text{ groups}
}
\]

---

# 12. Skirt Shape Space

The 40 skirt silhouettes are processed similarly.

Three groups emerge in PCA space.

The authors interpret them approximately as:

1. innovative/practical/flexible designs
2. structured/formal designs
3. classic/conservative silhouettes

Therefore:

\[
\boxed{
40\text{ skirt silhouettes}
\rightarrow
4D\ geometric representation
\rightarrow
2D\ PCA
\rightarrow
3\text{ groups}
}
\]

---

# 13. This Is Genuine Population-Level Shape Analysis

This is where we need to update our FOMO assessment.

The paper **does satisfy several components of our original gap question**.

It has:

\[
\boxed{
\text{population}
+
\text{geometric representation}
+
\text{multivariate statistics}
+
\text{low-dimensional shape space}
+
\text{grouping}
}
\]

Therefore we absolutely **cannot claim**:

> "Nobody has quantitatively analyzed a population of fashion silhouettes."

That would be false.

Indrie et al. clearly do this.

---

# 14. But What Population?

The crucial distinction is:

\[
\boxed{
\text{population of predefined garment silhouettes}
}
\]

rather than:

\[
\boxed{
\text{population of arbitrary 2D fashion sketches/flats}
}
\]

The silhouettes are selected from existing classifications/literature and already function as recognized silhouette categories.

This means the study investigates:

> **How do known garment silhouette types organize geometrically?**

rather than:

> **Does an unconstrained population of fashion drawings spontaneously exhibit morphological structure?**

---

# 15. Representation Is Hand-Designed

The shape representation is explicitly engineered.

The researchers choose:

\[
K_1,\ldots,K_{24}
\]

from geometric quantities such as area, perimeter, axes and related ratios.

ReliefF then selects the informative subset.

Therefore:

\[
\boxed{
\text{human-designed geometric descriptors}
\rightarrow
\text{statistical shape space}
}
\]

rather than:

\[
\boxed{
\text{raw sketch geometry}
\rightarrow
\text{representation discovered from population}
}
\]

---

# 16. What the Paper DOES Establish for Our Literature Review

It establishes strong precedent for:

### Quantitative garment morphology

\[
\boxed{\text{YES}}
\]

### Population-level silhouette analysis

\[
\boxed{\text{YES}}
\]

### Geometric shape descriptors

\[
\boxed{\text{YES}}
\]

### Statistical dimensionality reduction

\[
\boxed{\text{YES}}
\]

### PCA-based garment shape space

\[
\boxed{\text{YES}}
\]

### PCA-based silhouette grouping

\[
\boxed{\text{YES}}
\]

### Multiple garment populations

\[
\boxed{\text{YES}}
\]

Both dresses and skirts are analyzed.

---

# 17. What It Does NOT Establish

The paper does not establish:

### A large-scale population of raw fashion sketches

\[
\boxed{\text{NO}}
\]

### A population of technical fashion flats drawn by different designers

\[
\boxed{\text{NO}}
\]

### Morphology learned directly from sketch geometry

\[
\boxed{\text{NO}}
\]

### An unconstrained morphological population

\[
\boxed{\text{NO}}
\]

### A common shape space spanning arbitrary garment categories

\[
\boxed{\text{NO}}
\]

### Independent geometric representations recovering the same structure

\[
\boxed{\text{NO}}
\]

### Semantic relationships between garment primitives

\[
\boxed{\text{NO}}
\]

### A learned semantic language of fashion sketches

\[
\boxed{\text{NO}}
\]

---

# 18. The Most Important Comparison

We should now distinguish three different research questions.

## A. Indrie et al.

\[
\boxed{
\text{known silhouette population}
\rightarrow
\text{engineered geometric descriptors}
\rightarrow
PCA
\rightarrow
\text{groups}
}
\]

Question:

> How can recognized clothing silhouettes be quantitatively characterized and grouped?

---

## B. Modular Flat-Sketch Alignment Paper

\[
\boxed{
\text{garment modules}
\rightarrow
\text{anchor points}
\rightarrow
\text{translation/rotation/scale}
\rightarrow
\text{assembled flat}
}
\]

Question:

> How can garment components be geometrically aligned and assembled?

This is **not PCA morphology**.

---

## C. CLO-SKET

Potentially:

\[
\boxed{
\text{population of 2D fashion sketches}
\rightarrow
\text{geometric/morphological representation}
\rightarrow
\text{population structure}
\rightarrow
\text{semantic organization}
}
\]

Question:

> Does the geometry of fashion sketches itself contain a reproducible morphological organization that can be computationally characterized?

That is a different scientific question.

---

# 19. Very Important FOMO Update

Before reading the actual paper, we were asking:

> "Has anyone actually treated a population/collection of 2D fashion sketches or fashion flats as a morphological population and performed quantitative shape-space analysis?"

After reading this paper, the answer becomes:

### If "fashion silhouettes" counts:

\[
\boxed{\textbf{YES}}
\]

Indrie et al. absolutely do this.

### If the requirement is:

> **raw / technical 2D fashion sketches or fashion flats as the observational population**

then:

\[
\boxed{\textbf{NOT ESTABLISHED BY THIS PAPER}}
\]

That distinction is now critical.

---

# 20. Even More Important: They Explicitly Position Themselves Against Earlier Work

The authors discuss Tsuru et al., who also analyze dress silhouettes using PCA, mean squared displacement and cluster analysis.

Tsuru et al. obtain three categories.

Indrie et al. state that their approach obtains four dress groups directly from PCA-reduced form factors, arguing that ratio-based form factors provide an advantage over raw measurements.

Thus Indrie et al. are **not the first quantitative silhouette-shape-space paper**.

They are an extension/refinement of an existing quantitative silhouette-analysis lineage.

---

# 21. Literature Lineage

We can now represent this part of the literature as:

\[
\boxed{
\text{qualitative silhouette taxonomy}
}
\]

↓

\[
\boxed{
\text{geometric measurements}
}
\]

↓

\[
\boxed{
\text{multivariate statistical analysis}
}
\]

↓

\[
\boxed{
\text{PCA / clustering}
}
\]

↓

\[
\boxed{
\text{quantitative silhouette populations}
}
\]

Indrie et al. belong firmly in this lineage.

---

# 22. What Remains Interesting for CLO-SKET

The remaining gap is therefore **much narrower and much stronger**.

Not:

> "Nobody has studied fashion morphology quantitatively."

Instead:

> **Existing quantitative studies have demonstrated statistical organization of predefined garment silhouettes using hand-designed geometric descriptors. What remains less established is whether a broader population of 2D fashion sketches/flats can be treated directly as a morphological population, with the morphological organization emerging from the geometry of the sketches rather than from predefined silhouette categories and hand-designed descriptors.**

That is a much more defensible claim.

---

# 23. Reviewer-Proof Classification

### Paper type

**Quantitative garment-silhouette morphology**

### Population

**29 dresses + 40 skirts + 19 necklines**

### Representation

**24 explicit geometric/form coefficients**

### Feature selection

**ReliefF**

### Dimensionality reduction

**PCA**

### Final dimensionality

**2 principal components**

### Variance explained

**>95%**

### Dress groups

**4**

### Skirt groups

**3**

### Raw fashion-sketch population?

**No**

### Technical-flat population?

**Not established**

### Learned representation?

**No**

### Hand-designed geometric representation?

**Yes**

### Statistical shape space?

**Yes**

### Direct CLO-SKET competitor?

**Partial / adjacent**

### Importance for FOMO

\[
\boxed{\textbf{CRITICAL PRIOR ART}}
\]

---

# 24. One-Sentence Takeaway

> **Indrie et al. (2025) demonstrate that a population of predefined women's garment silhouettes can be represented using engineered geometric form factors, reduced with ReliefF and PCA, and organized into low-dimensional statistical shape spaces containing four dress groups and three skirt groups; however, this does not establish morphological analysis of a broad population of raw 2D fashion sketches/flats or morphology emerging independently of predefined silhouette categories and hand-designed descriptors.**

---

# 25. Status for Our Literature Review

\[
\boxed{
\textbf{KEEP — VERY IMPORTANT PRIOR ART}
}
\]

**Why:**

This paper means we must **narrow the novelty claim** around fashion morphology.

It also gives us a very useful benchmark:

\[
\boxed{
\text{24 geometric descriptors}
\rightarrow
\text{ReliefF}
\rightarrow
\text{PCA}
\rightarrow
\text{shape groups}
}
\]

So when we eventually present CLO-SKET, the reviewer will immediately be able to see that we know this literature and are **not claiming PCA or quantitative silhouette morphology as new**.