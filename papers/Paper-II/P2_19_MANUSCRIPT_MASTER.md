# Evidence-Controlled Radial–Spectral Representation of Garment-Sketch Morphology

**NITIKA GUPTA**

---

# Abstract

Compact spectral shape descriptors commonly apply one encoding rule across the transform domain, although representational requirements may vary with scale. We test this assumption for garment-sketch morphology using a conditional radial-angular representation whose angular Fourier transform yields explicit radial harmonic functions. On 2,300 sketches representing 230 garment identities in 23 categories, candidate radial encodings were evaluated separately across four prespecified harmonic bands using garment-identity-disjoint validation and family-wise-error-rate-controlled inference. Compact four-coefficient DCT and db4-wavelet representations were supported for the lowest and highest tested harmonic bands, respectively, whereas tested compression was not supported for the intermediate harmonics, for which complete 72-shell radial structure was preserved. The resulting heterogeneous DCT/raw/raw/wavelet representation reduced coefficient count by 41.98% without imposing uniform compression. Conditional on this selected hybrid representation, nonlinear AE/VAE alternatives subsequently failed to establish a multiplicity-controlled task advantage over same-dimensional PCA, despite separately detectable nonlinear pairwise structure. Exact inverse mapping of the retained PCA representation localized latent variation back to radial-harmonic morphology, with most variance-weighted mapped energy concentrated in intermediate harmonics and outer radial shells. These findings introduce an evidence-controlled strategy for allocating representational complexity within a structured morphology field: compression is accepted where held-out evidence supports it, unsupported structure is preserved, and latent variation remains mathematically traceable to the coordinates on which representation decisions were made.


---

# Keywords

garment-sketch morphology; evidence-controlled representation; Fourier shape analysis; radial–angular representation; spectral compression; latent morphology; garment-identity-disjoint validation


---

# 1. Introduction

Representing garment sketches computationally requires a choice about what geometric information to preserve. A sketch contains spatial structure across multiple radial locations and angular scales, yet many representation pipelines resolve this choice globally: a single descriptor, basis, compression rule, or learned embedding is applied to the representation as a whole. Such uniformity is computationally convenient, but it need not reflect how discriminative morphology is distributed across scales.

This issue is particularly relevant for radial–angular spectral representations. Once sketch morphology is expressed as a conditional angular distribution \(P(\theta\mid r)\), its angular organization can be decomposed into harmonic morphology functions \(F_k(r)\). The harmonic index \(k\) then distinguishes angular scales, while the radial coordinate \(r\) retains information about where those structures occur. This produces an explicit two-coordinate morphology field rather than an undifferentiated image embedding. Fourier and radial–angular shape representations themselves are well established; the unresolved question considered here is therefore not whether such transforms can represent shape, but **how much radial structure should be retained at different angular harmonic scales**.

A common response to high-dimensional spectral representations is compression. However, imposing one compression family or coefficient budget across all harmonics assumes that radial information has comparable representational requirements throughout the angular spectrum. The opposite extreme—retaining every radial coefficient—avoids that assumption but preserves potentially unnecessary dimensionality. Neither strategy asks whether compression is actually supported by held-out morphological evidence in a particular spectral regime.

We therefore formulate representation construction as an **evidence-controlled selection problem**. Rather than selecting one radial basis globally, candidate radial representations are evaluated separately within prespecified harmonic bands. Compact encoding is retained only when its advantage over the complete radial representation survives garment-identity-disjoint validation and multiplicity control; where such support is absent, complete radial structure is preserved. Thus, failure to establish compression support is treated as a representation decision rather than converted into evidence that the underlying structure is intrinsically incompressible.

This principle leads naturally to a heterogeneous representation,

\[
\mathcal H
=
\bigoplus_b
\mathcal R_b\!\left(F_k(r)\right),
\]

where the radial operator \(\mathcal R_b\) is permitted to differ between harmonic bands \(b\). The resulting representation is therefore determined neither by architectural symmetry nor by a prespecified global compression ratio. Instead, complexity is retained selectively according to the evidence available for each spectral region.

A second representation question arises after this radial–spectral structure has been established. High-dimensional morphology can exhibit nonlinear predictive structure, but the existence of such geometry does not by itself demonstrate that a nonlinear encoder provides a better practical representation. Autoencoders and variational autoencoders can model nonlinear mappings, whereas PCA provides a simpler linear baseline with exact and transparent inverse structure. We therefore separate two questions that are often conflated:

\[
\text{Is nonlinear predictive structure detectable?}
\]

and

\[
\text{Does a nonlinear latent model provide validated task advantage?}
\]

Conditional on the hybrid representation selected by the preceding cross-validated band analysis, nonlinear alternatives are compared directly with same-dimensional PCA representations under garment-identity-disjoint evaluation and multiplicity-controlled inference. Nonlinear predictive structure is then audited separately, so that evidence of a quadratic coordinate relationship cannot retrospectively determine the model-selection conclusion. This distinction allows representational complexity, like radial compression, to **earn empirical support rather than being assumed from model flexibility alone**.

A third requirement is traceability. A compact latent coordinate is useful for downstream modelling, but its relationship to the original morphology can become opaque. Because the radial–spectral representation constructed here retains an exact inverse path, a perturbation along principal latent direction \(j\) can be mapped back to the Fourier morphology field,

\[
PC_j
\longrightarrow
\Delta F_j(r,k),
\]

and localized through the sign-invariant energy

\[
E_j(r,k)
=
\left|
\Delta F_j(r,k)
\right|^2.
\]

This provides an explicit description of where latent variation occurs in radial–harmonic coordinates. It does not require assigning individual principal components to garment parts or semantic attributes. That boundary is deliberate: localization in a mathematical morphology field is not equivalent to semantic garment understanding.

We study these questions using CLO-SKET (Arnia, 2020), a controlled garment-sketch corpus containing 2,300 sketches representing 230 recovered garment identities across 23 garment categories. The repeated-identity structure is central to the experimental design: validation is organized so that sketches of the same garment identity do not appear across training and held-out groups. Representation selection is therefore evaluated on transfer to unseen garment identities rather than on replication-specific similarity.

The study makes three methodological contributions:

1. **Harmonic-conditioned, evidence-controlled radial representation selection.** We test radial compression separately across angular harmonic regimes and construct a heterogeneous representation in which compact bases are retained only where inferential support is established, while complete radial structure is preserved elsewhere.
2. **Evidence-controlled latent-complexity selection.** We compare PCA with nonlinear AE and VAE alternatives under the same identity-disjoint validation framework and distinguish predictive utility from the separate question of nonlinear predictive structure.
3. **Exact latent-to-morphology traceability.** We map retained PCA directions through the inverse hybrid representation into explicit radial–harmonic morphology fields, allowing latent variation to be localized without assigning unsupported semantic meaning.

The resulting experiments show that radial representation requirements are not uniform across the tested harmonic spectrum. Evidence supports compact representations at the lowest and highest tested harmonic ranges but not across the intermediate orders, yielding a DCT/raw/raw/wavelet hybrid rather than a globally imposed basis. Nonlinear encoders subsequently fail to establish a multiplicity-controlled task advantage over same-dimensional PCA despite separately detectable nonlinear predictive structure. Finally, inverse mapping of the retained PCA representation reveals structured but heterogeneous radial–harmonic localization of latent morphology.

Together, these results motivate a general representation principle:

\[
\boxed{
\text{compress where evidence supports compression;}
\quad
\text{preserve structure where it does not.}
\]

The contribution is therefore **not a new Fourier transform, DCT, wavelet family, or latent model**. It is an evidence-controlled strategy for allocating representation complexity across a structured morphology field while retaining an explicit path from compact latent coordinates back to the geometry from which they were derived. Claims remain restricted to the tested candidate representations, validation criterion, dataset, and retained latent subspace.


---

# 2. Related Work

## 2.1 Spectral shape representation: from global Fourier descriptors to explicit radial–angular structure

Fourier representations have a long history in quantitative shape analysis. Early contour-based formulations encoded closed boundaries through Fourier coefficients, including classical Fourier contour descriptors and elliptic Fourier descriptors (Zahn and Roskies, 1972; Kuhl and Giardina, 1982). Such methods established that shape can be represented compactly in the frequency domain and reconstructed from spectral coefficients, but a global contour spectrum does not explicitly retain where variation occurs relative to the interior of the shape.

Region-based polar methods retain more spatial organization. The Generic Fourier Descriptor (GFD) applies a two-dimensional Fourier transform to a polar-raster representation of a shape, thereby incorporating radial and angular frequency information in a common descriptor (Zhang and Lu, 2002). The Angular Radial Transform (ART), adopted within MPEG-7 for region-based shape description, similarly represents shape through radial and angular basis functions; later generalizations extended the formulation for robust 2D and 3D retrieval (Ricard et al., 2005). Polar Harmonic Transforms provide further precedent for orthogonal two-dimensional bases defined in polar coordinates and for selecting discriminative features from a larger radial–angular transform family (Yap et al., 2010).

These studies establish that neither polar coordinates nor joint radial–angular spectral analysis are new. CLO-SKET uses a different decomposition for a different question. For sketch \(i\), angular morphology is represented conditionally at each radial shell,

\[
P_i(\theta\mid r),
\]

and Fourier analysis over \(\theta\) produces, for every harmonic \(k\), an explicit complex radial function

\[
F_{i,k}(r).
\]

The radial coordinate is therefore not immediately absorbed into a fixed two-dimensional transform basis. Keeping \(F_k(r)\) explicit allows the radial representation itself to become an object of validation: the study asks whether different angular harmonic ranges support different radial encodings.

## 2.2 Multiscale, wavelet and compact spectral descriptors

Spectral shape descriptors have also been extended across scale. Kunttu et al. (2006) proposed multiscale Fourier descriptors for contour-based shape retrieval, demonstrating that Fourier shape information can be organized at multiple resolutions. Fourier and wavelet operations have likewise been combined directly in fashion-flat analysis. An and Li (2014) used a Wavelet Fourier Descriptor together with linear discriminant analysis and an extreme learning machine for multiclass fashion-flat-sketch classification. Consequently, combining Fourier analysis with wavelets is established prior art and is not the contribution claimed here.

The distinction in CLO-SKET concerns **how a basis and coefficient budget are accepted**. Conventional compact-descriptor construction commonly chooses a descriptor family and then controls dimensionality through truncation, scale selection, feature selection, or a fixed coefficient budget. Here, DCT, wavelet and complete radial representations are candidate encodings rather than globally prescribed components. Candidate compression is evaluated separately within prespecified harmonic bands, using training garment identities for selection and held-out garment identities for confirmation. A compact representation is adopted only when its effect survives the frozen inferential criterion and simultaneous error control.

This creates an important role for a negative result. If tested compression is not supported in a harmonic band, the full 72-shell radial function is retained. Such preservation does **not** establish that the band is intrinsically incompressible; it states only that the tested lower-dimensional alternatives did not earn replacement of the complete representation under the specified data, candidate family, coefficient budgets and validation criterion. Representation construction is therefore governed by evidential sufficiency rather than by a requirement that every spectral region be compressed.

## 2.3 Garment sketches: classification, modular design and learned visual representations

Garment and fashion sketches have been studied for objectives that include classification, retrieval, design assistance, vectorization and image synthesis. The Wavelet Fourier Descriptor pipeline of An and Li (2014) is particularly relevant because it demonstrates handcrafted spectral shape analysis directly on fashion flat sketches. More recent systems use neural image-processing pipelines to extract flat-sketch design elements from clothing imagery through edge detection, vectorization and graph-based shape extraction (Lee et al., 2024).

A parallel literature represents fashion sketches through learned image features for cross-domain retrieval and generation. Fashion-specific sketch–photo retrieval has used cross-domain transformation to reduce the sketch/photo domain gap (Lei et al., 2021), while broader sketch-based image retrieval has continued to develop representation learning for zero-shot transfer, data-free learning, noise tolerance and abstraction-aware retrieval (Li et al., 2022; Bhunia et al., 2022; Chaudhuri et al., 2023; Koley et al., 2024). Recent fashion-retrieval surveys likewise position sketch-guided retrieval within a wider learned visual-retrieval ecosystem (Islam et al., 2024). These approaches are valuable when the target is semantic matching, cross-domain retrieval or learned visual invariance, but their representation objective differs from the present study. CLO-SKET does not attempt to infer garment construction modules, generate realistic garments, or assign semantic meanings to latent coordinates. Its target is narrower: to test how an explicit morphology field should allocate radial representational complexity across angular harmonic scale while preserving a mathematically traceable inverse.

This distinction also motivates the use of garment identity rather than category alone as the held-out unit. Category labels provide coarse semantic grouping, whereas repeated drawings of the same garment identity permit evaluation of whether a representation preserves identity-specific morphology across sketch realizations. The resulting validation question is therefore not simply whether dresses can be separated from trousers, but whether representation decisions transfer to garment identities absent from model fitting and candidate selection.

## 2.4 Linear latent representations, nonlinear encoders and manifold geometry

After representation construction, dimensionality reduction introduces a second complexity decision. PCA supplies an orthogonal variance-ordered coordinate system with a direct linear inverse to the original feature space (Jolliffe and Cadima, 2016). Autoencoders learn nonlinear low-dimensional representations through reconstruction objectives (Hinton and Salakhutdinov, 2006), while variational autoencoders introduce a probabilistic latent-variable formulation optimized through variational inference (Kingma and Welling, 2014). Nonlinear manifold methods—including principal curves, Isomap and diffusion maps—provide additional tools for diagnosing curved or locally low-dimensional structure (Hastie and Stuetzle, 1989; Tenenbaum et al., 2000; Coifman and Lafon, 2006).

The presence of nonlinear predictive structure, however, is logically distinct from evidence that a nonlinear encoder improves a held-out task. A curved data distribution can be detectable while a simpler linear representation remains competitive or preferable under finite-sample validation. CLO-SKET therefore separates these hypotheses experimentally. Conditional on the previously selected hybrid representation, same-dimensional AE and VAE representations are compared with PCA using identity-disjoint held-out retrieval and multiplicity-controlled inference, whereas fixed quadratic coordinate relationships and other manifold-oriented sensitivity analyses are treated as separate diagnostics.

This separation prevents either result from being overinterpreted. Failure of a nonlinear encoder to establish task advantage does not prove that all relationships in the representation are linear; conversely, evidence of a quadratic coordinate relationship does not by itself justify replacing the task-validated representation with a nonlinear model. In this study, latent complexity is subjected to the same broader principle as radial compression: additional flexibility must be supported by the relevant validation evidence.

## 2.5 Traceability from latent coordinates back to morphology

Interpretability in latent representations can refer to several different properties. One is semantic disentanglement, in which individual coordinates correspond to human-named factors. Another, more limited form is **mathematical traceability**: determining how a latent perturbation changes the original structured representation even when no semantic label is assigned.

PCA is particularly useful for the latter because a displacement along a principal direction can be mapped exactly through the frozen preprocessing and inverse hybrid representation. CLO-SKET uses this path

\[
PC_j
\rightarrow
\Delta x_j
\rightarrow
\Delta F_j(r,k)
\]

and summarizes the resulting perturbation with the sign-invariant field

\[
E_j(r,k)=|\Delta F_j(r,k)|^2.
\]

The use of PCA reconstruction or Fourier-domain visualization is not itself presented as new. The methodological role of this analysis is to preserve interpretability after evidence-controlled heterogeneous compression: latent variation remains localizable in the same radial–harmonic coordinates in which representation decisions were made. This is intentionally weaker than semantic disentanglement. A concentration of energy at an outer radial shell or within a harmonic range is a statement about mathematical localization, not evidence that a PC corresponds to a hem, sleeve, silhouette attribute, or other garment concept.

## 2.6 Position of the present study

The individual mathematical ingredients used in CLO-SKET have substantial precedent. Fourier descriptors establish spectral shape encoding; GFD, ART and polar harmonic transforms establish radial–angular spectral representations; multiscale and wavelet Fourier descriptors establish scale-dependent and Fourier–wavelet shape analysis; PCA, autoencoders, VAEs and manifold methods provide established linear and nonlinear latent tools. Fashion-flat research further demonstrates both spectral classification and structural or learned processing of garment sketches.

The gap addressed here lies at the **representation-decision level**. Rather than assuming that one radial basis or one compression budget should apply uniformly across a structured Fourier morphology field, CLO-SKET evaluates radial compression separately across prespecified angular harmonic bands and requires candidate compression to survive garment-identity-disjoint, multiplicity-controlled confirmation. The resulting representation is allowed to be heterogeneous:

\[
\boxed{
\text{compress where support is established;}
\qquad
\text{preserve complete structure otherwise.}
}
\]

The same evidential discipline is then applied to latent-model complexity, while an exact inverse path retains traceability from the selected latent representation back to radial–harmonic morphology coordinates.

Accordingly, the paper does **not** claim invention of Fourier descriptors, polar shape representation, DCT or wavelet compression, PCA-based reconstruction, nonlinear latent modelling, or fashion-sketch analysis. Nor does it claim a universally optimal harmonic partition or a universal law of garment morphology. Its contribution is an evidence-controlled framework for deciding **where representational simplification is justified within a structured morphology field**, together with validation safeguards that preserve unsupported structure and distinguish mathematical localization from semantic interpretation.


## 2.7 Contemporary CV context and remaining gap

Recent sketch-based computer-vision work increasingly addresses learned invariance across sketch and image domains. Structure-aware disentanglement has been used for zero-shot sketch-based image retrieval (Li et al., 2022); noise-tolerant retrieval explicitly models unhelpful sketch strokes (Bhunia et al., 2022); data-free SBIR transfers knowledge from pretrained single-modality teachers without paired training data (Chaudhuri et al., 2023); and abstraction-aware retrieval models variation in sketch abstraction and retrieval granularity (Koley et al., 2024). In fashion, cross-domain transformation has been used to align sketches and product photographs for fine-grained retrieval (Lei et al., 2021), while recent flat-sketch work has focused on automatic extraction and vectorization of design elements from clothing images (Lee et al., 2024).

These advances strengthen rather than remove the distinction motivating the present study. Their principal question is how to learn representations that improve recognition, retrieval, domain transfer, or vector extraction. The question here is different: given an explicit radial–harmonic morphology field, **where is dimensional simplification empirically justified, and where should structure be preserved?** The proposed framework therefore does not compete with learned SBIR systems as a retrieval architecture. It addresses representation governance within an interpretable structured descriptor, using held-out garment identities and simultaneous inference to decide which radial encodings are permitted to replace the complete field.

This positioning is important for CVIU. The novelty claim is not that handcrafted spectral descriptors supersede contemporary learned features. It is that structured representations expose subdomains in which complexity decisions can be tested explicitly, negative evidence can preserve information rather than being hidden by a global bottleneck, and retained latent variation can remain exactly traceable to the coordinates on which those decisions were made.


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

The \(0.95\) value served as a **training-only admissibility threshold**: a compact candidate was not considered unless its category-restricted prototype-retrieval MRR retained at least 95% of the complete radial reference within the outer-training identities. It was not estimated from the held-out identities, was not treated as a statistically calibrated non-inferiority margin, and is not claimed to be a universally optimal retention threshold.

Among eligible candidates, the smallest radial budget \(B\) was selected. If several representation families shared the minimum budget, the candidate with the greatest training reconstruction-energy fraction was retained; remaining ties were resolved deterministically by representation name. Thus basis family and radial coefficient budget were chosen without reference to the outer held-out garment identities.

The training MRR screen and the subsequent held-out inferential endpoint intentionally served different roles. Training MRR was used only to prevent severe loss of identity-retrieval utility during candidate selection. The held-out statistic \(S_g\), defined below, then asked a stricter and separate question: whether the training-selected compact representation produced a positive change in category-controlled garment-identity separation relative to the complete radial field. The procedure therefore was **not** formulated as a conventional held-out non-inferiority test of retrieval performance.

The retention threshold \(0.95\), radial-budget grid \(B\in\{4,8,12,18,24,36,48,72\}\), and harmonic-band boundaries were fixed design choices of the frozen analysis. Prespecification prevents held-out adaptation but does not establish that these constants are optimal. No post hoc threshold or boundary search is used here to strengthen the primary inferential claims; conclusions are conditional on these design choices.


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

This preserves dependence among harmonic bands within category while removing systematic effect direction. The category-cluster sign-flip procedure relies on sign exchangeability of the four-band category effect vector under the null: conditional on the observed effect magnitudes, reversing the sign of a category's complete effect vector is treated as equally plausible under no systematic directional compression effect. The 10,000 randomly generated sign configurations therefore provide a Monte Carlo randomization approximation rather than an exhaustive enumeration of all possible category-sign assignments. The permutation seed was

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


This confirmatory effect should not be interpreted as a held-out retrieval non-inferiority test. The \(Q_c\geq0.95\) criterion was used only inside each outer-training fold to define candidate eligibility; the confirmatory endpoint was the distinct held-out category-balanced separation statistic \(T_b\). Consequently, inferential support below means that the training-selected compact representation showed a positive held-out separation effect under the frozen design. It does not imply that discarded coefficients were noise or that compression is universally superior to the complete representation. Inferential decisions use the max-statistic FWER-adjusted \(p\)-values from the joint four-band category-cluster sign-flip procedure; unadjusted tail probabilities, where reported, are not the confirmatory decision quantities.

For the lowest harmonic band, \(k=1{:}4\), the training-selected four-coefficient DCT representation yielded

\[
\Delta=0.059306,
\]

with bootstrap 95% CI

\[
[0.023295,\;0.108196],
\]

and max-statistic FWER-adjusted \(p\)-value

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


---

# 5. Discussion

## 5.1 Evidence-controlled representation design is the central contribution

The main contribution of this study is not a new Fourier transform, DCT basis, wavelet family, or PCA procedure. Each of those elements has substantial prior precedent. The methodological contribution lies instead in treating representation complexity as an empirical decision that may differ across a structured spectral field.

Starting from the radial-harmonic morphology field \(F_k(r)\), radial representation was evaluated separately across prespecified angular harmonic ranges. Compact encodings entered the final representation only when they were supported under garment-identity-disjoint validation with simultaneous family-wise error control. Where that support was not established, complete radial structure was preserved rather than compressed by default.

The resulting representation was

\[
\boxed{
\mathrm{DCT}_4/
\mathrm{RAW}_{72}/
\mathrm{RAW}_{72}/
\mathrm{db4}_4
}.
\]

This structure is important because it was not chosen for architectural symmetry. The low and highest tested harmonic bands supported compact radial encodings, while the two intermediate ranges did not. The framework therefore embodies the principle

\[
\boxed{
\text{compress where supported; preserve otherwise.}
}
\]

This is more than a compression rule. It is a representation-preservation rule. Negative evidence contributes directly to the architecture by preventing unsupported dimensional reduction.


The decision rule also separates **candidate admissibility** from **confirmatory evidence**. A compact candidate first had to retain at least 95% of training-fold retrieval MRR relative to the complete radial reference. Passing that screen did not itself authorize compression. The selected candidate then had to show multiplicity-controlled positive held-out evidence on the category-balanced garment-separation endpoint. The framework therefore asks for more than ordinary retrieval retention before replacing the full radial field. This should not be interpreted as a denoising test: no discarded coefficient is classified as noise.

The conclusion is deliberately conditional. The present experiments establish that support for the tested radial compression strategies differed across angular harmonic scale under the frozen CLO-SKET validation design. They do not establish a universal law relating angular harmonic order to radial complexity, nor do they prove that the intermediate bands are intrinsically incompressible.

---

## 5.2 The heterogeneous representation rejects simple spectral heuristics

The selected DCT/raw/raw/wavelet structure also cautions against a simple low-frequency-signal/high-frequency-noise interpretation of garment-sketch morphology. If useful structure decreased monotonically with harmonic order, one might expect progressively stronger compression support toward the highest harmonics. That pattern was not observed. The highest tested band, \(k=25{:}36\), supported compact db4-wavelet encoding, whereas both intermediate bands, \(k=5{:}24\), retained complete 72-shell radial structure.

The retained latent morphology showed a similarly non-monotonic organization. Within the PCA-64 subspace, 78.54% of variance-weighted mapped morphology energy occurred at intermediate harmonic orders \(k=5{:}24\). Thus, the bands that were not supported for tested compression also contained much of the mapped variation represented by the retained latent subspace. These two results should not be conflated causally: compression inference asks whether a tested compact representation can replace the full radial field under the held-out identity criterion, whereas latent localization asks where retained PCA perturbation energy lies after the final representation has been frozen.

The two supported compact bases also differed. The lowest harmonic band retained four DCT coefficients, whereas the highest band retained four db4-wavelet coefficients. The contrast is consistent with different radial organizations being represented efficiently by different basis families, but the experiment does not establish an intrinsic physical correspondence between low harmonics and global smoothness or between high harmonics and wavelet-like structure.

The hybrid representation reduced the complex coefficient count from 2592 to 1504, a 41.98% reduction. That value is strictly a representation-dimensionality result. It is not an estimate of removed noise, redundant morphology, irrelevant geometry, or semantic content.

---


### 5.2.1 Conditional angular morphology intentionally differs from radial occupancy and mass

The exclusion of \(k=0\) from the frozen hybrid requires a precise interpretation. For an occupied radial shell, conditioning over angle fixes

\[
F_0(r)=\sum_{\theta}P(\theta\mid r)=1,
\]

whereas an empty shell has \(F_0(r)=0\). The DC coefficient therefore represents occupancy status under the conditional normalization rather than the amount of ink occurring at that radius. Radial mass,

\[
M(r),
\]

is a separate quantity defined before within-shell angular normalization.

This distinction matters because an empty shell and an occupied shell with perfectly uniform angular probability both have zero positive harmonics. The dedicated occupancy sensitivity analysis showed that this theoretical ambiguity had negligible practical consequence for CLO-SKET: 99.8569% of sketch-shell locations were occupied, and appending the complete 72-dimensional occupancy mask slightly decreased mean MRR by 0.000651. The frozen positive-harmonic descriptor therefore does not require an occupancy channel for the present identity-retrieval task.

Radial mass was more informative, but only modestly so. Appending the independently reconstructed and lineage-verified \(M(r)\) profile increased mean MRR by 0.003486 and mean top-1 retrieval by 0.006973. Four of five folds improved, although 2,230 of 2,300 query ranks remained unchanged. Because this was a descriptive sensitivity analysis rather than a prespecified inferential comparison, the gain is not interpreted as statistically established superiority.

The primary 3008-dimensional representation is therefore retained unchanged. Its scope is deliberately narrower than a complete reconstruction of sketch ink: it represents angular morphology conditional on radial location. The radial-mass result indicates that \(M(r)\) contains modest complementary identity information and may be useful as an auxiliary channel in future extensions, but it does not invalidate the evidence-controlled positive-harmonic representation studied here.



### 5.2.2 Whole-representation baselines support heterogeneity without establishing universal superiority

The descriptor-level sensitivity analysis provides an important complement to the band-wise inferential results. The heterogeneous hybrid did not exceed the complete \(\mathrm{RAW}_{72}\) representation in mean retrieval: full radial structure was descriptively higher by 0.002607 MRR. However, the complete representation required 5184 real coordinates, compared with 3008 for the hybrid. The central benefit of the hybrid is therefore not maximum raw retrieval score, but substantial dimensional reduction with little loss in the present identity-retrieval task.

The nearly dimension-matched uniform \(\mathrm{RAW}_{42}\) descriptor was also competitive, differing from the hybrid by only \(-0.000870\) mean MRR. This result prevents an overly strong claim that heterogeneous encoding is uniquely necessary for competitive retrieval. A simple uniformly subsampled radial representation can preserve much of the same identity information at a similar dimensionality.

The uniform transform baselines nevertheless reveal why the evidence-controlled architecture is useful. Applying DCT-42 uniformly across all harmonics reduced mean MRR by 0.033263 relative to the hybrid, and uniform db4-wavelet-42 reduced it by 0.027388. Both deficits occurred in all five identity-disjoint folds. These results are consistent with the primary finding that one compact radial basis should not be assumed appropriate across the complete harmonic field.

Accordingly, the whole-representation evidence supports a bounded conclusion:

\[
\boxed{
\text{heterogeneous encoding preserves near-full retrieval at reduced dimension}
}
\]

while avoiding the losses associated with uniformly imposing the tested compact DCT or wavelet bases. It does not establish that the hybrid is universally optimal, and the competitive performance of uniform \(\mathrm{RAW}_{42}\) should remain visible when interpreting the contribution.


## 5.3 Nonlinear pairwise structure and nonlinear-model utility are different scientific questions

The latent analysis illustrates a second methodological principle: detectable nonlinear predictive structure does not automatically justify a nonlinear latent model.

At matched latent dimensions, the tested AE and VAE representations did not establish a multiplicity-controlled held-out garment-identity retrieval advantage over PCA. This comparison is conditional on the hybrid representation already selected by the preceding cross-validated band analysis; it is not an untouched end-to-end validation of representation selection followed by latent-model selection. The strongest observed nonlinear contrast was \(\mathrm{VAE}_{16}-\mathrm{PCA}_{16}\), with mean \(\Delta\mathrm{MRR}=+0.014341\), but its max-statistic adjusted fold-level probability was \(p=0.2500\). PCA was therefore retained as the practical latent baseline **within the frozen hybrid representation** because the downstream comparison did not provide sufficient evidence to replace it.

That decision does not imply that every relationship in the representation is linear. A separate held-out audit found one FWER-supported quadratic PCA-coordinate relation, with best mean improvement

\[
\overline{\Delta R^2}=+0.432042.
\]

The appropriate interpretation is **pairwise nonlinear predictability**: for one prespecified directed PC relation, the fixed quadratic predictor improved held-out prediction relative to the corresponding linear predictor. This result is not, by itself, evidence of differential-geometric manifold curvature; category structure or other mixture effects may also generate nonlinear coordinate relationships.

The neighborhood dimensionality calculation is retained only as a scale-conditioned descriptive diagnostic. At 20 neighbours, the identity-level median number of directions required for 90% within-neighborhood variance was 15, but a centered 20-neighbour matrix has rank at most 19 by construction. The value therefore cannot support a quantitative comparison with the global PCA dimension or an intrinsic-dimensionality claim, and the previously reported ratio between local and global dimensions is retired.

These results are compatible rather than contradictory. Nonlinear pairwise predictability can be present without producing a measurable generalization advantage for a particular nonlinear encoder, dataset size, task, or validation design. Conversely, failure of the tested nonlinear models to outperform PCA is not evidence that all relationships in the morphology representation are linear.

The principal-curve and diffusion-map sensitivity analyses reinforce this bounded interpretation. They did not establish a single stable nonlinear coordinate system or canonical one-dimensional morphology trajectory that warranted replacing PCA. Accordingly,

\[
\boxed{
\text{nonlinear pairwise structure}
\neq
\text{validated nonlinear-model utility}.
}
\]

PCA should therefore be understood here as a practical validated basis, not as a claim about the fundamental geometry of garment morphology.

---

## 5.4 Exact latent-to-Fourier mapping provides mathematical traceability

A central advantage of retaining an explicit radial-harmonic representation is that latent variation can be mapped back to the coordinates from which the representation was constructed.

For PCA direction \(j\), a one-score-standard-deviation perturbation is mapped through the exact frozen inverse hybrid representation to obtain

\[
\Delta F_j(r,k).
\]

Because PCA eigenvector orientation is arbitrary, interpretation is based on the sign-invariant morphology-energy field

\[
E_j(r,k)
=
|\Delta F_j(r,k)|^2.
\]

The resulting traceability chain is

\[
\boxed{
PC_j
\rightarrow
\Delta F_j(r,k)
\rightarrow
E_j(r,k).
}
\]

This construction does not make PCA components semantic factors. Its value is more basic: variation expressed in a latent coordinate can be localized in explicit radial and harmonic coordinates rather than remaining an opaque embedding dimension.

The selected examples illustrate that different latent directions occupy different regions of the morphology field. PC1 and PC3 were strongly outer-radial, whereas PC15 was predominantly inner-radial. Their maximum-energy harmonic coordinates also differed. These differences show that the retained PCA space contains multiple radial-harmonic modes of variation rather than a single uniform morphology pattern.

This form of interpretability is mathematical rather than semantic. It establishes where a latent perturbation acts in the representation; it does not establish what garment attribute that perturbation means.

---

## 5.5 Retained-subspace localization is informative only with its denominator and claim boundary intact

The first 64 principal components accounted for 44.65% of variance in the standardized frozen representation. All subsequent radial-harmonic localization therefore applies only to that retained PCA-64 subspace.

Within this subspace, 78.54% of variance-weighted mapped morphology energy occurred at intermediate harmonic orders \(k=5{:}24\), 66.84% occurred in the outer radial zone \(r=49{:}72\), and 51.30% occurred jointly in the outer-radial × intermediate-harmonic region. The largest individual radial-harmonic cells were outer × \(k=13{:}24\) and outer × \(k=5{:}12\).

These numbers describe how variation represented by PCA-64 is localized after exact inverse mapping. They are not percentages of total garment morphology, not percentages of the complete 3008-dimensional representation, and not estimates of semantic garment-part contribution.

The radial coordinates themselves also remain morphological rather than semantic. In particular,

\[
\boxed{
\text{outer radial}
\neq
\text{garment boundary}.
}
\]

The radial zones are partitions of the representation space, not annotated regions such as hem, sleeve, neckline, waist, or silhouette edge. Likewise, harmonic order and PCA index are mathematical coordinates rather than garment attributes.

The 51.30% joint outer-radial × intermediate-harmonic quantity is also descriptive. No radial-zone-by-harmonic-band interaction or independence hypothesis was tested, so the observation should not be described as enrichment, synergy, coupling, or interaction.

These boundaries are not merely conservative wording. They define what kind of interpretability the present framework actually supplies: explicit spatial-spectral localization with a verifiable mathematical denominator, without semantic labels that the data do not contain.

---

## 5.6 Limitations and generalizability

Several limitations determine how broadly these findings can be interpreted.

First, the empirical results are currently specific to CLO-SKET. Garment identity and category structure were incorporated into validation, but independent garment-sketch datasets are required before the selected DCT/raw/raw/wavelet pattern can be considered a general property of fashion-sketch morphology.

Second, radial-representation selection is conditional on the candidate family, coefficient budgets, objective, validation statistic, \(Q_c=0.95\) training-retention threshold, and prespecified harmonic-band boundaries tested here. The \(0.95\) value is a design admissibility threshold rather than a statistically calibrated non-inferiority margin, and the present analysis does not establish that this threshold, the eight tested budgets, or the four band boundaries are optimal. Prespecification prevents held-out tuning but does not remove this design dependence. The lack of support for compression at \(k=5{:}24\) therefore does not imply that no compact representation exists for those ranges. Alternative thresholds, partitions, analytical bases, adaptive dictionaries, learned representations, larger budgets, or different evaluation objectives could lead to different decisions.

Third, the nonlinear-model conclusion is also model-conditional. It applies to the tested PCA, AE, and VAE configurations, latent dimensions, dataset size, and five-fold outer validation design. With only five outer folds, exhaustive fold-level sign-flip inference has coarse probability resolution, and overlapping training sets limit population-level interpretation. The result therefore supports retention of PCA under the present evidence rather than a general rejection of nonlinear latent modeling.

Fourth, the neighborhood dimensionality diagnostic is scale- and sample-size-dependent. At the prespecified 20-neighbour scale, the centered local matrix has rank at most 19; the observed median of 15 is therefore retained only as a descriptive within-neighborhood variance summary and is not interpreted as an intrinsic dimension or compared quantitatively with the global PCA dimension.

Finally, the PCA localization analysis is limited by its 44.65% retained-variance denominator and by the absence of independent semantic or spatial garment annotations. The current study can localize variation mathematically but cannot determine whether particular radial-harmonic patterns correspond reproducibly to named garment features.

---

## 5.7 Implications and future work

The broad methodological implication is that dimensionality reduction need not be imposed uniformly across a structured representation. When the representation has interpretable subdomains—here, angular harmonic ranges with explicit radial dependence—complexity can instead be treated as a locally testable design choice.

This suggests a more general workflow:

\[
\boxed{
\text{structured representation}
\rightarrow
\text{subdomain-specific candidate encodings}
\rightarrow
\text{held-out evidence}
\rightarrow
\text{compress or preserve}
}.
\]

Such a principle could be useful beyond garment sketches wherever morphology is represented over organized spatial, spectral, temporal, or multiscale coordinates. The present study does not establish transfer to those domains, but it provides a concrete example of how representation reduction can be made conditional on evidence rather than architectural convenience.

For garment morphology specifically, the first priority is external replication of the harmonic-dependent radial-selection pattern. The candidate radial family can then be expanded while retaining the same identity-disjoint and multiplicity-controlled decision logic. A larger dataset would also permit stronger tests of nonlinear latent models and more stable geometry inference.

A second priority is semantic validation. Spatial annotations or garment-attribute labels would allow direct tests of whether particular radial-harmonic localization patterns correspond reproducibly to sleeves, neckline structure, waist shape, hem geometry, silhouette, or other interpretable garment properties. Until such labels are introduced, those meanings should not be inferred from mathematical coordinates alone.

A third direction follows from the exact inverse mapping. Controlled perturbations localized to selected \((r,k)\) regions could be reconstructed and evaluated to determine whether they produce reproducible geometric changes. Such experiments would move the framework from descriptive localization toward experimentally testable morphology control. They would constitute a new study rather than evidence already established here.

---

## 5.8 Scientific interpretation

The strongest conclusion from Paper II is not that one transform is superior to another. It is that representation complexity did not behave uniformly across the radial-harmonic morphology field, and that this heterogeneity could be handled explicitly rather than hidden inside a single global descriptor.

Under the CLO-SKET identity-disjoint inferential framework, compact radial representations were supported for the lowest and highest tested harmonic bands, whereas full radial structure was preserved in the intermediate ranges because the tested compression alternatives did not receive sufficient support. These band-level conclusions are conditional on the category-level sign-exchangeability assumption underlying the prespecified cluster sign-flip randomization procedure and on max-statistic family-wise error control across the four tested bands. The resulting hybrid reduced coefficient count without assuming uniform compressibility.

At the latent level, greater model complexity likewise had to earn empirical support. The tested nonlinear encoders did not establish a multiplicity-controlled task advantage over PCA, even though a separate audit detected nonlinear pairwise predictability. PCA therefore remained the practical representation for interpretation without being promoted to a claim of intrinsic linearity.

Finally, exact inverse mapping retained traceability from latent coordinates back to radial-harmonic morphology. Within the PCA-64 subspace, mapped variation showed strong intermediate-harmonic and outer-radial organization while individual components remained heterogeneous.

The scientific identity of the paper can therefore be summarized as follows:

\[
\boxed{
\text{representation complexity must earn empirical support;}
\newline
\text{unsupported structure is preserved rather than discarded;}
\newline
\text{and retained latent variation remains traceable to explicit morphology coordinates.}
}
\]

The contribution is thus not a new spectral transform, but an evidence-controlled strategy for deciding how different parts of a structured morphology representation should be encoded, preserved, and interpreted.


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

Manuscript-associated analysis code, figure-generation scripts, and reproducibility
materials available for the present study are maintained in the accompanying
public WeaveAI research repository. The original CLO-SKET dataset remains available
from Mendeley Data under the DOI given above.


---

# Code Availability

The accompanying public WeaveAI research repository preserves the computational
provenance associated with this study, including the upstream radial–angular
analysis notebook and the frozen executed notebook underlying the reported
Paper-II analyses. SHA-256 checksums are provided for integrity verification.

The preserved computational lineage begins with the publicly available CLO-SKET
image data and includes radial–angular probability construction, angular Fourier
morphology, radial-representation analysis, bootstrap and permutation inference,
hybrid representation construction, latent-model validation, and PCA-based
morphology mapping.

The provenance notebooks retain elements of the original Google Colab/Google
Drive execution environment and historical intermediate-state workflow.
Accordingly, they document the computational origin of the reported results but
should not presently be interpreted as a clean-environment, end-to-end
reproduction package. Portable execution instructions and publication-figure
export code will be included with the frozen submission release.


---

# Figure Captions

**Figure 1. Probabilistic radial–angular Fourier representation of garment-sketch morphology.** Sketch morphology is expressed in radial–angular coordinates and normalized within each occupied radial shell to obtain the conditional angular distribution \(P_i(\theta\mid r)\). Angular Fourier transformation then yields the complex radial–harmonic field \(F_{i,k}(r)\), retaining radial position \(r\) explicitly for positive harmonic orders \(k=1,\ldots,36\). The four prespecified harmonic bands \(k=1{:}4\), \(5{:}12\), \(13{:}24\), and \(25{:}36\) define the spectral regions in which radial representation is subsequently evaluated. The construction is mathematical; no semantic garment-part interpretation is assigned to radial shells or harmonic orders.

**Figure 2. Harmonic-dependent evidence for radial representation and the resulting frozen hybrid descriptor.** Candidate raw, DCT, and db4-wavelet radial encodings were selected using training identities and evaluated on held-out garment identities. Points show the category-balanced held-out separation effect \(\Delta=T_b\); intervals are 95% garment-identity bootstrap intervals, and decisions use the prespecified Monte Carlo category-cluster sign-flip randomization procedure with max-statistic family-wise error control across the four harmonic bands. Compact radial encoding was supported for \(k=1{:}4\) (DCT\(_4\), \(p_{\mathrm{FWER}}=0.000200\)) and \(k=25{:}36\) (db4-wavelet\(_4\), \(p_{\mathrm{FWER}}=0.019698\)), but not for \(k=5{:}12\) or \(k=13{:}24\); complete 72-shell radial structure was therefore preserved in the unsupported bands. The frozen DCT/raw/raw/wavelet representation contains 1,504 complex coefficients versus 2,592 in the complete field, a 41.98% coefficient reduction. Lack of compression support is not interpreted as proof of intrinsic incompressibility.

**Figure 3. Conditional latent-model comparison and nonlinear pairwise structure.** **(A)** Conditional on the previously selected hybrid representation, mean held-out MRR differences for AE and VAE relative to same-dimensional PCA across five garment-identity-disjoint outer folds and latent dimensions \(8,16,24,32,64\). None of the ten prespecified nonlinear-versus-PCA contrasts survived the common max-statistic fold-level sensitivity analysis; the largest observed mean improvement was VAE\(_{16}\)−PCA\(_{16}\), \(\Delta\mathrm{MRR}=+0.014341\), with adjusted \(p=0.25\). **(B)** A separate held-out audit detected one FWER-supported fixed quadratic PCA-coordinate relation (best mean \(\Delta R^2=+0.432042\)), establishing pairwise nonlinear predictability rather than differential-geometric manifold curvature. At the prespecified 20-neighbour scale, the identity-level median number of directions required for 90% within-neighborhood variance was 15 (IQR 15–15); because a centered 20-neighbour matrix has rank at most 19, this quantity is shown only as a scale-conditioned descriptive diagnostic and is not compared with the global PCA dimension. PCA is retained as the practical validated latent baseline; detectable nonlinear pairwise structure is not evidence of nonlinear-model superiority.

**Figure 4. Principal latent variation localizes in radial–harmonic morphology space.** **(A–C)** Sign-invariant morphology-energy maps \(E_j(r,k)=|\Delta F_j(r,k)|^2\), obtained by exact inverse mapping of one-score-standard-deviation perturbations for representative retained axes PC1, PC3, and PC15. PC1 and PC3 peak at \((r,k)=(72,17)\) and \((72,13)\), respectively, whereas PC15 peaks at \((5,5)\), illustrating heterogeneous radial–harmonic localization. **(D)** Explained-variance-weighted localization across the retained PCA-64 subspace in the prespecified 3×4 radial-region × harmonic-band partition. **(E)** Spectral-centroid × radial-centroid localization of all 64 retained PCA axes; marker area is proportional to PCA explained-variance ratio. Within PCA-64, which accounts for 44.65% of standardized representation variance, 78.54% of variance-weighted mapped morphology energy lies at \(k=5{:}24\), 66.84% in the outer radial zone (shells 49–72), and 51.30% jointly in outer-radial × \(k=5{:}24\) coordinates. These quantities are descriptive localization within the retained subspace; they do not denote semantic garment regions or a tested radial-by-harmonic interaction.


---

# References

An, L., & Li, W. (2014). An integrated approach to fashion flat sketches classification. *International Journal of Clothing Science and Technology*, 26(5), 346–366. https://doi.org/10.1108/IJCST-05-2013-0054

Arnia, F. (2020). *Clo-Sket* (Version 1) [Data set]. Mendeley Data. https://doi.org/10.17632/jt533nkhsf.1

Bhunia, A. K., Koley, S., Khilji, A. F. U. R., Sain, A., Chowdhury, P. N., Xiang, T., & Song, Y.-Z. (2022). Sketching without worrying: Noise-tolerant sketch-based image retrieval. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 999–1008.

Chaudhuri, A., Bhunia, A. K., Song, Y.-Z., & Dutta, A. (2023). Data-free sketch-based image retrieval. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 12084–12093.

Coifman, R. R., & Lafon, S. (2006). Diffusion maps. *Applied and Computational Harmonic Analysis*, 21(1), 5–30. https://doi.org/10.1016/j.acha.2006.04.006

Efron, B. (1979). Bootstrap methods: Another look at the jackknife. *The Annals of Statistics*, 7(1), 1–26. https://doi.org/10.1214/aos/1176344552

Hastie, T., & Stuetzle, W. (1989). Principal curves. *Journal of the American Statistical Association*, 84(406), 502–516. https://doi.org/10.1080/01621459.1989.10478797

Hinton, G. E., & Salakhutdinov, R. R. (2006). Reducing the dimensionality of data with neural networks. *Science*, 313(5786), 504–507. https://doi.org/10.1126/science.1127647

Islam, S. M., Joardar, S., & Sekh, A. A. (2024). A survey on fashion image retrieval. *ACM Computing Surveys*, 56(6). https://doi.org/10.1145/3636552

Jolliffe, I. T., & Cadima, J. (2016). Principal component analysis: A review and recent developments. *Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences*, 374(2065), 20150202. https://doi.org/10.1098/rsta.2015.0202

Kingma, D. P., & Welling, M. (2014). Auto-Encoding Variational Bayes. *International Conference on Learning Representations (ICLR)*. arXiv:1312.6114. https://doi.org/10.48550/arXiv.1312.6114

Koley, S., Bhunia, A. K., Sain, A., Chowdhury, P. N., Xiang, T., & Song, Y.-Z. (2024). How to handle sketch-abstraction in sketch-based image retrieval? *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 16859–16869.

Kuhl, F. P., & Giardina, C. R. (1982). Elliptic Fourier features of a closed contour. *Computer Graphics and Image Processing*, 18(3), 236–258. https://doi.org/10.1016/0146-664X(82)90034-X

Kunttu, I., Lepistö, L., Rauhamaa, J., & Visa, A. (2006). Multiscale Fourier descriptors for defect image retrieval. *Pattern Recognition Letters*, 27(2), 123–132. https://doi.org/10.1016/j.patrec.2005.08.022

Lee, Y., Kang, Y., & Kim, S. (2024). Automatic extraction of flat sketch design element from clothing images using artificial intelligence. *Journal of Engineered Fibers and Fabrics*, 19. https://doi.org/10.1177/15589250241228266

Lei, H.-P., Chen, S., Wang, M., He, X., Jia, W., & Li, S. (2021). A new algorithm for sketch-based fashion image retrieval based on cross-domain transformation. *Wireless Communications and Mobile Computing*, 2021, 5577735. https://doi.org/10.1155/2021/5577735

Li, J., Ling, Z., Niu, L., & Zhang, L. (2022). Zero-shot sketch-based image retrieval with structure-aware asymmetric disentanglement. *Computer Vision and Image Understanding*, 218, 103412. https://doi.org/10.1016/j.cviu.2022.103412

Ricard, J., Coeurjolly, D., & Baskurt, A. (2005). Generalizations of angular radial transform for 2D and 3D shape retrieval. *Pattern Recognition Letters*, 26(14), 2174–2186. https://doi.org/10.1016/j.patrec.2005.03.030

Rohlf, F. J., & Archie, J. W. (1984). A comparison of Fourier methods for the description of wing shape in mosquitoes (Diptera: Culicidae). *Systematic Zoology*, 33(3), 302–317. https://doi.org/10.2307/2413076

Tenenbaum, J. B., de Silva, V., & Langford, J. C. (2000). A global geometric framework for nonlinear dimensionality reduction. *Science*, 290(5500), 2319–2323. https://doi.org/10.1126/science.290.5500.2319

Yap, P.-T., Jiang, X., & Kot, A. C. (2010). Two-dimensional polar harmonic transforms for invariant image representation. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 32(7), 1259–1270. https://doi.org/10.1109/TPAMI.2009.119

Zahn, C. T., & Roskies, R. Z. (1972). Fourier descriptors for plane closed curves. *IEEE Transactions on Computers*, C-21(3), 269–281. https://doi.org/10.1109/TC.1972.5008949

Zhang, D., & Lu, G. (2002). Shape-based image retrieval using generic Fourier descriptor. *Signal Processing: Image Communication*, 17(10), 825–848. https://doi.org/10.1016/S0923-5965(02)00084-X
