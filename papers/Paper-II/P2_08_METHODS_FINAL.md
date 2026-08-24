# CLO-SKET Paper 2 — Final Methods

## Status

**FINAL METHODS ASSEMBLY: EVIDENCE-CONTROLLED REPRESENTATION + REPRODUCIBILITY LOCKED**

This Methods section is assembled from the frozen mathematical and computational contracts. No new analysis is introduced here.

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

The radial-angular field was constructed directly from each grayscale TIFF without resizing, rotation, thresholding, or binarization. For an image of width \(W\) and height \(H\), grayscale intensity \(I(x,y)\in[0,255]\) was converted to continuous ink weight

\[
w(x,y)=\max\{255-I(x,y),0\}.
\]

To preserve image aspect ratio, both spatial axes were scaled by the common factor

\[
S=\max(W,H).
\]

Pixel coordinates were first expressed relative to the image-canvas center and divided by \(S\). The morphology center was then defined as the intensity-weighted centroid of these isotropically scaled coordinates,

\[
c_x=
\frac{\sum_{x,y}w(x,y)X(x,y)}
     {\sum_{x,y}w(x,y)},
\qquad
c_y=
\frac{\sum_{x,y}w(x,y)Y(x,y)}
     {\sum_{x,y}w(x,y)}.
\]

Centroid-relative polar coordinates were

\[
R(x,y)
=
\sqrt{
\left(X(x,y)-c_x\right)^2
+
\left(Y(x,y)-c_y\right)^2
},
\]

\[
\Theta(x,y)
=
\operatorname{atan2}
\left(
Y(x,y)-c_y,\,
X(x,y)-c_x
\right).
\]

Radius was normalized separately for each sketch as

\[
R_{\mathrm{norm}}(x,y)
=
\frac{R(x,y)}{R_{\max}},
\]

where \(R_{\max}\) is the maximum centroid-relative radius over the complete image grid. Thus \(R_{\mathrm{norm}}\in[0,1]\) describes a centroid-relative normalized canvas domain; it is not defined by the farthest nonzero-ink pixel.

The normalized radial interval \([0,1]\) was divided uniformly into 72 shells and the angular interval \([-\pi,\pi]\) uniformly into 72 bins. Pixels were assigned by hard bin membership; no interpolation or smoothing was applied. Boundary handling retained \(R_{\mathrm{norm}}=1\) in the final radial shell. The normalized radial-shell centers are therefore

\[
\frac{j+1/2}{72},
\qquad
j=0,\ldots,71.
\]

Downstream code that uses bin-center coordinates \(j+1/2\) refers to the same 72 shell locations expressed in index units.

Let \(W_i(r_j,\theta_n)\) denote the continuous ink weight accumulated in radial shell \(j\) and angular bin \(n\) for sketch \(i\). The construction explicitly preserved total ink mass under binning. Before conditional angular normalization, normalized radial mass was defined as

\[
M_i(r_j)
=
\frac{
\sum_n W_i(r_j,\theta_n)
}{
\sum_{j,n}W_i(r_j,\theta_n)
}.
\]

A shell was treated as occupied when its unnormalized shell mass exceeded

\[
10^{-14}.
\]

For occupied shells, angular morphology was normalized within radius:

\[
P_i(\theta_n\mid r_j)
=
\frac{
W_i(r_j,\theta_n)
}{
\sum_m W_i(r_j,\theta_m)
},
\]

so that

\[
P_i(\theta_n\mid r_j)\geq0,
\qquad
\sum_n P_i(\theta_n\mid r_j)=1.
\]

Empty shells were retained as all-zero 72-vectors rather than assigned an artificial angular distribution. The angular Fourier representation used subsequently in this study was obtained by applying the one-sided discrete real Fourier transform along the angular axis of this \(72\times72\) conditional field. Figure 1 summarizes the image-to-probability construction, angular Fourier transformation, and prespecified harmonic-band partition used for subsequent representation decisions.

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


### 3.3.1 Occupancy and radial-mass completeness sensitivity

The positive-harmonic field used for representation selection retained \(k=1,\ldots,36\) and excluded the angular DC coefficient. For the conditional angular distribution defined in Section 3.2,

\[
F_{i,0}(r)
=
\sum_{\theta}P_i(\theta\mid r),
\]

so that \(F_{i,0}(r)=1\) on occupied shells and \(F_{i,0}(r)=0\) on empty shells. Thus \(F_0\) carries shell-occupancy status under the conditional normalization; it does **not** encode radial ink mass. Radial mass is the distinct quantity

\[
M_i(r)
=
\frac{\sum_{\theta}W_i(r,\theta)}
     {\sum_{r,\theta}W_i(r,\theta)}.
\]

Because a positive-harmonic-only representation cannot distinguish an empty shell from an occupied shell with a perfectly uniform conditional angular distribution, representation completeness was examined in two fixed post hoc sensitivity analyses. These analyses did not reopen harmonic-band selection or alter the frozen 3008-dimensional hybrid.

First, the frozen hybrid was augmented with the 72-dimensional occupied-shell indicator. Second, it was augmented with the 72-dimensional normalized radial-mass profile \(M_i(r)\). Radial mass was reconstructed deterministically from the original TIFF images using the exact image-to-polar procedure defined in Section 3.2. As a lineage verification, the reconstructed occupied-shell mask was required to reproduce the previously frozen \(2300\times72\) occupancy mask exactly; any mismatch would have invalidated the reconstructed mass profile.

Both sensitivity analyses used the same five frozen garment-identity-disjoint folds. Within each fold, `StandardScaler` parameters were estimated from outer-training identities only and applied unchanged to the outer-test sketches. Retrieval was category-restricted and prototype-based: for each query sketch, the true garment prototype excluded that query, other garment prototypes used all available same-garment test-fold sketches, Euclidean distance determined ranking, and ties were resolved deterministically by garment identity. No hyperparameter optimization, representation reselection, or additional inferential test was introduced. The sensitivity quantities are therefore descriptive comparisons of the frozen hybrid with the corresponding augmented representation.


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


### 3.6.1 Category-restricted prototype retrieval

Category-restricted garment-identity prototype retrieval was used as an evaluation procedure, not as a learned classifier. For a query sketch \(q\) belonging to category \(c_q\), the candidate gallery consisted of the garment identities represented within that same category. In CLO-SKET this yielded ten candidate garment identities per query.

For garment identity \(g\), the prototype was the arithmetic mean of the corresponding representation vectors. The true-garment prototype explicitly excluded the query sketch:

\[
\mu_{g_q,-q}
=
\frac{
\sum_{i:g_i=g_q}x_i-x_q
}{
n_{g_q}-1
}.
\]

For every competing garment \(g\neq g_q\), the prototype was

\[
\mu_g
=
\frac{1}{n_g}
\sum_{i:g_i=g}x_i.
\]

Thus the query never contributed to its own identity prototype.

Retrieval distance was Euclidean,

\[
d(q,g)
=
\left\|
x_q-\mu_g
\right\|_2.
\]

Candidate garments were ordered by increasing distance. Rare exact ties were resolved deterministically by the stable lexical order of garment identity labels. If \(r_q\) denotes the resulting rank of the true garment for query \(q\), mean reciprocal rank was

\[
\mathrm{MRR}
=
\frac{1}{N}
\sum_{q=1}^{N}
\frac{1}{r_q},
\]

and top-1 retrieval accuracy was

\[
\mathrm{Top1}
=
\frac{1}{N}
\sum_{q=1}^{N}
\mathbf 1[r_q=1].
\]

The coordinate geometry used for retrieval depended on the analysis being performed. During harmonic-order and radial-representation selection, candidates were compared within the common frozen comparison geometry defined for that experiment so that basis or bandwidth changes did not introduce candidate-specific rescaling. In particular, the controlled radial-basis comparisons reconstructed candidate representations into the common radial field before retrieval. By contrast, the later whole-descriptor sensitivity analysis in Section 3.10.1 evaluated the actual retained descriptor coordinates directly, with standardization estimated from the corresponding outer-training identities only. These two retrieval contexts were therefore not treated as interchangeable.


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

and the same training-fold parameters were applied unchanged to the corresponding outer test data. Within each latent-validation fold, this train-only preprocessing prevents the corresponding outer-test identities from entering feature standardization or PCA/AE/VAE fitting. The 3008-dimensional hybrid input representation itself, however, had already been frozen from the preceding cross-validated band-selection analysis conducted across the complete CLO-SKET dataset. The downstream latent comparison is therefore **conditional on that previously selected hybrid representation**; it is not an independent end-to-end validation of the combined representation-selection and latent-model-selection pipeline.

After model selection was complete, the final descriptive PCA used for morphology interpretation was fitted to the frozen full representation with its corresponding full-data standardization. This final descriptive fit was not used to estimate held-out predictive performance.


### 3.10.1 Whole-representation baseline sensitivity

After the heterogeneous hybrid had been frozen, a fixed whole-representation sensitivity analysis compared it with simple descriptors applied uniformly across all 36 retained positive harmonics. This analysis was post-selection and descriptive; it did not reopen the band-selection procedure or introduce additional representation optimization.

Five representations were compared:

\[
\mathrm{HYBRID}
=
\mathrm{DCT}_4/
\mathrm{RAW}_{72}/
\mathrm{RAW}_{72}/
\mathrm{db4}_4,
\]

with 1504 complex coefficients (3008 real coordinates);

\[
\mathrm{FULL\ RAW}_{72},
\]

with \(36\times72=2592\) complex coefficients (5184 real coordinates); and three approximately dimension-matched uniform representations with a fixed radial budget \(B=42\),

\[
\mathrm{UNIFORM\ RAW}_{42},
\qquad
\mathrm{UNIFORM\ DCT}_{42},
\qquad
\mathrm{UNIFORM\ db4}_{42}.
\]

Each uniform \(B=42\) descriptor contained

\[
36\times42=1512
\]

complex coefficients, corresponding to 3024 real coordinates and differing from the hybrid by only eight complex coefficients (0.532%).

For the uniform raw representation, 42 approximately equally spaced radial coordinates were retained for every harmonic. For the uniform DCT representation, a type-II orthonormal DCT was applied along radius and the first 42 coefficients were retained for every harmonic. For the uniform wavelet representation, the same `db4` wavelet, `periodization` boundary handling, maximum admissible decomposition level, and fixed coarse-to-fine coefficient ordering used in the primary analysis were applied uniformly to every harmonic, with the first 42 coefficients retained.

All descriptors were evaluated using the same five frozen garment-identity-disjoint folds. Standardization parameters were estimated from outer-training identities only and applied unchanged to the outer-test sketches. Retrieval used the same category-restricted leave-one-sketch-out garment prototypes, Euclidean distance, and deterministic tie handling defined above. No hyperparameter search, additional feature selection, or inferential test was introduced for this sensitivity comparison.


## 3.11 Latent representation comparison

Three latent representation families were evaluated:

\[
\mathrm{PCA},\qquad\mathrm{AE},\qquad\mathrm{VAE},
\]

at latent dimensions

\[
z\in\{8,16,24,32,64\}.
\]

Conditional on the previously frozen hybrid representation, all three latent families were evaluated under the same five garment-identity-disjoint folds. Within a given fold, latent-model fitting and preprocessing used training identities only; the fold split does not erase the earlier use of the complete dataset in deciding the globally frozen hybrid.

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

Because only five outer folds were available, the sign-flip distribution has coarse probability resolution. In addition, overlap among the corresponding training sets limits population-level interpretation of fold-wise resampling. Accordingly, this procedure was used as a **conservative validation sensitivity analysis**, not as an exact population-level inferential test of model-family superiority. Its decision question was whether, **conditional on the previously selected hybrid representation**, the frozen five-fold evidence was sufficient to justify replacing PCA with one of the tested AE or VAE configurations.

The nonlinear-model comparison tested validated task advantage, not whether the representation contained detectable nonlinear predictive structure. Failure of a nonlinear contrast to survive this analysis was therefore interpreted as absence of sufficient validation evidence to replace PCA, not as evidence that PCA is universally superior or that all relationships among PCA coordinates are linear. Nonlinear predictive structure was examined separately in Section 3.13.

## 3.13 Nonlinear predictive-structure characterization

Nonlinear predictive structure was evaluated **after and separately from** the PCA/AE/VAE task comparison. The purpose of this audit was not to reopen latent-model selection, but to test whether fixed quadratic relationships among PCA coordinates improved held-out prediction relative to corresponding linear relationships. Such evidence was not interpreted as differential-geometric manifold curvature or as evidence that a nonlinear encoder should replace PCA.

### 3.13.1 Canonical PCA geometry

The geometry audit operated on the frozen real-valued radial-spectral representation,
\[
x_i\in\mathbb R^{3008},
\]
for 2,300 sketches from 230 garment identities and 23 categories. The same five garment-identity-disjoint outer-fold assignment used for latent validation was retained. For descriptive visualization only, the complete dataset was standardized and a 64-component PCA was fitted to obtain the eigenspectrum, cumulative explained variance, and leading-PC score plots. These full-population coordinates were **not** used for confirmatory curvature testing.

For the held-out quadratic-predictability audit, preprocessing was repeated independently within every outer fold. If \(f\in\{1,\ldots,5\}\) denotes the held-out fold, the standardization parameters and PCA basis were estimated exclusively from identities outside \(f\), and the held-out sketches were subsequently transformed using those training-fold quantities. Thus,
\[
G_{\mathrm{train}}^{(f)}\cap G_{\mathrm{test}}^{(f)}=\varnothing,
\]
and held-out identities influenced neither feature standardization, PCA-axis estimation, nor regression fitting.

### 3.13.2 Prespecified pairwise quadratic-predictability family

The curvature family was fixed to the first eight fold-local principal components before inspection of pairwise results. Every unordered pair was evaluated in both prediction directions, yielding
\[
2\binom{8}{2}=56
\]
directed relations \(PC_i\rightarrow PC_j\).

For each directed relation and outer fold, two nested models were fitted on the training-fold PCA scores. The linear model was
\[
y=\beta_0+\beta_1x,
\]
whereas the nonlinear alternative was deliberately restricted to the fixed quadratic form
\[
y=\beta_0+\beta_1x+\beta_2x^2.
\]
No polynomial-degree search or post-hoc basis selection was performed.

Both models were evaluated on the same held-out identities. Let
\[
R^{2,(f)}_{ij,\mathrm{lin}}
\quad\text{and}\quad
R^{2,(f)}_{ij,\mathrm{quad}}
\]
denote their held-out coefficients of determination. The fold-level quadratic-predictability effect was
\[
d^{(f)}_{ij}
=
R^{2,(f)}_{ij,\mathrm{quad}}
-
R^{2,(f)}_{ij,\mathrm{lin}},
\]
and the observed relation-level statistic was the mean across the five outer folds,
\[
T_{ij}
=
\frac{1}{5}\sum_{f=1}^{5}d^{(f)}_{ij}.
\]
Positive \(T_{ij}\) therefore indicates improved held-out prediction from the fixed quadratic relation relative to the corresponding linear relation.

### 3.13.3 Exact sign-flip inference and family-wise error control

Because each directed relation produced exactly five fold-level effects, all
\[
2^5=32
\]
possible sign configurations were enumerated. For sign vector
\[
s=(s_1,\ldots,s_5),\qquad s_f\in\{-1,+1\},
\]
the null statistic for relation \((i,j)\) was
\[
T_{ij}^{(s)}
=
\frac{1}{5}\sum_{f=1}^{5}s_fd^{(f)}_{ij}.
\]
The one-sided unadjusted exact probability was the fraction of the 32 sign configurations satisfying
\[
T_{ij}^{(s)}\ge T_{ij}.
\]
Consequently, the attainable probability resolution was explicitly limited by the five-fold design.

Multiplicity across the complete family of 56 directed relations was controlled by a common max-statistic. For every sign configuration,
\[
M^{(s)}
=
\max_{(i,j)}T_{ij}^{(s)},
\]
where the maximum was taken over all prespecified directed relations using the **same fold-sign vector jointly across the relation family**. The family-wise-error-rate-adjusted probability for relation \((i,j)\) was
\[
p_{\mathrm{FWER},ij}
=
\frac{1}{32}
\sum_{s}
\mathbf 1\!\left[
M^{(s)}\ge T_{ij}
\right].
\]
A pairwise quadratic-predictability relation was designated supported only when
\[
p_{\mathrm{FWER},ij}\le0.05.
\]
This procedure tests whether the fixed quadratic term improves held-out prediction for at least one member of the prespecified PCA-coordinate family while controlling selection across all 56 searched directions.

As in the nonlinear-model sensitivity analysis, the five outer training sets overlap. The sign-flip calculation is therefore used as a conservative fold-level geometry audit rather than as an exact population-level experiment with five independent replicates.

### 3.13.4 Neighborhood dimensionality diagnostic

A descriptive neighborhood-scale diagnostic was retained only to characterize within-neighborhood variance concentration. Using Euclidean distance in the global PCA score space, the primary analysis used 20 nearest neighbours per sketch after excluding the sketch itself. Each 20-neighbour score matrix was centered, singular values were computed, and squared singular-value energy was accumulated until 90% of within-neighborhood variance was retained. The resulting sketch-level dimensions were first summarized within garment identity and only then summarized across identities.

This quantity is **not** interpreted as an intrinsic dimension and is not compared numerically with the global PCA dimension. With 20 centered neighbours, the local matrix has rank at most 19 by construction; consequently, a local/global dimension ratio would be mechanically constrained by neighborhood size. The previously computed global-versus-local ratio is therefore retired from scientific interpretation. Neighborhood-size sensitivity at 10, 20, 30, and 50 neighbours is retained only as evidence that the descriptive quantity is scale dependent. The independently held-out pairwise quadratic-predictability analysis in Sections 3.13.1–3.13.3 is unaffected.

### 3.13.5 Interpretation boundary

The geometry audit was governed by
\[
\boxed{
\text{detectable nonlinear predictive structure}
\;\not\equiv\;
\text{validated nonlinear-model superiority}.
}
\]
Held-out improvement from a fixed quadratic relation can demonstrate nonlinear pairwise predictability among PCA coordinates, but it does not establish differential-geometric manifold curvature, a unique nonlinear manifold, a true intrinsic dimension, causal morphology factors, or superiority of AE/VAE representations. Conversely, absence of a supported AE/VAE task advantage cannot be interpreted as evidence that all relationships in the morphology representation are linear.

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
