# CLO-SKET Paper 2 — Reconciled Results v1.0

## Status

**RESULTS RECONCILED WITH P2_13 v1.0: REPRESENTATION VALIDITY + EVIDENCE-CONTROLLED REPRESENTATION**

This Results section reports only frozen evidence. It preserves the original representation-selection, latent-model, and morphology-localization results while incorporating the later 05F–05K representation-validity audit without retroactively changing any historical selection decision.

---

# 4. Results

## 4.1 The historical raster-relative representation was sensitive to raster support

Before interpreting harmonic-dependent representation requirements, we examined whether the historical radial-angular coordinate system itself was sensitive to preprocessing changes that altered the observation frame. This audit was completed after the original band-wise representation-selection analysis had been frozen and did not alter the four harmonic bands, candidate radial families, coefficient budgets, inferential thresholds, frozen hybrid representation, or downstream latent-model decisions.

The audit proceeded from localization of the historical preprocessing effect to a controlled same-pixel support intervention.

### 4.1.1 Most of the historical high-band change entered with cropping rather than text removal or later resize/pad

The historical RAW-to-CLEAN transformation was decomposed into TEXT_ONLY, CROP_ONLY, LOCALIZE_ONLY, and CLEAN variants.

For the high harmonic band, the mean effect changes were:

\[
\Delta_{\mathrm{TEXT\_ONLY}-\mathrm{RAW}}
=
+0.0054165112,
\]

\[
\Delta_{\mathrm{CROP\_ONLY}-\mathrm{RAW}}
=
-0.0391425304,
\]

\[
\Delta_{\mathrm{LOCALIZE\_ONLY}-\mathrm{CROP\_ONLY}}
=
-0.0001572699,
\]

and

\[
\Delta_{\mathrm{CLEAN}-\mathrm{LOCALIZE\_ONLY}}
=
-0.0001045733.
\]

Thus text blanking alone did not reproduce the population-level high-band loss, whereas the major change entered with the crop-only transformation. The additional resize/pad stage contributed little further change in the high band.

The supported localization statement is therefore:

\[
\boxed{
\text{most of the historical high-band change entered with cropping/new raster support}
}
\]

rather than with subsequent bicubic resize/pad processing.

This result falsified the earlier working suspicion that bicubic resampling was the dominant source of the high-band collapse. It did not yet identify a causal explanation for the crop-only effect.

### 4.1.2 Crop-associated spectral change tracked raster-relative support geometry more strongly than centroid or border-gradient descriptors

The 05G audit verified exact equality of the retained garment rectangle between RAW and CROP_ONLY representations, zero centroid map-back error, and unchanged retained intensities.

Median descriptive changes included a crop-area fraction of approximately

\[
0.2559,
\]

foreground fraction increasing from approximately

\[
0.02293
\quad\text{to}\quad
0.09448,
\]

and radius/grid ratio changing from approximately

\[
0.92886
\quad\text{to}\quad
0.92238.
\]

Gradient concentration and border-gradient fraction also increased after cropping.

Among the tested candidate descriptors, the strongest surviving category-centered FDR associations were linked to changes in foreground radial scale relative to the raster grid. Representative associations were

\[
\rho
\left(
\Delta\text{foreground-radius/grid-radius},
\Delta\text{high fraction}
\right)
=
0.268988,
\]

with

\[
p=0.000200,
\qquad
q=0.002200,
\]

and

\[
\rho
\left(
\Delta\text{foreground-radius/grid-radius},
\Delta\log\text{high energy}
\right)
=
0.290318,
\]

with

\[
p=0.000100,
\qquad
q=0.001650.
\]

These results associated the historical spectral instability more strongly with raster-relative support geometry than with centroid displacement, interpolation, or border-gradient concentration alone. They remained associational and were not interpreted as proof of mechanism.

### 4.1.3 Population-level support change was associated with systematic spectral redistribution

The 05J population audit tested whether RAW-to-CROP changes in robust raster-relative support geometry covaried with changes in the four frozen angular-frequency band fractions.

Among the audited descriptors, the strongest population associations involved

\[
\Delta
\left(
\frac{r_{q99}}{R_{\mathrm{grid}}}
\right).
\]

The category-preserving permutation analysis yielded:

\[
\Delta\text{low}:
\qquad
\rho=-0.332738,
\]

\[
\Delta\text{mid}:
\qquad
\rho=-0.155208,
\]

\[
\Delta\text{high-mid}:
\qquad
\rho=+0.345008,
\]

\[
\Delta\text{high}:
\qquad
\rho=+0.257411.
\]

These associations survived the frozen BH-FDR procedure.

Stratification by the support-change descriptor showed the same directional pattern. Comparing the lowest and highest support-change quartiles, median changes were:

| Quantity | Q1 | Q4 |
|---|---:|---:|
| \(\Delta q_{99}/R_{\mathrm{grid}}\) | 0.062476 | 0.483714 |
| \(\Delta\) low | +0.012615 | -0.018741 |
| \(\Delta\) mid | -0.040995 | -0.053228 |
| \(\Delta\) high-mid | +0.005523 | +0.027711 |
| \(\Delta\) high | +0.013246 | +0.041898 |
| bandwise \(L_1\) | 0.127022 | 0.160238 |

All 23 garment-category medians showed positive high-band change descriptively under natural crop tightening.

The population pattern was therefore:

\[
\boxed{
\text{greater crop-induced raster-relative tightening}
\Rightarrow
\text{lower low/mid allocation and higher high-mid/high allocation}
}
\]

under the historical representation.

However, the largest absolute association was only moderate. The 05J result therefore establishes a population association, not a deterministic explanation:

\[
\boxed{
\text{association}\neq\text{causation}.
}
\]

### 4.1.4 Same-pixel support enlargement produced the predicted inverse spectral redistribution

The 05K intervention directly manipulated surrounding raster support while keeping the frozen garment rectangle unchanged. Seven support levels were used:

\[
s
\in
\{1.00,1.10,1.25,1.50,2.00,2.50,3.00\}.
\]

No garment resize, interpolation, antialiasing, contour retracing, crop recomputation, rethresholding, square forcing, or post-padding resizing was introduced.

The full primary experiment contained

\[
2300\times7=16100
\]

support conditions.

The \(s=1\) replay reproduced the baseline for

\[
2300/2300
\]

sketches, with maximum discrepancy approximately

\[
2.22\times10^{-16}.
\]

The matched object-relative construction remained invariant for

\[
\boxed{
16100/16100
}
\]

support conditions within numerical precision.

In contrast, the historical raster-relative representation showed graded population-level redistribution as support increased.

### Table 1. Population median band-fraction changes under support enlargement

| Support level \(s\) | Low | Mid | High-mid | High | Bandwise \(L_1\) |
|---:|---:|---:|---:|---:|---:|
| 1.00 | 0 | 0 | 0 | 0 | 0 |
| 1.10 | +0.014163 | +0.004217 | -0.008783 | -0.011837 | 0.045464 |
| 1.25 | +0.024044 | +0.004795 | -0.013892 | -0.020213 | 0.072890 |
| 1.50 | +0.031578 | +0.006666 | -0.017996 | -0.027958 | 0.099140 |
| 2.00 | +0.041836 | +0.011776 | -0.023574 | -0.038519 | 0.132808 |
| 2.50 | +0.051059 | +0.014783 | -0.029119 | -0.046172 | 0.157245 |
| 3.00 | +0.060047 | +0.016530 | -0.034858 | -0.052944 | 0.179920 |

The prespecified endpoint directions from \(s=1\) to \(s=3\) were therefore observed at population level:

\[
\boxed{
\Delta\text{low}>0
}
\]

\[
\boxed{
\Delta\text{high-mid}<0
}
\]

\[
\boxed{
\Delta\text{high}<0.
}
\]

At image level, endpoint concordance was:

\[
2104/2300
=
91.5\%
\]

for low,

\[
2059/2300
=
89.5\%
\]

for high-mid, and

\[
2008/2300
=
87.3\%
\]

for high.

All

\[
\boxed{
23/23
}
\]

category medians followed the predicted endpoint direction for low, high-mid, and high.

Full seven-level monotonicity was less universal:

\[
1171/2300
=
50.9\%
\]

for low,

\[
1015/2300
=
44.1\%
\]

for high-mid,

\[
869/2300
=
37.8\%
\]

for high, and

\[
1296/2300
=
56.3\%
\]

for bandwise \(L_1\).

Thus the support response was broad and category-consistent at the endpoint, but not a universal per-image monotonic law.

### 4.1.5 Exact category-level inference supported the prespecified endpoint directions

Primary inference compared \(s=3\) with \(s=1\) across the 23 garment categories using exact joint enumeration of all

\[
2^{23}
\]

category sign assignments and a studentized maximum-\(T\) statistic across the three directional endpoints.

For the low band, the median category effect was

\[
+0.052497,
\]

the mean category effect was

\[
+0.070816,
\]

and

\[
T=8.876063.
\]

The raw exact probability was

\[
1.192093\times10^{-7},
\]

with max-\(T\) family-wise-error-rate probability

\[
\boxed{
p_{\mathrm{FWER}}
=
1.430511\times10^{-6}.
}
\]

For the high-middle band, the median and mean category effects were

\[
-0.035074
\]

and

\[
-0.037901,
\]

with

\[
T=11.942573.
\]

The raw and max-\(T\) FWER probabilities reached the exact enumeration floor:

\[
\boxed{
1.192093\times10^{-7}.
}
\]

For the high band, the median and mean category effects were

\[
-0.046223
\]

and

\[
-0.053174,
\]

with

\[
T=15.210773.
\]

The raw and max-\(T\) FWER probabilities again reached

\[
\boxed{
1.192093\times10^{-7}.
}
\]

Taken together, the support audit establishes that:

\[
\boxed{
\text{raster support is a demonstrated dependency of angular spectral allocation}
}
\]

under the tested historical raster-relative representation.

The matched object-relative construction removes this tested same-pixel support dependency under the controlled intervention.

This result is deliberately narrower than a complete explanation of the natural RAW-to-CROP effect. The observational 05J association and the controlled 05K intervention converge on raster support as a genuine representation dependency, while additional contributors to natural preprocessing differences remain possible.

---

## 4.2 Radial representation requirements differed across angular harmonic scale

The original frozen representation-selection analysis asked whether the radial dependence of the Fourier morphology field could be represented uniformly across angular harmonic orders, or whether different harmonic ranges required different radial treatments. Candidate radial representations were evaluated separately within four prespecified harmonic bands under garment-identity-disjoint validation and family-wise-error-rate-controlled inference.

Importantly, this analysis preceded the later 05F–05K validity audit. The validity audit did not reopen or alter any of the following decisions.

For each band \(b\), the confirmatory statistic measured the category-balanced held-out garment-identity separation difference between the training-selected compressed representation and the complete radial representation,

\[
T_b
=
\operatorname{median}_{c}
\left[
\operatorname{median}_{g\in c}
\left(
S^{(\mathrm{selected})}_{g,b}
-
S^{(\mathrm{full})}_{g,b}
\right)
\right].
\]

We denote the observed value by

\[
\Delta=T_b.
\]

This confirmatory effect should not be interpreted as a held-out retrieval non-inferiority test. The \(Q_c\geq0.95\) criterion was used only inside each outer-training fold to define candidate eligibility; the confirmatory endpoint was the distinct held-out category-balanced separation statistic \(T_b\). Consequently, inferential support below means that the training-selected compact representation showed a positive held-out separation effect under the frozen design. It does not imply that discarded coefficients were noise or that compression is universally superior to the complete representation.

For the lowest harmonic band, \(k=1{:}4\), the training-selected four-coefficient DCT representation yielded

\[
\Delta=0.059306,
\]

with bootstrap 95% CI

\[
[0.023295,\;0.108196],
\]

and max-statistic FWER-adjusted probability

\[
\boxed{
p_{\mathrm{FWER}}
=
0.000200.
}
\]

The compact representation was therefore retained:

\[
\boxed{
k=1{:}4
\rightarrow
\mathrm{DCT}_4.
}
\]

For \(k=5{:}12\), the training-selected four-coefficient wavelet candidate produced

\[
\Delta=0.005984,
\qquad
95\%\ \mathrm{CI}
=
[-0.014164,\;0.060361],
\]

with

\[
p_{\mathrm{FWER}}
=
0.608939.
\]

For \(k=13{:}24\),

\[
\Delta=0.010959,
\qquad
95\%\ \mathrm{CI}
=
[-0.003088,\;0.073320],
\]

with

\[
p_{\mathrm{FWER}}
=
0.487751.
\]

Neither intermediate-band compression survived the prespecified inferential criterion. Complete 72-shell radial structure was therefore preserved:

\[
\boxed{
k=5{:}12
\rightarrow
\mathrm{RAW}_{72},
\qquad
k=13{:}24
\rightarrow
\mathrm{RAW}_{72}.
}
\]

At \(k=25{:}36\), the selected four-coefficient db4-wavelet representation again received inferential support:

\[
\Delta=0.039300,
\]

\[
95\%\ \mathrm{CI}
=
[0.019130,\;0.091021],
\]

and

\[
\boxed{
p_{\mathrm{FWER}}
=
0.019698.
}
\]

The retained representation was therefore

\[
\boxed{
k=25{:}36
\rightarrow
\mathrm{db4\ wavelet}_4.
}
\]

### Table 2. Confirmatory radial-representation decisions

| Harmonic band | Tested compressed representation | \(\Delta=T_b\) | Bootstrap 95% CI | \(p_{\mathrm{FWER}}\) | Retained representation |
|---|---|---:|---:|---:|---|
| \(k=1{:}4\) | DCT, \(B=4\) | 0.059306 | [0.023295, 0.108196] | 0.000200 | \(\mathrm{DCT}_4\) |
| \(k=5{:}12\) | Wavelet, \(B=4\) | 0.005984 | [-0.014164, 0.060361] | 0.608939 | \(\mathrm{RAW}_{72}\) |
| \(k=13{:}24\) | Wavelet, \(B=4\) | 0.010959 | [-0.003088, 0.073320] | 0.487751 | \(\mathrm{RAW}_{72}\) |
| \(k=25{:}36\) | db4 wavelet, \(B=4\) | 0.039300 | [0.019130, 0.091021] | 0.019698 | \(\mathrm{db4\ wavelet}_4\) |

The four decisions produced the heterogeneous radial-spectral representation

\[
\boxed{
\mathrm{DCT}_4/
\mathrm{RAW}_{72}/
\mathrm{RAW}_{72}/
\mathrm{db4}_4
}.
\]

The important result is not simply that some bands could be compressed. Rather, **support for radial compression was harmonic-dependent under the tested inferential framework**. Compact radial encodings were supported at \(k=1{:}4\) and \(k=25{:}36\), whereas the evidence was insufficient to replace complete radial structure at \(k=5{:}24\).

Failure to establish compression support is not interpreted as proof of intrinsic incompressibility; it determines only that compression was not justified by the present validation design.

---

## 4.3 Evidence-controlled selection produced a heterogeneous hybrid representation

The complete positive-harmonic morphology field contains

\[
36\times72
=
2592
\]

complex coefficients per sketch. Applying the four frozen representation decisions gave

\[
4\times4
=
16
\]

coefficients for \(k=1{:}4\),

\[
8\times72
=
576
\]

for \(k=5{:}12\),

\[
12\times72
=
864
\]

for \(k=13{:}24\), and

\[
12\times4
=
48
\]

for \(k=25{:}36\).

The resulting hybrid therefore contained

\[
16+576+864+48
=
\boxed{
1504
}
\]

complex coefficients per sketch, corresponding to a

\[
\boxed{
41.98\%
}
\]

reduction relative to the complete 2592-coefficient field and a compression ratio of

\[
\boxed{
1.7234\times.
}
\]

Exact block-wise real/imaginary packing produced a frozen

\[
\boxed{
3008\text{-dimensional}
}
\]

real representation.

This dimensional reduction follows from the original inferential decisions in Section 4.2; it was not obtained by selecting a global compression rate or by treating discarded coefficients as noise.

### 4.3.1 Occupancy and radial mass provided little additional identity-retrieval information

The positive-harmonic hybrid omits the conditional DC coefficient \(F_0(r)\). Because \(F_0(r)\) equals one on occupied shells and zero on empty shells, we first tested whether explicitly restoring the 72-dimensional occupied-shell indicator materially altered garment-identity retrieval.

Shell occupancy was nearly saturated:

\[
\boxed{
99.8569\%
}
\]

of the \(2300\times72\) sketch-shell locations were occupied. The mean number of occupied shells was

\[
71.897/72,
\]

and the median was

\[
72/72.
\]

Appending the occupancy indicator changed mean held-out MRR from

\[
0.816766
\]

for the frozen hybrid to

\[
0.816114,
\]

giving

\[
\boxed{
\Delta\mathrm{MRR}
=
-0.000651.
}
\]

Mean top-1 retrieval changed from

\[
0.633531
\]

to

\[
0.632229,
\]

giving

\[
\boxed{
\Delta\mathrm{Top1}
=
-0.001302.
}
\]

Across the five frozen folds, MRR improved in one fold, decreased in two, and was unchanged in two. At query level, 2,291 of 2,300 ranks were unchanged, three improved, and six worsened.

Radial ink mass \(M(r)\) was reconstructed deterministically from the original TIFFs using the frozen image-to-polar algorithm. The reconstruction reproduced the previously frozen occupancy mask exactly:

\[
\boxed{
0\ \text{mismatched shell cells across 2,300 sketches}.
}
\]

Appending the 72-dimensional radial-mass profile increased mean held-out MRR from

\[
0.816766
\]

to

\[
0.820252,
\]

giving

\[
\boxed{
\Delta\mathrm{MRR}
=
+0.003486,
}
\]

and mean top-1 retrieval from

\[
0.633531
\]

to

\[
0.640504,
\]

giving

\[
\boxed{
\Delta\mathrm{Top1}
=
+0.006973.
}
\]

Four of five folds showed positive MRR differences and one showed a decrease. At query level, 2,230 of 2,300 ranks were unchanged, 43 improved, and 27 worsened.

The effect is therefore reported descriptively as a small amount of complementary identity information carried by radial mass, not as an inferentially established improvement.

These sensitivities do not change the frozen primary representation.

### 4.3.2 The heterogeneous descriptor matched full radial retrieval closely and avoided larger losses from uniform compact transforms

The frozen hybrid contained 1504 complex coefficients (3008 real coordinates), whereas the complete \(\mathrm{RAW}_{72}\) field contained 2592 complex coefficients (5184 real coordinates). The dimension-matched uniform descriptors used 1512 complex coefficients (3024 real coordinates), only 0.532% more than the hybrid.

Mean held-out retrieval for the complete radial field was

\[
\mathrm{MRR}
=
0.819373,
\qquad
\mathrm{Top1}
=
0.638746.
\]

The frozen hybrid yielded

\[
\mathrm{MRR}
=
0.816766,
\qquad
\mathrm{Top1}
=
0.633531.
\]

Thus the complete \(\mathrm{RAW}_{72}\) field was descriptively higher by only

\[
\Delta\mathrm{MRR}
=
+0.002607
\]

and

\[
\Delta\mathrm{Top1}
=
+0.005215,
\]

while requiring 5184 rather than 3008 real coordinates.

The dimension-matched uniform raw descriptor was similarly close:

\[
\mathrm{MRR}
=
0.815896,
\qquad
\mathrm{Top1}
=
0.631792,
\]

corresponding to

\[
\Delta\mathrm{MRR}
=
-0.000870
\]

relative to the hybrid.

In contrast, applying one compact transform uniformly across all harmonics produced larger descriptive retrieval losses. Uniform DCT-42 yielded

\[
\mathrm{MRR}
=
0.783503,
\qquad
\mathrm{Top1}
=
0.567006,
\]

with

\[
\boxed{
\Delta\mathrm{MRR}
=
-0.033263
}
\]

relative to the hybrid.

Uniform db4-wavelet-42 yielded

\[
\mathrm{MRR}
=
0.789378,
\qquad
\mathrm{Top1}
=
0.578755,
\]

with

\[
\boxed{
\Delta\mathrm{MRR}
=
-0.027388.
}
\]

Both uniform compact-transform baselines had lower MRR than the hybrid in all five identity-disjoint folds.

### Table 3. Whole-representation descriptive sensitivity

| Representation | Complex coefficients | Real dimension | Mean MRR | Mean Top-1 | Mean \(\Delta\)MRR vs hybrid |
|---|---:|---:|---:|---:|---:|
| Full \(\mathrm{RAW}_{72}\) | 2592 | 5184 | 0.819373 | 0.638746 | +0.002607 |
| Frozen heterogeneous hybrid | 1504 | 3008 | 0.816766 | 0.633531 | 0 |
| Uniform \(\mathrm{RAW}_{42}\) | 1512 | 3024 | 0.815896 | 0.631792 | -0.000870 |
| Uniform db4-wavelet-42 | 1512 | 3024 | 0.789378 | 0.578755 | -0.027388 |
| Uniform DCT-42 | 1512 | 3024 | 0.783503 | 0.567006 | -0.033263 |

These comparisons are descriptive post-selection sensitivities rather than a new inferential family. They therefore do not establish population-level superiority of the hybrid over every alternative descriptor. Uniform \(\mathrm{RAW}_{42}\) remained a competitive simple baseline and is reported explicitly.

---

## 4.4 Nonlinear latent models did not earn a validated replacement of PCA

Conditional on the heterogeneous radial-spectral representation selected by the preceding full cross-validated band analysis, PCA, autoencoder (AE), and variational autoencoder (VAE) representations were compared at

\[
z\in
\{8,16,24,32,64\}
\]

using held-out garment-identity mean reciprocal rank across five identity-disjoint outer folds.

Ten prespecified same-dimensional nonlinear-versus-PCA contrasts were evaluated using exhaustive fold-level sign flips and a maximum statistic across the entire contrast family.

### Table 4. Nonlinear latent-model contrasts relative to same-dimensional PCA

| Contrast | Mean \(\Delta\)MRR | Median \(\Delta\)MRR | \(+\;/\;-\;/\;0\) folds | Raw one-sided \(p\) | Max-stat adjusted \(p\) |
|---|---:|---:|---:|---:|---:|
| AE8 − PCA8 | +0.009789 | +0.008696 | 5 / 0 / 0 | 0.03125 | 0.4375 |
| AE16 − PCA16 | +0.009778 | +0.007625 | 4 / 1 / 0 | 0.09375 | 0.4375 |
| AE24 − PCA24 | −0.006105 | −0.021739 | 2 / 3 / 0 | 0.81250 | 1.0000 |
| AE32 − PCA32 | −0.016968 | −0.011931 | 0 / 5 / 0 | 1.00000 | 1.0000 |
| AE64 − PCA64 | −0.016305 | −0.023913 | 1 / 4 / 0 | 0.93750 | 1.0000 |
| VAE8 − PCA8 | +0.007621 | +0.002169 | 3 / 0 / 2 | 0.12500 | 0.6875 |
| VAE16 − PCA16 | +0.014341 | +0.015251 | 4 / 1 / 0 | 0.06250 | 0.2500 |
| VAE24 − PCA24 | −0.001525 | +0.003261 | 3 / 2 / 0 | 0.65625 | 1.0000 |
| VAE32 − PCA32 | −0.011527 | −0.008696 | 1 / 4 / 0 | 0.96875 | 1.0000 |
| VAE64 − PCA64 | −0.018260 | −0.026087 | 0 / 4 / 1 | 1.00000 | 1.0000 |

The largest observed mean improvement was

\[
\boxed{
\mathrm{VAE}_{16}
-
\mathrm{PCA}_{16}
=
+0.014341\ \mathrm{MRR},
}
\]

but its selection-aware adjusted probability was

\[
\boxed{
p_{\mathrm{FWER}}
=
0.2500.
}
\]

None of the ten tested nonlinear contrasts survived multiplicity control. Conditional on the previously selected hybrid representation, PCA was therefore retained as the **practical latent baseline** for morphology interpretation.

This negative result is deliberately narrow. With five outer folds, the exhaustive paired analysis contains only

\[
2^5
=
32
\]

sign configurations, and the outer training portions overlap. The analysis does not prove population-level superiority of PCA and does not imply that all relationships in the representation are linear.

---

## 4.5 Detectable nonlinear pairwise structure did not imply nonlinear-model utility

To separate nonlinear predictive structure from model selection, the validated PCA representation was subsequently examined without reopening the PCA/AE/VAE decision.

The prespecified pairwise audit identified

\[
\boxed{
1
}
\]

FWER-supported quadratic PCA-coordinate relation. The strongest held-out improvement of the fixed quadratic predictor over the corresponding linear predictor was

\[
\boxed{
\overline{\Delta R^2}
=
+0.432042.
}
\]

This result establishes detectable pairwise nonlinear predictability within the retained PCA-coordinate description. It is not interpreted as differential-geometric manifold curvature, a unique nonlinear manifold, or evidence that a nonlinear encoder should replace PCA.

At the prespecified 20-neighbour scale, the identity-level median number of directions required to retain 90% of within-neighborhood variance was 15 (IQR 15–15). Because a centered 20-neighbour matrix has rank at most 19 by construction, this value is reported only as a scale-conditioned descriptive quantity. It is not compared with the global 90%-variance PCA dimension, and the previously reported local/global ratio remains retired from scientific interpretation.

Additional nonlinear embedding, principal-curve, and diffusion-map audits did not establish a stable nonlinear replacement representation.

The supported conclusion remains:

\[
\boxed{
\text{detectable nonlinear pairwise structure}
\not\Rightarrow
\text{validated nonlinear-model advantage}.
}
\]

---

## 4.6 Retained PCA axes mapped to heterogeneous radial-harmonic morphology

The first 64 PCA components accounted for

\[
\boxed{
44.65\%
}
\]

of variance in the standardized 3008-dimensional hybrid representation. All subsequent morphology localization is therefore conditional on this retained PCA-64 subspace.

Each PCA direction \(j\) was mapped through the exact frozen inverse representation to obtain

\[
\Delta F_j(r,k).
\]

Because PCA eigenvector signs are arbitrary, localization was quantified using the sign-invariant morphology-energy field

\[
E_j(r,k)
=
\left|
\Delta F_j(r,k)
\right|^2.
\]

PC1 was strongly outer-radial: 97.59% of its morphology energy occurred in shells 49–72, while 81.68% occurred across the combined intermediate harmonics \(k=5{:}24\). Its maximum-energy coordinate was

\[
(r,k)
=
(72,17).
\]

PC3 showed a similarly strong outer-radial pattern, with 96.47% of its energy in the outer region and 79.61% at \(k=5{:}24\), with maximum energy at

\[
(r,k)
=
(72,13).
\]

PC15 provided a contrasting morphology mode. Its energy was predominantly inner-radial:

\[
71.51\%
\]

occurred in shells 1–24, with maximum energy at

\[
(r,k)
=
(5,5).
\]

These examples establish heterogeneous radial-harmonic localization across retained PCA axes. They do not assign garment-part, causal, or semantic identities to individual PCs.

---

## 4.7 Retained morphology variation was concentrated in intermediate harmonics and outer radial structure

Aggregating morphology localization across all 64 retained components using their PCA explained-variance ratios as within-subspace weights yielded the following \(3\times4\) radial-region × harmonic-band distribution.

### Table 5. Variance-weighted radial-harmonic localization within the retained PCA-64 subspace

| Radial region | \(k=1{:}4\) | \(k=5{:}12\) | \(k=13{:}24\) | \(k=25{:}36\) |
|---|---:|---:|---:|---:|
| Inner, shells 1–24 | 2.29% | 9.57% | 7.21% | 1.59% |
| Middle, shells 25–48 | 2.04% | 5.47% | 4.98% | <0.01% |
| Outer, shells 49–72 | 8.60% | 24.13% | 27.17% | 6.94% |

Summed across radial zones,

\[
\boxed{
78.54\%
}
\]

of variance-weighted mapped morphology energy occurred at intermediate angular harmonics

\[
k=5{:}24.
\]

Summed across harmonic ranges,

\[
\boxed{
66.84\%
}
\]

occurred in the outer radial zone.

The joint outer-radial × intermediate-harmonic region contained

\[
\boxed{
51.30\%
}
\]

of the retained mapped morphology energy. The two largest individual cells were outer × \(k=13{:}24\),

\[
27.17\%,
\]

and outer × \(k=5{:}12\),

\[
24.13\%.
\]

These percentages have a strict denominator. They describe variance-weighted morphology localization within the retained PCA-64 subspace, which itself represents 44.65% of standardized representation variance. They are not percentages of total garment morphology, the full 3008-dimensional representation, semantic garment parts, or causal morphology factors.

---

## 4.8 Results synthesis

The combined evidence resolves two ordered representation questions.

First, the later representation-validity audit showed that the historical raster-relative coordinate system was not neutral to surrounding raster support. The natural RAW-to-CROP audit associated raster-relative tightening with redistribution away from lower angular bands and toward high-middle/high bands. The controlled 05K intervention then changed only surrounding support while holding garment pixels fixed and produced the predicted inverse endpoint redistribution. All 23 category medians followed the prespecified low/high-middle/high endpoint directions, the category-level effects survived exact joint max-\(T\) inference, and the matched object-relative construction remained invariant under the same intervention.

The supported validity conclusion is therefore:

\[
\boxed{
\text{raster support is a demonstrated dependency of the historical representation}
}
\]

under the tested same-pixel intervention.

This does not imply that support explains every natural RAW-to-CROP difference, nor that every image follows a monotonic support trajectory.

Second, the original frozen representation-selection analysis showed that radial structure did **not** receive uniform compression support across angular harmonic scale. Identity-disjoint, multiplicity-controlled validation produced

\[
\boxed{
\mathrm{DCT}_4/
\mathrm{RAW}_{72}/
\mathrm{RAW}_{72}/
\mathrm{db4}_4
},
\]

reducing the complete Fourier field from 2592 to 1504 complex coefficients while preserving full radial structure in harmonic ranges where compression was not supported.

Greater latent-model complexity also had to earn its place. Tested AE and VAE alternatives did not establish a multiplicity-controlled retrieval advantage over same-dimensional PCA, so PCA remained the practical latent baseline. A separate audit nevertheless detected nonlinear pairwise predictability, preserving the boundary that lack of validated nonlinear-model advantage is not evidence of globally linear geometry.

Finally, exact inverse mapping returned retained PCA variation to explicit radial-harmonic coordinates. Within the retained PCA-64 subspace, mapped morphology energy was concentrated predominantly in intermediate harmonic orders and outer radial structure, while individual components showed heterogeneous localization.

The overall empirical logic is therefore:

\[
\boxed{
\text{audit the measurement frame}
\rightarrow
\text{allocate representation complexity where evidence supports it}
\rightarrow
\text{validate latent complexity conservatively}
\rightarrow
\text{map retained variation back to explicit morphology coordinates}.
}
\]

The 05F–05K audit changes the hierarchy of interpretation, not the historical numerical selections.
