# CLO-SKET Paper 2 — Final Results

## Status

**FINAL RESULTS ASSEMBLY: READY FOR MANUSCRIPT INTEGRATION**

This Results section reports only frozen evidence. It emphasizes the paper's central scientific contribution: harmonic-conditioned, evidence-controlled radial representation selection, followed by conservative latent-model validation and exact radial-harmonic morphology localization.

---

# 4. Results

## 4.1 Radial representation requirements differed across angular harmonic scale

The first question was whether the radial dependence of the Fourier morphology field could be represented uniformly across angular harmonic orders, or whether different harmonic ranges required different radial treatments. Candidate radial representations were therefore evaluated separately within four prespecified harmonic bands under garment-identity-disjoint validation and family-wise-error-rate-controlled inference (Fig. 2).

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

We denote the observed value by \(\Delta=T_b\).

For the lowest harmonic band, \(k=1{:}4\), the training-selected four-coefficient DCT representation yielded

\[
\Delta=0.059306,
\]

with bootstrap 95% CI

\[
[0.023295,\;0.108196],
\]

and multiplicity-controlled probability

\[
\boxed{p_{\mathrm{FWER}}=0.000200}.
\]

The compact representation was therefore retained:

\[
\boxed{k=1{:}4\rightarrow\mathrm{DCT}_4}.
\]

The result differed for the two intermediate harmonic ranges. For \(k=5{:}12\), the training-selected four-coefficient wavelet candidate produced

\[
\Delta=0.005984,
\qquad
95\%\ \mathrm{CI}=[-0.014164,\;0.060361],
\]

with

\[
p_{\mathrm{FWER}}=0.608939.
\]

For \(k=13{:}24\),

\[
\Delta=0.010959,
\qquad
95\%\ \mathrm{CI}=[-0.003088,\;0.073320],
\]

with

\[
p_{\mathrm{FWER}}=0.487751.
\]

Neither intermediate-band compression survived the prespecified inferential criterion. Complete 72-shell radial structure was therefore preserved in both ranges rather than forcing dimensional reduction:

\[
\boxed{
k=5{:}12\rightarrow\mathrm{RAW}_{72},
\qquad
k=13{:}24\rightarrow\mathrm{RAW}_{72}.
}
\]

At the highest tested harmonic range, \(k=25{:}36\), the selected four-coefficient db4-wavelet representation again received inferential support:

\[
\Delta=0.039300,
\]

\[
95\%\ \mathrm{CI}=[0.019130,\;0.091021],
\]

and

\[
\boxed{p_{\mathrm{FWER}}=0.019698}.
\]

The retained representation was therefore

\[
\boxed{k=25{:}36\rightarrow\mathrm{db4\ wavelet}_4}.
\]

### Table 1. Confirmatory radial-representation decisions

| Harmonic band | Tested compressed representation | \(\Delta=T_b\) | Bootstrap 95% CI | \(p_{\mathrm{FWER}}\) | Retained representation |
|---|---|---:|---:|---:|---|
| \(k=1{:}4\) | DCT, \(B=4\) | 0.059306 | [0.023295, 0.108196] | 0.000200 | \(\mathrm{DCT}_4\) |
| \(k=5{:}12\) | Wavelet, \(B=4\) | 0.005984 | [-0.014164, 0.060361] | 0.608939 | \(\mathrm{RAW}_{72}\) |
| \(k=13{:}24\) | Wavelet, \(B=4\) | 0.010959 | [-0.003088, 0.073320] | 0.487751 | \(\mathrm{RAW}_{72}\) |
| \(k=25{:}36\) | db4 wavelet, \(B=4\) | 0.039300 | [0.019130, 0.091021] | 0.019698 | \(\mathrm{db4\ wavelet}_4\) |

The four decisions therefore produced the heterogeneous radial-spectral representation

\[
\boxed{
\mathrm{DCT}_4/
\mathrm{RAW}_{72}/
\mathrm{RAW}_{72}/
\mathrm{db4}_4
}.
\]

The important result is not simply that some bands could be compressed. Rather, **support for radial compression was harmonic-dependent under the tested inferential framework**. Compact radial encodings were supported at \(k=1{:}4\) and \(k=25{:}36\), whereas the evidence was insufficient to replace complete radial structure at \(k=5{:}24\). Failure to establish compression support is not interpreted as proof of intrinsic incompressibility; it determines only that compression was not justified by the present validation design. This distinction is central to the evidence-controlled representation strategy.

---

## 4.2 Evidence-controlled selection produced a heterogeneous hybrid representation

The complete positive-harmonic morphology field contains

\[
36\times72=2592
\]

complex coefficients per sketch. Applying the four evidence-supported representation decisions gave

\[
4\times4=16
\]

coefficients for \(k=1{:}4\),

\[
8\times72=576
\]

for \(k=5{:}12\),

\[
12\times72=864
\]

for \(k=13{:}24\), and

\[
12\times4=48
\]

for \(k=25{:}36\).

As summarized in Fig. 2, the resulting hybrid representation therefore contained

\[
16+576+864+48
=
\boxed{1504}
\]

complex coefficients per sketch, corresponding to a

\[
\boxed{41.98\%}
\]

reduction relative to the complete 2592-coefficient field and a compression ratio of

\[
\boxed{1.7234\times}.
\]

Exact block-wise real/imaginary packing produced a frozen

\[
\boxed{3008\text{-dimensional}}
\]

real representation.

This dimensional reduction follows from the inferential decisions in Section 4.1; it was **not** obtained by selecting a global compression rate or by treating discarded coefficients as noise. In particular, the two intermediate harmonic ranges account for most of the retained dimensionality precisely because the tested compression alternatives were not supported there. The final representation therefore preserves heterogeneity in radial representation requirements rather than imposing a uniform basis across the Fourier field.

---

## 4.3 Nonlinear latent models did not earn a validated replacement of PCA

We next asked whether the heterogeneous radial-spectral representation required a nonlinear latent model for practical identity-preserving representation. PCA, autoencoder (AE), and variational autoencoder (VAE) representations were compared at

\[
z\in\{8,16,24,32,64\}
\]

using held-out garment-identity mean reciprocal rank (MRR) across five identity-disjoint outer folds.

Ten prespecified same-dimensional nonlinear-versus-PCA contrasts were evaluated using exhaustive fold-level sign flips and a maximum statistic across the entire contrast family.

### Table 2. Nonlinear latent-model contrasts relative to same-dimensional PCA

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
\mathrm{VAE}_{16}-\mathrm{PCA}_{16}
=
+0.014341\ \mathrm{MRR}
},
\]

but its selection-aware adjusted probability was

\[
\boxed{p_{\mathrm{FWER}}=0.2500}.
\]

None of the ten tested nonlinear contrasts survived multiplicity control. PCA was therefore retained as the **practical validated latent baseline** for morphology interpretation; the experiment did not establish sufficient task evidence to replace it with AE or VAE.

This negative result is deliberately narrow. With five outer folds, the exhaustive paired analysis contains only

\[
2^5=32
\]

sign configurations, giving coarse probability resolution, and the training portions of the outer folds overlap. The analysis therefore does not prove population-level superiority of PCA, nor does failure of nonlinear-model superiority imply that the morphology geometry itself is linear.

---

## 4.4 Detectable nonlinear pairwise structure did not imply nonlinear-model utility

To separate **nonlinear predictive structure** from **model selection**, the validated PCA representation was subsequently examined without reopening the PCA/AE/VAE decision.

The prespecified pairwise audit identified

\[
\boxed{1}
\]

FWER-supported quadratic PCA-coordinate relation. The strongest held-out improvement of the fixed quadratic predictor over the corresponding linear predictor was

\[
\boxed{\overline{\Delta R^2}=+0.432042}.
\]

This result establishes detectable **pairwise nonlinear predictability** within the retained PCA-coordinate description. It is not interpreted as differential-geometric manifold curvature, a unique nonlinear manifold, or evidence that a nonlinear encoder should replace PCA.

A separate neighborhood-scale dimensionality diagnostic found that, at the prespecified 20-neighbour scale, the identity-level median number of directions required to retain 90% of within-neighborhood variance was 15 (IQR 15–15). Because a centered 20-neighbour matrix has rank at most 19 by construction, this value is reported only as a scale-conditioned descriptive quantity. It is **not** compared with the global 90%-variance PCA dimension, and the previously reported local/global ratio is retired from scientific interpretation.

Additional nonlinear embedding, principal-curve and diffusion-map audits likewise failed to establish a stable nonlinear representation that warranted replacing the practical PCA baseline. The supported conclusion is therefore deliberately narrow:

\[
\boxed{
\text{detectable nonlinear pairwise structure}
\;\not\Rightarrow\;
\text{validated nonlinear-model advantage}.
}
\]

Figure 3 summarizes this separation. The result guards against treating PCA utility as proof that all relationships in the representation are linear, while also avoiding the converse error of treating a supported quadratic coordinate relation as sufficient justification for a more complex latent model.

---

## 4.5 Retained PCA axes mapped to heterogeneous radial–harmonic morphology

The first 64 PCA components accounted for

\[
\boxed{44.65\%}
\]

of variance in the standardized 3008-dimensional hybrid representation. All subsequent morphology localization is therefore conditional on this retained PCA-64 subspace.

To determine what the latent coordinates represented in the original morphology domain, each PCA direction \(j\) was mapped through the exact frozen inverse representation to obtain

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

The selected axes in Fig. 4A–C demonstrate that PCA directions did not correspond to one common spatial-spectral mode. PC1 was strongly outer-radial: 97.59% of its morphology energy occurred in shells 49–72, while 81.68% occurred across the combined intermediate harmonics \(k=5{:}24\). Its maximum-energy coordinate was

\[
(r,k)=(72,17).
\]

PC3 showed a similarly strong outer-radial pattern, with 96.47% of its energy in the outer region and 79.61% at \(k=5{:}24\), but with maximum energy at

\[
(r,k)=(72,13).
\]

PC15 provided a contrasting morphology mode. Its energy was predominantly inner-radial:

\[
71.51\%
\]

occurred in shells 1–24, with maximum energy at

\[
(r,k)=(5,5).
\]

These examples establish that the latent representation contains distinct radial–harmonic modes rather than a single uniform morphology pattern. The differences are localization differences only: PC1, PC3 and PC15 are not assigned garment-part, causal or semantic identities.

---

## 4.6 Retained morphology variation was concentrated in intermediate harmonics and outer radial structure

We then aggregated morphology localization across all 64 retained components using their PCA explained-variance ratios as within-subspace weights.

The resulting \(3\times4\) radial-region × harmonic-band distribution (Fig. 4D) was:

| Radial region | \(k=1{:}4\) | \(k=5{:}12\) | \(k=13{:}24\) | \(k=25{:}36\) |
|---|---:|---:|---:|---:|
| Inner, shells 1–24 | 2.29% | 9.57% | 7.21% | 1.59% |
| Middle, shells 25–48 | 2.04% | 5.47% | 4.98% | <0.01% |
| Outer, shells 49–72 | 8.60% | 24.13% | 27.17% | 6.94% |

Summed across radial zones,

\[
\boxed{78.54\%}
\]

of variance-weighted mapped morphology energy occurred at intermediate angular harmonics

\[
k=5{:}24.
\]

Summed across harmonic ranges,

\[
\boxed{66.84\%}
\]

occurred in the outer radial zone.

Most notably, the joint outer-radial × intermediate-harmonic region contained

\[
\boxed{51.30\%}
\]

of the retained mapped morphology energy. The two largest individual cells were outer × \(k=13{:}24\),

\[
27.17\%,
\]

and outer × \(k=5{:}12\),

\[
24.13\%.
\]

The spectral and radial centroids of the 64 retained PCA directions were likewise heterogeneous (Fig. 4E): leading axes were concentrated toward larger radial centroids, while later directions extended toward more internal radial locations and across different harmonic-centroid positions.

These percentages have a strict denominator. They describe **variance-weighted morphology localization within the retained PCA-64 subspace**, which itself represents 44.65% of standardized representation variance. They are not percentages of total garment morphology, the full 3008-dimensional representation, semantic garment parts, or causal morphology factors.

---

## 4.7 Results synthesis

Taken together, the experiments resolve a sequence of representation questions.

Radial structure did **not** receive uniform compression support across angular harmonic scale. Instead, identity-disjoint, multiplicity-controlled validation produced the heterogeneous representation

\[
\boxed{
\mathrm{DCT}_4/
\mathrm{RAW}_{72}/
\mathrm{RAW}_{72}/
\mathrm{db4}_4
},
\]

reducing the complete Fourier field from 2592 to 1504 complex coefficients while preserving full radial structure in the harmonic ranges where compression was not supported.

A second level of validation showed that greater latent-model complexity also had to earn its place. Tested AE and VAE alternatives did not establish a multiplicity-controlled retrieval advantage over same-dimensional PCA, so PCA remained the practical latent baseline. Yet a separate audit detected nonlinear pairwise predictability, demonstrating that **lack of validated nonlinear-model utility is not evidence that all relationships in the representation are linear**.

Finally, exact inverse mapping of PCA perturbations returned latent variation to explicit radial–harmonic coordinates. Within the retained PCA-64 subspace, mapped morphology energy was concentrated predominantly in intermediate harmonic orders and outer radial structure, while individual components showed substantially heterogeneous localization.

The overall empirical pattern is therefore not one of uniformly simplifying garment morphology. It is one of **selective representation**: compact encoding where held-out evidence supports it, preservation where it does not, conservative latent-model selection, and explicit mapping of retained latent variation back to the morphology coordinates from which the representation was constructed.
