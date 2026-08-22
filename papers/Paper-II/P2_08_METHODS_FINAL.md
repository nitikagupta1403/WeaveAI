# CLO-SKET Paper 2 — Final Methods

## Status

**FINAL METHODS ASSEMBLY: READY FOR MANUSCRIPT INTEGRATION**

This Methods section is assembled from the frozen mathematical and computational contracts.

No new analysis is introduced here.

---

# 3. Methods

## 3.1 Dataset and analysis units

The analysis used 2,300 CLO-SKET garment sketches corresponding to 230 garment identities across 23 garment categories, with 10 garment identities represented within each category.

Garment identity, rather than individual sketch, was treated as the primary grouping unit for validation and statistical inference. This distinction is necessary because repeated sketches originating from the same garment identity cannot be treated as independent examples when evaluating representation generalization.

All grouped evaluation procedures therefore enforced complete garment-identity separation between training and test partitions.

For every validation fold,

\[
G_{\mathrm{train}}
\cap
G_{\mathrm{test}}
=
\varnothing,
\]

where \(G_{\mathrm{train}}\) and \(G_{\mathrm{test}}\) denote the sets of garment identities assigned to the respective partitions.

Category structure was retained where required by the frozen validation and inferential procedures.

---

## 3.2 Probabilistic radial-angular morphology representation

Each sketch was represented relative to a fixed radial-angular coordinate system centered on the sketch morphology.

Let

\[
r
\]

denote radial shell and

\[
\theta
\]

denote angular position.

For sketch \(i\), the angular morphology observed at radial shell \(r\) was normalized to define the conditional probability field

\[
P_i(\theta\mid r).
\]

For every occupied radial shell,

\[
P_i(\theta\mid r)\geq0,
\]

with normalization

\[
\sum_{\theta}
P_i(\theta\mid r)
=
1.
\]

The representation used 72 radial shells and 72 angular bins.

Radial shells containing no sketch morphology were retained as structurally empty rather than being assigned an artificial angular probability distribution.

The resulting field therefore provides a probability-normalized description of angular morphology conditional on radial location.

---

## 3.3 Angular Fourier morphology

Angular structure at each radial shell was transformed using the discrete Fourier representation

\[
F_{i,k}(r)
=
\sum_{\theta}
P_i(\theta\mid r)
\exp(-\mathrm{i}k\theta),
\]

where:

- \(i\) indexes sketches;
- \(r\) indexes radial shells;
- \(k\) denotes angular harmonic order.

The analysis retained positive harmonics

\[
k=1,\ldots,36.
\]

Thus, rather than collapsing the sketch into a single global Fourier descriptor, each harmonic remained an explicit function of radial location:

\[
r
\mapsto
F_{i,k}(r).
\]

This construction produced a full radial-harmonic field containing

\[
72\times36
=
2592
\]

complex coefficients per sketch.

---

## 3.4 Harmonic-band partition

To evaluate whether radial representation requirements depended on angular harmonic scale, the 36 retained positive harmonics were partitioned into four frozen bands:

\[
K_1 = 1{:}4,
\]

\[
K_2 = 5{:}12,
\]

\[
K_3 = 13{:}24,
\]

and

\[
K_4 = 25{:}36.
\]

The corresponding numbers of harmonics were

\[
4,\quad8,\quad12,\quad12,
\]

respectively.

Radial representation was evaluated separately within each band.

The purpose of this partition was not to assign semantic meaning to harmonic ranges, but to test whether one radial encoding strategy was supported uniformly across the Fourier field.

---

## 3.5 Candidate radial representations

For each harmonic band, the radial functions

\[
F_{i,k}(r)
\]

were evaluated under alternative radial representations.

The candidate representation families included:

1. full radial structure retained across all 72 shells;
2. compact discrete-cosine-transform representations;
3. compact wavelet representations.

For a compact radial representation, only a prescribed number \(B\) of radial coefficients was retained.

The candidate families were treated as alternative encodings of the radial dependence of the angular Fourier field rather than as assumptions about the intrinsic morphology of a harmonic band.

The representation finally retained for each band was determined by the frozen validation and inferential procedure described below.

---

## 3.6 Garment-identity-disjoint validation

Representation comparisons were conducted under grouped validation in which complete garment identities were assigned to folds.

For every fold,

\[
G_{\mathrm{train}}
\cap
G_{\mathrm{test}}
=
\varnothing.
\]

This prevents sketches originating from the same garment identity from appearing in both training and evaluation partitions.

Grouped validation therefore measures generalization to previously unseen garment identities rather than to additional sketches of garments already represented during model construction.

Where category-balanced evaluation was required, category structure was retained within the grouped validation design.

---

## 3.7 Compression evaluation and inferential selection

Candidate radial representations were compared using the frozen task-oriented evaluation procedure.

For each harmonic band, the performance of a compact radial representation was evaluated relative to the corresponding full radial structure under garment-identity-disjoint validation.

A category-balanced effect statistic was used to summarize the observed performance difference.

Uncertainty was estimated using bootstrap resampling at the complete garment-identity level.

The primary compression inference used

\[
5000
\]

bootstrap replicates.

To test whether the observed representation effects could arise under the relevant null structure, permutation inference was performed using

\[
10000
\]

replicates under the frozen category-preserving permutation design.

Because compression decisions were evaluated simultaneously across multiple harmonic bands, family-wise error was controlled using the frozen max-statistic procedure.

For harmonic band \(b\), let

\[
\Delta_b
\]

denote the observed category-balanced effect.

A compact representation was retained only when the corresponding inferential result survived the family-wise-error-rate criterion at

\[
\alpha=0.05.
\]

Failure to establish compression support was treated as a reason to preserve the complete radial representation rather than as evidence that the corresponding band contained no redundancy or no morphology.

---

## 3.8 Evidence-selected hybrid radial-spectral representation

Application of the inferential selection procedure produced the frozen radial encoding:

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

Accordingly, the hybrid complex representation for sketch \(i\) was

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

The four complex blocks contain:

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

complex coefficients, respectively.

The complete frozen representation therefore contains

\[
16+576+864+48
=
1504
\]

complex coefficients per sketch.

Relative to the original

\[
2592
\]

complex coefficients, this corresponds to

\[
41.98\%
\]

coefficient reduction and a compression ratio of approximately

\[
1.7234\times.
\]

This reduction is interpreted strictly as representation dimensionality reduction and not as removal of noise.

---

## 3.9 Exact complex-to-real representation

Each complex representation block was converted to real form independently.

For a complex block \(A\),

\[
\rho(A)
=
[
\Re(\operatorname{vec}(A)),
\Im(\operatorname{vec}(A))
].
\]

The four packed blocks were concatenated in the frozen order:

\[
\text{low}
\rightarrow
\text{mid}
\rightarrow
\text{high-mid}
\rightarrow
\text{high}.
\]

The exact verified packing convention was

\[
\boxed{
\texttt{BLOCK\_FLAT\_REAL\_THEN\_IMAG}
}.
\]

The resulting representation is

\[
x_i
\in
\mathbb R^{3008}.
\]

The real/complex lineage was verified numerically before latent-space interpretation.

---

## 3.10 Feature standardization

Each real representation coordinate was standardized before latent analysis.

For coordinate \(m\),

\[
\tilde{x}_{im}
=
\frac{x_{im}-\mu_m}{\sigma_m},
\]

where

\[
\mu_m
\]

and

\[
\sigma_m
\]

denote the empirical mean and standard deviation of feature \(m\).

Equivalently,

\[
\tilde{x}_i
=
D_\sigma^{-1}
(x_i-\mu),
\]

where

\[
D_\sigma
=
\operatorname{diag}
(\sigma_1,\ldots,\sigma_d)
\]

and

\[
d=3008.
\]

---

## 3.11 Principal-component representation

Principal-component analysis was applied to the standardized hybrid representation.

Let

\[
v_j
\]

denote loading vector \(j\), and let

\[
\lambda_j
\]

denote its associated eigenvalue.

For sketch \(i\), the score on principal component \(j\) is

\[
z_{ij}
=
v_j^\top
\tilde{x}_i.
\]

The PCA loading vectors satisfy

\[
v_j^\top v_l
=
\delta_{jl}.
\]

The first

\[
64
\]

principal components were retained for the final morphology interpretation.

PCA was treated as an orthogonal descriptive latent basis.

Orthogonality was not interpreted as semantic, physical, statistical, or causal independence between garment attributes.

---

## 3.12 Nonlinear latent-model comparison

PCA was evaluated against the frozen set of nonlinear latent alternatives under the same garment-identity-disjoint validation framework.

The purpose of this comparison was to test whether nonlinear latent representations established a reproducible downstream task advantage over the linear PCA baseline.

Model comparisons used the frozen primary performance metrics and multiplicity-controlled inference.

This analysis was distinct from the nonlinear geometry audit.

A nonlinear model could therefore fail to improve validated task performance even if the representation contained nonlinear geometric structure.

---

## 3.13 Nonlinear geometry characterization

The geometry of the frozen representation was examined using additional nonlinear analyses including:

- Isomap-based neighborhood geometry;
- principal-curve analysis;
- principal-curve stability analysis;
- diffusion-map sensitivity analysis.

These analyses were used to characterize departures from a purely linear latent geometry.

They were not used to redefine the frozen representation unless they established a validated and stable replacement for PCA.

The geometric analyses were therefore treated as characterization and sensitivity analyses rather than as a separate representation-selection stage.

---

## 3.14 PCA morphology perturbation

To interpret each retained PCA direction in the original radial-harmonic domain, a one-score-standard-deviation displacement was constructed.

For component \(j\), a one-standard-deviation movement in PCA score space is

\[
\sqrt{\lambda_j}v_j.
\]

Mapping this perturbation back to the original hybrid feature units gives

\[
\Delta x_j
=
D_\sigma
\left[
\sqrt{\lambda_j}v_j
\right].
\]

The perturbation

\[
\Delta x_j
\]

was then unpacked using the exact verified complex-to-real lineage.

The inverse hybrid transformation applied:

- inverse DCT reconstruction for \(k=1{:}4\);
- identity radial mapping for \(k=5{:}12\);
- identity radial mapping for \(k=13{:}24\);
- inverse db4-wavelet reconstruction for \(k=25{:}36\).

This produced

\[
\Delta F_j(r,k),
\]

the radial-angular Fourier perturbation associated with a one-score-standard-deviation movement along principal component \(j\).

---

## 3.15 Sign-invariant morphology energy

The orientation of a PCA eigenvector is arbitrary:

\[
v_j
\]

and

\[
-v_j
\]

represent the same principal axis.

Morphology interpretation was therefore based on squared complex perturbation magnitude:

\[
E_j(r,k)
=
|\Delta F_j(r,k)|^2.
\]

This quantity is invariant to PCA sign reversal.

For each retained component, morphology energy was normalized as

\[
p_j(r,k)
=
\frac{
E_j(r,k)
}{
\sum_r
\sum_k
E_j(r,k)
},
\]

such that

\[
\sum_r
\sum_k
p_j(r,k)
=
1.
\]

Thus,

\[
p_j(r,k)
\]

describes the relative localization of the morphology variation associated with PCA direction \(j\) across radial and harmonic coordinates.

---

## 3.16 Radial and harmonic localization

For descriptive interpretation, radial space was partitioned into three equal-shell zones:

\[
R_{\mathrm{inner}}
=
1{:}24,
\]

\[
R_{\mathrm{middle}}
=
25{:}48,
\]

and

\[
R_{\mathrm{outer}}
=
49{:}72.
\]

The harmonic field retained the same four frozen bands used during representation selection:

\[
1{:}4,
\]

\[
5{:}12,
\]

\[
13{:}24,
\]

and

\[
25{:}36.
\]

For radial region \(R\) and harmonic band \(B\), component-specific morphology localization was defined as

\[
P_j(R,B)
=
\sum_{r\in R}
\sum_{k\in B}
p_j(r,k).
\]

Marginal radial and harmonic localization followed by summing over the complementary coordinate.

The radial zones are representation-space partitions and were not interpreted as semantic garment regions.

---

## 3.17 Variance-weighted retained-subspace morphology

Let

\[
\eta_j
\]

denote the explained-variance ratio of PCA component \(j\).

Weights were normalized within the retained 64-component subspace:

\[
w_j
=
\frac{
\eta_j
}{
\sum_{\ell=1}^{64}
\eta_\ell
},
\]

with

\[
\sum_{j=1}^{64}
w_j
=
1.
\]

The variance-weighted morphology localization was defined as

\[
\bar{P}(R,B)
=
\sum_{j=1}^{64}
w_j
P_j(R,B).
\]

The quantity

\[
\bar{P}(R,B)
\]

therefore characterizes where variation represented by the retained PCA subspace is localized in radial-harmonic Fourier coordinates.

It does not constitute a decomposition of:

- the complete 3008-dimensional representation;
- total garment morphology;
- semantic garment parts;
- causal morphology factors.

---

## 3.18 Numerical and provenance audits

All frozen computational representations used for manuscript inference and interpretation were checked for numerical validity.

Required audits included:

\[
N_{\mathrm{NaN}}=0
\]

and

\[
N_{\mathrm{Inf}}=0
\]

for all primary real and complex representation objects.

The following lineage checks were additionally performed:

- exact sketch-order consistency;
- zero garment-identity overlap between grouped train/test folds;
- exact harmonic-band coverage;
- exact complex-to-real packing;
- reconstruction of frozen hybrid dimensions;
- normalization of PCA morphology energy;
- normalization of retained-PC variance weights;
- exact reproduction of final radial-harmonic localization quantities from the mathematical definitions.

These checks were used to ensure that the manuscript equations corresponded directly to the computational implementation.

---

# Methods claim boundary

The Methods establish the analysis procedure.

They do not by themselves establish that:

- low harmonics are signal;
- high harmonics are noise;
- intermediate harmonics are mathematically incompressible;
- outer radial regions correspond to garment boundaries;
- PCA axes correspond to semantic garment attributes;
- PCA describes complete garment morphology;
- nonlinear morphology is absent.

Those questions are constrained by the Results and Discussion evidence.

---

# Final mathematical pipeline

The complete Paper 2 analysis is:

\[
P_i(\theta\mid r)
\]

\[
\downarrow
\]

\[
F_{i,k}(r)
\]

\[
\downarrow
\]

\[
\text{harmonic-conditioned radial representation inference}
\]

\[
\downarrow
\]

\[
Z_i
\in
\mathbb C^{1504}
\]

\[
\downarrow
\]

\[
x_i
\in
\mathbb R^{3008}
\]

\[
\downarrow
\]

\[
\tilde{x}_i
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
\Delta x_j
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
|\Delta F_j(r,k)|^2
\]

\[
\downarrow
\]

\[
\bar P(R,B).
\]

---

# Step 8 lock

\[
\boxed{
\textbf{PAPER 2 FINAL METHODS — ASSEMBLED}
}
\]

Next:

\[
\boxed{
\textbf{STEP 9 — FINAL RESULTS ASSEMBLY}
}
\]

Results must use only frozen values from the Evidence Ledger and must distinguish inferential findings from descriptive morphology localization.