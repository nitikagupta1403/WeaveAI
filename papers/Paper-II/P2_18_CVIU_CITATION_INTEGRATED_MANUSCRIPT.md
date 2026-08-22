# Evidence-Controlled Radial-Spectral Shape Representation for Garment Sketches

## Abstract

Compact spectral shape representations often impose a common encoding rule
across the transform domain, although representation requirements may vary
across spatial and harmonic scales. We investigate this question for garment
sketch morphology using a conditional radial-angular probability representation
\(P_i(\theta\mid r)\), whose angular Fourier transform yields radial harmonic
functions

\[
F_{i,k}(r),
\qquad
k=1,\ldots,36.
\]

Using 2,300 sketches from 230 garment identities across 23 categories, candidate
radial representations were evaluated separately across four angular harmonic
bands under garment-identity-disjoint validation with family-wise-error-rate-
controlled inference. Four-coefficient DCT compression was supported for
\(k=1{:}4\), while four-coefficient db4-wavelet compression was supported for
\(k=25{:}36\). Compression was not supported for the intermediate
\(k=5{:}24\) harmonics, whose complete 72-shell radial structure was retained.

The resulting heterogeneous DCT/raw/raw/wavelet representation reduced the
spectral field from 2,592 to 1,504 complex coefficients per sketch, corresponding
to a 41.98% coefficient reduction. Tested nonlinear latent models did not
establish a multiplicity-controlled task advantage over PCA, although separate
geometric audits identified nonlinear structure that did not establish a stable
replacement representation.

The first 64 principal components retained 44.65% of standardized representation
variance. Within this retained subspace, 78.54% of variance-weighted mapped
morphology energy occurred at intermediate harmonic orders \(k=5{:}24\),
66.84% occurred in the outer radial zone, and 51.30% occurred jointly in the
outer-radial × intermediate-harmonic region.

These results support a representation-selection principle in which radial
encoding is conditioned on angular harmonic scale and compression is retained
only where supported by held-out evidence.

**Keywords:** shape representation; Fourier shape analysis; radial-angular
representation; spectral dimensionality reduction; statistical representation
selection; garment sketches

---

# 1. Introduction

Shape representations must balance compactness against preservation of
geometrically informative structure. Global spectral descriptors can summarize
shape efficiently, but compression may obscure where particular structures occur.
Fully resolved spatial descriptions preserve localization but can produce
high-dimensional representations containing substantial redundancy.

This tension has motivated a long history of Fourier-based shape analysis.
Classical Fourier descriptors represent closed contours through harmonic
coefficients and provide reconstructable spectral descriptions of shape
(Zahn and Roskies, 1972; Kuhl and Giardina, 1982). Fourier-derived shape
variables have also been used as inputs to multivariate morphology analysis
(Rohlf and Archie, 1984).

Polar formulations extend spectral analysis by representing radial and angular
organization explicitly. The Generic Fourier Descriptor applies a
two-dimensional Fourier transform to a polar-raster representation of shape
(Zhang and Lu, 2002). Angular Radial Transform methods similarly construct
compact descriptors using radial and angular basis functions
(Ricard et al., 2005), while Polar Harmonic Transforms provide orthogonal
radial-angular harmonic representations for invariant image analysis
(Yap et al., 2010).

These developments establish that radial-angular spectral shape representation
is itself well precedented. They leave a different question open, however:
whether the radial encoding applied to a spectral shape field should remain
uniform across angular harmonic scale.

This question matters because regularity of a representation does not imply
regularity of the information it represents. Radial structure associated with
one angular harmonic range may admit compact approximation, whereas another
range may require substantially greater radial resolution. A single global
compression rule can therefore either preserve unnecessary coefficients in some
spectral regions or remove useful structure in others.

Multiscale and wavelet-based shape descriptors provide an alternative mechanism
for accommodating localized structure. Fourier and wavelet transforms have
previously been combined in multiscale descriptors (Kunttu et al., 2006), and
a Wavelet Fourier Descriptor has been used specifically for fashion-flat sketch
classification (An and Li, 2014). Accordingly, the contribution of the present
study is not the combination of Fourier and wavelet methods.

Instead, we treat radial encoding as an empirically testable representation
choice conditional on angular harmonic scale.

For sketch \(i\), angular morphology conditional on radial location is represented
as

\[
P_i(\theta\mid r),
\]

and angular Fourier transformation is applied independently at each radius:

\[
F_{i,k}(r)
=
\sum_{\theta}
P_i(\theta\mid r)
e^{-ik\theta}.
\]

Each angular harmonic therefore remains a radial function,

\[
F_{i,k}:r\mapsto\mathbb C,
\]

rather than being immediately collapsed into a global coefficient.

This formulation makes it possible to ask

\[
\boxed{
\text{Does the appropriate radial representation of }F_k(r)
\text{ depend on angular harmonic scale }k?
}
\]

We address this question by evaluating candidate radial representations separately
across prespecified harmonic bands. Representation decisions are tested using
complete held-out garment identities, and simultaneous inference is controlled
across confirmatory compression comparisons.

The resulting methodological rule is deliberately conservative:

\[
\boxed{
\text{compress where supported; preserve where support is absent}.
}
\]

After freezing the resulting hybrid spectral representation, we separately
evaluate two further questions. First, we test whether nonlinear latent models
establish a validated task advantage over principal-component analysis (PCA).
Second, we characterize nonlinear geometry independently using established
manifold-oriented methods including Isomap (Tenenbaum et al., 2000), principal
curves (Hastie and Stuetzle, 1989), and diffusion maps
(Coifman and Lafon, 2006).

Finally, retained PCA directions are mapped exactly back through the frozen
spectral representation so that latent variation can be localized directly in
radial-harmonic coordinates.

The study therefore addresses four research questions:

1. **RQ1:** Does support for radial compression differ across angular harmonic
   scale?
2. **RQ2:** Can harmonic-conditioned selection produce a lower-dimensional
   hybrid spectral representation while preserving complete radial structure
   where compression is unsupported?
3. **RQ3:** Does detectable nonlinear geometry imply that a nonlinear latent
   representation should replace PCA under garment-identity-disjoint validation?
4. **RQ4:** Where is variation within the retained PCA subspace localized across
   radial position and angular harmonic order?

The methodological contribution is not a new spectral transform. It is an
evidence-controlled strategy for deciding how different angular harmonic ranges
should be represented radially.

---

# 2. Related Work

## 2.1 Fourier shape representation

Fourier descriptors are among the earliest spectral approaches to computational
shape representation. Zahn and Roskies (1972) represented plane closed curves
through Fourier coefficients of a parametric contour description. Kuhl and
Giardina (1982) subsequently developed elliptic Fourier descriptors that permit
normalized reconstruction of closed contours.

Such representations established that harmonic coefficients can provide compact,
reconstructable descriptions of shape. Fourier-derived descriptors have also been
used in multivariate morphology studies, including comparisons of alternative
Fourier descriptions of biological outlines (Rohlf and Archie, 1984).

The present work builds on this spectral tradition but does not collapse the
radial coordinate after angular transformation. Instead, each angular harmonic
is retained as a radial function \(F_k(r)\).

---

## 2.2 Polar Fourier and radial-angular representations

Polar shape analysis has long provided mechanisms for expressing radial and
angular structure jointly.

Zhang and Lu (2002) introduced the Generic Fourier Descriptor, which applies a
two-dimensional Fourier transform to a polar-raster representation of shape.
The method explicitly incorporates radial and circular spectral information.

The Angular Radial Transform provides another established polar representation.
ART constructs compact region descriptors using radial and angular basis
functions and forms part of the MPEG-7 region-shape framework
(Ricard et al., 2005). Subsequent ART methods have additionally exploited
coefficient magnitude and phase information (Lee and Kim, 2012).

Polar Harmonic Transforms further establish precedent for explicit orthogonal
radial-angular harmonic representations (Yap et al., 2010).

These methods are important novelty boundaries for the present study.
Radial-angular harmonic representation is therefore not claimed as a new idea.

The distinction here is representational rather than transformational:
instead of prescribing a single analytical radial basis throughout the spectral
domain, we retain \(F_k(r)\) explicitly and test whether its radial encoding
should vary across angular harmonic ranges.

---

## 2.3 Multiscale and wavelet shape descriptors

Global spectral bases can be complemented by localized or multiresolution
representations. Kunttu et al. (2006), for example, developed multiscale Fourier
descriptors in which Fourier analysis is combined with wavelet-based
multiresolution structure.

Fourier-wavelet integration has also appeared directly in the fashion-sketch
domain. An and Li (2014) used a Wavelet Fourier Descriptor as part of a
classification pipeline for fashion-flat sketches.

These studies establish that combining Fourier and wavelet representations is
not itself novel.

The present framework differs in how the basis is assigned. Wavelet
representation is treated as one candidate radial encoding rather than a
universal descriptor. It is retained only for harmonic ranges where the
corresponding compression is supported by the frozen inferential procedure.

Similarly, compact DCT representation is not imposed globally.

---

## 2.4 Fashion-sketch representation

Fashion sketches have been used for classification, retrieval, and computational
garment analysis. Of particular relevance to the present work, An and Li (2014)
showed that Fourier-wavelet features can be used for fashion-flat sketch
classification.

The CLO-SKET dataset provides a complementary setting for morphology analysis.
Its public record contains 2,300 sketches derived from 230 clothing
photographs/design instances distributed over 23 subcategories
(Arnia, 2020).

The repeated sketch structure is useful for the present methodological question
because representation decisions can be evaluated using complete garment
identities rather than random sketch-level partitions.

The present objective is therefore not to develop another sketch classifier.
It is to study the structure and defensible reduction of an explicit
radial-angular morphology representation.

---

## 2.5 Linear and nonlinear latent shape representations

Fourier descriptors have long been combined with multivariate analyses of
morphological variation (Rohlf and Archie, 1984). PCA provides a particularly
useful linear reference because it supplies orthogonal directions ordered by
variance and permits direct inverse perturbation through an explicit
representation.

Nonlinear dimensionality-reduction methods address a different issue: whether
geometric relationships are poorly represented by a globally linear coordinate
system.

Isomap estimates nonlinear geometry through neighborhood-based geodesic
relationships (Tenenbaum et al., 2000). Principal curves provide smooth
one-dimensional nonlinear summaries through multidimensional data
(Hastie and Stuetzle, 1989). Diffusion maps construct multiscale coordinates from
diffusion processes defined over a data graph (Coifman and Lafon, 2006).

In the present study these methods are used to distinguish two questions:

\[
\text{Does nonlinear geometry exist?}
\]

and

\[
\text{Does a nonlinear representation improve validated task performance?}
\]

The two are evaluated separately.

---

## 2.6 Position of the present work

Existing literature establishes:

- classical Fourier shape description;
- polar Fourier descriptors;
- explicit radial-angular transforms;
- polar harmonic representations;
- wavelet-Fourier multiscale descriptors;
- fashion-specific Wavelet Fourier Descriptors;
- multivariate and nonlinear shape analysis.

The present contribution lies at a different level.

We evaluate radial representation separately across angular harmonic bands under

\[
\boxed{
\text{garment-identity-disjoint validation}
}
\]

and

\[
\boxed{
\text{multiplicity-controlled inference}.
}
\]

A compact radial encoding is retained only where it receives inferential support.
Where the tested compression is unsupported, complete radial structure is
preserved.

The resulting heterogeneous representation is subsequently interpreted through
an exact mapping from retained PCA directions back into radial-harmonic Fourier
space.

No literature-wide priority claim is made.

---

# 3. Methods

## 3.1 Dataset and analysis units

The analysis used the CLO-SKET dataset (Arnia, 2020), comprising 2,300 garment
sketches associated with 230 underlying garment identities across 23 categories.

The repeated sketches corresponding to the same underlying garment were treated
as belonging to a common garment identity.

Garment identity, rather than individual sketch, was used as the primary grouping
unit for validation and inferential resampling.

For every validation fold,

\[
G_{\mathrm{train}}
\cap
G_{\mathrm{test}}
=
\varnothing,
\]

where \(G_{\mathrm{train}}\) and \(G_{\mathrm{test}}\) denote the sets of garment
identities assigned to the respective partitions.

This design evaluates generalization to previously unseen garment identities
rather than to additional sketches of garments already represented during model
construction.

---

## 3.2 Probabilistic radial-angular representation

Each sketch was represented relative to a frozen radial-angular coordinate system.

Let \(r\) denote radial shell and \(\theta\) angular position.

For sketch \(i\), angular morphology at radial shell \(r\) was normalized to form

\[
P_i(\theta\mid r).
\]

For every occupied shell,

\[
P_i(\theta\mid r)\geq0
\]

and

\[
\sum_\theta P_i(\theta\mid r)=1.
\]

The representation used 72 radial shells.

Empty shells were preserved as structurally empty rather than being assigned an
artificial angular distribution.

---

## 3.3 Angular Fourier morphology

Angular morphology was transformed independently within each radial shell:

\[
F_{i,k}(r)
=
\sum_\theta
P_i(\theta\mid r)
\exp(-\mathrm{i}k\theta).
\]

Positive angular harmonic orders

\[
k=1,\ldots,36
\]

were retained.

Consequently, each harmonic remained explicitly resolved across radius:

\[
F_{i,k}:r\mapsto\mathbb C.
\]

The complete radial-harmonic field contained

\[
72\times36
=
2592
\]

complex coefficients per sketch.

---

## 3.4 Harmonic-band partition

The positive harmonic range was partitioned into four frozen bands:

\[
K_1=1{:}4,
\qquad
K_2=5{:}12,
\qquad
K_3=13{:}24,
\qquad
K_4=25{:}36.
\]

Radial representation was evaluated separately for these four ranges.

The bands were used as representation partitions and were not assigned semantic
garment interpretations.

---

## 3.5 Candidate radial representations

Candidate radial representations included:

1. the complete 72-shell radial field;
2. compact discrete-cosine-transform encodings;
3. compact wavelet encodings.

For compact candidates, a prescribed radial coefficient budget was retained.

These transforms were treated as alternative encodings of the radial dependence
of \(F_k(r)\), not as hypotheses that particular harmonic bands represented
signal, noise, or semantic garment regions.

---

## 3.6 Garment-identity-disjoint validation

Candidate representations were evaluated using grouped validation in which
complete garment identities were assigned to folds.

For every fold,

\[
|G_{\mathrm{train}}\cap G_{\mathrm{test}}|=0.
\]

Category structure was retained in the frozen evaluation design where required.

This grouped procedure prevents repeated sketches from the same underlying
garment from appearing in both model-construction and test partitions.

---

## 3.7 Compression inference

For each harmonic band, compact radial representation was evaluated relative to
the corresponding complete radial structure using the frozen task-oriented
criterion.

A category-balanced effect statistic summarized representation performance.

Sampling uncertainty was estimated with 5,000 bootstrap replicates using complete
garment identities as the resampling unit. Bootstrap methodology follows the
general resampling framework introduced by Efron (1979), while the clustered
garment-identity unit is specific to the present experimental design.

Permutation inference used 10,000 replicates under the frozen category-preserving
null design.

Because confirmatory representation comparisons were evaluated simultaneously,
family-wise error was controlled using the frozen max-statistic procedure.

A compact radial representation was retained only when its inferential result
survived the family-wise-error-rate criterion at

\[
\alpha=0.05.
\]

Failure to establish support for compression resulted in preservation of the full
radial representation.

It was not interpreted as proof of mathematical incompressibility.

---

## 3.8 Frozen hybrid radial-spectral representation

Application of the inferential selection procedure yielded

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

The hybrid complex representation for sketch \(i\) was

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

The four blocks contained

\[
4\times4=16,
\]

\[
8\times72=576,
\]

\[
12\times72=864,
\]

and

\[
12\times4=48
\]

complex coefficients.

Thus,

\[
16+576+864+48
=
1504
\]

complex coefficients were retained per sketch.

Relative to the original 2,592-coefficient field, this represents a 41.98%
reduction in coefficient count.

Coefficient reduction was not interpreted as removal of noise.

---

## 3.9 Exact complex-to-real representation

Each complex block \(A\) was packed independently using

\[
\rho(A)
=
[
\Re(\operatorname{vec}(A)),
\Im(\operatorname{vec}(A))
].
\]

The verified implementation used block-wise flattened real coefficients followed
by flattened imaginary coefficients.

The four packed blocks were concatenated to obtain

\[
x_i\in\mathbb R^{3008}.
\]

The complex-to-real lineage was verified numerically before latent
interpretation.

---

## 3.10 Standardization and principal-component analysis

Each real feature was standardized as

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

The first 64 principal components were retained for the frozen latent morphology
interpretation.

PCA was used as an orthogonal descriptive basis.

Orthogonality was not interpreted as semantic, physical, or causal independence
between garment attributes.

---

## 3.11 Nonlinear latent-model comparison and geometry audit

Nonlinear latent alternatives were compared with PCA under the same
garment-identity-disjoint validation framework.

This model-comparison analysis was kept separate from the geometric audit.

Nonlinear geometry was characterized using Isomap
(Tenenbaum et al., 2000), principal-curve analysis
(Hastie and Stuetzle, 1989), and diffusion maps
(Coifman and Lafon, 2006), together with the frozen stability and sensitivity
procedures.

These analyses were treated as geometric characterization rather than as a reason
to replace PCA unless a stable, validated alternative representation was
established.

---

## 3.12 PCA morphology perturbation

For PCA component \(j\), a one-score-standard-deviation displacement in
standardized feature coordinates is

\[
\sqrt{\lambda_j}v_j,
\]

where \(\lambda_j\) is the corresponding PCA eigenvalue.

Mapping this displacement into original hybrid feature units gives

\[
\Delta x_j
=
D_\sigma
\left[
\sqrt{\lambda_j}v_j
\right].
\]

The perturbation was then unpacked using the exact frozen representation lineage.

Inverse transformation consisted of:

- inverse DCT mapping for \(k=1{:}4\);
- identity radial mapping for \(k=5{:}12\);
- identity radial mapping for \(k=13{:}24\);
- inverse db4-wavelet mapping for \(k=25{:}36\).

This produced

\[
\Delta F_j(r,k).
\]

Because PCA eigenvector orientation is arbitrary, morphology energy was defined as

\[
E_j(r,k)
=
|\Delta F_j(r,k)|^2.
\]

This quantity is invariant to the transformation

\[
v_j\rightarrow-v_j.
\]

---

## 3.13 Radial-harmonic morphology localization

For each retained component,

\[
p_j(r,k)
=
\frac{E_j(r,k)}
{\sum_r\sum_k E_j(r,k)},
\]

so that

\[
\sum_r\sum_k p_j(r,k)=1.
\]

Radial space was divided into three equal-shell descriptive zones:

\[
R_{\mathrm{inner}}=1{:}24,
\]

\[
R_{\mathrm{middle}}=25{:}48,
\]

\[
R_{\mathrm{outer}}=49{:}72.
\]

The same four frozen harmonic bands used for representation inference were used
for morphology localization.

For radial region \(R\) and harmonic band \(B\),

\[
P_j(R,B)
=
\sum_{r\in R}
\sum_{k\in B}
p_j(r,k).
\]

Let \(\eta_j\) denote the explained-variance ratio of PCA component \(j\).

Within the retained PCA-64 subspace,

\[
w_j
=
\frac{\eta_j}
{\sum_{\ell=1}^{64}\eta_\ell},
\]

with

\[
\sum_{j=1}^{64}w_j=1.
\]

The final variance-weighted localization was

\[
\bar P(R,B)
=
\sum_{j=1}^{64}
w_jP_j(R,B).
\]

These quantities characterize morphology localization only within the retained
PCA-64 subspace.

They are not interpreted as fractions of total garment morphology.

---

# 4. Results

## 4.1 Radial compression support differed across angular harmonic bands

For the low harmonic band

\[
k=1{:}4,
\]

the four-coefficient DCT representation yielded a category-balanced effect of

\[
\Delta=0.059306,
\]

with bootstrap 95% confidence interval

\[
[0.023295,\ 0.108196].
\]

The result remained supported under family-wise-error-rate control:

\[
p_{\mathrm{FWER}}=0.000200.
\]

The frozen radial representation was therefore

\[
\boxed{\mathrm{DCT}_4}.
\]

For

\[
k=5{:}12,
\]

the tested four-coefficient wavelet representation yielded

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

Compression was not supported, and the full radial representation was retained:

\[
\boxed{\mathrm{RAW}_{72}}.
\]

For

\[
k=13{:}24,
\]

the corresponding tested compact representation yielded

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

Compression was again not supported:

\[
\boxed{\mathrm{RAW}_{72}}.
\]

For the highest tested harmonic range,

\[
k=25{:}36,
\]

the four-coefficient db4-wavelet representation yielded

\[
\Delta=0.039300,
\]

with bootstrap 95% confidence interval

\[
[0.019130,\ 0.091021]
\]

and

\[
p_{\mathrm{FWER}}=0.019698.
\]

The frozen representation was therefore

\[
\boxed{\mathrm{db4\ wavelet}_4}.
\]

Taken together,

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

was selected across the four harmonic ranges.

Thus, support for radial compression differed across angular harmonic scale.

### Table 1. Harmonic-dependent radial representation inference

| Harmonic band | Compact representation tested | Effect | Bootstrap 95% CI | \(p_{\mathrm{FWER}}\) | Frozen representation |
|---|---|---:|---:|---:|---|
| \(k=1{:}4\) | DCT, \(B=4\) | 0.059306 | [0.023295, 0.108196] | 0.000200 | DCT\(_4\) |
| \(k=5{:}12\) | Wavelet, \(B=4\) | 0.005984 | [-0.014164, 0.060361] | 0.608939 | RAW\(_{72}\) |
| \(k=13{:}24\) | Wavelet, \(B=4\) | 0.010959 | [-0.003088, 0.073320] | 0.487751 | RAW\(_{72}\) |
| \(k=25{:}36\) | db4 wavelet, \(B=4\) | 0.039300 | [0.019130, 0.091021] | 0.019698 | db4\(_4\) |

**[Figure 2 near here]**

---

## 4.2 The evidence-selected representation reduced coefficient count by 41.98%

The complete radial-harmonic field contained

\[
2592
\]

complex coefficients per sketch.

The frozen hybrid representation contained

\[
1504.
\]

Thus,

\[
2592\rightarrow1504
\]

corresponded to

\[
\boxed{41.98\%}
\]

coefficient reduction and a compression ratio of approximately

\[
\boxed{1.7234\times}.
\]

After exact real packing, each sketch was represented by

\[
3008
\]

real dimensions.

The reduction is a count of retained coefficients and is not interpreted as
removal of noise.

---

## 4.3 Tested nonlinear latent models did not establish an advantage over PCA

The nonlinear latent alternatives were compared with PCA under the frozen
garment-identity-disjoint framework.

The tested nonlinear models did not establish a multiplicity-controlled task
advantage over PCA.

PCA was therefore retained as the practical latent representation.

This result concerns validated model utility and does not establish that the
underlying representation geometry is globally linear.

---

## 4.4 Nonlinear geometry was detectable without a stable replacement representation

Separate geometric analyses identified departures from a purely linear
description.

However, the explored nonlinear embeddings did not establish a single stable
canonical nonlinear coordinate system.

Principal-curve analysis did not support a stable one-dimensional morphology
trajectory, and the corresponding stability analysis did not establish a
reproducible principal curve.

Diffusion-map analysis likewise did not provide sufficient evidence to replace
the PCA representation.

The nonlinear analyses were therefore retained as geometric characterization and
sensitivity evidence rather than used to redefine the frozen latent
representation.

---

## 4.5 PCA-64 retained 44.65% of standardized representation variance

The first 64 principal components accounted for

\[
\boxed{44.65\%}
\]

of standardized representation variance.

All morphology-localization results below refer specifically to variation within
this retained PCA-64 subspace.

---

## 4.6 Retained PCA morphology was concentrated in intermediate harmonic orders

After mapping the retained PCA perturbations back into the radial-harmonic domain,

\[
\boxed{78.54\%}
\]

of variance-weighted mapped morphology energy occurred in

\[
k=5{:}24.
\]

The complementary low and highest harmonic ranges together contained 21.46%.

Thus, within PCA-64, retained mapped morphology energy was predominantly
localized to intermediate angular harmonic orders.

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

The remaining energy was distributed across the inner and middle radial zones.

The outer radial zone is a representation-space partition and is not interpreted
as a semantic garment boundary.

---

## 4.8 Joint radial-harmonic localization

Joint localization showed that

\[
\boxed{51.30\%}
\]

of variance-weighted mapped morphology energy within PCA-64 occurred in the

\[
\text{outer radial}
\times
k=5{:}24
\]

region.

This quantity is descriptive.

No formal radial-zone × harmonic-band interaction hypothesis was tested.

Accordingly, the value is not interpreted as enrichment, synergy, or preferential
coupling.

---

## 4.9 Individual PCA directions showed heterogeneous radial-harmonic organization

Although the retained-subspace summary was dominated by intermediate harmonics
and outer radial structure, individual PCA directions displayed heterogeneous
localization.

Leading components were predominantly outer-radial, whereas later retained
directions included components with stronger inner-radial localization.

Integrated harmonic-band dominance and individual harmonic maxima also did not
always coincide.

Thus, PCA-64 contained multiple radial-harmonic modes of variation rather than a
single uniform morphology pattern.

No semantic labels were assigned to individual PCA directions.

---

# 5. Discussion

## 5.1 Radial representation requirements are harmonic-scale dependent

The principal finding is that radial representation could not be treated
uniformly across angular harmonic scale under the present validation framework.

Compact representation was supported for the low and highest tested harmonic
ranges, whereas tested compression was not supported for either intermediate
range.

The resulting representation was therefore heterogeneous:

\[
\boxed{
\mathrm{DCT}_4
/
\mathrm{RAW}_{72}
/
\mathrm{RAW}_{72}
/
\mathrm{db4}_4
}.
\]

This outcome differs conceptually from descriptor architectures that impose a
single analytical radial basis or a uniform multiscale construction throughout
the spectral domain.

Polar Fourier, ART, and Polar Harmonic Transform methods demonstrate that
radial-angular shape structure can be represented compactly
(Zhang and Lu, 2002; Ricard et al., 2005; Yap et al., 2010).

The present result concerns a different level of design: whether one radial
encoding should be imposed uniformly after the angular morphology field has been
constructed.

Our evidence does not support that uniform assumption for CLO-SKET.

---

## 5.2 Unsupported compression is an informative representation outcome

The intermediate harmonic results are central rather than incidental.

For both

\[
k=5{:}12
\]

and

\[
k=13{:}24,
\]

the tested compact representations did not survive the simultaneous inferential
criterion.

The response was therefore to retain the complete 72-shell radial functions.

This creates a different philosophy from dimensional reduction performed to meet
a predefined compactness target:

\[
\boxed{
\text{absence of compression support}
\Rightarrow
\text{preservation}.
}
\]

The negative compression findings consequently contribute directly to the
architecture of the representation.

They do not establish that intermediate harmonics are mathematically
incompressible.

Other bases, coefficient budgets, or downstream objectives may support different
representations.

---

## 5.3 The spectral organization is not a simple low-signal/high-noise hierarchy

A common intuition is that low Fourier orders primarily represent meaningful
global shape while progressively higher orders increasingly represent negligible
detail or noise.

The current results do not support such a monotonic interpretation.

The highest tested harmonic range supported compact wavelet representation, while
the two intermediate bands retained complete radial resolution.

Moreover, within the retained PCA-64 subspace, most mapped morphology energy
occurred at intermediate harmonic orders.

Thus, neither compressibility nor retained latent morphology follows a simple
low-to-high signal/noise gradient.

A more appropriate description is that radial organization varies with angular
scale.

---

## 5.4 Different compact bases may reflect different radial organization

The two supported compact bands also preferred different representation families.

Low harmonics supported four DCT coefficients, whereas the highest tested range
supported four db4-wavelet coefficients.

A small cosine basis provides a compact global radial encoding, whereas wavelet
representations provide localized and multiscale structure.

Wavelet-Fourier combinations themselves are well established
(Kunttu et al., 2006), including in fashion-flat sketch analysis
(An and Li, 2014).

The present contribution is therefore not that a wavelet representation can be
combined with Fourier morphology.

Rather, wavelets emerged as the supported radial encoding only in one part of the
angular spectrum, while other parts retained different representations.

This pattern is consistent with harmonic-dependent radial organization, but the
analysis does not establish a unique physical mechanism underlying the basis
preferences.

---

## 5.5 The hybrid representation follows evidence rather than architectural symmetry

The final representation reduced coefficient count by 41.98%.

More important than this numerical reduction is how it was obtained.

The representation deliberately lacks symmetry across harmonic ranges.

It is not

\[
\mathrm{DCT/DCT/DCT/DCT}
\]

or

\[
\mathrm{WAV/WAV/WAV/WAV}.
\]

Instead,

\[
\boxed{
\text{compression is applied only where supported}.
}
\]

The coefficient reduction should therefore not be interpreted as the amount of
noise or irrelevant morphology removed from the sketches.

It is the dimensional consequence of the evidence-supported representation
decisions.

---

## 5.6 Nonlinear geometry and nonlinear-model utility are distinct

The nonlinear analyses yielded an important methodological distinction.

Geometric audits identified departures from a purely linear description, yet the
tested nonlinear latent models did not establish a multiplicity-controlled task
advantage over PCA.

These findings address different questions.

Isomap, principal curves, and diffusion maps provide tools for characterizing
nonlinear geometry (Tenenbaum et al., 2000; Hastie and Stuetzle, 1989;
Coifman and Lafon, 2006).

Detecting such geometry does not imply that a nonlinear latent model must improve
generalization for a particular task.

Conversely, failure to demonstrate nonlinear-model superiority does not prove
that the underlying morphology space is linear.

The two conclusions should therefore remain separate.

---

## 5.7 Why PCA remained the practical latent representation

PCA was retained because the tested nonlinear alternatives did not establish
sufficient validated advantage to justify replacing it.

Its role is pragmatic rather than ontological.

PCA provides:

- deterministic orthogonal coordinates;
- variance ordering;
- an exact inverse path through the frozen representation;
- straightforward perturbation analysis;
- a stable baseline for nonlinear comparison.

These properties made it useful for interpreting variation back in

\[
F_k(r).
\]

The conclusion is not

\[
\text{garment morphology is linear}.
\]

It is

\[
\boxed{
\text{PCA remained the validated practical latent basis}.
}
\]

---

## 5.8 No canonical one-dimensional nonlinear morphology trajectory was established

The geometry analyses also constrain stronger manifold interpretations.

Although nonlinear structure was detectable, principal-curve analysis did not
establish a stable one-dimensional morphology trajectory.

Diffusion geometry likewise did not provide a validated replacement
representation.

The current evidence therefore does not support describing CLO-SKET morphology as
lying along one unique nonlinear curve or canonical manifold.

Complex morphology can exhibit nonlinear local organization without admitting one
stable low-dimensional trajectory.

---

## 5.9 Exact inverse mapping preserves spectral interpretability

A useful property of the frozen representation is that retained PCA directions
can be traced exactly back into the spectral morphology domain.

For component \(j\),

\[
PC_j
\rightarrow
\Delta x_j
\rightarrow
\Delta F_j(r,k)
\rightarrow
E_j(r,k).
\]

This differs from assigning post hoc semantic labels to latent axes.

Instead, interpretation remains attached to mathematically defined radial and
harmonic coordinates.

PCA of Fourier-derived morphology has prior precedent in multivariate shape
analysis (Rohlf and Archie, 1984); the present analysis uses the exact inverse
hybrid mapping to determine where latent perturbation energy occurs across the
retained radial-harmonic field.

---

## 5.10 Intermediate harmonic structure dominates retained PCA morphology

Within PCA-64, 78.54% of variance-weighted mapped morphology energy occurred at

\[
k=5{:}24.
\]

This result is especially notable because the same broad intermediate harmonic
range was the range for which compact radial encoding was not supported.

The two findings are conceptually compatible with an important role for
radially resolved intermediate-harmonic structure.

However, they answer different questions.

The compression analysis asks whether tested radial reduction is supported.

The localization analysis asks where variation represented by PCA-64 is located.

The present study does not establish that intermediate harmonics resisted
compression *because* they contained most retained PCA morphology energy.

That would require a separate inferential test.

---

## 5.11 Retained latent morphology is strongly radially organized

Within PCA-64, 66.84% of mapped morphology energy occurred in the outer radial
zone.

More than half occurred jointly in outer radial positions and intermediate
harmonic orders.

These results show that retained latent variation is not radially homogeneous.

However,

\[
\boxed{
\text{outer radial}
\neq
\text{semantic garment boundary}.
}
\]

The radial zones are mathematical partitions of the representation.

No garment-part annotations were used.

The outer radial result therefore cannot automatically be interpreted as a
sleeve, hem, contour, silhouette, waist, or other semantic region.

---

## 5.12 Joint localization is not an interaction effect

The 51.30% outer-radial × intermediate-harmonic value is a joint localization
quantity.

No formal independence or interaction hypothesis was tested.

Accordingly, the value should not be interpreted as evidence of enrichment,
synergy, or preferential radial-harmonic coupling.

The supported statement is simply that more than half of the mapped morphology
energy within PCA-64 occupies that joint region.

---

## 5.13 The representation remains morphological rather than semantic

The present framework describes mathematical organization of sketch morphology.

It does not establish one-to-one semantic correspondence between

\[
r,
\qquad
k,
\qquad
PC_j
\]

and garment concepts.

Individual PCs were not shown to correspond specifically to sleeve structure,
neckline, waist, hem, drape, fit, or style.

Establishing such mappings will require independent semantic annotations or
controlled morphology perturbation experiments.

This distinction is important for future generative applications: mathematical
controllability of a representation does not automatically imply semantic
controllability.

---

## 5.14 Limitations

Several limitations constrain the interpretation of the findings.

First, the analysis was performed on CLO-SKET. Although its repeated garment
identities permit strong grouped validation, external replication is required
before the observed representation pattern can be treated as a general property
of garment sketches or broader shape classes.

Second, compression conclusions are conditional on the candidate radial
representations and coefficient budgets evaluated. Failure to support compact
representation for \(k=5{:}24\) does not establish mathematical
incompressibility.

Third, the first 64 principal components retained 44.65% of standardized
representation variance. The morphology-localization percentages therefore
characterize only the retained PCA-64 subspace and not total garment morphology.

Fourth, the radial zones were equal-shell representation partitions rather than
semantic garment regions.

Fifth, the PCA directions were not independently associated with semantic
attributes.

Sixth, the nonlinear negative findings are conditional on the tested model
families, hyperparameters, sample size, validation framework, and downstream
objective.

Finally, radial representation was selected using a task-oriented criterion.
Other objectives, such as pure reconstruction, semantic prediction, retrieval,
or generation, could favor different representation choices.

---

## 5.15 Future work

Independent datasets should first be used to test whether harmonic-conditioned
radial representation replicates beyond CLO-SKET.

A second direction is semantic annotation. Spatial garment-part or attribute
labels could determine whether reproducible relationships exist between
radial-harmonic localization and recognizable design components.

Third, candidate radial basis families could be expanded while retaining the same
inferential selection principle. This would test whether the intermediate bands
continue to favor full radial resolution when richer compact bases are available.

Larger datasets could additionally provide stronger tests of nonlinear latent
representations and manifold geometry.

Finally, the mapping

\[
PC_j
\rightarrow
\Delta F_j(r,k)
\]

provides a basis for controlled morphology interventions. Perturbations localized
to selected radial-harmonic regions could be tested for predictable changes in
reconstructed or generated garment sketches.

Such experiments would extend the present work from descriptive morphology
interpretation toward validated morphology control.

---

# 6. Conclusion

This study examined whether radial representation requirements remain constant
across angular harmonic scale in a probabilistic Fourier shape representation of
garment sketches.

They did not.

Under garment-identity-disjoint and multiplicity-controlled inference, compact
radial representations were supported for the low and highest tested harmonic
ranges, whereas complete radial structure was retained throughout the
intermediate harmonics.

The resulting

\[
\mathrm{DCT}_4/
\mathrm{RAW}_{72}/
\mathrm{RAW}_{72}/
\mathrm{db4}_4
\]

hybrid reduced the spectral representation from 2,592 to 1,504 complex
coefficients without imposing uniform compression across the Fourier field.

Separate latent analyses showed that nonlinear geometric structure can coexist
with the absence of a validated nonlinear-model advantage. PCA therefore
remained the practical latent basis without requiring an assumption that
morphology is globally linear.

Exact inverse mapping further showed that retained PCA variation is organized
strongly across both radial and angular-harmonic coordinates.

Together, these findings support a broader representation principle:

\[
\boxed{
\text{dimensional reduction should follow evidence rather than precede it}.
}
\]

For radial-angular spectral morphology, this means allowing different harmonic
ranges to retain different radial encodings—and preserving full structure where
the evidence does not justify compression.

---

# Data Availability

The CLO-SKET dataset used in this study is publicly available as:

Arnia, F. (2020). *Clo-Sket* (Version 1). Mendeley Data.

DOI: `10.17632/jt533nkhsf.1`

Derived representations, analysis code, and figure-generation scripts associated
with the present study will be linked to the accompanying research repository
when the submission release is frozen.

---

# Code Availability

The analysis repository will provide the implementation of:

- radial-angular probability construction;
- angular Fourier morphology;
- grouped radial-representation selection;
- bootstrap and permutation inference;
- hybrid representation construction;
- latent-model validation;
- PCA inverse morphology mapping;
- manuscript figure generation.

The release will include execution order, software-environment information,
random seeds, and provenance checks required to reproduce the reported results.

---

# References

An, L., & Li, W. (2014). An integrated approach to fashion flat sketches
classification. *International Journal of Clothing Science and Technology*,
26(5), 346–366.
https://doi.org/10.1108/IJCST-05-2013-0054

Arnia, F. (2020). *Clo-Sket* (Version 1) [Data set]. Mendeley Data.
https://doi.org/10.17632/jt533nkhsf.1

Coifman, R. R., & Lafon, S. (2006). Diffusion maps.
*Applied and Computational Harmonic Analysis*, 21(1), 5–30.
https://doi.org/10.1016/j.acha.2006.04.006

Efron, B. (1979). Bootstrap methods: Another look at the jackknife.
*The Annals of Statistics*, 7(1), 1–26.
https://doi.org/10.1214/aos/1176344552

Hastie, T., & Stuetzle, W. (1989). Principal curves.
*Journal of the American Statistical Association*, 84(406), 502–516.
https://doi.org/10.1080/01621459.1989.10478797

Kuhl, F. P., & Giardina, C. R. (1982). Elliptic Fourier features of a closed
contour. *Computer Graphics and Image Processing*, 18(3), 236–258.
https://doi.org/10.1016/0146-664X(82)90034-X

Kunttu, I., Lepistö, L., Rauhamaa, J., & Visa, A. (2006). Multiscale Fourier
descriptors for defect image retrieval. *Pattern Recognition Letters*, 27(2),
123–132.
https://doi.org/10.1016/j.patrec.2005.08.022

Lee, J.-M., & Kim, W.-Y. (2012). A new shape description method using angular
radial transform. *IEICE Transactions on Information and Systems*, E95-D(6),
1628–1635.
https://doi.org/10.1587/transinf.E95.D.1628

Ricard, J., Coeurjolly, D., & Baskurt, A. (2005). Generalizations of angular
radial transform for 2D and 3D shape retrieval. *Pattern Recognition Letters*,
26(14), 2174–2186.
https://doi.org/10.1016/j.patrec.2005.03.030

Rohlf, F. J., & Archie, J. W. (1984). A comparison of Fourier methods for the
description of wing shape in mosquitoes (Diptera: Culicidae).
*Systematic Zoology*, 33(3), 302–317.
https://doi.org/10.2307/2413076

Tenenbaum, J. B., de Silva, V., & Langford, J. C. (2000). A global geometric
framework for nonlinear dimensionality reduction. *Science*, 290(5500),
2319–2323.
https://doi.org/10.1126/science.290.5500.2319

Yap, P.-T., Jiang, X., & Kot, A. C. (2010). Two-dimensional polar harmonic
transforms for invariant image representation.
*IEEE Transactions on Pattern Analysis and Machine Intelligence*, 32(7),
1259–1270.
https://doi.org/10.1109/TPAMI.2009.119

Zahn, C. T., & Roskies, R. Z. (1972). Fourier descriptors for plane closed
curves. *IEEE Transactions on Computers*, C-21(3), 269–281.
https://doi.org/10.1109/TC.1972.5008949

Zhang, D., & Lu, G. (2002). Shape-based image retrieval using generic Fourier
descriptor. *Signal Processing: Image Communication*, 17(10), 825–848.
https://doi.org/10.1016/S0923-5965(02)00084-X