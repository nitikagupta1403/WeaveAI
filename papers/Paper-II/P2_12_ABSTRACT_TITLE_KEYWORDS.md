# CLO-SKET Paper 2 — Abstract, Title, and Keywords

## Status

**MANUSCRIPT-FACING TITLE + ABSTRACT + KEYWORDS: ALIGNED WITH FINAL EVIDENCE-CONTROLLED SPINE**

No new scientific claim is introduced here. Wording is aligned with the frozen Methods, Results, Discussion, and novelty boundary.

---

# Title

**Evidence-Controlled Radial–Spectral Representation of Garment-Sketch Morphology**

This title foregrounds the methodological contribution rather than the individual transforms used to implement it. It avoids implying that Fourier, DCT, wavelets, or radial–angular shape analysis are themselves introduced by this study.

---

# Abstract

Compact spectral shape descriptors commonly apply one encoding rule across the transform domain, although representational requirements may vary with scale. We test this assumption for garment-sketch morphology using a conditional radial-angular representation whose angular Fourier transform yields explicit radial harmonic functions. On 2,300 sketches representing 230 garment identities in 23 categories, candidate radial encodings were evaluated separately across four prespecified harmonic bands using garment-identity-disjoint validation and family-wise-error-rate-controlled inference. Compact four-coefficient DCT and db4-wavelet representations were supported for the lowest and highest tested harmonic bands, respectively, whereas tested compression was not supported for the intermediate harmonics, for which complete 72-shell radial structure was preserved. The resulting heterogeneous DCT/raw/raw/wavelet representation reduced coefficient count by 41.98% without imposing uniform compression. Nonlinear AE/VAE alternatives subsequently failed to establish a multiplicity-controlled task advantage over same-dimensional PCA, despite separately detectable nonlinear pairwise structure. Exact inverse mapping of the retained PCA representation localized latent variation back to radial-harmonic morphology, with most variance-weighted mapped energy concentrated in intermediate harmonics and outer radial shells. These findings introduce an evidence-controlled strategy for allocating representational complexity within a structured morphology field: compression is accepted where held-out evidence supports it, unsupported structure is preserved, and latent variation remains mathematically traceable to the coordinates on which representation decisions were made.

---

# Keywords

garment-sketch morphology; evidence-controlled representation; Fourier shape analysis; radial–angular representation; spectral compression; latent morphology; garment-identity-disjoint validation

---

# Running title

**Evidence-Controlled Garment Morphology Representation**

---

# Claim boundary

The title and abstract do not claim invention of Fourier descriptors, radial–angular shape representation, DCT or wavelet compression, PCA reconstruction, nonlinear latent modelling, or garment-sketch analysis. They do not claim literature-wide priority, universal transform optimality, intrinsic incompressibility of unsupported bands, universal PCA superiority, semantic interpretation of PCA axes or radial zones, or total-morphology interpretation of PCA-64 localization percentages. The nonlinear-geometry statement is kept separate from the task-based PCA/AE/VAE decision.
