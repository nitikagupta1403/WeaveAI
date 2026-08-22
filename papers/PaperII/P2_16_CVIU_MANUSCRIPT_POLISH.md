# CLO-SKET Paper 2 — CVIU Manuscript Polish and Citation Completion

## Status

**CVIU-SPECIFIC POLISH PLAN: LOCKED**

Primary target:

\[
\boxed{
\textbf{Computer Vision and Image Understanding}
}
\]

This stage does not reopen the scientific analysis.

It adapts the frozen manuscript to the intellectual and editorial expectations of
a computer-vision / image-understanding audience.

---

# 1. CVIU scope alignment

Computer Vision and Image Understanding emphasizes the computer analysis of
pictorial information and explicitly includes areas such as:

- theory;
- data structures and representations;
- shape;
- matching and recognition;
- image understanding.

Paper 2 should therefore be positioned primarily as:

\[
\boxed{
\textbf{a shape-representation methodology paper}
}
\]

demonstrated using garment sketches.

The manuscript should not read primarily as a fashion-technology paper.

---

# 2. Primary CVIU positioning

The main CVIU-facing question is:

> **Should the radial encoding of a polar Fourier shape representation be
> imposed uniformly across angular harmonics, or selected conditionally on
> harmonic scale using held-out evidence?**

This framing should dominate:

- title;
- Abstract;
- Introduction;
- contribution statement;
- Figure 2;
- Discussion opening.

The garment-sketch context provides the structured morphology dataset on which
the representation question is tested.

---

# 3. Preferred CVIU title

## Primary title

**Evidence-Controlled Radial-Spectral Shape Representation for Garment Sketches**

This version is slightly preferable for CVIU to:

> Evidence-Controlled Radial-Spectral Representation of Garment-Sketch Morphology

because it foregrounds:

\[
\boxed{
\text{shape representation}
}
\]

which is directly aligned with the journal.

---

## Alternative title

**Harmonic-Conditioned Radial Representation of Garment-Sketch Fourier Morphology**

This is technically precise but less immediately readable.

---

## Current preference

\[
\boxed{
\textbf{Evidence-Controlled Radial-Spectral Shape Representation for Garment Sketches}
}
\]

No claim of novelty or optimality appears in the title.

---

# 4. CVIU abstract positioning

The Abstract should lead with the general representation issue rather than the
fashion application.

Preferred first sentence:

> Compact spectral shape representations often impose a common encoding rule
> across the transform domain, although representation requirements may vary
> across spatial or harmonic scales.

Then introduce garment sketches as the experimental setting.

The abstract should retain:

- \(P(\theta\mid r)\);
- \(F_k(r)\);
- identity-disjoint validation;
- harmonic-conditioned representation selection;
- DCT/raw/raw/wavelet outcome;
- 41.98% coefficient reduction;
- nonlinear-model qualification;
- retained PCA morphology localization.

PCA should remain secondary to the representation-selection result.

---

# 5. Recommended CVIU abstract

Compact spectral shape representations often impose a common encoding rule across
the transform domain, although representation requirements may vary across
spatial and harmonic scales. We investigate this question for garment-sketch
morphology using a conditional radial-angular probability representation
\(P_i(\theta\mid r)\), whose angular Fourier transform yields radial harmonic
functions \(F_{i,k}(r)\), \(k=1,\ldots,36\).

Using 2,300 sketches from 230 garment identities across 23 categories, candidate
radial representations were evaluated separately across four angular harmonic
bands under garment-identity-disjoint validation with family-wise-error-rate
controlled inference. Four-coefficient DCT compression was supported for
\(k=1{:}4\), while four-coefficient db4-wavelet compression was supported for
\(k=25{:}36\). Compression was not supported for the intermediate
\(k=5{:}24\) harmonics, whose full 72-shell radial structure was retained.

The resulting heterogeneous DCT/raw/raw/wavelet representation reduced the
spectral field from 2,592 to 1,504 complex coefficients per sketch, a 41.98%
coefficient reduction. Tested nonlinear latent models did not establish a
multiplicity-controlled task advantage over PCA. Within the retained PCA-64
subspace, variance-weighted mapped morphology energy was concentrated in
intermediate harmonics and outer radial positions.

These results support a representation-selection principle in which radial
encoding is conditioned on angular harmonic scale and compression is retained
only where supported by held-out evidence.

---

# 6. CVIU Introduction restructuring

The Introduction should move from general vision methodology toward the specific
application.

Preferred order:

## Paragraph 1 — General shape-representation problem

Discuss the tension between:

\[
\text{compactness}
\]

and:

\[
\text{preservation of localized shape structure}.
\]

Do not mention fashion immediately.

---

## Paragraph 2 — Polar and spectral representations

Introduce:

- Fourier descriptors;
- polar Fourier representations;
- angular-radial transforms;
- multiscale spectral descriptors.

Establish that radial and angular shape structure have longstanding representation
precedent.

---

## Paragraph 3 — Unresolved representation-selection issue

State:

> Existing descriptors usually specify their radial or multiscale basis as part
> of the representation design. Less attention has been paid to whether radial
> encoding itself should vary across angular harmonic scale and whether such
> choices can be selected from held-out evidence.

This is the key gap.

---

## Paragraph 4 — Why garment sketches are useful here

Introduce CLO-SKET.

The dataset is useful because it provides:

- many sketches;
- repeated garment identities;
- multiple categories;
- an opportunity for identity-disjoint validation.

Do not frame the dataset merely as a fashion benchmark.

---

## Paragraph 5 — Proposed framework

Introduce:

\[
P(\theta\mid r)
\rightarrow
F_k(r)
\]

followed by:

\[
\text{harmonic-conditioned radial representation testing}.
\]

State:

\[
\boxed{
\text{compress where supported; preserve otherwise}.
}
\]

---

## Paragraph 6 — Contributions

List three contributions:

1. evidence-controlled radial encoding across harmonic bands;
2. heterogeneous hybrid spectral representation;
3. exact latent-to-radial-harmonic interpretation.

The nonlinear geometry audit should not be listed as an equal primary novelty.

---

# 7. CVIU Related Work weighting

For CVIU, Related Work should emphasize shape-analysis literature more heavily
than fashion literature.

Recommended weight:

\[
\boxed{
70\%
\text{ general shape/image representation}
}
\]

\[
+
\]

\[
\boxed{
30\%
\text{ garment/fashion-sketch literature}
}
\]

Approximate subsection order:

## 2.1 Fourier shape descriptors

## 2.2 Polar Fourier and angular-radial representations

## 2.3 Multiscale and wavelet shape descriptors

## 2.4 Fourier descriptors and latent shape analysis

## 2.5 Garment and fashion-sketch representation

## 2.6 Position of the present work

---

# 8. Mandatory literature families

Before submission, verify primary references for all of the following.

## Classical Fourier descriptors

Purpose:

Establish broad prior art for harmonic shape representation.

---

## Generic Fourier Descriptor

Purpose:

Acknowledge direct polar Fourier precedent.

Required distinction:

GFD provides a polar Fourier descriptor, whereas Paper 2 retains
\(F_k(r)\) explicitly and evaluates radial encoding conditionally on \(k\).

---

## Angular Radial Transform

Purpose:

Acknowledge explicit radial-angular basis precedent.

Required distinction:

ART specifies a radial-angular basis; Paper 2 treats radial basis selection as
an inferential question.

---

## Polar Harmonic Transforms / orthogonal moments

Purpose:

Acknowledge broader families of separable radial/angular harmonic bases.

---

## Wavelet and multiscale Fourier descriptors

Purpose:

Make clear that Fourier + wavelet is established prior art.

---

## Fashion-flat Wavelet Fourier Descriptor

Purpose:

Direct garment/fashion-domain precedent.

This citation is mandatory.

---

## PCA / Fourier morphometrics

Purpose:

Acknowledge that Fourier coefficients followed by PCA and shape reconstruction
along PC axes are established.

---

# 9. Citation quality standard

Every reference should be verified from:

- publisher page;
- DOI record;
- Crossref;
- journal site;
- authoritative bibliographic database.

Do not rely on:

- search snippets;
- ResearchGate metadata alone;
- secondary citation lists.

Every sentence in Related Work should be checked against what the cited source
actually did.

---

# 10. Citation categories

Maintain four citation categories.

## A. Direct methodological precedent

Very close to Paper 2.

Examples:

- Generic Fourier Descriptor;
- ART;
- Fourier-wavelet shape descriptors.

---

## B. Supporting methodological precedent

Relevant mathematical tools.

Examples:

- Fourier descriptors;
- wavelets;
- PCA;
- manifold learning.

---

## C. Domain precedent

Garment/fashion sketch methods.

---

## D. Statistical methodology

Bootstrap, permutation, grouped validation, multiple-testing methodology where
formal citations are useful.

This categorization helps prevent overclaiming literature proximity.

---

# 11. CVIU Methods polish

The current Methods are scientifically complete, but for CVIU they should be
slightly more compact.

Main text should retain:

- representation definitions;
- grouping design;
- candidate representation logic;
- primary inference;
- hybrid dimensions;
- PCA inverse mapping.

Move highly technical diagnostics to Supplement:

- packing-debug history;
- extensive Isomap parameter sweeps;
- principal-curve variants;
- diffusion-map variants;
- complete latent-model hyperparameter tables.

Main Methods should remain reproducible without becoming a notebook transcript.

---

# 12. CVIU Results emphasis

The main Results hierarchy should be:

\[
\boxed{
\textbf{1. harmonic-conditioned representation inference}
}
\]

then:

\[
\boxed{
\textbf{2. hybrid representation}
}
\]

then:

\[
\boxed{
\textbf{3. latent validation}
}
\]

then:

\[
\boxed{
\textbf{4. morphology localization}.
}
\]

The nonlinear geometry analysis should remain concise.

---

# 13. CVIU Figure hierarchy

Recommended final main figures:

## Figure 1 — Representation

\[
P(\theta\mid r)
\rightarrow
F_k(r)
\]

Purpose:

teach the representation.

---

## Figure 2 — Harmonic-conditioned representation selection

Purpose:

primary inferential contribution.

This should remain the strongest figure.

---

## Figure 3 — Latent-model validation and geometry

Purpose:

defend PCA choice.

Keep compact.

---

## Figure 4 — Radial-harmonic latent morphology

Purpose:

show interpretability.

---

# 14. CVIU figure count

The current four-figure design is appropriate for a standard research article.

Elsevier's general guidance notes that typical original research papers commonly
contain roughly three to five figures, although journal-specific requirements
should always take precedence.

Therefore:

\[
\boxed{
4\text{ main figures is reasonable}
}
\]

for the current manuscript.

Move extensive sensitivity figures to Supplement.

---

# 15. CVIU Highlights

Elsevier Highlights generally consist of three to five concise bullet points,
each no more than 85 characters.

Candidate Highlights:

- Radial encoding is tested separately across angular harmonic scales
- Identity-disjoint inference selects a heterogeneous spectral representation
- Unsupported compression preserves full radial morphology
- The hybrid representation reduces complex coefficients by 41.98%
- Latent morphology maps exactly back to radial-harmonic Fourier space

Character count must be verified before final submission.

Avoid abbreviations such as PCA or DCT if the specific journal follows
Elsevier's general recommendation to minimize jargon in Highlights.

---

# 16. Graphical abstract candidate

A graphical abstract could use the single chain:

\[
P(\theta\mid r)
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
DCT_4
/
RAW_{72}
/
RAW_{72}
/
WAV_4
}
\]

\[
\downarrow
\]

\[
2592
\rightarrow
1504
\]

\[
\downarrow
\]

\[
PCA
\rightarrow
\Delta F_j(r,k).
\]

Main visual message:

\[
\boxed{
\text{compress where supported; preserve otherwise}.
}
\]

Do not build the graphical abstract yet unless CVIU requires or encourages one
at the submission stage.

---

# 17. Keywords for CVIU

Recommended:

- shape representation
- Fourier shape analysis
- radial-angular representation
- spectral dimensionality reduction
- statistical representation selection
- garment sketches

This is better for CVIU discoverability than leading with fashion terminology.

---

# 18. CVIU contribution paragraph

Recommended Introduction contribution paragraph:

> This study makes three contributions. First, we formulate radial encoding within
> an angular Fourier morphology field as an evidence-controlled representation
> selection problem, evaluating candidate radial representations separately across
> harmonic bands under garment-identity-disjoint and multiplicity-controlled
> validation. Second, this procedure yields a heterogeneous hybrid representation
> that applies compact radial bases only where compression is supported and
> preserves complete radial structure elsewhere. Third, we provide an exact
> inverse interpretation of the retained latent representation by mapping PCA
> perturbations back into radial-harmonic Fourier coordinates and quantifying
> their sign-invariant morphology localization.

Do not use:

> first-ever;

> novel Fourier descriptor;

> unique representation.

---

# 19. CVIU novelty sentence

Preferred:

> **The contribution is not a new spectral transform, but an evidence-controlled
> strategy for selecting how different angular harmonic ranges should be
> represented radially.**

This sentence is reviewer-resistant because it acknowledges established
transforms directly.

---

# 20. CVIU reviewer-defense paragraph

If a reviewer asks whether the method is merely Fourier + DCT + wavelets + PCA,
our formal response is:

> The component transforms are established and are not claimed as inventions.
> The methodological contribution lies in treating radial representation as a
> statistically evaluated design choice conditional on angular harmonic scale.
> Candidate radial encodings are compared using complete held-out garment
> identities and multiplicity-controlled inference, allowing compact
> representations where supported while preserving full radial structure where
> support is absent. The latent representation is subsequently interpreted
> through the exact inverse frozen representation rather than through semantic
> labels assigned post hoc.

---

# 21. CVIU generalization language

Because only CLO-SKET is analyzed, use:

> demonstrated on garment sketches;

> under the present dataset and validation framework;

> within CLO-SKET;

where needed.

Avoid:

> shape representations generally behave this way;

> all garment morphology has this spectral structure.

The Discussion should explicitly call independent shape datasets a future test.

---

# 22. External-validation issue

This is likely the largest CVIU reviewer concern.

We have two defensible choices.

## Current strategy

Submit the scientifically frozen CLO-SKET study as is and state external
replication as a limitation.

This preserves the completed analysis.

## Not recommended before first submission

Adding an unrelated second shape dataset merely to satisfy an anticipated reviewer.

That would:

- reopen the scientific analysis;
- require new representation decisions;
- require new inferential design;
- potentially turn Paper 2 into a different study.

Therefore:

\[
\boxed{
\text{do not add a second dataset unless editorial/reviewer feedback specifically requires it}.
}
\]

---

# 23. Supplement structure for CVIU

Recommended:

## Supplement S1

Dataset identity reconstruction and fold audit.

## Supplement S2

Complete candidate radial representation comparisons.

## Supplement S3

Bootstrap and permutation details.

## Supplement S4

Representation packing and provenance.

## Supplement S5

Complete latent-model comparison.

## Supplement S6

Nonlinear geometry sensitivity analyses.

## Supplement S7

All PCA morphology localization maps.

## Supplement S8

Software environment and seeds.

This keeps the main article centered on the representation contribution.

---

# 24. Reproducibility language

A CVIU reader should be able to determine:

1. how \(P(\theta\mid r)\) is constructed;
2. how \(F_k(r)\) is computed;
3. how harmonic bands are defined;
4. what radial bases are tested;
5. how grouped folds are generated;
6. what statistic selects compression;
7. how multiplicity is controlled;
8. how the final hybrid representation is assembled;
9. how PCA perturbations are inverted.

All implementation details beyond this can move to Supplement/code.

---

# 25. Data availability statement — draft

> The CLO-SKET dataset used in this study is publicly available through its
> original repository and persistent dataset identifier. Derived representations,
> analysis code, and figure-generation scripts associated with the present study
> will be made available through the accompanying research repository.

Before submission, insert the exact dataset DOI and repository release/commit.

---

# 26. Code availability statement — draft

> Code implementing the radial-angular probability representation, Fourier
> morphology construction, grouped representation-selection analysis, latent
> validation, and figure generation will be released with the manuscript
> materials. The repository will include environment information, frozen random
> seeds, execution order, and provenance checks required to reproduce the reported
> results.

Do not say code is publicly released until it actually is.

---

# 27. Conflict-of-interest statement

Prepare according to Elsevier submission requirements.

Do not invent a declaration now.

Use the actual author circumstances at submission.

---

# 28. Funding statement

Insert only verified funding information.

If there was no dedicated funding, use the journal's accepted no-funding form at
submission.

---

# 29. Author contribution statement

Prepare using CRediT roles if required by the submission system.

Possible roles may include:

- Conceptualization;
- Methodology;
- Software;
- Validation;
- Formal analysis;
- Investigation;
- Data curation;
- Visualization;
- Writing — original draft;
- Writing — review and editing.

Assign roles only to actual contributors.

---

# 30. Reference formatting

Elsevier's flexible initial-submission system generally allows references in any
consistent style at first submission, provided core bibliographic information is
complete.

Therefore:

\[
\boxed{
\text{bibliographic correctness first; journal styling second}.
}
\]

Do not waste time manually converting references before every reference has been
verified.

---

# 31. Citation-completion workflow

For every `[CITATIONS]` placeholder:

## Step A

Identify the exact claim.

## Step B

Choose the closest primary source.

## Step C

Read enough of that source to verify the methodological claim.

## Step D

Record:

- exact citation;
- DOI;
- claim supported;
- claim not supported.

## Step E

Insert citation.

## Step F

Update the Paper 2 bibliography ledger.

This should be systematic rather than ad hoc.

---

# 32. Citation table template

| Ref ID | Paper | Year | Topic | Claim supported | Directness |
|---|---|---:|---|---|---|
| R01 | Zahn & Roskies | 1972 | Fourier descriptors | harmonic contour representation | foundational |
| R02 | Zhang & Lu | 2002 | Generic Fourier Descriptor | polar Fourier shape representation | direct |
| R03 | ART reference | — | angular-radial transform | fixed polar radial-angular basis | direct |
| R04 | PHT reference | — | polar harmonic representation | separable radial/angular bases | direct |
| R05 | multiscale Fourier | — | wavelet + Fourier | established hybrid precedent | direct |
| R06 | An & Li | 2014 | fashion flat sketches | fashion-specific Fourier/wavelet precedent | direct |
| R07 | PCA/Fourier morphometrics | — | latent shape analysis | PCA on Fourier coefficients | supporting |

Fill exact metadata only after verification.

---

# 33. CVIU manuscript-length strategy

Do not artificially shorten the manuscript before checking the live journal
submission guide.

The current structure should aim for:

- concise Introduction;
- focused Related Work;
- reproducible but non-notebook-like Methods;
- compact Results;
- Discussion centered on representation implications.

Detailed diagnostics belong in Supplement.

Elsevier's general author guidance supports keeping essential experimental
procedures in the main body while placing extensive supporting material in
Supplementary Information.

---

# 34. CVIU writing style

Preferred:

- technically precise;
- direct;
- representation-focused;
- minimal promotional language.

Avoid phrases such as:

- remarkably;
- surprisingly;
- groundbreaking;
- unprecedented;
- powerful;
- revolutionary.

Let the inference carry the argument.

---

# 35. Final CVIU paper hierarchy

The reader should finish the paper remembering:

## First

\[
\boxed{
\text{radial representation support varies across harmonic scale}
}
\]

## Second

\[
\boxed{
\text{representation selection is evidence-controlled}
}
\]

## Third

\[
\boxed{
\text{unsupported compression leads to preservation}
}
\]

## Fourth

\[
\boxed{
\text{the resulting latent representation remains spectrally interpretable}
}
\]

Not:

> PCA was 44.65%.

Not:

> we tried diffusion maps.

---

# 36. Step 16 completion checklist

- [ ] CVIU-facing title selected.
- [ ] Abstract shifted toward general shape representation.
- [ ] Introduction reordered for computer-vision audience.
- [ ] Related Work weighted toward shape representation.
- [ ] Direct GFD comparison included.
- [ ] ART/PHT comparison included.
- [ ] Wavelet-Fourier prior art acknowledged.
- [ ] Fashion-flat Fourier/wavelet precedent included.
- [ ] PCA/Fourier precedent acknowledged.
- [ ] Main contribution wording narrowed appropriately.
- [ ] Four main figures retained.
- [ ] Nonlinear zoo moved largely to Supplement.
- [ ] Highlights drafted.
- [ ] Data/code availability drafts prepared.
- [ ] Citation placeholders identified.
- [ ] All citations awaiting primary-source verification marked explicitly.

---

# STEP 16 LOCK

\[
\boxed{
\textbf{PAPER 2 CVIU POSITIONING — LOCKED}
}
\]

The paper should now read as:

\[
\boxed{
\textbf{a general shape-representation methodology demonstrated on garment sketches}
}
\]

rather than:

\[
\boxed{
\text{a fashion application using Fourier transforms}.
}
\]

Next:

\[
\boxed{
\textbf{STEP 17 — VERIFIED BIBLIOGRAPHY + CLAIM-TO-CITATION MAP}
}
\]

Step 17 should verify the actual primary papers one by one and produce the final
citation ledger used to replace every `[CITATIONS]` placeholder.