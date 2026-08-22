# CLO-SKET Paper 2 — Final Manuscript Assembly

## Manuscript Status

**SCIENTIFIC CONTENT FROZEN — INTEGRATED MANUSCRIPT DRAFT**

This manuscript assembles the previously frozen Paper 2 components.

No new experiment, numerical result, statistical inference, or scientific claim
is introduced during assembly.

---

# Evidence-Controlled Radial-Spectral Representation of Garment-Sketch Morphology

## Abstract

Garment sketches contain morphology distributed jointly across radial position
and angular scale, yet compact spectral representations typically impose a
common encoding rule across the transform domain. We investigate whether radial
representation requirements instead vary with angular harmonic scale.

Each sketch is represented as a conditional radial-angular probability field,

\[
P_i(\theta\mid r),
\]

and angular Fourier transformation yields radial harmonic functions

\[
F_{i,k}(r),
\qquad k=1,\ldots,36.
\]

Using 2,300 sketches from 230 garment identities across 23 categories, candidate
radial representations were evaluated separately across four harmonic bands
under garment-identity-disjoint validation with family-wise-error-rate-controlled
inference. Compact four-coefficient radial representations were supported for
\(k=1{:}4\) using a DCT basis and for \(k=25{:}36\) using a db4-wavelet basis,
whereas compression was not supported for the intermediate \(k=5{:}24\)
harmonics, whose complete 72-shell radial structure was retained.

The resulting heterogeneous DCT/raw/raw/wavelet representation reduced the
spectral description from 2,592 to 1,504 complex coefficients per sketch,
corresponding to a 41.98% coefficient reduction. Nonlinear latent models did not
establish a multiplicity-controlled task advantage over PCA, although geometric
audits identified nonlinear structure that was insufficient to justify replacing
the validated linear latent representation.

The first 64 principal components retained 44.65% of standardized representation
variance. Within this retained subspace, 78.54% of variance-weighted mapped
morphology energy occurred at intermediate harmonic orders \(k=5{:}24\),
66.84% occurred in the outer radial zone, and 51.30% occurred jointly in the
outer-radial × intermediate-harmonic region.

These results show that radial representation requirements and retained latent
morphology vary systematically across angular scale. The study supports an
evidence-controlled representation principle in which spectral structure is
compressed only where supported and otherwise preserved at full radial
resolution.

**Keywords:** garment sketch morphology; Fourier shape analysis; radial-angular
representation; spectral compression; principal component analysis;
interpretable morphology

---

# 1. Introduction

Representing the morphology of a garment sketch requires capturing structure
across multiple spatial scales while preserving the organization of shape across
the image.

A single global descriptor can provide a compact summary of shape, but such
compression may obscure where particular geometric structures occur. Conversely,
retaining a fully resolved spatial representation preserves localization but can
produce a high-dimensional description containing substantial redundancy.

The representation problem is therefore not simply how much morphology should be
compressed, but which dimensions of morphology can be compressed and under what
evidence.

This distinction is particularly relevant in polar coordinates, where radial
position and angular structure describe different aspects of geometry. Collapsing
both dimensions simultaneously can obscure whether radial representation
requirements vary with angular scale.

Fourier descriptors, polar spectral representations, angular-radial transforms,
and multiscale Fourier-wavelet approaches provide established mechanisms for
representing shape in frequency and polar domains [CITATIONS].

These methods establish that radial, angular, and multiscale structure can be
encoded spectrally. The present study addresses a different representation
question: whether the radial encoding itself should remain identical across
angular harmonic order.

For sketch \(i\), we represent angular morphology conditional on radial position
as

\[
P_i(\theta\mid r),
\]

and apply angular Fourier transformation independently at each radius:

\[
F_{i,k}(r)
=
\sum_\theta
P_i(\theta\mid r)e^{-ik\theta}.
\]

Thus each angular harmonic remains a radial function,

\[
F_{i,k}:r\mapsto\mathbb C,
\]

rather than being immediately collapsed into a global spectral coefficient.

This formulation allows us to ask

\[
\text{Does the radial information structure of }F_k(r)
\text{ depend on angular harmonic scale }k?
\]

We address this question by treating radial compression as an inferential
representation-selection problem. Candidate radial representations are evaluated
separately across prespecified harmonic bands under garment-identity-disjoint
validation and multiplicity-controlled inference.

The resulting principle is intentionally conservative:

\[
\boxed{
\text{compress where supported; preserve where support is absent}.
}
\]

After representation selection, we separately examine whether nonlinear latent
models provide validated task advantages over PCA and whether the representation
nevertheless exhibits nonlinear geometric structure.

Finally, PCA perturbations are mapped exactly back into the original
radial-harmonic Fourier domain, allowing latent variation to be localized in
\((r,k)\) space without assigning unsupported semantic meaning to latent axes.

Accordingly, this study addresses four questions:

1. Does support for radial compression differ across angular harmonic scale?
2. Can band-specific selection produce a lower-dimensional hybrid representation
   while preserving full radial structure where compression is unsupported?
3. Does nonlinear geometry imply that a nonlinear latent representation should
   replace PCA under garment-identity-disjoint validation?
4. Where is variation within the retained PCA subspace localized across radial
   position and angular harmonic order?

---

# 2. Related Work

## 2.1 Fourier and polar shape representations

Fourier descriptors are established tools for contour- and region-based shape
analysis. Their compact spectral representations and transformation properties
have supported applications in recognition and retrieval [CITATIONS].

Polar formulations extend this idea by retaining radial and angular organization.

The Generic Fourier Descriptor applies Fourier analysis to a polar-raster
representation, while the Angular Radial Transform constructs basis functions
jointly over radial and angular dimensions [CITATIONS].

These approaches establish the value of polar spectral shape representation.

Our framework differs in retaining

\[
F_k(r)
\]

explicitly as a radial function for each angular harmonic before determining
whether radial compression is justified.

---

## 2.2 Multiscale and wavelet shape representations

Wavelet and multiscale Fourier approaches introduce localized or
multiresolution information into spectral shape description [CITATIONS].

These methods establish that global Fourier and localized wavelet representations
can coexist productively.

The present framework does not claim novelty for combining these transforms.

Instead, it asks whether different radial bases should be assigned to different
angular harmonic ranges according to validation evidence rather than imposed
uniformly across the spectrum.

---

## 2.3 Evidence-guided representation selection

Classical descriptor design often emphasizes compactness.

Here, compactness is conditional on validation support.

If a tested compact representation is unsupported for a harmonic range, the
complete radial structure is retained.

The representation is therefore allowed to be heterogeneous:

\[
\text{compressed}
+
\text{uncompressed}
\]

regions can coexist within one spectral descriptor.

---

## 2.4 Linear and nonlinear latent representations

PCA provides an orthogonal linear representation, whereas nonlinear
dimensionality-reduction and manifold-learning approaches attempt to preserve
nonlinear geometric relationships [CITATIONS].

The existence of nonlinear geometry, however, is distinct from validated
nonlinear-model utility.

We therefore evaluate these questions separately: nonlinear latent models are
compared against PCA under grouped validation, while manifold-oriented methods
are used as geometric characterization and sensitivity analyses.

---

## 2.5 Position of the present study

The methodological contribution does not lie in Fourier analysis, DCTs,
wavelets, PCA, or polar representations individually.

The contribution investigated here is their integration around the principle

\[
\boxed{
\text{radial representation is selected conditionally on angular harmonic scale}
}
\]

under garment-identity-disjoint validation and multiplicity-controlled inference.

The framework additionally preserves complete radial structure where tested
compression is unsupported and maps retained latent directions exactly back to
their radial-harmonic morphology domain.

No literature-wide priority claim is made.

---

# 3. Methods

## 3.1 Dataset and analysis units

The analysis used 2,300 CLO-SKET garment sketches corresponding to 230 garment
identities across 23 garment categories.

Garment identity was treated as the primary grouping unit for validation and
statistical inference.

For every validation fold,

\[
G_{\mathrm{train}}\cap G_{\mathrm{test}}=\varnothing.
\]

This prevents sketches derived from the same garment identity from contributing
to both model construction and evaluation.

---

## 3.2 Probabilistic radial-angular representation

Each sketch was represented using a radial-angular conditional probability field

\[
P_i(\theta\mid r).
\]

For every occupied radial shell,

\[
P_i(\theta\mid r)\geq0
\]

and

\[
\sum_\theta P_i(\theta\mid r)=1.
\]

The representation contained 72 radial shells.

Empty shells were retained as structurally empty rather than assigned an
artificial angular distribution.

---

## 3.3 Angular Fourier morphology

For sketch \(i\), radial shell \(r\), and harmonic order \(k\),

\[
F_{i,k}(r)
=
\sum_\theta
P_i(\theta\mid r)
\exp(-\mathrm{i}k\theta).
\]

Positive harmonics

\[
k=1,\ldots,36
\]

were retained.

The complete field therefore contained

\[
72\times36=2592
\]

complex coefficients per sketch.

---

## 3.4 Harmonic-band partition

The retained harmonics were partitioned into four frozen ranges:

\[
K_1=1{:}4,
\qquad
K_2=5{:}12,
\qquad
K_3=13{:}24,
\qquad
K_4=25{:}36.
\]

Radial representation was evaluated independently within each range.

---

## 3.5 Candidate radial representations and inference

Candidate representations included complete 72-shell radial structure and
compact transform representations based on DCT and wavelet families.

Representation comparisons were conducted under garment-identity-disjoint
validation.

Uncertainty was estimated using complete garment-identity bootstrap resampling
with

\[
5000
\]

replicates.

Permutation inference used

\[
10000
\]

replicates under the frozen category-preserving design.

Family-wise error across the confirmatory compression comparisons was controlled
using the frozen max-statistic procedure.

A compact representation was retained only when supported under the
family-wise-error-rate criterion.

Otherwise, complete radial structure was preserved.

---

## 3.6 Frozen hybrid representation

The resulting radial encoding was

\[
k=1{:}4
\rightarrow
\mathrm{DCT}_4,
\]

\[
k=5{:}12
\rightarrow
\mathrm{RAW}_{72},
\]

\[
k=13{:}24
\rightarrow
\mathrm{RAW}_{72},
\]

and

\[
k=25{:}36
\rightarrow
\mathrm{db4\ wavelet}_4.
\]

The hybrid representation was

\[
Z_i
=
\Big[
\mathcal C_{\mathrm{DCT},4}\{F_{i,k}(r)\}_{k=1}^{4},
\{F_{i,k}(r)\}_{k=5}^{12},
\{F_{i,k}(r)\}_{k=13}^{24},
\mathcal C_{\mathrm{WAV},4}\{F_{i,k}(r)\}_{k=25}^{36}
\Big].
\]

It contained

\[
16+576+864+48=1504
\]

complex coefficients per sketch.

---

## 3.7 Exact real representation

Each complex block \(A\) was packed independently as

\[
\rho(A)
=
[
\Re(\operatorname{vec}(A)),
\Im(\operatorname{vec}(A))
].
\]

The verified convention was block-wise flattened real coefficients followed by
imaginary coefficients.

The resulting representation was

\[
x_i\in\mathbb R^{3008}.
\]

---

## 3.8 Standardization and PCA

Each real feature was standardized:

\[
\tilde{x}_{im}
=
\frac{x_{im}-\mu_m}{\sigma_m}.
\]

PCA was then applied to the standardized representation.

For loading vector \(v_j\),

\[
z_{ij}
=
v_j^\top\tilde{x}_i.
\]

The first 64 principal components were retained for latent morphology
interpretation.

PCA was treated as an orthogonal descriptive basis rather than as evidence of
semantic or causal independence.

---

## 3.9 Nonlinear latent-model and geometry analyses

Nonlinear latent alternatives were evaluated against PCA under the same
garment-identity-disjoint validation framework.

Separately, nonlinear geometry was characterized using the frozen manifold and
sensitivity analyses, including Isomap-oriented geometry, principal-curve
analysis and stability assessment, and diffusion-map analysis.

Geometry characterization was not used to replace PCA unless a stable validated
alternative representation was established.

---

## 3.10 PCA morphology perturbation

A one-score-standard-deviation displacement for component \(j\) was defined in
standardized coordinates as

\[
\sqrt{\lambda_j}v_j.
\]

Mapping to original hybrid units gave

\[
\Delta x_j
=
D_\sigma
[
\sqrt{\lambda_j}v_j
].
\]

The exact inverse representation produced

\[
\Delta F_j(r,k).
\]

Sign-invariant morphology energy was defined as

\[
E_j(r,k)
=
|\Delta F_j(r,k)|^2.
\]

Normalization gave

\[
p_j(r,k)
=
\frac{E_j(r,k)}
{\sum_r\sum_kE_j(r,k)}.
\]

---

## 3.11 Radial-harmonic localization

Radial space was divided into:

\[
R_{\mathrm{inner}}=1{:}24,
\]

\[
R_{\mathrm{middle}}=25{:}48,
\]

\[
R_{\mathrm{outer}}=49{:}72.
\]

For radial region \(R\) and harmonic band \(B\),

\[
P_j(R,B)
=
\sum_{r\in R}
\sum_{k\in B}
p_j(r,k).
\]

If \(\eta_j\) denotes PCA explained-variance ratio,

\[
w_j
=
\frac{\eta_j}
{\sum_{\ell=1}^{64}\eta_\ell}.
\]

Variance-weighted localization was

\[
\bar P(R,B)
=
\sum_{j=1}^{64}
w_jP_j(R,B).
\]

These quantities describe only the retained PCA-64 subspace.

---

# 4. Results

## 4.1 Radial compression differed across harmonic bands

For \(k=1{:}4\), the four-coefficient DCT representation produced

\[
\Delta=0.059306,
\]

with bootstrap 95% CI

\[
[0.023295,\ 0.108196]
\]

and

\[
p_{\mathrm{FWER}}=0.000200.
\]

Compression was supported.

For \(k=5{:}12\), the tested compact wavelet representation produced

\[
\Delta=0.005984,
\]

95% CI

\[
[-0.014164,\ 0.060361],
\]

with

\[
p_{\mathrm{FWER}}=0.608939.
\]

Compression was not supported.

For \(k=13{:}24\),

\[
\Delta=0.010959,
\]

95% CI

\[
[-0.003088,\ 0.073320],
\]

and

\[
p_{\mathrm{FWER}}=0.487751.
\]

Compression was again not supported.

For \(k=25{:}36\), the four-coefficient db4-wavelet representation produced

\[
\Delta=0.039300,
\]

95% CI

\[
[0.019130,\ 0.091021],
\]

with

\[
p_{\mathrm{FWER}}=0.019698.
\]

Compression was supported.

### Table 1. Harmonic-dependent radial representation inference

| Harmonic band | Representation evaluated | Effect | Bootstrap 95% CI | \(p_{\mathrm{FWER}}\) | Frozen decision |
|---|---|---:|---:|---:|---|
| \(1{:}4\) | DCT, \(B=4\) | 0.059306 | [0.023295, 0.108196] | 0.000200 | DCT\(_4\) |
| \(5{:}12\) | Wavelet \(B=4\) | 0.005984 | [-0.014164, 0.060361] | 0.608939 | RAW\(_{72}\) |
| \(13{:}24\) | Wavelet \(B=4\) | 0.010959 | [-0.003088, 0.073320] | 0.487751 | RAW\(_{72}\) |
| \(25{:}36\) | db4 wavelet, \(B=4\) | 0.039300 | [0.019130, 0.091021] | 0.019698 | db4\(_4\) |

**[FIGURE 1 NEAR HERE — harmonic-band compression inference]**

---

## 4.2 Hybrid representation reduced coefficient count by 41.98%

The evidence-selected representation contained

\[
1504
\]

complex coefficients compared with

\[
2592
\]

in the complete radial-harmonic field.

This corresponds to a

\[
41.98\%
\]

coefficient reduction and approximately

\[
1.7234\times
\]

compression.

After exact real packing, each sketch was represented by 3008 real dimensions.

**[FIGURE 2 NEAR HERE — full versus hybrid representation architecture]**

---

## 4.3 Nonlinear models did not establish superiority over PCA

The tested nonlinear latent models did not establish a multiplicity-controlled
task advantage over PCA.

PCA was therefore retained as the practical latent representation.

Separate geometric audits nevertheless identified departures from a purely
linear geometric description.

Principal-curve analysis did not establish a stable one-dimensional trajectory,
and diffusion-map analysis did not provide sufficient evidence to replace PCA.

Thus, nonlinear geometry was detectable without establishing a validated
nonlinear replacement representation.

---

## 4.4 PCA-64 retained 44.65% of standardized variance

The first 64 principal components accounted for

\[
44.65\%
\]

of standardized representation variance.

All subsequent morphology-localization results therefore refer specifically to
this retained subspace.

---

## 4.5 Retained morphology was concentrated in intermediate harmonics

After exact inverse mapping of PCA perturbations,

\[
78.54\%
\]

of variance-weighted mapped morphology energy occurred at

\[
k=5{:}24.
\]

The complementary low and highest harmonic bands together contained 21.46%.

---

## 4.6 Retained morphology showed strong outer-radial localization

Across radial position,

\[
66.84\%
\]

of variance-weighted mapped morphology energy occurred in the outer radial zone.

The remaining energy was distributed across the inner and middle zones.

---

## 4.7 Joint radial-harmonic localization

Joint localization showed that

\[
51.30\%
\]

of retained variance-weighted mapped morphology energy occurred within the

\[
\text{outer radial}
\times
k=5{:}24
\]

region.

This is a descriptive joint localization quantity and was not tested as a
statistical interaction.

**[FIGURE 3 NEAR HERE — variance-weighted radial × harmonic localization]**

**[FIGURE 4 NEAR HERE — PC-specific morphology maps]**

---

# 5. Discussion

The principal finding is that radial representation requirements differed across
angular harmonic scale.

A uniform radial encoding was not supported by the present evidence. Instead,
compact representations were supported at the low and highest tested harmonic
ranges, while the intermediate ranges retained their complete radial structure.

This produced the heterogeneous representation

\[
\mathrm{DCT}_4/
\mathrm{RAW}_{72}/
\mathrm{RAW}_{72}/
\mathrm{db4}_4.
\]

Importantly, the unsupported intermediate compression results are part of the
representation evidence rather than failed experiments.

The selection rule was

\[
\boxed{
\text{compress where supported; preserve otherwise}.
}
\]

The results also argue against a simple interpretation in which low harmonic
orders correspond to useful signal and progressively higher orders correspond to
noise.

Within the retained PCA-64 subspace, most mapped morphology energy occurred at
intermediate harmonic orders, despite compact representation being supported at
both ends of the tested harmonic range.

The type of compact representation also differed. Low harmonic radial structure
supported a compact DCT basis, whereas the highest tested range supported a
compact db4-wavelet basis.

This is consistent with different forms of radial organization across angular
scale, although the present analysis does not establish a unique physical
mechanism for either transform preference.

A second important result is the separation between nonlinear geometry and
nonlinear-model utility.

The morphology representation showed nonlinear geometric structure, but the
tested nonlinear latent models did not establish a multiplicity-controlled task
advantage over PCA.

Thus,

\[
\text{nonlinear geometry}
\neq
\text{validated nonlinear-model superiority}.
\]

PCA remained useful because it provided a stable, interpretable, and exactly
invertible practical latent basis under the present evaluation framework, not
because the morphology space was assumed to be globally linear.

Mapping PCA perturbations back into \(F_k(r)\) additionally showed that retained
latent variation was strongly organized across both angular harmonic order and
radial position.

However, radial localization remains a representation-space property.

In particular,

\[
\text{outer radial}
\neq
\text{semantic garment boundary}.
\]

Similarly, PCA axes were not demonstrated to correspond directly to sleeves,
necklines, hems, drape, fit, or other garment attributes.

The 51.30% outer-radial × intermediate-harmonic localization is also descriptive
rather than evidence of statistical interaction.

---

## 5.1 Limitations

First, the findings were established within CLO-SKET and require independent
replication before being treated as general properties of garment-sketch
morphology.

Second, compression conclusions are conditional on the tested representation
families and coefficient budgets. Failure to support intermediate-band
compression does not establish mathematical incompressibility.

Third, PCA-64 retained 44.65% of standardized representation variance.
Morphology-localization percentages therefore characterize only this retained
subspace and not total garment morphology.

Fourth, the radial zones were equal-shell representation partitions rather than
semantic garment regions.

Fifth, PCA axes lack independently validated semantic garment labels.

Finally, the nonlinear negative results apply to the tested models,
hyperparameter ranges, sample size, validation framework, and downstream
objectives and should not be interpreted as a general rejection of nonlinear
representation learning.

---

## 5.2 Future work

Future work should test whether harmonic-conditioned radial representation
replicates on independent garment-sketch datasets.

Semantic and spatial annotation could determine whether specific radial-harmonic
structures correspond reproducibly to garment components or attributes.

The candidate representation family could also be expanded while preserving the
same inferential selection principle.

Larger datasets would permit stronger tests of nonlinear latent representations
and manifold structure.

Finally, the exact mapping

\[
PC_j
\rightarrow
\Delta F_j(r,k)
\]

provides a foundation for controlled morphology perturbation experiments in which
selected radial-harmonic structures could be manipulated and evaluated for
predictable semantic or generative effects.

---

# 6. Conclusion

This study investigated whether radial representation requirements in
garment-sketch Fourier morphology remain constant across angular harmonic scale.

They did not.

Under garment-identity-disjoint, multiplicity-controlled inference, compact
radial representations were supported for the low and highest tested harmonic
ranges, while full radial structure was preserved across the intermediate
harmonics.

The resulting evidence-selected

\[
\mathrm{DCT}_4/
\mathrm{RAW}_{72}/
\mathrm{RAW}_{72}/
\mathrm{db4}_4
\]

representation reduced the spectral coefficient count by 41.98% without imposing
uniform compression across the Fourier field.

Nonlinear geometric structure was detectable, but the tested nonlinear latent
models did not establish a validated task advantage over PCA. PCA consequently
remained the practical latent basis while retaining exact traceability to the
original radial-harmonic representation.

Within the retained PCA-64 subspace, mapped morphology variation was concentrated
predominantly at intermediate angular harmonics and outer radial positions.

Together, these findings support a representation principle in which radial and
angular spectral structure are considered jointly and dimensional reduction is
applied conditionally on evidence rather than imposed uniformly across
morphology space.

---

# 7. Figure Plan

## Figure 1 — Harmonic-dependent compression inference

Show the four harmonic bands with:

- observed effect;
- bootstrap confidence interval;
- FWER-supported / unsupported decision;
- final radial representation.

Scientific purpose:

\[
\boxed{
\text{establish the primary inferential result}
}
\]

---

## Figure 2 — Evidence-selected representation architecture

Show:

\[
P(\theta\mid r)
\rightarrow
F_k(r)
\]

followed by:

\[
1{:}4\rightarrow DCT_4
\]

\[
5{:}12\rightarrow RAW_{72}
\]

\[
13{:}24\rightarrow RAW_{72}
\]

\[
25{:}36\rightarrow db4_4
\]

and finally:

\[
2592
\rightarrow
1504
\text{ complex coefficients}.
\]

Scientific purpose:

\[
\boxed{
\text{make the representation immediately understandable}
}
\]

---

## Figure 3 — Variance-weighted radial-harmonic localization

Display the frozen

\[
\bar P(R,B)
\]

radial-zone × harmonic-band matrix.

Highlight descriptively, not inferentially:

- intermediate harmonics: 78.54%;
- outer radial: 66.84%;
- outer × intermediate: 51.30%.

---

## Figure 4 — PC-specific radial-harmonic morphology

Display selected frozen PCA morphology maps from the existing interpretation
objects.

Scientific purpose:

show that individual latent directions contain heterogeneous radial-harmonic
organization despite the retained-subspace aggregate pattern.

---

# 8. Table Plan

## Table 1

Primary harmonic-band compression inference.

Already included in Results.

## Table 2

Optional representation dimensionality table:

| Block | Harmonics | Radial encoding | Complex dimensions |
|---|---:|---|---:|
| Low | 1–4 | DCT-4 | 16 |
| Mid | 5–12 | RAW-72 | 576 |
| High-mid | 13–24 | RAW-72 | 864 |
| High | 25–36 | db4 wavelet-4 | 48 |
| **Total** | **1–36** | **Hybrid** | **1504** |

---

# 9. Citation Completion

Before submission, replace all `[CITATIONS]` placeholders using the verified
literature ledger.

At minimum the bibliography should cover:

1. classical Fourier shape descriptors;
2. Generic Fourier Descriptor;
3. Angular Radial Transform / MPEG-7 region shape representation;
4. multiscale Fourier-wavelet shape descriptors;
5. PCA;
6. nonlinear dimensionality reduction / manifold methods used in the study;
7. bootstrap and permutation methodology where journal conventions require;
8. family-wise error / max-statistic inference where appropriate.

No citation should be added merely to create an appearance of literature breadth.

Every reference should support the specific sentence to which it is attached.

---

# 10. Final Claim Firewall

## Primary supported claim

\[
\boxed{
\text{radial representation requirements differed across angular harmonic scale}
}
\]

under the tested CLO-SKET validation framework.

## Methodological principle

\[
\boxed{
\text{compress where supported; preserve otherwise}
}
\]

## Geometry conclusion

\[
\boxed{
\text{nonlinear geometry does not imply nonlinear-model superiority}
}
\]

## Interpretation scope

\[
\boxed{
\text{PCA morphology percentages refer only to PCA}_{64}
}
\]

## Semantic boundary

\[
\boxed{
(r,k,PC)
\neq
\text{semantic garment attributes without independent validation}
}
\]

---

# 11. Final Manuscript Evidence Chain

\[
P(\theta\mid r)
\]

\[
\downarrow
\]

\[
F_k(r)
\]

\[
\downarrow
\]

\[
\text{harmonic-conditioned compression inference}
\]

\[
\downarrow
\]

\[
DCT_4/RAW_{72}/RAW_{72}/db4_4
\]

\[
\downarrow
\]

\[
2592\rightarrow1504
\]

\[
\downarrow
\]

\[
x_i\in\mathbb R^{3008}
\]

\[
\downarrow
\]

\[
PCA_{64}
\]

\[
\downarrow
\]

\[
\Delta F_j(r,k)
\]

\[
\downarrow
\]

\[
E_j(r,k)
\]

\[
\downarrow
\]

\[
\bar P(R,B).
\]

---

# STEP 13 LOCK

\[
\boxed{
\textbf{PAPER 2 — SCIENTIFIC MANUSCRIPT ASSEMBLED}
}
\]

No new representation experiment is required for manuscript assembly.

The next stage is:

\[
\boxed{
\textbf{STEP 14 — SUBMISSION READINESS AUDIT}
}
\]

Step 14 should verify:

- every number against the frozen evidence ledger;
- every equation against the mathematical contract;
- every figure against its frozen source object;
- every literature claim against the cited paper;
- terminology consistency;
- train/test identity-disjoint wording;
- statistical reporting;
- claim strength;
- abstract/body consistency;
- figure/table numbering;
- supplementary-material requirements;
- reproducibility information.

Only after that audit should the manuscript be formatted for a target journal.