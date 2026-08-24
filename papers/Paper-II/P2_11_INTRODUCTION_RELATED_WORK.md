# CLO-SKET Paper 2 — Introduction and Related Work

## Status

**MANUSCRIPT-FACING INTRODUCTION + RELATED WORK: CITATION-INTEGRATED**

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

A second representation question arises after this radial–spectral structure has been established. High-dimensional morphology can exhibit nonlinear geometry, but the existence of such geometry does not by itself demonstrate that a nonlinear encoder provides a better practical representation. Autoencoders and variational autoencoders can model nonlinear mappings, whereas PCA provides a simpler linear baseline with exact and transparent inverse structure. We therefore separate two questions that are often conflated:

\[
\text{Is nonlinear geometry detectable?}
\]

and

\[
\text{Does a nonlinear latent model provide validated task advantage?}
\]

Nonlinear alternatives are compared directly with same-dimensional PCA representations under garment-identity-disjoint evaluation and multiplicity-controlled inference. Geometric nonlinearity is then audited separately, so that evidence of curvature cannot retrospectively determine the model-selection conclusion. This distinction allows representational complexity, like radial compression, to **earn empirical support rather than being assumed from model flexibility alone**.

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

We study these questions using CLO-SKET, a controlled garment-sketch corpus containing 2,300 sketches representing 230 recovered garment identities across 23 garment categories. The repeated-identity structure is central to the experimental design: validation is organized so that sketches of the same garment identity do not appear across training and held-out groups. Representation selection is therefore evaluated on transfer to unseen garment identities rather than on replication-specific similarity.

The study makes three methodological contributions:

1. **Harmonic-conditioned, evidence-controlled radial representation selection.** We test radial compression separately across angular harmonic regimes and construct a heterogeneous representation in which compact bases are retained only where inferential support is established, while complete radial structure is preserved elsewhere.
2. **Evidence-controlled latent-complexity selection.** We compare PCA with nonlinear AE and VAE alternatives under the same identity-disjoint validation framework and distinguish predictive utility from the separate question of nonlinear geometry.
3. **Exact latent-to-morphology traceability.** We map retained PCA directions through the inverse hybrid representation into explicit radial–harmonic morphology fields, allowing latent variation to be localized without assigning unsupported semantic meaning.

The resulting experiments show that radial representation requirements are not uniform across the tested harmonic spectrum. Evidence supports compact representations at the lowest and highest tested harmonic ranges but not across the intermediate orders, yielding a DCT/raw/raw/wavelet hybrid rather than a globally imposed basis. Nonlinear encoders subsequently fail to establish a multiplicity-controlled task advantage over same-dimensional PCA despite separately detectable nonlinear geometry. Finally, inverse mapping of the retained PCA representation reveals structured but heterogeneous radial–harmonic localization of latent morphology.

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

Garment and fashion sketches have been studied for objectives that include classification, retrieval, design assistance, vectorization and image synthesis. The Wavelet Fourier Descriptor pipeline of An and Li (2014) is particularly relevant because it demonstrates handcrafted spectral shape analysis directly on fashion flat sketches. Other work has treated flats structurally: feature-based CAD systems decompose garments into modules such as bodices, sleeves, collars, cuffs and pockets and assemble new designs from those components (Lee and Kim, 2021). More recent systems use neural image-processing pipelines to extract flat-sketch design elements from clothing imagery through edge detection, vectorization and graph-based shape extraction (Lee et al., 2024).

A parallel literature represents fashion sketches through learned image features for cross-domain retrieval and generation. Fashion-specific sketch–photo retrieval has used cross-domain transformation to reduce the sketch/photo domain gap (Lei et al., 2021), while broader sketch-based image retrieval has continued to develop representation learning for zero-shot transfer, data-free learning, noise tolerance and abstraction-aware retrieval (Li et al., 2022; Bhunia et al., 2022; Chaudhuri et al., 2023; Koley et al., 2024). Recent fashion-retrieval surveys likewise position sketch-guided retrieval within a wider learned visual-retrieval ecosystem (Islam et al., 2024). These approaches are valuable when the target is semantic matching, cross-domain retrieval or learned visual invariance, but their representation objective differs from the present study. CLO-SKET does not attempt to infer garment construction modules, generate realistic garments, or assign semantic meanings to latent coordinates. Its target is narrower: to test how an explicit morphology field should allocate radial representational complexity across angular harmonic scale while preserving a mathematically traceable inverse.

This distinction also motivates the use of garment identity rather than category alone as the held-out unit. Category labels provide coarse semantic grouping, whereas repeated drawings of the same garment identity permit evaluation of whether a representation preserves identity-specific morphology across sketch realizations. The resulting validation question is therefore not simply whether dresses can be separated from trousers, but whether representation decisions transfer to garment identities absent from model fitting and candidate selection.

## 2.4 Linear latent representations, nonlinear encoders and manifold geometry

After representation construction, dimensionality reduction introduces a second complexity decision. PCA supplies an orthogonal variance-ordered coordinate system with a direct linear inverse to the original feature space (Jolliffe and Cadima, 2016). Autoencoders learn nonlinear low-dimensional representations through reconstruction objectives (Hinton and Salakhutdinov, 2006), while variational autoencoders introduce a probabilistic latent-variable formulation optimized through variational inference (Kingma and Welling, 2014). Nonlinear manifold methods—including principal curves, Isomap and diffusion maps—provide additional tools for diagnosing curved or locally low-dimensional structure (Hastie and Stuetzle, 1989; Tenenbaum et al., 2000; Coifman and Lafon, 2006).

The presence of nonlinear geometry, however, is logically distinct from evidence that a nonlinear encoder improves a held-out task. A curved data distribution can be detectable while a simpler linear representation remains competitive or preferable under finite-sample validation. CLO-SKET therefore separates these hypotheses experimentally. Same-dimensional AE and VAE representations are compared with PCA using identity-disjoint held-out retrieval and multiplicity-controlled inference, whereas curvature, local/global dimensionality and other manifold-oriented analyses are treated as separate geometric audits.

This separation prevents either result from being overinterpreted. Failure of a nonlinear encoder to establish task advantage does not prove that the underlying morphology is linear; conversely, evidence of curvature does not by itself justify replacing the task-validated representation with a nonlinear model. In this study, latent complexity is subjected to the same broader principle as radial compression: additional flexibility must be supported by the relevant validation evidence.

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
