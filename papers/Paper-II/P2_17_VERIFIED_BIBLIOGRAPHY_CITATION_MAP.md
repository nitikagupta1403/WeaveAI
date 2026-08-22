# CLO-SKET Paper 2 — Verified Bibliography and Claim-to-Citation Map

## Status

**VERIFIED BIBLIOGRAPHY + CLAIM MAP: CORE SET LOCKED**

This document records the primary literature currently verified for Paper 2.

The purpose is to ensure that every literature statement in the manuscript is
supported by a source that actually establishes the corresponding methodological
precedent.

This bibliography is not intended to maximize citation count.

It is intended to provide:

1. foundational shape-analysis precedent;
2. the closest radial-angular spectral precedents;
3. multiscale and Fourier-wavelet precedent;
4. direct fashion-sketch precedent;
5. latent-geometry method references;
6. statistical-method references;
7. dataset provenance.

No citation supports the empirical results of the present CLO-SKET study.
Those results derive from the frozen computational evidence.

---

# 1. Citation classes

The bibliography is divided into four evidence classes.

## Class A — Direct methodological precedent

These papers overlap closely with the representation ideas in Paper 2.

Examples:

- Generic Fourier Descriptor;
- Angular Radial Transform;
- Polar Harmonic Transform;
- multiscale Fourier-wavelet descriptors.

These references are essential for defining what Paper 2 does **not** claim as new.

---

## Class B — Foundational / supporting methodology

These establish broader methods used or discussed in the manuscript.

Examples:

- classical Fourier descriptors;
- elliptic Fourier descriptors;
- PCA-related Fourier morphometrics;
- Isomap;
- principal curves;
- diffusion maps.

---

## Class C — Domain precedent

These establish prior computational work specifically on garment or fashion sketches.

The most important current example is the fashion-flat Wavelet Fourier Descriptor study.

---

## Class D — Statistical methodology and data provenance

These establish:

- bootstrap methodology;
- dataset provenance;
- other formal analysis tools where citation is appropriate.

---

# 2. R01 — Classical Fourier descriptors

## Reference

Zahn, C. T., & Roskies, R. Z. (1972).

**Fourier Descriptors for Plane Closed Curves.**

*IEEE Transactions on Computers*, C-21(3), 269–281.

DOI:

`10.1109/TC.1972.5008949`

## Evidence class

**B — Foundational**

## Verified methodological content

The paper develops Fourier descriptors for planar closed curves by expanding a
parametric representation of curve direction in a Fourier series.

It establishes classical precedent for:

- Fourier description of closed contours;
- shape analysis using harmonic coefficients;
- shape reconstruction from Fourier descriptors;
- symmetry characterization using Fourier coefficients.

## Paper 2 claim supported

Use this citation for statements such as:

> Fourier descriptors have long provided harmonic representations of planar shape.

or:

> Classical Fourier shape analysis represents closed contours using spectral coefficients.

## Paper 2 claim NOT supported

Do not cite Zahn and Roskies as precedent for:

- conditional probability fields \(P(\theta\mid r)\);
- radial-harmonic functions \(F_k(r)\);
- polar raster descriptors;
- harmonic-dependent radial compression;
- wavelet representations.

---

# 3. R02 — Elliptic Fourier contour representation

## Reference

Kuhl, F. P., & Giardina, C. R. (1982).

**Elliptic Fourier Features of a Closed Contour.**

*Computer Graphics and Image Processing*, 18(3), 236–258.

DOI:

`10.1016/0146-664X(82)90034-X`

## Evidence class

**B — Foundational / morphometric**

## Verified methodological content

The paper presents a direct procedure for obtaining Fourier coefficients from a
chain-encoded closed contour and describes normalization and reconstruction of
the resulting elliptic Fourier representation.

## Paper 2 claim supported

Use for statements such as:

> Fourier coefficients can provide reconstructable and normalized contour representations.

## Importance for novelty

This paper reinforces that:

\[
\text{Fourier coefficient reconstruction}
\]

is established prior art.

Paper 2 must therefore not claim novelty simply because latent perturbations can
ultimately be reconstructed through Fourier coefficients.

---

# 4. R03 — Fourier descriptors used for multivariate shape analysis

## Reference

Rohlf, F. J., & Archie, J. W. (1984).

**A Comparison of Fourier Methods for the Description of Wing Shape in Mosquitoes
(Diptera: Culicidae).**

*Systematic Zoology*, 33(3), 302–317.

DOI:

`10.2307/2413076`

## Evidence class

**B — Morphometric precedent**

## Verified methodological content

The study compares multiple Fourier-based representations of biological outlines,
including radial and tangent-angle Fourier descriptions and elliptic Fourier
descriptors, and analyzes the resulting descriptors using multivariate methods.

## Paper 2 claim supported

Use as precedent for:

> Fourier descriptors can serve as inputs to multivariate analysis of morphology.

## Novelty implication

Fourier representation followed by multivariate latent analysis is not itself a
Paper 2 novelty claim.

---

# 5. R04 — Generic Fourier Descriptor

## Reference

Zhang, D., & Lu, G. (2002).

**Shape-Based Image Retrieval Using Generic Fourier Descriptor.**

*Signal Processing: Image Communication*, 17(10), 825–848.

DOI:

`10.1016/S0923-5965(02)00084-X`

## Evidence class

**A — Direct methodological precedent**

## Verified methodological content

The Generic Fourier Descriptor is obtained by applying a two-dimensional Fourier
transform to a polar-raster sampled representation of shape.

The descriptor explicitly captures shape information in:

- radial directions;
- circular/angular directions.

## Paper 2 claim supported

Use this reference whenever stating that polar Fourier methods already encode
radial and angular shape information.

Recommended manuscript wording:

> Polar spectral shape representations have previously combined radial and
> angular information, including the Generic Fourier Descriptor of Zhang and Lu.

## Critical novelty boundary

Because GFD exists, Paper 2 must NOT claim:

> the first radial-angular Fourier representation;

or:

> the first Fourier descriptor to preserve radial and angular structure.

## Paper 2 distinction

Paper 2 instead retains:

\[
F_k(r)
\]

as a radial function for each angular harmonic and asks whether its radial
representation should vary with \(k\).

---

# 6. R05 — Angular Radial Transform / MPEG-7

## Reference

Ricard, J., Coeurjolly, D., & Baskurt, A. (2005).

**Generalizations of Angular Radial Transform for 2D and 3D Shape Retrieval.**

*Pattern Recognition Letters*, 26(14), 2174–2186.

DOI:

`10.1016/j.patrec.2005.03.030`

## Evidence class

**A — Direct methodological precedent**

## Verified methodological content

The paper describes Angular Radial Transform (ART) as:

- a moment-based image representation;
- a transform in polar coordinates;
- the MPEG-7 region-based shape descriptor.

ART uses a predetermined radial-angular basis and provides a compact descriptor.

## Paper 2 claim supported

Use for statements such as:

> Angular Radial Transform provides established precedent for compact shape
> description using separable radial and angular functions.

## Critical distinction

ART specifies the transform basis as part of the descriptor.

Paper 2 instead treats radial representation as a design choice to be tested
separately across angular harmonic ranges.

---

# 7. R06 — ART coefficient magnitude and phase

## Reference

Lee, J.-M., & Kim, W.-Y. (2012).

**A New Shape Description Method Using Angular Radial Transform.**

*IEICE Transactions on Information and Systems*, E95-D(6), 1628–1635.

DOI:

`10.1587/transinf.E95.D.1628`

## Evidence class

**A/B — Direct supporting precedent**

## Verified methodological content

The paper develops a rotation-invariant ART descriptor combining:

- ART coefficient magnitudes;
- aligned ART coefficient phases.

It demonstrates continuing use of ART as a polar region-shape representation.

## Paper 2 use

This reference may support a more detailed Related Work discussion of how ART
coefficients themselves can retain magnitude and phase information.

It is not mandatory if R05 is sufficient for the main ART precedent.

---

# 8. R07 — Polar Harmonic Transforms

## Reference

Yap, P.-T., Jiang, X., & Kot, A. C. (2010).

**Two-Dimensional Polar Harmonic Transforms for Invariant Image Representation.**

*IEEE Transactions on Pattern Analysis and Machine Intelligence*, 32(7), 1259–1270.

DOI:

`10.1109/TPAMI.2009.119`

## Evidence class

**A — Direct methodological precedent**

## Verified methodological content

The paper introduces a family of two-dimensional Polar Harmonic Transforms based
on orthogonal projection bases for rotation-invariant image representation.

The family provides explicit radial/angular harmonic representations over a
polar domain.

## Paper 2 claim supported

Use for statements such as:

> Polar harmonic transforms provide established orthogonal radial-angular image
> representations.

## Critical novelty boundary

Paper 2 cannot claim that the general idea

\[
R_n(r)e^{im\theta}
\]

or radial-angular harmonic decomposition is new.

## Paper 2 distinction

The Paper 2 contribution lies in testing the radial representation conditional on
angular harmonic band rather than specifying a uniform analytical radial basis.

---

# 9. R08 — Multiscale Fourier descriptors

## Reference

Kunttu, I., Lepistö, L., Rauhamaa, J., & Visa, A. (2006).

**Multiscale Fourier Descriptors for Defect Image Retrieval.**

*Pattern Recognition Letters*, 27(2), 123–132.

DOI:

`10.1016/j.patrec.2005.08.022`

## Evidence class

**A — Direct multiscale precedent**

## Verified methodological content

The paper introduces multiresolution Fourier shape descriptors.

One proposed method combines:

\[
\text{wavelet transform}
\]

with:

\[
\text{Fourier transform}.
\]

Fourier descriptors are constructed over multiscale wavelet coefficients.

## Paper 2 claim supported

Use for:

> Fourier and wavelet shape representations have previously been combined in
> multiscale descriptors.

## Critical novelty boundary

Paper 2 must NOT claim novelty for:

\[
\text{Fourier + wavelet}.
\]

## Paper 2 distinction

Paper 2 does not define wavelet processing as the universal descriptor.

Wavelet representation is retained only for the harmonic range where it survives
the inferential selection procedure.

---

# 10. R09 — Direct fashion-sketch Fourier/wavelet precedent

## Reference

An, L., & Li, W. (2014).

**An Integrated Approach to Fashion Flat Sketches Classification.**

*International Journal of Clothing Science and Technology*, 26(5), 346–366.

DOI:

`10.1108/IJCST-05-2013-0054`

## Evidence class

**C — Direct domain precedent**

## Verified methodological content

The paper studies classification of fashion-flat sketches using an integrated
pipeline containing:

- Wavelet Fourier Descriptor;
- linear discriminant analysis;
- extreme learning machine.

The descriptor combines discrete wavelet and Fourier transformations to extract
shape features from fashion-flat sketches.

## Paper 2 claim supported

Use for:

> Fourier-wavelet shape description has previously been applied specifically to
> fashion-flat sketches.

## Critical novelty boundary

This citation is mandatory.

Paper 2 must NOT claim:

> the first Fourier-wavelet garment-sketch method.

## Paper 2 distinction

An and Li use a predetermined Wavelet Fourier Descriptor for supervised
classification.

Paper 2 instead:

- retains explicit radial-harmonic structure;
- evaluates radial basis choices separately across harmonic ranges;
- uses garment-identity-disjoint validation;
- controls multiplicity;
- preserves full radial structure where compression is unsupported.

---

# 11. R10 — CLO-SKET dataset

## Reference

Arnia, F. (2020).

**Clo-Sket.**

Mendeley Data, Version 1.

DOI:

`10.17632/jt533nkhsf.1`

## Evidence class

**D — Dataset provenance**

## Verified dataset content

The dataset documentation reports:

- 2,300 garment sketches;
- 230 underlying clothing photographs/design instances;
- 23 subcategories;
- 10 examples per subcategory;
- sketches produced by multiple sketchers.

## Paper 2 claim supported

Use for dataset provenance and basic dataset structure.

## Important distinction

Paper 2's reconstructed garment-identity identifiers and grouped-validation logic
are present-study analytical constructions.

The dataset citation establishes the dataset origin, not every identity-recovery
step in the present analysis.

---

# 12. R11 — Isomap

## Reference

Tenenbaum, J. B., de Silva, V., & Langford, J. C. (2000).

**A Global Geometric Framework for Nonlinear Dimensionality Reduction.**

*Science*, 290(5500), 2319–2323.

DOI:

`10.1126/science.290.5500.2319`

## Evidence class

**B — Nonlinear geometry methodology**

## Verified methodological content

The paper introduces Isomap as a nonlinear dimensionality-reduction method that
uses local neighborhood distances to estimate global manifold geometry.

## Paper 2 claim supported

Use when describing Isomap as a geometric nonlinear-dimensionality-reduction
audit.

## Claim NOT supported

This citation does not establish that CLO-SKET lies on an Isomap manifold.

That is an empirical question of the present study.

---

# 13. R12 — Principal curves

## Reference

Hastie, T., & Stuetzle, W. (1989).

**Principal Curves.**

*Journal of the American Statistical Association*, 84(406), 502–516.

DOI:

`10.1080/01621459.1989.10478797`

## Evidence class

**B — Nonlinear geometry methodology**

## Verified methodological content

Principal curves are defined as smooth one-dimensional curves passing through the
middle of a multidimensional dataset and provide a nonlinear summary of the data.

## Paper 2 claim supported

Use when introducing the principal-curve geometry audit.

## Paper 2 empirical boundary

The source establishes the method.

The Paper 2 result:

> a stable one-dimensional principal trajectory was not established

comes from CLO-SKET analysis, not from this citation.

---

# 14. R13 — Diffusion maps

## Reference

Coifman, R. R., & Lafon, S. (2006).

**Diffusion Maps.**

*Applied and Computational Harmonic Analysis*, 21(1), 5–30.

DOI:

`10.1016/j.acha.2006.04.006`

## Evidence class

**B — Nonlinear geometry methodology**

## Verified methodological content

Diffusion maps construct low-dimensional coordinates from diffusion processes on
a data graph and provide a multiscale geometric representation based on diffusion
distances.

## Paper 2 claim supported

Use when describing diffusion maps as a nonlinear geometric characterization
method.

## Paper 2 boundary

The citation establishes the algorithm, not whether diffusion geometry is an
appropriate final representation for CLO-SKET.

---

# 15. R14 — Bootstrap

## Reference

Efron, B. (1979).

**Bootstrap Methods: Another Look at the Jackknife.**

*The Annals of Statistics*, 7(1), 1–26.

DOI:

`10.1214/aos/1176344552`

## Evidence class

**D — Statistical methodology**

## Verified methodological content

The paper introduces the bootstrap as a general resampling method for estimating
the sampling distribution of statistics.

## Paper 2 claim supported

Use as foundational citation for bootstrap uncertainty estimation.

## Important Paper 2 distinction

The specific choice to bootstrap **complete garment identities** is a feature of
the present clustered inferential design.

Efron establishes bootstrap methodology generally, not the present grouping unit.

---

# 16. Optional additional statistical reference — multiplicity

The present analysis uses a max-statistic family-wise-error-rate procedure.

Before the final manuscript bibliography is closed, the exact theoretical
reference should be selected to match the implementation.

Likely methodological family:

Westfall and Young, resampling-based multiple-testing procedures.

Do not insert a citation until the precise implementation-to-reference match is
verified.

Status:

\[
\boxed{
\text{VERIFY BEFORE FINAL BIBLIOGRAPHY LOCK}
}
\]

---

# 17. Optional PCA reference

PCA is sufficiently standard that a dedicated citation may or may not be required
depending on CVIU style.

If included, use a standard authoritative source such as a recognized PCA
monograph rather than a secondary web source.

The more important Related Work citation is not PCA itself but Fourier
morphometrics / Fourier descriptors used in multivariate analysis.

Current supporting precedents:

- Kuhl & Giardina (1982);
- Rohlf & Archie (1984).

Status:

\[
\boxed{
\text{PCA GENERAL REFERENCE OPTIONAL}
}
\]

---

# 18. Claim-to-citation map

| Manuscript claim | Required citation(s) | Citation role |
|---|---|---|
| Fourier descriptors provide classical harmonic contour representations | Zahn & Roskies (1972) | Foundational |
| Closed contours can be reconstructed/normalized using elliptic Fourier coefficients | Kuhl & Giardina (1982) | Foundational morphometric |
| Fourier shape coefficients have long been used in multivariate morphology analysis | Rohlf & Archie (1984) | Morphometric precedent |
| Polar Fourier descriptors can encode radial and circular shape information | Zhang & Lu (2002) | Direct precedent |
| ART is an established radial-angular region shape descriptor | Ricard et al. (2005) | Direct precedent |
| ART coefficient magnitude/phase have been used for invariant shape description | Lee & Kim (2012) | Supporting ART precedent |
| Polar harmonic transforms provide orthogonal radial-angular harmonic representations | Yap et al. (2010) | Direct precedent |
| Wavelet and Fourier transforms have been combined for multiscale shape descriptors | Kunttu et al. (2006) | Direct precedent |
| Wavelet Fourier descriptors have already been applied to fashion-flat sketches | An & Li (2014) | Direct fashion precedent |
| CLO-SKET contains 2,300 sketches across 23 subcategories | Arnia (2020) | Dataset provenance |
| Isomap is a nonlinear manifold-learning method based on neighborhood geometry | Tenenbaum et al. (2000) | Method |
| Principal curves provide smooth nonlinear one-dimensional summaries | Hastie & Stuetzle (1989) | Method |
| Diffusion maps provide diffusion-based nonlinear geometric coordinates | Coifman & Lafon (2006) | Method |
| Bootstrap resampling estimates sampling distributions | Efron (1979) | Statistics |

---

# 19. Related Work paragraph-to-reference map

## Paragraph: Classical Fourier shape representation

Cite:

- Zahn & Roskies (1972);
- Kuhl & Giardina (1982).

Core message:

\[
\text{Fourier shape description is established}.
\]

---

## Paragraph: Polar spectral shape representation

Cite:

- Zhang & Lu (2002);
- Ricard et al. (2005);
- Yap et al. (2010).

Core message:

\[
\text{radial-angular spectral representation is established}.
\]

Therefore Paper 2 does not claim novelty at this level.

---

## Paragraph: Multiscale / wavelet representations

Cite:

- Kunttu et al. (2006).

Core message:

\[
\text{Fourier + wavelet shape representation is established}.
\]

---

## Paragraph: Fashion-sketch precedent

Cite:

- An & Li (2014).

Core message:

\[
\text{fashion-flat Fourier-wavelet descriptors already exist}.
\]

This is essential to the novelty firewall.

---

## Paragraph: Latent and nonlinear geometry

Cite as needed:

- Rohlf & Archie (1984) for multivariate Fourier morphology;
- Tenenbaum et al. (2000) for Isomap;
- Hastie & Stuetzle (1989) for principal curves;
- Coifman & Lafon (2006) for diffusion maps.

---

# 20. Exact novelty comparison

## Existing literature establishes

\[
\text{Fourier shape descriptors}
\]

\[
+
\]

\[
\text{polar radial-angular transforms}
\]

\[
+
\]

\[
\text{polar harmonic transforms}
\]

\[
+
\]

\[
\text{wavelet-Fourier multiscale descriptors}
\]

\[
+
\]

\[
\text{fashion-specific Wavelet Fourier Descriptors}.
\]

---

## Paper 2 therefore must NOT claim novelty for

- Fourier decomposition;
- polar coordinates;
- radial-angular transforms;
- wavelets;
- Fourier-wavelet combination;
- PCA of spectral shape features.

---

## Current differentiating contribution

The reviewed literature does not provide a close precedent identified so far for
the complete Paper 2 chain:

\[
F_k(r)
\]

\[
\downarrow
\]

\[
\text{test radial representation separately by harmonic band}
\]

\[
\downarrow
\]

\[
\text{complete held-out garment identities}
\]

\[
\downarrow
\]

\[
\text{multiplicity-controlled inference}
\]

\[
\downarrow
\]

\[
\begin{cases}
\text{compress}, & \text{if supported}\\
\text{preserve complete radial structure}, & \text{otherwise}
\end{cases}
\]

\[
\downarrow
\]

\[
\text{heterogeneous DCT/raw/raw/wavelet representation}.
\]

This remains the primary novelty candidate.

Absence of a close precedent in the current audit is not proof of absolute
literature priority.

---

# 21. Safe Related Work wording

Recommended:

> Fourier descriptors provide longstanding spectral representations of shape,
> including contour-based and reconstructable formulations
> [Zahn and Roskies, 1972; Kuhl and Giardina, 1982].

> Polar spectral descriptors extend shape representation to radial and angular
> coordinates. The Generic Fourier Descriptor applies a two-dimensional Fourier
> transform to a polar-raster sampled shape, while Angular Radial Transform and
> Polar Harmonic Transform families use explicit radial-angular bases
> [Zhang and Lu, 2002; Ricard et al., 2005; Yap et al., 2010].

> Fourier and wavelet representations have also been combined in multiscale shape
> descriptors [Kunttu et al., 2006], including a Wavelet Fourier Descriptor
> developed specifically for fashion-flat sketch classification
> [An and Li, 2014].

Then the gap:

> These methods establish the usefulness of Fourier, polar, and multiscale shape
> representations. The present study addresses a different question: whether the
> radial encoding itself should be selected conditionally on angular harmonic
> scale using held-out statistical evidence.

---

# 22. Unsafe wording

Do not write:

> Previous Fourier descriptors lose radial information.

Generic Fourier Descriptor and ART make this overly broad.

Do not write:

> No previous work combines Fourier and wavelets.

False.

Do not write:

> No previous work uses Fourier descriptors for fashion sketches.

False.

Do not write:

> Paper 2 introduces radial-angular harmonic shape analysis.

Too broad given ART and PHT precedent.

Do not write:

> PCA reconstruction of Fourier morphology is new.

Fourier morphometric reconstruction and multivariate analysis have established
precedent.

---

# 23. Bibliography — core verified set

Arnia, F. (2020). *Clo-Sket* (Version 1) [Data set]. Mendeley Data.
DOI: 10.17632/jt533nkhsf.1

An, L., & Li, W. (2014). An integrated approach to fashion flat sketches
classification. *International Journal of Clothing Science and Technology*,
26(5), 346–366.
DOI: 10.1108/IJCST-05-2013-0054

Coifman, R. R., & Lafon, S. (2006). Diffusion maps.
*Applied and Computational Harmonic Analysis*, 21(1), 5–30.
DOI: 10.1016/j.acha.2006.04.006

Efron, B. (1979). Bootstrap methods: Another look at the jackknife.
*The Annals of Statistics*, 7(1), 1–26.
DOI: 10.1214/aos/1176344552

Hastie, T., & Stuetzle, W. (1989). Principal curves.
*Journal of the American Statistical Association*, 84(406), 502–516.
DOI: 10.1080/01621459.1989.10478797

Kuhl, F. P., & Giardina, C. R. (1982). Elliptic Fourier features of a closed
contour. *Computer Graphics and Image Processing*, 18(3), 236–258.
DOI: 10.1016/0146-664X(82)90034-X

Kunttu, I., Lepistö, L., Rauhamaa, J., & Visa, A. (2006). Multiscale Fourier
descriptors for defect image retrieval. *Pattern Recognition Letters*, 27(2),
123–132.
DOI: 10.1016/j.patrec.2005.08.022

Lee, J.-M., & Kim, W.-Y. (2012). A new shape description method using angular
radial transform. *IEICE Transactions on Information and Systems*, E95-D(6),
1628–1635.
DOI: 10.1587/transinf.E95.D.1628

Ricard, J., Coeurjolly, D., & Baskurt, A. (2005). Generalizations of angular
radial transform for 2D and 3D shape retrieval. *Pattern Recognition Letters*,
26(14), 2174–2186.
DOI: 10.1016/j.patrec.2005.03.030

Rohlf, F. J., & Archie, J. W. (1984). A comparison of Fourier methods for the
description of wing shape in mosquitoes (Diptera: Culicidae).
*Systematic Zoology*, 33(3), 302–317.
DOI: 10.2307/2413076

Tenenbaum, J. B., de Silva, V., & Langford, J. C. (2000). A global geometric
framework for nonlinear dimensionality reduction. *Science*, 290(5500),
2319–2323.
DOI: 10.1126/science.290.5500.2319

Yap, P.-T., Jiang, X., & Kot, A. C. (2010). Two-dimensional polar harmonic
transforms for invariant image representation.
*IEEE Transactions on Pattern Analysis and Machine Intelligence*, 32(7),
1259–1270.
DOI: 10.1109/TPAMI.2009.119

Zahn, C. T., & Roskies, R. Z. (1972). Fourier descriptors for plane closed
curves. *IEEE Transactions on Computers*, C-21(3), 269–281.
DOI: 10.1109/TC.1972.5008949

Zhang, D., & Lu, G. (2002). Shape-based image retrieval using generic Fourier
descriptor. *Signal Processing: Image Communication*, 17(10), 825–848.
DOI: 10.1016/S0923-5965(02)00084-X

---

# 24. References still requiring deliberate decision

The following should not be inserted automatically.

## Multiple-testing reference

Need to identify the reference that most precisely matches the frozen max-statistic
FWER implementation.

Status:

**VERIFY IMPLEMENTATION FIRST**

---

## PCA reference

Optional because PCA is a standard method.

If CVIU expects a reference, select an authoritative primary/monograph source.

---

## DCT reference

Not required merely because DCT is used, unless the Methods discussion requires
historical attribution.

---

## Wavelet/db4 reference

A wavelet reference may be useful if the implementation needs the formal db4
definition.

If included, choose the appropriate Daubechies primary/book reference.

---

## Autoencoder/VAE references

Include only if these specific model classes remain explicitly discussed in the
final main manuscript.

If moved largely to Supplement, references can accompany the Supplementary Methods.

---

# 25. Citation-priority hierarchy

When multiple citations support one statement, prefer:

1. original methodological paper;
2. authoritative journal source;
3. primary domain application;
4. review only when broad context is needed.

Avoid citing a modern review for a method whose primary source is readily
available.

---

# 26. Final bibliography firewall

Every citation must satisfy:

\[
\boxed{
\text{paper actually supports adjacent claim}
}
\]

and not merely:

\[
\text{paper contains similar keywords}.
\]

Likewise:

\[
\boxed{
\text{literature citation}
\neq
\text{evidence for CLO-SKET result}.
}
\]

Present-study effects, confidence intervals, p-values, dimensions, and morphology
localization percentages derive exclusively from the frozen Paper 2 evidence.

---

# 27. Step 17 lock

\[
\boxed{
\textbf{PAPER 2 CORE VERIFIED BIBLIOGRAPHY — LOCKED}
}
\]

The closest precedent structure is now explicit:

\[
\text{classical Fourier descriptors}
\]

\[
\downarrow
\]

\[
\text{polar Fourier / ART / PHT}
\]

\[
\downarrow
\]

\[
\text{multiscale Fourier-wavelet descriptors}
\]

\[
\downarrow
\]

\[
\text{fashion-specific Wavelet Fourier Descriptor}
\]

while Paper 2 contributes at the level of:

\[
\boxed{
\textbf{evidence-controlled harmonic-conditioned radial representation selection}
}
\]

rather than at the level of inventing the underlying transforms.

Next:

\[
\boxed{
\textbf{STEP 18 — CITATION-INTEGRATED CVIU MANUSCRIPT}
}
\]

Step 18 should replace every `[CITATIONS]` placeholder in the assembled manuscript
with the verified references above and tighten the Related Work so that each
precedent is compared explicitly with Paper 2.