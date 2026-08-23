# 2. Related Work

## 2.1 Garment sketches as computational inputs

Garment sketches have been used as computational inputs for reconstruction, editing, synthesis, retrieval, and pattern generation. Earlier geometry-oriented systems established that sparse drawings can carry information sufficient for downstream garment construction. Yasseen et al. (2013) converted mannequin-guided sketches into quadrilateral garment meshes. Wang et al. (2018) learned a shared latent space linking sketched fold patterns, sewing-pattern parameters, body shape, and simulated garments. Fondevilla et al. (2021) transferred style from annotated fashion sketches to three-dimensional characters. More recently, SketchTailor maps a single garment sketch to three-dimensional sewing patterns using a Vision Mamba encoder and deformable Transformer decoder (Huang et al., 2025).

A parallel line of work treats the sketch principally as a conditioning signal for image synthesis or editing. Multimodal Garment Designer conditions latent-diffusion fashion editing on sketches together with text and human pose (Baldrati et al., 2023). TexControl uses a two-stage diffusion pipeline in which a sketch constrains garment outline before a second stage refines texture (Zhang et al., 2024). FashionSD-X similarly incorporates sketch and text information into a latent-diffusion garment-synthesis framework (Singh and Patras, 2024). Cao et al. (2023) condition compatible clothing generation jointly on user sketches and reference garments.

The scale and scope of sketch-based fashion benchmarks are also increasing. GarmentSketch contains 26,249 sketches spanning 21 garment categories, paired with detailed textual descriptions and evaluated for sketch-guided fashion image generation (Bui et al., 2026). VietFashion instead studies sketch-text composed retrieval for culturally specific garments, beginning from 650 sketches and expanding the associated image collection to more than 21,000 generated examples (Cao et al., 2026).

These developments establish that garment sketches are computationally informative, but their dominant objective is task performance: generating an image, reconstructing a garment or sewing pattern, transferring style, or retrieving a compatible target. CLO-SKET addresses a different question. The sketch is treated as an observational geometric object, and the objective is to construct an explicit low-dimensional measurement whose algebraic dependencies, coordinate assumptions, repeated-measure structure, and sensitivity to analysis choices can be examined directly.

## 2.2 Explicit garment-shape and frequency-domain representations

Explicit numerical representations of garment form predate current generative systems. An and Li (2014) combined wavelet Fourier descriptors with supervised dimensionality reduction for fashion-flat classification. Tsuru et al. (2021) represented garment silhouettes using standardized measurements and analysed designer collections using multidimensional scaling and clustering. Such work demonstrates that garment outlines can be transformed into interpretable numerical summaries rather than represented only by learned latent embeddings.

More generally, Fourier descriptors provide a classical representation of periodic outline structure (Zahn and Roskies, 1972), while geometric morphometrics provides alternative methods for analysing curves and shapes, including forms without conventional anatomical landmarks (Bookstein, 1997; McCane, 2013). These approaches motivate explicit representations in which geometric assumptions remain inspectable.

Frequency-domain methods have also appeared in modern garment synthesis. Liang et al. (2023), for example, incorporated Fast Fourier Transform features into a controllable garment-image generator to model periodic texture structure. Their objective and signal differ fundamentally from the present work: the frequency-domain representation is used to improve texture expansion and regularity during synthesis, whereas CLO-SKET applies angular harmonics to the spatial distribution of sketch foreground geometry itself.

CLO-SKET therefore does not claim novelty for Fourier analysis, polar coordinates, outline measurement, or statistical shape analysis individually. Its methodological contribution lies in combining centroid-referenced polar occupancy, shell-conditional angular distributions, axial harmonic statistics, repeated-sketch validation, and explicit sensitivity controls in a single auditable measurement framework.

## 2.3 Radial–angular geometry

Let a retained sketch foreground location be represented relative to the foreground centroid \((c_x,c_y)\) by

\[
r=\sqrt{(x-c_x)^2+(y-c_y)^2},
\qquad
\theta=\operatorname{atan2}(y-c_y,x-c_x).
\]

The radial coordinate records distance from the centroid, while the angular coordinate records occupancy around it. Polar parameterizations also occur in garment-pattern analysis, although for different representations and objectives (Oh and Kim, 2026).

For radial shell \(r_k\), CLO-SKET constructs the observed conditional angular distribution

\[
p(\theta_j\mid r_k)
=
\frac{H(r_k,\theta_j)}
{\sum_{j'}H(r_k,\theta_{j'})},
\]

where \(H(r_k,\theta_j)\) denotes foreground mass in radial bin \(k\) and angular bin \(j\). The shell therefore defines a circular probability distribution from which harmonic structure can be measured directly.

For harmonic order \(m\),

\[
F_m(r_k)
=
\sum_j
p(\theta_j\mid r_k)e^{-\mathrm{i}m\theta_j}.
\]

The primary analysis uses \(m=2\). This choice follows from axial rather than directional geometry. If orientations separated by \(\pi\) denote the same undirected axis,

\[
\theta\equiv\theta+\pi,
\]

then

\[
F_m(\theta+\pi)
=
(-1)^m F_m(\theta).
\]

Odd harmonics change sign under a \(180^\circ\) reversal, whereas even harmonics are invariant. Consequently, \(m=2\) is the lowest non-zero harmonic compatible with axial symmetry. Higher even harmonics such as \(m=4\) are also axially invariant but describe finer angular organization rather than the lowest-order axial structure. This symmetry argument, rather than retrospective predictive performance, determines the primary harmonic order.

A prespecified low-order control over \(m=1,2,3,4\) was subsequently used to assess whether the observed spectrum is consistent with that choice and whether \(m=2\) is redundant with neighbouring harmonics. The control does not treat harmonic order as a post-hoc model-selection parameter.

## 2.4 Axial statistics and second-harmonic representation

For the primary harmonic,

\[
F_2(r_k)
=
C_2(r_k)-\mathrm{i}S_2(r_k).
\]

Axial data require doubled-angle treatment because orientations separated by \(180^\circ\) represent the same undirected axis (Jammalamadaka and SenGupta, 2001). The second-harmonic magnitude and axial orientation are therefore

\[
R_2(r_k)
=
|F_2(r_k)|
=
\sqrt{C_2(r_k)^2+S_2(r_k)^2},
\]

and

\[
\alpha_2(r_k)
=
\frac12
\operatorname{atan2}
\left(
S_2(r_k),
C_2(r_k)
\right)
\pmod{\pi}.
\]

Thus \(R_2\in[0,1]\) measures the strength of shell-level second-harmonic axial organization, while \(\alpha_2\) gives the corresponding undirected orientation.

These quantities are deterministic summaries of the observed conditional angular histogram. In particular,

\[
R_2^2=C_2^2+S_2^2
\]

is an algebraic identity, not independent evidence. CLO-SKET does not fit a von Mises distribution, estimate a likelihood-based concentration parameter, or reconstruct the complete angular density from \(F_2\).

The final representation aggregates this field into eight radial-magnitude descriptors and six axial-orientation descriptors,

\[
\mathbf{x}
=
\left[
\mathbf{x}_{F_2}^{(8)},
\mathbf{x}_{\alpha_2}^{(6)}
\right]
\in\mathbb{R}^{14}.
\]

The representation is explicit: each coordinate has a defined geometric construction and no PCA or learned embedding is used to create the 14-dimensional vector.

## 2.5 Coordinate dependence, discretization, and measurement sensitivity

Explicit geometric descriptors remain interpretable only if their dependence on coordinate conventions and numerical design choices is also examined. This issue is especially important for angular statistics because Cartesian harmonic components depend on the image coordinate frame even when the underlying axial structure is unchanged.

For a physical image rotation by \(\phi\),

\[
F_2'(r)
=e^{-\,\mathrm{i}2\phi}F_2(r),
\]

so

\[
R_2'(r)=R_2(r),
\]

while \((C_2,S_2)\) rotate in doubled-angle Cartesian space. A global-rotation control therefore distinguishes coordinate-dependent component behaviour from coordinate-free vector and magnitude behaviour. A separate garment-identity-randomized rotation control removes population-wide alignment while preserving repeated-sketch identity structure, providing a direct diagnostic of how much reconstruction depends on a shared canonical image frame.

Numerical discretization presents a related issue. The radial and angular histograms require finite binning, while several radial descriptors depend on support thresholds, local windows, and a finite analysis domain. CLO-SKET therefore treats these settings as measurement specifications rather than empirically optimal constants. Sensitivity analyses vary angular resolution, radial resolution, radial domain, support threshold, and concentration-window width while leaving the frozen primary representation unchanged.

This distinction is particularly important for localized radial descriptors. Integrated magnitude, radial centroid, and radial spread summarize broad radial structure. In contrast, onset, termination, concentration, and discrete peak location depend more directly on domain boundaries and resolution. Peak radius is therefore interpreted as a window-dependent localization statistic rather than a universal intrinsic radial scale.

## 2.6 Reconstruction as a shared-source consistency diagnostic

The reconstruction experiment uses the observed shell coordinate and second-harmonic magnitude as predictors,

\[
(r,R_2(r)),
\]

and estimates the Cartesian components

\[
\widehat C_2(r)
=
f_C(r,R_2(r)),
\qquad
\widehat S_2(r)
=
f_S(r,R_2(r)).
\]

The predicted vector then implies

\[
\widehat R_2(r)
=
\sqrt{
\widehat C_2(r)^2+
\widehat S_2(r)^2
},
\]

and

\[
\widehat\alpha_2(r)
=
\frac12
\operatorname{atan2}
\left(
\widehat S_2(r),
\widehat C_2(r)
\right)
\pmod{\pi}.
\]

Because predictors and targets arise from the same observed angular field, reconstruction is explicitly treated as a shared-source consistency diagnostic. It does not demonstrate semantic recognition, recovery of garment parts, reconstruction of the full angular distribution, or a physical radial law.

The rotation controls further constrain its interpretation. A common global rotation preserves the substantive coordinate-free reconstruction behaviour, whereas independent garment-identity rotations remove the shared absolute orientation frame. The purpose of these controls is not to improve reconstruction performance but to identify which aspects of recoverability arise from intrinsic harmonic magnitude and which depend on population-level coordinate alignment.

## 2.7 Phase conditioning and interpretation of angular error

The magnitude of a harmonic vector also determines the numerical conditioning of its orientation. For

\[
\alpha_2
=
\frac12
\operatorname{atan2}(S_2,C_2),
\]

a first-order perturbation gives

\[
d\alpha_2
=
\frac{
C_2\,dS_2-S_2\,dC_2
}{
2(C_2^2+S_2^2)
}
=
\frac{
C_2\,dS_2-S_2\,dC_2
}{
2R_2^2
}.
\]

By the Cauchy--Schwarz inequality,

\[
|d\alpha_2|
\le
\frac{
\sqrt{dC_2^2+dS_2^2}
}{
2R_2
}.
\]

Thus phase becomes intrinsically less well-conditioned as \(R_2\rightarrow0\), even for comparable Cartesian perturbations. This geometric fact is important when interpreting associations between harmonic magnitude and reconstruction error. A negative association between \(R_2\) and angular error should not automatically be treated as an independent empirical law: part of the relationship is expected from the geometry of phase estimation itself.

CLO-SKET therefore supplements the magnitude-error association with the Cartesian perturbation norm and the corresponding conditioning quantity

\[
\frac{
\|\Delta(C_2,S_2)\|
}{
2R_2
}.
\]

The role of this analysis is explanatory rather than causal. It tests whether observed out-of-fold angular errors are consistent with the expected conditioning geometry and explicitly avoids treating \(R_2\) alone as a deterministic cause of error.

## 2.8 Repeated sketches and identity-aware validation

Repeated observations create another form of dependency that is distinct from algebraic dependence. CLO-SKET contains multiple sketches associated with recovered source-garment identities. An image-level split can therefore place drawings of the same garment in both training and test sets, creating an evaluation that measures unseen image files rather than transfer to unseen garments.

The final validation design assigns complete garment identities to folds. Five category-balanced folds each hold out two identities per category, and train/test garment-identity overlap is zero. Reconstruction is consequently evaluated out of fold on unseen recovered garment identities.

The same principle governs uncertainty and confirmatory inference. Complete garment identities, not individual sketches, form the bootstrap resampling unit. Association analyses first reduce repeated sketches to garment-identity summaries and then perform permutation within category strata. These choices address the measured dependence created by repeated sketches, while inference remains conditional on the recovered garment identities being appropriate independent sampling units.

The distinction matters because increasingly large fashion datasets do not by themselves guarantee an appropriate statistical evaluation unit. GarmentSketch, VietFashion, and recent multimodal fashion datasets expand the scale and diversity of sketch-conditioned tasks (Baldrati et al., 2023; Bui et al., 2026; Cao et al., 2026), whereas the present study emphasizes dependency-aware evaluation within a smaller repeated-sketch dataset.

## 2.9 Research gap and study position

Recent work demonstrates rapid progress in sketch-conditioned fashion generation, editing, retrieval, and sewing-pattern reconstruction. Large generative and multimodal systems increasingly learn how sketches correspond to rendered garments, text, people, or production patterns. Explicit shape-analysis research, in parallel, establishes that garment outlines and periodic geometric signals can be represented numerically.

A narrower gap remains between these two traditions. Comparatively little work treats repeated garment sketches as a statistical measurement population and simultaneously keeps visible

\[
\text{representation}
\rightarrow
\text{algebraic dependency}
\rightarrow
\text{coordinate dependence}
\rightarrow
\text{parameter sensitivity}
\rightarrow
\text{validation unit}
\rightarrow
\text{uncertainty}
\rightarrow
\text{claim boundary}.
\]

CLO-SKET addresses this measurement problem rather than competing directly with generative fashion systems.

The study asks whether foreground geometry can be encoded as an explicit 14-dimensional radial--angular representation; whether its second-harmonic field exhibits reproducible structure for unseen garment identities; how reconstruction depends on the canonical coordinate frame; whether the representation is stable to reasonable discretization and parameter perturbations; why the second harmonic is the appropriate lowest-order axial statistic; and how observed harmonic magnitude and Cartesian reconstruction perturbation jointly condition axial error.

The intended contribution is therefore an auditable geometric measurement and validation framework for repeated garment sketches. It does not establish semantic garment understanding, causal geometric laws, a universally optimal radial window or harmonic order, prospective reliability classification, complete angular-density reconstruction, or human-like interpretation.
