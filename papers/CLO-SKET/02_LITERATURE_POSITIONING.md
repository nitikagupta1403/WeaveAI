# 2. Related Work

## 2.1 Computational Analysis of Fashion Sketches

Computational research on fashion sketches has addressed several related problems, including geometric garment reconstruction, sketch-based garment modeling, garment-style transfer, classification, and multimodal representation learning. These studies establish that 2D garment drawings contain structured geometric information that can be computationally extracted and used for downstream garment analysis or synthesis.

Geometry-driven approaches interpret the sketch directly as a specification of garment structure. Robson et al. use garment silhouettes, boundaries, characteristic curves, and folds to construct plausible 3D garments, demonstrating that geometric constraints extracted from a sketch can determine substantial aspects of garment form. Yasseen et al. similarly convert sketched garment boundaries into quadrilateral mesh structures suitable for subsequent garment simulation. These approaches establish that sketch geometry can serve as a direct computational representation of garment form, but their objective is reconstruction rather than population-level analysis of sketch morphology.

Fondevilla et al. extend this geometric interpretation to the transfer of garment style from a 2D fashion sketch to 3D characters. Their representation separates sketch-derived information into proportionality, fit, overall garment shape, and fold structure. The extracted geometric information is subsequently used to synthesize garments for characters with different poses and body morphologies. The work therefore demonstrates that meaningful geometric style information can be recovered from a single fashion sketch, but it does not investigate whether geometric variation across a population of sketches forms a reproducible morphological organization.

Wang et al. approach the problem through multimodal representation learning, linking 2D fashion sketches with garment and body parameters and simulated 3D garments. Their framework learns mappings between these modalities in a shared latent representation for garment reconstruction and retargeting. This differs fundamentally from an explicit morphology representation: the sketch is encoded using learned image features, while PCA is applied to the simulated 3D garment representation rather than being used to characterize the population of 2D sketches themselves.

Taken together, these studies establish that:

\[
\boxed{
\text{2D garment sketches contain computationally recoverable geometric information}
}
\]

However, their primary objectives are reconstruction, transfer, classification, or multimodal prediction. The sketch is generally treated as an input to a downstream task rather than as the primary observational unit of a population-level morphological analysis.

---

## 2.2 Quantitative Representations of Fashion Flats

A second body of work has developed explicit quantitative representations for fashion flats and garment contours.

An and Li proposed an integrated approach for fashion-flat-sketch classification based on a Wavelet Fourier Descriptor (WFD), followed by Linear Discriminant Analysis (LDA) and an Extreme Learning Machine classifier. Their method extracts contour shape information using wavelet and Fourier transforms and uses the resulting representation for multiclass classification. The study therefore provides direct evidence that fashion-flat contours can be transformed into mathematically defined shape descriptors. However, the representation is constructed to distinguish predefined classes rather than to characterize the geometry of a sketch population as a morphological space.

This distinction is important because dimensionality reduction used for classification should not automatically be interpreted as population morphology. In An and Li, LDA is supervised by the classification problem. The resulting representation therefore answers the question:

\[
\boxed{
\text{Can shape descriptors discriminate predefined fashion-flat classes?}
}
\]

rather than:

\[
\boxed{
\text{How is geometric variation organized across a population of fashion flats?}
}
\]

Lee and Kim provide another explicit geometric representation of fashion flats through garment modularization. Their system decomposes fashion flats into components such as bodices, sleeves, collars, cuffs, and pockets and uses geometric alignment to assemble these components into new designs. The transformations used for module alignment include translation, rotation, and scaling.

These geometric transformations should be distinguished from statistical transformations such as PCA. Geometric alignment changes the spatial configuration of an object, whereas PCA changes the coordinate basis used to represent variation across observations.

Thus, prior fashion-flat research establishes that:

\[
\boxed{
\text{fashion flat}
\rightarrow
\text{quantitative geometric representation}
}
\]

and

\[
\boxed{
\text{fashion flat}
\rightarrow
\text{explicit structural components}
}
\]

but these representations have primarily been developed for classification or design construction rather than for investigating population-level morphological organization.

---

## 2.3 Geometric Morphometrics and Quantitative Shape

The methodological basis for treating visual form as a quantitative morphological object is provided by geometric morphometrics.

Bookstein introduced methods for analyzing outlines without conventional landmarks through the use of semilandmarks. Because arbitrary positions along a curve need not correspond across observations, semilandmarks can slide along the tangent direction, reducing variation caused by arbitrary sampling position. The resulting representation permits quantitative comparison of outline shape.

The general principle is:

\[
\boxed{
\text{outline}
\rightarrow
\text{correspondence}
\rightarrow
\text{quantitative shape}
}
\]

This establishes an important methodological distinction:

\[
\boxed{
\text{geometric representation}
\neq
\text{meaningful morphology automatically}
}
\]

The mathematical representation must be appropriate to the scientific question and to the form of variation being investigated.

McCane extends this perspective toward population-level analysis of outlines by defining distances between complete shapes rather than requiring a fixed set of corresponding landmarks. For a population of shapes

\[
S_1,S_2,\ldots,S_N,
\]

pairwise distances

\[
d(S_i,S_j)
\]

can be used to construct a distance matrix and subsequently a low-dimensional representation of the population.

The conceptual progression is therefore:

\[
\boxed{
\text{individual outline}
\rightarrow
\text{shape distance}
\rightarrow
\text{population geometry}
}
\]

This is particularly relevant to the present work because it establishes that shape analysis can move beyond describing individual forms toward characterizing the organization of an entire population.

However, these geometric-morphometric methods are general methodological frameworks and do not provide a garment-specific representation or establish that 2D fashion sketches form a morphological population.

---

## 2.4 Quantitative Morphology in Fashion

Importantly, quantitative population-level morphology is not absent from fashion research.

Tsuru et al. analyzed a population of garments from luxury fashion collections using standardized geometric measurements corresponding to garment locations such as the neck, shoulder, waist, hip, hem, knee, and garment length. Multivariate analysis, including multidimensional scaling and clustering, was then used to investigate the organization of garment silhouettes.

Their work establishes the following pipeline:

\[
\boxed{
\text{garment population}
\rightarrow
\text{geometric measurements}
\rightarrow
\text{multivariate analysis}
\rightarrow
\text{silhouette organization}
}
\]

Thus, it would not be accurate to claim that quantitative population morphology has not previously been applied to fashion.

Indrie et al. provide a more recent example using collections of dress and skirt silhouettes. Their study analyzes 29 dress silhouettes and 40 skirt silhouettes using explicitly defined geometric form coefficients derived from measurements such as axes, perimeter, and area. Feature selection is followed by PCA, producing a low-dimensional representation in which groups of dress and skirt silhouettes can be identified.

The resulting pipeline is:

\[
\boxed{
\text{silhouette}
\rightarrow
\text{geometric form coefficients}
\rightarrow
\text{feature selection}
\rightarrow
\text{PCA}
\rightarrow
\text{silhouette groups}
}
\]

This establishes strong precedent for the statistical analysis of garment morphology and, specifically, for the use of PCA to organize fashion-silhouette variation.

Consequently, neither geometric garment descriptors nor PCA-based analysis of fashion morphology constitute the novelty of the present study.

---

## 2.5 Distinguishing Garment Morphology from Sketch Morphology

The existing literature nevertheless differs in the nature of the objects used as observations.

Fashion morphology studies such as Tsuru et al. analyze photographs or representations of physical garments, while Indrie et al. analyze predefined garment-silhouette representations collected from existing literature. These studies therefore investigate the geometry of garments or recognized silhouette types.

In contrast, computational fashion-sketch studies generally use drawings as inputs to downstream tasks such as classification, reconstruction, module assembly, or transfer.

This creates an important distinction between two questions:

\[
\boxed{
\text{How is the morphology of garments organized?}
}
\]

and

\[
\boxed{
\text{How is the morphology expressed in a population of 2D garment sketches organized?}
}
\]

The first question has clear precedent in fashion research.

The second is less established in the literature reviewed here.

In particular, the reviewed studies do not establish a general framework in which a heterogeneous population of 2D garment sketches or technical flats is treated directly as the primary morphological population, using explicit image-derived measurements without first defining the population through semantic silhouette categories.

---

# 2.6 The Remaining Gap

The literature therefore establishes four important capabilities.

First:

\[
\boxed{
\text{fashion sketches}
\rightarrow
\text{geometric representation}
}
\]

has been demonstrated.

Second:

\[
\boxed{
\text{fashion flats}
\rightarrow
\text{quantitative shape descriptors}
}
\]

has been demonstrated.

Third:

\[
\boxed{
\text{fashion garment population}
\rightarrow
\text{statistical morphology}
}
\]

has been demonstrated.

Fourth:

\[
\boxed{
\text{general outline population}
\rightarrow
\text{quantitative shape space}
}
\]

has been established in geometric-morphometric methodology.

The less-established intersection is therefore:

\[
\boxed{
\textbf{
\text{2D garment-sketch population}
\rightarrow
\text{explicit image-derived morphology}
\rightarrow
\text{population-level organization}
}
}
\]

The distinction is not that previous work lacked shape descriptors, PCA, clustering, or garment morphology. Rather, the unresolved question concerns whether the geometry of a heterogeneous collection of 2D garment sketches itself exhibits a reproducible population-level organization when the representation is constructed directly from the images without predefined semantic categories.

This leads to a more precise scientific question:

> **Can a population of 2D garment sketches be characterized as a quantitatively organized morphological population using explicit image-derived measurements without semantic supervision?**

---

# 2.7 Independent Representation as a Second Test of Morphology

A second limitation of relying on a single representation is that population structure may depend on the particular choice of descriptors.

A low-dimensional organization observed in one feature system could arise from properties specific to that representation. Consequently, agreement between independently constructed representations provides a stronger test than the existence of structure in a single coordinate system.

The present study therefore introduces a second geometric description based on radial-angular measurements.

The two representations are conceptually distinct:

\[
\mathbf{x}_i\in\mathbb{R}^{135}
\]

for the explicit morphology representation, and

\[
\mathbf{r}_i\in\mathbb{R}^{28}
\]

for the radial-angular representation.

The scientific question is not whether the two representations are mathematically identical. Rather, it is whether they recover reproducible information about the same underlying sketches:

\[
\boxed{
\mathbf{x}_i
\longleftrightarrow
\mathbf{r}_i
}
\]

relative to a row-permuted null:

\[
\boxed{
\mathbf{x}_i
\longleftrightarrow
\mathbf{r}_{\pi(i)}
}
\]

This provides a test of sketch-level correspondence between independently derived geometric descriptions.

---

# 2.8 From Correspondence to Complementarity

Correspondence alone does not imply that the two representations contain identical information.

If the radial-angular representation captures aspects of sketch geometry that are not fully represented by the morphology coordinates, it may provide additional predictive information in a downstream task.

The present study therefore distinguishes:

\[
\boxed{
\text{association}
}
\]

from

\[
\boxed{
\text{individual-sketch correspondence}
}
\]

and from

\[
\boxed{
\text{complementary utility}
}
\]

These are tested separately.

The downstream comparison is formulated as:

\[
\Delta M
=
M(\mathbf{X},\mathbf{R})
-
M(\mathbf{X}),
\]

where \(M\) denotes the chosen downstream performance measure.

Because adding dimensions alone can improve performance, dimensionality-matched controls are required before interpreting a positive \(\Delta M\) as evidence of complementary geometric information. Descriptor-block ablations provide a further test of whether any observed improvement is concentrated in a particular component of the radial-angular representation.

Thus, the contribution is not simply the introduction of another feature vector. It is the empirical testing of whether independently derived geometric descriptions agree and whether one provides additional information beyond the other.

---

# 2.9 Position of the Present Study

The present work therefore occupies the intersection of three established research traditions:

\[
\boxed{
\begin{array}{c}
\text{Geometric morphometrics}\\
\text{Fashion sketch geometry}\\
\text{Quantitative fashion morphology}
\end{array}
}
\]

The first provides the methodological principle that shape can be represented and analyzed quantitatively.

The second demonstrates that fashion sketches and flats contain recoverable geometric structure.

The third demonstrates that garment populations can exhibit statistically measurable morphological organization.

The present study combines these perspectives by treating a population of 2D garment sketches as the primary observational population and constructing an explicit image-derived morphology representation for its analysis.

It then introduces an independently derived radial-angular representation to test whether the observed organization is reproducible across geometric descriptions and whether the second representation contributes complementary information under a downstream task.

The resulting scientific logic is:

\[
\boxed{
\text{2D garment sketches}
\rightarrow
\text{explicit morphology}
\rightarrow
\text{population organization}
}
\]

followed by:

\[
\boxed{
\text{independent radial-angular representation}
\rightarrow
\text{cross-representation correspondence}
}
\]

and finally:

\[
\boxed{
\text{combined representation}
\rightarrow
\text{complementary downstream utility}
}
\]

---

# 2.10 Literature Gap and Research Questions

Based on the literature reviewed above, the gap addressed here is deliberately narrower than a claim that quantitative garment morphology is unexplored.

Existing work has already established:

- quantitative representations of fashion-flat contours;
- explicit geometric representations of garment sketches;
- statistical analysis of garment and silhouette populations;
- PCA and other dimensionality-reduction methods for fashion morphology;
- learned multimodal representations linking sketches to garment parameters and 3D garments.

What remains less established is whether a heterogeneous population of 2D garment sketches or technical flats can itself be treated as a morphological population in which geometric organization emerges directly from image-derived measurements without predefined semantic categories.

The present study therefore asks:

### Primary Research Question

> **Do garment sketches exhibit reproducible quantitative morphology organization that can be characterized directly from explicit image-derived morphology measurements without predefined semantic categories?**

### Secondary Research Question

> **Does an independently derived radial-angular representation capture geometric structure that is reproducibly associated with the morphology representation, recoverable from morphology at the sketch level, and complementary to morphology in a downstream discrimination task?**

The corresponding hypotheses are deliberately empirical rather than semantic:

\[
\boxed{
H_1:
\text{The 135-D morphology representation exhibits reproducible population-level organization.}
}
\]

\[
\boxed{
H_2:
\text{The independently derived radial-angular representation is associated with morphology at the population and sketch levels.}
}
\]

\[
\boxed{
H_3:
\text{The radial-angular representation provides complementary information beyond morphology under the tested downstream task.}
}
\]

The study does not interpret these findings as evidence for a universal semantic vocabulary, a compositional grammar, a mathematical manifold, causal mechanisms, or human-like visual understanding.

Instead, the intended contribution is narrower:

\[
\boxed{
\textbf{
an empirical quantitative geometric layer for characterizing
the morphology of 2D garment sketches.
}
}
\]

---

# 2.11 Summary of the Gap

The literature can therefore be summarized as:

\[
\boxed{
\begin{array}{lll}
\text{Bookstein / McCane}
&
\rightarrow
&
\text{quantitative shape and population geometry}
\\[4pt]
\text{Robson / Yasseen / Fondevilla / Wang}
&
\rightarrow
&
\text{computational geometry of fashion sketches}
\\[4pt]
\text{An \& Li / Lee \& Kim}
&
\rightarrow
&
\text{quantitative representations of fashion flats}
\\[4pt]
\text{Tsuru / Indrie}
&
\rightarrow
&
\text{population-level quantitative fashion morphology}
\\[4pt]
\hline
\text{Present study}
&
\rightarrow
&
\textbf{2D garment-sketch morphology population}
\\
&
&
\textbf{+ independent representation correspondence}
\\
&
&
\textbf{+ complementary-utility testing}
\end{array}
}
\]

Thus, the contribution is positioned not as the first use of geometric descriptors, PCA, or quantitative morphology in fashion, but as an empirical investigation of whether **2D garment sketches themselves exhibit reproducible quantitative morphological organization**, together with an independent test of that organization using a second geometric representation.