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

Representing morphology compactly requires deciding not only how to compress a descriptor, but where simplification is justified. We study this problem for garment sketches using an explicit radial–angular morphology field. Each sketch is represented by a shell-conditional angular distribution \(P_i(\theta\mid r)\), whose Fourier coefficients define complex radial functions \(F_{i,k}(r)\). Using 2,300 sketches representing 230 garment identities across 23 categories, candidate radial encodings were evaluated separately within four prespecified angular-harmonic bands under garment-identity-disjoint validation and family-wise-error-rate-controlled inference. Compression support was harmonic-dependent: four-coefficient DCT encoding was supported for \(k=1{:}4\), four-coefficient db4-wavelet encoding for \(k=25{:}36\), whereas tested compression was not supported for \(k=5{:}24\), where the complete 72-shell radial structure was therefore preserved. The resulting DCT/raw/raw/wavelet representation reduced dimensionality from 2,592 to 1,504 complex coefficients (41.98%). At the latent level, tested autoencoder and variational-autoencoder representations did not establish a multiplicity-controlled held-out garment-identity retrieval advantage over same-dimensional PCA, although separate geometry audits detected nonlinear structure. PCA was therefore retained as the practical latent baseline without implying intrinsically linear morphology. Exact inverse mapping of retained PCA perturbations back to radial–harmonic coordinates showed heterogeneous morphology localization; within PCA-64, which accounted for 44.65% of standardized representation variance, 78.54% of variance-weighted mapped energy occurred at \(k=5{:}24\), 66.84% in the outer radial zone, and 51.30% jointly in outer-radial × intermediate-harmonic coordinates. These results support an evidence-controlled representation principle: compress where held-out evidence supports simplification, preserve complete structure otherwise, and retain explicit traceability from latent variation to the morphology coordinates from which the representation was constructed.

---

# Keywords

garment-sketch morphology; evidence-controlled representation; Fourier shape analysis; radial–angular representation; spectral compression; latent morphology; garment-identity-disjoint validation

---

# Running title

**Evidence-Controlled Garment Morphology Representation**

---

# Claim boundary

The title and abstract do not claim invention of Fourier descriptors, radial–angular shape representation, DCT or wavelet compression, PCA reconstruction, nonlinear latent modelling, or garment-sketch analysis. They do not claim literature-wide priority, universal transform optimality, intrinsic incompressibility of unsupported bands, universal PCA superiority, semantic interpretation of PCA axes or radial zones, or total-morphology interpretation of PCA-64 localization percentages. The nonlinear-geometry statement is kept separate from the task-based PCA/AE/VAE decision.
