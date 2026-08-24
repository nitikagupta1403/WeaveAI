# CLO-SKET Paper 2 — Final Results

## Status

**FINAL RESULTS ASSEMBLY: READY FOR MANUSCRIPT INTEGRATION**

This Results section reports only frozen evidence. It separates confirmatory radial-compression inference, validated latent-model comparison, and descriptive retained-subspace morphology localization.

---

# 4. Results

## 4.1 Radial compression support differed across tested angular harmonic bands

Radial representation was evaluated separately across four angular harmonic bands under garment-identity-disjoint validation with family-wise-error-rate-controlled inference. The confirmatory effect statistic was the category-balanced held-out garment-identity separation effect defined in Methods,

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

For compactness, the observed value is denoted \(\Delta=T_b\) below.

For the low harmonic band \(k=1{:}4\), the training-selected four-coefficient DCT representation produced

\[
\Delta=0.059306,
\]

with bootstrap 95% confidence interval

\[
[0.023295,\ 0.108196]
\]

and max-statistic family-wise-error-rate-controlled probability

\[
\boxed{p_{\mathrm{FWER}}=0.000200}.
\]

Compression was therefore supported, and the retained representation was

\[
\boxed{\mathrm{DCT}_4}.
\]

For \(k=5{:}12\), the training-selected four-coefficient wavelet representation produced

\[
\Delta=0.005984,
\]

with bootstrap 95% confidence interval

\[
[-0.014164,\ 0.060361]
\]

and

\[
p_{\mathrm{FWER}}=0.608939.
\]

Compression was not inferentially supported, and the complete radial representation was retained:

\[
\boxed{\mathrm{RAW}_{72}}.
\]

For \(k=13{:}24\), the training-selected four-coefficient wavelet representation produced

\[
\Delta=0.010959,
\]

with bootstrap 95% confidence interval

\[
[-0.003088,\ 0.073320]
\]

and

\[
p_{\mathrm{FWER}}=0.487751.
\]

Compression was again not inferentially supported, and the complete radial representation was retained:

\[
\boxed{\mathrm{RAW}_{72}}.
\]

For the highest tested harmonic band, \(k=25{:}36\), the training-selected four-coefficient db4-wavelet representation produced

\[
\Delta=0.039300,
\]

with bootstrap 95% confidence interval

\[
[0.019130,\ 0.091021]
\]

and

\[
\boxed{p_{\mathrm{FWER}}=0.019698}.
\]

Compression was therefore supported, and the retained representation was

\[
\boxed{\mathrm{db4\ wavelet}_4}.
\]

### Table 1. Confirmatory radial-compression inference

| Harmonic band | Tested / retained radial representation | \(T_b\) | Bootstrap 95% CI | \(p_{\mathrm{FWER}}\) | Final decision |
|---|---|---:|---:|---:|---|
| \(k=1{:}4\) | DCT, \(B=4\) | 0.059306 | [0.023295, 0.108196] | 0.000200 | Compression supported |
| \(k=5{:}12\) | Wavelet, \(B=4\), tested; RAW retained | 0.005984 | [-0.014164, 0.060361] | 0.608939 | Compression not supported |
| \(k=13{:}24\) | Wavelet, \(B=4\), tested; RAW retained | 0.010959 | [-0.003088, 0.073320] | 0.487751 | Compression not supported |
| \(k=25{:}36\) | db4 wavelet, \(B=4\) | 0.039300 | [0.019130, 0.091021] | 0.019698 | Compression supported |

Taken together, the four confirmatory decisions yielded

\[
\boxed{
k=1{:}4\rightarrow\mathrm{DCT}_4,
\quad
k=5{:}12\rightarrow\mathrm{RAW}_{72},
\quad
k=13{:}24\rightarrow\mathrm{RAW}_{72},
\quad
k=25{:}36\rightarrow\mathrm{db4\ wavelet}_4
}.
\]

Thus, under the tested identity-disjoint inferential framework, support for radial compression differed across angular harmonic bands. Failure to establish compression support for \(k=5{:}24\) is not interpreted as evidence that those bands are intrinsically incompressible.

---

## 4.2 Evidence-supported hybrid radial-spectral representation

The complete radial-harmonic field contains

\[
36\times72=2592
\]

complex coefficients per sketch. The inferentially selected hybrid representation contained

\[
4\times4=16,
\qquad
8\times72=576,
\qquad
12\times72=864,
\qquad
12\times4=48
\]

complex coefficients across the four harmonic bands, respectively. The resulting field therefore contained

\[
16+576+864+48
=
\boxed{1504}
\]

complex coefficients per sketch.

Relative to the original 2592-coefficient field, this corresponds to

\[
\boxed{41.98\%}
\]

coefficient reduction and a compression ratio of

\[
\boxed{1.7234\times}.
\]

After exact block-wise real/imaginary packing, the frozen representation contained

\[
\boxed{3008}
\]

real dimensions per sketch. This reduction is a representation-dimensionality result and is not interpreted as removal of noise or irrelevant morphology.

---

## 4.3 Nonlinear latent models did not establish a multiplicity-controlled task advantage over PCA

PCA, autoencoder (AE), and variational autoencoder (VAE) representations were compared at latent dimensions

\[
z\in\{8,16,24,32,64\}
\]

using held-out garment-identity mean reciprocal rank across five outer identity-disjoint folds. The ten prespecified AE-versus-PCA and VAE-versus-PCA contrasts were evaluated with simultaneous family-wise error control using the exact fold-level sign-flip procedure described in Methods.

Across these confirmatory comparisons, no nonlinear representation established a multiplicity-controlled improvement over PCA. PCA was therefore retained as the practical latent basis for subsequent morphology interpretation.

This negative result concerns validated downstream task utility. It does not establish that PCA is universally superior to nonlinear latent models, nor that the underlying representation geometry is globally linear.

---

## 4.4 Geometry audits identified nonlinear structure without a stable replacement representation

Separate geometric analyses identified departures from a purely linear description of the retained morphology space. The explored nonlinear embeddings showed evidence of local geometric structure, but they did not establish a single stable canonical nonlinear coordinate system suitable for replacing PCA.

In particular, principal-curve analysis and its stability audit did not establish a reproducible one-dimensional morphology trajectory as a canonical latent coordinate. Diffusion-map sensitivity analysis likewise did not provide sufficient evidence to replace PCA.

These analyses were therefore retained as geometric characterization and sensitivity evidence rather than used to redefine the frozen latent representation.

---

## 4.5 PCA-64 accounted for 44.65% of variance in the standardized frozen representation

The first

\[
64
\]

principal components accounted for

\[
\boxed{44.65\%}
\]

of variance in the standardized frozen 3008-dimensional representation.

All subsequent radial-harmonic morphology localization is therefore explicitly conditional on this retained PCA-64 subspace; it is not a decomposition of the complete representation variance.

---

## 4.6 Retained PCA morphology was concentrated in intermediate harmonic orders

Each retained PCA direction was mapped through the exact frozen inverse representation to obtain

\[
\Delta F_j(r,k),
\]

with sign-invariant morphology energy

\[
E_j(r,k)=|\Delta F_j(r,k)|^2.
\]

After normalization and variance weighting across the 64 retained components,

\[
\boxed{78.54\%}
\]

of mapped morphology energy occurred in the intermediate harmonic range

\[
k=5{:}24.
\]

The complementary low and highest harmonic ranges together contained 21.46% of the retained mapped morphology energy. Thus, within the retained PCA-64 subspace, mapped morphology energy was concentrated predominantly in intermediate angular harmonic orders.

---

## 4.7 Retained PCA morphology showed strong outer-radial localization

Across radial position,

\[
\boxed{66.84\%}
\]

of variance-weighted mapped morphology energy occurred in the outer radial zone

\[
r=49{:}72.
\]

The remaining energy was distributed across the inner and middle radial zones. These radial zones are representation-space partitions; no semantic garment-part or garment-boundary interpretation is assigned to the outer radial region.

---

## 4.8 More than half of retained mapped morphology energy occupied the outer-radial × intermediate-harmonic region

Joint radial-harmonic localization showed that

\[
\boxed{51.30\%}
\]

of variance-weighted mapped morphology energy occurred jointly in the outer radial zone and

\[
k=5{:}24.
\]

This is a joint localization quantity. No formal radial-zone-by-harmonic-band interaction hypothesis was tested; the result is therefore not interpreted as evidence of enrichment, synergy, or preferential coupling beyond the observed localization.

---

## 4.9 Individual principal components exhibited heterogeneous radial-harmonic localization

Although the variance-weighted retained-subspace summary was dominated by intermediate harmonics and outer radial structure, individual principal directions were heterogeneous. Leading components were predominantly localized toward outer radial regions, while later retained directions included components with stronger inner-radial localization. Integrated harmonic-band dominance and the location of individual harmonic maxima were also not always identical.

The retained PCA representation therefore contains multiple radial-harmonic modes of variation rather than one uniform spatial-spectral pattern. This result is descriptive and does not assign semantic meaning to individual PCA axes.

---

## 4.10 Summary of primary results

The primary confirmatory result is that radial compression support differed across the tested harmonic bands under the identity-disjoint inferential framework. The resulting frozen representation was

\[
\boxed{
\mathrm{DCT}_4/
\mathrm{RAW}_{72}/
\mathrm{RAW}_{72}/
\mathrm{db4}_4
},
\]

reducing the complex coefficient count from 2592 to 1504, or 41.98%.

Separately, validated PCA/AE/VAE comparison did not establish a multiplicity-controlled nonlinear task advantage over PCA. PCA-64 accounted for 44.65% of variance in the standardized frozen representation.

Within that retained PCA-64 subspace, 78.54% of mapped morphology energy occurred at intermediate harmonic orders, 66.84% occurred in the outer radial zone, and 51.30% occurred jointly in the outer-radial × intermediate-harmonic region. These localization quantities are descriptive properties of the retained subspace and are not semantic or interaction effects.
