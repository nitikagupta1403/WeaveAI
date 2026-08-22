# CLO-SKET Paper 2 — Introduction and Related Work

## Status

**INTRODUCTION + RELATED WORK: MANUSCRIPT ASSEMBLY DRAFT**

This section positions the frozen CLO-SKET Paper 2 contribution against
established Fourier, polar, angular-radial, and multiscale shape representations.

The novelty claim is deliberately narrow.

We do NOT claim novelty for:

- Fourier shape analysis;
- polar shape representation;
- angular-radial transforms;
- DCT compression;
- wavelet shape representation;
- PCA;
- multiscale Fourier descriptors.

The contribution investigated here is the evidence-controlled integration of
radial and angular spectral morphology in which radial representation is selected
conditionally on angular harmonic scale and unsupported compression leads to
preservation rather than forced dimensional reduction.

---

# 1. Introduction

Representing the morphology of a garment sketch requires capturing structure
across multiple spatial scales while preserving the organization of shape across
the image.

A single global descriptor can provide a compact summary of shape, but such
compression may obscure where particular geometric structures occur. Conversely,
retaining a fully resolved spatial representation preserves localization but can
produce a high-dimensional description containing substantial redundancy.

The central representation problem is therefore not simply

\[
\text{how much should morphology be compressed?}
\]

but more specifically

\[
\boxed{
\text{which dimensions of morphology can be compressed,
and under what evidence?}
}
\]

This question becomes particularly relevant when shape is represented in polar
coordinates.

Radial position and angular structure describe different aspects of geometry.
Collapsing them simultaneously can prevent determination of whether radial
complexity changes with angular scale.

---

## 1.1 Fourier representations of shape

Fourier methods provide a natural framework for shape description because they
represent geometric variation through harmonic components.

Classical Fourier descriptors have been extensively used for contour and
region-based shape analysis, recognition, and retrieval. Fourier representations
can provide compact descriptors and useful transformation properties, but global
Fourier coefficients may also combine structures occurring at different spatial
locations.

Polar representations provide one route to retaining additional spatial
organization.

Generic Fourier Descriptor approaches, for example, apply Fourier analysis to
polar-raster representations of shape, allowing radial and angular frequency
information to contribute to a region-based descriptor.

Angular Radial Transform methods similarly describe shapes using basis functions
defined over radial and angular coordinates and have been used extensively in
region-based shape retrieval.

These approaches establish that radial and angular structure can be represented
jointly in a transform domain.

The question addressed here is different.

Rather than asking only how to construct a compact polar spectral descriptor, we
ask whether the radial representation itself should remain the same across
angular harmonic order.

---

## 1.2 Radial-angular morphology as a conditional probability field

We begin with a probability-normalized radial-angular representation.

For sketch \(i\), angular morphology conditional on radial shell \(r\) is
represented as

\[
P_i(\theta\mid r),
\]

with

\[
\sum_\theta P_i(\theta\mid r)=1
\]

for every occupied shell.

Angular Fourier transformation is then applied independently at each radial
location:

\[
F_{i,k}(r)
=
\sum_\theta
P_i(\theta\mid r)
e^{-ik\theta}.
\]

The resulting quantity is not a single Fourier coefficient for harmonic \(k\).

It is a radial function:

\[
\boxed{
F_{i,k}:r\mapsto\mathbb C.
}
\]

Consequently, angular harmonic scale \(k\) and radial location \(r\) remain
explicitly separable.

This makes it possible to pose a representation question that is unavailable
after complete radial collapse:

\[
\boxed{
\text{Does the radial information structure of }F_k(r)
\text{ depend on }k?
}
\]

---

## 1.3 Why uniform spectral compression may be unnecessarily restrictive

A common dimensionality-reduction strategy is to retain a fixed number of
coefficients from a chosen transform.

Such a rule is attractive because it produces a regular representation.

However, regularity of the representation does not imply that the underlying
information structure is regular across frequency.

Suppose radial morphology at one angular scale is adequately represented by a
small number of smooth global coefficients, whereas another angular scale
requires substantially more radial resolution.

Applying the same radial compression rule to both ranges creates one of two
problems:

\[
\text{over-retention}
\]

where unnecessary coefficients are preserved,

or

\[
\text{over-compression}
\]

where useful radial structure is discarded.

This motivates a conditional representation principle:

\[
\boxed{
\text{radial representation should be evaluated as a function of angular scale.}
}
\]

---

## 1.4 Multiscale and wavelet shape representations

The broader shape-analysis literature has long recognized that morphology can
contain information at multiple spatial scales.

Wavelet-based and multiscale Fourier descriptors combine localized or
multiresolution representations with Fourier analysis to capture both coarse and
fine geometric structure.

These approaches demonstrate that Fourier and wavelet representations need not
be mutually exclusive.

However, the existence of multiple useful bases creates another methodological
question:

\[
\boxed{
\text{which basis should be used where?}
}
\]

Selecting a transform solely because it reconstructs a signal efficiently does
not necessarily establish that the compressed representation preserves the
information required for a downstream morphology task.

This distinction motivates evaluating compression empirically under the same
validation framework used to evaluate the resulting representation.

---

## 1.5 Representation selection as an inferential problem

In the present framework, radial compression is therefore treated as a model
selection problem rather than as an assumed preprocessing operation.

The positive angular harmonics are divided into prespecified ranges.

Within each range, candidate radial representations are evaluated under
garment-identity-disjoint validation.

The relevant question is not simply whether a compact representation can
reconstruct

\[
F_k(r),
\]

but whether replacing the complete radial field with that representation is
supported under the frozen task-oriented criterion.

This produces an intentionally conservative rule:

\[
\boxed{
\text{compress where supported}
}
\]

and

\[
\boxed{
\text{preserve where compression support is absent}.
}
\]

Statistical multiplicity is controlled across the confirmatory representation
comparisons.

The final representation is therefore permitted to be heterogeneous across
angular harmonic scale.

---

## 1.6 Representation geometry after compression

Dimensionality reduction does not end with spectral compression.

Once a frozen hybrid representation has been constructed, a second question
arises:

\[
\text{what is the geometry of variation within this representation?}
\]

Linear latent methods such as principal-component analysis provide stable and
interpretable coordinate systems, but complex morphology may exhibit nonlinear
geometric structure.

Conversely, detecting nonlinear geometry does not establish that a nonlinear
latent representation improves downstream performance.

We therefore separate:

\[
\boxed{
\text{geometric nonlinearity}
}
\]

from

\[
\boxed{
\text{nonlinear-model utility}.
}
\]

Nonlinear latent models are evaluated against PCA under the same grouped
validation logic, while manifold-oriented analyses are used separately to
characterize geometry.

This prevents geometric evidence alone from being used to justify replacement of
a validated latent representation.

---

## 1.7 Interpreting latent variation in the original morphology domain

Latent coordinates are useful only to the extent that their relationship to the
original representation remains interpretable.

For a PCA direction \(j\), we therefore map a one-score-standard-deviation
perturbation exactly back through the frozen representation:

\[
PC_j
\rightarrow
\Delta x_j
\rightarrow
\Delta F_j(r,k).
\]

Morphology energy is then defined as

\[
E_j(r,k)
=
|\Delta F_j(r,k)|^2.
\]

This creates a direct correspondence between latent variation and its radial and
angular-harmonic localization.

Rather than assigning semantic labels to principal components, the analysis asks
a more restricted mathematical question:

\[
\boxed{
\text{where in }(r,k)\text{ space is retained latent variation expressed?}
}
\]

---

## 1.8 Study objectives

Using 2,300 garment sketches representing 230 garment identities across 23
categories, we investigate four questions.

### RQ1

Does support for radial compression differ across angular harmonic scale?

### RQ2

Can band-specific representation selection produce a lower-dimensional hybrid
spectral representation while preserving full radial structure where compression
is not supported?

### RQ3

Does nonlinear geometry imply that a nonlinear latent representation should
replace PCA under garment-identity-disjoint task validation?

### RQ4

Where is variation within the retained PCA subspace localized across radial
position and angular harmonic order?

These questions define the complete scope of the study.

---

# 2. Related Work

## 2.1 Fourier descriptors for shape representation

Fourier descriptors are among the established spectral approaches for shape
analysis.

Contour-based approaches represent a boundary sequence in a Fourier basis,
whereas region-based methods extend spectral description to the complete shape
region.

Fourier descriptors have been attractive because of their compactness,
computational efficiency, and ability to support invariance to geometric
transformations through suitable normalization.

However, conventional global Fourier descriptors primarily summarize spectral
content.

For the present problem, retaining explicit radial organization is important
because we wish to determine whether radial representation requirements themselves
change with angular harmonic scale.

---

## 2.2 Generic Fourier Descriptor

Zhang and Lu introduced the Generic Fourier Descriptor as a region-based shape
descriptor obtained by applying a two-dimensional Fourier transform to a
polar-raster representation of shape.

This is an important methodological precedent because radial and angular
frequencies both contribute to the resulting descriptor.

The present framework shares the use of polar geometry and Fourier representation
but differs in its primary objective.

We retain

\[
F_k(r)
\]

as an explicit radial function for each angular harmonic and subsequently test
whether its radial dimension can be compressed differently across harmonic
ranges.

Thus, the emphasis is not solely on constructing a compact global descriptor,
but on preserving the conditional relationship between radial organization and
angular harmonic scale during representation selection.

---

## 2.3 Angular Radial Transform

The Angular Radial Transform provides another established framework for
region-based shape representation in polar coordinates.

ART uses basis functions defined jointly over radial and angular dimensions and
has been adopted in MPEG-7 region-based shape description.

Subsequent work has extended ART and incorporated additional coefficient
information such as aligned phase to improve shape discrimination and invariance.

These approaches demonstrate the value of explicit radial-angular basis
construction.

Our objective is complementary but distinct.

Instead of fixing one radial-angular basis family for the complete descriptor,
we retain angular Fourier harmonics as radial functions and ask whether the
appropriate radial encoding depends empirically on harmonic order.

---

## 2.4 Multiscale Fourier and wavelet descriptors

Multiscale Fourier descriptors have combined wavelet decompositions with Fourier
analysis to describe shape at multiple resolutions.

Such approaches address an important limitation of purely global Fourier
descriptors by introducing localized or scale-dependent information.

They also establish that wavelet and Fourier representations can be combined
productively within one shape-analysis system.

The present framework differs in how multiple representations are assigned.

Rather than applying a fixed multiscale transform architecture uniformly, we
evaluate radial representation alternatives separately across angular harmonic
bands.

A wavelet representation is therefore not assumed to be appropriate for all
harmonic ranges.

Likewise, a global cosine representation is not imposed everywhere.

The final basis assignment follows the frozen inferential comparison.

---

## 2.5 Compact descriptors versus evidence-guided preservation

Much of classical descriptor design necessarily emphasizes compactness because
storage and retrieval efficiency are major objectives.

Our problem places an additional constraint on compression:

\[
\boxed{
\text{a lower-dimensional representation is desirable only when its use is supported.}
}
\]

This changes the interpretation of a negative compression result.

If a compact representation is not supported for a harmonic band, the outcome is
not considered a failure to obtain a descriptor.

Instead, preservation of the complete radial structure becomes the selected
representation.

The final descriptor can consequently contain compressed and uncompressed
spectral regions simultaneously.

---

## 2.6 Linear and nonlinear latent representations

PCA is widely used to construct orthogonal low-dimensional representations of
high-dimensional data.

Nonlinear dimensionality-reduction and manifold-learning approaches instead seek
coordinates capable of preserving nonlinear geometric relationships.

For morphology data, however, two distinct questions must be separated:

1. whether nonlinear geometry exists;
2. whether a nonlinear latent representation improves the validated downstream
   objective.

The present study evaluates these questions independently.

PCA and nonlinear latent alternatives are compared under garment-identity-disjoint
validation, while manifold-oriented methods are used as geometric diagnostics.

This design avoids interpreting a visually nonlinear embedding as evidence of
predictive superiority.

---

## 2.7 Position of the present study

The present work builds on established ideas from:

- Fourier shape description;
- polar shape representation;
- angular-radial transforms;
- multiscale Fourier analysis;
- wavelet representations;
- PCA and nonlinear dimensionality reduction.

The methodological contribution does not lie in any of these components
individually.

Instead, the framework integrates them around a different representation
selection principle:

\[
\boxed{
\text{radial compression is evaluated conditionally on angular harmonic scale}
}
\]

under:

\[
\boxed{
\text{garment-identity-disjoint validation}
}
\]

and:

\[
\boxed{
\text{multiplicity-controlled inference}.
}
\]

This permits the representation to retain complete radial structure wherever the
tested compression is unsupported.

The resulting latent directions are then mapped exactly back to the
radial-harmonic Fourier domain for localization without assigning unsupported
semantic meaning to the latent axes.

---

# 3. Contribution statement

The study makes four linked contributions.

## Contribution 1 — Conditional radial-angular spectral representation

We formulate sketch morphology as

\[
P(\theta\mid r)
\rightarrow
F_k(r),
\]

preserving radial position and angular harmonic order as explicit coordinates.

---

## Contribution 2 — Harmonic-conditioned inferential compression

Radial compression is evaluated separately across angular harmonic ranges under
garment-identity-disjoint and multiplicity-controlled inference.

The framework therefore permits:

\[
\boxed{
\text{different radial representations at different angular scales}.
}
\]

---

## Contribution 3 — Separation of geometry from model utility

Nonlinear geometry is characterized independently from nonlinear latent-model
performance.

This prevents the existence of nonlinear structure from being treated
automatically as evidence that PCA should be replaced.

---

## Contribution 4 — Exact latent-to-spectral interpretation

PCA perturbations are mapped through the exact frozen inverse representation to

\[
\Delta F_j(r,k),
\]

allowing sign-invariant radial-harmonic localization of variation within the
retained PCA subspace.

---

# 4. Novelty boundary

The manuscript must NOT state:

> We introduce the first polar Fourier descriptor.

> We introduce the first radial-angular shape descriptor.

> We are the first to combine Fourier and wavelet representations.

> We introduce the first multiscale Fourier representation.

> We introduce the first use of PCA for morphology.

These statements are contradicted by established literature or are not
demonstrated by our literature audit.

The defensible contribution is narrower:

> We investigate an evidence-controlled radial-angular morphology framework in
> which radial representation is selected conditionally on angular harmonic
> scale under garment-identity-disjoint validation and multiplicity-controlled
> inference, with full radial structure preserved where tested compression is
> unsupported.

Until a systematic literature review establishes otherwise, even this should be
described as the contribution of the present study rather than as an absolute
"first".

---

# 5. Introduction logic

\[
\text{shape morphology}
\]

\[
\downarrow
\]

\[
\text{Fourier representation}
\]

\[
\downarrow
\]

\[
\text{polar/radial-angular organization}
\]

\[
\downarrow
\]

\[
F_k(r)
\]

\[
\downarrow
\]

\[
\boxed{
\text{should radial compression be identical for every }k?
}
\]

\[
\downarrow
\]

\[
\text{inferential representation selection}
\]

\[
\downarrow
\]

\[
\text{hybrid spectral representation}
\]

\[
\downarrow
\]

\[
\text{latent validation}
\]

\[
\downarrow
\]

\[
\text{exact morphology interpretation}.
\]

---

# Step 11 lock

\[
\boxed{
\textbf{PAPER 2 INTRODUCTION + RELATED WORK — ASSEMBLED}
}
\]

Literature boundary:

\[
\boxed{
\text{established transforms acknowledged}
}
\]

\[
+
\]

\[
\boxed{
\text{our evidence-selection principle isolated}
}
\]

\[
+
\]

\[
\boxed{
\text{no unsupported priority claim}
}
\]

Next:

\[
\boxed{
\textbf{STEP 12 — ABSTRACT + TITLE + KEYWORDS}
}
\]

After Step 12, the manuscript has all major scientific sections and can move to
final paper assembly and citation formatting.