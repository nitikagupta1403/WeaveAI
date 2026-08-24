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
