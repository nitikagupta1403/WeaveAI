# Garment-Sketch Morphology Radial-Spectral Representation: Evidence-Controlled Conditional Compression

**NITIKA GUPTA**

---

# Abstract

Garment-sketch morphology is distributed jointly across radial position and angular harmonic scale, yet spectral compression is often imposed uniformly across a representation. We represent each sketch by a shell-conditional angular distribution \(P_i(\theta\mid r)\), whose Fourier coefficients define complex radial functions \(F_{i,k}(r)\). Using 2,300 sketches from 230 recovered garment identities across 23 categories, candidate radial encodings were evaluated separately over four prespecified harmonic bands under garment-identity-disjoint validation and family-wise-error-rate-controlled inference. Four-coefficient DCT compression was supported for \(k=1{:}4\), and four-coefficient db4-wavelet compression for \(k=25{:}36\); compression was not supported for \(k=5{:}24\), for which the complete 72-shell radial representation was retained. The resulting DCT/raw/raw/wavelet representation reduced the field from 2,592 to 1,504 complex coefficients (41.98%). Across PCA, autoencoder, and variational-autoencoder comparisons, nonlinear models did not establish a multiplicity-controlled held-out task advantage over PCA. PCA-64 accounted for 44.65% of variance in the standardized frozen representation. Within this retained subspace, 78.54% of mapped morphology energy occurred at \(k=5{:}24\), 66.84% in the outer radial zone, and 51.30% jointly in the outer-radial × intermediate-harmonic region. These results support an evidence-controlled representation strategy in which radial compression is adopted where supported and complete radial structure is otherwise preserved.

---


---

# Keywords

garment sketch morphology; Fourier shape analysis; radial-angular representation; conditional spectral compression; evidence-controlled representation; garment-identity-disjoint validation

---


---

# 1. Introduction

Garment sketches encode morphology across both radial position and angular scale. A compact global descriptor can summarize shape efficiently, but complete collapse of spatial organization can obscure where geometric variation occurs. Conversely, retaining the full radial-angular field preserves localization at the cost of high dimensionality. The relevant representation question is therefore not simply how much morphology should be compressed, but **which parts of the representation can be compressed under held-out evidence**.

We represent sketch morphology in centroid-relative polar coordinates. For sketch \(i\), the angular distribution within radial shell \(r\) is written

\[
P_i(\theta\mid r),
\qquad
\sum_\theta P_i(\theta\mid r)=1,
\]

and its angular Fourier coefficients are evaluated independently at each radial location,

\[
F_{i,k}(r)
=
\sum_\theta P_i(\theta\mid r)e^{-ik\theta}.
\]

Thus, for each angular harmonic \(k\), the representation retains a complex radial function

\[
F_{i,k}:r\mapsto\mathbb C.
\]

Keeping \(r\) and \(k\) explicit makes it possible to test whether support for radial compression differs across angular harmonic bands rather than imposing one radial encoding on the complete Fourier field.

Classical Fourier descriptors provide longstanding precedent for spectral shape representation (Zahn and Roskies, 1972; Kuhl and Giardina, 1982). Polar Fourier and radial-angular methods further establish that radial and angular spectral organization can be represented jointly: the Generic Fourier Descriptor applies a two-dimensional Fourier transform to a polar-raster shape representation (Zhang and Lu, 2002), while the Angular Radial Transform is an established MPEG-7 region-shape descriptor (Ricard et al., 2005). Multiscale Fourier-wavelet descriptors likewise show that Fourier and multiresolution representations can be combined (Kunttu et al., 2006), including a Wavelet Fourier Descriptor developed specifically for fashion-flat sketch classification (An and Li, 2014). The present study therefore does not claim novelty for Fourier analysis, polar representation, DCT compression, wavelets, PCA, or their combination. Instead, it investigates an evidence-controlled representation-selection principle: candidate radial encodings are evaluated separately across prespecified angular harmonic bands under garment-identity-disjoint validation, and full radial structure is preserved whenever tested compression is not supported by multiplicity-controlled inference.

This principle deliberately allows a heterogeneous representation. A compact basis can be retained where supported without forcing the same transform or coefficient budget on harmonic bands for which the evidence does not justify compression. Negative compression results therefore contribute directly to representation construction rather than triggering an unrestricted search for a lower-dimensional alternative.

A second question concerns the geometry of the selected representation. Detecting nonlinear geometric structure does not imply that a nonlinear latent model improves held-out task performance. We therefore separate **geometric nonlinearity** from **nonlinear-model utility**: PCA provides the linear reference (Jolliffe and Cadima, 2016), while autoencoder and variational-autoencoder representations provide nonlinear alternatives (Hinton and Salakhutdinov, 2006; Kingma and Welling, 2014). Manifold-oriented analyses are treated separately as geometric diagnostics rather than as automatic evidence for replacing the validated task representation.

Finally, latent variation is mapped back to the original radial-harmonic coordinates. For PCA direction \(j\), a one-score-standard-deviation perturbation is reconstructed through the frozen representation,

\[
PC_j
\rightarrow
\Delta x_j
\rightarrow
\Delta F_j(r,k),
\]

and summarized by the sign-invariant morphology energy

\[
E_j(r,k)=|\Delta F_j(r,k)|^2.
\]

This permits localization of retained latent variation in \((r,k)\) space without assigning unsupported semantic labels to individual spectral or PCA coordinates.

Using 2,300 sketches representing 230 recovered garment identities across 23 categories, the study addresses four questions:

1. Does support for radial compression differ across the tested angular harmonic bands?
2. Can band-specific representation selection reduce dimensionality while preserving complete radial structure where tested compression is unsupported?
3. Do tested nonlinear latent representations establish a multiplicity-controlled held-out task advantage over PCA, independently of evidence for nonlinear geometry?
4. Where is variation within the retained PCA subspace localized across radial position and angular harmonic order?

**The primary contribution is to formulate compression of the structured radial-angular field \(F(r,k)\) as an inferential representation decision rather than a uniform descriptor-design choice.** For each prespecified angular-harmonic band, candidate radial encodings are selected using training identities and adopted only when their effect is supported on held-out garment identities under simultaneous inference; otherwise, the complete radial field is retained. The resulting representation can therefore be heterogeneous by construction, with compressed and uncompressed bands determined by evidence rather than a predetermined global coefficient budget. Two secondary safeguards preserve interpretability: nonlinear geometric structure is separated from validated nonlinear-model utility, and the selected latent representation retains an exact inverse path to radial-harmonic coordinates. The contribution is therefore not a new Fourier, cosine, wavelet, or PCA transform, but an evidence-controlled framework for deciding where a structured spectral representation may be compressed and where its original radial resolution should be preserved. Claims remain restricted to the tested candidate representations, validation criterion, dataset, and retained latent subspace.

---


---

# 2. Related Work

## 2.1 Fourier and polar shape representations

Fourier descriptors are established tools for contour- and region-based shape analysis, recognition, and retrieval. Early Fourier contour descriptions established compact harmonic representations of closed curves (Zahn and Roskies, 1972), while elliptic Fourier descriptors provided normalized reconstruction of closed contours (Kuhl and Giardina, 1982). Fourier-derived descriptors have also been used in multivariate morphology analysis (Rohlf and Archie, 1984). Their appeal lies in compact spectral representation and useful transformation properties under suitable normalization, but global descriptors can combine structures occurring at different spatial locations, motivating representations that retain additional spatial organization.

Polar spectral methods provide one such route. The Generic Fourier Descriptor introduced by Zhang and Lu (2002) applies a two-dimensional Fourier transform to a polar-raster representation so that radial and circular frequency information both contribute to region-based shape description. The Angular Radial Transform similarly uses basis functions defined jointly over radial and angular coordinates and forms part of the MPEG-7 region-shape framework (Ricard et al., 2005). Polar harmonic methods provide further precedent for explicit orthogonal radial-angular harmonic representations (Yap et al., 2010). These methods establish the value—and prior art—of explicit radial-angular spectral structure.

The present study asks a narrower question. Rather than fixing a single radial-angular basis for the complete descriptor, it retains each angular harmonic as the radial function \(F_k(r)\) and evaluates whether the radial encoding can be reduced differently across prespecified harmonic bands.

## 2.2 Multiscale and wavelet shape representations

Wavelet and multiscale Fourier descriptors address limitations of purely global spectral descriptions by introducing localized or scale-dependent structure. Kunttu et al. (2006) developed multiscale Fourier descriptors combining Fourier analysis with wavelet-based multiresolution structure. Fourier-wavelet integration also has direct precedent in the fashion domain: An and Li (2014) used a Wavelet Fourier Descriptor in a fashion-flat-sketch classification pipeline. Prior work therefore establishes that Fourier and wavelet representations can coexist productively within a shape-analysis system.

Our distinction lies in how the radial basis is assigned. A wavelet, cosine, or complete radial representation is not assumed to be appropriate across the full harmonic range. Candidate encodings are instead evaluated band by band under the same identity-disjoint validation and inferential framework. The selected representation may consequently contain compressed and uncompressed spectral regions simultaneously.

## 2.3 Compact descriptors and evidence-guided preservation

Classical descriptor design often emphasizes compactness because storage, matching, and retrieval efficiency are central objectives; compactness is an explicit motivation in established polar and multiscale shape descriptors (Zhang and Lu, 2002; Ricard et al., 2005; Kunttu et al., 2006). Here, dimensional reduction is subject to an additional requirement: a lower-dimensional radial representation is adopted only when its use is supported under the frozen held-out criterion.

Accordingly, failure to establish compression support is not treated as failure to construct a descriptor. It leads to preservation of the complete radial structure for that band. This design distinguishes evidence-guided representation selection from compression imposed primarily to meet a predetermined dimensionality target. It also does not imply that an unsupported band is intrinsically incompressible; conclusions remain conditional on the tested candidate family and coefficient budgets.

## 2.4 Linear and nonlinear latent representations

PCA provides an orthogonal, variance-ordered representation with a direct inverse map to the original feature coordinates (Jolliffe and Cadima, 2016). Autoencoders provide nonlinear low-dimensional codes learned through reconstruction (Hinton and Salakhutdinov, 2006), while variational autoencoders provide a probabilistic latent-variable formulation based on variational inference and the reparameterization estimator (Kingma and Welling, 2014). Manifold-oriented methods can characterize nonlinear geometry without necessarily defining a validated task representation; examples include principal curves (Hastie and Stuetzle, 1989), Isomap (Tenenbaum et al., 2000), and diffusion maps (Coifman and Lafon, 2006).

For morphology data, the existence of nonlinear geometry and the usefulness of a nonlinear latent model are distinct empirical questions. The present study therefore evaluates PCA and nonlinear latent alternatives under garment-identity-disjoint task validation while treating nonlinear geometry analyses separately. This prevents a nonlinear visualization or local geometric diagnostic from being interpreted automatically as evidence of superior held-out representation performance.

## 2.5 Position of the present study

The methodological components used here—Fourier shape analysis, polar representation, DCT and wavelet bases, PCA, and nonlinear latent models—are established (Zhang and Lu, 2002; Ricard et al., 2005; Kunttu et al., 2006; An and Li, 2014; Jolliffe and Cadima, 2016). The contribution lies in their integration around an evidence-controlled decision rule:

\[
\boxed{
\text{evaluate radial compression separately across angular harmonic bands}
}
\]

under garment-identity-disjoint validation and multiplicity-controlled inference, with complete radial structure retained wherever tested compression is unsupported.

The selected representation is then analysed in latent space, while PCA perturbations are mapped exactly back to radial-harmonic coordinates for descriptive localization. This preserves a direct mathematical path from latent variation to the original spectral representation without claiming semantic garment attributes, a universally optimal transform, or a universally valid harmonic-dependent compression law. No literature-wide priority claim is made.


---

# 3. Methods

## 3.1 Dataset and analysis units

The analysis used 2,300 CLO-SKET garment sketches corresponding to 230 garment identities across 23 garment categories, with 10 garment identities represented within each category.

Garment identity, rather than individual sketch, was treated as the primary grouping unit for validation and statistical inference because repeated sketches originating from the same garment identity cannot be treated as independent examples when evaluating representation generalization. All grouped evaluation procedures therefore enforced complete garment-identity separation between training and test partitions:

\[
G_{\mathrm{train}}\cap G_{\mathrm{test}}=\varnothing.
\]

Category structure was retained where required by the frozen validation and inferential procedures.

## 3.2 Probabilistic radial-angular morphology representation

Each sketch was represented relative to a fixed radial-angular coordinate system centered on the sketch morphology. Let \(r\) denote radial shell and \(\theta\) angular position. For sketch \(i\), angular morphology at radial shell \(r\) was normalized to define

\[
P_i(\theta\mid r),
\]

with

\[
P_i(\theta\mid r)\geq0,
\qquad
\sum_{\theta}P_i(\theta\mid r)=1
\]

for every occupied radial shell. The representation used 72 radial shells and 72 angular bins. Radial shells containing no sketch morphology were retained as structurally empty rather than assigned an artificial angular probability distribution.

## 3.3 Angular Fourier morphology

Angular structure at each radial shell was transformed using

\[
F_{i,k}(r)=\sum_{\theta}P_i(\theta\mid r)\exp(-\mathrm{i}k\theta),
\]

where \(i\) indexes sketches, \(r\) radial shells, and \(k\) angular harmonic order. Positive harmonics \(k=1,\ldots,36\) were retained. Thus each harmonic remained an explicit function of radial location,

\[
r\mapsto F_{i,k}(r),
\]

producing a full radial-harmonic field of

\[
72\times36=2592
\]

complex coefficients per sketch.

## 3.4 Harmonic-band partition and evidence-controlled compression rule

The 36 retained positive harmonics were partitioned a priori into four bands:

\[
K_1=1{:}4,\qquad K_2=5{:}12,\qquad K_3=13{:}24,\qquad K_4=25{:}36.
\]

The corresponding numbers of harmonics were \(4,8,12,12\). The partition was not assigned semantic meaning. It defined four prespecified regions of the radial-harmonic field in which **support for radial compression** was evaluated separately.

The methodological decision was deliberately conditional rather than global. For each band \(K_b\), candidate compact radial encodings were selected using training identities and then evaluated on held-out garment identities. Let \(\mathcal C_b\) denote the training-selected compact radial operator for band \(b\), and let \(\mathcal I_b\) denote the identity operator that preserves the complete 72-shell radial field. The final band operator was

\[
\mathcal R_b=
\begin{cases}
\mathcal C_b, & p_{\mathrm{FWER},b}\leq0.05,\\[2mm]
\mathcal I_b, & p_{\mathrm{FWER},b}>0.05.
\end{cases}
\]

Equivalently, the representation-design logic was

\[
\boxed{
\text{training-only candidate selection}
\rightarrow
\text{held-out garment-identity effect}
\rightarrow
\text{simultaneous inference}
\rightarrow
\begin{cases}
\text{compress}, & \text{supported},\\
\text{preserve full radial field}, & \text{otherwise}.
\end{cases}}
\]

Thus, dimensional reduction was not imposed uniformly across \(F_i(r,k)\), and failure to establish compression support was itself an explicit representation-preservation decision. Sections 3.5–3.8 define the candidate family, selection criterion, held-out effect, and simultaneous inference used to implement this rule.

## 3.5 Candidate radial representations

For each harmonic band \(K_b\), the complex radial functions \(F_{i,k}(r)\) were evaluated using three alternative radial representation families: uniformly sampled raw radial interpolation, an orthonormal discrete cosine transform (DCT), and a discrete wavelet representation.

All three families were evaluated under the same prespecified radial coefficient budgets,

\[
B\in\{4,8,12,18,24,36,48,72\}.
\]

For the raw representation, \(B\) approximately equally spaced radial samples were retained and linearly interpolated to the complete 72-shell grid. At \(B=72\), this operation is the identity.

For the DCT representation, a type-II orthonormal DCT was applied along the radial coordinate,

\[
c_{i,k,q}=\operatorname{DCT}_{\mathrm{II}}[F_{i,k}(r)]_q,
\]

and only the first \(B\) low-radial-frequency coefficients were retained. Reconstruction used the corresponding orthonormal inverse DCT.

The wavelet representation used a Daubechies-4 (`db4`) wavelet with `periodization` boundary handling and the maximum admissible decomposition level for a 72-sample radial signal. Coefficients were flattened in the fixed order

\[
[cA_L,cD_L,cD_{L-1},\ldots,cD_1],
\]

from coarse to progressively finer radial structure. The first \(B\) coefficients in this fixed ordering were retained. No sample-specific coefficient ranking or identity-dependent coefficient selection was performed.

The same representation families and coefficient budgets were evaluated independently within each outer training fold.

## 3.6 Garment-identity-disjoint representation selection

All representation selection was performed within outer garment-identity-disjoint folds. Complete garment identities were assigned to either training or test data such that

\[
G_{\mathrm{train}}\cap G_{\mathrm{test}}=\varnothing.
\]

Candidate radial representations were selected using training data only.

Within each harmonic band, the complete 72-shell representation provided the full-radial reference. Candidate representations were evaluated using category-restricted garment-identity prototype retrieval. Mean reciprocal rank (MRR) was used as the training-fold retention criterion. For candidate \(c\),

\[
Q_c=\frac{\operatorname{MRR}_{c,\mathrm{train}}}{\operatorname{MRR}_{\mathrm{full},\mathrm{train}}}.
\]

A candidate was eligible when

\[
Q_c\geq0.95.
\]

Among eligible candidates, the smallest radial budget \(B\) was selected. If several representation families shared the minimum budget, the candidate with the greatest training reconstruction-energy fraction was retained; remaining ties were resolved deterministically by representation name. Thus basis family and radial coefficient budget were chosen without reference to the outer held-out garment identities.

## 3.7 Held-out garment-identity effect

Compression support was evaluated on held-out identities using a category-controlled garment-identity separation statistic.

For garment identity \(g\), let \(W_g\) denote the median pairwise Euclidean distance among sketches belonging to \(g\), and let \(B_g\) denote the median distance from sketches of \(g\) to sketches belonging to other garment identities in the same garment category. Relative identity separation was

\[
S_g=\frac{B_g-W_g}{B_g}.
\]

Larger \(S_g\) indicates greater separation of between-garment variation from within-garment sketch variation.

For harmonic band \(b\), the paired held-out compression effect for garment \(g\) was

\[
D_{g,b}=S^{(\mathrm{selected})}_{g,b}-S^{(\mathrm{full})}_{g,b}.
\]

Within category \(c\), garment-level effects were summarized by

\[
D_{c,b}=\operatorname{median}_{g\in c}D_{g,b},
\]

and the primary category-balanced statistic was

\[
T_b=\operatorname{median}_{c=1}^{23}D_{c,b}.
\]

Thus \(T_b>0\) indicates that the training-selected compressed representation improved held-out category-controlled garment-identity separation relative to the complete radial representation. Held-out MRR and top-1 retrieval were retained as descriptive validation quantities and were not used as independent observations for the primary compression inference.

## 3.8 Bootstrap uncertainty and simultaneous permutation inference

Uncertainty in \(T_b\) was estimated using a stratified garment-identity bootstrap with 5,000 replicates. Within each category, its ten garment identities were sampled with replacement. The same sampled garment indices were used simultaneously for all four harmonic bands, preserving cross-band dependence. Category medians and the median across the 23 categories were recomputed for every replicate.

The 95% bootstrap interval was defined by the empirical 2.5th and 97.5th percentiles. The bootstrap random-number seed was

\[
20260913.
\]

The confirmatory null hypothesis was that radial compression had no systematic positive paired effect on garment-identity separation. A category-cluster sign-flip procedure was used. For each of 10,000 null replicates, one random sign

\[
s_c\in\{-1,+1\}
\]

was assigned to each category and applied jointly to that category's complete four-band effect vector,

\[
(D_{c,1},D_{c,2},D_{c,3},D_{c,4})\mapsto s_c(D_{c,1},D_{c,2},D_{c,3},D_{c,4}).
\]

This preserves dependence among harmonic bands within category while removing systematic effect direction. The permutation seed was

\[
20260914.
\]

For replicate \(q\), null band statistics \(T_b^{(q)}\) were calculated and the simultaneous maximum statistic was

\[
M^{(q)}=\max_{b=1,\ldots,4}T_b^{(q)}.
\]

The one-sided family-wise-error-rate-adjusted probability for observed band \(b\) was

\[
p_{\mathrm{FWER},b}=\frac{1+\sum_{q=1}^{10000}\mathbf 1[M^{(q)}\geq T_b]}{10001}.
\]

Compression support was established only when

\[
p_{\mathrm{FWER},b}\leq0.05.
\]

Failure to establish support resulted in retention of the complete 72-shell radial representation; it was not interpreted as evidence of absence of radial redundancy or morphology.

## 3.9 Frozen hybrid radial-spectral representation

The inferential procedure yielded the band-specific selections reported in Section 4.1. Those selections were subsequently frozen for all downstream latent analyses:

\[
k=1{:}4\rightarrow\mathrm{DCT}_4,
\]

\[
k=5{:}12\rightarrow\mathrm{RAW}_{72},
\]

\[
k=13{:}24\rightarrow\mathrm{RAW}_{72},
\]

\[
k=25{:}36\rightarrow\mathrm{db4\ wavelet}_4.
\]

Thus,

\[
Z_i=\Big[\mathcal C_{\mathrm{DCT},4}(F_{i,1:4}),F_{i,5:12},F_{i,13:24},\mathcal C_{\mathrm{db4},4}(F_{i,25:36})\Big].
\]

The resulting coefficient count and reduction relative to the complete radial-harmonic field are reported as Results rather than as prespecified methodological quantities.

## 3.10 Complex-to-real packing and standardization

Each complex block \(A\) was converted to real coordinates according to the verified packing convention

\[
\rho(A)=[\Re(\operatorname{vec}A),\Im(\operatorname{vec}A)].
\]

Blocks were concatenated in the fixed order

\[
\mathrm{low}\rightarrow\mathrm{mid}\rightarrow\mathrm{high\!-\!mid}\rightarrow\mathrm{high},
\]

giving

\[
x_i\in\mathbb R^{3008}.
\]

For validated latent-model comparisons, standardization was learned exclusively from each outer training fold. For feature \(m\),

\[
\tilde x_{im}=\frac{x_{im}-\mu_{m,\mathrm{train}}}{\sigma_{m,\mathrm{train}}},
\]

and the same training-fold parameters were applied unchanged to the corresponding outer test data. This train-only preprocessing prevents information from held-out garment identities entering latent-model construction.

After model selection was complete, the final descriptive PCA used for morphology interpretation was fitted to the frozen full representation with its corresponding full-data standardization. This final descriptive fit was not used to estimate held-out predictive performance.

## 3.11 Latent representation comparison

Three latent representation families were evaluated:

\[
\mathrm{PCA},\qquad\mathrm{AE},\qquad\mathrm{VAE},
\]

at latent dimensions

\[
z\in\{8,16,24,32,64\}.
\]

All families were evaluated under the same five outer garment-identity-disjoint folds.

The autoencoder and variational autoencoder used the same encoder/decoder hidden widths,

\[
512\rightarrow128,
\]

with batch size 128, maximum 250 epochs, early-stopping patience 20, learning rate \(10^{-3}\), weight decay \(10^{-5}\), and, for the VAE, \(\beta=1\). An internal identity-disjoint split of the outer training data was used for neural-model early stopping.

The base reproducibility seed was

\[
20260821,
\]

with deterministic fold/model-specific offsets used by the frozen implementation.

The primary held-out benchmark was garment-identity MRR; top-1 retrieval accuracy was retained as a secondary descriptive sensitivity measure.

## 3.12 Multiplicity-controlled fold-level nonlinear-model sensitivity analysis

Nonlinear latent representations were compared directly with PCA at the same latent dimension. The ten prespecified contrasts were

\[
\mathrm{AE}_z-\mathrm{PCA}_z
\]

and

\[
\mathrm{VAE}_z-\mathrm{PCA}_z,
\qquad z\in\{8,16,24,32,64\}.
\]

For each contrast, the five paired outer-fold differences in held-out MRR were used as the fold-level sensitivity observations, and the summary statistic was the mean paired outer-fold MRR difference. The outer test partitions were garment-identity-disjoint. However, because cross-validation training sets necessarily overlap, the five fitted-model comparisons were not treated as five independent population-level experimental replicates.

All

\[
2^5=32
\]

possible fold-level sign configurations were exhaustively enumerated. For each sign configuration, all ten nonlinear-versus-PCA mean effects were recomputed and their maximum retained. Each observed contrast was then compared with this common maximum-statistic distribution, controlling selection across the

\[
2\times5=10
\]

searched nonlinear contrasts within this fold-level sensitivity analysis.

Because only five outer folds were available, the sign-flip distribution has coarse probability resolution. In addition, overlap among the corresponding training sets limits population-level interpretation of fold-wise resampling. Accordingly, this procedure was used as a **conservative validation sensitivity analysis**, not as an exact population-level inferential test of model-family superiority. Its decision question was whether the frozen five-fold evidence was sufficient to justify replacing PCA with one of the tested AE or VAE configurations.

The nonlinear-model comparison tested validated task advantage, not whether the representation possessed nonlinear geometry. Failure of a nonlinear contrast to survive this analysis was therefore interpreted as absence of sufficient validation evidence to replace PCA, not as evidence that PCA is universally superior or that the representation geometry is globally linear. Nonlinear geometric structure was examined separately in Section 3.13.

## 3.13 Nonlinear geometry characterization

The geometry of the frozen representation was examined using additional nonlinear analyses including Isomap-based neighborhood geometry, principal-curve analysis, principal-curve stability analysis, and diffusion-map sensitivity analysis.

These analyses characterized departures from a purely linear latent geometry. They were not used to redefine the frozen representation unless they established a validated and stable replacement for PCA, and were therefore treated as characterization and sensitivity analyses rather than a separate representation-selection stage.

## 3.14 PCA morphology perturbation

For final descriptive morphology interpretation, PCA was applied to the full standardized frozen hybrid representation. Let \(v_j\) denote loading vector \(j\), \(\lambda_j\) its eigenvalue, and \(z_{ij}=v_j^\top\tilde x_i\) the corresponding score. The first 64 components were retained as the practical descriptive subspace.

To interpret each retained direction in the original radial-harmonic domain, a one-score-standard-deviation displacement was constructed:

\[
\sqrt{\lambda_j}v_j.
\]

Mapping this perturbation back to the original hybrid feature units gives

\[
\Delta x_j=D_\sigma[\sqrt{\lambda_j}v_j].
\]

The perturbation was unpacked using the exact verified complex-to-real lineage. The inverse hybrid transformation applied inverse DCT reconstruction for \(k=1{:}4\), identity radial mapping for \(k=5{:}24\), and inverse db4-wavelet reconstruction for \(k=25{:}36\). This produced

\[
\Delta F_j(r,k),
\]

the radial-angular Fourier perturbation associated with a one-score-standard-deviation movement along principal component \(j\).

PCA was treated as an orthogonal descriptive basis. Orthogonality was not interpreted as semantic, physical, statistical, or causal independence between garment attributes.

## 3.15 Sign-invariant morphology energy

Because \(v_j\) and \(-v_j\) represent the same PCA axis, morphology interpretation used squared complex perturbation magnitude,

\[
E_j(r,k)=|\Delta F_j(r,k)|^2,
\]

which is invariant to PCA sign reversal. For each retained component,

\[
p_j(r,k)=\frac{E_j(r,k)}{\sum_r\sum_kE_j(r,k)},
\qquad
\sum_r\sum_kp_j(r,k)=1.
\]

Thus \(p_j(r,k)\) describes relative localization of morphology variation associated with PCA direction \(j\) across radial and harmonic coordinates.

## 3.16 Radial and harmonic localization

For descriptive interpretation, radial space was partitioned into three equal-shell zones,

\[
R_{\mathrm{inner}}=1{:}24,
\qquad
R_{\mathrm{middle}}=25{:}48,
\qquad
R_{\mathrm{outer}}=49{:}72.
\]

These zones were used only as representation-space summaries. They were not interpreted as semantic garment regions.

For each retained PCA component, radial-zone energy fractions were

\[
E_j(R)=\sum_{r\in R}\sum_kp_j(r,k),
\]

and harmonic-band energy fractions were

\[
E_j(K)=\sum_r\sum_{k\in K}p_j(r,k).
\]

Joint radial-harmonic localization was

\[
E_j(R,K)=\sum_{r\in R}\sum_{k\in K}p_j(r,k).
\]

No radial-zone-by-harmonic-band independence or interaction hypothesis was tested. Joint localization was therefore interpreted descriptively rather than as enrichment, synergy, or interaction.

## 3.17 Variance-weighted retained-subspace morphology

To summarize morphology across the retained PCA subspace, component-specific localization maps were weighted by explained-variance fraction within the retained 64-component subspace. Let

\[
w_j=\frac{\lambda_j}{\sum_{\ell=1}^{64}\lambda_\ell}.
\]

The retained-subspace morphology map was

\[
P(r,k)=\sum_{j=1}^{64}w_jp_j(r,k).
\]

Because

\[
\sum_r\sum_kP(r,k)=1,
\]

radial, harmonic, and joint localization fractions can be obtained by summing \(P(r,k)\) over the corresponding regions.

All percentages derived from \(P(r,k)\) are explicitly conditional on the retained PCA-64 subspace. They are not interpreted as fractions of total garment morphology, total dataset information, or semantic garment variation.


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

## 4.3 Nonlinear latent models did not establish a validated task advantage over PCA

PCA, autoencoder (AE), and variational autoencoder (VAE) representations were compared at latent dimensions

\[
z\in\{8,16,24,32,64\}
\]

using held-out garment-identity mean reciprocal rank (MRR) across the same five outer garment-identity-disjoint folds. The ten prespecified same-dimensional AE-versus-PCA and VAE-versus-PCA contrasts were assessed using the exhaustive fold-level sign-flip sensitivity analysis described in Methods, with a maximum statistic across all ten contrasts.

The frozen contrast results were:

### Table 2. Fold-level nonlinear-versus-PCA MRR sensitivity analysis

| Contrast | Mean \(\Delta\)MRR | Median \(\Delta\)MRR | Positive / negative / zero folds | Raw one-sided fold-level \(p\) | Max-stat adjusted \(p\) |
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

The largest observed mean nonlinear improvement was

\[
\boxed{\mathrm{VAE}_{16}-\mathrm{PCA}_{16}=+0.014341\ \mathrm{MRR}},
\]

with maximum-statistic adjusted fold-level probability

\[
\boxed{p=0.2500}.
\]

No tested nonlinear contrast survived the multiplicity-controlled fold-level sensitivity analysis. PCA was therefore retained as the practical latent baseline for subsequent morphology interpretation because the frozen validation did not establish evidence sufficient to replace it with AE or VAE.

This result is deliberately bounded. The five outer test partitions are garment-identity-disjoint, but the corresponding training sets overlap; moreover, five folds permit only \(2^5=32\) fold-level sign configurations. The analysis is therefore interpreted as conservative validation evidence with coarse probability resolution, not as population-level proof that PCA is superior to nonlinear latent models. It also does not establish that the underlying representation geometry is globally linear.

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

Separately, the five-fold PCA/AE/VAE validation did not establish evidence sufficient to replace PCA with a tested nonlinear latent model; the strongest observed contrast was VAE16 − PCA16 (mean \(\Delta\)MRR \(+0.014341\), max-stat adjusted fold-level \(p=0.2500\)). PCA-64 accounted for 44.65% of variance in the standardized frozen representation.

Within that retained PCA-64 subspace, 78.54% of mapped morphology energy occurred at intermediate harmonic orders, 66.84% occurred in the outer radial zone, and 51.30% occurred jointly in the outer-radial × intermediate-harmonic region. These localization quantities are descriptive properties of the retained subspace and are not semantic or interaction effects.


---

# 5. Discussion

## 5.1 Compression as an evidence-controlled representation decision

The principal contribution is not the use of DCT, wavelets, Fourier analysis, or a hybrid descriptor in isolation. It is the treatment of radial compression as a **band-conditional inferential decision** over the structured field \(F(r,k)\). Candidate compact encodings were selected using training identities, but entered the frozen representation only when their held-out garment-identity effect survived simultaneous family-wise error control; otherwise, the complete radial field was preserved. This converts negative compression evidence into an explicit representation decision rather than a reason to continue searching until dimensional reduction succeeds.

The empirical consequence was that a uniform radial encoding was not supported across the four tested angular harmonic bands. Compact radial representations were supported for the lowest and highest tested harmonic ranges, whereas the tested compression of the two intermediate ranges was not supported. The resulting frozen representation was therefore heterogeneous by construction:

\[
\boxed{\mathrm{DCT}_4/\mathrm{RAW}_{72}/\mathrm{RAW}_{72}/\mathrm{db4}_4}.
\]

This finding is narrower, and more useful, than a claim that one radial transform is generally superior. Under the present candidate family and validation criterion, **support for radial compression differed across angular harmonic bands**. A representation strategy that imposed one basis and one coefficient budget on every harmonic order would not reflect the observed evidence. The result does not establish a universal mathematical dependence between angular frequency and radial complexity, and it does not establish that unsupported bands are intrinsically incompressible.

## 5.2 Unsupported compression appropriately led to preservation

The intermediate bands are central to the architecture of the final representation. For \(k=5{:}12\) and \(k=13{:}24\), the training-selected compact candidates did not establish positive held-out effects after simultaneous inference. The complete 72-shell radial functions were therefore retained.

This decision embodies the main methodological principle:

\[
\boxed{\text{compress where supported; preserve otherwise.}}
\]

Failure to establish compression support is not evidence that these bands are intrinsically incompressible. Other transforms, budgets, objectives, or datasets could yield different outcomes. The present result is only that replacing the full radial functions with the tested compact alternatives was not sufficiently supported under the frozen garment-identity criterion. Negative evidence therefore contributes directly to the representation rather than becoming a reason to continue searching until compression succeeds.

## 5.3 The observed pattern is not a simple low-frequency signal / high-frequency noise hierarchy

A common intuition is that low Fourier orders contain useful global structure while progressively higher orders contain increasingly disposable detail. The present results do not support such a monotonic interpretation. The highest tested harmonic band, \(k=25{:}36\), supported a compact db4-wavelet representation, while both intermediate ranges retained complete radial sampling. Moreover, within the retained PCA-64 subspace, 78.54% of variance-weighted mapped morphology energy occurred at \(k=5{:}24\).

Accordingly, neither compression support nor retained-subspace localization follows a simple low-to-high hierarchy. No harmonic band is labeled as signal, noise, semantic structure, or irrelevant detail on the basis of these experiments.

## 5.4 Different compact bases were supported at the two harmonic extremes

Four DCT coefficients were retained for \(k=1{:}4\), whereas four db4-wavelet coefficients were retained for \(k=25{:}36\). A DCT provides smooth global radial basis functions, whereas the tested wavelet construction provides localized multiscale support. The observed contrast is therefore consistent with different forms of radial organization being efficiently represented at the two ends of the tested harmonic range.

That interpretation remains conditional. The experiments compare candidate representations under a specific validation task; they do not prove that low-harmonic radial morphology is intrinsically globally smooth or that high-harmonic morphology is generated by a wavelet-like mechanism.

## 5.5 The hybrid representation follows evidence rather than architectural symmetry

The selected hybrid reduced the complete radial-harmonic field from 2592 to 1504 complex coefficients, a 41.98% reduction. The important point is not only the numerical reduction but the route by which it was obtained. Compact encoding was retained only where the held-out inferential criterion supported it, while complete radial sampling was preserved elsewhere.

The 41.98% value is a coefficient-count reduction. It is not an estimate of redundant information, removed noise, discarded morphology, or semantic irrelevance. The final DCT/raw/raw/wavelet structure is best understood as an evidence-selected representation under the present validation framework.

## 5.6 Nonlinear geometry and nonlinear model utility are distinct questions

The latent analyses produced two findings that should remain separate. Geometry audits indicated departures from a purely linear description, yet the tested autoencoder and variational-autoencoder representations did not establish a multiplicity-controlled held-out task advantage over PCA at matched latent dimensions.

These results are not contradictory. Local curvature or nonlinear neighborhood structure does not guarantee improved generalization from a nonlinear latent model for a particular task, dataset size, architecture, or validation design. Conversely, failure of the tested nonlinear models to outperform PCA does not imply that the underlying representation space is globally linear.

PCA was therefore retained pragmatically: it provided the validated reference basis, deterministic orthogonal coordinates, direct variance ordering, and an exact route for mapping latent perturbations back to radial-harmonic coordinates. The conclusion is not that garment morphology is linear, but that PCA remained the practical latent basis under the present evaluation.

The principal-curve and diffusion-map audits similarly did not establish one stable canonical nonlinear replacement. The evidence is compatible with nonlinear local geometry without supporting a unique one-dimensional garment-morphology trajectory or preferred nonlinear coordinate system.

## 5.7 Exact inverse mapping preserves mathematical traceability

For component \(j\), a one-score-standard-deviation perturbation produces \(\Delta F_j(r,k)\), from which sign-invariant morphology energy is defined as

\[
E_j(r,k)=|\Delta F_j(r,k)|^2.
\]

This gives the explicit chain

\[
\boxed{PC_j\rightarrow\Delta F_j(r,k)\rightarrow E_j(r,k)}.
\]

Because PCA eigenvector sign is arbitrary, the squared-magnitude formulation avoids assigning meaning to an arbitrary sign choice and keeps latent variation traceable to the radial-harmonic coordinates from which the representation was constructed.

## 5.8 Retained-subspace morphology localization is descriptive and conditional

PCA-64 accounted for 44.65% of variance in the standardized frozen representation. The subsequent localization results therefore describe this retained subspace, not the complete 3008-dimensional representation and not total garment morphology.

Within PCA-64, 78.54% of variance-weighted mapped morphology energy occurred at intermediate harmonic orders \(k=5{:}24\), 66.84% occurred in the outer radial zone \(r=49{:}72\), and 51.30% occurred jointly in the outer-radial × intermediate-harmonic region.

The compression and localization analyses answer different questions. Compression inference asks whether a tested radial reduction can replace the full radial representation under the held-out garment-identity criterion. PCA localization asks where perturbation energy lies within the retained latent subspace. The present analysis does not establish that the intermediate bands resisted compression because they contained 78.54% of retained mapped morphology energy.

Similarly, the 51.30% joint quantity is not an interaction effect. No radial-zone-by-harmonic-band independence or interaction hypothesis was tested.

## 5.9 Radial and harmonic coordinates remain morphological rather than semantic

The outer radial zone contained a large fraction of retained mapped energy, but

\[
\boxed{\text{outer radial}\neq\text{garment boundary}.}
\]

The radial zones are partitions of representation space, not annotated garment regions. Likewise, harmonic order \(k\), radius \(r\), and principal-component index \(PC_j\) are mathematical coordinates rather than semantic garment attributes.

The present analysis therefore does not establish axes corresponding specifically to sleeves, neckline, waist, hem, drape, fit, silhouette, or style. Such claims require independent semantic labels, spatial annotations, or controlled interventions. Mathematical controllability of a representation does not by itself establish semantic controllability.

## 5.10 Limitations

The findings are currently limited to CLO-SKET. Although garment identity and category structure were incorporated into validation, external replication is required before the observed band-specific selection pattern can be treated as a general property of garment sketches.

The compression conclusions are conditional on the tested raw, DCT, and db4-wavelet candidates, the prespecified coefficient budgets, and the garment-identity evaluation criterion. Lack of support for an intermediate-band candidate does not imply that no compact representation exists. Alternative transforms, learned bases, adaptive dictionaries, larger budgets, or different objectives may produce different selections.

The nonlinear-model conclusions are similarly method-conditional. They apply to the tested PCA, AE, and VAE configurations, latent dimensions, dataset, and validation framework. They do not constitute a general rejection of nonlinear latent modeling.

Finally, PCA-64 retains only 44.65% of standardized representation variance. The radial-harmonic localization percentages must therefore remain explicitly scoped to the retained PCA-64 subspace. The radial zones and PCA axes also lack independent semantic annotation.

## 5.11 Implications and future work

The main methodological implication is that dimensionality reduction need not be uniform across a structured spectral representation. A useful alternative is to make compression conditional on held-out evidence and preserve dimensions when replacement is not justified.

The band-specific selection pattern should first be tested on independent garment-sketch datasets. The candidate radial family can then be expanded while retaining the same identity-disjoint inferential framework. Semantic and spatial annotations would allow direct testing of whether radial-harmonic localization corresponds reproducibly to garment components or attributes. Larger datasets could provide stronger tests of nonlinear latent models and manifold stability.

Finally, the exact mapping

\[
PC_j\rightarrow\Delta F_j(r,k)
\]

provides a route toward controlled morphology experiments. Perturbations localized to selected radial-harmonic regions could be reconstructed and independently evaluated to determine whether they produce reproducible geometric and, eventually, semantically interpretable garment changes.

## 5.12 Scientific interpretation

Taken together, the evidence supports a bounded conclusion: **support for radial compression differed across the tested angular harmonic bands under the CLO-SKET identity-disjoint validation framework.** Compact DCT and db4-wavelet encodings were supported at the lowest and highest tested bands, while full radial structure was retained where tested compression was not supported.

The resulting representation reduced coefficient count without assuming uniform compressibility. Subsequent latent validation did not establish a multiplicity-controlled task advantage for the tested nonlinear alternatives over PCA, while separate geometry audits remained compatible with nonlinear local structure. Within the retained PCA-64 subspace, mapped morphology energy was concentrated in intermediate harmonic orders and outer radial positions, but these quantities remain descriptive representation-space measurements rather than semantic garment factors.

The contribution is therefore not a new Fourier, DCT, wavelet, or PCA method. It is an evidence-controlled framework for deciding **where radial compression is justified, where radial detail should be preserved, and how the resulting latent variation can be traced back to explicit radial-harmonic coordinates**.


---

# 6. Conclusion

This study formulates compression of a structured garment-sketch radial-angular Fourier field as a **band-conditional inferential representation decision**. Candidate compact radial encodings are selected using training identities and retained only when their held-out garment-identity effect is supported under simultaneous inference; where support is absent, the complete radial field is preserved. The central methodological principle is therefore

\[
\boxed{\text{compress where supported; preserve otherwise.}}
\]

Applied to CLO-SKET, support for radial compression differed across the four tested harmonic bands. Four-coefficient representations were supported for \(k=1{:}4\) using DCT and for \(k=25{:}36\) using db4 wavelets, whereas tested compression was not supported for \(k=5{:}24\), for which the complete 72-shell radial representation was retained. The resulting

\[
\mathrm{DCT}_4/\mathrm{RAW}_{72}/\mathrm{RAW}_{72}/\mathrm{db4}_4
\]

representation reduced the field from 2,592 to 1,504 complex coefficients, a 41.98% reduction, without imposing a uniform basis or global coefficient budget.

Separately, nonlinear latent models did not establish a multiplicity-controlled held-out task advantage over PCA, although geometric audits identified nonlinear structure. PCA therefore provided the practical validated basis for subsequent interpretation rather than evidence that garment-sketch morphology is globally linear. The exact inverse lineage from PCA perturbations to \(\Delta F_j(r,k)\) retained mathematical traceability to the original radial-harmonic coordinates; localization within PCA-64 remains descriptive of that retained subspace rather than semantic garment structure.

The contribution is not a new Fourier, DCT, wavelet, or PCA transform. It is an evidence-controlled framework for deciding **where a structured spectral representation may be compressed, where its original radial resolution should be preserved, and how the selected latent variation can be traced back to explicit radial-harmonic coordinates**. Independent datasets and broader candidate representation families are required to determine how far this principle generalizes beyond the present CLO-SKET analysis.


---

# Data Availability

The CLO-SKET dataset used in this study is publicly available as:

Arnia, F. (2020). *Clo-Sket* (Version 1). Mendeley Data.

DOI: `10.17632/jt533nkhsf.1`

Derived representations, analysis code, and figure-generation scripts associated
with the present study will be linked to the accompanying research repository
when the submission release is frozen.

---


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


---

# References

An, L., & Li, W. (2014). An integrated approach to fashion flat sketches classification. *International Journal of Clothing Science and Technology*, 26(5), 346–366. https://doi.org/10.1108/IJCST-05-2013-0054

Arnia, F. (2020). *Clo-Sket* (Version 1) [Data set]. Mendeley Data. https://doi.org/10.17632/jt533nkhsf.1

Coifman, R. R., & Lafon, S. (2006). Diffusion maps. *Applied and Computational Harmonic Analysis*, 21(1), 5–30. https://doi.org/10.1016/j.acha.2006.04.006

Efron, B. (1979). Bootstrap methods: Another look at the jackknife. *The Annals of Statistics*, 7(1), 1–26. https://doi.org/10.1214/aos/1176344552

Hastie, T., & Stuetzle, W. (1989). Principal curves. *Journal of the American Statistical Association*, 84(406), 502–516. https://doi.org/10.1080/01621459.1989.10478797

Hinton, G. E., & Salakhutdinov, R. R. (2006). Reducing the dimensionality of data with neural networks. *Science*, 313(5786), 504–507. https://doi.org/10.1126/science.1127647

Jolliffe, I. T., & Cadima, J. (2016). Principal component analysis: A review and recent developments. *Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences*, 374(2065), 20150202. https://doi.org/10.1098/rsta.2015.0202

Kingma, D. P., & Welling, M. (2014). Auto-Encoding Variational Bayes. *International Conference on Learning Representations (ICLR)*. arXiv:1312.6114. https://doi.org/10.48550/arXiv.1312.6114

Kuhl, F. P., & Giardina, C. R. (1982). Elliptic Fourier features of a closed contour. *Computer Graphics and Image Processing*, 18(3), 236–258. https://doi.org/10.1016/0146-664X(82)90034-X

Kunttu, I., Lepistö, L., Rauhamaa, J., & Visa, A. (2006). Multiscale Fourier descriptors for defect image retrieval. *Pattern Recognition Letters*, 27(2), 123–132. https://doi.org/10.1016/j.patrec.2005.08.022

Lee, J.-M., & Kim, W.-Y. (2012). A new shape description method using angular radial transform. *IEICE Transactions on Information and Systems*, E95-D(6), 1628–1635. https://doi.org/10.1587/transinf.E95.D.1628

Ricard, J., Coeurjolly, D., & Baskurt, A. (2005). Generalizations of angular radial transform for 2D and 3D shape retrieval. *Pattern Recognition Letters*, 26(14), 2174–2186. https://doi.org/10.1016/j.patrec.2005.03.030

Rohlf, F. J., & Archie, J. W. (1984). A comparison of Fourier methods for the description of wing shape in mosquitoes (Diptera: Culicidae). *Systematic Zoology*, 33(3), 302–317. https://doi.org/10.2307/2413076

Tenenbaum, J. B., de Silva, V., & Langford, J. C. (2000). A global geometric framework for nonlinear dimensionality reduction. *Science*, 290(5500), 2319–2323. https://doi.org/10.1126/science.290.5500.2319

Yap, P.-T., Jiang, X., & Kot, A. C. (2010). Two-dimensional polar harmonic transforms for invariant image representation. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 32(7), 1259–1270. https://doi.org/10.1109/TPAMI.2009.119

Zahn, C. T., & Roskies, R. Z. (1972). Fourier descriptors for plane closed curves. *IEEE Transactions on Computers*, C-21(3), 269–281. https://doi.org/10.1109/TC.1972.5008949

Zhang, D., & Lu, G. (2002). Shape-based image retrieval using generic Fourier descriptor. *Signal Processing: Image Communication*, 17(10), 825–848. https://doi.org/10.1016/S0923-5965(02)00084-X
