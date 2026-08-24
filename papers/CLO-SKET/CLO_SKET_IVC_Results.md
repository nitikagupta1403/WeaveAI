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

Thus, the prespecified and outcome-locked primary contrast was

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

These ablations indicate that radial organization carries most of the direct incremental signal in this classifier, while the axial block alone adds little to morphology. The fact that \(M+R+A\) exceeded \(M+R\) descriptively does not constitute a separately prespecified significance test for the axial contribution conditional on \(R\).

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

## 4.5 The incremental effect reproduced across repeated grouped partitions

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

## 4.8 Study population and primary representation

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

The resulting matrix had dimensions \(2300\times14\), contained only finite values, and exactly matched a separately recomputed \(8+6\) concatenation, with maximum absolute difference zero.

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

## 4.10 Duplicate-image screening and garment-identity structure

All 2,300 file paths were unique. SHA-256 hashing detected no repeated raw files, and hashing of decoded pixel arrays detected no repeated decoded images. Perceptual-hash screening identified 11 candidate pairs at Hamming distance 0, 39 at distance at most 2, and 248 at distance at most 4. These candidates were treated as a screen for visual similarity rather than evidence of duplicated files or shared lineage.

Filename and category structure recovered 230 category-qualified garment identities, exactly 10 identities within each of the 23 categories. Individual garment identities contained 9–11 sketches and 9–11 distinct replicate identifiers. Eight identity–replicate combinations appeared more than once in the filename records.

Recovered garment identity was therefore used as the clustering unit for validation, bootstrap resampling, and prespecified association analysis. The available metadata do not establish that the 230 recovered garment identities constitute mutually independent sampling units; population-level inference remains conditional on that assumption.

---

## 4.11 Garment-identity separation in validation

An initial image-level cross-validation design did not separate repeated sketches by garment identity: garment identities represented in each test fold were also represented in the corresponding training set. That design therefore evaluated unseen image files rather than unseen garments and was retained only as a sensitivity comparison.

The primary validation used five category-balanced, garment-identity-disjoint folds. Each test fold contained 46 complete garment identities—two identities from each of the 23 categories—and each training fold contained the remaining 184 identities. Test-fold sizes ranged from 459 to 461 sketches because the number of repeated sketches per garment identity varied slightly.

Every sketch and every recovered garment identity was held out exactly once. Train/test garment-identity overlap was zero in all five folds.

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

A separate post hoc shell-mass audit addressed the distinct question of whether the \(10^{-14}\) nonempty-shell guard admitted shells with negligible foreground support. Across all 57,500 sketch-shell observations in the 25-shell primary domain, the minimum shell-mass fraction was \(4.92\times10^{-4}\) of total sketch darkness mass (median \(2.06\times10^{-2}\)). For the selected \(R_2\)-peak shell, the minimum mass fraction was \(1.52\times10^{-3}\) (median \(2.07\times10^{-2}\)). No selected peak shell fell below \(10^{-3}\), and imposing an audit-only \(10^{-3}\) minimum shell-mass fraction left peak radius and peak magnitude unchanged for all 2,300 sketches. At \(2\times10^{-3}\), only 2/2,300 selected peak shells fell below the threshold; exact peak-radius agreement remained 0.999130 and peak-magnitude Spearman correlation was 0.999862. A stronger \(5\times10^{-3}\) threshold affected 187/2,300 selected peaks and reduced exact peak-radius agreement to 0.918696. Support-boundary quantities were more sensitive: the lower endpoint fell below \(10^{-3}\) in 81/2,300 sketches and below \(2\times10^{-3}\) in 304/2,300, whereas the upper endpoint never fell below any tested threshold through \(5\times10^{-3}\). These audit results support the numerical adequacy of the frozen nonempty-shell guard for peak selection in this dataset while reinforcing the more cautious interpretation of localized support-boundary descriptors. No feature definition or Experiment 06 result was changed by this audit.

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
