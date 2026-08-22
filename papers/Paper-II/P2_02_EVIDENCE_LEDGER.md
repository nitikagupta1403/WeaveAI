# CLO-SKET Paper 2 — Evidence Ledger

## Status

**Paper 2 Evidence Ledger: LOCKED**

This document records the exact relationship between:

- manuscript claims;
- computational evidence;
- statistical status;
- allowed wording;
- prohibited wording.

It is intended to prevent drift between the frozen analysis and the manuscript.

Novelty relative to prior literature is **not** established here and remains subject to the dedicated literature audit.

---

# 1. Evidence hierarchy

Paper 2 distinguishes four evidence levels.

## M — Mathematical / construction evidence

A statement follows directly from the definition of the representation or from an exact verified transformation.

Examples:

\[
P_i(\theta\mid r)
\rightarrow
F_{i,k}(r)
\]

and

\[
Z_i\in\mathbb{C}^{1504}
\rightarrow
x_i\in\mathbb{R}^{3008}.
\]

These are mathematical or computational facts, not statistical findings.

---

## I — Inferential evidence

A claim is supported or unsupported through the prespecified statistical inference.

Examples include:

- family-wise-error-rate-controlled radial compression tests;
- multiplicity-controlled latent-model comparisons.

Inferential non-support must not be rewritten as proof of impossibility.

---

## D — Descriptive evidence

A quantity describes the observed frozen representation or latent subspace but is not itself a formal statistical hypothesis test.

Examples include:

- PCA variance retained;
- radial-harmonic morphology-energy localization.

---

## Q — Qualified scientific interpretation

A statement synthesizes mathematical, inferential, and descriptive evidence while remaining within explicit claim boundaries.

Example:

> Radial redundancy is harmonic-scale dependent under the examined representation and validation framework.

Qualified interpretations are not universal laws.

---

# 2. Core mathematical representation

For sketch \(i\), the morphology is represented as a conditional angular probability field

\[
P_i(\theta\mid r),
\]

with

\[
P_i(\theta\mid r)\geq 0,
\]

and, for occupied radial shells,

\[
\sum_{\theta} P_i(\theta\mid r)=1.
\]

Angular Fourier morphology is then defined as

\[
F_{i,k}(r)
=
\sum_{\theta}
P_i(\theta\mid r)
e^{-ik\theta},
\]

for positive angular harmonic orders

\[
k=1,\ldots,36.
\]

The representation therefore retains two explicit coordinates:

\[
\boxed{r\times k}
\]

where:

- \(r\) denotes radial position;
- \(k\) denotes angular harmonic scale.

### Evidence type

**M — Mathematical / construction**

### Allowed wording

> Each sketch was represented as a conditional radial-angular probability field and transformed angularly into radial Fourier harmonic functions \(F_k(r)\).

### Not supported

> \(F_k(r)\) is a complete semantic representation of garment shape.

> Angular harmonic order directly identifies garment parts.

---

# 3. Harmonic-band partition

The frozen harmonic bands are:

\[
K_1 = 1{:}4,
\]

\[
K_2 = 5{:}12,
\]

\[
K_3 = 13{:}24,
\]

\[
K_4 = 25{:}36.
\]

Radial compression was evaluated separately for these four bands under strict garment-identity-disjoint validation.

---

# 4. Low harmonic band: \(k=1{:}4\)

## Frozen result

Selected radial representation:

\[
\boxed{\mathrm{DCT},\ B=4}
\]

Observed category-balanced effect:

\[
\Delta = 0.059306
\]

Bootstrap interval:

\[
95\%\ \mathrm{CI}
=
[0.023295,\ 0.108196]
\]

Family-wise-error-rate-controlled probability:

\[
\boxed{
p_{\mathrm{FWER}}=0.000200
}
\]

## Evidence type

**I — Inferential**

## Supported wording

> Four-coefficient DCT radial compression was supported for the low harmonic band \(k=1{:}4\) under the prespecified multiplicity-controlled inference.

## Not supported

> Low harmonics are inherently compressible.

> Low harmonics are signal.

> All information outside the retained DCT coefficients is noise.

---

# 5. Intermediate harmonic band: \(k=5{:}12\)

## Frozen tested result

Best tested compact representation:

\[
\mathrm{wavelet},\ B=4
\]

Observed effect:

\[
\Delta = 0.005984
\]

Bootstrap interval:

\[
95\%\ \mathrm{CI}
=
[-0.014164,\ 0.060361]
\]

Family-wise-error-rate-controlled probability:

\[
p_{\mathrm{FWER}}=0.608939
\]

Final frozen radial representation:

\[
\boxed{
\mathrm{RAW}_{72}
}
\]

## Evidence type

**I — Negative inferential boundary**

## Supported wording

> Compression was not inferentially supported for \(k=5{:}12\) under the tested framework, and the complete 72-shell radial structure was therefore retained.

## Not supported

> \(k=5{:}12\) is mathematically incompressible.

> No compact representation of this band could ever exist.

> Unsupported compression implies absence of redundancy.

---

# 6. High-middle harmonic band: \(k=13{:}24\)

## Frozen tested result

Best tested compact representation:

\[
\mathrm{wavelet},\ B=4
\]

Observed effect:

\[
\Delta = 0.010959
\]

Bootstrap interval:

\[
95\%\ \mathrm{CI}
=
[-0.003088,\ 0.073320]
\]

Family-wise-error-rate-controlled probability:

\[
p_{\mathrm{FWER}}=0.487751
\]

Final frozen radial representation:

\[
\boxed{
\mathrm{RAW}_{72}
}
\]

## Evidence type

**I — Negative inferential boundary**

## Supported wording

> Compression was not inferentially supported for \(k=13{:}24\) under the tested framework, and the complete radial structure was retained.

## Not supported

> The band is mathematically incompressible.

> Lack of compression support means lack of morphology.

---

# 7. High harmonic band: \(k=25{:}36\)

## Frozen result

Selected representation:

\[
\boxed{
\mathrm{db4\ wavelet},\ B=4
}
\]

Observed category-balanced effect:

\[
\Delta = 0.039300
\]

Bootstrap interval:

\[
95\%\ \mathrm{CI}
=
[0.019130,\ 0.091021]
\]

Family-wise-error-rate-controlled probability:

\[
\boxed{
p_{\mathrm{FWER}}=0.019698
}
\]

## Evidence type

**I — Inferential**

## Supported wording

> Four-coefficient db4-wavelet radial compression was supported for \(k=25{:}36\).

## Not supported

> High harmonics are noise.

> Wavelet compressibility proves that fine angular structure is unimportant.

---

# 8. Primary compression conclusion

The frozen band-specific representation is

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
\mathrm{db4\ wavelet}_4
}
\]

## Primary inferential interpretation

\[
\boxed{
\text{Support for radial compression depends on angular harmonic scale.}
}
\]

## Evidence type

**Q/I — Primary qualified interpretation supported by the band-wise inference**

## Allowed wording

> The data did not support a single uniform radial compression rule across angular harmonic bands.

> Radial representation requirements varied with angular harmonic scale under the tested framework.

## Not supported

> Radial complexity is universally determined by harmonic order.

---

# 9. Frozen hybrid radial-spectral representation

For sketch \(i\),

\[
Z_i
=
\Big[
\mathcal C_{\mathrm{DCT},4}
\{F_{i,k}(r)\}_{k=1}^{4},
\;
\{F_{i,k}(r)\}_{k=5}^{12},
\;
\{F_{i,k}(r)\}_{k=13}^{24},
\;
\mathcal C_{\mathrm{WAV},4}
\{F_{i,k}(r)\}_{k=25}^{36}
\Big].
\]

Its complex dimensions are:

\[
4\times4 = 16
\]

for \(k=1{:}4\),

\[
8\times72 = 576
\]

for \(k=5{:}12\),

\[
12\times72 = 864
\]

for \(k=13{:}24\),

and

\[
12\times4 = 48
\]

for \(k=25{:}36\).

Therefore,

\[
16+576+864+48
=
\boxed{1504}
\]

complex coefficients per sketch.

The complete uncompressed field contains

\[
72\times36
=
\boxed{2592}
\]

complex coefficients.

Thus,

\[
2592
\rightarrow
1504
\]

corresponds to

\[
\boxed{
41.98\%
}
\]

coefficient reduction, with compression ratio

\[
\boxed{
1.7234\times
}.
\]

## Evidence type

**M — Exact dimension calculation after frozen inferential selection**

## Supported wording

> The evidence-guided hybrid representation reduced the complex coefficient count by 41.98%.

## Not supported

> The representation removed 41.98% noise.

> The removed coefficients were irrelevant morphology.

---

# 10. Exact complex-to-real representation lineage

Each complex block \(A\) is packed as

\[
\rho(A)
=
[
\Re(\mathrm{vec}(A)),
\Im(\mathrm{vec}(A))
].
\]

The four blocks are concatenated independently using the verified convention:

\[
\boxed{
\texttt{BLOCK\_FLAT\_REAL\_THEN\_IMAG}
}
\]

yielding

\[
Z_i\in\mathbb C^{1504}
\]

and

\[
\boxed{
x_i\in\mathbb R^{3008}
}.
\]

The packing lineage was numerically verified exactly before latent morphology inversion.

## Evidence type

**M — Computational provenance**

## Supported wording

> Exact block-wise real/complex representation lineage was verified before latent interpretation.

---

# 11. PCA latent representation

The real representation was standardized feature-wise:

\[
\tilde x_{im}
=
\frac{x_{im}-\mu_m}{\sigma_m}.
\]

PCA coordinates are

\[
z_{ij}
=
v_j^\top \tilde x_i.
\]

The retained latent dimension is

\[
\boxed{
q=64
}
\]

with cumulative standardized representation variance

\[
\boxed{
44.65\%
}.
\]

## Evidence type

**D/M**

## Supported wording

> The first 64 principal components accounted for 44.65% of standardized representation variance.

## Not supported

> PCA captured 44.65% of total garment morphology.

> The remaining 55.35% is noise.

> PCA captured 44.65% of all useful information.

---

# 12. Nonlinear latent-model comparison

Nonlinear latent models were evaluated against PCA under the frozen validation framework.

The primary result is:

\[
\boxed{
\text{A multiplicity-controlled task advantage of the tested nonlinear models over PCA was not established.}
}
\]

PCA was therefore retained as the practical latent baseline.

## Evidence type

**I — Inferential negative boundary**

## Supported wording

> The tested nonlinear latent models did not establish a multiplicity-controlled task advantage over PCA.

> PCA was retained as the validated practical latent representation.

## Not supported

> PCA is universally superior to nonlinear latent models.

> Nonlinear models do not work.

> Garment morphology is linear.

---

# 13. Nonlinear geometry audit

Separate geometric analyses identified departures from a purely linear geometric description.

However:

- nonlinear model superiority was not established;
- a stable one-dimensional principal trajectory was not recovered;
- diffusion geometry did not establish a superior replacement representation;
- no unique canonical nonlinear latent coordinate system was established.

## Evidence type

**D/Q with negative inferential constraints**

## Supported interpretation

\[
\boxed{
\text{Nonlinear geometry can coexist with PCA remaining the practical validated latent representation.}
}
\]

Equivalently,

\[
\boxed{
\text{nonlinear geometry}
\not\Rightarrow
\text{nonlinear model required}
}
\]

and

\[
\boxed{
\text{PCA retained}
\not\Rightarrow
\text{geometry proven linear}.
}
\]

## Not supported

> The data have one canonical nonlinear manifold.

> The true morphology space is one-dimensional.

> A principal curve represents garment progression.

---

# 14. Exact PCA-to-Fourier morphology mapping

For retained PC \(j\), a one-score-standard-deviation displacement in standardized space is

\[
\sqrt{\lambda_j}v_j.
\]

Undoing feature standardization gives

\[
\Delta x_j
=
D_\sigma
\left[
\sqrt{\lambda_j}v_j
\right].
\]

The exact inverse representation then produces

\[
\boxed{
\Delta F_j(r,k)
}.
\]

Morphology energy is defined as

\[
\boxed{
E_j(r,k)
=
|\Delta F_j(r,k)|^2
}.
\]

Because PCA eigenvector orientation is arbitrary,

\[
E_j(r,k)
\]

is invariant to the sign choice

\[
v_j
\rightarrow
-v_j.
\]

Normalize:

\[
p_j(r,k)
=
\frac{
E_j(r,k)
}{
\sum_r\sum_k E_j(r,k)
}.
\]

For radial zone \(R\) and harmonic band \(B\),

\[
P_j(R,B)
=
\sum_{r\in R}
\sum_{k\in B}
p_j(r,k).
\]

Retained-PC variance weights are

\[
w_j
=
\frac{\eta_j}
{\sum_{\ell=1}^{64}\eta_\ell}.
\]

The final retained-subspace morphology localization is

\[
\boxed{
\bar P(R,B)
=
\sum_{j=1}^{64}
w_jP_j(R,B)
}.
\]

## Evidence type

**M — Mathematical / exact inverse construction**

## Supported wording

> PCA perturbations were mapped through the exact frozen inverse representation to localize retained latent variation in radial-harmonic Fourier space.

## Not supported

> PCA axes directly identify physical garment components.

> PCA axes are semantic or causal garment factors.

---

# 15. Intermediate-harmonic morphology localization

Within the retained PCA-64 subspace,

\[
\boxed{
78.54\%
}
\]

of variance-weighted mapped morphology energy occurred in

\[
k=5{:}24.
\]

The complementary extreme harmonic bands jointly contained

\[
21.46\%.
\]

## Evidence type

**D — Descriptive**

## Supported wording

> Within the retained PCA-64 subspace, mapped morphology energy was strongly concentrated in intermediate angular harmonic orders \(k=5{:}24\).

## Not supported

> 78.54% of total garment morphology is intermediate-frequency morphology.

> Intermediate harmonics contain 78.54% of all useful garment information.

---

# 16. Radial morphology localization

Within the retained PCA-64 subspace,

\[
\boxed{
66.84\%
}
\]

of variance-weighted mapped morphology energy occurred in the outer radial zone.

## Evidence type

**D — Descriptive**

## Supported wording

> Retained PCA morphology showed strong outer-radial localization.

## Not supported

> 66.84% of garment morphology occurs at the garment boundary.

> Outer radial structure corresponds to hem, sleeve, waist, silhouette, or any other semantic garment part.

No semantic radial annotation was used.

---

# 17. Joint radial-harmonic localization

Within the retained PCA-64 subspace,

\[
\boxed{
51.30\%
}
\]

of variance-weighted mapped morphology energy occurred in

\[
\text{outer radial}
\times
k=5{:}24.
\]

## Evidence type

**D — Descriptive**

## Important interaction guard

The marginal concentrations are

\[
P(k=5{:}24)=0.7854
\]

and

\[
P(\mathrm{outer})=0.6684.
\]

Their approximate product is

\[
0.7854\times0.6684
\approx
0.525.
\]

The observed joint fraction is

\[
0.5130.
\]

Therefore the joint value should **not** be presented as evidence of an additional outer-radial × intermediate-harmonic interaction.

No interaction hypothesis was tested.

## Supported wording

> More than half of the retained mapped morphology energy occupied the outer-radial × intermediate-harmonic region.

## Not supported

> A strong outer-radial × intermediate-harmonic interaction was discovered.

---

# 18. Overall morphology interpretation

The evidence supports the following descriptive synthesis:

\[
\boxed{
\text{Retained latent morphology is structured jointly across radial position and angular harmonic scale.}
}
\]

This differs from the primary compression inference:

\[
\boxed{
\text{Radial compression support depends on angular harmonic scale.}
}
\]

These statements should remain separate in the manuscript.

The first is based mainly on the PCA morphology localization.

The second is based mainly on multiplicity-controlled radial compression inference.

---

# 19. Signal-versus-noise boundary

The results do not support the simplistic hierarchy

\[
\text{low }k=\text{signal}
\]

and

\[
\text{high }k=\text{noise}.
\]

The intermediate harmonic range contains most of the mapped morphology energy within PCA-64, while both low and high harmonic bands show supported compact radial representations.

Therefore the defensible interpretation is:

\[
\boxed{
\text{The Fourier morphology field exhibits structured radial-angular organization rather than a simple signal-to-noise frequency gradient.}
}
\]

This remains a qualified scientific interpretation, not a universal theorem.

---

# 20. Master claim ledger

| ID | Claim | Evidence class | Status |
|---|---|---|---|
| C1 | \(P(\theta\mid r)\rightarrow F_k(r)\) retains explicit radial and angular-harmonic coordinates | M | Established |
| C2 | DCT \(B=4\) radial compression is supported for \(k=1{:}4\) | I | Supported |
| C3 | Tested compression is not supported for \(k=5{:}12\) | I | Negative supported boundary |
| C4 | Tested compression is not supported for \(k=13{:}24\) | I | Negative supported boundary |
| C5 | db4-wavelet \(B=4\) compression is supported for \(k=25{:}36\) | I | Supported |
| C6 | Frozen hybrid representation contains 1504 complex / 3008 real coefficients | M | Established |
| C7 | Hybrid representation reduces complex coefficient count by 41.98% | M | Established |
| C8 | PCA-64 retains 44.65% of standardized representation variance | D | Descriptive |
| C9 | Tested nonlinear models do not establish multiplicity-controlled task superiority over PCA | I | Negative supported boundary |
| C10 | Nonlinear geometric structure is detectable | D/Q | Qualified |
| C11 | No stable canonical nonlinear replacement representation was established | I/D | Supported boundary |
| C12 | PCA perturbations can be mapped exactly to \(\Delta F_j(r,k)\) | M | Established |
| C13 | 78.54% of retained mapped morphology energy lies in \(k=5{:}24\) | D | Descriptive |
| C14 | 66.84% lies in the outer radial zone | D | Descriptive |
| C15 | 51.30% lies jointly in outer radial × \(k=5{:}24\) | D | Descriptive, not an interaction claim |
| C16 | Radial compression support is harmonic-scale dependent | I/Q | Primary interpretation |
| C17 | Retained morphology is jointly structured across radial and angular spectral coordinates | D/Q | Supported interpretation |
| C18 | The results do not support a simple low-frequency-signal/high-frequency-noise hierarchy | Q | Supported interpretation |

---

# 21. Global unsupported claims

The Paper 2 manuscript must not state or imply any of the following:

- low harmonic order equals meaningful signal;
- high harmonic order equals noise;
- discarded coefficients are noise;
- unsupported compression proves mathematical incompressibility;
- outer radial location is a garment boundary;
- outer radial location corresponds to a hem, waist, sleeve, or other garment part;
- PCA axes correspond directly to semantic garment attributes;
- PCA axes are causal morphology factors;
- PCA-64 represents complete garment morphology;
- the unexplained PCA variance is noise;
- nonlinear models are generally inferior;
- garment morphology is globally linear;
- one canonical nonlinear morphology manifold exists;
- one canonical morphology trajectory exists;
- the observed joint outer × intermediate value establishes an interaction;
- the framework is the first of its kind in the literature.

---

# 22. Current novelty status

The analysis establishes:

1. the mathematical representation;
2. the inferential compression results;
3. the frozen hybrid representation;
4. the latent-model validation;
5. the inverse PCA-to-Fourier morphology construction;
6. the descriptive radial-harmonic localization.

It does **not** establish literature priority.

Therefore:

\[
\boxed{
\text{NOVELTY STATUS: UNLOCKED}
}
\]

Any statement containing terms such as:

- novel;
- first;
- first-ever;
- previously unexplored;
- unprecedented;

must wait until completion of the dedicated literature and novelty audit.

---

# 23. Figure-to-evidence mapping

## Figure 1 — Probabilistic radial-angular morphology representation

Primary role:

\[
P(\theta\mid r)
\rightarrow
F_k(r)
\]

Evidence class:

**M — Representation / Methods**

---

## Figure 2 — Harmonic-dependent radial information structure

Primary role:

- band-specific radial compression;
- inferential support and non-support;
- frozen hybrid representation.

Evidence class:

**I — Inferential**

---

## Figure 3 — Validated latent geometry

Primary role:

- PCA baseline;
- nonlinear-model comparison;
- nonlinear geometry qualification.

Evidence class:

**I + D/Q**

---

## Figure 4 — Principal-component morphology localization

Primary role:

\[
PC_j
\rightarrow
\Delta F_j(r,k)
\rightarrow
|\Delta F_j(r,k)|^2
\]

plus variance-weighted radial-harmonic localization.

Evidence class:

**M + D**

---

# 24. One-sentence evidence-constrained conclusion

> Under garment-identity-disjoint validation, radial compression support differed across angular harmonic bands, motivating a hybrid radial-spectral representation; within its retained PCA-64 subspace, mapped latent morphology exhibited strong intermediate-harmonic and outer-radial organization, while nonlinear geometric structure did not establish a validated nonlinear replacement for PCA.

---

# 25. Step 2 lock

\[
\boxed{
\textbf{PAPER 2 EVIDENCE LEDGER — LOCKED}
}
\]

The next stage is:

\[
\boxed{
\textbf{STEP 3 — LITERATURE + NOVELTY AUDIT}
}
\]

No new representation experiment should be added unless the literature or manuscript audit reveals a genuine scientific gap.