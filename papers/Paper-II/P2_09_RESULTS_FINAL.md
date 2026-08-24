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


This confirmatory effect should not be interpreted as a held-out retrieval non-inferiority test. The \(Q_c\geq0.95\) criterion was used only inside each outer-training fold to define candidate eligibility; the confirmatory endpoint was the distinct held-out category-balanced separation statistic \(T_b\). Consequently, inferential support below means that the training-selected compact representation showed a positive held-out separation effect under the frozen design. It does not imply that discarded coefficients were noise or that compression is universally superior to the complete representation.

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


### 4.2.1 Occupancy and radial mass provided little additional identity-retrieval information

The positive-harmonic hybrid omits the conditional DC coefficient \(F_0(r)\). Because \(F_0(r)\) equals one on occupied shells and zero on empty shells, we first tested whether explicitly restoring the 72-dimensional occupied-shell indicator materially altered garment-identity retrieval.

Shell occupancy was nearly saturated in CLO-SKET:

\[
\boxed{99.8569\%}
\]

of the \(2300\times72\) sketch-shell locations were occupied. The mean number of occupied shells was

\[
71.897/72,
\]

and the median was \(72/72\).

Appending the occupancy indicator changed mean held-out MRR from

\[
0.816766
\]

for the frozen 3008-dimensional hybrid to

\[
0.816114,
\]

giving

\[
\boxed{\Delta\mathrm{MRR}=-0.000651}.
\]

Mean top-1 retrieval changed from \(0.633531\) to \(0.632229\),

\[
\boxed{\Delta\mathrm{Top1}=-0.001302}.
\]

Across the five frozen folds, MRR improved in one fold, decreased in two, and was unchanged in two. At query level, 2,291 of 2,300 ranks were unchanged, three improved, and six worsened. Explicit occupancy therefore provided no material retrieval benefit under this sensitivity design.

Radial ink mass \(M(r)\) contains different information from occupancy and from \(F_0\). Because no canonical \(2300\times72\) radial-mass array had been retained in the analysis checkpoints, \(M(r)\) was deterministically reconstructed from the original TIFFs using the frozen image-to-polar algorithm. The reconstruction reproduced the previously frozen occupancy mask exactly:

\[
\boxed{0\ \text{mismatched shell cells across 2,300 sketches}}.
\]

Appending this verified 72-dimensional radial-mass profile increased mean held-out MRR from \(0.816766\) to \(0.820252\),

\[
\boxed{\Delta\mathrm{MRR}=+0.003486},
\]

and mean top-1 retrieval from \(0.633531\) to \(0.640504\),

\[
\boxed{\Delta\mathrm{Top1}=+0.006973}.
\]

Four of five folds showed positive MRR differences and one showed a decrease. At query level, 2,230 of 2,300 ranks were unchanged, 43 improved, and 27 worsened. The effect is therefore reported descriptively as a small amount of complementary identity information carried by radial mass, not as an inferentially established improvement.

These sensitivities do not change the frozen primary representation. The 3008-dimensional descriptor remains a representation of **conditional angular morphology across radius**; occupancy and radial ink mass are distinct auxiliary quantities.



### 4.2.2 The heterogeneous descriptor matched full radial retrieval closely and avoided losses from uniform compact transforms

We next compared the frozen heterogeneous hybrid with complete and uniform whole-representation baselines. The hybrid contained 1504 complex coefficients (3008 real coordinates), whereas the complete \(\mathrm{RAW}_{72}\) field contained 2592 complex coefficients (5184 real coordinates). The dimension-matched uniform descriptors used 1512 complex coefficients (3024 real coordinates), only 0.532% more than the hybrid.

Mean held-out retrieval for the complete radial field was

\[
\mathrm{MRR}=0.819373,
\qquad
\mathrm{Top1}=0.638746.
\]

The frozen hybrid yielded

\[
\mathrm{MRR}=0.816766,
\qquad
\mathrm{Top1}=0.633531.
\]

Thus the complete \(\mathrm{RAW}_{72}\) field was descriptively higher by only

\[
\Delta\mathrm{MRR}=+0.002607
\]

and

\[
\Delta\mathrm{Top1}=+0.005215,
\]

while requiring 5184 rather than 3008 real coordinates.

The dimension-matched uniform raw descriptor was similarly close:

\[
\mathrm{MRR}=0.815896,
\qquad
\mathrm{Top1}=0.631792,
\]

corresponding to

\[
\Delta\mathrm{MRR}=-0.000870
\]

relative to the hybrid. Its fold-wise MRR difference was positive in three folds and negative in two.

In contrast, applying one compact transform uniformly across all harmonics produced consistently lower retrieval. Uniform DCT-42 yielded

\[
\mathrm{MRR}=0.783503,
\qquad
\mathrm{Top1}=0.567006,
\]

with

\[
\boxed{\Delta\mathrm{MRR}=-0.033263}
\]

relative to the hybrid. Uniform db4-wavelet-42 yielded

\[
\mathrm{MRR}=0.789378,
\qquad
\mathrm{Top1}=0.578755,
\]

with

\[
\boxed{\Delta\mathrm{MRR}=-0.027388}.
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

These comparisons are descriptive post-selection sensitivities rather than a new inferential family. They therefore do not establish population-level superiority of the hybrid over every alternative descriptor. They do show that the heterogeneous representation preserved nearly the retrieval behaviour of the complete radial field at substantially lower dimensionality, while avoiding the larger losses observed when a single compact DCT or wavelet representation was imposed uniformly across the harmonic field. Uniform \(\mathrm{RAW}_{42}\) remained a competitive simple baseline and is reported explicitly.


## 4.3 Nonlinear latent models did not earn a validated replacement of PCA

We next asked, **conditional on the heterogeneous radial-spectral representation selected by the preceding full cross-validated band analysis**, whether a nonlinear latent model earned sufficient task evidence to replace PCA for practical identity-preserving representation. PCA, autoencoder (AE), and variational autoencoder (VAE) representations were compared at

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

None of the ten tested nonlinear contrasts survived multiplicity control. Conditional on the previously selected hybrid representation, PCA was therefore retained as the **practical latent baseline** for morphology interpretation; the experiment did not establish sufficient task evidence to replace it with AE or VAE. Because the hybrid itself had been selected using cross-validated evidence from the complete CLO-SKET dataset before this comparison, these results are not an independent end-to-end validation of the combined representation-selection and latent-model-selection pipeline.

This negative result is deliberately narrow. With five outer folds, the exhaustive paired analysis contains only

\[
2^5=32
\]

sign configurations, giving coarse probability resolution, and the training portions of the outer folds overlap. The analysis therefore does not prove population-level superiority of PCA, does not provide an untouched end-to-end test of the full selection pipeline, and does not imply from failure of nonlinear-model superiority that all relationships in the representation are linear.

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

A separate neighborhood-scale dimensionality diagnostic found that, at the prespecified 20-neighbour scale, the identity-level median number of directions required to retain 90% of within-neighborhood variance was 15 (IQR 15–15). Because a centered 20-neighbour matrix has rank at most 19 by construction, this value is reported only as a scale-conditioned descriptive quantity. It is **not** compared with the global 90%-variance PCA dimension, and the previously reported ratio between local and global dimensions is retired from scientific interpretation.

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
