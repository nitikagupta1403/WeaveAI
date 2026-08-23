# CLO-SKET — IVC Submission Manuscript

> **Submission front matter to complete before journal upload**
>
> - Final manuscript title: Garment Sketches to Axial–Radial Representations
> - Author names: NITIKA GUPTA
> - Affiliations: [TO BE CONFIRMED]
> - Corresponding author and email: [TO BE CONFIRMED]
>
> The scientific body below is assembled from the frozen repository source files. Do not edit scientific claims in this master independently; edit the canonical source section and rebuild instead.

---

# Abstract

Garment sketches encode shape through the radial and angular distribution of foreground structure. We introduce an explicit axial–radial representation of garment-sketch geometry based on the shell-conditional angular distribution \(p(\theta\mid r)\). Its second harmonic \(F_2(r)\) provides a radial magnitude \(R_2(r)\) and an axial orientation \(\alpha_2(r)\). The choice \(m=2\) follows directly from axial symmetry, \(\theta\equiv\theta+\pi\). These quantities are summarized by a 14-dimensional representation comprising eight radial and six axial descriptors.

The representation is evaluated on all 2,300 CLO-SKET sketches from 230 garment identities using garment-identity-disjoint validation. Reconstruction of the second-harmonic field from radius and magnitude achieves whole-field \(R_2\) RMSE \(=0.1456\), Pearson \(r=0.9264\), and median peak-shell axial error \(=4.10^\circ\). Rigid-image rotations exhibit the expected invariant/equivariant behavior, whereas independently rotating garment identities increases median axial error to \(44.68^\circ\), close to the \(45^\circ\) axial chance level. Thus, harmonic magnitude does not determine phase; successful phase recovery depends substantially on shared orientation structure.

The proposed representation provides a compact and interpretable description of garment-sketch geometry whose coordinate dependence, numerical sensitivity, and statistical limits can be tested explicitly.

**Keywords:** garment sketches; axial–radial representation; axial harmonics; Fourier descriptors; grouped cross-validation; rotation equivariance; phase conditioning

---

# 1. Introduction

Garment sketches encode design form through sparse foreground geometry. A small number of lines can establish silhouette, proportion, symmetry, and dominant orientation before a garment is physically realized. This motivates a measurement question distinct from recognition or generation: **can garment-sketch geometry be represented explicitly while keeping its construction, assumptions, dependencies, and limits mathematically visible?**

Most computational work involving garment sketches has focused on downstream tasks, including garment modelling, fashion-flat classification, multimodal design, image synthesis, retrieval, and sewing-pattern reconstruction (Yasseen et al., 2013; An and Li, 2014; Wang et al., 2018; Fondevilla et al., 2021; Baldrati et al., 2023; Cao et al., 2023; Zhang et al., 2024; Singh and Patras, 2024; Huang et al., 2025; Bui et al., 2026; Cao et al., 2026). These studies establish that sketches contain computationally useful information, but task performance does not necessarily reveal which geometric properties carry that information or how strongly a representation depends on coordinate and discretization choices.

Here we treat each sketch as an observed geometric object. Foreground intensity is expressed relative to an intensity-weighted centroid and accumulated in radial and angular bins. Within radial shell \(r\), normalization over angle gives the conditional distribution \(p(\theta\mid r)\). Its angular Fourier moments are

\[
F_m(r)=\sum_k p(\theta_k\mid r)e^{-\mathrm{i}m\theta_k}.
\]

The primary statistic is the second harmonic \(F_2(r)=C_2(r)-\mathrm{i}S_2(r)\), with magnitude \(R_2(r)=|F_2(r)|\) and axial orientation

\[
\alpha_2(r)=\frac12\operatorname{atan2}(S_2(r),C_2(r))\pmod{\pi}.
\]

The choice \(m=2\) follows from axial symmetry rather than retrospective model performance. Because an undirected axis satisfies \(\theta\equiv\theta+\pi\), \(F_m(\theta+\pi)=(-1)^mF_m(\theta)\); hence \(m=2\) is the lowest non-zero harmonic invariant under axial reversal.

The shell-level field is summarized by an explicit 14-dimensional representation: eight descriptors of radial second-harmonic magnitude and six doubled-angle axial descriptors. Algebraically redundant quantities are excluded, and axial directions are encoded in doubled-angle Cartesian form rather than as raw Euclidean angles.

We then ask how much of the observed second-harmonic Cartesian field can be reconstructed for unseen garment identities when only \([r,R_2(r)]\) is provided. This is a deliberately restricted information-reduction experiment: magnitude does not mathematically determine phase, and predictors and targets arise from the same observed angular field. Reconstruction is therefore interpreted as a shared-source consistency diagnostic, not as semantic or physical recovery.

Three additional design features constrain that interpretation. First, rigid-image, analytic global-rotation, and garment-identity-randomized rotation controls distinguish transformation behavior from dependence on a shared canonical image frame. Second, parameter and discretization analyses test sensitivity to support threshold, concentration width, angular and radial resolution, and radial-domain boundaries. Third, because phase becomes poorly conditioned as \(R_2\to0\), reconstruction error is interpreted jointly through harmonic magnitude and Cartesian perturbation rather than attributing angular error to magnitude alone.

CLO-SKET contains repeated sketches of source garments (Arnia, 2020). We recover 230 category-qualified garment identities from 2,300 sketches and therefore validate at the garment-identity level: complete identities are withheld during cross-validation, resampled during bootstrap uncertainty estimation, and reduced to garment-level summaries for category-stratified permutation inference.

The study addresses five questions: whether garment-sketch geometry admits an explicit 14-dimensional axial–radial representation; how much second-harmonic structure can be reconstructed for unseen garment identities and how strongly this depends on the coordinate frame; which descriptors remain stable under reasonable measurement perturbations; whether \(m=2\) is consistent with its axial-symmetry rationale; and whether observed angular error follows the expected phase-conditioning geometry.

The contribution is an auditable geometric measurement framework linking representation, coordinate dependence, numerical sensitivity, validation unit, uncertainty, and scope of inference. It does not claim semantic garment-part recognition, causal geometric laws, human-like visual understanding, a universally optimal harmonic order or radial domain, prospective reliability classification, likelihood-based circular modelling, or reconstruction of the complete angular density.

---

# 2. Related Work

## 2.1 Garment sketches as computational inputs

Garment sketches have been used for reconstruction, synthesis, editing, retrieval, and pattern generation. Geometry-oriented systems converted mannequin-guided sketches into garment meshes (Yasseen et al., 2013), linked sketched folds to sewing-pattern parameters and simulated garments (Wang et al., 2018), transferred sketch style to three-dimensional characters (Fondevilla et al., 2021), and more recently inferred sewing patterns from a single sketch (Huang et al., 2025).

A parallel line of work treats the sketch primarily as a conditioning signal. Multimodal Garment Designer combines sketches with text and pose for fashion editing (Baldrati et al., 2023); TexControl constrains garment outline before texture refinement (Zhang et al., 2024); FashionSD-X combines sketch and text conditioning for garment synthesis (Singh and Patras, 2024); and Cao et al. (2023) condition compatible-clothing generation on sketches and reference garments. Recent benchmarks further expand sketch-conditioned fashion tasks: GarmentSketch contains 26,249 sketches across 21 categories for sketch-guided image generation (Bui et al., 2026), while VietFashion studies sketch-text composed retrieval with culturally specific garments (Cao et al., 2026).

These studies establish the computational value of garment sketches, but their principal objective is downstream performance. CLO-SKET instead treats repeated sketches as a geometric measurement population and asks whether their structure can be represented explicitly and validated with its dependencies visible.

## 2.2 Explicit shape representations

Explicit numerical descriptions of garment form predate current generative systems. An and Li (2014) combined wavelet Fourier descriptors with supervised dimensionality reduction for fashion-flat classification, while Tsuru et al. (2021) represented garment silhouettes through standardized measurements and analysed designer collections using multidimensional scaling and clustering. More generally, Fourier descriptors provide classical representations of periodic outlines (Zahn and Roskies, 1972), and geometric morphometrics provides complementary approaches to curve and shape analysis (Bookstein, 1997; McCane, 2013).

Frequency-domain representations also appear in modern garment synthesis. Liang et al. (2023), for example, used Fast Fourier Transform features to model periodic texture structure in controllable garment-image generation. That objective differs from CLO-SKET: here angular harmonics describe the spatial distribution of sketch foreground geometry rather than synthesized texture.

CLO-SKET therefore does not claim novelty for Fourier analysis, polar coordinates, or shape descriptors individually. Its contribution is their use in an auditable radial–angular measurement framework that explicitly tests coordinate dependence, discretization sensitivity, repeated-measure structure, and inferential limits.

## 2.3 Axial harmonic representation

For centroid-relative polar coordinates \((r,\theta)\), CLO-SKET estimates a shell-conditional angular distribution \(p(\theta\mid r)\) and summarizes it by Fourier moments \(F_m(r)\). The primary order is \(m=2\), because axial orientations satisfy \(\theta\equiv\theta+\pi\): odd harmonics change sign under a \(180^\circ\) reversal, whereas even harmonics are invariant. Thus \(m=2\) is the lowest non-zero harmonic compatible with axial symmetry. A prespecified \(m=1,2,3,4\) control evaluates the observed low-order spectrum without treating harmonic order as a post-hoc model-selection parameter.

For \(F_2=C_2-\mathrm{i}S_2\), the magnitude \(R_2=\sqrt{C_2^2+S_2^2}\) measures second-harmonic axial organization and \(\alpha_2=\tfrac12\operatorname{atan2}(S_2,C_2)\pmod{\pi}\) gives its undirected orientation, following doubled-angle treatment of axial data (Jammalamadaka and SenGupta, 2001). Because \(R_2^2=C_2^2+S_2^2\) is an identity, these quantities are not treated as independent evidence. The final representation summarizes the field using eight radial-magnitude and six axial-orientation descriptors without PCA or a learned embedding.

## 2.4 Measurement dependence and validation

Interpretability also requires testing dependence on coordinate and numerical conventions. Under physical rotation by \(\phi\), \(F_2'(r)=e^{-\mathrm{i}2\phi}F_2(r)\): \(R_2\) is invariant while the harmonic components and axial phase transform with the coordinate frame. CLO-SKET therefore uses rigid-image, global analytic, and garment-identity-randomized rotation controls to separate intrinsic magnitude structure from population-level orientation alignment.

The measurement additionally depends on finite radial and angular binning and on support, concentration, and radial-domain choices. Sensitivity analyses therefore perturb these specifications while keeping the primary representation frozen. Broad radial summaries are distinguished from localized quantities such as peak, onset, and termination, which are expected to be more resolution- and boundary-dependent.

Repeated observations introduce a separate dependency. CLO-SKET contains multiple sketches associated with recovered source-garment identities. Primary validation therefore assigns complete garment identities to folds, bootstrap resampling operates at the garment-identity level, and confirmatory association analysis reduces repeated sketches to garment-level summaries before within-category permutation. This design evaluates transfer to unseen garments rather than merely unseen image files.

## 2.5 Study position

Recent work has substantially advanced sketch-conditioned fashion generation, retrieval, editing, and sewing-pattern reconstruction, while classical shape analysis provides explicit numerical descriptions of form. A narrower gap remains in treating repeated garment sketches as a statistical measurement population while simultaneously exposing representation, algebraic dependency, coordinate dependence, parameter sensitivity, validation unit, uncertainty, and claim boundaries.

CLO-SKET addresses this measurement problem. It evaluates an explicit 14-dimensional axial–radial representation, its second-harmonic reconstruction for unseen garment identities, its behavior under coordinate perturbation, its sensitivity to measurement choices, and the conditioning of axial reconstruction error. The intended contribution is an auditable geometric representation and validation framework, not semantic garment understanding, causal geometric inference, complete angular-density reconstruction, or a claim of universally optimal harmonic or radial parameters.

---

# 3. Methods

## 3.1 Study design and scope

CLO-SKET is analysed as a repeated-sketch geometric measurement dataset. The pipeline is fixed in the following order: raw-image foreground extraction; centroid-relative radial–angular construction; shell-conditional angular normalization; second-harmonic measurement; 14-dimensional descriptor extraction; garment-identity-disjoint reconstruction; rotation and coordinate-frame controls; parameter/discretization sensitivity; low-order harmonic control; phase-conditioning analysis; and garment-level uncertainty and association inference.

All primary quantities are computed from observed sketch geometry. Reconstruction is used only as a shared-source consistency diagnostic and is evaluated on unseen recovered garment identities. No semantic garment labels, learned embeddings, or post-hoc feature selection are used to construct the representation.

## 3.2 Dataset and garment-identity reconstruction

The analysis used all 2,300 images in the CLO-SKET dataset, organized into 23 garment categories. Garment identity was reconstructed from the category-qualified source identifier encoded in each filename. The accompanying replicate identifier denoted the repeated sketch associated with that source garment.

This procedure recovered

\[
N_{\mathrm{id}}=230
\]

garment identities, exactly 10 within each category. Individual identities contained 9–11 sketches because of irregular filename records.

All 2,300 file paths were unique. SHA-256 hashing detected no repeated raw files, and hashing of decoded pixel arrays detected no repeated decoded images. Perceptual hashing was used only to identify visually similar candidate pairs and was not interpreted as evidence of file duplication or shared lineage.

Recovered garment identity was treated as the indivisible clustering unit for cross-validation, bootstrap resampling, and confirmatory association analysis. The available metadata do not establish that the 230 recovered garment identities constitute mutually independent population sampling units; population-level inference is therefore conditional on that assumption.

---

## 3.3 Raw-image radial–angular construction

The radial–angular representation was constructed directly from the original grayscale TIFF images at their native spatial resolution. No foreground thresholding, binarization, resizing, rotation, straightening, or principal-axis alignment was applied in this branch.

For sketch \(i\), let \(I_{ip}\in[0,255]\) denote the grayscale intensity of pixel \(p\). Continuous foreground darkness was defined as

\[
w_{ip}
=
\max\left(255-I_{ip},\,0\right).
\]

Thus darker sketch pixels contribute more mass, while white background pixels contribute zero mass.

For an image of width \(W_i\) and height \(H_i\), a common isotropic scale was defined as

\[
S_i
=
\max(W_i,H_i).
\]

Pixel coordinates \((u_{ip},v_{ip})\) were mapped to an aspect-ratio-preserving isotropic coordinate system,

\[
x_{ip}
=
\frac{u_{ip}-(W_i-1)/2
}{
S_i
},
\qquad
y_{ip}
=
\frac{
v_{ip}-(H_i-1)/2
}{
S_i
}.
\]

The same scale factor was used for both axes, so portrait sketches were not independently stretched along \(x\) and \(y\).

The darkness-weighted centroid was

\[
c_{x,i}
=
\frac{
\sum_p w_{ip}x_{ip}
}{
\sum_p w_{ip}
},
\qquad
c_{y,i}
=
\frac{
\sum_p w_{ip}y_{ip}
}{
\sum_p w_{ip}
}.
\]

Centroid-relative coordinates were then

\[
\widetilde x_{ip}
=
x_{ip}-c_{x,i},
\qquad
\widetilde y_{ip}
=
y_{ip}-c_{y,i},
\]

with Euclidean radius

\[
R_{ip}
=
\sqrt{
\widetilde x_{ip}^{\,2}
+
\widetilde y_{ip}^{\,2}
},
\]

and polar angle

\[
\theta_{ip}
=
\operatorname{atan2}
\left(
\widetilde y_{ip},
\widetilde x_{ip}
\right).
\]

To remove sketch-specific overall scale while preserving internal radial proportions, radius was normalized separately within each sketch:

\[
R_{i,\max}
=
\max_p R_{ip},
\]

\[
\rho_{ip}
=
\frac{
R_{ip}
}{
R_{i,\max}
},
\qquad
0\leq\rho_{ip}\leq1.
\]

The normalized radial coordinate was divided into 72 equal-width bins with edges

\[
e_j^{(r)}
=
\frac{j}{72},
\qquad
j=0,\ldots,72.
\]

The corresponding normalized radial-bin centres were

\[
\rho_j
=
\frac{
j+\tfrac12
}{
72
},
\qquad
j=0,\ldots,71.
\]

For reporting and descriptor construction, these centres were expressed in shell-coordinate units,

\[
r_j
=
72\rho_j
=
j+\frac12,
\]

so that the full radial grid is

\[
r_j
=
0.5,1.5,\ldots,71.5.
\]

Angular position was divided into 72 equal-width bins over

\[
[-\pi,\pi],
\]

with edges

\[
e_k^{(\theta)}
=
-\pi
+
k\frac{2\pi}{72},
\qquad
k=0,\ldots,72.
\]

Each angular bin therefore spans

\[
5^\circ.
\]

Let

\[
H_i(r_j,\theta_k)
\]

denote the accumulated darkness mass of pixels assigned jointly to radial bin \(j\) and angular bin \(k\):

\[
H_i(r_j,\theta_k)
=
\sum_p
w_{ip}
\,
\mathbf 1
\left[
\rho_{ip}\in B_j^{(r)}
\right]
\mathbf 1
\left[
\theta_{ip}\in B_k^{(\theta)}
\right].
\]

Pixels with \(\rho_{ip}=1\) were retained in the final radial bin.

For radial shell \(r_j\), define its accumulated darkness mass as

\[
M_i(r_j)
=
\sum_{k=1}^{72}
H_i(r_j,\theta_k).
\]

For nonempty shells,

\[
M_i(r_j)>10^{-14},
\]

the conditional angular distribution was

\[
p_i(\theta_k\mid r_j)
=
\frac{
H_i(r_j,\theta_k)
}{
M_i(r_j)
},
\]

so that

\[
\sum_{k=1}^{72}
p_i(\theta_k\mid r_j)
=
1.
\]

Empty radial shells were represented by zeros.

This shell conditioning separates angular organization from the amount of foreground mass present at a given radius. Consequently, radial shells containing more total ink do not dominate the angular statistic solely because they contain more foreground intensity.

---

## 3.4 Rigid-image rotation control of the 14-dimensional representation

The analytic rotation controls described later test coordinate-frame dependence directly in second-harmonic space. A separate image-domain perturbation control was performed to verify that the final 14-dimensional representation exhibits the intended invariant and equivariant behavior when the input sketch itself is rigidly rotated and the complete radial-angular measurement is recomputed.

All 2,300 sketches were evaluated at the physical rotation angles

\[
\phi
\in
\{-20^\circ,-10^\circ,-5^\circ,0^\circ,5^\circ,10^\circ,20^\circ\}.
\]

This control was label-free and did not fit or refit any predictive model.

To prevent clipping of the original rectangular sketch under rotation, each grayscale image was first embedded in a square white canvas whose side length was at least the diagonal of the original image,

\[
L_i
=
\left\lceil
\sqrt{H_i^2+W_i^2}
\right\rceil,
\]

with a one-pixel parity adjustment where required to maintain centered embedding. The same padded canvas was used for the reference condition and every rotated condition.

For non-zero \(\phi\), the padded grayscale image was rotated using bilinear interpolation with fixed canvas size,

\[
\texttt{expand=False},
\]

and white background fill,

\[
\texttt{fillcolor}=255.
\]

The \(0^\circ\) condition used the same padded canvas without interpolation.

After rotation, the complete radial-angular construction was rerun from the rotated grayscale image using the same frozen measurement procedure as for the primary representation. No descriptor definition, radial domain, angular discretization, or post-processing rule was changed for the rotation control.

For second-harmonic magnitude, a rigid physical rotation ideally satisfies

\[
F_2'(r)
=
e^{-i2\phi}F_2(r),
\]

so that

\[
R_2'(r)
=
R_2(r).
\]

Accordingly, radial and magnitude-derived quantities were evaluated as approximately rotation-invariant numerical descriptors.

For an axial orientation \(\alpha\),

\[
\alpha'
=
\alpha+\phi
\pmod{\pi}.
\]

Its doubled-angle Cartesian representation therefore transforms as

\[
\begin{bmatrix}
\cos 2\alpha'\\
\sin 2\alpha'
\end{bmatrix}
=
\begin{bmatrix}
\cos 2\phi & -\sin 2\phi\\
\sin 2\phi & \cos 2\phi
\end{bmatrix}
\begin{bmatrix}
\cos 2\alpha\\
\sin 2\alpha
\end{bmatrix}.
\]

Thus, the peak-orientation and magnitude-weighted mean-orientation coordinate pairs were evaluated as axial-equivariant quantities under the expected \(R(2\phi)\) action.

Axial coherence,

\[
\kappa_i,
\]

and orientation drift,

\[
\delta_i,
\]

were treated as rotation-invariant scalar descriptors because they depend on relative rather than absolute axial orientation.

Numerical stability of the radial-magnitude field was summarized by the normalized mean absolute error of the primary-domain \(R_2(r)\) profile relative to the \(0^\circ\) reference. Axial equivariance was evaluated by decoding the rotated doubled-angle orientation pairs and comparing the observed orientation shift with the imposed physical rotation. Coherence and orientation drift were evaluated by their absolute changes from the reference condition.

This perturbation control evaluates empirical numerical behavior under the tested rotations only. It does not imply exact invariance under arbitrary image transformations, nor robustness beyond the evaluated rotation range.

---

## 3.5 Angular harmonics and axial orientation

For harmonic order \(m\), the complex angular moment at radial shell \(r_j\) was

\[
F_{m,i}(r_j)
=
\sum_{k=1}^{72}
p_i(\theta_k\mid r_j)
e^{-\mathrm{i}m\theta_k}.
\]

The negative exponential follows the discrete Fourier-transform convention used in the implementation.

The primary analysis uses \(m=2\):

\[
F_{2,i}(r_j)
=
C_{2,i}(r_j)
-
\mathrm{i}S_{2,i}(r_j),
\]

where

\[
C_{2,i}(r_j)
=
\sum_k
p_i(\theta_k\mid r_j)
\cos(2\theta_k),
\]

and

\[
S_{2,i}(r_j)
=
\sum_k
p_i(\theta_k\mid r_j)
\sin(2\theta_k).
\]

The second-harmonic magnitude is

\[
R_{2,i}(r_j)
=
|F_{2,i}(r_j)|
=
\sqrt{
C_{2,i}(r_j)^2+
S_{2,i}(r_j)^2
}.
\]

For notational convenience,

\[
m_i(r_j)
\equiv
R_{2,i}(r_j).
\]

The associated axial orientation is

\[
\alpha_{2,i}(r_j)
=
\frac12
\operatorname{atan2}
\left(
S_{2,i}(r_j),
C_{2,i}(r_j)
\right)
\pmod{\pi}.
\]

Because orientation is axial rather than directional,

\[
\alpha
\equiv
\alpha+\pi.
\]

Axial angular distance was therefore defined as

\[
d_{\mathrm{ax}}(a,b)
=
\min
\left[
|a-b|\bmod\pi,\,
\pi-(|a-b|\bmod\pi)
\right],
\]

which lies on

\[
[0,\pi/2].
\]

Reported angular errors are expressed on the equivalent interval

\[
[0^\circ,90^\circ].
\]

---

## 3.6 Why the second harmonic is the primary angular statistic

The primary harmonic order is fixed by axial symmetry. For an undirected orientation,

\[
\theta\equiv\theta+\pi.
\]

Therefore,

\[
F_m(\theta+\pi)=(-1)^mF_m(\theta).
\]

Odd harmonics reverse sign under a \(180^\circ\) reversal, whereas even harmonics are invariant. The second harmonic is thus the lowest non-zero harmonic compatible with the axial quantity represented here. Higher even orders describe finer angular structure but do not replace this lowest-order axial statistic. A prespecified \(m=1,2,3,4\) analysis (Section 3.14) is used as a control of the observed low-order spectrum, not as post-hoc harmonic selection.

## 3.7 Primary radial domain and peak quantities

The reported shell coordinate \(r_j=j+\tfrac12\) is a dimensionless bin-coordinate representation of the sketch-normalized radius \(\rho_j=(j+\tfrac12)/72\); it is not a physical pixel distance.

The primary radial analysis was defined on 25 shell centers,

\[
\mathcal R
=
\{3.5,4.5,\ldots,27.5\}.
\]

For sketch \(i\), the observed peak shell was

\[
j_i^\star
=
\arg\max_{j:r_j\in\mathcal R}
m_i(r_j),
\]

with peak radius

\[
r_i^\star
=
r_{j_i^\star},
\]

and peak magnitude

\[
m_i^\star
=
m_i(r_i^\star).
\]

Because

\[
m_i(r)=R_{2,i}(r)=|F_{2,i}(r)|,
\]

the identities

\[
m_i^\star
=
R_{2,i}(r_i^\star)
=
|F_{2,i}(r_i^\star)|
\]

refer to the same measured quantity and are not treated as independent evidence.

Peak radius is the location of a discrete argmax on a finite domain. It was therefore treated as a localized, window-dependent statistic, and its boundary occupancy and radial-domain sensitivity were evaluated explicitly.

---

## 3.8 Eight radial-magnitude descriptors

Let

\[
m_i(r)=R_{2,i}(r)
\]

over the primary domain \(\mathcal R\). Integrals were evaluated using the trapezoidal rule at radial-shell centers. Their units are radial-bin-coordinate units rather than physical distance, and the integrated magnitude is not interpreted as Fourier energy.

### Integrated magnitude

\[
I_i
=
\int_{\mathcal R}
m_i(r)\,dr.
\]

### Magnitude-weighted radial centroid

\[
\bar r_i
=
\frac{
\int_{\mathcal R}
r\,m_i(r)\,dr
}{
I_i
}.
\]

### Magnitude-weighted radial spread

\[
s_{r,i}
=
\sqrt{
\frac{
\int_{\mathcal R}
(r-\bar r_i)^2m_i(r)\,dr
}{
I_i
}
}.
\]

### Peak concentration

With \(r_i^\star\) denoting the discrete peak location, radial concentration was defined as the fraction of integrated magnitude within four shell-coordinate units of the peak,

\[
q_i
=
\frac{
\int_{
\mathcal R\cap
[r_i^\star-4,r_i^\star+4]
}
m_i(r)\,dr
}{
I_i
}.
\]

### Support onset and termination

Let

\[
\tau_i
=
0.10\,m_i^\star.
\]

The support onset and termination radii were

\[
r_i^{\mathrm{on}}
=
\min
\{
r\in\mathcal R:
m_i(r)\geq\tau_i
\},
\]

and

\[
r_i^{\mathrm{off}}
=
\max
\{
r\in\mathcal R:
m_i(r)\geq\tau_i
\}.
\]

The eight radial features were therefore

\[
\mathbf x_i^{(F_2)}
=
[
I_i,\,
\bar r_i,\,
s_{r,i},\,
q_i,\,
r_i^{\mathrm{on}},\,
r_i^{\mathrm{off}},\,
r_i^\star,\,
m_i^\star
]
\in\mathbb R^8.
\]

Radial extent,

\[
r_i^{\mathrm{off}}
-
r_i^{\mathrm{on}},
\]

was excluded because it is exactly determined by two retained coordinates.

---

## 3.9 Six axial descriptors

The peak axial orientation was

\[
\alpha_i^\star
=
\alpha_{2,i}(r_i^\star).
\]

A magnitude-weighted axial mean was constructed through the doubled-angle resultant

\[
Z_i
=
\sum_{r_j\in\mathcal R}
m_i(r_j)
e^{\mathrm{i}2\alpha_{2,i}(r_j)},
\]

with

\[
\bar\alpha_i
=
\frac12
\arg(Z_i)
\pmod{\pi}.
\]

Axial coherence was

\[
\kappa_i
=
\frac{
|Z_i|
}{
\sum_{r_j\in\mathcal R}
m_i(r_j)
},
\qquad
0\leq\kappa_i\leq1.
\]

Orientation drift across the primary radial domain was

\[
\delta_i
=
d_{\mathrm{ax}}
\left[
\alpha_{2,i}(3.5),
\alpha_{2,i}(27.5)
\right].
\]

Raw axial angles were not entered directly into the primary Euclidean feature vector. Peak and mean directions were encoded in doubled-angle Cartesian form:

\[
\mathbf x_i^{(\alpha_2)}
=
[
\cos(2\alpha_i^\star),\,
\sin(2\alpha_i^\star),\,
\cos(2\bar\alpha_i),\,
\sin(2\bar\alpha_i),\,
\kappa_i,\,
\delta_i
]
\in\mathbb R^6.
\]

This encoding is invariant under

\[
\alpha
\mapsto
\alpha+\pi.
\]

Additional persistence and weighted-dispersion summaries were excluded because they were redundant with retained coordinates. Algebraically reconstructed quantities were used only for numerical consistency checks and were not added as independent features.

---

## 3.10 Primary 14-dimensional representation

The final sketch-level representation was

\[
\mathbf x_i
=
\left[
\mathbf x_i^{(F_2)}
\mid
\mathbf x_i^{(\alpha_2)}
\right]
\in
\mathbb R^{14}.
\]

The representation matrix therefore had dimensions

\[
2300\times14.
\]

The eight radial and six axial coordinates were concatenated in the order defined above. An independent reconstruction of the two feature blocks reproduced the stored representation exactly, with maximum absolute numerical difference zero, and all values were finite.

---

## 3.11 Garment-identity-disjoint shell-field reconstruction

The reconstruction experiment interrogated the shell-level second-harmonic field underlying the 14-dimensional summary representation. It did not use the 14-dimensional vector itself as the predictor input.

Five category-balanced folds were constructed over the 230 recovered garment identities. Each test fold contained two complete identities from each of the 23 garment categories, giving 46 test identities per fold; the remaining 184 identities formed the training set. Train/test garment-identity overlap was zero in every fold, and every valid sketch-shell observation received exactly one out-of-fold prediction.

For sketch \(i\) and primary-domain shell \(r_j\), the predictor vector was

\[
\mathbf z_{ij}
=
\left[
r_j,\,
R_{2,i}(r_j)
\right]
=
\left[
r_j,\,
|F_{2,i}(r_j)|
\right].
\]

Separate regression models estimated the Cartesian second-harmonic components,

\[
\widehat C_{2,i}(r_j)
=
f_C(\mathbf z_{ij}),
\]

and

\[
\widehat S_{2,i}(r_j)
=
f_S(\mathbf z_{ij}).
\]

Both \(f_C\) and \(f_S\) were implemented using
`HistGradientBoostingRegressor` with

\[
\texttt{max\_iter}=250,
\qquad
\texttt{learning\_rate}=0.05,
\]

\[
\texttt{max\_leaf\_nodes}=15,
\qquad
\texttt{l2\_regularization}=1.0,
\]

and

\[
\texttt{random\_state}=42.
\]

No feature standardization or other scaling transformation was applied. All unspecified estimator arguments used the defaults of scikit-learn 1.6.1.

The final analysis was executed with Python 3.12.13, NumPy 2.0.2, and scikit-learn 1.6.1.

---

## 3.12 Rotation and coordinate-frame controls

Two complementary rotation controls evaluated the dependence of reconstruction on the common image coordinate frame.

### 3.12.1 Analytic harmonic rotation

For a physical image rotation by angle \(\phi\),

\[
\theta'
=
\theta+\phi.
\]

The \(m\)-th harmonic transforms as

\[
F_m'(r)
=
e^{-\mathrm{i}m\phi}
F_m(r).
\]

For \(m=2\),

\[
F_2'(r)
=
e^{-\mathrm{i}2\phi}
F_2(r).
\]

Writing

\[
F_2=C_2-\mathrm{i}S_2,
\]

the corresponding Cartesian transformation is

\[
C_2'
=
C_2\cos(2\phi)
-
S_2\sin(2\phi),
\]

\[
S_2'
=
C_2\sin(2\phi)
+
S_2\cos(2\phi).
\]

Magnitude is invariant:

\[
R_2'
=
\sqrt{C_2'^2+S_2'^2}
=
R_2,
\]

while axial orientation transforms as

\[
\alpha_2'
=
\alpha_2+\phi
\pmod{\pi}.
\]

This analytic transformation was used instead of rotating raster images, thereby avoiding interpolation, resampling, and cropping artifacts.

### 3.12.2 Global-rotation control

The complete observed harmonic field was rotated by

\[
\phi
\in
\{
0^\circ,
22.5^\circ,
45^\circ,
67.5^\circ,
90^\circ
\}.
\]

For each rotation, the same predictors, estimator specification, garment-identity-disjoint folds, and evaluation metrics were used.

Separate \(C_2\) and \(S_2\) RMSEs were retained to demonstrate their expected coordinate dependence, while vector RMSE, \(R_2\) error, peak-shell \(R_2\) performance, axial error, and coordinate-frame consistency error were used as substantive diagnostics.

### 3.12.3 Garment-identity-randomized rotation

A second control removed common population-level alignment while preserving repeated-sketch identity structure.

For each randomization, one angle

\[
\phi_g
\sim
\operatorname{Uniform}(0,\pi)
\]

was sampled independently for each garment identity \(g\). Every sketch belonging to identity \(g\) received the same \(\phi_g\).

Ten randomizations were performed using seeds

\[
20260830,\ldots,20260839.
\]

The procedure preserved:

\[
R_2,
\]

radius,

garment identity,

within-identity repeated-sketch structure,

category labels,

and the five validation folds,

while disrupting shared absolute orientation across garment identities.

For unrelated axial orientations, folded angular error is uniform on

\[
[0^\circ,90^\circ],
\]

giving the chance expectations

\[
\operatorname{median}(e)=45^\circ,
\]

\[
E[e]=45^\circ,
\]

\[
P(e\leq15^\circ)=\frac{1}{6},
\]

and

\[
P(e>45^\circ)=\frac12.
\]

These values were used as reference benchmarks rather than fitted null parameters.

---

## 3.13 Parameter and discretization sensitivity

Sensitivity analyses evaluated dependence of the radial–angular representation on the fixed numerical choices used in the primary measurement specification. The primary configuration was not altered after these analyses.

### 3.13.1 Support threshold

The primary support threshold was

\[
\tau_i
=
0.10\,m_i^\star.
\]

Alternative fractions were

\[
0.05
\quad\text{and}\quad
0.15.
\]

All eight radial descriptors were recomputed while holding the radial domain and concentration width fixed.

### 3.13.2 Concentration half-width

The primary concentration half-width was

\[
h=4
\]

radial shell-coordinate units. Alternatives were

\[
h=2
\quad\text{and}\quad
h=6.
\]

All other descriptor definitions were unchanged.

### 3.13.3 Radial-domain sensitivity

The primary domain was

\[
[3.5,27.5].
\]

The following inward and outward alternatives were evaluated:

\[
[5.5,25.5],
\]

\[
[4.5,26.5],
\]

\[
[3.5,27.5],
\]

\[
[2.5,28.5],
\]

\[
[1.5,29.5],
\]

and

\[
[0.5,30.5].
\]

The canonical full 72-shell radial field was reconstructed directly from the raw images before domain expansion was evaluated. The primary 25-shell \(C_2\), \(S_2\), and \(R_2\) fields were reproduced numerically before the expanded field was accepted for sensitivity analysis.

For each domain, descriptor rank stability, peak-location changes, endpoint occupancy, and peak-magnitude changes were quantified relative to the primary specification.

### 3.13.4 Angular-resolution sensitivity

The canonical 72 angular bins were coarsened to

\[
36
\quad\text{and}\quad
24
\]

bins by exact aggregation of adjacent angular mass bins. No image interpolation was used.

For each resolution, \(F_2\), \(C_2\), \(S_2\), \(R_2\), axial orientation, peak magnitude, and peak radius were recomputed. The 72-bin field served as the reference.

### 3.13.5 Radial-resolution sensitivity

The canonical 72 radial bins were coarsened by exact radial mass aggregation to

\[
36
\quad\text{and}\quad
24
\]

bins.

Because the primary radial-domain boundaries do not align exactly with all coarser grids, a second resolution analysis isolated bin resolution from domain mismatch using the common normalized physical interval

\[
\frac{1}{12}
\leq
r_{\mathrm{norm}}
\leq
\frac13.
\]

This interval corresponds exactly to 18 bins at resolution 72, 9 bins at resolution 36, and 6 bins at resolution 24.

The concentration half-width was kept constant in normalized physical coordinates,

\[
h_{\mathrm{norm}}
=
\frac{4}{72}.
\]

Rank stability and absolute changes in each radial descriptor were then quantified relative to the 72-bin representation.

These sensitivity analyses characterize measurement dependence; they are not parameter-selection procedures and do not establish that the primary configuration is universally optimal.

---

## 3.14 Low-order harmonic control

To place the primary second harmonic within the observed low-order spectrum, harmonics

\[
m\in\{1,2,3,4\}
\]

were computed from the same canonical 72-bin conditional angular distributions and evaluated on the same 25-shell primary radial domain.

For each \(m\), the following descriptive quantities were calculated:

\[
R_m(r)
=
|F_m(r)|,
\]

integrated radial harmonic magnitude,

median shell magnitude,

peak harmonic magnitude,

peak radius,

and the fraction of integrated magnitude carried by that order relative to the sum over \(m=1,\ldots,4\).

Rank correlations between \(m=2\) and neighbouring harmonic magnitudes were used to assess whether the second harmonic duplicated other low-order structure.

Because Section 3.6 defines \(m=2\) from the axial orientation convention of the measurement, these comparisons were interpreted as consistency and non-redundancy controls rather than a search for the empirically best harmonic order.

---

## 3.15 Phase-conditioning analysis

Axial phase becomes poorly conditioned when the magnitude of its underlying Cartesian vector is small. This relationship was derived explicitly for the second harmonic.

Let

\[
\alpha_2
=
\frac12
\operatorname{atan2}(S_2,C_2).
\]

Its first-order differential is

\[
d\alpha_2
=
\frac12
\frac{
C_2\,dS_2
-
S_2\,dC_2
}{
C_2^2+S_2^2
},
\]

or equivalently,

\[
d\alpha_2
=
\frac{
C_2\,dS_2
-
S_2\,dC_2
}{
2R_2^2
}.
\]

By the Cauchy--Schwarz inequality,

\[
|C_2\,dS_2-S_2\,dC_2|
\leq
R_2
\sqrt{
dC_2^2+dS_2^2
},
\]

giving

\[
|d\alpha_2|
\leq
\frac{
\sqrt{
dC_2^2+dS_2^2
}
}{
2R_2
}.
\]

For the observed out-of-fold reconstruction, define Cartesian perturbations

\[
\Delta C_2
=
\widehat C_2-C_2,
\]

\[
\Delta S_2
=
\widehat S_2-S_2,
\]

and perturbation norm

\[
E_{CS}
=
\sqrt{
(\Delta C_2)^2+
(\Delta S_2)^2
}.
\]

The empirical conditioning quantity was

\[
B_\alpha
=
\frac{
E_{CS}
}{
2R_2
}.
\]

The absolute first-order approximation was

\[
L_\alpha
=
\left|
\frac{
C_2\Delta S_2
-
S_2\Delta C_2
}{
2R_2^2
}
\right|.
\]

These quantities were computed over the out-of-fold field and at the observed peak shell.

For manuscript-facing association analysis, repeated sketches were reduced to garment-identity medians. Spearman correlations with median peak-shell axial error were calculated for:

\[
R_2,
\]

\[
1/R_2,
\]

\[
E_{CS},
\]

\[
B_\alpha,
\]

and

\[
L_\alpha.
\]

The analysis tests whether empirical axial reconstruction error is consistent with the expected geometry of phase estimation. It does not assume that the first-order approximation is exact for large perturbations or that \(R_2\) causally determines angular error.

### Magnitude-stratified conditioning

For descriptive visualization, the 230 garment identities were divided into quartiles according to median observed peak-shell \(R_2\). Within each quartile, median component-error norm, conditioning bound, first-order phase approximation, and actual axial error were summarized.

These quartiles were descriptive strata rather than independent inferential groups.

---

## 3.16 Garment-level association analysis

The principal association analysis evaluated the relationship between observed peak-shell harmonic magnitude and peak-shell axial reconstruction error.

For garment identity \(g\), repeated sketches were reduced to medians:

\[
\widetilde R_{2,g}
=
\operatorname{median}_{i\in g}
R_{2,i}(r_i^\star),
\]

\[
\widetilde e_g
=
\operatorname{median}_{i\in g}
e_i.
\]

Spearman's rank correlation was computed across the 230 garment identities:

\[
\rho_R
=
\rho_s
\left(
\widetilde R_{2,g},
\widetilde e_g
\right).
\]

Selected peak radius was evaluated as a secondary, sensitivity-qualified association:

\[
\widetilde r_g^\star
=
\operatorname{median}_{i\in g}
r_i^\star,
\]

\[
\rho_r
=
\rho_s
\left(
\widetilde r_g^\star,
\widetilde e_g
\right).
\]

Peak radius is interpreted more cautiously because it is defined by an argmax over a finite radial domain and showed material domain and resolution sensitivity.

Spearman correlations computed over all 2,300 sketches were retained only as descriptive pooled-sketch summaries and were not assigned inferential \(p\)-values.

The permutation probabilities for the two garment-level association tests were adjusted jointly using Holm's procedure.

---

## 3.17 Garment-cluster bootstrap

Uncertainty intervals were estimated using

\[
B=5000
\]

bootstrap replicates.

Complete garment identities, rather than individual sketches or sketch-shell rows, were sampled with replacement. Whenever an identity was selected, all of its repeated sketches and, where relevant, all 25 radial shells were included.

Percentile 95% confidence intervals were defined by the

\[
2.5^{\mathrm{th}}
\]

and

\[
97.5^{\mathrm{th}}
\]

percentiles of the bootstrap distribution.

The bootstrap was applied to reconstruction metrics, peak-shell quantities, garment-level correlations, and descriptive low/high error-group contrasts as appropriate.

---

## 3.18 Category-stratified permutation inference

For each of the two garment-level association tests,

\[
10{,}000
\]

permutations were performed.

Permutation was restricted within the 23 garment-category strata. Garment-level outcome values were shuffled only among identities belonging to the same category, preserving category composition while breaking the within-category correspondence between predictor and outcome.

For observed statistic \(T_{\mathrm{obs}}\), the two-sided corrected permutation probability was

\[
p
=
\frac{
1+
\sum_{b=1}^{B}
\mathbf 1
\left(
|T_b|
\geq
|T_{\mathrm{obs}}|
\right)
}{
B+1
},
\qquad
B=10{,}000.
\]

The two resulting permutation probabilities were adjusted by Holm's procedure.

Because permutation was conditional on garment category, the corresponding null distributions were not required to be centered at zero.

---

## 3.19 Outcome-defined error bands and threshold sensitivity

Peak-shell axial errors were summarized descriptively into low, intermediate, and high bands.

The primary descriptive thresholds were

\[
e_i\leq15^\circ,
\]

\[
15^\circ<e_i\leq45^\circ,
\]

and

\[
e_i>45^\circ.
\]

Sensitivity was evaluated using four tested low/high threshold pairs:

\[
10^\circ/30^\circ,
\]

\[
15^\circ/45^\circ,
\]

\[
20^\circ/45^\circ,
\]

and

\[
20^\circ/60^\circ.
\]

For each threshold definition, median observed peak-shell \(R_2\) was compared between the low- and high-error groups.

Effect size was summarized by Cliff's delta,

\[
\delta_C
=
P(R_{2,\mathrm{low}}>R_{2,\mathrm{high}})
-
P(R_{2,\mathrm{low}}<R_{2,\mathrm{high}}).
\]

Confidence intervals were obtained by resampling complete garment identities.

Because the error bands are defined using the observed outcome, overlap strongly across threshold choices, and are not independent experimental groups, no inferential \(p\)-values were assigned to these band comparisons. The thresholds were not optimized against the data and are not interpreted as prospective reliability cutoffs.

---

## 3.20 Algebraically coupled calibration diagnostic

Peak-shell magnitude error was defined as

\[
\Delta R_{2,i}
=
\widehat R_{2,i}(r_i^\star)
-
R_{2,i}(r_i^\star).
\]

Any association between observed \(R_2\) and \(\Delta R_2\) is mathematically coupled because the observed value appears explicitly with a negative sign in the definition of the difference.

Accordingly, the Spearman correlation

\[
\rho_s
\left[
R_{2,i}(r_i^\star),
\Delta R_{2,i}
\right]
\]

was reported only as a descriptive calibration diagnostic and was assigned no inferential \(p\)-value.

---

## 3.21 Scope of inference

Inference is conditional on the observed CLO-SKET population, the recovered garment identities, the frozen measurement specification, and the stated validation and resampling procedures. The analyses support claims about explicit radial–angular geometry, coordinate dependence, numerical sensitivity, and repeated-sketch statistical structure. They do not establish semantic garment understanding, causal geometric laws, universal parameter optimality, prospective reliability classification, likelihood-based circular modelling, or reconstruction of the complete angular density.

# 4. Results

## 4.1 Study population and primary representation

The analysis retained all 2,300 CLO-SKET sketches. The conditional angular tensor had dimensions \(2300\times72\times72\), the full second-harmonic field had dimensions \(2300\times72\), and the primary radial analysis comprised 25 shells spanning the fixed shell-coordinate domain

\[
r=3.5,4.5,\ldots,27.5.
\]

The construction from a representative sketch to the centroid-relative polar field, conditional angular distribution, second-harmonic magnitude, and axial orientation is illustrated in Figure 1.

![Figure 1. Radial–angular construction and second-harmonic interpretation.](figures/Figure_1_Radial_Angular_Construction.png)

**Figure 1. Radial–angular construction and second-harmonic interpretation.** (A) Representative CLO-SKET sketch with intensity-weighted centroid. (B) Centroid-relative polar geometry used to accumulate foreground intensity by radius and angle. (C) Conditional angular distribution \(p(\theta\mid r)\); the shaded interval marks the 25-shell primary radial domain \(r=3.5,\ldots,27.5\). (D) Second-harmonic magnitude \(R_2(r)=|F_2(r)|\), with the selected observed peak shell marked. (E) Axial orientation \(\alpha_2(r)\) over the primary domain. The second harmonic represents axial orientation because \(\alpha\equiv\alpha+\pi\).

The primary representation comprised eight radial second-harmonic descriptors and six axial descriptors (Figure 2),

\[
\mathbf x_i
=
\left[
\mathbf x_i^{(F_2)}
\mid
\mathbf x_i^{(\alpha_2)}
\right]
\in\mathbb R^{14}.
\]

The resulting matrix had dimensions \(2300\times14\), contained only finite values, and exactly matched an independently reconstructed \(8+6\) concatenation, with maximum absolute difference zero.

![Figure 2. Fourteen-dimensional radial–angular representation.](figures/Figure_2_Provenance_Locked_14D_Representation.png)

**Figure 2. Fourteen-dimensional radial–angular representation.** The radial block comprises integrated second-harmonic magnitude, radial centroid, radial spread, radial concentration, onset radius, termination radius, peak radius, and peak magnitude. The axial block represents peak and magnitude-weighted mean orientations through doubled-angle cosine/sine coordinates together with axial coherence and orientation drift. Radial extent is excluded because it is exactly termination radius minus onset radius.

The observed fields \(C_2\), \(S_2\), \(R_2\), and \(\alpha_2\), together with their reconstructed counterparts, each had dimensions \(2300\times25\). At the observed peak shell, the maximum absolute discrepancy between \(R_2\) and \(|F_2|\) was \(6.661\times10^{-16}\), numerically confirming the identity

\[
R_2=|F_2|
=\sqrt{C_2^2+S_2^2}.
\]

Accordingly, \(R_2\) and \(|F_2|\) were not treated as independent evidence.

---

## 4.2 Rigid-image rotation control of the 14-dimensional representation

A separate image-domain perturbation control evaluated whether the final 14-dimensional representation exhibited the intended transformation behavior when the raster sketch itself was rigidly rotated and the complete radial-angular measurement was recomputed.

All 2,300 sketches were evaluated at

\[
\phi
\in
\{-20^\circ,-10^\circ,-5^\circ,0^\circ,5^\circ,10^\circ,20^\circ\}.
\]

No garment labels were used and no predictive model was fitted.

### 4.2.1 Stability of the second-harmonic magnitude field

Across non-zero rotation conditions, the primary-domain second-harmonic magnitude profile showed small median numerical perturbations relative to the \(0^\circ\) reference.

The median normalized mean absolute errors were:

| Rotation | Median \(R_2\) NMAE | 95th percentile |
|---:|---:|---:|
| \(-20^\circ\) | 0.034374 | 0.110528 |
| \(-10^\circ\) | 0.025998 | 0.080176 |
| \(-5^\circ\) | 0.019959 | 0.065123 |
| \(+5^\circ\) | 0.020684 | 0.068462 |
| \(+10^\circ\) | 0.026253 | 0.083533 |
| \(+20^\circ\) | 0.033446 | 0.114846 |

The perturbation was smallest near the reference orientation and increased modestly toward the largest tested rotations, consistent with interpolation and finite-bin effects rather than exact raster-level invariance.

![Figure 3. Rigid-rotation control of the CLO-SKET radial–angular representation.](figures/Figure_3_Rigid_Rotation_Control.png)

**Figure 3. Rigid-rotation control of the CLO-SKET radial–angular representation.**  
(A) The same canonical sketch after rigid raster rotations of \(-20^\circ\), \(0^\circ\), and \(+20^\circ\), illustrating the image-domain perturbation applied in the control. (B) Stability of the primary-domain second-harmonic radial-magnitude profile, summarized by the median and 95th-percentile normalized mean absolute error relative to the \(0^\circ\) reference. (C) Axial orientation equivariance. Recovered shifts in peak and magnitude-weighted axial orientation closely followed the ideal \(\Delta\alpha=\phi\) relation; across the tested rotations, the maximum 95th-percentile transformation errors were \(4.87^\circ\) and \(0.85^\circ\), respectively. (D) Absolute changes in the intended rotation-invariant directional scalars. Axial coherence remained numerically stable, whereas orientation drift showed small median changes but a wider upper-tail response. Together, the control supports the intended invariant/equivariant organization of the representation over the evaluated rigid rotations without implying exact raster-level invariance or robustness outside the tested perturbations.

### 4.2.2 Axial orientation transformation consistency

The two doubled-angle orientation pairs followed the expected axial transformation closely.

For the peak axial orientation, median observed shifts closely matched the imposed physical rotations:

| Rotation | Median observed shift | Median transformation error | 95th percentile error |
|---:|---:|---:|---:|
| \(-20^\circ\) | \(-19.9968^\circ\) | \(0.2554^\circ\) | \(4.8725^\circ\) |
| \(-10^\circ\) | \(-9.9985^\circ\) | \(0.1947^\circ\) | \(3.6967^\circ\) |
| \(-5^\circ\) | \(-4.9930^\circ\) | \(0.1536^\circ\) | \(2.4070^\circ\) |
| \(+5^\circ\) | \(5.0130^\circ\) | \(0.1566^\circ\) | \(2.6419^\circ\) |
| \(+10^\circ\) | \(10.0089^\circ\) | \(0.2001^\circ\) | \(3.7304^\circ\) |
| \(+20^\circ\) | \(20.0127^\circ\) | \(0.2638^\circ\) | \(4.5054^\circ\) |

The magnitude-weighted mean orientation was even more stable:

| Rotation | Median observed shift | Median transformation error | 95th percentile error |
|---:|---:|---:|---:|
| \(-20^\circ\) | \(-19.9944^\circ\) | \(0.0925^\circ\) | \(0.8485^\circ\) |
| \(-10^\circ\) | \(-9.9939^\circ\) | \(0.0791^\circ\) | \(0.7474^\circ\) |
| \(-5^\circ\) | \(-4.9927^\circ\) | \(0.0722^\circ\) | \(0.6705^\circ\) |
| \(+5^\circ\) | \(5.0048^\circ\) | \(0.0717^\circ\) | \(0.6327^\circ\) |
| \(+10^\circ\) | \(10.0047^\circ\) | \(0.0797^\circ\) | \(0.7251^\circ\) |
| \(+20^\circ\) | \(20.0065^\circ\) | \(0.0901^\circ\) | \(0.8223^\circ\) |

Thus, the doubled-angle orientation coordinates transformed closely according to the expected \(R(2\phi)\) action over the tested rotation range.

### 4.2.3 Rotation-invariant directional scalars

Axial coherence showed very small absolute changes across the tested rotations.

| Rotation | Median \(|\Delta\kappa|\) | 95th percentile |
|---:|---:|---:|
| \(-20^\circ\) | 0.002789 | 0.015726 |
| \(-10^\circ\) | 0.002417 | 0.013304 |
| \(-5^\circ\) | 0.002110 | 0.011695 |
| \(+5^\circ\) | 0.002105 | 0.012179 |
| \(+10^\circ\) | 0.002307 | 0.013588 |
| \(+20^\circ\) | 0.002923 | 0.015927 |

Orientation drift also showed small median changes, ranging from approximately \(1.11^\circ\) to \(1.42^\circ\), but with substantially larger upper-tail variation. The 95th-percentile absolute changes ranged from approximately \(24.69^\circ\) to \(29.39^\circ\).

These results support the intended transformation structure of the representation over the tested rigid rotations: the radial-magnitude block showed small numerical perturbations, the doubled-angle orientation pairs followed the expected axial transformation, and coherence and orientation drift behaved as invariant scalar descriptors. The results do not imply exact invariance under raster rotation or robustness beyond the evaluated perturbations.

---

## 4.3 Duplicate-image screening and garment-identity structure

All 2,300 file paths were unique. SHA-256 hashing detected no repeated raw files, and hashing of decoded pixel arrays detected no repeated decoded images. Perceptual-hash screening identified 11 candidate pairs at Hamming distance 0, 39 at distance at most 2, and 248 at distance at most 4. These candidates were treated as a screen for visual similarity rather than evidence of duplicated files or shared lineage.

Filename and category structure recovered 230 category-qualified garment identities, exactly 10 identities within each of the 23 categories. Individual garment identities contained 9–11 sketches and 9–11 distinct replicate identifiers. Eight identity–replicate combinations appeared more than once in the filename records.

Recovered garment identity was therefore used as the clustering unit for validation, bootstrap resampling, and confirmatory association analysis. The available metadata do not establish that the 230 recovered garment identities constitute mutually independent sampling units; population-level inference remains conditional on that assumption.

---

## 4.4 Garment-identity separation in validation

An initial image-level cross-validation design did not separate repeated sketches by garment identity: garment identities represented in each test fold were also represented in the corresponding training set. That design therefore evaluated unseen image files rather than unseen garments and was retained only as a sensitivity comparison.

The primary validation used five category-balanced, garment-identity-disjoint folds. Each test fold contained 46 complete garment identities—two identities from each of the 23 categories—and each training fold contained the remaining 184 identities. Test-fold sizes ranged from 459 to 461 sketches because the number of repeated sketches per garment identity varied slightly.

Every sketch and every recovered garment identity was held out exactly once. Train/test garment-identity overlap was zero in all five folds.

---

## 4.5 Garment-identity-disjoint reconstruction of \(C_2\) and \(S_2\)

Two fixed `HistGradientBoostingRegressor` models reconstructed \(C_2\) and \(S_2\) independently from shell radius and observed second-harmonic magnitude,

\[
\mathbf z_{ij}
=
[r_j,R_{2,i}(r_j)].
\]

Across the five garment-identity-disjoint folds, \(C_2\) RMSE ranged from 0.210938 to 0.228147 and \(S_2\) RMSE ranged from 0.124814 to 0.131585 (Table 1). All 57,500 sketch-shell rows received exactly one out-of-fold prediction.

**Table 1. Garment-identity-disjoint fold performance for component reconstruction.**

| Fold | Training identities | Test identities | Identity overlap | \(C_2\) RMSE | \(S_2\) RMSE |
|---:|---:|---:|---:|---:|---:|
| 0 | 184 | 46 | 0 | 0.216957 | 0.124959 |
| 1 | 184 | 46 | 0 | 0.213426 | 0.124814 |
| 2 | 184 | 46 | 0 | 0.210938 | 0.127228 |
| 3 | 184 | 46 | 0 | 0.228147 | 0.128320 |
| 4 | 184 | 46 | 0 | 0.220904 | 0.131585 |

Across all held-out rows, the fold-local global baseline produced RMSEs of 0.300420 for \(C_2\) and 0.129034 for \(S_2\). A radius-only model produced RMSEs of 0.287288 and 0.128729, respectively. Adding \(R_2=|F_2|\) to radius reduced \(C_2\) RMSE to 0.218161, an absolute reduction of 0.069127 and a relative reduction of 24.06%. For \(S_2\), RMSE decreased to 0.127405, an absolute reduction of 0.001324 and a relative reduction of 1.03% (Table 2).

**Table 2. Comparator performance and incremental contribution of second-harmonic magnitude.**

| Model | \(C_2\) RMSE | \(S_2\) RMSE |
|---|---:|---:|
| Fold-local global baseline | 0.300420 | 0.129034 |
| Radius only | 0.287288 | 0.128729 |
| Radius + \(R_2\) | **0.218161** | **0.127405** |

The component-specific gains were strongly asymmetric. However, the rotation analysis in Section 4.8 shows that separate \(C_2\) and \(S_2\) errors are coordinate-dependent quantities and should not be interpreted as intrinsic differences between cosine-like and sine-like garment structure.

Because \(R_2\), \(C_2\), and \(S_2\) derive from the same conditional angular distribution, reconstruction remains a shared-source consistency diagnostic rather than recovery of an independent physical or semantic target.

---

## 4.6 Sensitivity to the validation unit

Changing the validation unit from individual sketches to complete garment identities produced little change in aggregate reconstruction estimates.

For the complete 25-shell field, the initial image-level out-of-fold analysis produced \(R_2\) RMSE 0.145516, Pearson \(r=0.927269\), and mean reconstructed \(R_2=0.212319\). Garment-identity-disjoint reconstruction produced RMSE 0.145610, Pearson \(r=0.926390\), and mean reconstructed \(R_2=0.212487\).

At the observed peak shell, median observed \(R_2\) was 0.660428 under both validations. The initial image-level analysis produced median reconstructed \(R_2=0.557371\), median

\[
\Delta R_2
=
\widehat R_2-R_2
=
-0.091925,
\]

peak-shell RMSE 0.149218, Pearson \(r=0.807987\), and median axial error \(4.157680^\circ\). Garment-identity-disjoint reconstruction produced median reconstructed \(R_2=0.566561\), median \(\Delta R_2=-0.084261\), peak-shell RMSE 0.148303, Pearson \(r=0.810543\), and median axial error \(4.104118^\circ\).

The proportion of sketches with axial error above \(45^\circ\) was 15.70% under both designs. The proportion with error at or below \(15^\circ\) changed from 78.04% to 78.17%, and the intermediate proportion changed from 6.26% to 6.13%.

Thus, correcting the validation unit had little effect on aggregate reconstruction estimates. All subsequent reconstruction results nevertheless use garment-identity-disjoint predictions because these evaluate transfer to previously unseen recovered garment identities.

---

## 4.7 Garment-cluster uncertainty for reconstruction

Bootstrap uncertainty was estimated by resampling complete garment identities.

Whole-field \(R_2\) RMSE was

\[
0.145610
\quad
(95\%~\mathrm{CI}:~0.144271\text{--}0.146947),
\]

and whole-field Pearson correlation was

\[
0.926390
\quad
(0.924356\text{--}0.928325).
\]

At the observed peak shell, \(R_2\) RMSE was

\[
0.148303
\quad
(0.143363\text{--}0.153125),
\]

and Pearson correlation was

\[
0.810543
\quad
(0.793049\text{--}0.827517).
\]

The median peak-shell magnitude difference was

\[
\operatorname{median}(\Delta R_2)
=
-0.084261
\quad
(95\%~\mathrm{CI}:~-0.095655\text{ to }-0.072696),
\]

indicating systematic attenuation of reconstructed peak magnitude.

Median peak-shell axial error was

\[
4.104118^\circ
\quad
(95\%~\mathrm{CI}:~3.815065^\circ\text{--}4.511576^\circ).
\]

The proportion with error at or below \(15^\circ\) was 78.17% (75.77%–80.60%), the proportion between \(15^\circ\) and \(45^\circ\) was 6.13% (5.13%–7.17%), and the proportion above \(45^\circ\) was 15.70% (13.50%–17.95%).

![Figure 4. Garment-identity-disjoint reconstruction validation.](figures/Figure_4_Identity_Disjoint_Reconstruction_Validation.png)

**Figure 4. Garment-identity-disjoint reconstruction validation.**  
(A) Observed versus reconstructed \(R_2\) over all 57,500 held-out sketch-shell rows (RMSE 0.145610; Pearson \(r=0.926390\)). (B) Observed versus reconstructed \(R_2\) at each sketch's observed peak shell (\(n=2,300\); RMSE 0.148303; Pearson \(r=0.810543\)). (C) Axial reconstruction error at the observed peak shell; the dashed line marks the median \(4.104^\circ\). (D) The five category-balanced folds withheld complete recovered garment identities, with 184 training identities, 46 test identities, all 23 categories represented in every test fold, and zero train/test identity overlap.

---

## 4.8 Rotation and coordinate-frame control

The observed second-harmonic field was subjected to analytic rotations in doubled-angle space without image interpolation, resampling, or cropping.

For a global physical rotation by \(\phi\),

\[
F_2'(r)
=
e^{-i2\phi}F_2(r),
\]

which preserves

\[
R_2'(r)=R_2(r)
\]

while rotating the Cartesian components \(C_2\) and \(S_2\).

### 4.8.1 Global rotation

Global rotations of \(0^\circ\), \(22.5^\circ\), \(45^\circ\), \(67.5^\circ\), and \(90^\circ\) left the substantive coordinate-free reconstruction metrics essentially unchanged.

Across the five rotations, vector RMSE varied over a range of only 0.000103, \(R_2\) RMSE over 0.000307, \(R_2\) Pearson correlation over 0.000665, peak-shell \(R_2\) RMSE over 0.000647, and median peak-shell axial error over only \(0.0556^\circ\).

At a physical \(45^\circ\) rotation, the component errors exchanged exactly:

\[
C_2\text{ RMSE at }0^\circ
=
S_2\text{ RMSE at }45^\circ,
\]

\[
S_2\text{ RMSE at }0^\circ
=
C_2\text{ RMSE at }45^\circ,
\]

with numerical discrepancies below \(10^{-12}\). This demonstrates that the observed \(C_2/S_2\) error asymmetry is coordinate-dependent rather than an intrinsic distinction between the two Cartesian components.

### 4.8.2 Garment-identity-randomized rotation

A second control assigned a single random physical rotation to every sketch belonging to the same garment identity, independently across the 230 identities. Ten randomizations were performed. These perturbations preserved radius, observed \(R_2\), garment identity, repeated-sketch structure, and the original validation folds while removing the shared absolute image-axis orientation across identities.

Relative to the original upright data, mean performance across the ten randomized controls changed as follows:

**Table 3. Reconstruction under global and garment-identity-randomized rotations.**

| Condition | Vector RMSE | \(R_2\) RMSE | \(R_2\) Pearson | Peak \(R_2\) RMSE | Peak \(R_2\) Pearson | Median peak axial error |
|---|---:|---:|---:|---:|---:|---:|
| Original upright | 0.252639 | 0.145610 | 0.926390 | 0.148303 | 0.810543 | \(4.104^\circ\) |
| Global rotations, mean | 0.252597 | 0.145487 | 0.926655 | 0.148044 | 0.812051 | \(4.126^\circ\) |
| Identity-randomized rotations, mean | 0.390756 | 0.362143 | 0.713536 | 0.589963 | 0.557625 | \(44.675^\circ\) |

Under identity-randomized rotations, median axial error averaged \(44.675^\circ\), compared with \(45^\circ\) for unrelated axial orientations. Mean error was \(44.769^\circ\), compared with the same \(45^\circ\) chance expectation. The proportion with error at or below \(15^\circ\) was 0.1655, close to the chance value \(15/90=0.1667\), and the proportion above \(45^\circ\) was 0.4972, close to the chance value 0.5.

Thus, radius and second-harmonic magnitude do not intrinsically determine second-harmonic phase. The strong phase reconstruction observed in the upright dataset depends substantially on population-level orientation structure relative to the common image coordinate frame.

This result does not invalidate the radial–angular representation; rather, it identifies the coordinate information contributing to the reconstruction experiment.

---

## 4.9 Parameter and discretization sensitivity

Sensitivity analyses varied one construction choice at a time while preserving the primary representation and analysis.

### 4.9.1 Support threshold and concentration width

The primary support threshold was \(0.10\,m^\star\). Alternative thresholds of 0.05 and 0.15 left six of the eight radial descriptors exactly unchanged. Changes were confined primarily to onset and termination radii, which were exactly preserved for approximately 95–97% of sketches and remained within two shells for approximately 98–100%.

Changing the concentration half-width from the primary \(\pm4\) shell-coordinate units to \(\pm2\) or \(\pm6\) altered only the concentration coordinate by construction. The remaining seven radial descriptors were identical. Rank correlation of the concentration coordinate with its primary value remained 0.888 at half-width 2 and 0.949 at half-width 6.

### 4.9.2 Angular resolution

The canonical 72 angular bins were coarsened by exact mass aggregation to 36 and 24 bins, without image interpolation.

**Table 4. Sensitivity of the harmonic field to angular resolution.**

| Angular bins | \(R_2\) Spearman vs 72 | \(C_2\) Spearman | \(S_2\) Spearman | Median axial difference | Exact peak-radius agreement | Peak-magnitude Spearman |
|---:|---:|---:|---:|---:|---:|---:|
| 72 | 1.000000 | 1.000000 | 1.000000 | \(0.000^\circ\) | 1.000000 | 1.000000 |
| 36 | 0.999193 | 0.998844 | 0.971118 | \(2.530^\circ\) | 0.926522 | 0.998305 |
| 24 | 0.997051 | 0.995460 | 0.912654 | \(5.040^\circ\) | 0.862174 | 0.994252 |

Second-harmonic magnitude was therefore highly stable to substantial reductions in angular resolution. The larger changes in \(S_2\) than \(C_2\) were interpreted as coordinate-component effects rather than distinct physical signals.

### 4.9.3 Radial domain

The primary domain \(3.5\text{--}27.5\) contained endpoint peak locations for 22.04% of sketches. Specifically, 12.70% peaked at the lower endpoint and 9.35% at the upper endpoint.

The primary domain was compared with inward and outward alternatives extending from \(5.5\text{--}25.5\) through \(0.5\text{--}30.5\). Global radial summaries remained more stable than localized quantities. Relative to the primary domain, rank correlations at the widest tested domain \(0.5\text{--}30.5\) were 0.955 for integrated magnitude, 0.883 for radial centroid, and 0.786 for radial spread, whereas peak radius decreased to 0.511, concentration to 0.476, and onset radius to 0.471.

Among the 215 sketches whose primary peak occurred at the upper boundary \(r=27.5\), expansion to \(r=30.5\) caused 40.93% to move to a larger radius. Only 38.14% remained at 27.5 under the widest tested expansion.

Accordingly, peak radius is a window-dependent localization statistic. The endpoint occupancy and outward migration indicate partial boundary censoring, particularly for upper-boundary peaks.

### 4.9.4 Radial resolution

Radial-resolution sensitivity was assessed after exact mass aggregation from 72 to 36 and 24 radial bins. To isolate resolution from domain mismatch, all three resolutions were compared over the same normalized physical interval, \(1/12\le r_{\mathrm{norm}}\le1/3\).

**Table 5. Radial-resolution rank stability on an exact common physical domain.**

| Feature | 36 bins vs 72 | 24 bins vs 72 |
|---|---:|---:|
| Integrated magnitude | 0.978486 | 0.942134 |
| Radial centroid | 0.967402 | 0.931144 |
| Radial spread | 0.948735 | 0.892909 |
| Peak magnitude | 0.935818 | 0.877158 |
| Peak radius | 0.790820 | 0.691084 |
| Peak concentration | 0.676002 | 0.606417 |
| Onset radius | 0.591605 | 0.463113 |
| Termination radius | 0.635755 | 0.418232 |

Median normalized physical displacement of peak radius was 0.006944 at 36 bins and 0.013889 at 24 bins.

Overall, integrated magnitude, centroid, and spread were substantially more stable to domain and resolution perturbations than localized peak-, onset-, termination-, and concentration-based descriptors. The primary parameterization is therefore treated as a fixed measurement specification rather than as an empirically optimal or universally invariant configuration.

---

## 4.10 Low-order harmonic spectrum and justification of \(m=2\)

The primary second harmonic was evaluated against the neighbouring low-order harmonics \(m=1,3,4\), all derived from the same canonical 72-bin conditional angular field.

For an angular rotation by \(\pi\),

\[
F_m(\theta+\pi)
=
(-1)^m F_m(\theta).
\]

Odd harmonics therefore change sign under a \(180^\circ\) reversal, whereas even harmonics remain invariant. The observed fields reproduced this transformation numerically to better than \(5\times10^{-16}\).

The second harmonic is thus the lowest non-zero harmonic compatible with the axial orientation convention used by the representation. The empirical spectrum was examined as a consistency control rather than as a post-hoc selection criterion.

**Table 6. Low-order harmonic magnitude on the primary radial domain.**

| \(m\) | Symmetry class | Median integrated magnitude | Median peak magnitude | Median fraction of \(m=1\ldots4\) integrated content |
|---:|---|---:|---:|---:|
| 1 | directional / odd | 6.240198 | 0.592390 | 0.244719 |
| 2 | axial-compatible | **7.891117** | **0.660428** | **0.302403** |
| 3 | directional / odd | 5.691281 | 0.533454 | 0.220732 |
| 4 | axial-compatible | 5.693895 | 0.539608 | 0.221296 |

Within this low-order comparison, \(m=2\) had the largest median integrated magnitude and largest median peak magnitude. Its integrated magnitude exceeded that of the higher-order axial harmonic \(m=4\) in 87.22% of sketches, and its peak magnitude exceeded \(m=4\) in 84.74%.

The \(m=2\) integrated magnitude was only weakly rank-associated with \(m=1\) (\(\rho=0.116\)) and \(m=3\) (\(\rho=0.185\)), and moderately associated with \(m=4\) (\(\rho=0.490\)). Peak-magnitude correlation between \(m=2\) and \(m=4\) was \(\rho=0.552\).

These results support the interpretation of \(m=2\) as a substantial, non-redundant lowest-order axial statistic. They do not imply that \(m=2\) is the only informative harmonic or that higher-order angular structure is absent.

---

## 4.11 Garment-level associations and phase conditioning

The garment-level association analysis assigned equal weight to each recovered garment identity by reducing its repeated sketches to medians.

Median observed peak-shell \(R_2\) was negatively associated with median peak-shell axial reconstruction error:

\[
\rho=-0.355875,
\qquad
95\%~\mathrm{cluster\mbox{-}bootstrap~CI}
=
[-0.455749,-0.248336].
\]

The category-stratified permutation probability was

\[
p_{\mathrm{raw}}=0.000100,
\]

and the Holm-adjusted probability across the two garment-level association tests was

\[
p_{\mathrm{Holm}}=0.000200.
\]

Selected peak radius was evaluated as a secondary, sensitivity-qualified association. Median selected peak radius was negatively associated with median axial error:

\[
\rho=-0.207675,
\qquad
95\%~\mathrm{CI}
=
[-0.322472,-0.095626],
\]

with

\[
p_{\mathrm{raw}}=0.030097,
\qquad
p_{\mathrm{Holm}}=0.030097.
\]

**Table 7. Garment-level monotonic associations (\(n=230\) garment identities).**

| Quantity | Spearman \(\rho\) | 95% cluster-bootstrap CI | Raw permutation \(p\) | Holm \(p\) |
|---|---:|---:|---:|---:|
| Median observed peak-shell \(R_2\) vs median axial error | −0.355875 | [−0.455749, −0.248336] | 0.000100 | 0.000200 |
| Median selected peak radius vs median axial error | −0.207675 | [−0.322472, −0.095626] | 0.030097 | 0.030097 |

At the sketch level, the corresponding descriptive Spearman correlations were −0.253366 for observed peak-shell \(R_2\) and −0.271404 for selected peak radius. No inferential probabilities were assigned to these pooled-sketch associations.

### 4.11.1 Conditioning of axial phase

The negative \(R_2\)-error association was further examined through the perturbation geometry of axial phase. For

\[
\alpha_2
=
\frac12\operatorname{atan2}(S_2,C_2),
\]

the first-order perturbation is

\[
d\alpha_2
=
\frac{
C_2\,dS_2-S_2\,dC_2
}{
2R_2^2
},
\]

with the bound

\[
|d\alpha_2|
\le
\frac{
\sqrt{dC_2^2+dS_2^2}
}{
2R_2
}.
\]

At the garment-identity level, median peak \(R_2\) had the association reported above,

\[
\rho=-0.356,
\]

whereas median Cartesian reconstruction-error norm was much more strongly associated with median axial error,

\[
\rho=+0.760.
\]

The combined conditioning quantity

\[
\frac{
\|\Delta(C_2,S_2)\|
}{
2R_2
}
\]

showed the strongest of these associations,

\[
\rho=+0.789.
\]

The absolute first-order linearized phase perturbation was also strongly associated with actual axial error,

\[
\rho=+0.712.
\]

**Table 8. Garment-level phase-conditioning associations.**

| Quantity vs median axial error | Spearman \(\rho\) |
|---|---:|
| Median observed peak \(R_2\) | −0.356 |
| Median Cartesian reconstruction-error norm | +0.760 |
| Median conditioning bound \(\|\Delta(C_2,S_2)\|/(2R_2)\) | **+0.789** |
| Median linearized phase error | +0.712 |

Magnitude-stratified results showed the same ordering. Across garment-identity quartiles of observed peak \(R_2\), median axial error decreased monotonically:

\[
5.988^\circ
\rightarrow
4.039^\circ
\rightarrow
3.725^\circ
\rightarrow
2.918^\circ.
\]

The corresponding median conditioning bound decreased

\[
10.160^\circ
\rightarrow
7.304^\circ
\rightarrow
6.975^\circ
\rightarrow
5.268^\circ.
\]

The weakest-harmonic quartile therefore had approximately 2.05 times the median axial error of the strongest-harmonic quartile. Median Cartesian component-error norm also decreased from 0.2028 in the weakest quartile to 0.1369 in the strongest.

These results are consistent with the expected conditioning geometry of phase estimation: small harmonic magnitude increases angular sensitivity, but \(R_2\) alone does not determine reconstruction error because the Cartesian prediction perturbation also varies.

![Figure 5. Association between second-harmonic organization and axial reconstruction error.](figures/Figure_5_Garment_Identity_Inference.png)

**Figure 5. Association between second-harmonic organization and axial reconstruction error.** (A) Across 230 garment-identity medians, observed peak-shell \(R_2\) was negatively associated with axial reconstruction error (Spearman \(\rho=-0.355875\), 95% garment-cluster bootstrap CI \([-0.455749,-0.248336]\), Holm-adjusted \(p=0.000200\)). (B) Selected peak radius showed a weaker, secondary association (\(\rho=-0.207675\), 95% CI \([-0.322472,-0.095626]\), Holm-adjusted \(p=0.030097\)); interpretation is sensitivity-qualified because peak location depends on the finite radial domain. (C) Garment-identity quartiles show decreasing median axial error with increasing peak \(R_2\). (D) Across four tested sketch-level low/high axial-error threshold pairs, the low-error group had higher median peak \(R_2\) in every comparison; threshold groups are descriptive rather than prospective reliability classes.

![Figure 6. Identity-aware uncertainty and category-stratified permutation inference.](figures/Figure_6_Bootstrap_Permutation_Inference.png)

**Figure 6. Garment-identity-aware uncertainty and category-stratified permutation inference for the two garment-level association tests.** (A,C) Garment-cluster bootstrap distributions from 5,000 replicates for the peak-shell \(R_2\) and selected peak-radius Spearman associations; dashed lines mark percentile 95% intervals and solid lines the observed statistics. (B,D) Null distributions from 10,000 permutations performed within garment category, with observed statistics marked. Because permutations were restricted within category, the conditional null distributions need not be centered at zero; the procedure preserves category structure while breaking within-category identity-level correspondence.

---

## 4.12 Outcome-defined error bands and threshold sensitivity

Under the primary descriptive \(15^\circ/45^\circ\) band definition, 1,798 sketches were in the low-error band, 141 in the intermediate band, and 361 in the high-error band.

Median observed peak-shell \(R_2\) was 0.674442 in the low-error group and 0.609574 in the high-error group. The median difference was

\[
0.064868
\quad
(95\%~\mathrm{CI}:~0.047036\text{--}0.084433),
\]

and Cliff's \(\delta\) was

\[
0.269838
\quad
(0.188673\text{--}0.351032).
\]

The same direction persisted across all four tested threshold pairs (Table 9). Median \(R_2\) differences ranged from 0.059442 to 0.072677, and Cliff's \(\delta\) ranged from 0.236987 to 0.300349. All garment-cluster bootstrap intervals remained above zero.

**Table 9. Threshold sensitivity of the descriptive low/high peak-\(R_2\) contrast.**

| Low/high thresholds | Low / middle / high \(n\) | Low median \(R_2\) | High median \(R_2\) | Median difference (95% CI) | Cliff's \(\delta\) (95% CI) |
|---|---:|---:|---:|---:|---:|
| \(10^\circ/30^\circ\) | 1665 / 239 / 396 | 0.679165 | 0.606488 | 0.072677 [0.055431, 0.093955] | 0.300349 [0.220369, 0.379317] |
| \(15^\circ/45^\circ\) | 1798 / 141 / 361 | 0.674442 | 0.609574 | 0.064868 [0.047036, 0.084433] | 0.269838 [0.188673, 0.351032] |
| \(20^\circ/45^\circ\) | 1853 / 86 / 361 | 0.672488 | 0.609574 | 0.062914 [0.044974, 0.083241] | 0.258506 [0.177205, 0.338632] |
| \(20^\circ/60^\circ\) | 1853 / 125 / 322 | 0.672488 | 0.613045 | 0.059442 [0.038585, 0.079032] | 0.236987 [0.151712, 0.325826] |

For selected peak radius under the \(15^\circ/45^\circ\) definition, low- and high-error median radii were 19.5 and 7.5 shell-coordinate units, with Cliff's

\[
\delta=0.435692
\quad
(95\%~\mathrm{CI}:~0.375745\text{--}0.494340).
\]

This peak-radius contrast is interpreted descriptively because the parameter-sensitivity analysis showed material dependence of exact peak location on radial domain and radial resolution.

The error bands are defined using the observed outcome and overlap substantially across threshold configurations. They are therefore descriptive outcome strata rather than independent replications, optimized decision thresholds, or validated prospective reliability classes. No band-comparison \(p\)-values were assigned.

---

## 4.13 Algebraically coupled calibration diagnostic

At the sketch level, the Spearman correlation between observed peak-shell \(R_2\) and

\[
\Delta R_2
=
\widehat R_2-R_2
\]

was \(+0.1714\).

Because the observed value appears algebraically in \(\Delta R_2\), this correlation is mathematically coupled and cannot be interpreted as an independent association. It is retained only as a descriptive calibration diagnostic and receives no inferential \(p\)-value.

---

---

# 5. Discussion

CLO-SKET shows that repeated garment sketches can be represented by an explicit axial–radial measurement while keeping the representation's mathematical dependencies and statistical limits visible. The central result is not that a Fourier descriptor alone solves garment understanding, but that shell-conditioned second-harmonic structure provides a compact and auditable description of sketch geometry.

## 5.1 What the 14-dimensional representation captures

The representation separates two complementary aspects of the second-harmonic field. Radial descriptors summarize where and how strongly axial organization occurs, while doubled-angle descriptors encode undirected orientation without treating \(0^\circ\) and \(180^\circ\) as different directions. This gives each coordinate a defined geometric meaning and avoids using algebraically redundant quantities as independent evidence.

The sensitivity analyses also clarify that the descriptors should not be interpreted uniformly. Integrated magnitude, radial centroid, and spread behave as broad summaries of the field and are comparatively stable. Peak radius, onset, termination, and concentration are more dependent on finite support, radial domain, and discretization. These localized descriptors remain useful, but their interpretation is conditional on the measurement specification rather than intrinsic to the garment.

## 5.2 Reconstruction reveals population structure, not a magnitude-to-phase identity

Identity-disjoint reconstruction produced strong agreement for the second-harmonic field in the canonical sketch frame, including whole-field \(R_2\) RMSE \(0.145610\), Pearson \(r=0.926390\), peak-shell RMSE \(0.148303\), peak-shell \(r=0.810543\), and median axial error \(4.104^\circ\). These values demonstrate reproducible structure for unseen garment identities under the observed coordinate convention.

They do not imply that phase is determined by magnitude. By construction, \(R_2=\sqrt{C_2^2+S_2^2}\) discards orientation. The rotation controls make this distinction explicit. A common global rotation preserves the substantive coordinate-free reconstruction behavior, whereas independently rotating garment identities increases median axial error to \(44.675^\circ\), close to the \(45^\circ\) expectation for unrelated axial orientations. The low canonical-frame error therefore reflects statistically recoverable population-level alignment in addition to harmonic magnitude.

This distinction is important for interpreting reconstruction as a validation device. The predictor and target quantities arise from the same measured angular field, so the experiment tests internal geometric consistency and generalization across garment identities; it is not evidence of semantic recognition or recovery of an independent physical variable.

## 5.3 Rotation behavior separates invariant and equivariant information

The rigid-raster perturbation experiment supports the intended transformation structure over the tested rotations. Radial-magnitude descriptors are designed to remain invariant to orientation, while doubled-angle axial coordinates should transform under the \(R(2\phi)\) action associated with axial geometry. Relative-orientation quantities are correspondingly expected to remain invariant.

The empirical control is valuable because exact analytic transformation laws do not guarantee exact raster-level behavior after image rotation, interpolation, re-binning, centroid recomputation, and finite support. The results therefore support numerical invariance/equivariance over the tested perturbation range rather than a claim of exact invariance for arbitrary image transformations.

## 5.4 Phase conditioning explains much of the angular-error structure

The garment-level association analysis is consistent with the local conditioning of harmonic phase. Axial error decreases as observed \(R_2\) increases (\(\rho=-0.356\)), but the Cartesian reconstruction perturbation is more strongly associated with error (\(\rho=+0.760\)). Combining perturbation magnitude with the \(1/(2R_2)\) phase-conditioning factor gives the strongest association (\(\rho=+0.789\)).

This pattern follows the first-order bound

\[
|d\alpha_2|
\leq
\frac{\|\Delta(C_2,S_2)\|}{2R_2}.
\]

Accordingly, the negative association between \(R_2\) and angular error should not be interpreted as an independent causal law. Small harmonic vectors are intrinsically more phase-sensitive, and actual Cartesian reconstruction error also matters. The association analysis is therefore explanatory: it shows that the observed error pattern is consistent with harmonic geometry rather than establishing a causal mechanism.

## 5.5 Relation to prior garment-sketch representations

Most recent garment-sketch research optimizes downstream generation, retrieval, editing, or sewing-pattern reconstruction (Baldrati et al., 2023; Cao et al., 2023; Zhang et al., 2024; Singh and Patras, 2024; Huang et al., 2025; Bui et al., 2026; Cao et al., 2026). CLO-SKET addresses a complementary problem. Instead of learning a high-capacity latent representation, it asks what can be measured directly from foreground geometry and how that measurement behaves under changes of coordinates, discretization, and validation unit.

The work is also distinct from claiming novelty for Fourier or shape analysis themselves. Fourier descriptors and geometric morphometrics have long provided explicit descriptions of shape (Zahn and Roskies, 1972; Bookstein, 1997; McCane, 2013), and frequency-domain features have been used in garment applications (An and Li, 2014; Liang et al., 2023). The contribution here is the integration of shell-conditional angular measurement, axial harmonic statistics, repeated-garment validation, rotation controls, sensitivity analysis, and dependency-aware inference into a single reproducible framework.

## 5.6 Limitations

Several limitations bound the conclusions. First, the analysis is restricted to CLO-SKET and its recovered garment identities; external generalization to other sketching conventions, datasets, or designers has not been demonstrated. Second, foreground extraction and polar discretization introduce measurement choices, and localized radial descriptors remain sensitive to some of those choices. Third, the common upright orientation of the dataset contributes substantially to phase recoverability, as shown by the identity-randomized rotation control.

Fourth, the second harmonic captures the lowest-order axial structure, not the complete angular distribution. Higher-order or multimodal geometry can therefore be omitted even when \(R_2\) is informative. Fifth, reconstruction uses quantities derived from the same observed angular field and should not be interpreted as an independent prediction task. Finally, garment identities are recovered from dataset structure rather than independently verified physical objects; inference is conditional on those recovered identities being appropriate repeated-measure units.

## 5.7 Implications

The main methodological implication is that interpretability requires more than assigning a verbal meaning to individual features. An explicit representation should also expose algebraic identities, transformation laws, discretization dependence, repeated-measure structure, and the conditioning of derived quantities. In CLO-SKET, these checks materially change interpretation: low canonical-frame axial error alone would suggest strong phase recoverability, whereas the rotation controls show how strongly that result depends on shared orientation; similarly, an \(R_2\)-error correlation alone would obscure the geometric role of Cartesian perturbation and phase conditioning.

Within these limits, the axial–radial representation provides a compact geometric layer that can be inspected independently of downstream fashion models. Future work can test the representation on externally collected sketches, compare it with alternative explicit shape descriptors, and examine whether interpretable geometric measurements add complementary information to learned representations without sacrificing their auditability.

---

# 6. Conclusion

This study introduces an explicit 14-dimensional axial–radial representation of garment-sketch geometry derived from shell-conditional angular distributions and their second harmonic. The representation separates radial organization from undirected axial orientation while keeping its algebraic structure and coordinate dependence explicit.

Evaluation on 2,300 CLO-SKET sketches from 230 recovered garment identities shows that second-harmonic structure is reproducible for unseen garment identities under identity-disjoint validation. Rotation controls provide an essential qualification: low axial reconstruction error in the canonical sketch frame depends substantially on shared population-level orientation, while the representation itself exhibits the intended invariant/equivariant behavior over the tested rigid rotations. Sensitivity analyses further distinguish stable broad radial summaries from localized descriptors that depend more strongly on discretization and radial-domain choices.

The association analysis is consistent with the geometry of phase conditioning. Axial reconstruction error depends not only on harmonic magnitude but also on Cartesian reconstruction perturbation relative to that magnitude. These relationships are observational and explanatory rather than causal.

The contribution is therefore a compact and auditable geometric measurement framework rather than a semantic garment-understanding model. Its main value lies in making representation, transformation behavior, numerical sensitivity, repeated-measure validation, uncertainty, and inferential limits directly testable. External validation on independently collected garment sketches and comparison with alternative explicit and learned representations are natural next steps.

# Declarations

## Funding

[TO BE COMPLETED TRUTHFULLY BEFORE SUBMISSION]

## Competing interests

[TO BE COMPLETED TRUTHFULLY BEFORE SUBMISSION]

## Author contributions (CRediT)

[TO BE COMPLETED TRUTHFULLY BEFORE SUBMISSION]

## Acknowledgements

[TO BE COMPLETED IF APPLICABLE]

## Ethics statement

[TO BE COMPLETED IF REQUIRED BY THE JOURNAL; DO NOT ADD AN ETHICS APPROVAL CLAIM UNLESS APPLICABLE]

---

# References

The canonical bibliography for journal typesetting is maintained in `CLO_SKET_References.bib`. Citation formatting should be generated from that file using the final Image and Vision Computing / Elsevier bibliography style rather than manually duplicating the bibliography here.
