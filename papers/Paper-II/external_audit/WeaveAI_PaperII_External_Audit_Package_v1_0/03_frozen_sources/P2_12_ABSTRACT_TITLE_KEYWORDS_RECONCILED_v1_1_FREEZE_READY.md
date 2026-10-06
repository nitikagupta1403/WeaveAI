# CLO-SKET Paper 2 — Reconciled Abstract, Title, and Keywords v1.1

## Status

**FREEZE-READY ABSTRACT + TITLE + KEYWORDS v1.1 — RECONCILED WITH P2_13 v1.0**

No new scientific claim is introduced here. The wording reflects the reconciled manuscript hierarchy:

\[
\boxed{
\text{representation validity}
\rightarrow
\text{evidence-controlled representation allocation}
\rightarrow
\text{traceable latent interpretation}
}
\]

---

# Preferred Title

**Auditing and Allocating Representation Complexity in Radial–Spectral Garment Morphology**

### Why this is preferred

This title keeps both principal contributions visible:

1. the representation-validity audit; and
2. the evidence-controlled allocation of radial representation complexity.

It avoids reducing the paper to a padding/support study while also avoiding the pre-05K framing in which representation selection appeared to be the first methodological question.

It does not imply invention of Fourier descriptors, polar coordinates, scale normalization, DCT, wavelets, or PCA.

---

# Alternative Title 1

**Representation Validity and Evidence-Controlled Radial–Spectral Encoding of Garment Sketches**

This version is more explicit and manuscript-like, but slightly longer.

---

# Alternative Title 2

**Evidence-Controlled Radial–Spectral Garment Morphology under Audited Raster Support**

This version emphasizes the 05K result more strongly and is therefore less preferred as the general title.

---

# Abstract

Interpreting structured morphology representations requires distinguishing object-related structure from variation introduced by the observation frame. We study this problem in a radial–angular representation of garment sketches whose angular Fourier transform retains explicit radial harmonic functions. Using 2,300 sketches representing 230 garment identities across 23 categories, we first audited the historical raster-relative coordinate system. A controlled same-pixel intervention enlarged only the surrounding raster support, without resizing or resampling the garment patch. Under this intervention, angular spectral allocation changed systematically in the raster-relative representation, whereas a matched object-relative construction remained numerically invariant. Separately, the representation-selection analysis had already been frozen under the historical raster-relative coordinate system; it evaluated radial encoding across four prespecified angular harmonic bands using garment-identity-disjoint validation and multiplicity-controlled inference. Compact four-coefficient DCT and db4-wavelet encodings were supported for the lowest and highest tested harmonic bands, respectively, while complete 72-shell radial structure was preserved in the intermediate bands where tested compression was not supported. The resulting heterogeneous DCT/raw/raw/wavelet representation reduced coefficient count by 41.98% relative to the complete radial-harmonic field. Conditional on this historical hybrid, nonlinear AE/VAE alternatives did not establish a multiplicity-controlled task advantage over same-dimensional PCA, despite separately detectable nonlinear pairwise structure. Exact inverse mapping localized retained PCA variation back to radial–harmonic morphology. Together, the results support a three-stage principle: audit the measurement frame, allocate representation complexity only where held-out evidence supports it, and keep retained latent variation traceable to explicit morphology coordinates.

---

# Keywords

garment-sketch morphology; representation validity; raster support; evidence-controlled representation; radial–angular Fourier analysis; spectral compression; latent morphology; garment-identity-disjoint validation

---

# Running Title

**Audited Radial–Spectral Garment Morphology**

---

# Claim Boundary

The title and abstract do **not** claim:

- a new Fourier transform;
- a new polar or radial–angular coordinate system;
- a new scale-normalization method;
- universal support invariance;
- universal descriptor superiority;
- intrinsic incompressibility of the intermediate harmonic bands;
- universal PCA superiority;
- semantic interpretation of PCA axes, harmonic bands, or radial zones;
- absolute literature-wide priority for the same-pixel support audit.

The support result is restricted to the tested historical raster-relative representation and controlled same-pixel intervention.

The object-relative construction is presented as a matched control, not as the final Paper-II replacement representation.

The historical hybrid remains:

\[
\mathrm{DCT}_4/
\mathrm{RAW}_{72}/
\mathrm{RAW}_{72}/
\mathrm{db4}_4,
\]

and its selection remains conditional on the coordinate system in which the original analysis was performed.

The literature-facing novelty boundary remains:

> **We did not identify a direct precedent in the reviewed literature for the specific controlled same-pixel raster-support audit used here.**

This is not an absolute priority claim.
