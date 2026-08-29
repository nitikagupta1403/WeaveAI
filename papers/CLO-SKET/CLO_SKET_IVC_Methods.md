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
