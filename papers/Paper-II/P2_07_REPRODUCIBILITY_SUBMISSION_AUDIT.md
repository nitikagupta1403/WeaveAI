# CLO-SKET Paper 2 — Reproducibility and Submission Evidence Audit

## Status

**REPRODUCIBILITY + SUBMISSION EVIDENCE AUDIT: LOCKED WHEN ALL ITEMS PASS**

This document verifies that every major manuscript claim can be reproduced from the frozen computational lineage.

The objective is not to run new scientific experiments.

The objective is to establish that:

1. every reported number has a computational source;
2. every figure can be regenerated from frozen objects;
3. every inferential claim has the correct sampling unit;
4. every dimensional transformation is traceable;
5. every negative result remains preserved;
6. manuscript language cannot exceed the evidence;
7. another researcher could reconstruct the reported pipeline.

---

# 1. Reproducibility principle

The required provenance chain is:

\[
\boxed{
\text{raw sketches}
\rightarrow
P(\theta\mid r)
\rightarrow
F_k(r)
\rightarrow
\text{compression inference}
\rightarrow
\text{hybrid representation}
\rightarrow
\text{latent validation}
\rightarrow
\text{PCA morphology}
\rightarrow
\text{manuscript claim}
}
\]

No final manuscript number should exist without a corresponding frozen computational object or deterministic derivation.

---

# 2. Dataset contract

The final Paper 2 dataset contract is:

\[
N_{\text{sketch}}=2300
\]

\[
N_{\text{identity}}=230
\]

\[
N_{\text{category}}=23.
\]

There are:

\[
10
\]

garment identities per category.

The dataset lineage must establish:

- 2300 unique sketch records;
- 230 recovered garment identities;
- 23 categories;
- garment identity as the grouped validation unit;
- category as the stratification/balancing variable where applicable.

## Audit requirement

The code or saved audit output must demonstrate that these quantities are not manually entered assumptions.

---

# 3. Radial-angular representation contract

The canonical conditional probability field must satisfy:

\[
P_i(\theta\mid r)\geq0
\]

and, for occupied radial shells,

\[
\sum_\theta P_i(\theta\mid r)=1.
\]

Frozen dimensions:

\[
2300
\times
72
\times
72.
\]

The angular Fourier field must satisfy:

\[
F_{i,k}(r)
=
\sum_\theta
P_i(\theta\mid r)
e^{-ik\theta}.
\]

Positive angular harmonics used in Paper 2:

\[
k=1,\ldots,36.
\]

Frozen hybrid field dimensions:

\[
\boxed{
2300\times72\times36
}
\]

for the reconstructed radial-harmonic field.

## Audit requirement

Verify:

- radial centers = 72;
- angular bins = 72;
- positive harmonic orders = 36;
- no NaN values;
- no infinite values;
- consistent sketch order across all derived representations.

---

# 4. Sketch-order lineage

This is critical.

Every frozen object must refer to the same sketch ordering.

The provenance chain must confirm alignment among:

- file paths;
- category labels;
- garment identity labels;
- \(P(\theta\mid r)\);
- \(F_k(r)\);
- hybrid representation;
- real-packed representation;
- latent-model inputs.

## Required condition

For any sketch index \(i\),

\[
\text{path}_i,
\quad
\text{identity}_i,
\quad
P_i,
\quad
F_i,
\quad
x_i
\]

must refer to the same original sketch.

No silent reordering is permitted.

---

# 5. Harmonic-band contract

The final harmonic bands are:

\[
B_1 = 1{:}4
\]

\[
B_2 = 5{:}12
\]

\[
B_3 = 13{:}24
\]

\[
B_4 = 25{:}36.
\]

The code used for inferential testing must reproduce this partition exactly.

## Audit requirement

Confirm:

- no overlapping harmonic indices;
- no missing harmonics;
- total count:

\[
4+8+12+12=36.
\]

---

# 6. Candidate radial-representation contract

The tested radial representation candidates must be recoverable from the notebook/code.

Candidate families include:

- full/raw radial structure;
- DCT compression;
- wavelet compression;
- any frozen candidate-budget variants used during selection.

The final manuscript must clearly distinguish:

\[
\text{tested compact candidate}
\]

from:

\[
\text{final retained representation}.
\]

For unsupported compact candidates, the final representation is RAW.

This distinction is mandatory.

---

# 7. Garment-identity-disjoint validation audit

The main validation contract is:

\[
G_{\mathrm{train}}
\cap
G_{\mathrm{test}}
=
\varnothing.
\]

No garment identity may occur in both training and testing within the same fold.

## Required audit outputs

For every fold report:

- training sketch count;
- test sketch count;
- training identity count;
- test identity count;
- number of categories in training;
- number of categories in testing;
- train/test identity intersection.

Required:

\[
\boxed{
|G_{\mathrm{train}}\cap G_{\mathrm{test}}|=0
}
\]

for every fold.

---

# 8. Category-balance audit

Where category-balanced evaluation is claimed, the code must verify that the grouped fold construction preserves the frozen category design.

The manuscript must not imply random sketch-level splitting.

The relevant unit is:

\[
\boxed{
\text{complete garment identity}.
}
\]

---

# 9. Bootstrap contract

Where confidence intervals are reported, complete garment identities must be the bootstrap unit.

Required:

\[
B_{\text{bootstrap}}=5000
\]

for the frozen confirmatory analysis unless the final notebook specifies otherwise for a particular secondary analysis.

Bootstrap resampling must not treat individual sketches as independent observations when the intended inferential unit is garment identity.

## Required documentation

Record:

- bootstrap unit;
- bootstrap replicate count;
- confidence interval method;
- random seed or deterministic seed strategy.

---

# 10. Permutation contract

The confirmatory compression inference must preserve the category structure used by the frozen null design.

Required permutation count:

\[
B_{\text{perm}}=10000
\]

for the primary inferential analysis.

Permutation must occur at the correct grouped level.

The manuscript must state exactly what correspondence is broken under the null.

---

# 11. Family-wise-error-rate contract

The main compression claim depends on simultaneous inference.

Therefore the manuscript must identify:

- the family of tested hypotheses;
- the max-statistic procedure;
- how the observed effects are compared against the null distribution;
- the definition of

\[
p_{\mathrm{FWER}}.
\]

The final four values must reproduce exactly:

\[
k=1{:}4:
\quad
p_{\mathrm{FWER}}=0.000200
\]

\[
k=5{:}12:
\quad
p_{\mathrm{FWER}}=0.608939
\]

\[
k=13{:}24:
\quad
p_{\mathrm{FWER}}=0.487751
\]

\[
k=25{:}36:
\quad
p_{\mathrm{FWER}}=0.019698.
\]

---

# 12. Compression-effect contract

The corresponding frozen category-balanced effects are:

\[
\boxed{
0.059306
}
\]

for \(k=1{:}4\),

\[
\boxed{
0.005984
}
\]

for \(k=5{:}12\),

\[
\boxed{
0.010959
}
\]

for \(k=13{:}24\),

and

\[
\boxed{
0.039300
}
\]

for \(k=25{:}36\).

Bootstrap intervals:

\[
[0.023295,\ 0.108196]
\]

\[
[-0.014164,\ 0.060361]
\]

\[
[-0.003088,\ 0.073320]
\]

\[
[0.019130,\ 0.091021].
\]

## Audit condition

These exact values must agree between:

- frozen notebook output;
- Table 2;
- Figure 2;
- Results prose;
- Abstract if reported there.

---

# 13. Compression-decision contract

The manuscript decision rule must reproduce:

\[
\boxed{
k=1{:}4
\rightarrow
DCT_4
}
\]

\[
\boxed{
k=5{:}12
\rightarrow
RAW_{72}
}
\]

\[
\boxed{
k=13{:}24
\rightarrow
RAW_{72}
}
\]

\[
\boxed{
k=25{:}36
\rightarrow
db4\text{-wavelet}_4.
}
\]

The reason RAW is retained in intermediate bands is:

\[
\boxed{
\text{compression support was not established}
}
\]

not:

\[
\text{RAW performed a positive compression effect}.
\]

---

# 14. Hybrid-dimension contract

The frozen complex block dimensions are:

## Low

\[
4\times4=16
\]

## Mid

\[
8\times72=576
\]

## High-middle

\[
12\times72=864
\]

## High

\[
12\times4=48.
\]

Therefore:

\[
16+576+864+48
=
\boxed{1504}.
\]

The original uncompressed field contains:

\[
36\times72
=
\boxed{2592}.
\]

Thus:

\[
\boxed{
2592\rightarrow1504
}
\]

with coefficient reduction:

\[
1-\frac{1504}{2592}
=
\boxed{41.98\%}
\]

and compression ratio:

\[
\frac{2592}{1504}
=
\boxed{1.7234\times}.
\]

These values must be generated programmatically rather than typed manually into figures.

---

# 15. Real-packing contract

The frozen real representation must be reconstructed using:

\[
\boxed{
\texttt{BLOCK\_FLAT\_REAL\_THEN\_IMAG}
}
\]

for each complex block.

For block \(A\),

\[
\rho(A)
=
[
\Re(\operatorname{vec}A),
\Im(\operatorname{vec}A)
].
\]

The block ranges in the final real vector must correspond to:

- low;
- mid;
- high-middle;
- high.

Required total dimension:

\[
\boxed{3008}.
\]

## Exact audit

Repacking the complex blocks must reproduce the frozen real representation with numerical error:

\[
\boxed{0}
\]

within floating-point audit tolerance.

---

# 16. Representation finiteness audit

All frozen representation objects must satisfy:

\[
N_{\mathrm{NaN}}=0
\]

and

\[
N_{\mathrm{Inf}}=0.
\]

This includes:

- real hybrid representation;
- complex hybrid field;
- PCA input;
- mapped PC perturbations;
- morphology-energy matrices.

---

# 17. Standardization contract

PCA is performed on feature-wise standardized real representations.

For feature \(m\),

\[
\tilde x_{im}
=
\frac{x_{im}-\mu_m}{\sigma_m}.
\]

The implementation must verify:

- mean and scale learned from the correct population/fold according to analysis purpose;
- no zero-variance feature causes undefined values;
- exact feature order preserved.

---

# 18. PCA contract

The retained interpretation model has:

\[
q=64
\]

principal components.

Frozen cumulative standardized variance:

\[
\boxed{
0.446455
}
\]

or:

\[
\boxed{
44.65\%
}.
\]

## Audit requirement

The exact value must agree across:

- PCA object;
- Cell 17D;
- Methods;
- Results;
- Figure 4 caption;
- Abstract where reported.

---

# 19. PCA interpretation scope

Every reproducibility record must preserve:

\[
\boxed{
\text{PCA-64 captures 44.65% of standardized representation variance.}
}
\]

It must not be transformed into:

> PCA captures 44.65% of garment morphology.

The denominator differs.

This is a claim-audit requirement as well as a mathematical one.

---

# 20. Nonlinear-model validation contract

The nonlinear latent-model comparison must retain:

- identical grouped evaluation logic;
- identical downstream task definition;
- identical primary evaluation metrics;
- multiplicity correction;
- fixed comparison against PCA.

The final reproducible conclusion is:

\[
\boxed{
\text{tested nonlinear models did not establish a multiplicity-controlled task advantage over PCA}.
}
\]

The audit must verify that this is a negative result, not an omitted comparison.

---

# 21. Geometry-audit reproducibility

The following analyses should remain reproducible but secondary:

- canonical PCA geometry audit;
- Isomap;
- principal-curve analysis;
- principal-curve stability;
- diffusion maps.

The exact parameter ranges and random seeds should be documented in Supplementary Material or code.

The final geometry conclusion is:

\[
\boxed{
\text{nonlinear structure detectable}
}
\]

while:

\[
\boxed{
\text{validated nonlinear replacement not established}.
}
\]

---

# 22. PCA perturbation contract

For PCA component \(j\),

\[
\Delta x_j
=
D_\sigma
\left[
\sqrt{\lambda_j}v_j
\right].
\]

The implementation must use the frozen PCA:

- loading vector \(v_j\);
- eigenvalue \(\lambda_j\);
- feature scaling \(D_\sigma\).

No manually modified PC direction is allowed.

---

# 23. Exact inverse-hybrid contract

The perturbation:

\[
\Delta x_j
\]

must be unpacked according to the exact verified real/complex lineage.

The inverse transformation must apply:

- inverse DCT for \(k=1{:}4\);
- identity mapping for \(k=5{:}12\);
- identity mapping for \(k=13{:}24\);
- inverse db4 wavelet mapping for \(k=25{:}36\).

This produces:

\[
\boxed{
\Delta F_j(r,k).
}
\]

The reconstructed dimensions must be:

\[
64
\times
72
\times
36.
\]

---

# 24. Morphology-energy contract

For PC \(j\),

\[
E_j(r,k)
=
|\Delta F_j(r,k)|^2.
\]

Normalize:

\[
p_j(r,k)
=
\frac{
E_j(r,k)
}{
\sum_r\sum_kE_j(r,k)
}.
\]

Required numerical condition:

\[
\sum_r\sum_kp_j(r,k)
=
1
\]

for every retained PC within numerical tolerance.

---

# 25. Radial-zone contract

The descriptive radial zones are:

## Inner

\[
r=1{:}24
\]

## Middle

\[
r=25{:}48
\]

## Outer

\[
r=49{:}72.
\]

These partitions are equal-shell descriptive regions.

They are not anatomical or semantic garment parts.

---

# 26. Harmonic-localization contract

The same four harmonic bands used in representation inference must be used for morphology localization:

\[
1{:}4
\]

\[
5{:}12
\]

\[
13{:}24
\]

\[
25{:}36.
\]

Do not silently redefine the bands for Figure 4.

---

# 27. Variance-weighting contract

For PCA explained-variance ratio \(\eta_j\),

\[
w_j
=
\frac{
\eta_j
}{
\sum_{\ell=1}^{64}\eta_\ell
}.
\]

Required:

\[
\sum_{j=1}^{64}w_j=1.
\]

Then:

\[
\bar P(R,B)
=
\sum_{j=1}^{64}
w_jP_j(R,B).
\]

---

# 28. Final morphology-value contract

The frozen quantities are:

## Intermediate harmonics

\[
\boxed{
0.785350
}
\]

or:

\[
\boxed{
78.54\%
}
\]

## Outer radial

\[
\boxed{
0.668410
}
\]

or:

\[
\boxed{
66.84\%
}
\]

## Outer × intermediate

\[
\boxed{
0.513031
}
\]

or:

\[
\boxed{
51.30\%
}.
\]

These must agree across:

- Cell 17D;
- Cell 18 evidence contract;
- Cell 19 mathematical reconstruction;
- Cell 21 Results;
- Cell 23 Abstract;
- Figure 4;
- final manuscript.

---

# 29. Mathematical reconstruction audit

Cell 19 demonstrated that the final mathematical definitions reproduce the frozen Cell 17D morphology values exactly.

The submission record should preserve this as a critical provenance check:

\[
\boxed{
\text{maximum reconstruction discrepancy}
\approx0
}
\]

within the frozen numerical tolerance.

This establishes that the manuscript equations correspond to what the code actually computed.

---

# 30. Figure-generation contract

Every main figure must have a dedicated deterministic generation script or notebook section.

Suggested files:

```text
figures/
├── make_fig01_representation.py
├── make_fig02_compression_inference.py
├── make_fig03_latent_validation.py
└── make_fig04_morphology_localization.py