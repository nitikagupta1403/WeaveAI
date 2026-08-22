# CLO-SKET Paper 2 — Novelty and Claim Lock

## Status

**Novelty and claim positioning: LOCKED PROVISIONALLY AGAINST THE CURRENT LITERATURE AUDIT**

This document freezes the manuscript-level contribution language for Paper 2.

It does not claim absolute priority over all published literature.

If later literature review reveals a closer precedent, this file must be revised before submission.

---

# 1. Final research gap

Existing shape-analysis literature already provides:

- Fourier descriptors;
- polar Fourier descriptors;
- angular-radial transforms;
- polar harmonic transforms;
- wavelet shape descriptors;
- Fourier-wavelet descriptors;
- multiscale Fourier representations;
- PCA of Fourier shape coefficients;
- reconstruction of shape variation along principal axes.

Fashion-specific prior work also includes Fourier- and wavelet-based shape descriptors for fashion-flat classification.

Therefore Paper 2 does **not** address the gap:

> How can Fourier, polar, wavelet, or PCA techniques be applied to garment sketches?

That gap is already occupied.

The more specific gap addressed here is:

> **Given an explicit radial-angular Fourier morphology field \(F_k(r)\), should radial structure be represented uniformly across angular harmonic orders, or should radial representation be selected conditionally on harmonic scale using held-out statistical evidence?**

A second gap is:

> **When a heterogeneous radial-spectral representation is learned from such evidence, can its retained latent variation be mapped exactly back into radial-harmonic morphology without assigning unsupported semantic meaning to latent coordinates?**

---

# 2. Primary methodological contribution

The primary contribution of Paper 2 is:

\[
\boxed{
\textbf{harmonic-conditioned, evidence-controlled radial representation selection}
}
\]

Specifically, building on the shared radial-angular Fourier
measurement substrate, the method:

1. takes the full radial-harmonic field

\[
F_k(r)
\]

as its representation-selection object;

2. retains radial location \(r\) and angular harmonic order \(k\)
explicitly during representation selection;

3. evaluates candidate radial representations separately across prespecified harmonic bands;

4. performs validation using complete held-out garment identities;

5. controls simultaneous inference across representation choices;

6. applies compact radial compression only where statistical support is established;

7. preserves complete radial structure where compression is not supported;

8. combines the resulting heterogeneous radial representations into one frozen hybrid spectral representation.

The resulting representation is:

\[
k=1{:}4
\rightarrow
\mathrm{DCT}_4,
\]

\[
k=5{:}12
\rightarrow
\mathrm{RAW}_{72},
\]

\[
k=13{:}24
\rightarrow
\mathrm{RAW}_{72},
\]

\[
k=25{:}36
\rightarrow
\mathrm{db4\ wavelet}_4.
\]

---

# 3. Primary contribution sentence

The preferred manuscript contribution sentence is:

> **We introduce an evidence-controlled radial-spectral representation strategy in which radial encoding is selected separately across angular harmonic bands using garment-identity-disjoint, multiplicity-controlled validation, yielding a heterogeneous hybrid representation that compresses supported bands while preserving complete radial structure where compression is not supported.**

This is the main methodological contribution statement.

---

# 4. Short contribution formulation

For Abstract or Introduction use:

> **Rather than imposing one radial basis across the Fourier field, we select radial representation conditionally on angular harmonic scale using identity-disjoint statistical evidence.**

---

# 5. One-line conceptual contribution

\[
\boxed{
\textbf{The contribution is not a new transform; it is an evidence-controlled strategy for deciding how different parts of the transform should be represented.}
}
\]

---

# 6. Secondary methodological contribution

The secondary methodological contribution is exact latent-to-spectral interpretation.

For PCA direction \(j\),

\[
\Delta x_j
\rightarrow
\Delta F_j(r,k)
\]

through the exact frozen inverse representation.

Morphology energy is then defined as

\[
E_j(r,k)
=
|\Delta F_j(r,k)|^2.
\]

This permits sign-invariant localization of latent variation in explicit radial-harmonic coordinates.

Preferred wording:

> **We additionally map standardized PCA perturbations through the exact inverse hybrid representation to quantify where retained latent variation is localized in radial-harmonic Fourier space.**

This is a secondary contribution because PCA-based Fourier morphology reconstruction has prior precedent, even though the exact hybrid inverse and energy-localization formulation appears distinctive.

---

# 7. Primary empirical finding

The primary inferential empirical finding is:

\[
\boxed{
\text{support for radial compression differs across angular harmonic scale}
}
\]

Specifically:

\[
k=1{:}4
\]

supports compact DCT radial representation,

\[
k=25{:}36
\]

supports compact db4-wavelet radial representation,

while tested compression is not supported for

\[
k=5{:}24.
\]

Preferred wording:

> **Radial representation requirements differed across angular harmonic bands under the tested identity-disjoint inferential framework.**

Avoid:

> radial complexity increases with harmonic frequency.

The results do not establish a monotonic law.

---

# 8. Secondary empirical finding

Within the retained PCA-64 subspace:

\[
78.54\%
\]

of variance-weighted mapped morphology energy occurs in

\[
k=5{:}24,
\]

\[
66.84\%
\]

occurs in the outer radial zone,

and

\[
51.30\%
\]

occurs jointly in the outer-radial × intermediate-harmonic region.

Preferred wording:

> **Within the retained PCA-64 subspace, mapped morphology energy showed strong intermediate-harmonic and outer-radial organization.**

This remains descriptive.

It is not a statistical interaction claim.

---

# 9. Third scientific contribution

Paper 2 also makes a methodological distinction between:

\[
\text{nonlinear geometry}
\]

and

\[
\text{nonlinear model utility}.
\]

The tested nonlinear latent models did not establish a multiplicity-controlled task advantage over PCA.

At the same time, nonlinear geometry audits showed departures from a purely linear geometric description.

Preferred wording:

> **The analysis separates nonlinear geometric structure from nonlinear-model utility: detectable nonlinear geometry did not establish the need to replace PCA as the validated practical latent representation.**

This is a scientific interpretation, not an algorithmic novelty claim.

---

# 10. Closest-prior-work differentiation

## 10.1 Versus classical Fourier descriptors

Prior work:

- represents contour or shape signals using Fourier coefficients;
- often truncates coefficients for compact representation.

Paper 2 differs because:

- the morphology field remains indexed by radius;
- radial representation is not uniformly truncated;
- compression decisions are tested separately across harmonic bands;
- unsupported compression leads to preservation rather than forced reduction.

Therefore:

> **Paper 2 does not introduce Fourier shape description; > **Paper 2 does not introduce Fourier shape description; it develops
> and evaluates evidence-conditioned radial representation within an
> angular Fourier morphology field.**

---

## 10.2 Versus Generic Fourier Descriptor

Generic Fourier Descriptor uses a Fourier transform over a polar-raster shape representation and encodes radial and circular spectral information.

Paper 2 differs because:

- it begins with a shell-conditioned angular probability field

\[
P(\theta\mid r);
\]

- performs angular Fourier analysis while retaining \(r\) explicitly;

- treats the radial dependence of \(F_k(r)\) as a representation-selection problem;

- does not impose one fixed transform design over all radial-angular frequencies;

- uses held-out inference to determine whether and how individual harmonic ranges should be compressed.

Safe wording:

> **Unlike fixed polar Fourier descriptors, the present approach treats radial encoding as an empirically selected component of each harmonic range.**

Do not say:

> Unlike previous work, we retain radial and angular information.

That would be false.

---

## 10.3 Versus Angular Radial Transform / Polar Harmonic Transform

ART, PHT, and related methods use predetermined radial and angular basis functions such as

\[
R_n(r)e^{im\theta}.
\]

Paper 2 differs because the radial basis is not fixed uniformly in advance.

Instead:

\[
\boxed{
\text{radial representation is selected conditionally on angular harmonic scale}
}
\]

and different harmonic bands may use:

- DCT;
- raw radial coefficients;
- wavelets.

Safe wording:

> **Whereas classical radial-angular transforms specify the radial basis analytically, our framework treats radial representation as an inferentially evaluated design choice that may differ across harmonic ranges.**

---

## 10.4 Versus Fourier-wavelet descriptors

Fourier-wavelet combinations and multiscale Fourier descriptors are established.

Paper 2 therefore does not claim novelty for combining Fourier and wavelets.

The distinction is:

> wavelet representation is not assumed globally.

Wavelet compression is retained only for the harmonic band where it receives inferential support.

Safe wording:

> **Wavelets constitute one candidate radial basis rather than the defining representation; they are retained only where supported by held-out inference.**

---

## 10.5 Versus fashion-specific Wavelet Fourier Descriptor

Fashion-flat classification has previously used Wavelet Fourier Descriptors.

Paper 2 differs in research objective and representation logic.

Prior fashion-flat work:

- constructs a predetermined descriptor;
- uses it for supervised classification.

Paper 2:

- analyzes morphology rather than optimizing classification;
- evaluates radial representation choices separately across harmonic ranges;
- retains unsupported-to-compress bands in full;
- performs grouped statistical inference at garment-identity level;
- interprets the resulting latent structure back in radial-harmonic coordinates.

Safe wording:

> **The contribution is not the application of wavelet-Fourier descriptors to fashion sketches, but inferential selection of heterogeneous radial encodings across the angular Fourier field.**

---

## 10.6 Versus PCA-based Fourier morphometrics

Prior morphometric work commonly applies PCA to Fourier coefficients and reconstructs shape variation along principal axes.

Paper 2 therefore does not claim novelty for:

\[
\text{Fourier}
\rightarrow
\text{PCA}.
\]

The secondary distinction is:

\[
\Delta x_j
\rightarrow
\Delta F_j(r,k)
\rightarrow
|\Delta F_j(r,k)|^2,
\]

which localizes PCA variation in explicit radial-harmonic coordinates of a heterogeneous hybrid representation.

Safe wording:

> **PCA is used as an interpretable latent baseline, while the exact inverse hybrid mapping provides radial-harmonic localization of latent perturbations.**

---

# 11. Novelty hierarchy

The contribution hierarchy for the manuscript is frozen as follows.

## Primary novelty candidate

\[
\boxed{
\text{harmonic-conditioned, inferentially selected radial representation}
}
\]

Confidence:

**High, based on the current literature audit.**

---

## Strong supporting novelty

\[
\boxed{
\text{preserving complete radial structure where compression is not supported}
}
\]

This is important.

The method is not merely a compression algorithm.

It is a controlled **representation-preservation strategy**.

---

## Secondary novelty candidate

\[
\boxed{
\text{exact PCA perturbation-to-radial-harmonic energy localization}
}
\]

Confidence:

**Moderate.**

Nearby precedents exist in Fourier-PCA morphometrics.

---

## Distinctive formulation but not primary novelty

\[
P(\theta\mid r)
\rightarrow
F_k(r).
\]

Confidence of standalone novelty:

**Low to moderate.**

Polar harmonic and circular harmonic precedent exists.

---

## Empirical novelty

The CLO-SKET findings regarding harmonic-dependent compression and retained radial-harmonic organization are novel results of the present analysis.

Their generality beyond CLO-SKET is not established.

---

# 12. Preferred manuscript novelty language

Use phrases such as:

- "we introduce an evidence-controlled representation strategy";
- "we evaluate radial encoding separately across angular harmonic bands";
- "the resulting hybrid representation is selected by held-out inference";
- "compression is retained only where inferentially supported";
- "full radial structure is preserved where compression is not supported";
- "the framework provides an interpretable radial-harmonic representation";
- "the results reveal harmonic-dependent radial representation requirements".

---

# 13. Prohibited novelty language

Until a substantially deeper literature search justifies otherwise, do not use:

- "first-ever";
- "for the first time";
- "the first Fourier representation";
- "the first radial-angular representation";
- "the first Fourier-wavelet garment descriptor";
- "novel Fourier transform";
- "novel wavelet transform";
- "novel PCA";
- "new angular-radial transform";
- "no previous method";
- "unprecedented";
- "state-of-the-art";
- "optimal representation";
- "universally superior".

Also do not state:

> No prior work selects radial bases across angular harmonic bands.

The current literature audit found no close precedent, but absence from the search is not proof of absence from the literature.

Instead use:

> **We are not aware of prior work in the reviewed literature that uses grouped, multiplicity-controlled evidence to select heterogeneous radial encodings separately across angular harmonic bands.**

Use even this sentence cautiously and only if appropriate for the target journal.

---

# 14. Contribution list for Introduction

The manuscript may state:

> The study makes three main contributions.

## Contribution 1 — Harmonic-resolved radial representation question

Building on the shared radial-angular Fourier substrate,

\[
P(\theta\mid r)
\rightarrow
F_k(r),
\]

we retain the full positive angular-harmonic field as a collection of
radial functions and ask whether the appropriate radial representation
depends on angular harmonic scale.

The contribution is therefore not the construction of the
radial-angular Fourier measurement itself, but the formulation and
evaluation of the representation-selection problem

\[
\boxed{
\text{Does the radial representation required for }F_k(r)
\text{ depend on }k?
}
\]

This establishes the full harmonic field as the object on which
band-specific radial representation selection is subsequently performed.

### Contribution 2

A heterogeneous hybrid radial-spectral representation that applies compact global or localized radial bases where supported while retaining full radial structure where compression is not supported.

### Contribution 3

An exact latent-to-Fourier interpretation framework that maps retained PCA variation back into radial-harmonic morphology and quantifies its sign-invariant energy localization.

A fourth empirical contribution may optionally be added:

> The resulting CLO-SKET analysis identifies strong harmonic-dependent radial representation differences and structured intermediate-harmonic/outer-radial organization within the retained latent subspace.

---

# 15. Research-gap paragraph

Recommended manuscript-ready research-gap language:

> Existing shape-analysis methods provide Fourier descriptors, polar Fourier representations, angular-radial transforms, polar harmonic bases, and Fourier-wavelet or multiscale descriptors. These approaches demonstrate that radial and angular shape information can be represented compactly, but the radial basis or multiscale construction is typically specified as part of the descriptor design. Less attention has been given to whether the appropriate radial representation itself varies across angular harmonic scale and whether compression decisions should be supported by held-out statistical evidence rather than imposed uniformly. This study addresses that question by retaining the angular harmonic field explicitly and evaluating radial representation separately across harmonic bands under garment-identity-disjoint, multiplicity-controlled validation.

This paragraph should later receive the exact citations established in the Related Work section.

---

# 16. Paper 2 scientific identity after novelty audit

The frozen scientific identity is now:

> **Paper 2 studies how radial representation requirements vary across angular harmonic scale in probabilistic Fourier morphology and develops an evidence-controlled hybrid representation that compresses only where support is established while preserving full radial structure elsewhere.**

The latent analysis then asks:

> **How is variation represented by that frozen hybrid field organized in radial-harmonic coordinates?**

---

# 17. Final title-level concept

The title should probably emphasize one of:

- evidence-controlled;
- harmonic-dependent;
- radial-spectral;
- probabilistic Fourier morphology.

It should not emphasize:

- wavelets;
- PCA;
- nonlinear manifolds.

Those are supporting components rather than the main contribution.

Possible working title family:

> **Evidence-Controlled Radial-Spectral Representation of Garment-Sketch Morphology**

or

> **Harmonic-Dependent Radial Representation in Probabilistic Fourier Garment Morphology**

or

> **Probabilistic Fourier Morphology with Harmonic-Conditioned Radial Representation**

Final title remains unlocked until journal positioning.

---

# 18. Reviewer-defense statement

If a reviewer asks:

> "Isn't this just Fourier descriptors plus DCT, wavelets, and PCA?"

The manuscript-level answer is:

> **The individual transforms are established methods and are not claimed as algorithmic inventions. The contribution is the representation-selection framework: radial encoding is treated as a testable design choice conditional on angular harmonic scale, evaluated under garment-identity-disjoint and multiplicity-controlled inference. This produces a heterogeneous representation that preserves unsupported-to-compress structure rather than imposing a uniform basis. The latent analysis is then mapped exactly back into that frozen radial-harmonic domain to retain interpretability.**

---

# 19. Final claim boundary

## Supported

- radial compression support differs across angular harmonic bands;
- a heterogeneous radial basis is justified by the frozen inferential results;
- the resulting hybrid representation reduces coefficient count by 41.98%;
- nonlinear task superiority over PCA was not established under the tested framework;
- retained PCA morphology is strongly organized across radial and angular spectral coordinates;
- PCA perturbations can be mapped exactly back to radial-harmonic Fourier morphology.

## Not established

- a universal optimal radial basis;
- mathematical incompressibility of intermediate harmonics;
- semantic meaning of radial zones;
- causal interpretation of PCA axes;
- complete morphology capture by PCA-64;
- universal superiority of PCA;
- one canonical nonlinear morphology manifold;
- generalization beyond CLO-SKET;
- literature-wide priority of the complete method.

---

# 20. Step 4 lock

\[
\boxed{
\textbf{PAPER 2 NOVELTY + CLAIM POSITIONING — LOCKED}
}
\]

Primary contribution:

\[
\boxed{
\textbf{harmonic-conditioned, evidence-controlled radial representation selection}
}
\]

Supporting principle:

\[
\boxed{
\textbf{compress where supported; preserve where unsupported}
}
\]

Secondary contribution:

\[
\boxed{
\textbf{exact latent-to-radial-harmonic morphology localization}
}
\]

Next:

\[
\boxed{
\textbf{STEP 5 — MANUSCRIPT ARCHITECTURE + OUTLINE}
}
\]