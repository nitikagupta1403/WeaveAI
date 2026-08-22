# 1. Introduction

Garment sketches encode design form before physical realization. A small number of lines can establish silhouette, proportion, symmetry, dominant direction, and the spatial organization of garment structure. Yet a fashion sketch is not simply a low-resolution photograph. It is a sparse geometric construction whose information is distributed relative to an implied centre, across distance from that centre, and around angular directions.

This makes garment sketches relevant not only to recognition, retrieval, generation, editing, and garment reconstruction, but also to a more fundamental measurement question:

**Can the geometry of a garment sketch be represented explicitly in a form whose construction, assumptions, dependencies, and limits remain mathematically visible?**

Most computational research involving garment sketches has emphasized downstream tasks. Earlier work used drawings for garment modelling, fashion-flat classification, multimodal garment design, and transfer from stylized sketches to three-dimensional characters (Yasseen et al., 2013; An and Li, 2014; Wang et al., 2018; Fondevilla et al., 2021). More recent systems increasingly use sketches as conditioning signals for diffusion-based image synthesis, multimodal fashion editing, retrieval, and sewing-pattern reconstruction (Baldrati et al., 2023; Cao et al., 2023; Zhang et al., 2024; Singh and Patras, 2024; Huang et al., 2025; Bui et al., 2026; Cao et al., 2026).

These studies demonstrate that garment sketches contain computationally useful information. Their primary objective, however, is usually task performance: generating an image, retrieving a compatible garment, reconstructing a sewing pattern, or transferring style. Such performance does not necessarily reveal which geometric properties of a sketch carry the signal. Learned embeddings may be effective while leaving individual coordinates difficult to interpret, whereas explicit descriptors may appear interpretable while containing algebraically redundant quantities or relying on coordinate and discretization assumptions that have not been tested.

The present study addresses a narrower problem. Rather than treating a sketch principally as input to a generative or recognition model, we treat each sketch as an observed geometric object and ask whether its radial and angular organization can be summarized by a compact, explicit measurement.

For each sketch, foreground intensity is represented relative to an intensity-weighted centroid. A foreground location is described by radius \(r\) and angle \(\theta\), and foreground mass is accumulated into radial and angular bins. Within radial shell \(r\), normalization over angle produces the conditional angular distribution

\[
p(\theta_k\mid r)
=
\frac{
H(r,\theta_k)
}{
\sum_j H(r,\theta_j)
}.
\]

This construction separates radial position from angular organization and prevents shells containing more foreground mass from dominating merely because they contain more ink.

The angular structure of each shell is summarized through Fourier moments,

\[
F_m(r)
=
\sum_k
p(\theta_k\mid r)
e^{-\mathrm{i}m\theta_k}.
\]

The primary statistic is the second harmonic,

\[
F_2(r)
=
C_2(r)-\mathrm{i}S_2(r).
\]

Its magnitude is

\[
R_2(r)
=
|F_2(r)|
=
\sqrt{
C_2(r)^2+
S_2(r)^2
},
\]

and its axial orientation is

\[
\mu_2(r)
=
\frac12
\operatorname{atan2}
\left(
S_2(r),
C_2(r)
\right)
\pmod{\pi}.
\]

The use of \(m=2\) is dictated by axial symmetry rather than by retrospective model performance. Garment orientation is treated as undirected, so

\[
\theta
\equiv
\theta+\pi.
\]

Under a \(180^\circ\) reversal,

\[
F_m(\theta+\pi)
=
(-1)^mF_m(\theta).
\]

Odd harmonics therefore change sign, whereas even harmonics remain invariant. The second harmonic is consequently the lowest non-zero harmonic compatible with the required axial equivalence. Higher even harmonics can describe finer angular organization, but they do not replace the lowest-order axial statistic. This geometric rationale is evaluated empirically through a low-order \(m=1,2,3,4\) control rather than used as a post-hoc harmonic-selection procedure.

The shell-level harmonic field is reduced to an explicit 14-dimensional sketch representation. Eight coordinates summarize radial second-harmonic magnitude: integrated magnitude, magnitude-weighted radial centroid, radial spread, concentration near the discrete peak, onset radius, termination radius, peak radius, and peak magnitude. Six coordinates summarize axial structure: doubled-angle Cartesian encodings of the peak and magnitude-weighted mean orientations, together with axial coherence and orientation drift.

The representation deliberately distinguishes mathematical identities from empirical information. In particular,

\[
R_2(r)=|F_2(r)|
\]

is true by construction and does not constitute independent corroborating evidence. Similarly, raw axial angles are inappropriate as ordinary Euclidean coordinates because \(0^\circ\) and \(180^\circ\) denote the same axis. Axial directions are therefore represented through doubled-angle sine and cosine coordinates.

The study also separates global radial summaries from more localized statistics. Integrated magnitude, centroid, and spread describe broad radial organization. Peak radius, onset, termination, and concentration depend more directly on a finite radial domain and discretization. Peak radius is therefore retained as a useful localization statistic but is interpreted as secondary and sensitivity-qualified rather than as an intrinsic physical scale.

The representation enables a controlled information-reduction experiment. If the complete second harmonic is

\[
F_2(r)
=
C_2(r)-\mathrm{i}S_2(r),
\]

then its magnitude \(R_2(r)\) retains vector length but discards explicit phase. We therefore ask how accurately \(C_2(r)\) and \(S_2(r)\) can be estimated for previously unseen garment identities when a model receives only

\[
[r,R_2(r)].
\]

Predicted Cartesian components imply reconstructed magnitude and axial orientation through the same harmonic identities used for the observations.

This experiment has a deliberately restricted interpretation. Predictor and targets arise from the same observed conditional angular field; reconstruction is therefore a shared-source consistency diagnostic rather than recovery of an independent semantic or physical quantity. More importantly, phase is not mathematically determined by magnitude. A common coordinate frame may allow population-level relationships between radius, magnitude, and orientation to become statistically recoverable. The study therefore includes explicit rotation controls to distinguish intrinsic magnitude information from structure associated with the common image axes.

For a physical rotation by \(\phi\),

\[
F_2'(r)
=
e^{-\mathrm{i}2\phi}F_2(r),
\]

so

\[
R_2'(r)=R_2(r),
\]

while the Cartesian components and axial phase rotate. Global analytic rotations test whether coordinate-free reconstruction behaviour remains stable under a common change of axes. A complementary garment-identity-randomized rotation assigns independent orientations to different garment identities while preserving radius, \(R_2\), repeated-sketch structure, and validation folds. Together, these controls identify how much phase reconstruction depends on population-level alignment relative to the image coordinate system.

Explicit measurements also depend on numerical design choices. The present analysis therefore examines sensitivity to support threshold, concentration width, angular resolution, radial resolution, and radial-domain boundaries. These analyses do not search for a configuration that maximizes a downstream result. Instead, they ask which geometric summaries are stable to reasonable perturbations of the measurement procedure and which require more cautious interpretation.

A further issue arises when interpreting axial reconstruction error. The phase of a short harmonic vector is intrinsically less stable than that of a long one. For

\[
\mu_2
=
\frac12
\operatorname{atan2}(S_2,C_2),
\]

first-order perturbation gives

\[
d\mu_2
=
\frac{
C_2\,dS_2-S_2\,dC_2
}{
2R_2^2
},
\]

with

\[
|d\mu_2|
\leq
\frac{
\sqrt{dC_2^2+dS_2^2}
}{
2R_2
}.
\]

Thus, an empirical association between smaller \(R_2\) and larger angular error is not an isolated statistical phenomenon: it is partly expected from the conditioning geometry of phase estimation. The analysis therefore evaluates harmonic magnitude, Cartesian reconstruction perturbation, and their combined phase-conditioning quantity separately rather than treating \(R_2\) alone as a causal explanation of error.

The statistical design is equally important because CLO-SKET contains repeated sketches of the same source garments (Arnia, 2020). Filename and category structure recover 230 category-qualified garment identities, approximately ten sketches per identity. A cross-validation split over image files can place different renderings of the same garment into training and test sets, thereby evaluating unseen files rather than unseen garments.

Primary reconstruction therefore uses five category-balanced folds that withhold complete garment identities. Each test fold contains two identities from every garment category, and train/test garment-identity overlap is zero. Uncertainty estimation resamples complete garment identities rather than individual sketches, and confirmatory association analysis first reduces repeated sketches to garment-level summaries. Permutations are performed within garment category so that category composition remains fixed.

Against this background, the study addresses five questions:

1. **Representation:** Can garment-sketch foreground geometry be encoded as an explicit 14-dimensional radial–angular vector whose coordinates have defined mathematical meaning and exclude algebraically redundant quantities?

2. **Reconstruction and coordinate dependence:** How much of the observed second-harmonic Cartesian field and axial orientation can be reconstructed from radius and harmonic magnitude for previously unseen garment identities, and how much of that recoverability depends on the common image coordinate frame?

3. **Robustness:** How stable are broad and localized radial–angular descriptors to changes in support threshold, concentration width, angular resolution, radial resolution, and radial domain?

4. **Harmonic rationale:** Is the primary \(m=2\) statistic justified by the axial symmetry of the measurement and consistent with the observed low-order harmonic spectrum?

5. **Error geometry and association:** Are garment-level differences in axial reconstruction error associated with observed harmonic magnitude, and are those differences consistent with the perturbation conditioning of axial phase?

The contribution of CLO-SKET is therefore not a new Fourier transform, a semantic garment-recognition model, or a new generative fashion architecture. It is an explicit geometric measurement framework for repeated garment sketches that keeps the chain

\[
\text{geometry}
\rightarrow
\text{representation}
\rightarrow
\text{coordinate dependence}
\rightarrow
\text{parameter sensitivity}
\rightarrow
\text{validation unit}
\rightarrow
\text{uncertainty}
\rightarrow
\text{scope of inference}
\]

visible throughout the analysis.

More specifically, the study contributes a shell-conditioned radial–angular representation based on axial Fourier moments; a mathematically justified and empirically controlled choice of the second harmonic; garment-identity-disjoint reconstruction of the observed harmonic field; analytic and identity-randomized rotation controls; parameter and discretization sensitivity analyses; a perturbation-theoretic interpretation of phase error; and dependency-aware uncertainty and association analysis at the garment-identity level.

The intended claims remain narrow. The analysis does not establish semantic garment-part recognition, causal geometric laws, human-like visual understanding, a universally optimal harmonic order or radial domain, a prospective reliability classifier, likelihood-based circular modeling, or reconstruction of the complete angular density. Within these boundaries, it demonstrates how repeated garment sketches can be studied as explicit radial–angular observations while preserving the distinction between mathematical identity, empirical regularity, and conditional statistical evidence.
