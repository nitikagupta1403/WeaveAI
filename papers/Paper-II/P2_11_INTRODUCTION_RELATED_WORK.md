# CLO-SKET Paper 2 — Introduction and Related Work

## Status

**MANUSCRIPT-FACING INTRODUCTION + RELATED WORK: CITATION-INTEGRATED**

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
