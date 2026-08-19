# 2. Related Work

## 2.1 Computational Representations of Fashion Sketches

Computational analysis of fashion sketches has developed along several distinct objectives, including garment reconstruction, design assistance, shape description, classification, and multimodal garment modeling. Across these studies, the sketch is generally treated as a geometric or visual input from which another computational representation is constructed, rather than as a population of morphological observations in its own right.

Geometry-driven approaches have demonstrated that substantial garment structure can be extracted directly from 2D sketches. Robson et al. interpreted garment silhouettes, boundaries, characteristic curves, and folds in the context of a 3D mannequin to construct plausible 3D garments. Their formulation introduced geometric constraints such as a spatially varying tightness field, thereby interpreting the sketch as a specification for garment geometry rather than as a conventional image-classification input.

Similarly, Yasseen et al. treated a garment sketch primarily as a geometric specification for constructing a quadrilateral mesh. Their method converts sketched garment boundaries into computationally useful mesh topology for subsequent garment simulation. The representation is therefore concerned with geometric construction and mesh connectivity rather than with learning a population-level representation of garment morphology.

Fondevilla et al. extended this geometric interpretation toward style transfer between 2D sketches and 3D garments. Their method decomposes sketch-derived style into proportionality, fit, silhouette shape, and fold appearance, and uses these geometric characteristics to construct garments on characters with different poses and morphologies. The resulting system demonstrates that meaningful garment-style information can be extracted from a single stylized sketch, but its objective remains 2D-to-3D garment generation rather than statistical analysis of variation across a sketch population.

A related multimodal formulation was proposed by Wang et al., who learned a shared latent space linking 2D sketches, garment and body parameters, and simulated 3D draped garments. Their synthetic dataset contains paired representations of the same garment-design instance, allowing mappings between these modalities to be learned jointly. Importantly, however, the PCA used in this work is applied to simulated 3D garment meshes as a compact representation of 3D geometry; the sketch itself is represented through DenseNet features. The resulting latent space therefore serves multimodal garment design and retargeting rather than population-level discovery of sketch morphology.

These approaches establish an important precedent:

\[
\boxed{
\text{2D fashion sketches contain computationally recoverable geometric information}
}
\]

However, they largely formulate the sketch as an input to a downstream task---reconstruction, simulation, design, transfer, or multimodal prediction. They do not primarily ask whether the geometry of a collection of sketches itself possesses an organized morphology.

---

## 2.2 Explicit Geometric Representations of Fashion Flats

Fashion-flat research provides an additional line of evidence that garment drawings can be represented explicitly in terms of geometric structure.

An and Li developed a Wavelet Fourier Descriptor (WFD) for fashion-flat-sketch classification. Their method converts garment contours into centroid-distance signals and combines wavelet and Fourier analysis to obtain a transformation-invariant shape descriptor. The resulting descriptor is used for multiclass classification.

This work is particularly relevant because it establishes that fashion-flat contours can be converted into mathematically defined quantitative shape representations. However, the scientific role of the representation is discriminative: the descriptor functions as a shape signature for classification. The study does not investigate whether a population of fashion flats forms a continuous morphological space or whether independent geometric descriptions recover common population structure.

Lee and Kim provide another explicit geometric formulation through modular representation of fashion flats. Their system decomposes flats into reusable garment components such as bodices, sleeves, collars, cuffs, and pockets, and automatically aligns and assembles these modules.

The geometric transformations in this framework---including translation, rotation, and scaling---should be distinguished from statistical coordinate transformations such as PCA. Module alignment physically transforms a garment component in object space, whereas PCA changes the coordinate basis in which variation across observations is expressed.

Thus, existing fashion-flat research already establishes two important capabilities:

\[
\boxed{
\text{fashion flat}
\rightarrow
\text{quantitative contour representation}
}
\]

and

\[
\boxed{
\text{fashion flat}
\rightarrow
\text{explicit garment modules}
}
\]

What remains different is the scientific question. These representations are used for classification or design assembly, rather than for investigating the statistical organization of morphology across a population of flats or sketches.

---

## 2.3 Quantitative Shape and Geometric Morphometrics

The methodological foundation for treating visual forms as quantitative morphological objects comes from geometric morphometrics.

Bookstein introduced a framework for analyzing outlines that lack conventional anatomical landmarks through semilandmarks. Because arbitrary positions along a curve do not necessarily correspond to meaningful morphological locations, semilandmarks can slide along the tangent direction to reduce variation attributable to arbitrary point placement.

This establishes a fundamental methodological principle:

\[
\boxed{
\text{geometric representation}
\neq
\text{meaningful morphology automatically}
}
\]

The correspondence criterion used to construct the representation therefore matters. Later methodological analysis by Mitteroecker and Schaefer emphasizes that bending-energy minimization and Procrustes-distance minimization optimize different mathematical objectives, and that geometric correspondence cannot automatically be equated with biological homology.

More generally, their review emphasizes that a mathematically valid representation does not automatically constitute a biologically meaningful representation. Interpretation must remain connected to the scientific question, the structure being measured, and the relevant notion of correspondence.

For the present study, this distinction is important. The goal is not simply to construct a mathematically convenient feature vector. The representation must be evaluated according to whether its dimensions capture reproducible and interpretable variation in garment drawings.

---

## 2.4 From Individual Outlines to Population Shape Spaces

McCane provides a methodological bridge from individual outline representation to population-level shape analysis.

Rather than requiring a fixed set of corresponding points on every outline, McCane formulates a distance between complete outlines. For a population of shapes

\[
S_1,\ldots,S_N,
\]

the pairwise distances

\[
d(S_i,S_j)
\]

define a distance matrix describing the geometry of the population. This matrix can subsequently be embedded into a lower-dimensional Euclidean representation, allowing population-level variation to be visualized and analyzed.

The conceptual transition is therefore:

\[
\boxed{
\text{individual outline}
\rightarrow
\text{shape distance}
\rightarrow
\text{population geometry}
}
\]

This differs fundamentally from using shape merely as a feature for classification. In McCane's formulation, the population geometry itself becomes the object of scientific analysis.

Nevertheless, this framework is developed for general biological/morphological outlines and does not establish garment-specific morphology, fashion-sketch semantics, garment primitives, or semantic relationships between garment components.

McCane therefore establishes the methodological legitimacy of studying a population of outlines through their shape relationships, but does not answer whether 2D fashion sketches constitute such a morphological population.

---

## 2.5 Quantitative Morphology Has Already Reached Fashion Silhouettes

Importantly, the literature also identifies direct precedent for population-level quantitative analysis within fashion itself.

Tsuru et al. analyzed 223 garment images from luxury fashion collections, representing each garment using 11 standardized measurements corresponding to garment-design locations such as neck, shoulder, waist, hips, hem, knee, and length. Multivariate analysis using multidimensional scaling and hierarchical clustering was then used to visualize and organize silhouette variation.

Thus, a genuine fashion morphology pipeline already exists:

\[
\boxed{
\text{garment population}
\rightarrow
\text{geometric measurements}
\rightarrow
\text{multivariate analysis}
\rightarrow
\text{silhouette space}
}
\]

Indrie et al. provide a more recent related study. Their analysis includes 29 dress silhouettes, 40 skirt silhouettes, and 19 neckline silhouettes. Each silhouette is converted into explicit geometric descriptors, including measurements of axes, perimeter, area, and related form factors, followed by feature selection and PCA.

The resulting representation is explicitly constructed before statistical analysis:

\[
\boxed{
\text{silhouette image}
\rightarrow
\text{geometric measurements}
\rightarrow
\text{form coefficients}
\rightarrow
\text{PCA}
}
\]

rather than directly learning an embedding from image pixels.

This literature therefore closes an important potential gap. It would no longer be defensible to state that quantitative morphological analysis has not been applied to fashion. It clearly has.

The relevant distinction is instead the nature of the observational population.

Tsuru et al. analyze photographed garments, while Indrie et al. analyze predefined silhouette representations collected from the literature. Neither study, as represented in the reviewed material, establishes a population of raw or technical 2D fashion sketches/flats as the primary morphological observations.

---

## 2.6 The Remaining Gap

Taken together, the literature reveals a progression:

\[
\boxed{
\text{fashion sketch}
\rightarrow
\text{geometric representation}
}
\]

has been established;

\[
\boxed{
\text{fashion contour}
\rightarrow
\text{quantitative descriptor}
\rightarrow
\text{classification}
}
\]

has been established;

\[
\boxed{
\text{fashion silhouette population}
\rightarrow
\text{geometric measurements}
\rightarrow
\text{statistical morphology}
}
\]

has also been established;

and general geometric-morphometric research has established:

\[
\boxed{
\text{outline population}
\rightarrow
\text{shape space}
\rightarrow
\text{morphological variation}
}
\]

as a principled methodological framework.

What is less established in the reviewed literature is the intersection of these lines:

\[
\boxed{
\textbf{
\text{population of 2D fashion sketches/flats}
\rightarrow
\text{explicit geometric morphology}
\rightarrow
\text{statistical population structure}
}
}
\]

In particular, the reviewed studies do not establish whether a heterogeneous population of 2D fashion sketches can be treated directly as morphological observations without first imposing predefined silhouette categories, nor whether independently constructed geometric representations of the same sketches recover corresponding population structure.

This distinction is critical because it changes the scientific question from:

> *Can fashion sketches be classified or represented?*

to:

> **Does the geometry of fashion sketches itself contain a reproducible morphological organization?**

The latter is a question about the structure of the observation population rather than the performance of a downstream classifier or generator.

---

## 2.7 Relation to the Present Study

The present study therefore builds on several established methodological traditions while combining them at a different analytical level.

First, geometric-morphometric research provides the conceptual basis for treating shape as a quantitative object and emphasizes the need to justify correspondence and representation choices.

Second, outline-shape methods demonstrate how populations of curves can be represented through pairwise shape relationships and embedded into low-dimensional shape spaces.

Third, fashion research demonstrates that garment contours and silhouettes can be converted into explicit geometric descriptors and statistically analyzed.

Finally, fashion-flat and sketch-based computational systems demonstrate that garment drawings contain structured geometric information that can support classification, module assembly, 3D reconstruction, and multimodal garment modeling.

The present study asks whether these ideas can be brought together to investigate the morphological organization of a population of 2D fashion sketches themselves.

The distinction can be summarized as:

\[
\boxed{
\begin{array}{c}
\text{Prior fashion-CV work}\\
\downarrow\\
\text{representation for a task}
\end{array}
}
\]

versus

\[
\boxed{
\begin{array}{c}
\text{Present study}\\
\downarrow\\
\text{representation as an object of morphological investigation}
\end{array}
}
\]

The study therefore does not claim novelty for individual descriptors, PCA, geometric measurements, or the underlying sketch dataset. Rather, its scientific question concerns whether these explicit measurements can provide a reproducible coordinate system in which morphological organization of garment sketches emerges independently of predefined semantic categories.

---

## 2.8 Literature Gap and Hypothesis

The literature therefore supports a specific rather than absolute gap:

> **Existing work has demonstrated quantitative representations of fashion contours, modular geometric representations of fashion flats, and population-level statistical analysis of garment silhouettes. However, the reviewed literature does not establish whether a heterogeneous population of 2D fashion sketches or technical flats can itself be treated as a morphological population in which geometric organization emerges directly from sketch geometry, independent of predefined semantic categories.**

This leads to the central hypothesis of the present study:

\[
\boxed{
\textbf{
2D fashion sketches contain a reproducible geometric organization
that can be characterized as a morphological population.
}
}
\]

A stronger version of the hypothesis can then be tested through representation correspondence:

\[
\boxed{
\text{independent geometric representations}
\rightarrow
\text{corresponding population structure}
}
\]

If independently constructed representations recover similar relationships among sketches, the resulting structure is less likely to be an artifact of a particular feature encoding.

This moves the study beyond the question of whether a descriptor is useful for classification and toward the more fundamental question of whether fashion sketch geometry exhibits an underlying, reproducible organization that can serve as a basis for computational morphological analysis.