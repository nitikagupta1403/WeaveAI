# 4. Results

## 4.1 Study population and locked representations

All 2,300 CLO-SKET sketches were retained. Filename reconstruction yielded 230 garment identities, exactly 10 per category across 23 categories; each identity contained 9–11 repeated sketches and was treated as the indivisible validation and resampling unit.

The frozen morphology representation contained 135 coordinates. RA14 contained eight radial and six axial coordinates,

\[
\mathbf z_{RA}
=
\mathbf z_R\oplus\mathbf z_A
\in\mathbb R^{14},
\]

and reproduced the previously locked representation hash exactly. Seven feature sets entered Experiment 06 without outcome-dependent modification: \(R\), \(A\), \(R+A\), \(M\), \(M+R\), \(M+A\), and \(M+R+A\).

The five primary folds were category-balanced and garment-identity-disjoint. Each test fold contained 46 identities—two per category—with zero train/test identity overlap.

---

## 4.2 RA14 added predictive utility beyond morphology

Morphology alone achieved macro-F1 0.297788 and balanced accuracy 0.298261. RA14 alone achieved 0.219993 and 0.231304, respectively. Adding RA14 to morphology increased performance to macro-F1 0.335765 and balanced accuracy 0.336087, giving the prespecified contrasts

\[
\Delta_{RA}^{F_1}=+0.037977,
\qquad
\Delta_{RA}^{BA}=+0.037826.
\]

The macro-F1 increment was positive in all five primary folds, ranging from +0.011157 to +0.085268; balanced-accuracy differences were also positive in all five folds.

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

The result establishes incremental predictive utility under the locked task; by itself it does not establish statistical independence or garment-specific complementarity.

---

## 4.3 Mechanistic ablation localized most direct utility to the radial block

The radial block was more discriminative alone than the axial block: macro-F1 was 0.206831 for \(R\) and 0.081165 for \(A\), while \(R+A\) reached 0.219993.

When added to morphology, the macro-F1 increments were +0.026752 for \(R\) and +0.002299 for \(A\); balanced-accuracy increments were +0.026957 and +0.002174. The complete \(R+A\) block produced the larger macro-F1 increment of +0.037977.

Thus most directly observed incremental utility was associated with radial organization. Although \(M+R+A\) exceeded \(M+R\) descriptively, no separately prespecified significance test was defined for the axial contribution conditional on \(R\).

---

## 4.4 Identity-cluster uncertainty supported a positive increment

The category-stratified garment-identity bootstrap used 5,000 paired replicates. Mean macro-F1 increment was +0.037909 with percentile 95% interval [+0.020242, +0.055852]; all 5,000 replicates were positive. Balanced accuracy had mean increment +0.037968 with interval [+0.020000, +0.056239], again with no non-positive replicate.

The unrestricted identity-cluster audit gave closely similar intervals: [+0.019230, +0.055573] for macro-F1 and [+0.019221, +0.057648] for balanced accuracy. The category-stratified result is emphasized because unrestricted resampling could omit an entire category.

**Table 2. Category-stratified garment-identity bootstrap for the primary contrast.**

| Metric | Observed \(\Delta\) | Bootstrap mean \(\Delta\) | 95% CI | Positive replicates |
|---|---:|---:|---:|---:|
| Macro-F1 | +0.037977 | +0.037909 | [+0.020242, +0.055852] | 5000 / 5000 |
| Balanced accuracy | +0.037826 | +0.037968 | [+0.020000, +0.056239] | 5000 / 5000 |

The fraction positive is descriptive and is not interpreted as a permutation probability.

---

## 4.5 The increment reproduced across repeated grouped partitions

Across 10 category-balanced grouped five-fold partitions, the complete RA14 increment was positive in every repeat. Macro-F1 increment had mean +0.032253, SD 0.006805, and range +0.020620 to +0.043275. Balanced-accuracy increment had mean +0.031565, SD 0.007362, and range +0.019565 to +0.043913.

At the individual-fold level, 44 of 50 macro-F1 differences were positive and six were negative. The radial increment was positive in all 10 repeated partitions, with mean macro-F1 increment +0.028850.

**Table 3. Stability of the primary increment across repeated garment-identity partitions.**

| Quantity | Mean | SD | Minimum | Maximum | Positive repeats |
|---|---:|---:|---:|---:|---:|
| \(\Delta_{RA}\), Macro-F1 | +0.032253 | 0.006805 | +0.020620 | +0.043275 | 10 / 10 |
| \(\Delta_{RA}\), balanced accuracy | +0.031565 | 0.007362 | +0.019565 | +0.043913 | 10 / 10 |
| \(\Delta_R\), Macro-F1 | +0.028850 | — | — | — | 10 / 10 |

The positive increment was therefore not confined to the primary deterministic partition.

---

## 4.6 Category-preserving misalignment did not support garment-specific correspondence

In 2,000 permutations, complete RA14 identity blocks were reassigned within category while matching block size, breaking exact morphology–RA14 correspondence for 97.3913% of rows while retaining category-conditioned RA14 structure.

For macro-F1, the correctly aligned increment was +0.037977. The misalignment null had mean +0.042896, SD 0.007141, and 2.5th, median, and 97.5th percentiles +0.029088, +0.043094, and +0.056838. Of 2,000 null permutations, 1,525 equalled or exceeded the observed increment, giving \(p_{\mathrm{align}}=0.762619\).

Balanced accuracy gave the same conclusion: observed increment +0.037826, null mean +0.042258, and \(p_{\mathrm{align}}=0.729635\).

**Table 4. Category-preserving garment-identity alignment control.**

| Metric | Observed \(\Delta\) | Null mean | Null SD | Null 2.5% | Null 97.5% | Empirical \(p\) |
|---|---:|---:|---:|---:|---:|---:|
| Macro-F1 | +0.037977 | +0.042896 | 0.007141 | +0.029088 | +0.056838 | 0.762619 |
| Balanced accuracy | +0.037826 | +0.042258 | 0.007145 | +0.028261 | +0.056522 | 0.729635 |

Correct alignment therefore did not produce an unusually large increment relative to category-preserving misalignment. Experiment 06 supports reproducible incremental predictive utility but not the stronger claim of garment-specific morphology–RA14 complementarity. The null mean being slightly larger than the observed effect is not evidence that misalignment is intrinsically beneficial; the control only tests whether correct garment pairing is unusually useful.

---

## 4.7 Visualizing the axial–radial representation

Figure 1 illustrates the construction from centroid-relative foreground evidence to shell-conditioned \(p(\theta\mid r)\), second-harmonic magnitude \(R_2(r)\), and undirected orientation \(\alpha_2(r)\).

![Figure 1. Radial–angular construction and second-harmonic interpretation.](figures/Figure_1_Radial_Angular_Construction.png)

**Figure 1. Radial–angular construction and second-harmonic interpretation.** The upper schematic contrasts the first three angular harmonics and highlights the two-fold second harmonic used here for axial orientation, together with the definitions of \(F_m(r)\), \(R_2(r)\), and \(\alpha_2(r)\). (A) Representative CLO-SKET sketch with intensity-weighted centroid. (B) Centroid-relative polar geometry used to accumulate foreground intensity by radius and angle. (C) Conditional angular distribution \(p(\theta\mid r)\). (D) Second-harmonic magnitude \(R_2(r)=|F_2(r)|\); the shaded interval marks the 25-shell primary radial domain \(r=3.5,\ldots,27.5\), and the selected observed peak shell is marked. (E) Axial orientation \(\alpha_2(r)\) over the primary domain. The second harmonic represents axial orientation because \(\alpha\equiv\alpha+\pi\).

Eight radial and six axial descriptors form RA14, summarized in Figure 2.

![Figure 2. Fourteen-dimensional axial–radial representation (RA14).](figures/Figure_2_Provenance_Locked_14D_Representation.png)

**Figure 2. Fourteen-dimensional axial–radial representation (RA14).** The radial block comprises integrated second-harmonic magnitude, radial centroid, radial spread, radial concentration, onset radius, termination radius, peak radius, and peak magnitude. The axial block represents peak and magnitude-weighted mean orientations through doubled-angle cosine/sine coordinates together with axial coherence and orientation drift. Radial extent is excluded because it is exactly termination radius minus onset radius.

---

## 4.8 Geometric and numerical diagnostics

The representation was evaluated through image-domain, analytic, sensitivity, harmonic, reconstruction, and phase-conditioning controls distinct from the primary Experiment-06 predictive contrast.

Figure 3 summarizes the earlier rigid-raster rotation control over all 2,300 sketches from \(-20^\circ\) to \(+20^\circ\). The largest 95th-percentile transformation error was \(4.87^\circ\) for peak orientation and \(0.85^\circ\) for magnitude-weighted mean orientation. Radial-magnitude perturbations remained small in the median but increased toward larger rotations, consistent with interpolation and finite-bin effects.

![Figure 3. Rigid-rotation control of the CLO-SKET axial–radial representation (RA14).](figures/Figure_3_Rigid_Rotation_Control.png)

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
