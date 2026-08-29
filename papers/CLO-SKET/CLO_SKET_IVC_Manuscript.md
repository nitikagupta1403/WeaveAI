# Garment Sketches: Axial–Radial Geometry and Identity-Aware Validation

**Nitika Gupta**

Independent Researcher, Hyderabad, Telangana, India

Corresponding author: Nitika Gupta, nitikashimla14@gmail.com

---

# Abstract

Garment sketches encode more than global outline shape: their foreground evidence is distributed across radial position and undirected orientation. We capture this structure with a compact 14-dimensional axial–radial representation derived from shell-conditioned second-harmonic magnitude and doubled-angle axial orientation.

We evaluate the representation on all 2,300 CLO-SKET sketches from 23 garment categories while treating the 230 recovered source garments—not individual image files—as the unit of validation. In the corrective annotation-controlled Experiment 06 analysis, a frozen 135-dimensional morphology representation achieved macro-F1 0.2714 and balanced accuracy 0.2730. Adding the frozen axial–radial representation increased performance to 0.3143 and 0.3157, corresponding to gains of +0.0428 and +0.0426. Category-stratified garment-identity bootstrap intervals excluded zero, and the macro-F1 increment remained positive across all 10 repeated grouped partitions.

Predictive improvement alone does not determine whether the added information is tied to the exact same garment instance. In 2,000 within-category identity-block permutations preserving category and block-size structure, the correctly aligned corrective increment was not exceptional (empirical \(p=0.723\) for macro-F1 and \(p=0.686\) for balanced accuracy). The evidence therefore supports reproducible incremental predictive utility beyond morphology, but not uniquely garment-specific complementarity.

A post-outcome audit of the frozen CLEAN image field identified two images containing exact target-category text. In a separately frozen sensitivity analysis excluding the two affected garment identities, the macro-F1 increment remained +0.0364; all 5,000 identity-bootstrap replicates and all 10 repeated grouped partitions remained positive. This sensitivity is descriptive post-outcome evidence and does not replace the corrective confirmatory result. A subsequent fresh Experiment-08 reproducibility audit also failed its prespecified raster harmonic-magnitude mechanical gate, so later Experiment-08 learned-feature comparisons remain post-outcome and exploratory.

The overall contribution is both representational and methodological: an explicit axial–radial description of garment-sketch geometry together with an identity-aware evaluation framework that separates predictive increment from instance-specific correspondence.

**Keywords:** garment sketches; axial–radial geometry; second harmonic; morphology; grouped cross-validation; identity-aware validation

---

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

---

# 2. Related Work

## 2.1 From garment sketches to explicit geometry

Garment sketches already serve as computational representations in a wide range of fashion tasks. Sparse drawings have been mapped to garment meshes, sewing-pattern parameters, and simulation variables [2,3], while stylized fashion sketches have also been used to transfer garment shape and fold structure to virtual characters [4]. Sketch-conditioned systems now span clothing-image generation and synthesis [5–9], sewing-pattern reconstruction [10], and sketch-based retrieval and benchmarking [11,12]. Together, these studies show that a sketch contains information that can support sophisticated downstream inference.

Our interest begins one step earlier: **what geometric organization is present in the sketch itself?**

Explicit shape descriptions provide a natural language for this question. Fourier descriptors and geometric morphometrics have long represented periodic outlines, curves, and shape variation numerically [13–15], including applications to fashion-flat classification [16]. Related fashion work has also treated silhouette geometry as an object of explicit classification [17] and used geometric relationships for garment-pattern construction [18]. These approaches motivate representing shape through quantities whose geometric meaning remains visible rather than only through downstream prediction.

The axial–radial representation developed here follows this tradition but changes the object being summarized. Rather than applying a harmonic descriptor only to an external contour, we condition foreground sketch evidence on radial distance from the centroid and examine its angular organization within each shell. The resulting description therefore asks not only **what direction is present**, but also **where in the sketch that directional organization occurs**.

## 2.2 Axial organization as a circular-geometry problem

Directional structure in a garment sketch is naturally axial. An undirected orientation at angle \(\theta\) is equivalent to one at \(\theta+\pi\), so the geometry is periodic over \(180^\circ\) rather than \(360^\circ\). This doubled-angle treatment is standard for axial data in circular statistics [19]. The second circular harmonic is the lowest non-zero Fourier order that respects this equivalence.

Within a radial shell, its magnitude \(R_2(r)\) describes the strength of second-harmonic directional organization, while its half-phase \(\alpha_2(r)\) describes the corresponding undirected axis. Doubled-angle coordinates \((\cos 2\alpha,\sin 2\alpha)\) then provide a continuous Euclidean representation of axial orientation without treating opposite directions as distinct.

This explicit construction also makes the expected behavior of the representation inspectable. Under rigid image rotation, harmonic magnitude and axial phase have different transformation roles; localized radial summaries can depend on discretization; and phase becomes unstable when directional organization is weak. Rotation, reconstruction, discretization, harmonic-order, and phase-conditioning analyses therefore serve as geometric diagnostics of the representation itself. They answer a different question from classification performance: whether the measured quantities behave in ways consistent with their intended interpretation.

## 2.3 From predictive increment to garment-level correspondence

A second issue arises from the structure of the observations rather than from the descriptor. CLO-SKET contains repeated sketches associated with recovered source-garment identities. Different drawings of the same garment are related observations, so an image-level train/test split can place evidence from one garment on both sides of the validation boundary.

Grouped evaluation addresses this dependency by treating the complete garment identity as the indivisible unit of train/test separation. The same principle extends naturally to uncertainty estimation and repeated validation: if the scientific unit is the garment, resampling and repartitioning should operate at the garment level rather than at the individual image level.

There is also a subtler issue when two representations are combined. If axial–radial features improve prediction when appended to morphology, the result shows that the added representation carries useful information under the tested protocol. It does not yet tell us whether that information must come from the **exact same garment**.

We therefore distinguish predictive increment from garment-level correspondence. Complete axial–radial identity blocks can be reassigned within garment category while preserving category membership and repeated-observation structure. This retains category-conditioned information while deliberately breaking exact morphology–axial–radial pairing. The comparison asks whether correct garment-level alignment contributes information beyond what remains after this controlled misalignment.

Together, these strands motivate the evaluation framework used in the remainder of the paper: explicit axial–radial measurement, garment-identity-aware prediction, and a separate test of exact garment-level correspondence.

---

# 3. Methods

## 3.1 Study design and scope

The study addressed two linked questions: **how can garment-sketch directional organization be represented explicitly, and does that representation add predictive information beyond morphology when complete source garments are withheld?**

Foreground sketch evidence was summarized relative to the sketch centroid using radial shells and shell-conditioned angular distributions. Their second circular harmonic provided a radial magnitude field and an undirected axial-orientation field, which were reduced to a 14-dimensional axial–radial representation (RA14): eight radial descriptors and six axial descriptors.

Predictive contribution was evaluated by comparing a frozen 135-dimensional morphology representation with the same representation augmented by RA14. All corrective primary comparisons used category-balanced, garment-identity-disjoint folds and the same fixed classifier. Historical radial-only and axial-only analyses are retained as descriptive provenance and were not rerun under the corrective CLEAN design; they therefore do not localize the corrected increment. A separate category-preserving identity-block permutation tested whether any predictive increment depended on exact garment-level correspondence.

Representation diagnostics examined transformation behavior, discretization, reconstruction, harmonic order, and phase conditioning. These characterize the measurement itself and are distinct from the Experiment-06 predictive contrast. Detailed diagnostic procedures are given in the Supplementary Methods.

---

## 3.2 Dataset and garment-identity reconstruction

All 2,300 CLO-SKET images from 23 garment categories were analyzed. Category-qualified source identifiers encoded in filenames were used to reconstruct 230 source-garment identities, exactly 10 per category. Individual identities contained 9–11 repeated sketches because of irregular filename records.

File-path, raw-file SHA-256, and decoded-pixel checks found no exact duplicate images. Perceptual hashing was used only to identify visually similar candidates and was not treated as evidence of duplication.

Recovered garment identity was the indivisible unit for train/test separation, resampling, and permutation. Inference therefore concerns the 230 recovered garment identities rather than 2,300 independent sketches.

---

## 3.3 Raw-image radial–angular construction

The representation was computed directly from the native grayscale TIFF images. No thresholding, binarization, resizing, straightening, rotation, or principal-axis alignment was applied.

For sketch \(i\), pixel darkness was

\[
w_{ip}=\max(255-I_{ip},0).
\]

Pixel position was expressed in an aspect-ratio-preserving isotropic coordinate system using the common scale

\[
S_i=\max(W_i,H_i),
\]

followed by subtraction of the darkness-weighted centroid. Centroid-relative Euclidean radius was normalized by the maximum foreground radius within each sketch,

\[
\rho_{ip}=\frac{R_{ip}}{R_{i,\max}}, \qquad 0\leq \rho_{ip}\leq 1.
\]

Normalized radius and polar angle were discretized into 72 radial and 72 angular bins. Radial-bin centres were reported in shell-coordinate units,

\[
r_j=j+\frac12,\qquad j=0,\ldots,71,
\]

and angular bins covered \([-\pi,\pi]\) at \(5^\circ\) resolution.

Let \(H_i(r_j,\theta_k)\) denote accumulated darkness mass in radial shell \(r_j\) and angular bin \(\theta_k\). For nonempty shells, the conditional angular distribution was

\[
p_i(\theta_k\mid r_j)
=
\frac{H_i(r_j,\theta_k)}
{\sum_{\ell=1}^{72}H_i(r_j,\theta_\ell)}.
\]

Empty shells were represented by zeros. Conditioning within each shell separates angular organization from total foreground mass. Full coordinate definitions, bin-edge conventions, empty-shell guards, and the source-image support audit are provided in Supplementary Methods.

---

## 3.4 Angular harmonics and axial orientation

For harmonic order \(m\), the shell-conditioned complex angular moment was

\[
F_{m,i}(r_j)
=
\sum_{k=1}^{72}
p_i(\theta_k\mid r_j)
e^{-\mathrm{i}m\theta_k}.
\]

The primary representation used the second harmonic,

\[
F_{2,i}(r_j)
=
C_{2,i}(r_j)-\mathrm{i}S_{2,i}(r_j),
\]

with magnitude

\[
R_{2,i}(r_j)
=
|F_{2,i}(r_j)|
=
\sqrt{C_{2,i}(r_j)^2+S_{2,i}(r_j)^2},
\]

and axial orientation

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

Because orientation is axial,

\[
\alpha\equiv\alpha+\pi,
\]

and angular differences were evaluated on the folded interval \([0^\circ,90^\circ]\).

---

## 3.5 Why the second harmonic is primary

The choice \(m=2\) follows from axial symmetry rather than predictive model selection. Under a \(180^\circ\) reversal,

\[
e^{-\mathrm{i}m(\theta+\pi)}
=
(-1)^m e^{-\mathrm{i}m\theta}.
\]

Odd harmonics change sign whereas even harmonics are invariant; \(m=2\) is therefore the lowest non-zero harmonic compatible with \(\theta\equiv\theta+\pi\). Harmonics \(m=1,3,4\) were used only as descriptive controls and did not redefine the primary representation.

---

## 3.6 Primary radial domain and peak quantities

The shell coordinate \(r_j=j+\tfrac12\) is dimensionless and corresponds to the sketch-normalized radial coordinate \(\rho_j=(j+\tfrac12)/72\); it is not a physical pixel distance.

The primary representation used the fixed 25-shell radial domain

\[
\mathcal R=\{3.5,4.5,\ldots,27.5\}.
\]

Writing

\[
m_i(r)=R_{2,i}(r),
\]

the observed peak radius and magnitude were

\[
r_i^\star
=
\arg\max_{r\in\mathcal R}m_i(r),
\qquad
m_i^\star=m_i(r_i^\star).
\]

Because \(m_i(r)=R_{2,i}(r)=|F_{2,i}(r)|\), these are alternative notations for the same measured second-harmonic magnitude. Sensitivity of localized radial quantities to the finite radial domain was evaluated separately.

---

## 3.7 Eight radial-magnitude descriptors

The radial block summarizes how second-harmonic magnitude is distributed over \(\mathcal R\). It contains:

1. integrated magnitude;
2. magnitude-weighted radial centroid;
3. magnitude-weighted radial spread;
4. concentration within four shell-coordinate units of the observed peak;
5. support onset radius;
6. support termination radius;
7. peak radius; and
8. peak magnitude.

Support onset and termination used the fixed threshold

\[
\tau_i=0.10\,m_i^\star.
\]

The resulting vector was

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

Radial extent was excluded because it is exactly \(r_i^{\mathrm{off}}-r_i^{\mathrm{on}}\). Full integral and support definitions are reported in Supplementary Methods.

---

## 3.8 Six axial descriptors

The axial block summarizes dominant undirected orientation across radius. Peak axial orientation was

\[
\alpha_i^\star=\alpha_{2,i}(r_i^\star).
\]

A magnitude-weighted axial mean was obtained from the doubled-angle resultant

\[
Z_i
=
\sum_{r_j\in\mathcal R}
R_{2,i}(r_j)e^{\mathrm{i}2\alpha_{2,i}(r_j)},
\qquad
\bar\alpha_i
=
\frac12\arg(Z_i)
\pmod{\pi}.
\]

Axial coherence was

\[
\kappa_i
=
\frac{|Z_i|}
{\sum_{r_j\in\mathcal R}R_{2,i}(r_j)},
\]

and orientation drift was the folded axial distance between the orientations at the two boundaries of the primary radial domain.

Raw angles were not entered directly into the Euclidean feature vector. Peak and mean orientations were encoded using doubled-angle Cartesian coordinates,

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

This representation is invariant to \(\alpha\mapsto\alpha+\pi\).

---

## 3.9 Primary 14-dimensional representation

The final RA14 vector was

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

The full matrix therefore had dimensions \(2300\times14\). An independent reconstruction of the radial and axial blocks reproduced the stored representation exactly, with maximum absolute difference zero and no non-finite values.

---

## 3.10 Rigid-image rotation control of the 14-dimensional representation

A descriptive image-domain control evaluated the completed representation after rigid raster rotation and complete remeasurement. All 2,300 sketches were tested at Pillow rotation arguments

\[
\beta\in
\{-20^\circ,-10^\circ,-5^\circ,0^\circ,5^\circ,10^\circ,20^\circ\}.
\]

The measurement uses native image coordinates with pixel row increasing downward. Therefore the corresponding measurement-coordinate angular increment is

\[
\phi=-\beta.
\]

Images were embedded in a clipping-safe square white canvas and non-zero rotations used bilinear interpolation with fixed canvas size and white fill. No predictive model was fitted in this control.

Under the adopted negative-exponential convention, ideal second-harmonic rotation in measurement coordinates is

\[
F_2'(r)=e^{-\mathrm{i}2\phi}F_2(r),
\]

so that

\[
R_2'(r)=R_2(r),
\qquad
\alpha_2'(r)=\alpha_2(r)+\phi
\pmod{\pi}.
\]

Equivalently, when expressed in the raw Pillow argument \(\beta\),

\[
F_2'(r)=e^{+\mathrm{i}2\beta}F_2(r),
\qquad
\alpha_2'(r)=\alpha_2(r)-\beta
\pmod{\pi}.
\]

Radial-magnitude descriptors were assessed for approximate numerical invariance, doubled-angle orientation pairs for the expected axial equivariance, and axial coherence and orientation drift as rotation-invariant scalar summaries. This earlier raster control is descriptive and does not override the separately prospectively gated Experiment-08 mechanical audit. Additional implementation details are given in Supplementary Methods.

---

## 3.11 Corrective incremental representation-value experiment

Experiment 06 tested whether the frozen 14-dimensional RA14 representation added garment-category information beyond the frozen 135-dimensional morphology representation. The historical Experiment-06 package contained seven prespecified feature sets, but the corrective confirmatory reanalysis retained the primary comparison only: morphology \(M\) versus morphology augmented with the complete frozen RA14 block \(M+R+A\). Historical standalone and radial/axial ablation results remain provenance and are not used to redefine the corrected confirmatory claim.

The corrected primary contrast was

\[
\Delta F_1
=
F_1^{\mathrm{macro}}(M+R+A)
-
F_1^{\mathrm{macro}}(M),
\]

with balanced-accuracy change secondary.

The corrective analysis repaired the garment-identity map and applied a prospectively frozen annotation-control policy before corrected predictive outcomes were computed. Two measurement conditions were materialized using the same corrected row order, identity map, folds, representations, estimator, and analysis machinery: a RAW diagnostic condition and an annotation-controlled CLEAN condition. RAW is diagnostic only; the CLEAN condition governs the corrected confirmatory claim.

The estimator specification, corrected validation unit, bootstrap count, repeated-partition seed schedule, alignment-permutation count, annotation-control policy, and CLEAN feature matrices were frozen before the corrective predictive outcome was computed. The historical Experiment-06 result remains part of the provenance record but is superseded for the manuscript-facing primary claim by the corrected CLEAN analysis.

---

## 3.12 Locked estimator and corrected grouped validation

Both corrective feature sets used fold-local `StandardScaler` followed by L2-regularized logistic regression with \(C=1.0\), `solver=lbfgs`, `max_iter=5000`, `class_weight=None`, and `random_state=20260820`. No hyperparameter search, feature selection, calibration, or feature-set-specific classifier change was performed.

Five deterministic category-balanced folds were constructed over the corrected 230-garment identity map. Each fold held out two complete identities from each of the 23 categories, giving 46 test identities and 184 training identities per fold with zero train/test identity overlap. Corrected test-row counts were 459, 460, 461, 460, and 460 sketches. Macro-F1 was primary and balanced accuracy secondary, both computed from pooled out-of-fold predictions.

The frozen CLEAN feature matrices contained 2,300 rows in the same corrected row order as the identity/fold map. The morphology matrix had 135 columns and the RA14 matrix 14 columns; the augmented model therefore used 149 coordinates.

---

## 3.13 Paired corrected-identity bootstrap

Primary-effect uncertainty was estimated from the frozen CLEAN out-of-fold predictions using 5,000 paired, category-stratified corrected-garment-identity bootstrap replicates. Sampling an identity retained all of its sketches and retained paired predictions from both models.

Within each garment category, the 10 corrected garment identities were sampled with replacement. Percentile 95% intervals were defined by the 2.5th and 97.5th percentiles of the paired metric differences. The bootstrap is conditional on the frozen out-of-fold predictions and does not incorporate model-refitting uncertainty. Fraction-positive values are descriptive and are not permutation probabilities.

---

## 3.14 Repeated corrected grouped-partition stability

The CLEAN comparison was repeated across 10 category-balanced grouped five-fold partitions using the prospectively frozen seed schedule 20260820–20260829. Each seeded partition was generated over the corrected garment identities. The estimator, preprocessing, representations, labels, and outcomes remained fixed. Repeat-level pooled macro-F1 and balanced-accuracy increments were retained for \(M+R+A-M\).

This analysis is a robustness assessment of partition sensitivity and does not constitute a second confirmatory endpoint.

---

## 3.15 Category-preserving corrected-identity alignment permutation

A separate control tested whether augmented-model utility required exact garment-level morphology–RA14 pairing. Complete RA14 identity blocks were reassigned within garment category while matching identity block size, preserving category composition and repeated-measure structure while disrupting exact morphology–RA14 correspondence.

Under the corrected identity map, 20 of 2,300 rows necessarily self-mapped within singleton category-by-block-size strata; thus 0.8696% of rows self-mapped and 99.1304% were misaligned in every permutation.

For each of 2,000 permutations, the same corrected primary folds, preprocessing, morphology baseline, and classifier specification were used. The null statistic was the augmented-model increment over morphology. The corrected one-sided empirical probability was

\[
p
=
\frac{
1+\sum_{b=1}^{B}
\mathbf 1
[
\Delta_b^{\mathrm{null}}
\geq
\Delta_{\mathrm{obs}}
]
}{
B+1
},
\qquad
B=2000.
\]

The test asks whether **correct garment-level alignment is more useful than category-preserving misalignment**. It does not test whether RA14 has predictive value at all.

---

## 3.16 Claim hierarchy and post-outcome target-text sensitivity

The corrected Experiment-06 primary analysis separates incremental predictive utility from garment-specific correspondence. A positive \(M+R+A-M\) contrast with corrected-identity bootstrap support and repeated-partition stability supports reproducible **incremental predictive utility** beyond morphology.

A stronger **garment-specific correspondence** claim requires the correctly aligned effect to exceed the category-preserving, block-size-matched misalignment null. Therefore,

\[
\text{incremental utility}
\not\Rightarrow
\text{garment-specific correspondence}.
\]

After the corrective predictive outcome had already been computed, a separate audit inspected all 2,300 frozen CLEAN images for visible target-category text. Exactly two images contained text exactly matching the garment-category target, corresponding to corrected identities `Cardigan__G02` and `Tunic__G02`; no partial/abbreviated or ambiguous cases were identified.

Before any sensitivity outcome was computed, a separate post-outcome protocol was frozen specifying exclusion of exactly those two complete garment identities. The sensitivity reused the frozen CLEAN representation, estimator, retained primary fold assignments, metrics, bootstrap count, repeated-partition seed schedule, and alignment-permutation count, with only adaptations required by the reduced identity set. It is explicitly descriptive post-outcome sensitivity evidence and cannot create, replace, or strengthen the confirmatory claim.

Broader semantic or causal interpretations are outside the tested design.

---

## 3.17 Secondary conventional-image-descriptor baseline (Experiment 07)

Experiment 07 provided a secondary conventional-image-descriptor comparison that was frozen before its own outcomes were computed. It did not alter Experiment 06 or replace its primary claim.

The comparator was histogram of oriented gradients (HOG) [20]. Each native grayscale sketch was converted to an aspect-ratio-preserving 256×256 image by isotropic bilinear resizing and centered white padding. HOG used 9 orientations, 16×16-pixel cells, 2×2-cell blocks, L2-Hys normalization, and produced 8,100 features per sketch. No HOG hyperparameter search, PCA, feature selection, or augmentation was used.

The exact frozen 2,300×14 RA14 matrix, category labels, garment identities, row order, and Experiment-06 fold assignment were reused. Two feature sets were evaluated:

\[
\mathrm{HOG}_{8100}
\]

and

\[
\mathrm{HOG}_{8100}
\oplus
\mathbf z_{RA,14}.
\]

Both used the same fold-local standardization and locked logistic-regression specification as Experiment 06. The primary Experiment-07 contrast was pooled out-of-fold macro-F1 for HOG+RA14 minus HOG; balanced accuracy was secondary. Uncertainty was quantified by a paired bootstrap over the 230 garment identities using 5,000 replicates.

Experiment 07 is interpreted strictly as a secondary comparator: it tests whether RA14 adds measurable predictive benefit after a high-dimensional local-gradient representation is already present. It is not a new primary hypothesis and does not replace the morphology-based Experiment-06 comparison.

---

## 3.18 Fresh reproducibility audit: Experiment 08

After the frozen Experiment-06 and Experiment-07 analyses, Experiment 08 provided a fresh executable audit of RA14 under a prospectively frozen mechanical gate and a frozen DINOv2 ViT-S/14 comparison [21]. Two additional predictive controls were specified only after Experiment 08 had already entered a post-outcome exploratory phase and were committed before their own execution.

The mechanical gate determined whether subsequent predictive comparison could be interpreted confirmatorily. Analytic harmonic-rotation checks passed, and raster axial-angle errors satisfied their locked criteria. The raster harmonic-magnitude criterion did not: median relative magnitude error was 1.3132%, while the 95th percentile was 21.332%, exceeding the prespecified 15% threshold. The overall frozen mechanical gate therefore failed.

Predictive analyses were subsequently completed, but all Experiment-08 predictive results are interpreted as **post-outcome / exploratory**. The frozen DINOv2 comparison and the later correspondence and repeated-partition controls remain within that exploratory status and do not change the failed mechanical-gate result.

---

## 3.19 Representation diagnostics

A complementary diagnostic program examined the shell-level second-harmonic field through garment-identity-disjoint reconstruction, coordinate-frame perturbations, discretization sensitivity, low-order harmonic comparisons, and phase conditioning. These analyses characterize the measurement and are distinct from the prespecified Experiment-06 predictive contrast and the prospectively gated Experiment-08 audit.

Garment-identity-disjoint reconstruction estimated \(C_2(r)\) and \(S_2(r)\) from radius and observed \(R_2(r)\) using fixed regressors while withholding complete garment identities. Because predictors and targets derive from the same conditional angular field, this was interpreted as a shared-source consistency diagnostic rather than recovery of an independent physical target.

Coordinate-frame controls included global analytic rotation of the observed harmonic field and garment-identity-randomized rotations that preserved radius, \(R_2\), category, repeated-sketch structure, and validation folds while disrupting shared absolute orientation. These controls were used to distinguish coordinate-free magnitude behavior from phase information tied to the common image frame.

Sensitivity analyses varied fixed construction choices one at a time, including radial support threshold, concentration width, radial domain, angular resolution, and radial resolution. Coarsening was performed by exact aggregation of canonical mass fields rather than image interpolation. These analyses were not used to optimize the primary representation.

Low-order harmonics \(m\in\{1,2,3,4\}\) were compared descriptively to assess whether the second harmonic represented a substantial and non-redundant component of the observed angular field; this did not redefine the primary \(m=2\) choice.

Phase conditioning was examined from

\[
\alpha_2
=
\frac12\operatorname{atan2}(S_2,C_2),
\]

for which first-order perturbations scale inversely with harmonic magnitude. Garment-level association analyses therefore examined the relationship between reconstruction error, \(R_2\), and conditioning quantities after reducing repeated sketches to garment-identity medians.

Full estimator settings, parameter grids, validation-unit comparisons, permutation procedures, magnitude-stratified conditioning, outcome-defined error bands, and calibration diagnostics are reported in Supplementary Methods.

---

# 4. Results

## 4.1 Corrected study population and frozen representations

The corrective Experiment-06 analysis retained all 2,300 CLO-SKET sketches and used the corrected map of 230 garment identities, exactly 10 per category across 23 categories. Complete corrected garment identity was the indivisible unit for the primary train/test split, bootstrap, and alignment permutation.

The frozen morphology representation contained 135 coordinates and the frozen RA14 representation contained eight radial and six axial coordinates,

\[
\mathbf z_{RA}
=
\mathbf z_R\oplus\mathbf z_A
\in\mathbb R^{14}.
\]

The corrective feature matrices reproduced the locked representation definitions and passed the pre-outcome feature-hash checks. The corrected CLEAN confirmatory comparison evaluated \(M\) against \(M+R+A\); historical standalone and radial/axial ablation outcomes are retained as provenance but are not used as corrected confirmatory evidence.

The five corrected primary folds were category-balanced and garment-identity-disjoint. Each test fold contained 46 identities—two per category—with zero train/test identity overlap. Test-row counts were 459, 460, 461, 460, and 460.

---

## 4.2 Corrected CLEAN analysis supported incremental predictive utility

Under the frozen annotation-controlled CLEAN condition, morphology alone achieved macro-F1 0.271429 and balanced accuracy 0.273043. Adding the complete frozen RA14 representation increased performance to macro-F1 0.314256 and balanced accuracy 0.315652, giving the corrected prespecified contrasts

\[
\Delta_{RA}^{F_1}=+0.042827,
\qquad
\Delta_{RA}^{BA}=+0.042609.
\]

The historical raw-canvas Experiment-06 result is retained for provenance but does not govern the corrected manuscript claim.

**Table 1. Corrective CLEAN pooled out-of-fold category-discrimination performance.**

| Feature set | Dimensions | Macro-F1 | Balanced accuracy |
|---|---:|---:|---:|
| \(M\) | 135 | 0.271429 | 0.273043 |
| **\(M+R+A\)** | **149** | **0.314256** | **0.315652** |
| **Increment** | — | **+0.042827** | **+0.042609** |

The result supports incremental predictive utility under the corrected locked task; by itself it does not establish statistical independence or garment-specific complementarity.

---

## 4.3 Historical ablations do not define the corrected confirmatory interpretation

The earlier Experiment-06 package included standalone \(R\), \(A\), and \(R+A\) results and morphology-plus-radial and morphology-plus-axial ablations. Those values were generated under the historical raw-canvas/historical-map analysis and were not rerun as part of the corrected CLEAN confirmatory package.

Accordingly, the corrected manuscript does not use those historical ablations to claim that the present \(+0.042827\) macro-F1 increment is predominantly radial or independently axial. The confirmatory inference concerns the complete frozen RA14 block added to morphology. Historical ablations remain available as provenance and hypothesis-generating context only.

---

## 4.4 Corrected-identity bootstrap supported a positive increment

The category-stratified corrected-garment-identity bootstrap used 5,000 paired replicates. For macro-F1, the observed increment was +0.042827, the bootstrap mean was +0.042915, and the percentile 95% interval was [+0.025798, +0.060559]; all 5,000 replicates were positive.

For balanced accuracy, the observed increment was +0.042609, the bootstrap mean was +0.042782, and the percentile interval was [+0.025640, +0.060861]; again all 5,000 replicates were positive.

**Table 2. Category-stratified corrected-garment-identity bootstrap for the CLEAN primary contrast.**

| Metric | Observed \(\Delta\) | Bootstrap mean \(\Delta\) | 95% interval | Positive replicates |
|---|---:|---:|---:|---:|
| Macro-F1 | +0.042827 | +0.042915 | [+0.025798, +0.060559] | 5000 / 5000 |
| Balanced accuracy | +0.042609 | +0.042782 | [+0.025640, +0.060861] | 5000 / 5000 |

These intervals are paired uncertainty summaries conditional on the frozen out-of-fold predictions; they are not model-refitting confidence intervals. The fraction positive is descriptive and is not interpreted as a permutation probability.

---

## 4.5 The corrected increment remained positive across repeated grouped partitions

Across the 10 corrected category-balanced grouped five-fold partitions, the complete RA14 increment was positive in every repeat.

Macro-F1 increment had mean +0.027676, SD 0.006393, and range +0.020214 to +0.035910. Balanced-accuracy increment had mean +0.028174, SD 0.006883, and range +0.018696 to +0.038261.

**Table 3. Stability of the corrective CLEAN increment across repeated corrected-identity partitions.**

| Quantity | Mean | SD | Minimum | Maximum | Positive repeats |
|---|---:|---:|---:|---:|---:|
| \(\Delta_{RA}\), Macro-F1 | +0.027676 | 0.006393 | +0.020214 | +0.035910 | 10 / 10 |
| \(\Delta_{RA}\), balanced accuracy | +0.028174 | 0.006883 | +0.018696 | +0.038261 | 10 / 10 |

The positive corrected increment was therefore not confined to the primary deterministic partition.

---

## 4.6 Corrected alignment control did not support garment-specific correspondence

In 2,000 permutations, complete RA14 identity blocks were reassigned within category while matching block size. Twenty of 2,300 rows necessarily self-mapped, so 99.1304% of rows were misaligned in each permutation while category and block-size structure were preserved.

For macro-F1, the correctly aligned increment was +0.042827. The misalignment null had mean +0.047423, SD 0.007776, 2.5th percentile +0.032437, and 97.5th percentile +0.062726. The corrected one-sided empirical probability was \(p_{\mathrm{align}}=0.722639\).

Balanced accuracy gave the same conclusion: observed increment +0.042609, null mean +0.046240, SD 0.007801, 2.5th percentile +0.030870, 97.5th percentile +0.061315, and \(p_{\mathrm{align}}=0.685657\).

**Table 4. Corrective category-preserving garment-identity alignment control.**

| Metric | Observed \(\Delta\) | Null mean | Null SD | Null 2.5% | Null 97.5% | Empirical \(p\) |
|---|---:|---:|---:|---:|---:|---:|
| Macro-F1 | +0.042827 | +0.047423 | 0.007776 | +0.032437 | +0.062726 | 0.722639 |
| Balanced accuracy | +0.042609 | +0.046240 | 0.007801 | +0.030870 | +0.061315 | 0.685657 |

Correct alignment therefore did not produce an unusually large increment relative to category-preserving misalignment. The corrected Experiment-06 evidence supports reproducible incremental predictive utility but not the stronger claim of garment-specific morphology–RA14 complementarity.

### Post-outcome target-text sensitivity

The subsequent frozen review of all 2,300 CLEAN images identified exactly two images with visible text exactly matching the garment-category target: one in corrected identity `Cardigan__G02` and one in `Tunic__G02`. No partial/abbreviated or ambiguous target-text cases were identified.

A separately frozen post-outcome sensitivity analysis excluded exactly those two complete identities, removing 20 rows and retaining 2,280 sketches from 228 garment identities. The morphology-only macro-F1 was 0.279058 and morphology+RA14 macro-F1 was 0.315460, giving an increment of +0.036402; balanced accuracy increased from 0.280338 to 0.316329, giving +0.035990.

The sensitivity identity bootstrap remained positive in all 5,000 replicates. Its macro-F1 percentile interval was [+0.019588, +0.052819], and all 10 repeated grouped partitions retained positive pooled macro-F1 increments (mean +0.029800; range +0.022971 to +0.039338).

This represents persistence with modest attenuation relative to the frozen corrective primary increment. Because the sensitivity was specified only after the target-text audit and after the corrective primary outcome already existed, it is descriptive post-outcome evidence only and does not replace or create a confirmatory result.

---

## 4.7 Visualizing the axial–radial representation

Figure 1 illustrates the construction from centroid-relative foreground evidence to shell-conditioned \(p(\theta\mid r)\), second-harmonic magnitude \(R_2(r)\), and undirected orientation \(\alpha_2(r)\).

![](figures/Figure_1_Radial_Angular_Construction.png)

**Figure 1. Radial–angular construction and second-harmonic interpretation.** The upper schematic contrasts the first three angular harmonics and highlights the two-fold second harmonic used here for axial orientation, together with the definitions of \(F_m(r)\), \(R_2(r)\), and \(\alpha_2(r)\). (A) Representative CLO-SKET sketch with intensity-weighted centroid. (B) Centroid-relative polar geometry used to accumulate foreground intensity by radius and angle. (C) Conditional angular distribution \(p(\theta\mid r)\). (D) Second-harmonic magnitude \(R_2(r)=|F_2(r)|\); the shaded interval marks the 25-shell primary radial domain \(r=3.5,\ldots,27.5\), and the selected observed peak shell is marked. (E) Axial orientation \(\alpha_2(r)\) over the primary domain. The second harmonic represents axial orientation because \(\alpha\equiv\alpha+\pi\).

Eight radial and six axial descriptors form RA14, summarized in Figure 2.

![](figures/Figure_2_Provenance_Locked_14D_Representation.png)

**Figure 2. Fourteen-dimensional axial–radial representation (RA14).** The radial block comprises integrated second-harmonic magnitude, radial centroid, radial spread, radial concentration, onset radius, termination radius, peak radius, and peak magnitude. The axial block represents peak and magnitude-weighted mean orientations through doubled-angle cosine/sine coordinates together with axial coherence and orientation drift. Radial extent is excluded because it is exactly termination radius minus onset radius.

---

## 4.8 Geometric and numerical diagnostics

The representation was evaluated through image-domain, analytic, sensitivity, harmonic, reconstruction, and phase-conditioning controls distinct from the primary Experiment-06 predictive contrast.

Figure 3 summarizes the earlier rigid-raster rotation control over all 2,300 sketches from \(-20^\circ\) to \(+20^\circ\). The largest 95th-percentile transformation error was \(4.87^\circ\) for peak orientation and \(0.85^\circ\) for magnitude-weighted mean orientation. Radial-magnitude perturbations remained small in the median but increased toward larger rotations, consistent with interpolation and finite-bin effects.

![](figures/Figure_3_Rigid_Rotation_Control.png)

**Figure 3. Rigid-rotation control of the CLO-SKET axial–radial representation (RA14).** (A) The same canonical sketch under three raster-rotation conditions. The raw Pillow rotation argument is denoted \(\beta\), while the corresponding angular increment in the native image-coordinate measurement is \(\phi=-\beta\) (Methods, Section 3.10). (B) Stability of the primary-domain second-harmonic radial-magnitude profile relative to the \(0^\circ\) reference. (C) Peak and magnitude-weighted axial orientations follow the expected \(\Delta\alpha=\phi\) transformation when expressed in the measurement-coordinate convention. (D) Axial coherence remains numerically stable, while orientation drift shows small median changes with a wider upper-tail response. This earlier control is descriptive; the separately prospectively gated Experiment-08 mechanical audit is reported in Section 4.10.

Analytic global rotations left coordinate-free reconstruction metrics essentially unchanged: over \(0^\circ,22.5^\circ,45^\circ,67.5^\circ,\) and \(90^\circ\), vector RMSE varied by 0.000103 and median peak-shell axial error by \(0.0556^\circ\). At \(45^\circ\), \(C_2\) and \(S_2\) errors exchanged to numerical precision. In contrast, independent garment-identity rotations produced median axial reconstruction error \(44.675^\circ\), close to the \(45^\circ\) expectation for unrelated axial orientations. Thus radius and \(R_2\) do not determine phase independently of the common image frame.

Second-harmonic magnitude remained highly stable under angular coarsening to 36 and 24 bins (rank correlations 0.9992 and 0.9971). Global radial summaries were also comparatively stable, whereas localized quantities were more domain-sensitive: at the widest tested radial domain, rank correlations fell to 0.511 for peak radius, 0.476 for concentration, and 0.471 for onset radius.

The second harmonic was selected from axial symmetry before examining the empirical spectrum. In the subsequent control, \(m=2\) had the largest median integrated magnitude (7.8911) and peak magnitude (0.6604) among \(m=1,\ldots,4\). Its integrated magnitude correlated weakly with \(m=1\) (\(\rho=0.116\)) and \(m=3\) (\(\rho=0.185\)), and moderately with \(m=4\) (\(\rho=0.490\)).

Phase conditioning followed the expected inverse dependence on harmonic magnitude. Median peak \(R_2\) was negatively associated with axial reconstruction error (\(\rho=-0.356\)), while \(\|\Delta(C_2,S_2)\|/(2R_2)\) showed a stronger positive association (\(\rho=0.789\)). Weak harmonic magnitude therefore increases angular sensitivity but does not alone determine reconstruction error.

Full diagnostic results and uncertainty analyses are retained in the Supplementary Results.

---

## 4.9 HOG showed no clear incremental benefit from RA14

Under the same garment-identity-disjoint folds, HOG alone achieved macro-F1 0.648242 and balanced accuracy 0.650435. HOG+RA14 achieved 0.649135 and 0.651304, yielding pooled increments of +0.000894 and +0.000870.

Fold-level macro-F1 values were 0.637525, 0.661015, 0.615841, 0.660780, and 0.643949 for HOG and 0.637661, 0.656870, 0.621629, 0.663732, and 0.644240 for HOG+RA14; the small pooled positive contrast was therefore not uniformly positive across folds.

The paired 5,000-replicate garment-identity bootstrap gave macro-F1 mean contrast +0.000961 with 95% interval [−0.002152, +0.004342] and 72.82% positive replicates. Balanced accuracy gave mean +0.000912 with interval [−0.002238, +0.004272] and 71.10% positive replicates.

**Table 5. Secondary conventional HOG baseline under the authoritative Experiment 06 garment-identity folds.**

| Feature set | Dimensions | Macro-F1 | Balanced accuracy |
|---|---:|---:|---:|
| HOG | 8,100 | 0.648242 | 0.650435 |
| HOG + RA14 | 8,114 | 0.649135 | 0.651304 |

**Table 6. Paired garment-identity bootstrap for the HOG+RA14-minus-HOG contrast.**

| Metric | Observed \(\Delta\) | Bootstrap mean \(\Delta\) | 95% identity-level interval | Positive replicates |
|---|---:|---:|---:|---:|
| Macro-F1 | +0.000894 | +0.000961 | [−0.002152, +0.004342] | 3641 / 5000 |
| Balanced accuracy | +0.000870 | +0.000912 | [−0.002238, +0.004272] | 3555 / 5000 |

Both intervals included zero. Experiment 07 therefore provides no clear evidence that RA14 adds predictive benefit beyond HOG under the tested protocol. This does not contradict Experiment 06; it shows that RA14's incremental value is representation-dependent.

---

## 4.10 Experiment 08 narrowed the transformation-validity claim

Experiment 08 prospectively applied a separate mechanical gate to frozen RA14. Analytic harmonic-rotation and raster axial-angle criteria passed, but the raster harmonic-magnitude criterion failed: median relative magnitude error was 1.3132%, while the 95th percentile was 21.332%, exceeding the prespecified 15% threshold. The overall frozen mechanical gate therefore failed.

All subsequent Experiment-08 predictive results are **post-outcome / exploratory**. DINOv2 alone achieved macro-F1 0.738020 and DINOv2+RA14 0.738967, an exploratory increment of +0.000947; the category-stratified garment-identity bootstrap interval crossed zero.

The corrected compactness comparison gave paired difference −0.493309 with 95% bootstrap interval [−0.532260, −0.453164], and the prespecified non-inferiority criterion was false. Earlier compactness bootstrap intervals and non-inferiority inference from the multiplicity-destroying bootstrap implementation are superseded; the point-estimate workflow is not invalidated solely by that defect.

A later exploratory correspondence control used 1,000 within-category, block-size-preserving garment-identity permutations. The aligned +0.000947 increment was not unusually high under this distribution (upper-tail empirical \(p=0.999001\)); the control addresses garment-instance correspondence while preserving category-associated RA14 structure.

Across 20 additional garment-identity-grouped partitions, the exploratory increment had mean +0.003927, median +0.002581, minimum −0.005814, and maximum +0.014055. Seventeen repeats were positive and three negative. These summaries are descriptive: the effect was **small and partition-sensitive; three of 20 repeats were negative**.

Experiment-08 predictive evidence remains exploratory and does not alter the failed mechanical gate. The audit narrows the transformation-validity claim while leaving the separately frozen Experiment-06 evidence unchanged.

---

# 5. Discussion

## 5.1 Corrective Experiment 06 supports incremental utility beyond morphology

The manuscript-facing Experiment-06 result is the corrected annotation-controlled CLEAN analysis. Morphology alone achieved macro-F1 \(0.271429\), whereas morphology+RA14 achieved \(0.314256\), giving

\[
\Delta F_1=+0.042827,
\]

with balanced-accuracy increment \(+0.042609\). Category-stratified corrected-garment-identity bootstrap intervals excluded zero, and the increment remained positive across all 10 corrected repeated grouped partitions.

This identifies a specific and bounded role for RA14: the complete frozen 14-dimensional representation contributes reproducible category-discriminative information beyond the frozen morphology representation under corrected garment-identity-disjoint evaluation. It does not imply statistical independence of the two representations, because both are derived from the same underlying images.

A post-outcome target-text audit identified two affected CLEAN images. Excluding their two complete garment identities reduced the macro-F1 increment from \(+0.042827\) to \(+0.036402\), while all 5,000 sensitivity bootstrap replicates and all 10 repeated grouped partitions remained positive. We therefore interpret the sensitivity as persistence with modest attenuation, not as evidence that the two target-text cases account for the existence of the corrected incremental effect. Because this analysis was specified after outcome exposure, it remains descriptive post-outcome evidence.

## 5.2 The corrected analysis does not localize the increment to radial or axial sub-blocks

The historical Experiment-06 package contained radial-only, axial-only, and combined ablations. Those analyses were generated under the historical raw-canvas and historical identity-map configuration and were not rerun under the corrected CLEAN confirmatory design.

Consequently, the corrected manuscript does not use the historical ablations to claim that the current \(+0.042827\) increment is predominantly radial or to establish an independent axial contribution. The supported confirmatory claim concerns the complete frozen RA14 block. Historical ablations may motivate future decomposition studies, but they do not define the inferential interpretation of the corrected result.

This distinction is important because repairing the identity map and annotation-controlled measurement field changes the confirmatory analysis population and preprocessing context. A component-level claim would require a separately locked corrected analysis rather than inheritance from superseded historical values.

## 5.3 The HOG comparator remains secondary and representation-dependent

Experiment 07 provides a secondary conventional-image-descriptor comparison. HOG alone achieved macro-F1 \(0.648242\), and HOG+RA14 achieved \(0.649135\); the paired garment-identity bootstrap interval crossed zero.

Experiment 07 was frozen under its own historical Experiment-06-derived fold provenance before the later corrective Experiment-06 identity-map repair. It is therefore retained as a secondary external baseline rather than treated as a same-fold rerun of the corrected CLEAN primary analysis.

The qualitative conclusion remains narrow: RA14 should not be interpreted as a universal accuracy booster. A clear increment is supported relative to the corrected morphology baseline, whereas no clear additional benefit was established beyond the tested high-dimensional HOG descriptor under Experiment 07's frozen protocol.

## 5.4 Predictive increment and garment-specific correspondence remain different questions

The corrected alignment experiment tested a stronger claim than predictive improvement. The CLEAN primary analysis established that correctly aligned morphology+RA14 outperformed morphology alone. The restricted permutation then asked whether correct garment-level pairing performed unusually well relative to category-preserving, block-size-matched RA14 reassignment.

It did not. Corrected empirical alignment probabilities were \(p=0.722639\) for macro-F1 and \(p=0.685657\) for balanced accuracy.

Thus the corrected predictive increment is reproducible, but the evidence does not localize it to exact garment-level morphology–RA14 correspondence. Category-conditioned RA14 structure remains compatible with the observed predictive gain even after exact correspondence is largely disrupted.

This distinction is methodologically important: feature concatenation, incremental predictive utility, and instance-specific complementarity are not equivalent claims.

## 5.5 The second harmonic gives the representation a direct geometric meaning

For each radial shell,

\[
F_2(r)
=
\sum_k p(\theta_k\mid r)e^{-i2\theta_k}
=
R_2(r)e^{-i2\alpha_2(r)}.
\]

Its magnitude \(R_2(r)\) measures the strength of second-order angular organization, while \(\alpha_2(r)\) gives undirected axial orientation modulo \(\pi\).

The choice \(m=2\) follows from axial symmetry rather than classification performance: it is the lowest non-zero Fourier order compatible with \(180^\circ\) equivalence. The later low-order spectrum was consistent with that choice but did not determine it.

This geometric interpretation should not be overextended semantically. RA14 does not identify sleeves, collars, waistlines, flare, or other garment parts. Likewise, algebraic relationships are not independent confirmations: \(R_2=\sqrt{C_2^2+S_2^2}\) is definitional, and radial extent was excluded because it is exactly termination radius minus onset radius.

## 5.6 Transformation behaviour separates intrinsic structure from coordinate-frame structure

Using the measurement-coordinate increment \(\phi\), with \(\phi=-\beta\) for raw Pillow raster angle \(\beta\),

\[
F_2'(r)=e^{-i2\phi}F_2(r),
\qquad
R_2'(r)=R_2(r),
\qquad
\alpha_2'=\alpha_2+\phi\pmod{\pi}.
\]

The earlier rigid-image rotation control was broadly consistent with the expected axial transformation over the tested perturbations, while radial-magnitude profiles showed modest raster-level deviations.

Analytic controls further separated coordinate-free structure from common-frame orientation. Global rotations left reconstruction behaviour essentially unchanged, whereas independent garment-identity rotations increased median peak-shell axial reconstruction error from \(4.104^\circ\) to \(44.675^\circ\), close to the \(45^\circ\) expectation for unrelated axial orientations. Radius and \(R_2\) therefore do not intrinsically determine phase; much of the observed phase regularity depends on the upright population frame.

Experiment 08 narrows this claim further. Its prospectively frozen raster harmonic-magnitude P95 criterion failed even though analytic rotation and raster axial-angle subchecks passed. The earlier rotation results remain descriptive controls, not confirmatory mechanical validation.

## 5.7 Broad radial summaries are more stable than localized coordinates

Sensitivity analyses revealed a hierarchy within the radial descriptors. Integrated magnitude, radial centroid, and radial spread were comparatively stable under changes in radial domain and discretization, whereas peak radius, support boundaries, and concentration were more sensitive to analysis choices.

Approximately 22% of sketches selected a peak at a boundary of the primary radial domain, and 40.9% of sketches peaking at the upper boundary moved outward when the domain was expanded. Peak radius is therefore best interpreted relative to the locked measurement window rather than as an intrinsic physical scale.

RA14 should consequently be treated as a fixed measurement specification: predictive usefulness under that specification does not imply equal numerical portability of every coordinate.

## 5.8 Harmonic magnitude explains part of axial uncertainty

For

\[
\alpha_2
=
\frac12\operatorname{atan2}(S_2,C_2),
\]

first-order perturbation gives the bound

\[
|d\alpha_2|
\le
\frac{\sqrt{dC_2^2+dS_2^2}}{2R_2}.
\]

Smaller harmonic magnitude therefore makes axial phase less well conditioned for a fixed Cartesian perturbation.

The garment-level results follow this geometry. Median peak \(R_2\) was negatively associated with axial error (\(\rho=-0.356\)), while Cartesian reconstruction-error magnitude had a stronger association (\(\rho=+0.760\)). Their combined conditioning quantity was stronger still (\(\rho=+0.789\)). The interpretation is geometric rather than causal: harmonic strength conditions angular sensitivity, but the actual Cartesian perturbation also matters.

## 5.9 Scope, contribution, and next steps

The effective experimental population is the 230 recovered garment identities. Identity-disjoint validation therefore tests transfer to unseen recovered garments within CLO-SKET, not external generalization to another dataset or design population.

Several boundaries remain. Garment identities were reconstructed rather than supplied through an independent lineage table, so higher-level dependencies cannot be excluded. Morphology and RA14 derive from the same images. The common upright frame carries orientation structure. Localized radial descriptors are domain-sensitive. The second harmonic is a targeted axial summary rather than a complete angular representation. No garment-part annotations or independent physical measurements are available.

Within these limits, the contribution is both representational and methodological. Representationally, RA14 provides an explicit 14-dimensional description of radial second-harmonic organization and axial orientation. Methodologically, the evaluation distinguishes whether the representation carries category information, whether it adds predictive value beyond another representation, and whether that added value depends on exact garment-level correspondence.

Experiment 06 supports incremental value beyond morphology. Experiment 07 shows that this value is baseline-dependent. The alignment control does not support garment-specific correspondence. Experiment 08 narrows the mechanical transformation-validity claim without altering the frozen Experiment-06 result.

The next step is external validation: independent garment-sketch collections with explicit garment, designer, and collection identifiers; orientation-normalized or rotation-equivariant variants; and prospective semantic annotation would test how far the present geometric findings generalize.

---

# 6. Conclusion

Garment sketches contain structured directional information that is not captured by outline morphology alone. We represent that structure with a compact 14-dimensional axial–radial description built from the second angular harmonic: eight coordinates summarize where and how strongly second-harmonic organization occurs radially, and six axial-safe coordinates describe its undirected orientation. The construction follows directly from the geometry of axial direction, for which \(\theta\equiv\theta+\pi\).

In the corrective annotation-controlled Experiment-06 analysis, evaluated with complete corrected garment identities withheld from training, morphology alone achieved macro-F1 \(0.271429\) and balanced accuracy \(0.273043\). Adding the complete frozen RA14 representation increased these values to \(0.314256\) and \(0.315652\), corresponding to increments of \(+0.042827\) and \(+0.042609\). Category-stratified corrected-garment-identity bootstrap intervals excluded zero, and the increment remained positive across all 10 corrected repeated grouped partitions.

A post-outcome audit subsequently identified two CLEAN images containing text that exactly matched their garment-category targets. A separately frozen sensitivity analysis excluded the two affected garment identities and retained 228 identities and 2,280 sketches. The macro-F1 increment remained \(+0.036402\), with all 5,000 identity-bootstrap replicates and all 10 repeated grouped partitions positive. This sensitivity shows persistence with modest attenuation but remains descriptive post-outcome evidence; it does not replace the frozen corrective primary result.

The corrected alignment experiment further limits interpretation. Correctly aligned morphology and RA14 did not outperform the category-preserving, block-size-matched misalignment null unusually strongly (\(p=0.722639\) for macro-F1; \(p=0.685657\) for balanced accuracy). The supported claim is therefore reproducible **incremental predictive utility beyond morphology**, not uniquely garment-specific morphology–RA14 correspondence. Historical radial and axial ablations were not rerun under the corrective CLEAN design and consequently do not establish which RA14 sub-block accounts for the corrected increment.

Experiment 07 remains a separately frozen secondary conventional-descriptor comparison and provides no clear evidence of incremental benefit when RA14 is appended to HOG under that experiment's historical frozen protocol. Experiment 08 further narrows the representation-validity claim: its prospectively frozen raster harmonic-magnitude mechanical gate failed, and subsequent Experiment-08 predictive analyses remain explicitly post-outcome and exploratory.

The contribution is therefore both representational and methodological. The study provides an explicit axial–radial measurement of sparse garment sketches together with an identity-aware evaluation framework that separates **representation**, **incremental predictive utility**, and **instance-specific correspondence**, while preserving the distinct inferential status of corrective, sensitivity, secondary, and exploratory evidence.

---

# Declarations

## Funding

No specific funding supported this research.

## Competing interests

The author declares no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Author contributions (CRediT)

Nitika Gupta: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Data curation, Visualization, Writing – original draft, Writing – review & editing.

## Acknowledgements

The author thanks the creators and maintainers of the publicly available CLO-SKET dataset.

## Ethics statement

This study analyzed a publicly available garment-sketch dataset and involved no human participants, animals, identifiable personal data, or intervention. Ethics approval and informed consent were therefore not applicable.

## Declaration of generative AI and AI-assisted technologies in the writing process

During preparation of this work, the author used ChatGPT and OpenAI Codex to assist with language editing, manuscript organization, and code and documentation review. The author reviewed and edited all resulting material and takes full responsibility for the content of the publication.

## Data and code availability

The image data analyzed in this study are from the publicly available CLO-SKET dataset released through Mendeley Data (Version 1; doi:10.17632/jt533nkhsf.1). The original images are not redistributed in this repository and should be obtained from the official dataset record.

Code, manuscript-supporting materials, and reviewer-facing numerical evidence are available in the public WeaveAI repository at https://github.com/nitikagupta1403/WeaveAI under `papers/CLO-SKET/`. Historical Experiment-06 and Experiment-07 evidence is retained for provenance. The manuscript-facing corrective Experiment-06 workflow is separately deposited under `Codes_paper_I/Experiment_06_Corrective/`, with its corrected identity/fold artifacts, annotation-control records, frozen outcomes, target-text audit, and separately frozen post-outcome target-text sensitivity under `evidence/Experiment_06_Corrective/`.

Experiment 07 remains a frozen secondary conventional-descriptor comparator under its historical Experiment-06-derived fold provenance. Experiment-08 executable materials are maintained separately under `Codes_paper_I/Experiment_08/`, with its evidence chronology recorded in `docs/experiment-08/EXPERIMENT08_EVIDENCE_PROVENANCE_MANIFEST.md`. Experiment 08 failed its frozen mechanical gate; all subsequent Experiment-08 predictive results remain explicitly post-outcome / exploratory.

The public evidence is intended for numerical audit, provenance verification, and reproduction of explicitly executable corrective workflows rather than as a self-contained replacement for the original dataset or every historical computational intermediate. The historical Experiment-06 runtime checkpoint and the 2,300 × 8,100 Experiment-07 HOG feature matrix are intentionally not redistributed through Git. The absence of that historical Experiment-06 checkpoint does not affect the executable status of the later corrective Experiment-06 pathway. `PUBLIC_EVIDENCE_MANIFEST.json` records the older public Experiment-06/07 evidence bundle; the corrective Experiment-06 evidence is additionally deposited under `evidence/Experiment_06_Corrective/`, and Experiment-08 evidence is maintained separately under `evidence/Experiment_08/`. No private image dataset or unpublished manual annotation is required for the reported analyses.

---

# References

[1] Arnia, F., 2020. Clo-Sket. Mendeley Data, Version 1. https://doi.org/10.17632/jt533nkhsf.1.

[2] Yasseen, Z., Nasri, A.H., Boukaram, W., Volino, P., Magnenat-Thalmann, N., 2013. Sketch-based garment design with quad meshes. *Computer-Aided Design* 45(2), 562–567. https://doi.org/10.1016/j.cad.2012.10.041.

[3] Wang, T.Y., Ceylan, D., Popović, J., Mitra, N.J., 2018. Learning a shared shape space for multimodal garment design. *ACM Transactions on Graphics* 37(6), 203:1–203:13. https://doi.org/10.1145/3272127.3275074.

[4] Fondevilla, A., Rohmer, D., Hahmann, S., Bousseau, A., Cani, M.-P., 2021. Fashion transfer: Dressing 3D characters from stylized fashion sketches. *Computer Graphics Forum* 40(6), 466–483. https://doi.org/10.1111/cgf.14390.

[5] Cao, X.-L., Lu, F.-N., Zhu, X., Weng, L.-B., Lu, S.-F., Gao, F., 2023. Sketch-based compatible clothing image generation. *Journal of Zhejiang University (Engineering Science)* 57(5), 939–947. https://doi.org/10.3785/j.issn.1008-973X.2023.05.010.

[6] Liang, X., Mo, H., Gao, C., 2023. Controllable garment image synthesis integrated with frequency domain features. *Computer Graphics Forum* 42(7), e14938. https://doi.org/10.1111/cgf.14938.

[7] Zhang, Y., Zhang, T., Xie, H., 2024. TexControl: Sketch-based two-stage fashion image generation using diffusion model. In: *Proceedings of the 2024 NICOGRAPH International (NICOInt)*, pp. 64–68. https://doi.org/10.1109/NICOInt62634.2024.00021.

[8] Singh, A.K., Patras, I., 2024. FashionSD-X: Multimodal fashion garment synthesis using latent diffusion. arXiv:2404.18591. https://doi.org/10.48550/arXiv.2404.18591.

[9] Baldrati, A., Morelli, D., Cartella, G., Cornia, M., Bertini, M., Cucchiara, R., 2023. Multimodal garment designer: Human-centric latent diffusion models for fashion image editing. In: *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)*, pp. 23393–23402. https://doi.org/10.1109/ICCV51070.2023.02138.

[10] Huang, D., Wang, Y., Qu, J., Wang, A., Tang, Y., 2025. SketchTailor: Lightweight sketch-driven modeling for high-fidelity garment pattern reconstruction. *Computers & Graphics* 131, 104345. https://doi.org/10.1016/j.cag.2025.104345.

[11] Bui, D.-D.-K., Pham, M.-T., Nguyen, T.V., Tran, M.-T., Le, T.-N., 2026. GarmentSketch: Large-scale sketch-to-fashion benchmark. arXiv:2606.14025. https://doi.org/10.48550/arXiv.2606.14025.

[12] Cao, H.-N., Bui, L.-H., Vo, D.-K., Tran, M.-T., Le, T.-N., 2026. VietFashion: Benchmarking sketch-text composed image retrieval for cultural outfits. arXiv:2606.13427. https://doi.org/10.48550/arXiv.2606.13427.

[13] Zahn, C.T., Roskies, R.Z., 1972. Fourier descriptors for plane closed curves. *IEEE Transactions on Computers* C-21(3), 269–281. https://doi.org/10.1109/TC.1972.5008949.

[14] Bookstein, F.L., 1997. Landmark methods for forms without landmarks: Morphometrics of group differences in outline shape. *Medical Image Analysis* 1(3), 225–243. https://doi.org/10.1016/S1361-8415(97)85012-8.

[15] McCane, B., 2013. Shape variation in outline shapes. *Systematic Biology* 62(1), 134–146. https://doi.org/10.1093/sysbio/sys080.

[16] An, L., Li, W., 2014. An integrated approach to fashion flat sketches classification. *International Journal of Clothing Science and Technology* 26(5), 346–366. https://doi.org/10.1108/IJCST-05-2013-0054.

[17] Tsuru, T., Sugahara, M., Nishimura, H., 2021. Silhouette classification of designer's collections in luxury fashion brands. *International Journal of Affective Engineering* 20(1), 33–40. https://doi.org/10.5057/ijae.IJAE-D-20-00002.

[18] Oh, J., Kim, S., 2026. Generation of body-fit garment patterns using a landmark matching algorithm. *Clothing and Textiles Research Journal* 44(1), 75–92. https://doi.org/10.1177/0887302X251340652.

[19] Jammalamadaka, S.R., SenGupta, A., 2001. *Topics in Circular Statistics*. World Scientific. https://doi.org/10.1142/4031.

[20] Dalal, N., Triggs, B., 2005. Histograms of oriented gradients for human detection. In: *Proceedings of the 2005 IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR)*, vol. 1, pp. 886–893. https://doi.org/10.1109/CVPR.2005.177.

[21] Oquab, M., Darcet, T., Moutakanni, T., Vo, H.V., Szafraniec, M., Khalidov, V., Fernandez, P., Haziza, D., Massa, F., El-Nouby, A., Assran, M., Ballas, N., Galuba, W., Howes, R., Huang, P.-Y., Li, S.-W., Misra, I., Rabbat, M., Sharma, V., Synnaeve, G., Xu, H., Jégou, H., Mairal, J., Labatut, P., Joulin, A., Bojanowski, P., 2024. DINOv2: Learning robust visual features without supervision. *Transactions on Machine Learning Research*.
