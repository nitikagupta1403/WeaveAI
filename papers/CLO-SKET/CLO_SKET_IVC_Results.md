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
