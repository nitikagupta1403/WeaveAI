# CLO-SKET Paper 2 — Final Results

## Status

**FINAL RESULTS ASSEMBLY: READY FOR MANUSCRIPT INTEGRATION**

This Results section reports only frozen evidence.

It contains:

- inferential findings;
- exact representation dimensions;
- validated negative results;
- descriptive retained-subspace morphology localization.

It does not introduce new interpretation beyond what is required to state the findings.

---

# 4. Results

## 4.1 Radial compression support differed across angular harmonic bands

Radial representation was evaluated separately across four angular harmonic bands under garment-identity-disjoint validation with family-wise-error-rate-controlled inference.

For the low harmonic band

\[
k=1{:}4,
\]

the four-coefficient DCT representation produced a positive category-balanced effect of

\[
\Delta=0.059306.
\]

The corresponding bootstrap 95% confidence interval was

\[
[0.023295,\ 0.108196],
\]

and the effect remained supported after max-statistic family-wise-error-rate correction:

\[
\boxed{
p_{\mathrm{FWER}}=0.000200
}.
\]

Accordingly, the frozen radial representation for this band was

\[
\boxed{
\mathrm{DCT}_4.
}
\]

---

For the intermediate harmonic band

\[
k=5{:}12,
\]

the tested four-coefficient wavelet representation produced an observed effect of

\[
\Delta=0.005984,
\]

with bootstrap 95% confidence interval

\[
[-0.014164,\ 0.060361]
\]

and family-wise-error-rate-controlled probability

\[
p_{\mathrm{FWER}}=0.608939.
\]

Compression was therefore not inferentially supported for this band.

The complete radial representation was retained:

\[
\boxed{
\mathrm{RAW}_{72}.
}
\]

---

For the high-middle harmonic band

\[
k=13{:}24,
\]

the tested four-coefficient wavelet representation produced an effect of

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

Compression was again not inferentially supported.

The complete 72-shell radial structure was therefore retained:

\[
\boxed{
\mathrm{RAW}_{72}.
}
\]

---

For the highest tested harmonic band

\[
k=25{:}36,
\]

the four-coefficient db4-wavelet representation produced a positive effect of

\[
\Delta=0.039300.
\]

The bootstrap 95% confidence interval was

\[
[0.019130,\ 0.091021],
\]

and the result remained supported after family-wise-error-rate correction:

\[
\boxed{
p_{\mathrm{FWER}}=0.019698.
}
\]

The frozen radial representation for this band was therefore

\[
\boxed{
\mathrm{db4\ wavelet}_4.
}
\]

---

Taken together, the four inferential decisions produced the frozen band-specific representation

\[
\boxed{
k=1{:}4
\rightarrow
\mathrm{DCT}_4
}
\]

\[
\boxed{
k=5{:}12
\rightarrow
\mathrm{RAW}_{72}
}
\]

\[
\boxed{
k=13{:}24
\rightarrow
\mathrm{RAW}_{72}
}
\]

\[
\boxed{
k=25{:}36
\rightarrow
\mathrm{db4\ wavelet}_4.
}
\]

Thus, under the tested validation framework, support for radial compression differed across angular harmonic bands.

---

## 4.2 Evidence-supported hybrid radial-spectral representation

The complete radial-harmonic field contains

\[
36\times72
=
2592
\]

complex coefficients per sketch.

After applying the inferentially selected band-specific radial representations, the frozen hybrid field contained:

\[
4\times4=16
\]

complex coefficients for \(k=1{:}4\),

\[
8\times72=576
\]

for \(k=5{:}12\),

\[
12\times72=864
\]

for \(k=13{:}24\),

and

\[
12\times4=48
\]

for \(k=25{:}36\).

The resulting hybrid representation therefore contained

\[
16+576+864+48
=
\boxed{1504}
\]

complex coefficients per sketch.

Relative to the original 2592-coefficient field, this corresponds to

\[
\boxed{
41.98\%
}
\]

coefficient reduction and a compression ratio of

\[
\boxed{
1.7234\times.
}
\]

After exact block-wise real/imaginary packing, the frozen representation contained

\[
\boxed{
3008
}
\]

real dimensions per sketch.

No numerical instability was detected in the frozen representation objects.

---

## 4.3 Nonlinear latent models did not establish a validated task advantage over PCA

The frozen 3008-dimensional representation was standardized before latent-model evaluation.

PCA provided the linear reference representation.

The tested nonlinear latent alternatives were evaluated under the same garment-identity-disjoint framework.

Across the confirmatory model comparisons, the nonlinear latent models did not establish a multiplicity-controlled task advantage over PCA.

PCA was therefore retained as the practical latent representation for subsequent morphology interpretation.

This result concerns validated model utility.

It does not establish that the underlying representation geometry is globally linear.

---

## 4.4 Geometry audits identified nonlinear structure without a stable replacement representation

Separate geometric analyses identified departures from a purely linear description of the retained morphology space.

The explored nonlinear embeddings showed evidence of local geometric structure, but they did not establish a single stable canonical nonlinear coordinate system suitable for replacing PCA.

In particular, the principal-curve analysis did not support a stable one-dimensional morphology trajectory.

The corresponding stability audit did not establish a reproducible principal curve as a canonical latent coordinate.

The diffusion-map analysis likewise did not provide sufficient evidence to replace the PCA representation.

These analyses were therefore retained as geometric characterization and sensitivity evidence rather than used to redefine the frozen latent representation.

---

## 4.5 PCA-64 retained 44.65% of standardized representation variance

The first

\[
64
\]

principal components accounted for

\[
\boxed{
44.65\%
}
\]

of standardized representation variance.

All subsequent radial-harmonic morphology localization was therefore interpreted explicitly within this retained PCA-64 subspace.

The retained subspace was used for interpretation because it provided the frozen practical latent representation after the nonlinear model-validation analysis.

---

## 4.6 Retained PCA morphology was concentrated in intermediate harmonic orders

Each retained PCA direction was mapped through the exact frozen inverse representation to obtain

\[
\Delta F_j(r,k),
\]

and corresponding sign-invariant morphology energy

\[
E_j(r,k)
=
|\Delta F_j(r,k)|^2.
\]

After normalization and variance weighting across the 64 retained components,

\[
\boxed{
78.54\%
}
\]

of mapped morphology energy occurred in the intermediate harmonic range

\[
k=5{:}24.
\]

The complementary low and high extreme harmonic ranges together contained

\[
21.46\%
\]

of the retained mapped morphology energy.

Thus, within the retained PCA-64 subspace, morphology energy was concentrated predominantly in the intermediate angular harmonic orders.

---

## 4.7 Retained PCA morphology showed strong outer-radial localization

Across radial position,

\[
\boxed{
66.84\%
}
\]

of variance-weighted mapped morphology energy occurred in the outer radial zone

\[
r=49{:}72.
\]

The remaining energy was distributed across the inner and middle radial zones.

The radial zones used here are representation-space partitions.

No semantic garment-part interpretation was assigned to the outer radial region.

---

## 4.8 More than half of retained mapped morphology energy occupied the outer-radial × intermediate-harmonic region

Joint radial-harmonic localization showed that

\[
\boxed{
51.30\%
}
\]

of variance-weighted mapped morphology energy occurred within the combination of:

\[
\text{outer radial}
\]

and

\[
k=5{:}24.
\]

This value is reported as a joint localization quantity.

No formal interaction hypothesis between radial zone and harmonic band was tested.

Accordingly, the result is not interpreted as evidence of enrichment, synergy, or preferential coupling beyond the observed marginal concentrations.

---

## 4.9 Individual principal components exhibited heterogeneous radial-harmonic localization

Although the variance-weighted retained-subspace summary was dominated by intermediate harmonics and outer radial structure, individual principal directions were not identical.

Leading components were predominantly localized toward outer radial regions, while later retained directions included components with stronger inner-radial localization.

Similarly, integrated harmonic-band dominance and the location of individual harmonic maxima were not always identical.

These component-specific differences indicate that the retained PCA representation contains multiple radial-harmonic modes of variation rather than one uniform spatial-spectral pattern.

This result remains descriptive and does not assign semantic meaning to individual PCA axes.

---

# 4.10 Summary of primary results

The primary inferential result is:

\[
\boxed{
\text{support for radial compression differed across angular harmonic bands.}
}
\]

The frozen representation was:

\[
\boxed{
\mathrm{DCT}_4
/
\mathrm{RAW}_{72}
/
\mathrm{RAW}_{72}
/
\mathrm{db4}_4
}
\]

across the four harmonic ranges.

This reduced the complex coefficient count from

\[
2592
\]

to

\[
1504,
\]

corresponding to

\[
41.98\%
\]

coefficient reduction.

The latent-model validation did not establish multiplicity-controlled superiority of the tested nonlinear representations over PCA.

The retained PCA-64 subspace accounted for

\[
44.65\%
\]

of standardized representation variance.

Within that retained subspace:

\[
\boxed{
78.54\%
}
\]

of mapped morphology energy occurred at intermediate harmonic orders,

\[
\boxed{
66.84\%
}
\]

occurred in the outer radial zone,

and

\[
\boxed{
51.30\%
}
\]

occurred jointly in the outer-radial × intermediate-harmonic region.

---

# Results claim boundary

## Supported

The Results support the following statements:

- radial compression support differed across harmonic bands;
- compact DCT representation was supported for \(k=1{:}4\);
- compact db4-wavelet representation was supported for \(k=25{:}36\);
- tested compression was not supported for \(k=5{:}24\);
- the frozen hybrid representation contains 1504 complex / 3008 real coefficients;
- coefficient count was reduced by 41.98%;
- tested nonlinear models did not establish a multiplicity-controlled task advantage over PCA;
- nonlinear geometric structure was detectable without establishing a stable nonlinear replacement representation;
- PCA-64 retained 44.65% of standardized representation variance;
- within PCA-64, mapped morphology energy was strongly concentrated in intermediate harmonic orders and outer radial positions.

---

## Not supported

The Results do not establish that:

- low harmonic orders are meaningful signal;
- high harmonic orders are noise;
- intermediate harmonics are mathematically incompressible;
- discarded coefficients are irrelevant;
- outer radial position corresponds to a garment boundary;
- PCA axes correspond to semantic garment factors;
- PCA captures complete garment morphology;
- nonlinear models are generally inferior;
- one canonical nonlinear manifold exists;
- 51.30% represents a radial-harmonic interaction effect.

---

# Primary result table

| Harmonic band | Tested / retained radial representation | Effect | Bootstrap 95% CI | \(p_{\mathrm{FWER}}\) | Final decision |
|---|---|---:|---:|---:|---|
| \(k=1{:}4\) | DCT, \(B=4\) | 0.059306 | [0.023295, 0.108196] | 0.000200 | Compression supported |
| \(k=5{:}12\) | Wavelet \(B=4\) tested; RAW retained | 0.005984 | [-0.014164, 0.060361] | 0.608939 | Compression not supported |
| \(k=13{:}24\) | Wavelet \(B=4\) tested; RAW retained | 0.010959 | [-0.003088, 0.073320] | 0.487751 | Compression not supported |
| \(k=25{:}36\) | db4 wavelet, \(B=4\) | 0.039300 | [0.019130, 0.091021] | 0.019698 | Compression supported |

---

# Results evidence flow

\[
\boxed{
\text{band-specific compression inference}
}
\]

\[
\downarrow
\]

\[
\boxed{
DCT/RAW/RAW/WAVELET
}
\]

\[
\downarrow
\]

\[
\boxed{
2592\rightarrow1504
}
\]

\[
\downarrow
\]

\[
\boxed{
PCA\ retained
}
\]

\[
\downarrow
\]

\[
\boxed{
PCA_{64}=44.65\%
}
\]

\[
\downarrow
\]

\[
\boxed{
78.54\%\ intermediate
}
\]

\[
\boxed{
66.84\%\ outer
}
\]

\[
\boxed{
51.30\%\ joint
}
\]

---

# Step 9 lock

\[
\boxed{
\textbf{PAPER 2 FINAL RESULTS — ASSEMBLED}
}
\]

Next:

\[
\boxed{
\textbf{STEP 10 — FINAL DISCUSSION ASSEMBLY}
}
\]

The Discussion may interpret these findings, but it may not strengthen the underlying evidence class.