# CLO-SKET — IVC Submission Manuscript

> **Submission front matter to complete before journal upload**
>
> - Final manuscript title: [TO BE CONFIRMED]
> - Author names: [TO BE CONFIRMED]
> - Affiliations: [TO BE CONFIRMED]
> - Corresponding author and email: [TO BE CONFIRMED]
>
> The scientific body below is assembled from the frozen repository source files. Do not edit scientific claims in this master independently; edit the canonical source section and rebuild instead.

---

# Abstract

Garment sketches encode design structure through multiple geometric organizations that need not be captured by a single representation. We investigate whether explicit radial–axial geometry provides reproducible information beyond conventional morphology in repeated garment sketches, while separating predictive utility from garment-specific correspondence. Using all 2,300 sketches in CLO-SKET, comprising 23 garment categories and 230 recovered garment identities, we construct a compact 14-dimensional representation from centroid-relative shell-conditioned second-harmonic geometry.

For foreground angular distribution \(p(\theta\mid r)\) at radial shell \(r\), the second harmonic is

\[
F_2(r)=\sum_k p(\theta_k\mid r)e^{-2\mathrm{i}\theta_k}
      =C_2(r)-\mathrm{i}S_2(r),
\]

from which radial organization and axial orientation are obtained as

\[
R_2(r)=|F_2(r)|,
\qquad
\alpha_2(r)=\frac{1}{2}\operatorname{atan2}\!\left(S_2(r),C_2(r)\right)
\pmod{\pi}.
\]

Eight radial descriptors summarize the distribution of \(R_2(r)\), while six axial descriptors encode orientation using doubled-angle coordinates, yielding an explicit 14-dimensional axial–radial representation. The second harmonic is used because \(m=2\) is the lowest non-zero Fourier order compatible with undirected axial orientation, \(\theta\equiv\theta+\pi\).

The central experiment tests whether this compact representation adds category-discriminative information beyond a frozen 135-dimensional morphology representation under category-balanced, garment-identity-disjoint validation. Morphology alone achieved a pooled out-of-fold macro-F1 of \(0.2978\); augmenting it with the 14-dimensional axial–radial representation increased macro-F1 to \(0.3358\), giving

\[
\Delta F_{1,\mathrm{macro}}=+0.0380.
\]

A category-stratified garment-identity bootstrap gave a 95% confidence interval of \([+0.0202,+0.0559]\), and the increment remained positive across all 10 repeated grouped partitions (mean \(+0.0323\), range \(+0.0206\) to \(+0.0433\)). Mechanistic ablation localized most of the direct increment to the radial component: adding the eight radial descriptors to morphology increased macro-F1 by \(+0.0268\), whereas the six axial descriptors alone contributed \(+0.0023\).

Critically, predictive improvement did not imply garment-specific complementary information. In a 2,000-replicate control that permuted complete axial–radial identity blocks within garment category while preserving category composition and block size, the correctly aligned increment did not exceed the misalignment null (null mean \(+0.0429\); empirical \(p=0.763\)). Thus, the observed gain cannot be attributed to exact morphology–axial–radial correspondence at the individual-garment level and is more consistent with category-level geometric organization.

Independent representation diagnostics establish the mathematical and numerical behavior underlying this result. Rigid-image rotation controls support the expected invariance of radial magnitude and doubled-angle equivariance of axial orientation; coordinate-frame randomization demonstrates that phase reconstruction depends substantially on canonical orientation; and sensitivity analyses distinguish stable global radial summaries from domain-sensitive localized descriptors.

These results establish a bounded but consequential finding: **explicit radial organization captures reproducible garment-category structure beyond a substantially larger morphology representation, but this additional utility is primarily distributional at the category level rather than evidence of garment-specific geometric complementarity.** The resulting framework provides both an interpretable representation of garment-sketch geometry and an identity-aware experimental procedure for determining where its predictive information resides.

**Keywords:** garment sketches; radial–axial geometry; second harmonic; Fourier descriptors; morphology; incremental representation value; grouped cross-validation; identity-aware validation

---

# 1. Introduction

Garment sketches occupy an unusual position in computational fashion. They are visually sparse, yet they encode substantial design structure: silhouette, proportion, symmetry, directional organization, and the placement of form relative to the garment centre. Contemporary systems have demonstrated that such sketches can support garment retrieval, image synthesis, editing, three-dimensional reconstruction, and sewing-pattern generation. In most of these settings, however, the sketch is treated primarily as an input signal whose usefulness is judged by downstream performance. Much less attention is given to a different question: **what geometric information is actually present in the sketch, and whether distinct geometric representations capture the same or different aspects of that information.**

This distinction matters because garment shape is not a single geometric property. A conventional morphology representation can describe properties of foreground form such as extent, occupancy, contour organization, and related shape statistics. The same sketch can also be viewed relative to its centre: structural evidence may occur preferentially at particular radial distances, and that evidence may exhibit characteristic orientation about the centre. These views are related because they arise from the same drawing, but they are not mathematically identical. Consequently, the presence of a second representation does not by itself establish that it contains useful information beyond morphology. That question requires an explicit incremental test.

We study this problem using CLO-SKET, containing 2,300 sketches from 23 garment categories. The repeated-sketch structure of the dataset is particularly important. The sketches correspond to 230 recovered source-garment identities, with approximately ten drawings per garment. Different sketches of the same source garment are therefore dependent observations. A random image-level train/test split can place renderings of the same garment on both sides of the validation boundary and thereby confound generalization to unseen files with generalization to unseen garment identities. Throughout this study, complete garment identities are consequently treated as the fundamental validation and resampling units.

## 1.1 Explicit radial–axial geometry

To characterize geometric organization beyond conventional morphology, we represent each sketch relative to its intensity-weighted centroid and examine the distribution of foreground evidence jointly over radius and angle. Within radial shell \(r\), foreground mass defines a conditional angular distribution \(p(\theta\mid r)\). Its second circular harmonic,

\[
F_2(r)=\sum_k p(\theta_k\mid r)\exp(-2\mathrm{i}\theta_k),
\]

provides two conceptually distinct quantities:

\[
R_2(r)=|F_2(r)|,
\qquad
\alpha_2(r)=\frac{1}{2}\arg F_2(r)\pmod{\pi}.
\]

Here, \(R_2(r)\) measures the strength of second-harmonic angular organization at radius \(r\), whereas \(\alpha_2(r)\) describes its undirected axial orientation. The use of the second harmonic follows from the axial equivalence \(\theta\equiv\theta+\pi\): \(m=2\) is the lowest non-zero Fourier order compatible with an orientation for which directions separated by \(180^\circ\) represent the same axis.

Rather than retaining the complete shell field as a high-dimensional representation, we summarize it with a compact 14-dimensional vector. Eight radial coordinates describe the distribution of second-harmonic magnitude across radius, including integrated magnitude, radial centroid, spread, concentration, support and peak quantities. Six axial coordinates describe peak and magnitude-weighted orientations through doubled-angle Cartesian encoding, together with axial coherence and orientation drift. Algebraically redundant quantities are excluded.

This construction provides an interpretable representation, but interpretability alone is not sufficient evidence of usefulness. Nor does mathematical difference from morphology imply empirically distinct information. The central question is therefore whether the compact axial–radial representation improves discrimination of previously unseen garment identities **after a substantially larger morphology representation is already available**.

## 1.2 From representation description to incremental information

Let

\[
\mathbf z_M\in\mathbb R^{135}
\]

denote the frozen morphology representation and let

\[
\mathbf z_R\in\mathbb R^{8},\qquad
\mathbf z_A\in\mathbb R^{6},\qquad
\mathbf z_{RA}=\mathbf z_R\oplus\mathbf z_A\in\mathbb R^{14}
\]

denote the radial, axial, and complete axial–radial representations, respectively.

The primary experiment compares a classifier receiving morphology alone with the same classifier receiving morphology augmented by the complete axial–radial vector. For a fixed evaluation score \(\mathcal S\), the primary effect is

\[
\boxed{
\Delta_{RA}
=
\mathcal S(\mathbf z_M\oplus\mathbf z_{RA})
-
\mathcal S(\mathbf z_M)
}
\tag{1}
\]

under identical garment-identity-disjoint folds, preprocessing, and classifier specification.

Equation (1) deliberately defines **incremental predictive utility**, not statistical independence. A positive \(\Delta_{RA}\) demonstrates that the augmented representation improves the specified prediction task under the locked protocol. It does not establish that axial–radial geometry is information-theoretically independent of morphology, nor does it identify the level at which the useful structure resides.

That distinction leads to a second question. Suppose correctly aligned axial–radial descriptors improve prediction beyond morphology. The improvement could depend on the particular radial–axial geometry of each garment, or it could arise from broader category-conditioned distributions. We distinguish these possibilities using a category-preserving alignment control. Complete axial–radial identity blocks are reassigned among garments within the same category while morphology, category composition, block-size structure, validation folds, and classifier specification remain fixed. This destroys exact garment-level morphology–axial–radial correspondence while preserving category-level axial–radial structure.

The comparison therefore separates two propositions that are easily conflated:

\[
\text{axial–radial descriptors add predictive utility}
\]

from

\[
\text{their utility requires correct garment-level correspondence}.
\]

The former is tested by the incremental contrast in Eq. (1); the latter requires the observed aligned increment to exceed the category-preserving misalignment distribution.

## 1.3 Why the distinction is scientifically important

Feature concatenation can produce an apparent performance gain for several reasons. A new feature block may encode genuinely useful instance-specific structure; it may provide a more convenient coordinate system for structure already associated with class; or its apparent benefit may be unstable across particular train/test partitions. Simply reporting that a concatenated model performs better cannot distinguish among these explanations.

We therefore treat incremental value as a sequence of increasingly restrictive tests. First, radial and axial components are evaluated separately to determine which mathematical component carries the observed utility. Second, complete garment identities rather than sketches are resampled to quantify uncertainty without treating repeated drawings as independent observations. Third, the complete experiment is repeated across multiple category-balanced identity partitions to assess split stability. Finally, category-preserving identity-block permutation tests whether correct garment-level alignment itself contributes beyond the category-level distribution of the added representation.

The radial–axial representation is also subjected to independent mathematical and numerical validation. Reconstruction experiments examine what information remains recoverable after explicit harmonic phase is omitted. Rigid-image rotations test the expected invariant behavior of radial magnitude and doubled-angle equivariance of axial orientation. Analytic coordinate-frame controls determine whether phase reconstruction reflects intrinsic magnitude information or shared orientation in the canonical image frame. Parameter-sensitivity analyses distinguish broad radial summaries from localized descriptors that depend more strongly on discretization and radial boundaries. Phase-conditioning analysis further establishes when axial orientation becomes numerically unstable as harmonic magnitude decreases.

These analyses have a different role from the incremental prediction experiment. They establish **what the representation measures, how it transforms, and where it becomes unreliable**. The incremental experiment establishes **whether the resulting measurements contribute predictive structure beyond morphology and at what level that contribution resides**.

## 1.4 Research questions and contributions

The study is organized around three primary research questions:

**RQ1 — Geometric representation.** Can garment sketches be represented by a compact and mathematically explicit radial–axial description whose radial and orientation components have defined transformation properties and measurable numerical limitations?

**RQ2 — Incremental representation value.** Does the 14-dimensional radial–axial representation add reproducible garment-category information beyond a frozen 135-dimensional morphology representation when validation withholds complete garment identities?

**RQ3 — Localization of incremental utility.** Which component of the representation carries the incremental utility, and does that utility require exact garment-level correspondence between morphology and radial–axial geometry, or can it be explained by category-level geometric structure?

The contributions are consequently not a new Fourier transform or a claim that handcrafted descriptors outperform learned fashion representations. Instead, the study contributes an explicit second-harmonic radial–axial measurement of garment sketches; a compact 14-dimensional representation with algebraic redundancy removed and axial quantities encoded according to their circular geometry; an identity-disjoint experimental framework for testing its incremental value beyond morphology; mechanistic radial/axial ablations; cluster-aware uncertainty and repeated-partition stability analysis; and a category-preserving identity-alignment control that distinguishes predictive improvement from garment-specific correspondence.

This distinction defines the intended scope of inference. Evidence that

\[
\mathcal S(\mathbf z_M\oplus\mathbf z_{RA})>\mathcal S(\mathbf z_M)
\]

supports incremental predictive utility under the tested task. Evidence that the aligned increment exceeds an appropriate misalignment null would additionally support a role for exact garment-level correspondence. Failure of the latter test would not invalidate the former; instead, it would localize the useful information at a different structural level.

The resulting framework therefore asks not merely whether an additional geometric representation *works*, but **what it contributes, whether that contribution reproduces under identity-aware validation, and where in the hierarchy from garment instance to garment category the useful geometric structure resides.**
---

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

---

# 3. Methods

## 3.1 Study design and scope

This study evaluates an explicit axial–radial representation of garment-sketch geometry and, as its central confirmatory question, tests whether that representation contributes reproducible garment-category information beyond a frozen morphology representation when complete source-garment identities are withheld from validation.

The study contains two linked but inferentially distinct components. First, a **representation-validation component** establishes the mathematical construction and numerical behavior of the axial–radial measurement: centroid-relative polar transformation, shell-conditioned angular distributions, second-harmonic magnitude and axial orientation, compact descriptor construction, reconstruction diagnostics, rotation controls, discretization and parameter sensitivity, phase conditioning, and garment-level association analysis. These analyses determine what the representation measures, how it transforms, and where its numerical limitations arise.

Second, a **locked incremental-value experiment** compares the frozen 135-dimensional morphology representation with the same representation augmented by the compact 14-dimensional axial–radial vector. This experiment uses identical category-balanced, garment-identity-disjoint folds, identical preprocessing, and one fixed classifier across all feature sets. Its primary estimand is the change in macro-F1 produced by adding the complete axial–radial representation to morphology. Radial-only and axial-only additions are mechanistic ablations and cannot replace the primary contrast.

The compact representation contains eight radial descriptors derived from second-harmonic magnitude and six axial descriptors represented with doubled-angle coordinates. No principal-component analysis, learned embedding, semantic segmentation, von Mises fitting, or reconstruction of the complete angular density is used to construct it.

A further category-preserving identity-block permutation distinguishes **incremental predictive utility** from **garment-specific correspondence**. A positive augmented-minus-morphology effect establishes utility for the tested category-discrimination task; only an observed effect exceeding the category-preserving misalignment null would support the stronger proposition that the utility depends on exact garment-level morphology–axial–radial correspondence. Statistical independence, information-theoretic uniqueness, semantic meaning, and causality are outside the claim boundary.

---

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

The choice \(m=2\) follows from the symmetry of the orientation quantity being represented rather than from retrospective comparison of harmonic performance. The representation targets undirected axial organization, so an axis at angle \(\theta\) is equivalent to the same axis at \(\theta+\pi\).

Under a \(180^\circ\) reversal,

\[
\theta
\mapsto
\theta+\pi.
\]

For harmonic order \(m\),

\[
e^{-\mathrm{i}m(\theta+\pi)}
=
e^{-\mathrm{i}m\theta}
e^{-\mathrm{i}m\pi}
=
(-1)^m
e^{-\mathrm{i}m\theta}.
\]

Hence

\[
F_m(\theta+\pi)
=
(-1)^mF_m(\theta).
\]

Odd harmonics change sign under axial reversal, whereas even harmonics are invariant. Consequently,

\[
m=2
\]

is the lowest non-zero harmonic compatible with this axial equivalence.

The higher even harmonic \(m=4\) is also axially invariant but represents finer angular organization. Harmonics \(m=1\) and \(m=3\) were used as directional controls and \(m=4\) as a higher-order axial control; these comparisons were descriptive and did not redefine the primary \(m=2\) representation.

---

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

## 3.11 Confirmatory incremental representation-value experiment

The central downstream experiment asked whether the frozen compact axial–radial representation adds garment-category information beyond the frozen morphology representation under validation that withholds complete garment identities.

Let

\[
\mathbf z_{R,i}\in\mathbb R^8,
\qquad
\mathbf z_{A,i}\in\mathbb R^6,
\qquad
\mathbf z_{RA,i}=\mathbf z_{R,i}\oplus\mathbf z_{A,i}\in\mathbb R^{14},
\]

and let

\[
\mathbf z_{M,i}\in\mathbb R^{135}
\]

denote the independently frozen morphology vector. Seven feature sets were fixed before the compact-representation outcomes were inspected:

\[
R,\quad A,\quad R{+}A,\quad M,\quad M{+}R,\quad M{+}A,\quad M{+}R{+}A,
\]

with dimensions

\[
8,\ 6,\ 14,\ 135,\ 143,\ 141,\ 149,
\]

respectively.

The primary augmented representation was

\[
\mathbf z_{MRA,i}
=
\mathbf z_{M,i}\oplus\mathbf z_{RA,i}.
\]

For score function \(\mathcal S\), the confirmatory effect was

\[
\Delta_{RA}
=
\mathcal S(M{+}R{+}A)-\mathcal S(M).
\]

Macro-F1 was the primary metric and balanced accuracy the secondary metric. The radial and axial mechanistic increments were

\[
\Delta_R
=
\mathcal S(M{+}R)-\mathcal S(M),
\]

and

\[
\Delta_A
=
\mathcal S(M{+}A)-\mathcal S(M).
\]

These ablations were retained regardless of their observed performance and were not eligible to replace \(\Delta_{RA}\) as the primary comparison.

The experiment was locked against outcome-dependent feature selection, classifier switching, hyperparameter search, category or identity removal, image-level random cross-validation, selective reporting of folds or repeated partitions, and promotion of a more favorable ablation to the primary hypothesis. A historical result from a broader 28-dimensional radial–angular representation had been seen before this experiment; this exposure was explicitly recorded. The compact 14-dimensional representation, its radial/axial decomposition, and the present confirmatory contrast were frozen separately before their scores were computed.

---

## 3.12 Identity-aware validation and fixed estimator

The 230 recovered garment identities were the indivisible grouping units. Five deterministic category-balanced folds were constructed so that each test fold contained exactly two garment identities from each of the 23 categories:

\[
46\ \text{test identities/fold},
\qquad
184\ \text{training identities/fold}.
\]

All repeated sketches belonging to a garment identity remained on the same side of a fold boundary. Train/test identity overlap was zero, and every sketch appeared in exactly one test fold.

Every feature set used the same estimator pipeline. Features were standardized using \(\texttt{StandardScaler}\) fitted only on the training portion of each fold, followed by multinomial logistic regression with

\[
\texttt{penalty}=\mathrm{L2},
\qquad
C=1.0,
\qquad
\texttt{solver}=\texttt{lbfgs},
\]

\[
\texttt{max\_iter}=5000,
\qquad
\texttt{class\_weight}=\texttt{None},
\qquad
\texttt{random\_state}=20260820.
\]

No classifier or hyperparameter was tuned separately for any feature block. Predictions from the five held-out folds were pooled to obtain the primary out-of-fold macro-F1 and balanced accuracy.

---

## 3.13 Identity-cluster uncertainty and repeated-partition stability

Uncertainty in the primary incremental effect was quantified by paired resampling of complete garment identities. Because unrestricted identity bootstrap samples can occasionally omit a garment category, the manuscript-facing robustness interval used a category-stratified identity bootstrap. Within each of the 23 categories, 10 garment identities were sampled with replacement; when an identity was selected, all of its repeated sketches and paired predictions from both \(M\) and \(M{+}R{+}A\) were retained.

For bootstrap replicate \(b\),

\[
\Delta_{RA}^{(b)}
=
\mathcal S^{(b)}(M{+}R{+}A)
-
\mathcal S^{(b)}(M).
\]

A total of

\[
B=5000
\]

replicates were generated with random state 20260820. Percentile 95% confidence intervals were defined by the 2.5th and 97.5th percentiles of the bootstrap distribution. The fraction of positive bootstrap replicates was treated descriptively and was not reported as a permutation \(p\)-value.

Partition sensitivity was assessed independently using 10 category-balanced grouped five-fold partitions with seeds

\[
20260820,20260821,\ldots,20260829.
\]

Within every repeat, each category again contributed two complete identities to each test fold, and the same locked estimator was used. No repeat was discarded. The distribution of \(\Delta_{RA}\), together with the radial increment \(\Delta_R\), was used to assess whether the observed effect depended on a particular deterministic identity partition.

---

## 3.14 Category-preserving garment-identity alignment permutation

Incremental predictive utility does not by itself show that the added axial–radial vector must correspond to the same individual garment as the morphology vector. To test this stronger proposition, a category-preserving alignment-permutation control was performed.

The morphology matrix, category labels, validation folds, estimator, and observed outcome labels remained fixed. Complete 14-dimensional axial–radial blocks were reassigned among garment identities **within the same garment category**. Reassignment was additionally restricted to identities with the same number of repeated sketches, so the 9-, 10-, and 11-sketch block structure was preserved exactly. This maintained the marginal category-conditioned axial–radial distribution while breaking exact garment-level correspondence wherever an alternative equal-size identity block existed.

For permutation \(b\), the null augmented effect was

\[
\Delta_{RA,\mathrm{null}}^{(b)}
=
\mathcal S\!\left(M+\pi_b(R{+}A)\right)
-
\mathcal S(M),
\]

where \(\pi_b\) denotes the category- and block-size-preserving identity reassignment. Structural audit showed that the procedure misaligned 97.3913% of sketch rows; the residual 2.6087% arose from singleton category-by-block-size groups for which no alternative equal-size identity existed.

The observed statistic was the correctly aligned effect

\[
\Delta_{RA,\mathrm{obs}}
=
\mathcal S(M{+}R{+}A)-\mathcal S(M).
\]

Using

\[
B=2000
\]

permutations and random state 20260820, the one-sided corrected empirical probability was

\[
p_{\mathrm{align}}
=
\frac{
1+
\sum_{b=1}^{B}
\mathbf 1
\left[
\Delta_{RA,\mathrm{null}}^{(b)}
\geq
\Delta_{RA,\mathrm{obs}}
\right]
}{
B+1
}.
\]

This test asks whether **correct garment-level alignment produces a larger increment than category-preserving misalignment**. Failure to reject this null does not negate a positive incremental effect; it limits its interpretation by showing that the observed utility need not depend on exact garment-level morphology–axial–radial correspondence.

---

## 3.15 Claim hierarchy for the incremental experiment

The confirmatory experiment was interpreted through an explicit hierarchy.

First, performance of \(R\), \(A\), or \(R{+}A\) alone demonstrates category-discriminative information in that representation under the tested classifier; it does not establish semantic interpretation.

Second,

\[
\Delta_{RA}>0
\]

with identity-cluster uncertainty excluding zero and positive effects across repeated grouped partitions supports reproducible **incremental predictive utility** beyond morphology under the locked task.

Third, radial and axial ablations localize which mathematical component carries the observed increment but do not redefine the primary hypothesis.

Fourth, evidence for **garment-specific correspondence** requires the correctly aligned \(\Delta_{RA}\) to exceed the category-preserving identity-misalignment null. Without such evidence, the appropriate interpretation is that the additional predictive utility is compatible with category-level distributional structure rather than exact garment-level complementarity.

None of these tests establishes statistical independence, information-theoretic uniqueness, semantic garment understanding, or causality.

---

## 3.16 Garment-identity-disjoint shell-field reconstruction

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

## 3.17 Rotation and coordinate-frame controls

Two complementary rotation controls evaluated the dependence of reconstruction on the common image coordinate frame.

### 3.17.1 Analytic harmonic rotation

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

### 3.17.2 Global-rotation control

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

### 3.17.3 Garment-identity-randomized rotation

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

## 3.18 Parameter and discretization sensitivity

Sensitivity analyses evaluated dependence of the radial–angular representation on the fixed numerical choices used in the primary measurement specification. The primary configuration was not altered after these analyses.

### 3.18.1 Support threshold

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

### 3.18.2 Concentration half-width

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

### 3.18.3 Radial-domain sensitivity

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

### 3.18.4 Angular-resolution sensitivity

The canonical 72 angular bins were coarsened to

\[
36
\quad\text{and}\quad
24
\]

bins by exact aggregation of adjacent angular mass bins. No image interpolation was used.

For each resolution, \(F_2\), \(C_2\), \(S_2\), \(R_2\), axial orientation, peak magnitude, and peak radius were recomputed. The 72-bin field served as the reference.

### 3.18.5 Radial-resolution sensitivity

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

## 3.19 Low-order harmonic control

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

## 3.20 Phase-conditioning analysis

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

## 3.21 Garment-level association analysis

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

## 3.22 Garment-cluster bootstrap

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

## 3.23 Category-stratified permutation inference

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

## 3.24 Outcome-defined error bands and threshold sensitivity

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

## 3.25 Algebraically coupled calibration diagnostic

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

## 3.26 Scope of inference

The study supports two distinct classes of claims. The representation-validation analyses support an explicit 14-dimensional second-harmonic description of garment sketches, its expected radial-magnitude and axial-orientation transformation behavior over the tested controls, numerical reconstruction diagnostics on withheld recovered garment identities, phase-conditioning analysis, parameter sensitivity, and cluster-aware garment-level associations.

The central confirmatory experiment supports a narrower downstream claim: under the locked logistic-regression protocol and garment-identity-disjoint validation, the compact axial–radial representation can be tested for reproducible incremental garment-category utility beyond the frozen 135-dimensional morphology representation. Bootstrap and repeated-partition analyses quantify uncertainty and split stability of that increment. Radial/axial ablations identify where the increment is concentrated.

The category-preserving alignment permutation imposes an additional claim boundary. Incremental predictive utility and garment-specific correspondence are not equivalent. Only an aligned effect exceeding the misalignment null would support the proposition that exact garment-level morphology–axial–radial pairing is necessary for the observed gain. Otherwise, the gain must be described more conservatively as compatible with category-level distributional geometric structure.

Several further boundaries are explicit. The identity

\[
R_2=|F_2|
\]

is algebraic and is not independent corroborating evidence. Reconstruction of \(C_2\) and \(S_2\) from \((r,R_2)\) is a shared-source consistency diagnostic because predictors and targets arise from the same conditional angular field. Rotation controls establish behavior only under the tested transformations and show that phase reconstruction depends substantially on population-level orientation relative to the common image frame. Localized radial descriptors, particularly peak radius and support boundaries, remain conditional on the chosen radial domain and discretization.

Finally, population-level inference is conditional on treating the 230 recovered garment identities as appropriate independent sampling units. No analysis establishes statistical independence between feature families, information-theoretic uniqueness, causal garment geometry, semantic garment-part recognition, human-like visual understanding, a physical radial law, a prospective reliability classifier, likelihood-based circular modeling, or reconstruction of the complete angular density.

---

# 4. Results

## 4.1 Study population and locked representations

All 2,300 CLO-SKET sketches were retained. Filename grammar and one explicitly recovered exceptional filename yielded 230 garment identities, exactly 10 identities in each of 23 garment categories. Complete garment identities contained 9–11 repeated sketches and were used as the indivisible validation and resampling units.

The independently frozen morphology matrix contained 135 coordinates. The manuscript-defined axial–radial representation contained eight radial and six axial coordinates,

\[
\mathbf z_{RA}=\mathbf z_R\oplus\mathbf z_A\in\mathbb R^{14}.
\]

The eight-dimensional radial block excluded radial extent because the stored quantity was exactly termination radius minus onset radius. Peak and magnitude-weighted axial orientations were encoded by doubled-angle cosine/sine pairs. The resulting 14-dimensional matrix reproduced the previously locked representation hash exactly. Seven feature sets entered the downstream experiment without outcome-dependent modification: \(R\), \(A\), \(R+A\), \(M\), \(M+R\), \(M+A\), and \(M+R+A\).

The five primary folds were category-balanced and garment-identity-disjoint. Every test fold contained 46 identities—two from each category—and every identity appeared in exactly one test fold. Train/test identity overlap was zero.

---

## 4.2 The compact axial–radial representation added predictive utility beyond morphology

Under the locked out-of-fold classifier, morphology alone achieved macro-F1 \(0.297788\) and balanced accuracy \(0.298261\). The complete compact axial–radial representation alone achieved macro-F1 \(0.219993\) and balanced accuracy \(0.231304\). When the 14 axial–radial coordinates were added to morphology, performance increased to macro-F1 \(0.335765\) and balanced accuracy \(0.336087\).

Thus, the preregistered primary contrast was

\[
\Delta_{RA}^{F_1}
=
0.335765-0.297788
=
+0.037977,
\]

with corresponding balanced-accuracy increment

\[
\Delta_{RA}^{BA}
=
0.336087-0.298261
=
+0.037826.
\]

The macro-F1 increment was positive in all five primary folds, ranging from \(+0.011157\) to \(+0.085268\). Balanced-accuracy differences were likewise positive in all five folds.

**Table 1. Locked pooled out-of-fold category-discrimination performance.**

| Feature set | Dimensions | Macro-F1 | Balanced accuracy |
|---|---:|---:|---:|
| \(R\) | 8 | 0.206831 | 0.224348 |
| \(A\) | 6 | 0.081165 | 0.106522 |
| \(R+A\) | 14 | 0.219993 | 0.231304 |
| \(M\) | 135 | 0.297788 | 0.298261 |
| \(M+R\) | 143 | 0.324540 | 0.325217 |
| \(M+A\) | 141 | 0.300087 | 0.300435 |
| **\(M+R+A\)** | **149** | **0.335765** | **0.336087** |

The observed improvement therefore establishes incremental predictive utility for the complete compact representation under the locked task. It does not by itself establish statistical independence or garment-specific complementarity.

---

## 4.3 Mechanistic ablation localized most direct utility to the radial block

The eight-dimensional radial representation was substantially more discriminative on its own than the six-dimensional axial representation: macro-F1 was \(0.206831\) for \(R\) compared with \(0.081165\) for \(A\). Their concatenation reached \(0.219993\).

The same pattern appeared when the blocks were added to morphology. The radial increment was

\[
\Delta_R^{F_1}
=
0.324540-0.297788
=
+0.026752,
\]

whereas the axial increment was

\[
\Delta_A^{F_1}
=
0.300087-0.297788
=
+0.002299.
\]

For balanced accuracy, the corresponding increments were \(+0.026957\) and \(+0.002174\). Adding the complete \(R+A\) block produced a larger macro-F1 increment, \(+0.037977\), than either component alone.

These ablations indicate that radial organization carries most of the direct incremental signal in this classifier, while the axial block alone adds little to morphology. The fact that \(M+R+A\) exceeded \(M+R\) descriptively does not constitute a separately preregistered significance test for the axial contribution conditional on \(R\).

---

## 4.4 Identity-cluster uncertainty supported a positive incremental effect

A category-stratified bootstrap resampled complete garment identities within each garment category while preserving the paired predictions from \(M\) and \(M+R+A\). Across 5,000 replicates, the mean macro-F1 increment was \(+0.037909\), with percentile 95% confidence interval

\[
[+0.020242,\,+0.055852].
\]

All 5,000 bootstrap replicates produced a positive macro-F1 difference. Balanced accuracy showed a mean increment of \(+0.037968\) with 95% interval

\[
[+0.020000,\,+0.056239],
\]

again with no non-positive replicate.

An unrestricted identity-cluster bootstrap, retained as an audit analysis, produced closely similar intervals: \([+0.019230,+0.055573]\) for macro-F1 and \([+0.019221,+0.057648]\) for balanced accuracy. The category-stratified analysis is emphasized because unrestricted resampling occasionally omitted an entire category.

**Table 2. Category-stratified garment-identity bootstrap for the primary contrast.**

| Metric | Observed \(\Delta\) | Bootstrap mean \(\Delta\) | 95% CI | Positive replicates |
|---|---:|---:|---:|---:|
| Macro-F1 | +0.037977 | +0.037909 | [+0.020242, +0.055852] | 5000 / 5000 |
| Balanced accuracy | +0.037826 | +0.037968 | [+0.020000, +0.056239] | 5000 / 5000 |

The bootstrap fraction positive is descriptive and is not interpreted as a permutation probability.

---

## 4.5 The incremental effect reproduced across independent grouped partitions

The locked comparison was repeated across 10 category-balanced grouped five-fold partitions. The full axial–radial increment was positive in every repeat.

For macro-F1,

\[
\overline{\Delta}_{RA}
=
+0.032253,
\qquad
SD=0.006805,
\]

with repeat-level values ranging from \(+0.020620\) to \(+0.043275\). Balanced-accuracy increments were also positive in all 10 repeats, with mean \(+0.031565\), standard deviation \(0.007362\), and range \(+0.019565\) to \(+0.043913\).

At the individual-fold level, 44 of 50 macro-F1 differences were positive and six were negative. The radial increment was positive in all 10 repeated partitions, with mean macro-F1 increment \(+0.028850\).

**Table 3. Stability of the primary increment across repeated garment-identity partitions.**

| Quantity | Mean | SD | Minimum | Maximum | Positive repeats |
|---|---:|---:|---:|---:|---:|
| \(\Delta_{RA}\), Macro-F1 | +0.032253 | 0.006805 | +0.020620 | +0.043275 | 10 / 10 |
| \(\Delta_{RA}\), balanced accuracy | +0.031565 | 0.007362 | +0.019565 | +0.043913 | 10 / 10 |
| \(\Delta_R\), Macro-F1 | +0.028850 | — | — | — | 10 / 10 |

The positive effect was therefore not confined to the single deterministic five-fold partition used for the primary pooled estimate.

---

## 4.6 Category-preserving misalignment did not support garment-specific correspondence

The strongest interpretive test produced a different result. In 2,000 permutations, complete axial–radial identity blocks were reassigned within garment category while matching block size exactly. This preserved category-conditioned axial–radial structure but broke exact morphology–axial–radial correspondence for 97.3913% of sketch rows.

For macro-F1, the correctly aligned observed increment was

\[
\Delta_{RA,\mathrm{obs}}=+0.037977.
\]

The category-preserving misalignment null had mean

\[
\mathbb E(\Delta_{RA,\mathrm{null}})=+0.042896,
\]

standard deviation \(0.007141\), and 2.5th, 50th, and 97.5th percentiles \(+0.029088\), \(+0.043094\), and \(+0.056838\), respectively. A total of 1,525 of 2,000 null permutations equalled or exceeded the observed increment, giving

\[
p_{\mathrm{align}}=0.762619.
\]

Balanced accuracy gave the same conclusion: observed increment \(+0.037826\), null mean \(+0.042258\), and empirical \(p_{\mathrm{align}}=0.729635\).

**Table 4. Category-preserving garment-identity alignment control.**

| Metric | Observed \(\Delta\) | Null mean | Null SD | Null 2.5% | Null 97.5% | Empirical \(p\) |
|---|---:|---:|---:|---:|---:|---:|
| Macro-F1 | +0.037977 | +0.042896 | 0.007141 | +0.029088 | +0.056838 | 0.762619 |
| Balanced accuracy | +0.037826 | +0.042258 | 0.007145 | +0.028261 | +0.056522 | 0.729635 |

The observed gain therefore did **not** exceed what was obtained after destroying almost all exact garment-level correspondence while retaining category-level structure. Experiment 06 consequently supports reproducible incremental predictive utility but does not support the stronger claim that the utility arises from garment-specific morphology–axial–radial complementarity.

The null mean being slightly larger than the observed aligned effect should not be interpreted as evidence that misalignment is intrinsically beneficial. The permutation experiment was designed to test whether correct alignment produces an unusually large increment; it did not. The scientifically supported localization is therefore conservative: the useful axial–radial signal is compatible with category-conditioned distributional structure and is not shown to require exact garment-level pairing.

---

## 4.7 Outcome-free visualization of radial–axial organization

To visualize what the measured field represents without selecting examples by classification success, prediction correctness, or Experiment 06 effect size, three sketches were chosen using frozen radial-organization magnitude alone at prespecified low, median, and high quantiles, with different garment categories enforced.

The selected examples were a Cardigan at the low radial-organization quantile, a Jumpsuit near the median, and a Dress at the high quantile. Their observed shell fields illustrate how \(R_2(r)\) localizes the strength of second-harmonic organization over radius while \(\alpha_2(r)\) records the corresponding undirected axial orientation. This figure is descriptive and is not evidence for category separation.

## 4.6 Study population and primary representation

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

## 4.7 Rigid-image rotation control of the 14-dimensional representation

A separate image-domain perturbation control evaluated whether the final 14-dimensional representation exhibited the intended transformation behavior when the raster sketch itself was rigidly rotated and the complete radial-angular measurement was recomputed.

All 2,300 sketches were evaluated at

\[
\phi
\in
\{-20^\circ,-10^\circ,-5^\circ,0^\circ,5^\circ,10^\circ,20^\circ\}.
\]

No garment labels were used and no predictive model was fitted.

### 4.7.1 Stability of the second-harmonic magnitude field

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

### 4.7.2 Axial orientation transformation consistency

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

### 4.7.3 Rotation-invariant directional scalars

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

## 4.8 Duplicate-image screening and garment-identity structure

All 2,300 file paths were unique. SHA-256 hashing detected no repeated raw files, and hashing of decoded pixel arrays detected no repeated decoded images. Perceptual-hash screening identified 11 candidate pairs at Hamming distance 0, 39 at distance at most 2, and 248 at distance at most 4. These candidates were treated as a screen for visual similarity rather than evidence of duplicated files or shared lineage.

Filename and category structure recovered 230 category-qualified garment identities, exactly 10 identities within each of the 23 categories. Individual garment identities contained 9–11 sketches and 9–11 distinct replicate identifiers. Eight identity–replicate combinations appeared more than once in the filename records.

Recovered garment identity was therefore used as the clustering unit for validation, bootstrap resampling, and confirmatory association analysis. The available metadata do not establish that the 230 recovered garment identities constitute mutually independent sampling units; population-level inference remains conditional on that assumption.

---

## 4.9 Garment-identity separation in validation

An initial image-level cross-validation design did not separate repeated sketches by garment identity: garment identities represented in each test fold were also represented in the corresponding training set. That design therefore evaluated unseen image files rather than unseen garments and was retained only as a sensitivity comparison.

The primary validation used five category-balanced, garment-identity-disjoint folds. Each test fold contained 46 complete garment identities—two identities from each of the 23 categories—and each training fold contained the remaining 184 identities. Test-fold sizes ranged from 459 to 461 sketches because the number of repeated sketches per garment identity varied slightly.

Every sketch and every recovered garment identity was held out exactly once. Train/test garment-identity overlap was zero in all five folds.

---

## 4.10 Garment-identity-disjoint reconstruction of \(C_2\) and \(S_2\)

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

## 4.11 Sensitivity to the validation unit

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

## 4.12 Garment-cluster uncertainty for reconstruction

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

## 4.13 Rotation and coordinate-frame control

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

### 4.13.1 Global rotation

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

### 4.13.2 Garment-identity-randomized rotation

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

## 4.14 Parameter and discretization sensitivity

Sensitivity analyses varied one construction choice at a time while preserving the primary representation and analysis.

### 4.14.1 Support threshold and concentration width

The primary support threshold was \(0.10\,m^\star\). Alternative thresholds of 0.05 and 0.15 left six of the eight radial descriptors exactly unchanged. Changes were confined primarily to onset and termination radii, which were exactly preserved for approximately 95–97% of sketches and remained within two shells for approximately 98–100%.

Changing the concentration half-width from the primary \(\pm4\) shell-coordinate units to \(\pm2\) or \(\pm6\) altered only the concentration coordinate by construction. The remaining seven radial descriptors were identical. Rank correlation of the concentration coordinate with its primary value remained 0.888 at half-width 2 and 0.949 at half-width 6.

### 4.14.2 Angular resolution

The canonical 72 angular bins were coarsened by exact mass aggregation to 36 and 24 bins, without image interpolation.

**Table 4. Sensitivity of the harmonic field to angular resolution.**

| Angular bins | \(R_2\) Spearman vs 72 | \(C_2\) Spearman | \(S_2\) Spearman | Median axial difference | Exact peak-radius agreement | Peak-magnitude Spearman |
|---:|---:|---:|---:|---:|---:|---:|
| 72 | 1.000000 | 1.000000 | 1.000000 | \(0.000^\circ\) | 1.000000 | 1.000000 |
| 36 | 0.999193 | 0.998844 | 0.971118 | \(2.530^\circ\) | 0.926522 | 0.998305 |
| 24 | 0.997051 | 0.995460 | 0.912654 | \(5.040^\circ\) | 0.862174 | 0.994252 |

Second-harmonic magnitude was therefore highly stable to substantial reductions in angular resolution. The larger changes in \(S_2\) than \(C_2\) were interpreted as coordinate-component effects rather than distinct physical signals.

### 4.14.3 Radial domain

The primary domain \(3.5\text{--}27.5\) contained endpoint peak locations for 22.04% of sketches. Specifically, 12.70% peaked at the lower endpoint and 9.35% at the upper endpoint.

The primary domain was compared with inward and outward alternatives extending from \(5.5\text{--}25.5\) through \(0.5\text{--}30.5\). Global radial summaries remained more stable than localized quantities. Relative to the primary domain, rank correlations at the widest tested domain \(0.5\text{--}30.5\) were 0.955 for integrated magnitude, 0.883 for radial centroid, and 0.786 for radial spread, whereas peak radius decreased to 0.511, concentration to 0.476, and onset radius to 0.471.

Among the 215 sketches whose primary peak occurred at the upper boundary \(r=27.5\), expansion to \(r=30.5\) caused 40.93% to move to a larger radius. Only 38.14% remained at 27.5 under the widest tested expansion.

Accordingly, peak radius is a window-dependent localization statistic. The endpoint occupancy and outward migration indicate partial boundary censoring, particularly for upper-boundary peaks.

### 4.14.4 Radial resolution

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

## 4.15 Low-order harmonic spectrum and justification of \(m=2\)

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

## 4.16 Garment-level associations and phase conditioning

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

### 4.16.1 Conditioning of axial phase

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

## 4.17 Outcome-defined error bands and threshold sensitivity

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

## 4.18 Algebraically coupled calibration diagnostic

At the sketch level, the Spearman correlation between observed peak-shell \(R_2\) and

\[
\Delta R_2
=
\widehat R_2-R_2
\]

was \(+0.1714\).

Because the observed value appears algebraically in \(\Delta R_2\), this correlation is mathematically coupled and cannot be interpreted as an independent association. It is retained only as a descriptive calibration diagnostic and receives no inferential \(p\)-value.

---

# 5. Discussion

## 5.1 Principal finding: incremental value without evidence of garment-specific alignment

The central result of this study is that a compact, explicitly defined axial–radial representation contributes reproducible garment-category information beyond the frozen morphology representation under garment-identity-disjoint validation. Morphology alone achieved macro-F1 \(0.297788\), whereas morphology augmented by the complete 14-dimensional axial–radial block achieved \(0.335765\), giving the preregistered increment

\[
\Delta F_1=+0.037977.
\]

The corresponding balanced-accuracy increment was \(+0.037826\). Category-stratified garment-identity bootstrap intervals excluded zero for both metrics, and the effect remained positive in all 10 repeated grouped partitions. These results establish that the compact representation contains predictive structure not fully exploited by the morphology baseline under the tested classification protocol.

The strongest control, however, materially narrows that interpretation. When complete axial–radial identity blocks were reassigned within garment category, preserving category and block-size structure while destroying exact garment-level correspondence for 97.39% of rows, the correctly aligned increment was not unusually large. The empirical alignment probabilities were \(p=0.762619\) for macro-F1 and \(p=0.729635\) for balanced accuracy. The null mean increment was in fact slightly larger than the observed aligned increment.

This is not evidence that misalignment improves prediction. Rather, the alignment permutation asks whether correct sketch/garment-level pairing yields an increment exceeding that obtainable from category-preserving axial–radial structure. It did not. The evidence therefore supports **incremental predictive utility**, but not the stronger proposition that this utility requires exact garment-specific morphology–axial–radial correspondence.

This distinction is central to the contribution. Without the alignment control, the improvement from \(M\) to \(M+R+A\) could easily be described as evidence of complementary garment-level geometry. The experiment shows that such wording would exceed the data. A more defensible interpretation is that the axial–radial representation captures category-conditioned geometric organization that remains useful alongside morphology, while the present experiment does not localize that gain to garment-specific correspondence.

---

## 5.2 What information is carried by the radial and axial blocks?

The ablation structure helps localize the observed predictive gain. The eight-dimensional radial block achieved substantially higher standalone category discrimination than the six-dimensional axial block: macro-F1 was \(0.206831\) for \(R\) and \(0.081165\) for \(A\). When added to morphology, the radial block increased macro-F1 by \(+0.026752\), whereas the axial block alone increased it by only \(+0.002299\). The complete block produced the largest observed increment, \(+0.037977\).

The direct empirical contribution is therefore concentrated primarily in radial organization. This is compatible with the construction of the representation. The radial coordinates summarize where and how strongly second-harmonic angular organization occurs relative to the sketch centroid—through integrated magnitude, centroid, spread, concentration, support limits, peak location, and peak strength. These quantities can vary systematically across garment categories even when exact correspondence to a particular morphology vector is unnecessary.

The axial block should be interpreted differently. Its low standalone performance does not imply that axial geometry is meaningless. Peak and magnitude-weighted orientations are coordinate-frame-dependent equivariant quantities, and the rotation analyses show that the canonical upright frame contains strong population-level orientation structure. Moreover, \(M+R+A\) descriptively exceeded \(M+R\). However, Experiment 06 did not preregister a separate conditional significance test of \(A\) given \(M+R\). We therefore do not claim an independently established axial increment beyond the radial block.

The ablation evidence supports a mechanistic description, not a hierarchy of universal feature importance: within this dataset, classifier, coordinate frame, and locked representation, radial second-harmonic organization accounts for most of the directly observed incremental category signal.

---

## 5.3 Why the alignment result matters scientifically

The alignment permutation distinguishes two forms of “complementarity” that are otherwise easy to conflate.

The first is **predictive complementarity**: adding one representation to another improves out-of-fold prediction. Experiment 06 supports this statement. The second is **instance-specific complementarity**: the additional benefit depends on the axial–radial representation belonging to the same garment instance or identity as the morphology representation. The alignment experiment does not support this stronger statement.

This distinction can be expressed schematically. Let \(M_i\) denote morphology for sketch \(i\), \(Z_i\) its correctly aligned axial–radial representation, and \(Z_{\pi(i)}\) a category-preserving identity-level reassignment. The observed comparison establishes

\[
\operatorname{Perf}(M_i,Z_i)
>
\operatorname{Perf}(M_i)
\]

under the locked evaluation. But the alignment control asks whether

\[
\operatorname{Perf}(M_i,Z_i)
>
\operatorname{Perf}(M_i,Z_{\pi(i)})
\]

more strongly than expected under the restricted permutation distribution. The data provide no such evidence.

This negative control is informative rather than disappointing. It identifies the scale at which the present evidence resides. The gain appears compatible with axial–radial distributions shared within garment categories rather than requiring exact garment-level coupling. In other words, the representation contributes useful structured information, but the experiment does not demonstrate that it encodes a unique geometric residual for each garment after morphology is known.

Several mechanisms could generate this pattern. Category-conditioned radial organization may be sufficiently stable that a misaligned representation from another garment in the same category still supplies useful category information. The morphology classifier may also leave category-level decision structure that the axial–radial block can reinforce without needing exact instance correspondence. These are plausible explanations, not separately tested mechanisms, and should not be elevated to causal conclusions.

The important methodological point is broader: an increase after feature concatenation is not, by itself, evidence that two representations contain uniquely paired information. Restricted alignment tests provide a practical way to separate predictive gain from instance-specific correspondence when repeated or grouped data permit such a control.

---

## 5.4 The second harmonic as an explicit axial measurement

The predictive experiment sits within a representation whose geometric meaning is defined independently of category performance. For each radial shell,

\[
F_2(r)
=
\sum_k p(\theta_k\mid r)e^{-i2\theta_k}
=
C_2(r)-iS_2(r)
=
R_2(r)e^{-i2\alpha_2(r)}.
\]

The magnitude

\[
R_2(r)=\sqrt{C_2(r)^2+S_2(r)^2}
\]

quantifies the strength of second-order angular organization, while

\[
\alpha_2(r)
=
\frac12\operatorname{atan2}(S_2(r),C_2(r))
\pmod{\pi}
\]

gives its undirected axial orientation.

The choice \(m=2\) follows from the symmetry being represented rather than from downstream classification performance. Because an axial orientation satisfies

\[
\theta\equiv\theta+\pi,
\]

a harmonic transforms under reversal as

\[
F_m(\theta+\pi)=(-1)^mF_m(\theta).
\]

The second harmonic is therefore the lowest non-zero Fourier order compatible with \(180^\circ\) axial equivalence. The empirical low-order spectrum is consistent with this choice: among \(m=1,2,3,4\), \(m=2\) had the largest median integrated and peak magnitude. That comparison is supportive, not a post-hoc selection rule.

The representation is geometric rather than semantic. A high \(R_2\) does not identify a sleeve, waistline, collar, flare, or other named garment component. Likewise, \(\alpha_2\) describes a harmonic axis, not a functional garment direction. Category discrimination demonstrates that these measurements carry information relevant to the tested labels; it does not convert the coordinates into semantic annotations.

---

## 5.5 Algebraic dependence and representation discipline

A central design principle was to keep deterministic relationships separate from empirical evidence. In particular,

\[
R_2=|F_2|=\sqrt{C_2^2+S_2^2}
\]

is an identity, not an independent confirmation among three measurements. Likewise, radial extent is exactly termination radius minus onset radius and was therefore removed from the compact radial block.

Axial directions cannot be treated as ordinary scalar angles because \(\alpha\equiv\alpha+180^\circ\). Peak and magnitude-weighted orientations were consequently represented by

\[
(\cos2\alpha,\sin2\alpha),
\]

which respects axial periodicity and permits ordinary Euclidean learning algorithms to operate on the encoded coordinates without introducing a discontinuity at the angular wrap point.

These choices matter for interpretation of Experiment 06. The observed gain is not obtained by simply appending obvious algebraic duplicates of the morphology baseline. The 14 coordinates are explicit summaries of a separately constructed radial–angular field. At the same time, “separately constructed” does not mean statistically independent: both representations ultimately derive from the same sketch images. The study therefore claims complementary predictive utility under a specified model, not information-theoretic independence.

---

## 5.6 Transformation behavior and the role of the canonical image frame

The representation contains both invariant and equivariant quantities under rigid in-plane rotation. For a physical rotation by \(\phi\),

\[
F_2'(r)=e^{-i2\phi}F_2(r),
\qquad
R_2'(r)=R_2(r),
\]

while axial orientation transforms as

\[
\alpha_2'=\alpha_2+\phi\pmod{\pi}.
\]

Accordingly, the doubled-angle pair transforms by the ordinary two-dimensional rotation \(R(2\phi)\), whereas magnitude-derived radial summaries and relative scalar quantities such as coherence are intended to remain invariant.

The rigid-image rotation control largely reproduced this structure over \(\pm5^\circ,\pm10^\circ,\pm20^\circ\). Radial-magnitude profiles showed small median perturbations attributable to raster interpolation and finite binning, and the doubled-angle orientations closely followed the imposed rotations. Magnitude-weighted mean orientation was especially stable, with 95th-percentile transformation error below \(0.85^\circ\) across the tested range. Coherence was numerically stable; orientation drift had small median changes but a wider upper tail.

A different rotation experiment exposed an important limitation of reconstruction from radius and magnitude. Common analytic rotations left coordinate-free reconstruction metrics essentially unchanged, whereas assigning independent rotations to garment identities increased median peak-shell axial error from \(4.104^\circ\) to \(44.675^\circ\), close to the \(45^\circ\) chance expectation for an axial angle.

Thus, radius and \(R_2\) do not intrinsically determine harmonic phase. Strong phase reconstruction in the canonical CLO-SKET images depends substantially on population-level orientation structure relative to the common image frame. This conclusion is conceptually consistent with the Experiment 06 alignment result: both controls caution against interpreting dataset-level regularities as uniquely paired garment-level geometry.

---

## 5.7 Garment identity defines the internal generalization target

CLO-SKET contains repeated drawings of common source garments. Treating all 2,300 sketches as independent would therefore overstate the effective independence of the dataset and could allow different renderings of the same garment to occur in both training and test sets.

The primary evaluation instead grouped the sketches into 230 recovered garment identities, with 10 identities in each of the 23 categories. Every primary test fold withheld two complete identities per category, and no garment identity occurred in both training and test data.

This design changes the interpretation of performance. The reported results concern transfer to previously unseen recovered garment identities **within CLO-SKET**. They do not establish generalization to another sketch dataset, another drawing population, another preprocessing pipeline, or another institutional or cultural source of garment designs.

The same grouping principle governs uncertainty estimation and the alignment control. Bootstrap resampling operates on complete garment identities, and misalignment is performed at the identity-block level rather than by independently shuffling sketch rows. This preserves the repeated-sketch dependency structure instead of manufacturing an artificially large number of independent units.

The identity labels themselves were reconstructed from filename and category structure, including one explicitly audited exceptional filename. They provide the strongest available grouping variable in CLO-SKET but cannot rule out higher-level dependence among source garments, designers, templates, or collections.

---

## 5.8 Reconstruction is a consistency experiment, not independent target prediction

The earlier reconstruction analysis remains useful, but its role is secondary to the incremental-representation experiment. It asks whether the Cartesian harmonic components \(C_2\) and \(S_2\) can be statistically reconstructed from radius and observed magnitude \(R_2\) under identity-disjoint validation.

Because

\[
R_2=\sqrt{C_2^2+S_2^2},
\]

the predictors and targets arise from the same harmonic field. Reconstruction therefore does not constitute prediction of an independently measured physical quantity. It is a controlled information-reduction experiment that probes regularities in the observed radial–angular field.

Under identity-disjoint validation, whole-field reconstructed \(R_2\) had RMSE \(0.145610\) and Pearson \(r=0.926390\); at the observed peak shell, RMSE was \(0.148303\), Pearson \(r=0.810543\), and median axial error \(4.104^\circ\). These values demonstrate reproducible internal structure but should not be interpreted as proof that magnitude mathematically determines phase.

The identity-randomized rotation control is decisive on this point. Once common absolute orientation was removed across identities, axial reconstruction approached chance. The original reconstruction performance therefore reflects statistical regularity in the canonical dataset rather than an intrinsic inversion of magnitude into phase.

This distinction also explains why reconstruction and Experiment 06 answer different questions. Reconstruction evaluates internal correspondence among quantities derived from the radial–angular field. Experiment 06 asks whether the compact representation improves an external downstream category-discrimination task relative to morphology. The latter provides the stronger evidence that the representation carries practically distinct predictive structure, although the alignment permutation limits the scale at which that distinctness can be localized.

---

## 5.9 Robustness is stronger for broad radial summaries than localized coordinates

The sensitivity analyses reveal a consistent hierarchy of numerical robustness. Integrated magnitude, radial centroid, and radial spread were comparatively stable across changes in radial domain and discretization. Localized descriptors—particularly peak radius, onset, termination, and concentration—were more dependent on analysis boundaries and resolution.

The primary radial domain contained endpoint peaks for approximately 22% of sketches. Among sketches whose primary peak occurred at the upper boundary \(r=27.5\), 40.9% moved to a larger radius when the domain was expanded to \(30.5\). Peak radius should therefore be interpreted as a domain-conditioned localization statistic rather than an intrinsic physical scale.

This qualification is particularly important because the radial block accounts for most of the direct incremental category signal in Experiment 06. The classifier result establishes usefulness of the **locked block as a whole**; it does not imply that every radial coordinate is equally stable or equally transferable. A feature may contribute predictive information in the fixed CLO-SKET measurement system while remaining sensitive to the chosen measurement window.

Accordingly, the 14-dimensional representation is best regarded as a reproducible measurement specification rather than an empirically optimized or universally invariant coordinate system.

---

## 5.10 Harmonic magnitude conditions axial uncertainty

The observed relationship between harmonic magnitude and axial reconstruction error has a direct perturbation-theoretic explanation. For

\[
\alpha_2
=
\frac12\operatorname{atan2}(S_2,C_2),
\]

a first-order perturbation gives

\[
d\alpha_2
=
\frac{C_2\,dS_2-S_2\,dC_2}{2R_2^2},
\]

and therefore

\[
|d\alpha_2|
\le
\frac{\sqrt{dC_2^2+dS_2^2}}{2R_2}.
\]

For a fixed Cartesian perturbation, phase becomes less well conditioned as harmonic magnitude decreases.

The garment-level results follow this geometry. Median observed peak \(R_2\) was negatively associated with median axial error (\(\rho=-0.356\)), but Cartesian reconstruction-error magnitude showed a stronger association (\(\rho=+0.760\)). Their combined conditioning quantity,

\[
\frac{\|\Delta(C_2,S_2)\|}{2R_2},
\]

was more strongly associated still (\(\rho=+0.789\)). Median axial error decreased from \(5.988^\circ\) in the weakest-\(R_2\) quartile to \(2.918^\circ\) in the strongest.

This provides an explanatory geometric account of the magnitude–error association without turning it into a causal statement. Increasing \(R_2\) is not shown to cause improved reconstruction; both harmonic strength and Cartesian prediction error contribute to angular uncertainty.

---

## 5.11 Inferential scope

The analysis deliberately separates mathematical identities, descriptive patterns, uncertainty estimates, and permutation-based hypothesis tests.

The primary Experiment 06 effect is supported by paired garment-identity bootstrap uncertainty and by reproducibility across repeated grouped partitions. The alignment permutation addresses a different hypothesis and fails to reject its restricted null. These results are not contradictory: the first establishes a reproducible predictive increment, whereas the second shows that the increment is not demonstrably dependent on exact garment-level alignment.

Similarly, the garment-level association between observed peak-shell \(R_2\) and axial reconstruction error is supported under category-stratified permutation, but this does not establish a causal effect of harmonic magnitude. Peak-radius associations are additionally sensitivity-qualified because peak localization depends materially on radial domain and resolution.

The effective inferential population is the 230 recovered garment identities, conditional on treating them as independent sampling units. CLO-SKET does not provide sufficient lineage metadata to establish independence among designers, templates, collections, or other higher-level sources. All population-level claims therefore remain internal to this dependency assumption.

No result in the study establishes information-theoretic independence between morphology and the axial–radial representation, semantic understanding of garment parts, causal geometric mechanisms, or universal performance beyond the evaluated dataset.

---

## 5.12 Scientific contribution

The individual mathematical tools used here—polar coordinates, Fourier moments, axial statistics, regularized classification, bootstrap resampling, and permutation testing—are established. The contribution lies in assembling them into an auditable representation-and-validation framework for sparse garment sketches and then testing progressively stronger interpretations of that representation.

The framework contributes four linked elements.

First, it provides an explicit 14-dimensional measurement of radial second-harmonic organization and axial orientation whose coordinates have defined geometric meanings and transformation rules.

Second, it evaluates that representation under garment-identity-disjoint validation rather than image-level random splitting, respecting the repeated-sketch structure of CLO-SKET.

Third, it demonstrates reproducible incremental category-discrimination value beyond a frozen 135-dimensional morphology representation: approximately \(+0.038\) macro-F1 in the primary partition, a positive category-stratified identity-bootstrap interval, and positive effects across all 10 repeated grouped partitions.

Fourth, it subjects the attractive interpretation of that gain to a stronger falsification control. Category-preserving identity-level misalignment does not reduce the increment sufficiently for correct alignment to appear exceptional. The contribution is therefore not a claim of uniquely paired garment-level complementarity. It is the narrower—and better supported—demonstration that a compact, geometrically interpretable axial–radial measurement contributes reproducible category-conditioned predictive structure beyond the tested morphology baseline.

This claim boundary is itself part of the methodological contribution. The study illustrates how representation research can move from “the added features improve prediction” to the more demanding question “what correspondence is actually required for that improvement?” without conflating the two.

---

## 5.13 Limitations

Several limitations constrain interpretation.

First, all experiments use a single dataset. Identity-disjoint validation tests internal transfer to unseen recovered garment identities within CLO-SKET, not external generalization.

Second, garment identities were reconstructed from filename and category structure rather than provided through an independently curated lineage table. Higher-level dependence among garments cannot be excluded.

Third, both morphology and axial–radial coordinates derive from the same source sketches. Incremental predictive utility therefore does not imply statistical or information-theoretic independence.

Fourth, the alignment control preserves garment category by design. It establishes that exact within-category garment pairing is not required for the observed gain, but it does not determine which category-conditioned distributional properties generate that gain. Resolving that mechanism requires additional experiments or external data.

Fifth, the canonical upright coordinate frame contains substantial population-level orientation structure. Phase reconstruction deteriorates to approximately chance after garment-identity-specific rotation, so orientation-dependent findings should not be assumed to transfer unchanged to arbitrarily oriented sketch collections.

Sixth, localized radial descriptors depend on analysis domain and discretization. Peak radius, onset, termination, and concentration require greater caution than integrated magnitude, centroid, and spread.

Seventh, \(m=2\) is a targeted lowest-order axial summary, not a complete representation of the angular distribution. Odd and higher even harmonics contain additional structure.

Eighth, the phase-conditioning analysis uses a first-order approximation and is most interpretable for local perturbations.

Finally, no garment-part annotations, independent physical measurements, causal interventions, or external prospective outcomes are available. The study therefore does not establish semantic garment understanding, causal design principles, calibrated reliability classes, or physical garment laws.

---

## 5.14 Future work

The most important next step is external validation on independently curated garment-sketch collections with explicit garment, designer, and collection identifiers. The 14-dimensional representation, morphology baseline, estimator, and evaluation protocol should be fixed before examining those data.

A second priority is to determine the source of the category-conditioned incremental signal revealed by Experiment 06. Because within-category misalignment preserved the gain, future analyses should test whether radial–axial category prototypes, distributional summaries, or other category-level geometric statistics reproduce the same benefit. Such analyses should be treated as new hypotheses rather than retroactive explanations of the current result.

A third direction is evaluation of explicitly orientation-normalized or rotation-equivariant variants. This would help separate information intrinsic to garment geometry from information introduced by the canonical acquisition frame.

Radial localization could also be improved through continuous or multiscale estimators and through domains normalized to garment extent. This is particularly important before treating peak radius as a transferable geometric characteristic.

Finally, semantic validation requires independent annotations. Expert-defined attributes such as silhouette, flare, symmetry, sleeve organization, or other design properties could be tested prospectively against the geometric coordinates. Such work would determine whether the present representation is merely category-informative or also corresponds to interpretable design concepts.


---

# 6. Conclusion

This study introduces a compact, explicit axial–radial representation of garment-sketch geometry and tests whether it contributes predictive information beyond a frozen morphology representation under garment-identity-disjoint validation. The 14-dimensional representation comprises eight radial descriptors of second-harmonic magnitude and six axial-safe orientation descriptors. Its construction follows directly from the geometry of undirected orientation: because an axial direction satisfies \(\theta\equiv\theta+\pi\), the second angular harmonic is the lowest non-zero Fourier order compatible with that symmetry.

The primary Experiment 06 result is a reproducible incremental predictive effect. Under the locked five-fold grouped evaluation, morphology alone achieved macro-F1 \(0.297788\) and balanced accuracy \(0.298261\), whereas morphology augmented with the complete axial–radial representation achieved macro-F1 \(0.335765\) and balanced accuracy \(0.336087\). The corresponding increments were

\[
\Delta F_1=+0.037977
\]

and

\[
\Delta BA=+0.037826.
\]

Category-stratified garment-identity bootstrap intervals excluded zero for both metrics: \([+0.020242,+0.055852]\) for macro-F1 and \([+0.020000,+0.056239]\) for balanced accuracy. The effect was also positive across all 10 repeated category-balanced grouped partitions, with mean macro-F1 increment \(+0.032253\) and range \(+0.020620\) to \(+0.043275\). Thus, the observed gain is not attributable to a single favorable identity partition.

The ablations localize most of the directly observed increment to radial organization. The radial block alone achieved macro-F1 \(0.206831\), compared with \(0.081165\) for the axial block, and adding the radial block to morphology increased macro-F1 by \(+0.026752\). Adding the axial block alone increased it by \(+0.002299\). The complete \(M+R+A\) representation nevertheless produced the largest primary score. These results support the predictive relevance of second-harmonic radial organization while leaving any additional conditional contribution of the axial block beyond \(M+R\) as a question for a separately specified test.

The alignment-permutation control places the strongest boundary on interpretation. Correctly aligned \(M+R+A\) did not outperform a category-preserving identity-level misalignment null unusually strongly: the empirical probabilities were \(p=0.762619\) for macro-F1 and \(p=0.729635\) for balanced accuracy. Consequently, the improvement over morphology cannot be attributed, on the present evidence, to exact garment-specific correspondence between the morphology and axial–radial representations. The supported claim is narrower: the compact axial–radial representation contains reproducible **category-conditioned predictive structure** that is useful alongside morphology, but the experiment does not demonstrate uniquely paired garment-level complementarity, statistical independence, or information-theoretic uniqueness.

The complementary geometric controls explain why such caution is necessary. Rigid-image rotation experiments supported the intended invariant/equivariant transformation structure of the representation over the tested perturbations, while garment-identity-specific analytic rotations caused peak-shell axial reconstruction error to approach the \(45^\circ\) chance expectation. Thus, strong phase regularities in upright CLO-SKET sketches depend substantially on the common image coordinate frame. Sensitivity analyses further showed that broad radial summaries are more stable than localized quantities such as peak radius, onset, termination, and concentration, which remain conditional on radial domain and discretization.

Taken together, the evidence supports an explicit but bounded contribution. CLO-SKET contains radial–angular geometric structure that can be measured compactly, transferred to withheld garment identities, and used to improve category discrimination beyond a morphology baseline. The study also shows that predictive improvement alone is insufficient to establish instance-specific representational complementarity: a category-preserving alignment control is required to test that stronger interpretation, and here that test was negative.

The principal contribution is therefore both representational and methodological: a mathematically explicit axial–radial measurement of sparse garment sketches, coupled to a dependency-aware validation framework that distinguishes **predictive increment** from **garment-specific correspondence**. By retaining that distinction, the study identifies not only what the representation adds, but also where the available evidence stops.


---

## Data Availability

The image data analyzed in this study are from the publicly available CLO-SKET dataset originally released by Fitri Arnia (2020) through Mendeley Data (Version 1; doi:10.17632/jt533nkhsf.1). This study did not collect a new image dataset and does not claim ownership of CLO-SKET. All 2,300 sketches available in the dataset were included in the analysis.

Garment identities used for dependency-aware validation were reconstructed from the category-qualified source identifiers encoded in the original CLO-SKET filenames, as described in the Methods. No additional private, proprietary, or manually annotated image dataset was used in the reported analyses.

Derived analysis code, representation-construction procedures, validation routines, and manuscript-supporting materials are maintained separately from the source image data so that redistribution of the original dataset is not required. The original CLO-SKET images should be obtained from the dataset's official Mendeley Data record.

## Code Availability

The curated computational materials supporting CLO-SKET Paper I are available in this repository under:

```text
papers/CLO-SKET/Codes_paper_I/
```

The public Paper-I package contains five scientific notebooks:

1. `01_Core_Radial_Angular_14D_and_Reconstruction.ipynb` — source-TIFF radial-angular construction, explicit second-harmonic measurements, final 14-dimensional representation, garment-identity-aware validation, and the canonical reconstruction analyses;
2. `02_Parameter_Sensitivity.ipynb` — prespecified parameter, radial-domain, angular-resolution, and radial-resolution sensitivity analyses;
3. `03_Harmonic_Order_Control.ipynb` — low-order harmonic diagnostics supporting the second-harmonic focus;
4. `04_Phase_Conditioning.ipynb` — axial phase/orientation conditioning analyses at the garment-identity level;
5. `05_Rotation_Controls.ipynb` — both analytic/randomized coordinate-frame controls and the distinct rigid-image invariance/equivariance control.

The package also contains `audit_Final_Validation_Shield.ipynb`, retained as an audit/provenance record rather than as the canonical source-to-result execution path.

The intended public computational lineage is source-code driven: the official CLO-SKET TIFF images are supplied to Notebook 01, and the downstream validation notebooks operate on the same Paper-I measurement lineage. Large historical runtime-memory pickle snapshots are not treated as the scientific source of record. Where historical checkpoint-loading cells remain for provenance, they should be interpreted as audit/recovery records unless the corresponding checkpoint is explicitly supplied.

Full-harmonic representation-selection, bandwise compression, and latent-geometry analyses belonging to Paper II are intentionally excluded from the Paper-I reproducibility package. The formal ownership boundary is documented in `P1_P2_CLAIM_FIREWALL.md`.

## Software Environment

The final validation environment recorded by the Paper-I validation shield was:

- Python 3.12.13;
- NumPy 2.0.2;
- pandas 2.2.3;
- scikit-learn 1.6.1;
- Linux x86_64 execution environment.

The scientific notebooks additionally use SciPy, Matplotlib, Pillow (`PIL`), Joblib, and standard-library modules as declared in their import cells. Pillow is used for TIFF decoding and for the rigid-image rotation control. Because exact SciPy, Matplotlib, Pillow, and Joblib version strings were not written into the frozen validation-shield environment record, no retrospective version number is asserted for those packages here. Their imports and algorithmic roles are explicit in the notebooks, and the manuscript reports the fixed image-rotation operator and interpolation settings used in the rigid-image control.

The canonical source notebook supports a configurable dataset location through `CLO_SKET_DATA_ROOT`; its historical Colab path is only the default used during the reported execution.

## Randomness and Reproducibility Lock

Randomness is restricted to explicitly declared model, resampling, permutation, or rotation-control procedures. Deterministic geometric construction of the radial-angular field and the 14-dimensional descriptor does not depend on random initialization.

The manuscript-facing stochastic controls currently frozen in the public notebooks include:

- `HistGradientBoostingRegressor` reconstruction models with `random_state=42`;
- bootstrap diagnostics in the core notebook with `BOOTSTRAP_SEED=20260820` and `N_BOOT=5000` where those diagnostics are used;
- held-out permutation-importance diagnostics with fold-specific seeds `42 + fold` and `142 + fold`;
- analytic garment-identity-randomized rotation control with 10 independent repeats and seeds `20260830, ..., 20260839`;
- the rigid-image rotation experiment itself is deterministic for a given input image and angle because the tested angles are fixed at `[-20, -10, -5, 0, 5, 10, 20]` degrees and the image operator is fixed.

Some older exploratory/category-discrimination cells retained inside the historical core notebook declare additional random states or permutation seeds. Those cells are not promoted here as independent manuscript claims; the governing numerical and inferential design is the one described in the final Methods and Results.

For reproducibility, users should preserve the exact garment-identity grouping structure, fold assignments where frozen, tested rotation angles, estimator hyperparameters, random states, and declared resampling units. A different random seed may produce numerically different bootstrap or randomized-control realizations even when the qualitative conclusion is unchanged.

## Reproducibility Boundary

The reproducibility package is intended to regenerate and audit the Paper-I measurement and validation chain without requiring Paper-II-only code. Historical `.pkl` checkpoint references that survive inside audit/recovery cells do not redefine the scientific source of record. The canonical evidence remains the explicit source code, the original CLO-SKET images, the final manuscript Methods/Results, and the claim firewall.

---

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
