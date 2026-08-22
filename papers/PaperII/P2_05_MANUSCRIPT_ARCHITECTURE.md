# CLO-SKET Paper 2 — Manuscript Architecture

## Status

**MANUSCRIPT ARCHITECTURE: LOCKED**

This document defines the scientific structure of Paper 2 before manuscript prose is written.

The architecture must preserve the locks established in:

- P2_01 — Scientific Identity
- P2_02 — Evidence Ledger
- P2_03 — Literature and Novelty Audit
- P2_04 — Novelty and Claim Lock

No section of the manuscript may introduce a stronger claim than permitted by those documents.

---

# 1. Paper identity

## Central scientific question

> Does the appropriate radial representation of probabilistic Fourier sketch morphology remain constant across angular harmonic scale, or should radial encoding vary conditionally with harmonic order?

The paper answers this through:

\[
P_i(\theta\mid r)
\rightarrow
F_{i,k}(r)
\rightarrow
\text{harmonic-dependent radial representation testing}
\]

followed by:

\[
\text{identity-disjoint inference}
\rightarrow
\text{hybrid representation}
\rightarrow
\text{latent interpretation}.
\]

---

# 2. Central methodological principle

The paper is organized around:

\[
\boxed{
\text{compress where supported; preserve where unsupported}
}
\]

This principle must remain distinct from ordinary dimensionality reduction.

The method does not assume that every spectral region should be compressed.

Instead:

\[
\text{candidate compression}
\rightarrow
\text{held-out evidence}
\rightarrow
\begin{cases}
\text{compress}, & \text{if supported},\\
\text{preserve}, & \text{if not supported}.
\end{cases}
\]

---

# 3. Research questions

The manuscript is structured around four research questions.

## RQ1 — Representation

> How can garment-sketch morphology be represented while retaining radial position and angular harmonic scale as explicit coordinates?

Answer:

\[
P_i(\theta\mid r)
\rightarrow
F_{i,k}(r).
\]

This establishes the morphology domain in which the subsequent questions are asked.

---

## RQ2 — Radial representation

> Does support for radial compression remain uniform across angular harmonic scale?

This is the **primary inferential research question**.

Answer from the frozen evidence:

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

Therefore:

\[
\boxed{
\text{uniform radial compression is not supported}
}
\]

under the tested framework.

---

## RQ3 — Latent representation

> Does detectable nonlinear geometry require replacement of PCA by a nonlinear latent representation?

Answer:

No such replacement was established under the tested validation framework.

The nonlinear models did not establish a multiplicity-controlled task advantage over PCA.

At the same time, geometric audits identified nonlinear structure.

Therefore:

\[
\boxed{
\text{nonlinear geometry}
\neq
\text{demonstrated nonlinear-model advantage}.
}
\]

---

## RQ4 — Morphology localization

> Where is variation represented by the retained PCA subspace localized in radial-harmonic Fourier coordinates?

Answer:

Within PCA-64:

\[
78.54\%
\]

of variance-weighted mapped morphology energy occurs at

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

These are descriptive retained-subspace quantities.

---

# 4. Manuscript narrative

The entire paper should follow one logical chain:

\[
\boxed{
\text{REPRESENT}
\rightarrow
\text{TEST}
\rightarrow
\text{SELECT}
\rightarrow
\text{VALIDATE}
\rightarrow
\text{INTERPRET}
}
\]

More explicitly:

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
\text{Does radial representation depend on }k?
\]

\[
\downarrow
\]

\[
\text{identity-disjoint inferential testing}
\]

\[
\downarrow
\]

\[
\mathrm{DCT/RAW/RAW/WAVELET}
\]

\[
\downarrow
\]

\[
Z_i\in\mathbb C^{1504}
\]

\[
\downarrow
\]

\[
x_i\in\mathbb R^{3008}
\]

\[
\downarrow
\]

\[
\text{PCA versus nonlinear alternatives}
\]

\[
\downarrow
\]

\[
PCA_{64}
\]

\[
\downarrow
\]

\[
\Delta F_j(r,k)
\]

\[
\downarrow
\]

\[
\text{radial-harmonic morphology localization}.
\]

Every major manuscript section should advance this chain.

---

# 5. Proposed manuscript structure

## 1. Introduction

### 1.1 Problem

Garment sketches contain geometric structure at multiple angular scales and radial positions.

A representation that collapses radial structure or imposes one compression rule across all harmonic orders may remove task-relevant morphology.

---

### 1.2 Existing approaches

Briefly introduce:

- Fourier shape descriptors;
- polar Fourier descriptors;
- angular-radial transforms;
- polar harmonic transforms;
- multiscale Fourier representations;
- Fourier-wavelet descriptors;
- fashion-sketch descriptors;
- learned sketch embeddings.

Do not turn the Introduction into the full literature review.

---

### 1.3 Gap

Lead directly to:

> Existing radial-angular descriptors generally specify their radial basis or multiscale construction as part of the representation design. It remains less clear whether the appropriate radial representation itself should vary across angular harmonic scale and whether compression decisions can instead be determined from held-out statistical evidence.

---

### 1.4 Proposed approach

Introduce:

\[
P(\theta\mid r)
\rightarrow
F_k(r)
\]

followed by harmonic-band-specific radial representation testing.

State the philosophy:

> Compression is retained only where supported; otherwise the complete radial structure is preserved.

---

### 1.5 Contributions

Use three primary contributions.

**Contribution 1**

Evidence-controlled radial representation selection separately across angular harmonic bands.

**Contribution 2**

A heterogeneous hybrid representation that combines compact and uncompressed radial encodings according to identity-disjoint inferential support.

**Contribution 3**

Exact mapping of retained latent perturbations back into radial-harmonic Fourier morphology for interpretable localization.

Optionally state the empirical result separately rather than calling it a fourth methodological contribution.

---

# 6. Related Work

Related Work should be organized by the scientific gap, not chronologically.

## 2.1 Fourier and polar shape representations

Cover:

- classical Fourier descriptors;
- polar Fourier representations;
- Generic Fourier Descriptor.

Purpose:

Establish that Fourier and radial-angular shape description are prior art.

End with the distinction:

> Paper 2 retains \(F_k(r)\) explicitly and asks whether its radial encoding should vary across \(k\).

---

## 2.2 Angular-radial and polar harmonic transforms

Cover:

- Angular Radial Transform;
- Polar Harmonic Transform;
- related orthogonal moments.

General form:

\[
R_n(r)e^{im\theta}.
\]

Distinction:

> These methods specify radial bases analytically; Paper 2 treats radial representation as an inferentially evaluated design decision.

---

## 2.3 Wavelet and multiscale Fourier descriptors

Cover:

- wavelet shape descriptors;
- multiscale Fourier descriptors;
- Fourier-wavelet combinations.

Explicitly acknowledge that Fourier + wavelet is established.

Distinction:

> Wavelet representation is one candidate basis rather than an assumed global representation.

---

## 2.4 Fashion-sketch representation

Cover:

- fashion-flat Wavelet Fourier Descriptor;
- sketch retrieval;
- sketch-photo embedding;
- deep sketch representations;
- generative fashion-sketch systems.

Establish the difference in research objective:

\[
\text{retrieval/generation}
\neq
\text{explicit statistical morphology analysis}.
\]

---

## 2.5 Fourier morphometrics and latent interpretation

Cover:

- PCA on Fourier coefficients;
- morphology reconstruction along PC axes.

Acknowledge this precedent explicitly.

Then motivate the exact hybrid inverse mapping:

\[
PC_j
\rightarrow
\Delta F_j(r,k).
\]

---

# 7. Methods

Methods should mirror the mathematical dependency graph.

## 3.1 Dataset and analysis units

Report:

- 2300 sketches;
- 230 garment identities;
- 23 categories;
- 10 identities/category;
- repeated sketches within identities.

Explain why garment identity is the relevant grouping unit.

No result should appear here.

---

## 3.2 Probabilistic radial-angular morphology

Define:

\[
P_i(\theta\mid r).
\]

For occupied shells:

\[
P_i(\theta\mid r)\geq0
\]

and

\[
\sum_\theta P_i(\theta\mid r)=1.
\]

Describe treatment of empty shells explicitly.

---

## 3.3 Angular Fourier morphology

Define:

\[
F_{i,k}(r)
=
\sum_\theta
P_i(\theta\mid r)e^{-ik\theta}.
\]

Use:

\[
r=1,\ldots,72
\]

and

\[
k=1,\ldots,36.
\]

Explain that \(r\) remains explicit.

This is essential.

---

## 3.4 Harmonic-band partition

Define:

\[
1{:}4,\qquad
5{:}12,\qquad
13{:}24,\qquad
25{:}36.
\]

Explain why representation selection is evaluated separately across these frozen bands.

Do not justify bands retrospectively using the final results.

---

## 3.5 Candidate radial representations

Describe candidate radial encodings.

Include:

- raw radial field;
- DCT compression;
- wavelet compression;
- retained coefficient counts.

No winner should be stated yet.

---

## 3.6 Garment-identity-disjoint validation

This subsection is critical.

Define the grouping structure and ensure:

\[
G_{\text{train}}
\cap
G_{\text{test}}
=
\varnothing.
\]

Explain:

- grouped folds;
- category balance;
- complete identity separation;
- why individual sketches are not treated as independent identities.

---

## 3.7 Compression inference

Define:

- evaluation statistic;
- category-balanced effect;
- bootstrap;
- permutation procedure;
- simultaneous inference;
- FWER correction.

The reader should understand exactly what constitutes evidence for retaining compression.

State the decision rule before presenting any results.

---

## 3.8 Frozen hybrid representation

Only after the selection procedure has been defined, describe the representation mathematically as a procedure.

Avoid presenting the observed winning bases as though they were predetermined.

The Methods can state that the selected representation is frozen after inference, but the inferential outcomes themselves belong primarily in Results.

---

## 3.9 Exact complex-to-real packing

Define:

\[
\rho(A)
=
[
\Re(\operatorname{vec}(A)),
\Im(\operatorname{vec}(A))
].
\]

Explain block-wise packing.

Mention exact numerical lineage verification.

---

## 3.10 Standardization and PCA

Define:

\[
\tilde{x}_{im}
=
\frac{x_{im}-\mu_m}{\sigma_m}
\]

and

\[
z_{ij}
=
v_j^\top\tilde{x}_i.
\]

Explain PCA as:

> an orthogonal descriptive latent basis.

Not:

> a semantic latent factor model.

---

## 3.11 Nonlinear latent-model comparison

Describe tested nonlinear alternatives and the common validation framework.

Keep:

\[
\text{model utility}
\]

separate from:

\[
\text{geometry audit}.
\]

---

## 3.12 Nonlinear geometry audit

Describe:

- Isomap/neighborhood geometry;
- principal-curve stability;
- diffusion-map sensitivity analysis.

These are characterization analyses.

They should not become a second paper inside Paper 2.

---

## 3.13 PCA morphology perturbation

Define:

\[
\Delta x_j
=
D_\sigma
[
\sqrt{\lambda_j}v_j
].
\]

Map:

\[
\Delta x_j
\rightarrow
\Delta F_j(r,k).
\]

Then:

\[
E_j(r,k)
=
|\Delta F_j(r,k)|^2.
\]

Explain sign invariance.

---

## 3.14 Radial-harmonic morphology localization

Define:

\[
p_j(r,k)
=
\frac{E_j(r,k)}
{\sum_r\sum_kE_j(r,k)}.
\]

Define radial zones:

- inner: 1–24;
- middle: 25–48;
- outer: 49–72.

Define harmonic bands.

Then:

\[
P_j(R,B)
=
\sum_{r\in R}
\sum_{k\in B}
p_j(r,k).
\]

Variance weighting:

\[
w_j
=
\frac{\eta_j}
{\sum_{\ell=1}^{64}\eta_\ell}
\]

and

\[
\bar P(R,B)
=
\sum_{j=1}^{64}
w_jP_j(R,B).
\]

State explicitly:

> These quantities characterize the retained PCA-64 subspace and not total garment morphology.

---

# 8. Results

Results must answer the RQs in order.

## 4.1 Harmonic-dependent radial compression

This is the main Results section.

Report all four bands, including negative results.

### \(k=1{:}4\)

\[
\Delta=0.059306
\]

\[
95\%\,CI=[0.023295,0.108196]
\]

\[
p_{\mathrm{FWER}}=0.000200.
\]

Supported:

\[
\mathrm{DCT}_4.
\]

### \(k=5{:}12\)

\[
\Delta=0.005984
\]

\[
95\%\,CI=[-0.014164,0.060361]
\]

\[
p_{\mathrm{FWER}}=0.608939.
\]

Compression not supported.

### \(k=13{:}24\)

\[
\Delta=0.010959
\]

\[
95\%\,CI=[-0.003088,0.073320]
\]

\[
p_{\mathrm{FWER}}=0.487751.
\]

Compression not supported.

### \(k=25{:}36\)

\[
\Delta=0.039300
\]

\[
95\%\,CI=[0.019130,0.091021]
\]

\[
p_{\mathrm{FWER}}=0.019698.
\]

Supported:

\[
\mathrm{db4}_4.
\]

Conclude only:

\[
\boxed{
\text{radial compression support differed across harmonic bands}.
}
\]

---

## 4.2 Evidence-supported hybrid representation

Report:

\[
2592
\rightarrow
1504
\]

complex coefficients.

Reduction:

\[
\boxed{41.98\%}.
\]

Compression ratio:

\[
\boxed{1.7234\times}.
\]

After real packing:

\[
\boxed{3008}
\]

real dimensions.

Do not call discarded coefficients noise.

---

## 4.3 Latent-model validation

Report PCA versus nonlinear alternatives.

Central result:

> Tested nonlinear latent models did not establish a multiplicity-controlled task advantage over PCA.

Then state that PCA is retained as the practical latent baseline.

---

## 4.4 Nonlinear geometry audit

Report the geometric findings succinctly.

Required logic:

\[
\text{nonlinear structure detected}
\]

but

\[
\text{stable canonical nonlinear replacement not established}.
\]

Do not let this section dominate the paper.

---

## 4.5 PCA morphology localization

Report:

\[
PCA_{64}
=
44.65\%
\]

of standardized representation variance.

Then:

\[
\boxed{78.54\%}
\]

intermediate harmonic,

\[
\boxed{66.84\%}
\]

outer radial,

and

\[
\boxed{51.30\%}
\]

outer × intermediate.

Explicitly state that these percentages refer only to retained PCA-64 morphology energy.

---

# 9. Discussion

Discussion should contain five arguments.

## 5.1 Radial redundancy is harmonic-scale dependent

This is the central interpretation.

Do not imply monotonicity.

The observed structure is:

\[
\text{compact}
\rightarrow
\text{preserved}
\rightarrow
\text{preserved}
\rightarrow
\text{compact}
\]

rather than a simple increasing/decreasing complexity gradient.

---

## 5.2 Compression should be evidence-controlled

Discuss the methodological principle:

\[
\boxed{
\text{absence of support for compression}
\rightarrow
\text{preserve structure}.
}
\]

This is more important than the fact that the final representation happens to use DCT and wavelets.

---

## 5.3 Morphology is not a low-frequency-signal/high-frequency-noise hierarchy

Use the intermediate-harmonic PCA localization to qualify simplistic Fourier interpretations.

Do not say high harmonics are signal either.

The conclusion is:

> morphology is organized across spectral scales.

---

## 5.4 Nonlinear geometry does not imply nonlinear-model necessity

Discuss:

\[
\text{geometry}
\neq
\text{model utility}.
\]

PCA remains useful because of validation and interpretability, not because the geometry was proven linear.

---

## 5.5 Interpretation boundaries and limitations

Mandatory limitations:

1. PCA-64 retains only 44.65% of standardized representation variance.
2. Radial zones are equal-shell descriptive partitions.
3. Radial zones lack semantic garment annotations.
4. PCA axes are not semantic or causal factors.
5. Nonlinear negative results apply only to tested models/settings.
6. Generalization beyond CLO-SKET remains unestablished.
7. Harmonic-band boundaries are part of the present framework and should be tested independently in future datasets.

---

# 10. Conclusion

The Conclusion should be short.

Logical structure:

> We represented garment sketches as probabilistic radial-angular Fourier morphology.

Then:

> Radial compression support differed across harmonic scale.

Then:

> This motivated an evidence-controlled hybrid representation that compressed supported bands while preserving unsupported-to-compress radial structure.

Then:

> Mapping retained PCA variation back into Fourier morphology revealed structured radial-harmonic organization.

Finish with the broader principle:

\[
\boxed{
\text{representation reduction should follow evidence rather than precede it}.
}
\]

Do not introduce new results in the Conclusion.

---

# 11. Figure architecture

The main manuscript should use four primary figures.

---

## Figure 1 — Representation

### Purpose

Explain:

\[
P(\theta\mid r)
\rightarrow
F_k(r).
\]

### Panels

**A.** Example garment sketch.

**B.** radial-angular coordinate construction.

**C.**

\[
P(\theta\mid r)
\]

heatmap.

**D.**

\[
|F_k(r)|
\]

radial-harmonic heatmap.

**E.** conceptual harmonic-band partition.

### Role

**Methods / representation figure**

No inferential claim.

---

## Figure 2 — Harmonic-dependent radial representation

### Purpose

This is the **main paper figure**.

### Panels

**A.** four harmonic bands.

**B.** candidate radial encodings.

**C.** category-balanced effects with bootstrap intervals.

**D.** FWER-controlled decisions.

**E.** final:

\[
\boxed{
DCT_4/RAW_{72}/RAW_{72}/WAV_4
}
\]

representation.

**F.** coefficient reduction:

\[
2592\rightarrow1504.
\]

### Role

**Primary inferential figure**

If a reviewer remembers one figure, it should be Figure 2.

---

## Figure 3 — Latent validation and geometry

### Purpose

Separate:

\[
\text{task utility}
\]

from:

\[
\text{geometric nonlinearity}.
\]

### Possible panels

**A.** PCA versus nonlinear model performance.

**B.** multiplicity-controlled comparison.

**C.** Isomap geometry audit.

**D.** principal-curve stability.

**E.** diffusion-map sensitivity result.

### Role

**Validation / sensitivity figure**

Keep compact.

---

## Figure 4 — PCA morphology localization

### Purpose

Show:

\[
PC_j
\rightarrow
\Delta F_j(r,k)
\rightarrow
E_j(r,k).
\]

### Panels

**A.** inverse-mapping schematic.

**B.** example PC energy maps.

**C.** harmonic-band energy distribution.

**D.** radial-zone distribution.

**E.** \(3\times4\) radial × harmonic localization matrix.

Highlight descriptively:

\[
78.54\%,\quad
66.84\%,\quad
51.30\%.
\]

### Role

**Interpretability / morphology figure**

---

# 12. Table architecture

Avoid too many tables.

## Table 1 — Dataset and representation

Include:

- sketches;
- garment identities;
- categories;
- radial shells;
- angular harmonics;
- harmonic bands;
- original dimensions;
- hybrid dimensions.

---

## Table 2 — Radial compression inference

Columns:

| Harmonic band | Candidate retained | Effect | 95% CI | \(p_{\mathrm{FWER}}\) | Decision |
|---|---|---:|---:|---:|---|

This is the main quantitative table.

---

## Optional Table 3 — Latent-model comparison

Only if the results cannot be communicated cleanly in Figure 3.

Otherwise move it to Supplementary Material.

---

# 13. Supplementary architecture

The supplement should contain technical material needed for reproducibility but not central narrative flow.

Suggested sections:

## S1 — Dataset identity reconstruction

## S2 — Grouped-fold verification

## S3 — Complete candidate compression grid

## S4 — Bootstrap implementation

## S5 — Permutation and max-statistic implementation

## S6 — FWER decision details

## S7 — Frozen representation dimensions

## S8 — Exact real/complex packing audit

Including:

\[
\texttt{BLOCK\_FLAT\_REAL\_THEN\_IMAG}.
\]

## S9 — PCA implementation details

## S10 — Full nonlinear-model comparison

## S11 — Isomap sensitivity

## S12 — Principal-curve stability

## S13 — Diffusion-map audit

## S14 — Complete PCA morphology maps

## S15 — PC-specific radial/harmonic localization

## S16 — Reproducibility / software / random seeds

---

# 14. Evidence-to-section map

| Evidence | Manuscript location |
|---|---|
| \(P(\theta\mid r)\) | Methods 3.2 |
| \(F_k(r)\) | Methods 3.3 |
| harmonic bands | Methods 3.4 |
| compression candidates | Methods 3.5 |
| grouped validation | Methods 3.6 |
| FWER inference | Methods 3.7 |
| compression results | Results 4.1 |
| hybrid representation | Results 4.2 |
| PCA/nonlinear comparison | Results 4.3 |
| geometry audit | Results 4.4 |
| PCA inverse mapping | Methods 3.13 |
| localization definition | Methods 3.14 |
| localization results | Results 4.5 |
| scientific interpretation | Discussion |
| novelty comparison | Introduction + Related Work |

---

# 15. Figure-to-RQ map

| Research question | Primary figure |
|---|---|
| RQ1 — How is morphology represented? | Figure 1 |
| RQ2 — Does radial encoding vary across harmonic scale? | **Figure 2** |
| RQ3 — Is nonlinear representation required? | Figure 3 |
| RQ4 — Where is retained latent morphology localized? | Figure 4 |

This creates a simple reviewer-facing structure:

\[
\boxed{
1\ RQ
\leftrightarrow
1\ primary\ figure
}
\]

---

# 16. Importance hierarchy

Not every result receives equal manuscript weight.

## Tier 1 — Core paper

\[
\boxed{
\text{harmonic-dependent radial compression inference}
}
\]

and

\[
\boxed{
\text{evidence-controlled hybrid representation}.
}
\]

These must dominate the Abstract, Introduction, Results, and Discussion.

---

## Tier 2 — Strong supporting result

\[
\boxed{
\text{PCA radial-harmonic morphology localization}.
}
\]

This demonstrates what the representation enables scientifically.

---

## Tier 3 — Validation / qualification

\[
\boxed{
\text{PCA versus nonlinear models}
}
\]

and

\[
\boxed{
\text{nonlinear geometry audits}.
}
\]

These strengthen the choice of latent representation.

They must not become the paper's central story.

---

# 17. Material deliberately excluded from the main story

Do not expand the manuscript around:

- nonlinear-PCA zoo comparisons;
- Isomap as an alternative final representation;
- principal curves as a morphology trajectory;
- diffusion maps as another proposed model;
- semantic interpretation of individual PCs;
- garment-part claims without annotations;
- new compression experiments;
- arbitrary additional transforms.

These analyses may support sensitivity or supplementary evidence.

They do not redefine the paper.

---

# 18. Abstract architecture

The Abstract should follow six moves.

### Sentence 1 — Problem

Uniform dimensional reduction may discard radial morphology differently across angular harmonic scales.

### Sentence 2 — Representation

Introduce:

\[
P(\theta\mid r)\rightarrow F_k(r).
\]

### Sentence 3 — Method

State harmonic-specific, identity-disjoint, multiplicity-controlled radial representation testing.

### Sentence 4 — Main result

Report DCT/raw/raw/wavelet outcome and coefficient reduction.

### Sentence 5 — Latent result

Briefly state PCA/nonlinear result and retained morphology localization.

### Sentence 6 — Conclusion

State harmonic-dependent radial representation rather than uniform compression.

Do not lead the Abstract with PCA.

---

# 19. Introduction architecture

The Introduction should contain approximately five conceptual paragraphs.

## Paragraph 1

Scientific problem:

multi-scale garment-sketch morphology.

## Paragraph 2

Existing spectral/radial-angular approaches.

## Paragraph 3

Unresolved representation-selection problem.

## Paragraph 4

Our framework and inferential philosophy.

## Paragraph 5

Contributions and paper roadmap.

The Introduction should reach the research gap quickly.

---

# 20. Results architecture

The Results must preserve the following order:

\[
\boxed{
\text{compression inference}
}
\]

first.

Then:

\[
\boxed{
\text{hybrid representation}
}
\]

then:

\[
\boxed{
\text{latent validation}
}
\]

then:

\[
\boxed{
\text{morphology interpretation}.
}
\]

Never begin Results with PCA.

Otherwise the reader may incorrectly infer that PCA is the main contribution.

---

# 21. Discussion architecture

The Discussion must answer:

### What did we discover?

Radial representation requirements differ across harmonic scale.

### Why does it matter?

Uniform compression is not automatically justified.

### What principle follows?

Compress where supported; preserve where unsupported.

### What does the latent analysis add?

Retained variation is radially and spectrally structured.

### What does it NOT prove?

No semantic garment parts, no causal PCs, no globally linear manifold, no universal optimal basis.

---

# 22. Manuscript claim flow

The paper should progressively increase claim strength only when evidence allows it:

\[
\text{definition}
\]

\[
\downarrow
\]

\[
\text{measurement}
\]

\[
\downarrow
\]

\[
\text{inference}
\]

\[
\downarrow
\]

\[
\text{representation decision}
\]

\[
\downarrow
\]

\[
\text{descriptive latent characterization}
\]

\[
\downarrow
\]

\[
\text{qualified interpretation}.
\]

Never reverse this order.

---

# 23. Working title candidates

## Candidate A — strongest current option

**Harmonic-Dependent Radial Representation in Probabilistic Fourier Garment Morphology**

Strength:

Scientific and precise.

---

## Candidate B

**Evidence-Controlled Radial-Spectral Representation of Garment-Sketch Morphology**

Strength:

Highlights the methodological contribution.

---

## Candidate C

**Probabilistic Fourier Morphology with Harmonic-Conditioned Radial Representation**

Strength:

Method-focused and compact.

---

## Candidate D

**Compress Where Supported: Evidence-Controlled Radial Representation of Fourier Garment Morphology**

Strength:

Memorable.

Risk:

Possibly too informal for some journals.

---

## Current provisional preference

\[
\boxed{
\textbf{Evidence-Controlled Radial-Spectral Representation of Garment-Sketch Morphology}
}
\]

Final title remains unlocked until target-journal selection.

---

# 24. One-paragraph paper blueprint

> Paper 2 represents garment sketches as conditional radial-angular probability fields and transforms their angular structure into radial Fourier harmonic functions \(F_k(r)\). Rather than imposing a uniform radial basis, candidate radial representations are evaluated separately across angular harmonic bands under garment-identity-disjoint, multiplicity-controlled inference. The resulting evidence-supported hybrid representation applies compact DCT encoding to low harmonics, retains complete radial structure across intermediate harmonics, and applies compact wavelet encoding to the highest tested harmonics. After validating PCA against nonlinear latent alternatives, retained PCA perturbations are mapped exactly back into radial-harmonic Fourier space to characterize the spatial-spectral organization of latent morphology. The paper therefore connects inferential representation selection with interpretable spectral morphology while explicitly preserving structure where compression is unsupported.

---

# 25. Paper architecture in one diagram

\[
\boxed{
\begin{array}{c}
\textbf{PROBLEM}\\
\text{Uniform radial compression may be unjustified}\\[4pt]
\downarrow\\[4pt]

\textbf{REPRESENTATION}\\
P(\theta\mid r)\rightarrow F_k(r)\\[4pt]
\downarrow\\[4pt]

\textbf{PRIMARY TEST}\\
\text{Does radial compression support vary with }k?\\[4pt]
\downarrow\\[4pt]

\textbf{INFERENCE}\\
\text{identity-disjoint + FWER controlled}\\[4pt]
\downarrow\\[4pt]

\textbf{REPRESENTATION LOCK}\\
DCT_4/RAW_{72}/RAW_{72}/WAV_4\\[4pt]
\downarrow\\[4pt]

\textbf{LATENT VALIDATION}\\
PCA\quad\text{vs}\quad\text{nonlinear alternatives}\\[4pt]
\downarrow\\[4pt]

\textbf{INTERPRETATION}\\
PC_j\rightarrow\Delta F_j(r,k)\\[4pt]
\downarrow\\[4pt]

\textbf{SCIENTIFIC FINDING}\\
\text{structured radial-harmonic morphology}\\[4pt]
\downarrow\\[4pt]

\textbf{PRINCIPLE}\\
\text{compress where supported;}\\
\text{preserve where unsupported}
\end{array}
}
\]

---

# 26. Architecture guard

Before adding any section, figure, experiment, or claim, ask:

### Question 1

Does it help answer one of RQ1–RQ4?

If no:

**exclude or move to Supplementary Material.**

### Question 2

Does it alter the frozen representation?

If yes:

**do not add without reopening the evidence lock.**

### Question 3

Is it stronger than the Evidence Ledger permits?

If yes:

**rewrite or remove.**

### Question 4

Is it another interesting manifold experiment?

If yes:

**STOP.**

The nonlinear zoo is closed.

---

# 27. Step 5 lock

\[
\boxed{
\textbf{PAPER 2 MANUSCRIPT ARCHITECTURE — LOCKED}
}
\]

The scientific hierarchy is:

\[
\boxed{
\textbf{PRIMARY}
=
\text{harmonic-dependent radial representation inference}
}
\]

\[
\boxed{
\textbf{SECONDARY}
=
\text{evidence-supported hybrid representation}
}
\]

\[
\boxed{
\textbf{INTERPRETABILITY}
=
\text{latent-to-radial-harmonic morphology mapping}
}
\]

\[
\boxed{
\textbf{VALIDATION}
=
\text{nonlinear geometry/model-utility audit}
}
\]

Next:

\[
\boxed{
\textbf{STEP 6 — FIGURE + TABLE BLUEPRINT}
}
\]

Only after the figure/table evidence structure is frozen should full manuscript prose be assembled.