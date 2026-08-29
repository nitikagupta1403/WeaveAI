# 1. Introduction

Consider a garment sketch. Different regions of the drawing contribute different amounts of foreground evidence and may exhibit different directional organization. A narrow central region, a laterally extending structure, or a broad lower silhouette can therefore leave distinct geometric signatures.

A natural way to describe this variation is to organize the sketch radially. Imagine concentric shells placed around the sketch centroid. Within each shell, the foreground strokes define an angular distribution. Some shells contain little directional organization; others exhibit a pronounced undirected axis.

This leads to two local geometric questions: **how strongly is the sketch organized directionally at a given radial location, and along which axis is that organization expressed?**

We describe these quantities using the second circular harmonic of the shell-conditioned angular distribution. For shell \(r\), let \(p(\theta\mid r)\) denote the normalized angular distribution of foreground evidence. We define

\[
F_2(r)=\sum_k p(\theta_k\mid r)e^{-2\mathrm{i}\theta_k}.
\]

Its magnitude,

\[
R_2(r)=|F_2(r)|,
\]

measures the strength of second-harmonic directional organization, while its half-phase gives the corresponding undirected axial orientation,

\[
\alpha_2(r)
=
-\tfrac12\arg F_2(r)\pmod{\pi}
=
\tfrac12\operatorname{atan2}\!\left(S_2(r),C_2(r)\right)\pmod{\pi},
\]

under the adopted negative-exponential convention \(F_2=C_2-\mathrm{i}S_2\).

The use of the second harmonic follows directly from the geometry. A garment axis is undirected: an orientation at angle \(\theta\) is equivalent to one at \(\theta+\pi\). The second harmonic is the lowest non-zero circular harmonic that respects this \(180^\circ\) equivalence. The mathematics therefore follows the structure we want to describe rather than being selected retrospectively for classification performance.

Across radial shells, \(R_2(r)\) tells us **where directional organization is strong**, while \(\alpha_2(r)\) tells us **how that organization is oriented**.

**sketch → concentric shells → angular evidence → \(R_2(r)\): strength | \(\alpha_2(r)\): axis**

The resulting shell field is summarized by a compact 14-dimensional representation: eight coordinates describe the radial distribution of second-harmonic magnitude and six describe axial organization using doubled-angle coordinates. The representation is explicit, low-dimensional, and geometrically interpretable rather than learned as a latent embedding.

The next question is whether this geometric description carries information that is useful beyond conventional morphology.

CLO-SKET [1] provides an important setting in which to ask that question. The dataset contains 2,300 sketches from 23 garment categories, but these are not 2,300 independent garment instances. They correspond to 230 recoverable source-garment identities, with repeated sketches associated with each garment. Treating individual image files as independent could therefore place different drawings of the same garment in both training and test data.

We instead treat the complete source-garment identity as the indivisible unit of train/test separation, uncertainty resampling, and permutation. Validation therefore asks whether a representation transfers to **unseen recovered garments**, rather than merely to unseen image files.

With this dependency respected, the central predictive question becomes simple:

**Does axial–radial geometry add garment-category information beyond morphology when complete garment identities are withheld?**

Let \(\mathbf z_M\) denote the frozen 135-dimensional morphology representation and \(\mathbf z_{RA}\) the 14-dimensional axial–radial representation. For evaluation score \(\mathcal S\), the prespecified increment is

\[
\Delta_{RA}
=
\mathcal S(\mathbf z_M\oplus\mathbf z_{RA})
-
\mathcal S(\mathbf z_M).
\tag{1}
\]

A positive \(\Delta_{RA}\) shows that axial–radial geometry contributes predictive information under the tested protocol.

But predictive improvement raises a subtler question.

Suppose adding axial–radial geometry improves category discrimination. Does the improvement depend on pairing the geometry with the **exact same garment**, or could the representation mainly carry category-conditioned structure that remains useful when paired with another garment from the same category?

Ordinary feature concatenation cannot distinguish these possibilities.

We therefore deliberately break exact garment-level correspondence while preserving garment category and repeated-observation structure. Complete axial–radial identity blocks are reassigned within category, giving the comparison

\[
\mathcal S(\mathbf z_{M,i},\mathbf z_{RA,i})
\quad \text{versus} \quad
\mathcal S(\mathbf z_{M,i},\mathbf z_{RA,\pi(i)}).
\tag{2}
\]

If exact garment-level pairing contributes additional predictive information, the correctly aligned representation should outperform this category-preserving misalignment.

The study consequently unfolds as a sequence of connected questions. First, can radial and directional organization in garment sketches be represented explicitly? Second, does that geometry add predictive information beyond morphology when garment identities are respected during validation? Third, where does the added information arise, and does it depend on pairing the geometry with the exact same garment?

The experiments follow this progression. We first construct and characterize the axial–radial representation. We then evaluate the complete RA14 representation for incremental predictive value under garment-identity-disjoint validation and assess its behavior across repeated grouped partitions. Historical radial and axial ablations are retained as descriptive provenance but are not used to localize the corrected predictive increment. Finally, a category-preserving identity-block permutation separates predictive usefulness from exact garment-level correspondence. Rotation, reconstruction, discretization, harmonic, and phase-conditioning analyses provide complementary diagnostics of how the measurement behaves and where its numerical limits lie.

The evidence supports a correspondingly focused interpretation. The axial–radial representation contributes reproducible **category-conditioned geometric information beyond morphology**, while the correspondence control does not support the stronger claim that this advantage depends uniquely on exact garment-level pairing. A subsequent fresh reproducibility audit identified a limitation in raster harmonic-magnitude stability, narrowing the transformation-validity claim while leaving the separately frozen Experiment-06 predictive evidence unchanged.

The contribution is therefore both representational and methodological: an explicit description of **where directional organization occurs in a garment sketch and how it is oriented**, together with an identity-aware evaluation framework that distinguishes **predictive increment** from **instance-specific correspondence**.
