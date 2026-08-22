# CLO-SKET Paper 2 — Literature and Novelty Audit

## Status

**Literature audit: PROVISIONAL COMPLETE**

**Novelty lock: NOT YET FINAL**

This document evaluates the proposed Paper 2 contribution against prior work in:

- Fourier shape description;
- polar and radial-angular image representations;
- circular and polar harmonic transforms;
- multiscale and wavelet-Fourier descriptors;
- PCA-based Fourier morphology;
- fashion-sketch representation;
- learned fashion-sketch embeddings.

The objective is not to maximize novelty language.

The objective is to determine precisely:

1. what is already established;
2. what is a known technique applied in a new context;
3. what appears to be a new combination;
4. what appears to be the strongest defensible methodological contribution.

---

# 1. Proposed Paper 2 contribution stack

Paper 2 currently contains four candidate contribution layers.

## C1 — Probabilistic radial-angular spectral representation

\[
P_i(\theta\mid r)
\rightarrow
F_{i,k}(r)
\]

with radius \(r\) retained explicitly while the angular coordinate is decomposed into Fourier harmonics \(k\).

---

## C2 — Harmonic-dependent inferential radial compression

Radial representation is selected separately by angular harmonic band:

\[
k=1{:}4
\rightarrow
\mathrm{DCT}_4
\]

\[
k=5{:}12
\rightarrow
\mathrm{RAW}_{72}
\]

\[
k=13{:}24
\rightarrow
\mathrm{RAW}_{72}
\]

\[
k=25{:}36
\rightarrow
\mathrm{db4\ wavelet}_4.
\]

Compression is retained only where supported under garment-identity-disjoint,
multiplicity-controlled inference.

---

## C3 — Exact latent-to-Fourier morphology interpretation

PCA perturbations are mapped through the exact inverse representation:

\[
\Delta x_j
\rightarrow
\Delta F_j(r,k)
\]

and interpreted through sign-invariant morphology energy

\[
E_j(r,k)
=
|\Delta F_j(r,k)|^2.
\]

---

## C4 — Empirical radial-harmonic organization

Within the retained PCA-64 subspace:

\[
78.54\%
\]

of variance-weighted mapped morphology energy lies in \(k=5{:}24\),

\[
66.84\%
\]

is outer-radial, and

\[
51.30\%
\]

lies jointly in the outer-radial × intermediate-harmonic region.

---

# 2. Classical Fourier shape descriptors

Fourier analysis of object shape is well established.

Classical Fourier descriptors represent contours or shape signatures using
harmonic coefficients. Fourier descriptors have been used for shape recognition,
retrieval, morphometrics, and reconstruction for decades.

Therefore Paper 2 must NOT claim novelty for:

- Fourier descriptors;
- harmonic decomposition of shape;
- truncating Fourier coefficients;
- reconstructing shapes from Fourier coefficients;
- interpreting low versus high Fourier orders as different geometric scales.

## Novelty consequence

\[
\boxed{
\text{Fourier representation itself is prior art.}
}
\]

Paper 2's novelty cannot rest on the use of Fourier coefficients.

---

# 3. Polar Fourier and radial-angular shape descriptors

A particularly important precedent is the Generic Fourier Descriptor.

Zhang and Lu developed a Generic Fourier Descriptor by applying a two-dimensional
Fourier transform to a polar-raster representation of a shape.

The method explicitly captures both:

- radial information;
- circular/angular information.

This is a close conceptual precedent to any broad claim that CLO-SKET is the
first method to represent shape jointly in radial and angular spectral coordinates.

## Consequence

We must NOT claim:

> This is the first radial-angular Fourier representation of shape.

or:

> Previous Fourier descriptors collapse radial and angular information.

That would be false.

## Difference from Paper 2

The Generic Fourier Descriptor applies a two-dimensional spectral transform to
a polar-raster shape representation.

Paper 2 instead constructs a conditional angular probability field

\[
P(\theta\mid r)
\]

and performs the angular Fourier decomposition while retaining the radial
coordinate explicitly:

\[
P(\theta\mid r)
\rightarrow
F_k(r).
\]

The distinction is potentially important, but it is not sufficient by itself
to establish strong methodological novelty.

## Provisional status of C1

\[
\boxed{
\text{C1 = DISTINCTIVE FORMULATION, BUT NOT SAFE AS PRIMARY NOVELTY}
}
\]

---

# 4. Circular harmonic and polar harmonic precedent

The idea of representing an image through angular harmonics with radial functions
is considerably older than Paper 2.

Circular-harmonic image methods describe images using radial modulators of
angular Fourier components.

Polar Harmonic Transforms and related orthogonal moment families explicitly use
separable bases of the form

\[
V_{nm}(r,\theta)
=
R_n(r)e^{im\theta}.
\]

Related families include:

- Angular Radial Transform;
- Polar Harmonic Transform;
- Polar Complex Exponential Transform;
- Zernike moments;
- generic harmonic-function-based moments.

These methods establish strong precedent for separating radial and angular modes.

## Consequence

We cannot claim novelty for the general mathematical principle

\[
\text{radial function}
\times
\text{angular harmonic}.
\]

## Important distinction

Most of these methods define a predetermined orthogonal radial basis

\[
R_n(r)
\]

for every angular order.

Paper 2 does something materially different:

> it empirically tests the appropriate radial representation separately across
> angular harmonic bands and allows different angular ranges to retain different
> radial bases or no compression at all.

That distinction becomes central to the novelty argument.

---

# 5. Angular Radial Transform precedent

The Angular Radial Transform is an established MPEG-7 region-shape descriptor.

It represents shape using angular and radial basis functions and was designed
to provide a compact region-based shape representation.

Later work also incorporated magnitude and phase information into ART-derived
descriptors.

## Consequence

The phrase

> angular-radial transform

should not be used as if CLO-SKET invented the concept.

Paper 2 should explicitly distinguish its method from ART:

- ART chooses a fixed analytical basis;
- Paper 2 begins from \(P(\theta\mid r)\);
- Fourier transformation is performed angularly;
- radial representation is subsequently selected empirically and separately
  across harmonic bands.

---

# 6. Wavelets and multiscale Fourier shape descriptors

Wavelet-based shape representation is also well established.

Wavelet descriptors have long been motivated by their ability to provide:

- localization;
- multiresolution structure;
- local frequency information.

Several studies combine Fourier and wavelet representations.

Multiscale Fourier descriptors, for example, apply wavelet operations to
shape-boundary representations and then use Fourier descriptors across multiple
scales.

Wavelet-Fourier descriptors have also been compared directly with conventional
Fourier descriptors and Generic Fourier Descriptors.

## Major implication

Paper 2 CANNOT claim novelty for:

\[
\boxed{
\text{Fourier + wavelet}
}
\]

as a combination.

That combination has substantial prior art.

---

# 7. Fashion-specific Wavelet Fourier precedent

This point is especially important.

An and Li (2014) applied a Wavelet Fourier Descriptor to fashion-flat sketches.

Their pipeline combined:

- discrete wavelet transformation;
- Fourier shape description;
- dimensionality reduction;
- supervised classification.

This is direct fashion-domain precedent for combining wavelet and Fourier shape
information.

## Consequence

Paper 2 absolutely must NOT say:

> We introduce wavelet-Fourier analysis for garment sketches.

That would be indefensible.

## Critical distinction from Paper 2

An and Li use a fixed Wavelet Fourier Descriptor for classification.

Paper 2 does NOT begin by assuming that wavelet representation is appropriate
throughout the morphology spectrum.

Instead, it compares candidate radial representations and retains wavelet
compression only where inferential support survives.

Specifically:

\[
k=25{:}36
\rightarrow
\mathrm{db4}_4
\]

while

\[
k=5{:}24
\]

is left uncompressed.

This conditional selection appears substantially different from a fixed
wavelet-Fourier descriptor.

---

# 8. Multiscale Fourier precedent

Kunttu and colleagues developed multiscale Fourier descriptors for shape retrieval.

Their work combines Fourier descriptors with wavelet-based multiresolution
representation and shows that shape can benefit from analysis at multiple scales.

This again establishes that:

\[
\text{Fourier}
+
\text{multiresolution}
\]

is established prior art.

## Difference from Paper 2

The prior multiscale methods construct a multiresolution descriptor as part of
the representation design.

Paper 2 instead asks a statistical question:

> Is radial compression support the same across angular harmonic scale?

The answer is empirically heterogeneous.

The resulting representation is therefore not a uniform multiscale descriptor.

It is an evidence-conditioned hybrid:

\[
\mathrm{DCT}
/
\mathrm{RAW}
/
\mathrm{RAW}
/
\mathrm{wavelet}.
\]

---

# 9. DCT as radial basis

Cosine-based radial bases also have clear precedent.

Angular Radial Transform itself uses cosine radial functions in its conventional
form, and other polar harmonic families employ trigonometric or exponential
radial kernels.

Therefore:

\[
\boxed{
\text{using a cosine/DCT radial basis is not novel by itself.}
}
\]

What may be distinctive is the inferential decision that a compact global
cosine basis is supported specifically for one angular range while another
radial basis is supported for another range.

---

# 10. The strongest distinction identified so far

Across the literature examined, many methods use:

- Fourier angular descriptors;
- polar coordinate systems;
- radial basis functions;
- wavelets;
- DCT/cosine bases;
- multiresolution representations;
- combinations of Fourier and wavelet features.

However, I did not identify a close precedent in the reviewed literature for the
following complete procedure:

1. retain angular Fourier order \(k\) explicitly;
2. treat the radial dependence \(F_k(r)\) as an object whose representation may
   differ with \(k\);
3. compare candidate radial representations separately across harmonic bands;
4. validate those choices using complete held-out object identities;
5. perform simultaneous/multiplicity-controlled inference over the representation
   choices;
6. compress only the harmonic bands where compression survives inference;
7. preserve full radial structure where compression is not supported;
8. combine the resulting heterogeneous radial bases into one frozen spectral
   representation.

This currently appears to be the strongest candidate methodological contribution.

## Provisional novelty statement

\[
\boxed{
\textbf{Evidence-controlled harmonic-dependent radial representation selection}
}
\]

rather than:

\[
\boxed{
\text{a new Fourier descriptor}
}
\]

or:

\[
\boxed{
\text{a new Fourier-wavelet descriptor}.
}
\]

---

# 11. Why the negative compression results matter

Many dimensionality-reduction methods ask:

> How aggressively can the representation be compressed?

Paper 2 uses a different principle:

\[
\boxed{
\text{compress only where support is established}
}
\]

and therefore treats

\[
\text{failure to establish compression support}
\]

as a reason to preserve structure.

This creates the final representation

\[
\mathrm{DCT}_4
/
\mathrm{RAW}_{72}
/
\mathrm{RAW}_{72}
/
\mathrm{WAV}_4.
\]

The methodological novelty, if maintained after further review, is therefore as
much about **preserving unsupported-to-compress structure** as it is about
compressing supported bands.

---

# 12. PCA on Fourier descriptors is established prior art

PCA has repeatedly been applied to Fourier shape descriptors.

Elliptic Fourier analysis combined with PCA is common in biological
morphometrics and has been used to study:

- leaves;
- petals;
- grains;
- anatomical structures;
- animal body shapes;
- other biological outlines.

Thus Paper 2 cannot claim novelty for

\[
\text{Fourier coefficients}
\rightarrow
\text{PCA}.
\]

## Provisional status

\[
\boxed{
\text{PCA on spectral shape representations = established prior art.}
}
\]

---

# 13. Reconstructing morphology along PCA axes is also established

Morphometric Fourier analysis commonly reconstructs shapes at different values
along principal components to visualize the morphology represented by each PC.

Therefore the general idea

\[
\text{PC direction}
\rightarrow
\text{reconstructed shape}
\]

is not new.

## Important Paper 2 distinction

Paper 2 does not merely reconstruct an outline.

It maps a standardized PCA perturbation through the exact inverse hybrid
spectral representation:

\[
\Delta x_j
\rightarrow
\Delta F_j(r,k)
\]

and then defines

\[
E_j(r,k)
=
|\Delta F_j(r,k)|^2.
\]

This gives an explicit radial × harmonic localization of each latent direction.

That exact construction may be distinctive.

However, because PCA inversion and Fourier-morphology reconstruction have strong
precedent, this should currently be treated as a **secondary methodological
contribution**, not the primary novelty claim.

## Provisional status of C3

\[
\boxed{
\text{C3 = POSSIBLY DISTINCTIVE IMPLEMENTATION / SECONDARY CONTRIBUTION}
}
\]

---

# 14. Nonlinear geometry versus nonlinear-model utility

The distinction

\[
\text{nonlinear geometry}
\neq
\text{need for a nonlinear predictive model}
\]

is scientifically important.

However, it should not currently be treated as an algorithmic novelty claim.

Model comparison between PCA, kernel methods, autoencoders, manifold methods,
and related nonlinear techniques is well established across many fields.

Paper 2's value here lies in methodological discipline:

- nonlinear geometry was evaluated separately;
- nonlinear task superiority was tested separately;
- failure of nonlinear model superiority was not interpreted as proof of
  linear geometry.

## Provisional status

\[
\boxed{
\text{VALUABLE SCIENTIFIC QUALIFICATION, NOT PRIMARY NOVELTY}
}
\]

---

# 15. Fashion-sketch literature

Fashion-sketch research is increasingly dominated by downstream tasks such as:

- sketch-based image retrieval;
- cross-domain sketch-photo retrieval;
- garment modelling;
- three-dimensional garment generation;
- sketch-guided image synthesis;
- learned shared embeddings.

Recent work includes deep and self-supervised systems for fine-grained
sketch-based retrieval and large sketch-to-fashion datasets.

The dominant research question is generally:

> Can a sketch retrieve, reconstruct, transfer, or generate the intended garment?

Paper 2 asks a different question:

> How is the geometry of sketch morphology organized across radial position and
> angular harmonic scale?

This makes Paper 2 unusual in the fashion-sketch literature even though many of
its mathematical tools have broader precedent.

---

# 16. Recent fashion-sketch developments

Recent fashion-sketch work reinforces the distinction between Paper 2 and the
mainstream literature.

Modern systems use:

- CNNs;
- Vision Transformers;
- contrastive representation learning;
- generative models;
- sketch-photo alignment;
- large paired or captioned datasets.

These approaches optimize downstream retrieval or generation performance.

Paper 2 instead studies an explicit, auditable morphology coordinate system and
asks which structure survives controlled representation reduction.

## Consequence

The likely novelty is not:

> better fashion-sketch recognition.

The likely novelty is:

> an interpretable statistical morphology framework for fashion sketches.

---

# 17. Candidate novelty matrix

| Proposed element | Prior-art status | Paper 2 status |
|---|---|---|
| Fourier shape description | Strong prior art | NOT novel |
| Polar representation of shape | Strong prior art | NOT novel |
| Angular harmonics | Strong prior art | NOT novel |
| Radial × angular separable transforms | Strong prior art | NOT novel |
| Generic polar Fourier descriptors | Strong prior art | NOT novel |
| Angular Radial Transform | Strong prior art | NOT novel |
| Polar Harmonic Transform | Strong prior art | NOT novel |
| Wavelet shape descriptors | Strong prior art | NOT novel |
| Fourier + wavelet descriptors | Strong prior art | NOT novel |
| Fashion-flat Wavelet Fourier descriptor | Direct prior art | NOT novel |
| PCA of Fourier shape coefficients | Strong prior art | NOT novel |
| PCA reconstruction of morphology | Strong prior art | NOT novel |
| Conditional \(P(\theta\mid r)\) normalization | Potentially distinctive | Possible supporting contribution |
| Keeping \(F_k(r)\) explicit rather than collapsing radial dimension | Distinctive but related to circular-harmonic work | Supporting contribution |
| Testing radial representation separately by harmonic band | No close precedent identified in reviewed literature | Strong novelty candidate |
| Identity-disjoint validation of representation choice | No close shape-descriptor precedent identified | Strong supporting novelty |
| FWER-controlled radial-basis selection | No close precedent identified | Strong novelty candidate |
| Preserving full bands when compression unsupported | Methodologically distinctive | Strong novelty candidate |
| DCT/raw/raw/wavelet hybrid selected by inference | No close precedent identified | Strong novelty candidate |
| Exact PCA perturbation → \(F_k(r)\) energy localization | Related concepts exist; exact formulation not identified | Secondary novelty candidate |
| Nonlinear geometry/model-utility distinction | General methodological idea | Scientific contribution, not algorithmic novelty |
| 78.54/66.84/51.30 radial-harmonic organization | Dataset-specific empirical result | Novel empirical finding for CLO-SKET |

---

# 18. Direct precedents that MUST appear in Related Work

The following literature families are mandatory because reviewers familiar with
shape analysis are likely to expect them.

## A. Classical Fourier descriptors

Purpose:

Establish that Fourier shape description and harmonic reconstruction are old and
well understood.

---

## B. Generic Fourier Descriptor

Purpose:

Acknowledge direct precedent for polar-raster Fourier representation containing
radial and angular shape information.

This is one of the most important comparisons for Paper 2.

---

## C. Angular Radial Transform / MPEG-7 RegionShape

Purpose:

Acknowledge established separable angular-radial shape descriptors.

---

## D. Polar Harmonic Transforms

Purpose:

Acknowledge general orthogonal decompositions of images into radial kernels and
angular harmonics.

---

## E. Fourier-wavelet / multiscale shape descriptors

Purpose:

Establish that combining Fourier and wavelet representations is not itself novel.

---

## F. Fashion-flat Wavelet Fourier Descriptor

Purpose:

Direct fashion-domain precedent.

This citation is mandatory because otherwise a reviewer could correctly argue
that Paper 2 ignores highly relevant earlier fashion-sketch Fourier-wavelet work.

---

## G. Fourier descriptors + PCA morphometrics

Purpose:

Acknowledge that PCA of Fourier coefficients and reconstruction of shape
variation along PCs are established.

---

## H. Modern fashion-sketch representation

Purpose:

Position Paper 2 relative to current deep retrieval/generation literature and
explain why explicit morphology analysis remains a different research question.

---

# 19. Current strongest novelty formulation

The strongest defensible provisional statement is:

> Existing shape descriptors provide Fourier, polar, radial-angular and
> multiresolution representations, including Fourier-wavelet approaches and
> fashion-specific Wavelet Fourier Descriptors. Paper 2 differs by treating the
> radial dependence of each angular harmonic range as an empirically testable
> representation problem and selecting compression separately across harmonic
> bands under garment-identity-disjoint, multiplicity-controlled inference.
> The resulting representation preserves full radial structure where compression
> is unsupported and applies compact global or localized bases only where
> supported.

This wording deliberately avoids a literature-priority claim.

---

# 20. Even shorter contribution formulation

\[
\boxed{
\textbf{The contribution is not a new transform; it is a new evidence-controlled representation-selection strategy.}
}
\]

This is currently the most defensible framing.

---

# 21. Candidate final primary contribution

Subject to the final novelty lock:

> We introduce an evidence-controlled radial-spectral representation strategy in
> which the radial encoding of angular Fourier morphology is selected separately
> across harmonic bands using identity-disjoint, multiplicity-controlled
> validation, producing a heterogeneous hybrid representation that compresses
> supported bands while preserving complete radial structure where compression
> is not supported.

---

# 22. Secondary contribution

> We provide an exact latent-to-spectral interpretation framework that maps PCA
> perturbations back into radial-harmonic Fourier morphology and quantifies their
> sign-invariant energy localization.

This is scientifically useful but should probably remain the secondary rather
than title-level novelty.

---

# 23. Empirical contribution

> Applied to CLO-SKET, the framework shows that radial representation requirements
> differ across angular harmonic scales and that retained latent morphology is
> strongly concentrated in intermediate harmonics and outer radial structure.

This is an empirical finding, not a universal mathematical law.

---

# 24. What Paper 2 should NOT claim after this review

The manuscript should not claim that it introduces:

- Fourier shape descriptors;
- polar shape representation;
- radial-angular spectral analysis;
- angular harmonics;
- DCT radial functions;
- wavelet shape representation;
- Fourier-wavelet descriptors;
- multiscale Fourier descriptors;
- PCA of Fourier descriptors;
- reconstruction of morphology along principal components.

These all have meaningful precedent.

---

# 25. What currently appears genuinely distinctive

The following combination has no close match identified in the reviewed
literature:

\[
\boxed{
\begin{aligned}
&\text{conditional radial-angular morphology}\\
&\rightarrow
\text{angular Fourier field }F_k(r)\\
&\rightarrow
\text{harmonic-band-specific radial representation testing}\\
&\rightarrow
\text{identity-disjoint validation}\\
&\rightarrow
\text{simultaneous inferential control}\\
&\rightarrow
\text{compress supported bands}\\
&+
\text{preserve unsupported bands}\\
&\rightarrow
\text{hybrid radial-spectral morphology representation}.
\end{aligned}
}
\]

This should be the focus of the final novelty audit.

---

# 26. Novelty confidence assessment

## C1 — \(P(\theta\mid r)\rightarrow F_k(r)\)

**Confidence of standalone novelty: LOW–MODERATE**

Reason:

Strong prior art exists for polar Fourier, circular harmonic and polar harmonic
representations.

The shell-normalized conditional-probability construction may be distinctive,
but should not presently carry the paper's novelty claim.

---

## C2 — harmonic-dependent inferential radial compression

**Confidence of novelty: HIGH, provisionally**

Reason:

No close precedent was identified for selecting heterogeneous radial bases
separately across angular harmonic bands through grouped,
multiplicity-controlled inference.

This is currently the strongest contribution.

---

## C3 — exact PCA-to-\(F_k(r)\) morphology localization

**Confidence of novelty: MODERATE**

Reason:

PCA of Fourier descriptors and reconstruction along PC axes are established.

The exact inverse hybrid mapping and radial-harmonic energy localization appear
more distinctive, but the general idea has nearby precedent.

---

## C4 — empirical radial-harmonic findings

**Confidence of novelty for CLO-SKET: HIGH**

Reason:

These are new empirical findings generated by the present analysis.

Their generality outside CLO-SKET has not been established.

---

# 27. Provisional paper positioning

Paper 2 should currently be positioned as an:

\[
\boxed{
\textbf{interpretable, evidence-controlled radial-spectral morphology framework}
}
\]

rather than as:

\[
\text{a new Fourier transform}
\]

or:

\[
\text{a new wavelet descriptor}.
\]

The methodological philosophy is:

\[
\boxed{
\text{do not decide the compression basis first;}
\quad
\text{let held-out evidence determine where compression is defensible.}
}
\]

---

# 28. Relationship to Paper 1

Paper 1 establishes an auditable low-order radial-angular morphology framework and
identity-aware validation.

Paper 2 generalizes the morphology field across

\[
k=1,\ldots,36
\]

and investigates how radial representation requirements change with angular
harmonic scale.

The two papers therefore have separate principal questions.

Paper 2 should cite Paper 1 as methodological foundation once Paper 1 is publicly
available, but should not reproduce Paper 1's full second-harmonic reconstruction
and axial-error inference.

---

# 29. Literature-audit conclusion

The literature substantially narrows the novelty claim in a productive way.

The paper should NOT be sold as:

> Fourier analysis for fashion sketches.

That literature already exists.

Nor should it be sold as:

> a radial-angular Fourier descriptor.

Strong adjacent precedent exists.

The more defensible and potentially stronger contribution is:

\[
\boxed{
\textbf{harmonic-conditioned, inferentially selected radial representation}
}
\]

with:

\[
\boxed{
\textbf{preservation rather than forced compression where statistical support is absent.}
}
\]

This distinction is both technically specific and scientifically aligned with the
actual analysis.

---

# 30. Step 3 status

\[
\boxed{
\textbf{PAPER 2 LITERATURE AUDIT — PROVISIONALLY COMPLETE}
}
\]

The next task is:

\[
\boxed{
\textbf{STEP 4 — NOVELTY AND CLAIM LOCK}
}
\]

Step 4 should freeze exactly:

1. the primary contribution;
2. secondary contributions;
3. the research gap;
4. the manuscript novelty sentence;
5. prohibited novelty language;
6. how Paper 2 differs explicitly from Generic Fourier Descriptor, ART/PHT,
   Wavelet Fourier Descriptor, and Fourier-PCA morphometrics.