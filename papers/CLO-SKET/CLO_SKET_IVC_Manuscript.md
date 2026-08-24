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

Garment sketches contain geometric structure that can be described through distinct geometric coordinate systems, but improved prediction after feature concatenation does not establish that the added information is specific to the same garment instance. We test this distinction in CLO-SKET using all 2,300 sketches from 23 categories and 230 recovered garment identities. From centroid-relative shell-conditioned angular distributions, we construct a compact 14-dimensional axial–radial representation based on the second circular harmonic,

\[
F_2(r)=\sum_k p(\theta_k\mid r)e^{-2\mathrm{i}\theta_k},
\]

whose magnitude \(R_2(r)=|F_2(r)|\) measures radial second-harmonic organization and whose half-phase \(\alpha_2(r)=\tfrac12\arg F_2(r)\pmod{\pi}\) represents undirected axial orientation. Eight radial descriptors and six doubled-angle axial descriptors form the final representation.

The prospectively locked confirmatory experiment asked whether these 14 coordinates add garment-category information beyond a frozen 135-dimensional morphology representation under category-balanced, garment-identity-disjoint validation. Morphology alone achieved pooled out-of-fold macro-F1 \(0.2978\) and balanced accuracy \(0.2983\); morphology plus the axial–radial representation achieved \(0.3358\) and \(0.3361\), respectively, yielding \(\Delta F_1=+0.0380\) and \(\Delta BA=+0.0378\). Category-stratified garment-identity bootstrap intervals excluded zero for macro-F1 (95% CI \([+0.0202,+0.0559]\)) and balanced accuracy (\([+0.0200,+0.0562]\)). The macro-F1 increment remained positive across all 10 repeated grouped partitions (mean \(+0.0323\), range \(+0.0206\) to \(+0.0433\)). Ablation localized most direct predictive value to the radial block: adding radial descriptors to morphology increased macro-F1 by \(+0.0268\), compared with \(+0.0023\) for the axial block alone.

A stronger category-preserving alignment control materially limited interpretation. Across 2,000 identity-block permutations that destroyed 97.39% of exact garment-level morphology–axial–radial correspondence while preserving category and block-size structure, the correctly aligned increment was not exceptional (null mean macro-F1 increment \(+0.0429\); empirical \(p=0.763\); balanced-accuracy \(p=0.730\)). Thus, the compact representation provides reproducible incremental predictive utility, but the evidence does not support uniquely paired garment-level complementarity. Rotation and sensitivity controls further show that radial magnitudes behave approximately invariantly under tested rigid rotations, axial orientation is equivariant in doubled-angle form, canonical image orientation contributes substantially to phase regularity, and localized radial descriptors are more measurement-sensitive than broad radial summaries. These controls bound interpretation of the representation; they are distinct from the confirmatory predictive-increment test.

The resulting contribution is both representational and methodological: an explicit axial–radial measurement of sparse garment-sketch geometry and an identity-aware validation framework that separates **predictive increment** from **garment-specific correspondence**.

**Keywords:** garment sketches; radial–axial geometry; second harmonic; Fourier descriptors; morphology; incremental predictive utility; grouped cross-validation; identity-aware validation

---

# 1. Introduction

Garment sketches are sparse visual objects, but their sparsity does not imply geometric simplicity. A few strokes can encode silhouette, proportion, bilateral organization, directional structure, and the distribution of form around the garment centre. Computational fashion systems commonly exploit such sketches as inputs for retrieval, generation, editing, reconstruction, or pattern-related tasks. In those settings, representation quality is usually judged by downstream performance. A different question is less often isolated: **what geometric organization is explicitly measurable in a garment sketch, and does that organization contribute predictive information beyond a conventional morphology representation?**

This question requires more than constructing another descriptor. Two representations extracted from the same image may differ mathematically yet carry largely overlapping predictive information. Conversely, a compact representation may add useful structure even when a substantially larger baseline is already available. Demonstrating such an increment requires the baseline and augmented representations to be compared under identical validation conditions. Demonstrating that the increment is *garment-specific* requires a stronger test still: the gain must depend on pairing each morphology vector with the axial–radial geometry of the correct garment.

The distinction is particularly important in CLO-SKET. The dataset contains 2,300 sketches from 23 garment categories, but these are not 2,300 independent garment instances. Filename and category provenance recover 230 source-garment identities, with 10 identities per category and approximately 10 repeated sketches per identity. Different renderings of the same source garment are therefore dependent observations. Image-level random splitting could place drawings of the same garment on both sides of the validation boundary and confound recognition of an unseen file with transfer to an unseen garment. We consequently treat the complete garment identity as the fundamental unit of validation, resampling, and permutation.

Against this dependency-aware design, we study an explicit radial–axial representation derived from the angular organization of foreground evidence around the sketch centroid. The objective is not to replace morphology or to claim a new Fourier formalism. It is to determine whether a small set of geometrically defined second-harmonic measurements contributes reproducible information beyond a frozen 135-dimensional morphology representation, and then to test how strongly that additional information can be localized.

## 1.1 Axial–radial geometry of a garment sketch

Let foreground evidence within radial shell \(r\) define the conditional angular distribution \(p(\theta\mid r)\). We characterize its undirected directional organization using the second circular harmonic

\[
F_2(r)
=
\sum_k p(\theta_k\mid r)e^{-2\mathrm{i}\theta_k}
=
C_2(r)-\mathrm{i}S_2(r).
\]

Its magnitude,

\[
R_2(r)=|F_2(r)|=\sqrt{C_2(r)^2+S_2(r)^2},
\]

measures the strength of second-harmonic angular organization at radius \(r\), while its half-phase,

\[
\alpha_2(r)
=
\frac12\operatorname{atan2}\!\left(S_2(r),C_2(r)\right)
\pmod{\pi},
\]

describes the corresponding undirected axial orientation.

The choice of \(m=2\) follows from the symmetry of an axis rather than from downstream classification performance. For axial orientation,

\[
\theta\equiv\theta+\pi.
\]

Under this reversal,

\[
e^{-\mathrm{i}m(\theta+\pi)}
=
(-1)^m e^{-\mathrm{i}m\theta},
\]

so \(m=2\) is the lowest non-zero Fourier order invariant to the \(180^\circ\) directional equivalence.

The complete shell field is summarized by a compact 14-dimensional vector. Eight radial coordinates describe the distribution of \(R_2(r)\): integrated magnitude, radial centroid, radial spread, radial concentration, onset radius, termination radius, peak radius, and peak magnitude. Radial extent is excluded because it is algebraically identical to termination radius minus onset radius. Six axial coordinates describe peak and magnitude-weighted orientations using doubled-angle Cartesian pairs,

\[
(\cos2\alpha,\sin2\alpha),
\]

together with axial coherence and orientation drift. This encoding respects the \(\pi\)-periodicity of an undirected axis and avoids treating axial angles as ordinary linear scalars.

The representation is therefore explicit and geometrically interpretable, but neither property demonstrates incremental value. That requires a downstream comparison against morphology.

## 1.2 From predictive increment to correspondence

Let

\[
\mathbf z_M\in\mathbb R^{135}
\]

denote the frozen morphology representation and

\[
\mathbf z_R\in\mathbb R^{8},
\qquad
\mathbf z_A\in\mathbb R^{6},
\qquad
\mathbf z_{RA}
=
\mathbf z_R\oplus\mathbf z_A
\in\mathbb R^{14}
\]

denote the radial, axial, and complete axial–radial representations.

For a fixed evaluation score \(\mathcal S\), the prospectively locked primary effect is

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

under the same garment-identity-disjoint folds, fold-local preprocessing, and classifier specification.

A positive \(\Delta_{RA}\) establishes **incremental predictive utility under the tested protocol**. It does not establish statistical independence between the representations. Both representations originate from the same sketch, and mathematical non-equivalence is not information-theoretic independence.

More importantly, Eq. (1) does not establish that the gain depends on the *correct pairing* of morphology and axial–radial geometry. Suppose \(\mathbf z_{RA,i}\) is the axial–radial representation of garment identity \(i\), and \(\mathbf z_{RA,\pi(i)}\) is reassigned from another identity in the same garment category. A garment-specific complementarity interpretation requires evidence not merely that

\[
\mathcal S(\mathbf z_{M,i},\mathbf z_{RA,i})
>
\mathcal S(\mathbf z_{M,i}),
\]

but that correct alignment is unusually advantageous relative to category-preserving misalignment:

\[
\mathcal S(\mathbf z_{M,i},\mathbf z_{RA,i})
>
\mathcal S(\mathbf z_{M,i},\mathbf z_{RA,\pi(i)}).
\tag{2}
\]

We test Eq. (2) by permuting complete axial–radial identity blocks within garment category while matching block size. This destroys almost all exact garment-level correspondence while retaining category membership, repeated-sketch block structure, validation design, and the marginal category-conditioned axial–radial distributions. The experiment therefore separates **predictive increment** from **garment-specific correspondence**.

## 1.3 Evidence hierarchy

The study is designed as a sequence of increasingly restrictive questions rather than a single performance comparison.

First, the seven locked feature sets \(R\), \(A\), \(R+A\), \(M\), \(M+R\), \(M+A\), and \(M+R+A\) establish standalone discrimination, the primary morphology-to-augmented contrast, and radial/axial ablations under one common estimator.

Second, uncertainty in the primary contrast is quantified by resampling complete garment identities. A category-stratified identity bootstrap preserves all 23 garment classes in every replicate and avoids treating repeated sketches as independent units.

Third, the full comparison is repeated across 10 independently generated category-balanced grouped partitions. This asks whether the increment survives changes in which garment identities define the train/test boundary rather than depending on a favorable deterministic split.

Fourth, the category-preserving identity-block permutation in Eq. (2) asks the strongest interpretive question: whether exact garment-level morphology–axial–radial correspondence is required for the observed benefit.

These predictive analyses are complemented by representation diagnostics that answer different questions. Rigid-image rotations test the expected invariance of radial magnitude and equivariance of axial orientation. Coordinate-frame randomization tests whether phase reconstruction reflects intrinsic information in magnitude or population-level orientation structure in the canonical image frame. Radial-domain and discretization analyses identify descriptors whose numerical values are sensitive to the measurement specification. Phase-conditioning analysis explains why axial uncertainty increases as harmonic magnitude weakens.

Together, these analyses distinguish four levels of evidence: **what is measured; whether it transforms as intended; whether it improves prediction; and whether that improvement requires correct garment-level correspondence.**

## 1.4 Research questions

The study addresses three primary research questions.

**RQ1 — Representation validity.** Can sparse garment sketches be summarized by a compact second-harmonic axial–radial representation with explicit geometric meaning, correct axial encoding, defined transformation behavior, and identifiable numerical limitations?

**RQ2 — Incremental predictive value.** Does the locked 14-dimensional axial–radial representation improve garment-category discrimination beyond a frozen 135-dimensional morphology representation when complete garment identities are withheld from training?

**RQ3 — Localization of the increment.** Is the observed increment concentrated in radial or axial organization, is it reproducible across garment-identity partitions, and does it require exact garment-level correspondence between morphology and axial–radial geometry?

RQ3 deliberately contains a falsifiable claim boundary. Evidence for RQ2 does not imply a positive answer to the alignment component of RQ3. A representation may contribute reproducible category-conditioned structure even if correct within-category garment pairing is unnecessary.

## 1.5 Contributions and scope

The contribution is not a new Fourier transform, a semantic garment-part model, or a claim that handcrafted descriptors supersede learned fashion representations. It is an auditable representation-and-validation framework for asking what explicit radial–angular geometry contributes beyond morphology.

Specifically, the study contributes: (i) a mathematically defined 14-dimensional second-harmonic axial–radial representation with algebraic redundancy removed and axial quantities encoded in doubled-angle coordinates; (ii) garment-identity reconstruction and category-balanced identity-disjoint validation for all 2,300 CLO-SKET sketches; (iii) a locked incremental test against a 135-dimensional morphology baseline with radial and axial ablations; (iv) category-stratified garment-identity bootstrap uncertainty and repeated grouped-partition stability analysis; (v) a category-preserving identity-level alignment permutation that tests whether predictive gain requires correct garment pairing; and (vi) rotation, reconstruction, sensitivity, harmonic, and conditioning controls that define the representation's mathematical behavior and interpretive limits.

The intended inference is correspondingly bounded. A positive value of Eq. (1) supports incremental predictive utility for the tested garment-category task. A positive alignment test in Eq. (2) would additionally support garment-specific correspondence. Neither result, alone or together, would establish semantic understanding, causality, or information-theoretic independence.

The central methodological premise is therefore simple: **showing that an added representation improves prediction is only the beginning of the analysis. The stronger scientific question is what structure must be preserved for that improvement to survive.**

---

# 2. Related Work

## 2.1 Garment sketches in computational fashion

Garment sketches have become established inputs to computational fashion systems, particularly for reconstruction, generation, editing, and retrieval. Geometry-oriented work has shown that sparse drawings can constrain garment form: Yasseen et al. (2013) converted mannequin-guided sketches into garment meshes, Wang et al. (2018) linked sketched fold patterns with sewing-pattern parameters, body shape, and simulated garments, and Fondevilla et al. (2021) transferred fashion-sketch style to three-dimensional characters. More recently, SketchTailor predicts garment patterns from a single sketch using a Vision Mamba encoder and deformable Transformer decoder (Huang et al., 2025).

A parallel literature treats sketches primarily as conditioning signals for learned image models. Multimodal Garment Designer combines garment sketches with text and human pose for latent-diffusion fashion editing (Baldrati et al., 2023). TexControl uses sketch guidance in a two-stage diffusion pipeline designed to preserve outline before texture refinement (Zhang et al., 2024), while FashionSD-X and related multimodal systems similarly use sketches to constrain fashion synthesis. Recent benchmarks further expand the scale and scope of sketch-conditioned fashion research: GarmentSketch contains 26,249 sketches across 21 garment categories paired with textual descriptions for sketch-guided generation (Bui et al., 2026), and VietFashion studies sketch–text composed retrieval for culturally specific garments using 650 human-drawn sketches and a substantially larger associated image collection (Cao et al., 2026).

These systems establish that garment sketches are computationally informative. Their principal scientific question, however, is usually whether a sketch can improve or control a downstream task. The present study asks a narrower representation question: **which explicitly measurable geometric organization is present in the sketch, whether it contributes information beyond morphology, and what correspondence must be preserved for that contribution to survive.**

## 2.2 Explicit shape representations and frequency-domain descriptors

Explicit numerical representations of garment form predate modern generative models. An and Li (2014) combined wavelet Fourier descriptors with supervised dimensionality reduction for fashion-flat classification, while Tsuru et al. (2021) represented garment silhouettes through standardized measurements and analysed designer collections using multidimensional scaling and clustering. More broadly, Fourier descriptors provide classical representations of periodic outline structure (Zahn and Roskies, 1972), and geometric morphometrics provides established tools for quantitative curve and shape analysis (Bookstein, 1997; McCane, 2013).

Frequency-domain computation has also been incorporated into contemporary fashion synthesis. Liang et al. (2023), for example, used Fast Fourier Transform features to model periodic texture structure in controllable garment-image generation. That use differs from the present one in both signal and purpose. Here, Fourier analysis is not applied to texture or used as an internal neural-network feature. It is applied to the **angular distribution of foreground sketch geometry at fixed radial distance**, producing explicit measurements whose magnitude and phase have defined geometric interpretations.

Accordingly, novelty is not claimed for polar coordinates, Fourier analysis, shape descriptors, or circular statistics individually. The relevant contribution is their combination into a compact radial–axial representation whose algebraic dependencies, transformation behavior, numerical sensitivity, incremental predictive value, and alignment dependence are tested separately.

## 2.3 Radial–angular and axial geometry

Relative to a foreground centroid \((c_x,c_y)\), each retained sketch location can be represented by

\[
r=\sqrt{(x-c_x)^2+(y-c_y)^2},
\qquad
\theta=\operatorname{atan2}(y-c_y,x-c_x).
\]

For radial shell \(r_k\), foreground mass defines a conditional angular distribution

\[
p(\theta_j\mid r_k)
=
\frac{H(r_k,\theta_j)}
{\sum_{j'}H(r_k,\theta_{j'})},
\]

where \(H(r_k,\theta_j)\) is the foreground mass in the corresponding radial–angular bin. Its circular harmonic of order \(m\) is

\[
F_m(r_k)
=
\sum_j p(\theta_j\mid r_k)e^{-\mathrm{i}m\theta_j}.
\]

The present representation focuses on \(m=2\) because garment orientation at this level is treated as **axial** rather than directional. Axial observations identify directions separated by \(180^\circ\), so \(\theta\equiv\theta+\pi\). Circular-statistical treatment therefore requires doubled angles (Jammalamadaka and SenGupta, 2001). Under a half-turn,

\[
F_m(\theta+\pi)=(-1)^mF_m(\theta),
\]

making \(m=2\) the lowest non-zero harmonic compatible with axial equivalence.

For

\[
F_2(r)=C_2(r)-\mathrm{i}S_2(r),
\]

the magnitude and axial orientation are

\[
R_2(r)=\sqrt{C_2(r)^2+S_2(r)^2}
\]

and

\[
\alpha_2(r)
=
\frac12\operatorname{atan2}\!\left(S_2(r),C_2(r)\right)
\pmod{\pi}.
\]

This distinction between magnitude and phase is fundamental. \(R_2\) measures the strength of second-harmonic organization; \(\alpha_2\) measures its undirected orientation. Because

\[
R_2^2=C_2^2+S_2^2,
\]

these are not independent empirical measurements of the same phenomenon. The magnitude is algebraically determined by the Cartesian harmonic components.

The final CLO-SKET representation compresses the shell field into eight radial-magnitude descriptors and six axial descriptors. Peak and magnitude-weighted axial directions are encoded as \((\cos2\alpha,\sin2\alpha)\), respecting their \(\pi\)-periodicity. No PCA, learned embedding, or outcome-dependent feature selection is used to construct the 14-dimensional vector.

## 2.4 Transformation behavior and coordinate-frame dependence

Explicit orientation measurements are meaningful only when their behavior under coordinate transformations is clear. For a rigid in-plane rotation by \(\phi\),

\[
F_2'(r)=e^{-\mathrm{i}2\phi}F_2(r),
\]

and hence

\[
R_2'(r)=R_2(r),
\qquad
\alpha_2'(r)=\alpha_2(r)+\phi\pmod{\pi}.
\]

Thus second-harmonic magnitude is theoretically rotation invariant, whereas phase is equivariant. In doubled-angle Cartesian form, the axial pair transforms by an ordinary two-dimensional rotation through \(2\phi\).

This distinction is relevant to garment-sketch datasets because sketches are commonly stored in a canonical upright frame. Strong regularity in axial phase can therefore arise from the acquisition coordinate system as well as from garment geometry. A model that reconstructs or predicts orientation successfully in an upright dataset need not retain that ability after identity-specific rotations destroy population-wide alignment.

The present study consequently separates physical rigid-image rotation tests from analytic coordinate-frame randomization. The former asks whether the implemented descriptors approximately obey their theoretical transformation laws despite rasterization and binning. The latter asks whether observed phase recoverability depends on the shared canonical frame. This distinction prevents coordinate-frame regularity from being interpreted as intrinsic phase information.

## 2.5 Measurement sensitivity and conditioning

Explicit descriptors also depend on their measurement specification. Radial and angular histograms require finite discretization, and localized radial summaries depend on a finite analysis domain, support threshold, and neighborhood definition. These parameters are therefore treated as measurement choices rather than hyperparameters optimized for downstream performance.

Broad summaries such as integrated magnitude, radial centroid, and radial spread aggregate information across many shells. Peak radius, onset, termination, and local concentration depend more directly on domain boundaries and discretization. A peak located at the largest analysed radius, for example, is inherently censored by the measurement window. Sensitivity analysis is therefore necessary before a localized descriptor can be interpreted as an intrinsic geometric scale.

Phase has a separate conditioning problem. For

\[
\alpha_2
=
\frac12\operatorname{atan2}(S_2,C_2),
\]

a first-order perturbation yields

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

Orientation is consequently ill-conditioned as harmonic magnitude approaches zero. Associations between \(R_2\) and angular error cannot automatically be interpreted as independent empirical laws; part of that relationship follows from the geometry of phase estimation itself. This motivates analysing Cartesian perturbation magnitude together with \(R_2\), rather than attributing angular error to magnitude alone.

## 2.6 Repeated observations and identity-aware validation

A separate methodological issue concerns dependency among observations. When several sketches depict the same source garment, individual images are not exchangeable independent garment instances. An image-level random split may therefore place different renderings of one garment in both training and test sets. Performance under such a split can reflect transfer across repeated renderings rather than transfer to unseen garments.

The relevant validation unit should follow the scientific generalization target. In CLO-SKET, the recoverable unit is the source-garment identity. Complete identities are therefore assigned to folds, bootstrap resamples, and alignment permutations. This changes the effective sample size from 2,300 sketch files to 230 garment identities for inferential purposes and makes the reported target explicit: generalization to withheld recovered garment identities within the same dataset.

Group-aware validation is necessary but not sufficient for claims about complementary representations. Even when two feature blocks are evaluated on unseen identities, improved prediction after concatenation does not establish that their useful information is uniquely paired at the identity level. The additional block may instead carry class-conditioned structure that remains useful when paired with another member of the same class.

## 2.7 Predictive complementarity versus instance-specific correspondence

This distinction is the principal methodological gap addressed here.

Suppose a baseline representation \(M_i\) and an added representation \(Z_i\) are extracted from the same observation. If

\[
\operatorname{Perf}(M_i,Z_i)>\operatorname{Perf}(M_i),
\]

then \(Z\) has incremental predictive utility under that evaluation. This is a meaningful result, but it does not determine **why** the additional block helps.

A stronger claim is that the benefit depends on the exact pairing between \(M_i\) and \(Z_i\). That proposition requires comparison with a restricted misalignment null,

\[
\operatorname{Perf}(M_i,Z_i)
\quad\text{versus}\quad
\operatorname{Perf}(M_i,Z_{\pi(i)}),
\]

where the permutation \(\pi\) destroys instance correspondence while preserving nuisance structure that could otherwise make the test trivial. In the present setting, complete axial–radial identity blocks are permuted within garment category and matched by block size. Category information and repeated-measure structure are retained; exact morphology–axial–radial pairing is largely removed.

This control asks a different question from ordinary permutation importance, feature ablation, or dimensionality controls. Ablation asks whether a block contributes to prediction. Restricted misalignment asks whether the contribution depends on belonging to the **same garment identity**. The two hypotheses can therefore yield different conclusions without contradiction.

For representation studies, this distinction is consequential. Calling two feature families “complementary” solely because their concatenation improves classification can overstate the evidence. The more precise hierarchy is:

\[
\text{different construction}
\not\Rightarrow
\text{incremental utility}
\not\Rightarrow
\text{instance-specific correspondence}
\not\Rightarrow
\text{statistical independence}.
\]

Each implication requires its own empirical or mathematical support.

## 2.8 Position of the present study

The literature establishes three relevant foundations: garment sketches are useful computational signals; explicit geometric and frequency-domain representations can summarize shape; and axial/circular statistics provide the correct mathematics for undirected orientation. What is less commonly combined is a validation framework that asks, in sequence, whether an explicit sketch representation is geometrically well-defined, whether it behaves correctly under transformation and measurement perturbation, whether it adds predictive value beyond another representation under dependency-aware validation, and whether that gain requires correct instance-level alignment.

CLO-SKET is positioned at this intersection. It does not compete with large sketch-conditioned generative or retrieval systems on synthesis quality, nor does it propose Fourier analysis as a new mathematical technique. Instead, it treats repeated garment sketches as a measurement population and uses a compact second-harmonic representation to test a hierarchy of increasingly strong claims.

The study therefore moves through

\[
\boxed{
\text{measurement}
\rightarrow
\text{transformation validity}
\rightarrow
\text{incremental prediction}
\rightarrow
\text{partition reproducibility}
\rightarrow
\text{alignment dependence}
\rightarrow
\text{claim boundary}
}
\]

while keeping the garment identity as the unit of generalization.

The intended novelty is this integration. The representation is explicit enough to audit algebraically and geometrically; the evaluation is grouped enough to respect repeated sketches; and the alignment control is restrictive enough to distinguish category-conditioned predictive structure from garment-specific correspondence. This permits a narrower but stronger conclusion than a performance gain alone: the analysis can identify not only whether the added geometry is useful, but also the structural level at which the evidence supports that usefulness.

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

Experiment 06 tested whether the frozen compact axial–radial representation adds garment-category information beyond the frozen 135-D morphology representation. The seven prespecified feature sets were (R), (A), (R+A), (M), (M+R), (M+A), and (M+R+A), with dimensions 8, 6, 14, 135, 143, 141, and 149. The primary contrast was

\[
\Delta F_1=F_1^{\mathrm{macro}}(M+R+A)-F_1^{\mathrm{macro}}(M),
\]

with \(\Delta BA=BA(M+R+A)-BA(M)\) secondary. Radial-only and axial-only additions were mechanistic ablations and could not replace the primary contrast.

The experiment was confirmatory for the compact 14-D representation but not historically blind. Before its outcome was computed, frozen metadata had exposed a positive result for an earlier, broader 28-D radial–angular representation (macro-F1 increment +0.070984; balanced-accuracy increment +0.073043). This exposure was disclosed in the design lock. No compact-representation outcome had been computed when its features, primary contrast, estimator, validation unit, bootstrap count, repeated-partition count, or alignment-permutation count were frozen.

## 3.12 Locked estimator and grouped validation

Every feature set used training-fold `StandardScaler` followed by `LogisticRegression` with L2 penalty, \(C=1.0\), `solver=lbfgs`, `max_iter=5000`, `class_weight=None`, and `random_state=20260820`. No hyperparameter search or feature-set-specific classifier change was performed.

Five deterministic category-balanced folds were constructed over the 230 garment identities. Each fold held out exactly two complete identities from each of 23 categories (46 test identities; 184 train identities), with zero identity overlap. Every sketch appeared in exactly one test fold; test-fold sizes ranged from 459 to 461 sketches because identity block sizes varied slightly. Macro-F1 (primary) and balanced accuracy (secondary) were computed from pooled out-of-fold predictions.

## 3.13 Paired garment-identity bootstrap

Primary-effect uncertainty was estimated from paired frozen out-of-fold predictions using 5,000 complete-garment-identity bootstrap replicates (random state 20260820). Sampling an identity included all its sketches for both models.

The prespecified unrestricted bootstrap was retained in the audit trail. Because some replicates omitted an entire category, a category-stratified robustness analysis was added without model refitting or feature changes. It sampled 10 identities with replacement within each of the 23 categories, preserving every category in every replicate. Percentile 95% confidence intervals were the 2.5th and 97.5th percentiles of paired metric differences. Fraction-positive values were descriptive, not permutation probabilities.

## 3.14 Repeated grouped-partition stability

Ten complete repetitions of five-fold category-balanced grouped cross-validation used seeds 20260820 through 20260829. Within each repeat, every category again contributed exactly two identities to each test fold. The estimator, preprocessing, features, and outcomes remained fixed.

The repeated analysis evaluated (M), (M+R), and (M+R+A). For every repeat, pooled out-of-fold macro-F1 and balanced accuracy were computed and the full augmented-minus-morphology difference retained; the (M+R-M) macro-F1 difference was retained as radial-ablation stability. All 10 repeats and all 50 constituent folds were retained.

## 3.15 Category-preserving identity-alignment permutation

A separate control tested whether augmented-model utility required exact garment-level pairing. Complete (R+A) identity blocks were reassigned within garment category while also matching identity block size. Thus category composition and 9-, 10-, or 11-sketch repeated-measure structure were preserved while exact morphology–axial–radial correspondence was disrupted.

Dress, Harem, and Jumpsuit each contained singleton 9-sketch and 11-sketch category-by-size strata, so those six identities necessarily self-mapped. The audited null retained the same identity for 2.6087% of rows and misaligned 97.3913% in every permutation.

For each of 2,000 permutations, the same five frozen grouped folds, fold-local standardization, and locked logistic-regression specification were used to fit and evaluate (M+R+A_{\pi}). The null statistic was its performance increment over the frozen morphology baseline. The one-sided corrected empirical probability was

\[
p=\frac{1+\sum_{b=1}^{B}\mathbf 1[\Delta_b^{\mathrm{null}}\geq\Delta_{\mathrm{obs}}]}{B+1},
\qquad B=2000.
\]

The test was evaluated for macro-F1 and balanced accuracy. It asks whether **correct garment-level alignment is more useful than category-preserving misalignment**, not whether the axial–radial block has incremental predictive utility at all.

## 3.16 Claim hierarchy for Experiment 06

Standalone (R), (A), or (R+A) performance establishes discriminative information only. A positive (M+R+A-M) contrast with garment-identity bootstrap support and repeated-partition stability supports reproducible **incremental predictive utility**. The radial and axial ablations localize the directly observed increment but do not redefine the primary hypothesis. A stronger claim of **garment-specific correspondence** requires the correctly aligned effect to exceed the category-preserving, block-size-matched misalignment null.

Accordingly,

\[
\text{incremental utility}\not\Rightarrow\text{garment-specific correspondence}.
\]

Neither result establishes statistical independence, information-theoretic uniqueness, semantic understanding, or causality.

---

## 3.17 Garment-identity-disjoint shell-field reconstruction

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

The earlier representation/reconstruction validation lineage was executed with Python 3.12.13, NumPy 2.0.2, and scikit-learn 1.6.1; the separately frozen Experiment 06 confirmatory run used Python 3.13.15, NumPy 2.1.3, pandas 2.2.3, and scikit-learn 1.6.1 (Section 7, Software Environment).

---

## 3.18 Rotation and coordinate-frame controls

Two complementary rotation controls evaluated the dependence of reconstruction on the common image coordinate frame.

### 3.18.1 Analytic harmonic rotation

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
+
S_2\sin(2\phi),
\]

\[
S_2'
=
- C_2\sin(2\phi)
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

### 3.18.2 Global-rotation control

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

### 3.18.3 Garment-identity-randomized rotation

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

## 3.19 Parameter and discretization sensitivity

Sensitivity analyses evaluated dependence of the radial–angular representation on the fixed numerical choices used in the primary measurement specification. The primary configuration was not altered after these analyses.

### 3.19.1 Support threshold

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

### 3.19.2 Concentration half-width

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

### 3.19.3 Radial-domain sensitivity

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

### 3.19.4 Angular-resolution sensitivity

The canonical 72 angular bins were coarsened to

\[
36
\quad\text{and}\quad
24
\]

bins by exact aggregation of adjacent angular mass bins. No image interpolation was used.

For each resolution, \(F_2\), \(C_2\), \(S_2\), \(R_2\), axial orientation, peak magnitude, and peak radius were recomputed. The 72-bin field served as the reference.

### 3.19.5 Radial-resolution sensitivity

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

## 3.20 Low-order harmonic control

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

## 3.21 Phase-conditioning analysis

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

## 3.22 Garment-level association analysis

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

## 3.23 Garment-cluster bootstrap

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

## 3.24 Category-stratified permutation inference

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

## 3.25 Outcome-defined error bands and threshold sensitivity

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

## 3.26 Algebraically coupled calibration diagnostic

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

## 3.27 Scope of inference

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

Thus, the prospectively locked primary contrast was

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

These ablations indicate that radial organization carries most of the direct incremental signal in this classifier, while the axial block alone adds little to morphology. The fact that \(M+R+A\) exceeded \(M+R\) descriptively does not constitute a separately prospectively specified significance test for the axial contribution conditional on \(R\).

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

## 4.8 Measurement-field integrity and representation construction

For the retained 2,300-sketch cohort defined in Section 4.1, the conditional angular tensor had dimensions \(2300\times72\times72\), the full second-harmonic field had dimensions \(2300\times72\), and the primary radial analysis comprised 25 shells spanning the fixed shell-coordinate domain

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

## 4.9 Rigid-image rotation control of the 14-dimensional representation

A separate image-domain perturbation control evaluated whether the final 14-dimensional representation exhibited the intended transformation behavior when the raster sketch itself was rigidly rotated and the complete radial-angular measurement was recomputed.

All 2,300 sketches were evaluated at

\[
\phi
\in
\{-20^\circ,-10^\circ,-5^\circ,0^\circ,5^\circ,10^\circ,20^\circ\}.
\]

No garment labels were used and no predictive model was fitted.

### 4.9.1 Stability of the second-harmonic magnitude field

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

### 4.9.2 Axial orientation transformation consistency

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

### 4.9.3 Rotation-invariant directional scalars

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

## 4.10 Duplicate-image screening and provenance audit

All 2,300 file paths were unique. SHA-256 hashing detected no repeated raw files, and hashing of decoded pixel arrays detected no repeated decoded images. Perceptual-hash screening identified 11 candidate pairs at Hamming distance 0, 39 at distance at most 2, and 248 at distance at most 4. These candidates were treated as a screen for visual similarity rather than evidence of duplicated files or shared lineage.

Beyond the cohort summary in Section 4.1, the provenance audit showed that individual recovered garment identities contained 9–11 sketches and 9–11 distinct replicate identifiers, with eight identity–replicate combinations appearing more than once in the filename records. These irregularities did not alter the category-qualified recovery of 230 garment identities used throughout the study.

The available metadata do not establish that the recovered garment identities constitute mutually independent sampling units; population-level inference remains conditional on that assumption.

---

## 4.11 Validation-unit audit and sensitivity rationale

An initial image-level cross-validation design did not separate repeated sketches by garment identity: garment identities represented in each test fold were also represented in the corresponding training set. That design therefore evaluated unseen image files rather than unseen garments and was retained only as a sensitivity comparison.

The primary garment-identity-disjoint design summarized in Section 4.1 eliminated that leakage route. Test-fold sizes ranged from 459 to 461 sketches because the number of repeated sketches per garment identity varied slightly; every sketch and every recovered garment identity was held out exactly once, with zero train/test garment-identity overlap in all five folds.

---

## 4.12 Garment-identity-disjoint reconstruction of \(C_2\) and \(S_2\)

Two fixed `HistGradientBoostingRegressor` models reconstructed \(C_2\) and \(S_2\) independently from shell radius and observed second-harmonic magnitude,

\[
\mathbf z_{ij}
=
[r_j,R_{2,i}(r_j)].
\]

Across the five garment-identity-disjoint folds, \(C_2\) RMSE ranged from 0.210938 to 0.228147 and \(S_2\) RMSE ranged from 0.124814 to 0.131585 (Table 5). All 57,500 sketch-shell rows received exactly one out-of-fold prediction.

**Table 5. Garment-identity-disjoint fold performance for component reconstruction.**

| Fold | Training identities | Test identities | Identity overlap | \(C_2\) RMSE | \(S_2\) RMSE |
|---:|---:|---:|---:|---:|---:|
| 0 | 184 | 46 | 0 | 0.216957 | 0.124959 |
| 1 | 184 | 46 | 0 | 0.213426 | 0.124814 |
| 2 | 184 | 46 | 0 | 0.210938 | 0.127228 |
| 3 | 184 | 46 | 0 | 0.228147 | 0.128320 |
| 4 | 184 | 46 | 0 | 0.220904 | 0.131585 |

Across all held-out rows, the fold-local global baseline produced RMSEs of 0.300420 for \(C_2\) and 0.129034 for \(S_2\). A radius-only model produced RMSEs of 0.287288 and 0.128729, respectively. Adding \(R_2=|F_2|\) to radius reduced \(C_2\) RMSE to 0.218161, an absolute reduction of 0.069127 and a relative reduction of 24.06%. For \(S_2\), RMSE decreased to 0.127405, an absolute reduction of 0.001324 and a relative reduction of 1.03% (Table 6).

**Table 6. Comparator performance and incremental contribution of second-harmonic magnitude.**

| Model | \(C_2\) RMSE | \(S_2\) RMSE |
|---|---:|---:|
| Fold-local global baseline | 0.300420 | 0.129034 |
| Radius only | 0.287288 | 0.128729 |
| Radius + \(R_2\) | **0.218161** | **0.127405** |

The component-specific gains were strongly asymmetric. However, the rotation analysis in Section 4.15 shows that separate \(C_2\) and \(S_2\) errors are coordinate-dependent quantities and should not be interpreted as intrinsic differences between cosine-like and sine-like garment structure.

Because \(R_2\), \(C_2\), and \(S_2\) derive from the same conditional angular distribution, reconstruction remains a shared-source consistency diagnostic rather than recovery of an independent physical or semantic target.

---

## 4.13 Sensitivity to the validation unit

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

## 4.14 Garment-cluster uncertainty for reconstruction

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

## 4.15 Rotation and coordinate-frame control

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

### 4.15.1 Global rotation

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

### 4.15.2 Garment-identity-randomized rotation

A second control assigned a single random physical rotation to every sketch belonging to the same garment identity, independently across the 230 identities. Ten randomizations were performed. These perturbations preserved radius, observed \(R_2\), garment identity, repeated-sketch structure, and the original validation folds while removing the shared absolute image-axis orientation across identities.

Relative to the original upright data, mean performance across the ten randomized controls changed as follows:

**Table 7. Reconstruction under global and garment-identity-randomized rotations.**

| Condition | Vector RMSE | \(R_2\) RMSE | \(R_2\) Pearson | Peak \(R_2\) RMSE | Peak \(R_2\) Pearson | Median peak axial error |
|---|---:|---:|---:|---:|---:|---:|
| Original upright | 0.252639 | 0.145610 | 0.926390 | 0.148303 | 0.810543 | \(4.104^\circ\) |
| Global rotations, mean | 0.252597 | 0.145487 | 0.926655 | 0.148044 | 0.812051 | \(4.126^\circ\) |
| Identity-randomized rotations, mean | 0.390756 | 0.362143 | 0.713536 | 0.589963 | 0.557625 | \(44.675^\circ\) |

Under identity-randomized rotations, median axial error averaged \(44.675^\circ\), compared with \(45^\circ\) for unrelated axial orientations. Mean error was \(44.769^\circ\), compared with the same \(45^\circ\) chance expectation. The proportion with error at or below \(15^\circ\) was 0.1655, close to the chance value \(15/90=0.1667\), and the proportion above \(45^\circ\) was 0.4972, close to the chance value 0.5.

Thus, radius and second-harmonic magnitude do not intrinsically determine second-harmonic phase. The strong phase reconstruction observed in the upright dataset depends substantially on population-level orientation structure relative to the common image coordinate frame.

This result does not invalidate the radial–angular representation; rather, it identifies the coordinate information contributing to the reconstruction experiment.

---

## 4.16 Parameter and discretization sensitivity

Sensitivity analyses varied one construction choice at a time while preserving the primary representation and analysis.

### 4.16.1 Support threshold and concentration width

The primary support threshold was \(0.10\,m^\star\). Alternative thresholds of 0.05 and 0.15 left six of the eight radial descriptors exactly unchanged. Changes were confined primarily to onset and termination radii, which were exactly preserved for approximately 95–97% of sketches and remained within two shells for approximately 98–100%.

Changing the concentration half-width from the primary \(\pm4\) shell-coordinate units to \(\pm2\) or \(\pm6\) altered only the concentration coordinate by construction. The remaining seven radial descriptors were identical. Rank correlation of the concentration coordinate with its primary value remained 0.888 at half-width 2 and 0.949 at half-width 6.

### 4.16.2 Angular resolution

The canonical 72 angular bins were coarsened by exact mass aggregation to 36 and 24 bins, without image interpolation.

**Table 8. Sensitivity of the harmonic field to angular resolution.**

| Angular bins | \(R_2\) Spearman vs 72 | \(C_2\) Spearman | \(S_2\) Spearman | Median axial difference | Exact peak-radius agreement | Peak-magnitude Spearman |
|---:|---:|---:|---:|---:|---:|---:|
| 72 | 1.000000 | 1.000000 | 1.000000 | \(0.000^\circ\) | 1.000000 | 1.000000 |
| 36 | 0.999193 | 0.998844 | 0.971118 | \(2.530^\circ\) | 0.926522 | 0.998305 |
| 24 | 0.997051 | 0.995460 | 0.912654 | \(5.040^\circ\) | 0.862174 | 0.994252 |

Second-harmonic magnitude was therefore highly stable to substantial reductions in angular resolution. The larger changes in \(S_2\) than \(C_2\) were interpreted as coordinate-component effects rather than distinct physical signals.

### 4.16.3 Radial domain

The primary domain \(3.5\text{--}27.5\) contained endpoint peak locations for 22.04% of sketches. Specifically, 12.70% peaked at the lower endpoint and 9.35% at the upper endpoint.

The primary domain was compared with inward and outward alternatives extending from \(5.5\text{--}25.5\) through \(0.5\text{--}30.5\). Global radial summaries remained more stable than localized quantities. Relative to the primary domain, rank correlations at the widest tested domain \(0.5\text{--}30.5\) were 0.955 for integrated magnitude, 0.883 for radial centroid, and 0.786 for radial spread, whereas peak radius decreased to 0.511, concentration to 0.476, and onset radius to 0.471.

Among the 215 sketches whose primary peak occurred at the upper boundary \(r=27.5\), expansion to \(r=30.5\) caused 40.93% to move to a larger radius. Only 38.14% remained at 27.5 under the widest tested expansion.

Accordingly, peak radius is a window-dependent localization statistic. The endpoint occupancy and outward migration indicate partial boundary censoring, particularly for upper-boundary peaks.

### 4.16.4 Radial resolution

Radial-resolution sensitivity was assessed after exact mass aggregation from 72 to 36 and 24 radial bins. To isolate resolution from domain mismatch, all three resolutions were compared over the same normalized physical interval, \(1/12\le r_{\mathrm{norm}}\le1/3\).

**Table 9. Radial-resolution rank stability on an exact common physical domain.**

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

## 4.17 Low-order harmonic spectrum and justification of \(m=2\)

The primary second harmonic was evaluated against the neighbouring low-order harmonics \(m=1,3,4\), all derived from the same canonical 72-bin conditional angular field.

For an angular rotation by \(\pi\),

\[
F_m(\theta+\pi)
=
(-1)^m F_m(\theta).
\]

Odd harmonics therefore change sign under a \(180^\circ\) reversal, whereas even harmonics remain invariant. The observed fields reproduced this transformation numerically to better than \(5\times10^{-16}\).

The second harmonic is thus the lowest non-zero harmonic compatible with the axial orientation convention used by the representation. The empirical spectrum was examined as a consistency control rather than as a post-hoc selection criterion.

**Table 10. Low-order harmonic magnitude on the primary radial domain.**

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

## 4.18 Garment-level associations and phase conditioning

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

**Table 11. Garment-level monotonic associations (\(n=230\) garment identities).**

| Quantity | Spearman \(\rho\) | 95% cluster-bootstrap CI | Raw permutation \(p\) | Holm \(p\) |
|---|---:|---:|---:|---:|
| Median observed peak-shell \(R_2\) vs median axial error | −0.355875 | [−0.455749, −0.248336] | 0.000100 | 0.000200 |
| Median selected peak radius vs median axial error | −0.207675 | [−0.322472, −0.095626] | 0.030097 | 0.030097 |

At the sketch level, the corresponding descriptive Spearman correlations were −0.253366 for observed peak-shell \(R_2\) and −0.271404 for selected peak radius. No inferential probabilities were assigned to these pooled-sketch associations.

### 4.18.1 Conditioning of axial phase

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

**Table 12. Garment-level phase-conditioning associations.**

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

## 4.19 Outcome-defined error bands and threshold sensitivity

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

The same direction persisted across all four tested threshold pairs (Table 13). Median \(R_2\) differences ranged from 0.059442 to 0.072677, and Cliff's \(\delta\) ranged from 0.236987 to 0.300349. All garment-cluster bootstrap intervals remained above zero.

**Table 13. Threshold sensitivity of the descriptive low/high peak-\(R_2\) contrast.**

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

## 4.20 Algebraically coupled calibration diagnostic

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

The central result of this study is that a compact, explicitly defined axial–radial representation contributes reproducible garment-category information beyond the frozen morphology representation under garment-identity-disjoint validation. Morphology alone achieved macro-F1 \(0.297788\), whereas morphology augmented by the complete 14-dimensional axial–radial block achieved \(0.335765\), giving the prospectively locked increment

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

The axial block should be interpreted differently. Its low standalone performance does not imply that axial geometry is meaningless. Peak and magnitude-weighted orientations are coordinate-frame-dependent equivariant quantities, and the rotation analyses show that the canonical upright frame contains strong population-level orientation structure. Moreover, \(M+R+A\) descriptively exceeded \(M+R\). However, Experiment 06 did not prospectively specify a separate conditional significance test of \(A\) given \(M+R\). We therefore do not claim an independently established axial increment beyond the radial block.

The ablation evidence supports a mechanistic description, not a hierarchy of universal feature importance: within this dataset, classifier, coordinate frame, and locked representation, radial second-harmonic organization accounts for most of the directly observed incremental category signal.

---

## 5.3 Why the alignment result matters scientifically

The alignment permutation distinguishes two forms of “complementarity” that are otherwise easy to conflate.

The first is **incremental predictive utility**: adding one representation to another improves out-of-fold prediction. Experiment 06 supports this statement. The second is **instance-specific complementarity**: the additional benefit depends on the axial–radial representation belonging to the same garment instance or identity as the morphology representation. The alignment experiment does not support this stronger statement.

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

These choices matter for interpretation of Experiment 06. The observed gain is not obtained by simply appending obvious algebraic duplicates of the morphology baseline. The 14 coordinates are explicit summaries of a separately constructed radial–angular field. At the same time, “separately constructed” does not mean statistically independent: both representations ultimately derive from the same sketch images. The study therefore claims incremental predictive utility under a specified model, not information-theoretic independence.

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

Fourth, it subjects the attractive interpretation of that gain to a stronger falsification control. Category-preserving identity-level misalignment does not reduce the increment sufficiently for correct alignment to appear exceptional. The contribution is therefore not a claim of uniquely paired garment-level complementarity. It is the narrower—and better supported—demonstration that a compact, geometrically interpretable axial–radial measurement contributes reproducible predictive structure beyond the tested morphology baseline, while the alignment control shows that this gain is compatible with category-conditioned structure that does not require exact garment-level pairing.

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

The alignment-permutation control places the strongest boundary on interpretation. Correctly aligned \(M+R+A\) did not outperform a category-preserving identity-level misalignment null unusually strongly: the empirical probabilities were \(p=0.762619\) for macro-F1 and \(p=0.729635\) for balanced accuracy. Consequently, the improvement over morphology cannot be attributed, on the present evidence, to exact garment-specific correspondence between the morphology and axial–radial representations. The supported claim is narrower: the compact axial–radial representation contains reproducible predictive structure that is useful alongside morphology and is **compatible with category-conditioned structure that does not require exact garment-level pairing**; the experiment does not demonstrate uniquely paired garment-level complementarity, statistical independence, or information-theoretic uniqueness.

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

The primary incremental-representation experiment is additionally frozen as **Experiment 06**. Its permanent evidence bundle contains the master checkpoint `CLO_SKET_EXPERIMENT06_FINAL_CHECKPOINT.pkl` (SHA256 `6e2c600c9cef37c3edcae18300793e37265ba866ee93d83c825aa1b5ad522018`), a final manifest, pooled primary results, ablation contrasts, the category-stratified identity bootstrap, all repeated grouped-CV summaries and fold results, the complete 2,000-permutation alignment null and summary, the evidence ledger, manuscript summary, claim lock, final decision, provenance hashes, and figure metadata. The bundle is the frozen source of record for Experiment 06 numerical claims.

The intended public computational lineage is source-code driven: the official CLO-SKET TIFF images are supplied to Notebook 01, and the downstream validation notebooks operate on the same Paper-I measurement lineage. Large historical runtime-memory pickle snapshots are not treated as the scientific source of record. Where historical checkpoint-loading cells remain for provenance, they should be interpreted as audit/recovery records unless the corresponding checkpoint is explicitly supplied.

Full-harmonic representation-selection, bandwise compression, and latent-geometry analyses belonging to Paper II are intentionally excluded from the Paper-I reproducibility package. The formal ownership boundary is documented in `P1_P2_CLAIM_FIREWALL.md`.

## Software Environment

Two frozen execution lineages support the reported analyses and are distinguished explicitly rather than collapsed into a single retrospective environment.

The earlier Paper-I validation shield recorded:

- Python 3.12.13;
- NumPy 2.0.2;
- pandas 2.2.3;
- scikit-learn 1.6.1;
- Linux x86_64 execution environment.

The permanently frozen Experiment 06 confirmatory run recorded:

- Python 3.13.15;
- NumPy 2.1.3;
- pandas 2.2.3;
- scikit-learn 1.6.1;
- random state 20260820.

The difference reflects separate frozen execution sessions; no claim is made that all analyses were executed under one software image.

The scientific notebooks additionally use SciPy, Matplotlib, Pillow (`PIL`), Joblib, and standard-library modules as declared in their import cells. Pillow is used for TIFF decoding and for the rigid-image rotation control. Because exact SciPy, Matplotlib, Pillow, and Joblib version strings were not written into the frozen validation-shield environment record, no retrospective version number is asserted for those packages here. Their imports and algorithmic roles are explicit in the notebooks, and the manuscript reports the fixed image-rotation operator and interpolation settings used in the rigid-image control.

The canonical source notebook supports a configurable dataset location through `CLO_SKET_DATA_ROOT`; its historical Colab path is only the default used during the reported execution.

## Randomness and Reproducibility Lock

Randomness is restricted to explicitly declared model, resampling, permutation, or rotation-control procedures. Deterministic geometric construction of the radial-angular field and the 14-dimensional descriptor does not depend on random initialization.

The manuscript-facing stochastic controls currently frozen in the public notebooks include:

- `HistGradientBoostingRegressor` reconstruction models with `random_state=42`;
- bootstrap diagnostics in the core notebook with `BOOTSTRAP_SEED=20260820` and `N_BOOT=5000` where those diagnostics are used;
- Experiment 06 paired garment-identity bootstrap and category-stratified robustness bootstrap with 5,000 replicates and random state `20260820`;
- Experiment 06 repeated grouped partitions with seeds `20260820, ..., 20260829`;
- Experiment 06 category-preserving, block-size-matched alignment control with 2,000 permutations and random state `20260820`;
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
