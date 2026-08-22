# CLO-SKET Paper 2 — Figure and Table Blueprint

## Status

**FIGURE + TABLE ARCHITECTURE: LOCKED**

This document defines the visual evidence architecture for Paper 2.

The manuscript uses four primary figures:

\[
\boxed{
\text{Representation}
\rightarrow
\text{Inference}
\rightarrow
\text{Validation}
\rightarrow
\text{Interpretation}
}
\]

The central figure is Figure 2.

No figure may introduce a scientific claim that is absent from the frozen Evidence Ledger.

---

# 1. Visual hierarchy

The figures answer the four research questions directly.

| Figure | Research question | Evidence role |
|---|---|---|
| Figure 1 | What is the morphology representation? | Mathematical / descriptive |
| Figure 2 | Does radial representation depend on harmonic scale? | **Primary inferential** |
| Figure 3 | Is nonlinear latent representation required? | Validation / qualification |
| Figure 4 | Where is retained latent variation localized? | Mathematical + descriptive |

The visual narrative is:

\[
\boxed{
P(\theta\mid r)
\rightarrow
F_k(r)
\rightarrow
\text{representation test}
\rightarrow
\text{hybrid lock}
\rightarrow
\text{latent validation}
\rightarrow
\text{morphology localization}
}
\]

---

# 2. Figure 1 — Probabilistic radial-angular Fourier morphology

## Scientific purpose

Figure 1 teaches the reader the representation.

It should answer:

> What exactly is \(F_k(r)\), and why are both \(r\) and \(k\) retained?

It should contain no primary statistical result.

---

## Figure 1A — Example sketch

Show one representative CLO-SKET garment sketch.

Overlay only the minimum geometry needed to establish:

- morphology center;
- radial coordinate \(r\);
- angular coordinate \(\theta\).

Avoid clutter.

### Message

A garment sketch is represented relative to radial and angular position.

---

## Figure 1B — Radial-angular construction

Show the transformation from sketch geometry into radial shells and angular bins.

Conceptually:

\[
(x,y)
\rightarrow
(r,\theta).
\]

Illustrate:

- concentric radial shells;
- angular sectors;
- occupied morphology.

### Message

Spatial morphology is reorganized into explicit radial-angular coordinates.

---

## Figure 1C — Conditional probability field

Show:

\[
P_i(\theta\mid r).
\]

Preferred visualization:

**heatmap**

with:

- x-axis: angular position \(\theta\);
- y-axis: radial shell \(r\);
- intensity: conditional probability.

Include:

\[
\sum_\theta P_i(\theta\mid r)=1
\]

for occupied shells.

### Message

Angular morphology is represented conditionally at each radius.

---

## Figure 1D — Angular Fourier morphology

Show:

\[
F_{i,k}(r)
=
\sum_\theta
P_i(\theta\mid r)e^{-ik\theta}.
\]

Preferred visualization:

\[
|F_{i,k}(r)|
\]

heatmap.

Axes:

- x-axis: harmonic order \(k\);
- y-axis: radial shell \(r\).

### Message

Angular Fourier transformation retains radial position explicitly.

---

## Figure 1E — Harmonic bands

Show the frozen partition:

\[
1{:}4
\]

\[
5{:}12
\]

\[
13{:}24
\]

\[
25{:}36.
\]

Use simple vertical partitions over the \(r\times k\) field.

Do not show compression decisions yet.

### Message

Radial representation will subsequently be evaluated separately across harmonic ranges.

---

## Figure 1 claim boundary

### Figure supports

> The representation preserves explicit radial and angular-harmonic coordinates.

### Figure does NOT support

- semantic garment parts;
- frequency importance;
- compression superiority;
- signal-versus-noise interpretation.

---

# 3. Figure 2 — Harmonic-dependent radial representation

# THIS IS THE PRIMARY PAPER FIGURE

If a reader remembers one result from Paper 2, it should be Figure 2.

Its scientific question is:

\[
\boxed{
\text{Does support for radial compression depend on angular harmonic scale?}
}
\]

---

## Figure 2A — Representation candidates

For each harmonic band, show candidate radial representations schematically:

\[
F_k(r)
\]

followed by alternatives such as:

\[
RAW
\]

\[
DCT_B
\]

\[
WAVELET_B.
\]

This panel should communicate that radial representation is a **tested design choice**, not predetermined.

---

## Figure 2B — Validation design

Show:

\[
2300\ \text{sketches}
\]

nested within:

\[
230\ \text{garment identities}
\]

across:

\[
23\ \text{categories}.
\]

Then illustrate:

\[
G_{\text{train}}
\cap
G_{\text{test}}
=
\varnothing.
\]

Use grouped identity blocks rather than individual sketch icons if necessary.

### Message

Representation decisions are evaluated on unseen garment identities.

---

## Figure 2C — Band-specific inferential effects

This is the central quantitative panel.

Plot one point and bootstrap interval for each harmonic band.

Required values:

### \(k=1{:}4\)

\[
\Delta=0.059306
\]

\[
95\%\ CI=[0.023295,\ 0.108196]
\]

\[
p_{\mathrm{FWER}}=0.000200.
\]

### \(k=5{:}12\)

\[
\Delta=0.005984
\]

\[
95\%\ CI=[-0.014164,\ 0.060361]
\]

\[
p_{\mathrm{FWER}}=0.608939.
\]

### \(k=13{:}24\)

\[
\Delta=0.010959
\]

\[
95\%\ CI=[-0.003088,\ 0.073320]
\]

\[
p_{\mathrm{FWER}}=0.487751.
\]

### \(k=25{:}36\)

\[
\Delta=0.039300
\]

\[
95\%\ CI=[0.019130,\ 0.091021]
\]

\[
p_{\mathrm{FWER}}=0.019698.
\]

Include a vertical zero-effect reference.

### Critical visual rule

Supported and unsupported results must receive equal visual treatment.

Do not visually hide the negative results.

---

## Figure 2D — Multiplicity-controlled decision

Show the four final decisions:

\[
k=1{:}4
\rightarrow
\boxed{DCT_4}
\]

\[
k=5{:}12
\rightarrow
\boxed{RAW_{72}}
\]

\[
k=13{:}24
\rightarrow
\boxed{RAW_{72}}
\]

\[
k=25{:}36
\rightarrow
\boxed{db4_4}.
\]

This panel should make the heterogeneous structure immediately visible:

\[
\boxed{
DCT/RAW/RAW/WAVELET
}
\]

---

## Figure 2E — Frozen hybrid representation

Show:

\[
Z_i
=
[
DCT_4
\mid
RAW_{72}
\mid
RAW_{72}
\mid
WAV_4
].
\]

Label dimensions:

\[
16
+
576
+
864
+
48
=
1504
\]

complex coefficients.

---

## Figure 2F — Representation reduction

Show:

\[
2592
\rightarrow
1504
\]

complex coefficients.

Then:

\[
\boxed{41.98\%\ reduction}
\]

and optionally:

\[
1.7234\times
\]

compression ratio.

### Important wording

Use:

> coefficient reduction

not:

> information removed

or:

> noise removed.

---

# 4. Figure 2 central caption claim

The caption should eventually contain a sentence close to:

> Radial compression support differed across angular harmonic bands under garment-identity-disjoint, family-wise-error-rate-controlled inference, yielding a heterogeneous DCT/raw/raw/wavelet representation rather than a uniform radial compression rule.

That is the visual heart of the paper.

---

# 5. Figure 3 — Latent validation and nonlinear geometry

## Scientific purpose

Figure 3 answers:

> Does detectable nonlinear geometry justify replacing PCA with a nonlinear latent representation?

The required distinction is:

\[
\boxed{
\text{geometry}
\neq
\text{model utility}.
}
\]

Figure 3 should be smaller and visually quieter than Figure 2.

---

## Figure 3A — PCA versus nonlinear models

Show validated task performance for:

- PCA;
- tested nonlinear alternatives.

Use the exact frozen performance metric and uncertainty structure from the corresponding validation cells.

Do not cherry-pick one metric if multiple confirmatory metrics were frozen.

### Message

Nonlinear task superiority was not established.

---

## Figure 3B — Multiplicity-controlled model comparison

Show the confirmatory differences relative to PCA.

The visual conclusion should be:

\[
\boxed{
\text{no multiplicity-controlled nonlinear advantage established}.
}
\]

Do NOT label PCA as universally superior.

---

## Figure 3C — Nonlinear geometry audit

Show the strongest compact geometric evidence for departure from a purely linear description.

Potential content:

- neighborhood preservation;
- Isomap dimensional behavior;
- curvature diagnostic.

Only one concise panel is necessary.

---

## Figure 3D — Principal-curve stability

Show the instability result succinctly.

The reader should see:

\[
\text{candidate nonlinear trajectory}
\]

but:

\[
\boxed{
\text{stable 1D canonical trajectory not established}.
}
\]

---

## Figure 3E — Diffusion-map sensitivity

Only include this in the main figure if it materially contributes to the conclusion.

Otherwise:

\[
\boxed{
\text{MOVE TO SUPPLEMENT}
}
\]

The main manuscript does not need to display every nonlinear experiment.

---

# 6. Figure 3 claim boundary

### Supported

> Nonlinear geometric structure was detectable, but the tested nonlinear representations did not establish a validated practical replacement for PCA.

### Not supported

> PCA proves the morphology space is linear.

> PCA is the true morphology manifold.

> Nonlinear methods are inferior in general.

---

# 7. Figure 4 — Latent-to-Fourier morphology localization

## Scientific purpose

Figure 4 demonstrates what the frozen representation enables scientifically.

It answers:

> Where is retained PCA variation expressed in radial-harmonic morphology space?

---

## Figure 4A — Exact inverse-mapping schematic

Show:

\[
PC_j
\]

\[
\downarrow
\]

\[
\sqrt{\lambda_j}v_j
\]

\[
\downarrow
\]

\[
\Delta x_j
\]

\[
\downarrow
\]

\[
\text{exact block-wise inverse}
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
E_j(r,k)
=
|\Delta F_j(r,k)|^2.
\]

This panel is conceptual rather than quantitative.

---

## Figure 4B — Example PC morphology-energy maps

Show selected representative PCs.

Preferred:

- one leading outer-radial PC;
- one later PC with stronger inner-radial localization;
- optionally one qualitatively different intermediate mode.

Do not select examples because they look aesthetically impressive.

Selection criterion must be explicit and reproducible.

---

## Figure 4C — Harmonic localization

Show the variance-weighted energy by harmonic band.

The key result:

\[
\boxed{
78.54\%
}
\]

for:

\[
k=5{:}24.
\]

Complement:

\[
21.46\%
\]

for the low and high extreme bands together.

If four bands are plotted individually, retain the original four-band structure.

---

## Figure 4D — Radial localization

Show:

- inner;
- middle;
- outer.

Key result:

\[
\boxed{
66.84\%
}
\]

outer-radial.

### Caption guard

State:

> outer radial zone

not:

> garment boundary

or:

> silhouette.

---

## Figure 4E — Joint radial × harmonic localization

Create a:

\[
3\times4
\]

matrix.

Rows:

- inner;
- middle;
- outer.

Columns:

\[
1{:}4,\quad
5{:}12,\quad
13{:}24,\quad
25{:}36.
\]

Each cell contains:

\[
\bar P(R,B).
\]

Highlight descriptively:

\[
\boxed{
51.30\%
}
\]

for:

\[
\text{outer radial}
\times
k=5{:}24
\]

when the two intermediate columns are aggregated.

---

# 8. Figure 4 interaction guard

This is important.

We have:

\[
P(\text{outer})=0.6684
\]

and:

\[
P(k=5{:}24)=0.7854.
\]

Their product is approximately:

\[
0.6684\times0.7854
\approx0.525.
\]

Observed joint localization:

\[
0.5130.
\]

Therefore Figure 4 must NOT visually imply a statistical interaction.

Do not use language such as:

- enrichment;
- synergy;
- interaction;
- preferential coupling.

unless such a hypothesis is formally tested later.

The correct language is:

> joint localization.

---

# 9. Figure 4 retained-subspace guard

Every relevant Figure 4 caption must make clear that the localization concerns:

\[
\boxed{
\text{the retained PCA-64 subspace}
}
\]

which accounts for:

\[
\boxed{
44.65\%
}
\]

of standardized representation variance.

Do not write:

> 78.54% of garment morphology.

Write:

> 78.54% of variance-weighted mapped morphology energy within the retained PCA-64 subspace.

---

# 10. Main Table 1 — Dataset and representation contract

Suggested structure:

| Property | Value |
|---|---:|
| Sketches | 2300 |
| Garment identities | 230 |
| Categories | 23 |
| Radial shells | 72 |
| Positive angular harmonics | 36 |
| Original complex coefficients | 2592 |
| Frozen hybrid complex coefficients | 1504 |
| Frozen real dimensions | 3008 |
| PCA retained dimensions | 64 |
| PCA-64 standardized variance | 44.65% |

This table establishes the dimensional contract.

No inferential result belongs here.

---

# 11. Main Table 2 — Harmonic-band compression inference

This is the primary numerical table.

| Harmonic band | Selected radial representation | Effect | Bootstrap 95% CI | \(p_{\mathrm{FWER}}\) | Decision |
|---|---|---:|---:|---:|---|
| \(k=1{:}4\) | DCT, \(B=4\) | 0.059306 | [0.023295, 0.108196] | 0.000200 | Supported |
| \(k=5{:}12\) | RAW, 72 | 0.005984* | [-0.014164, 0.060361] | 0.608939 | Compression not supported |
| \(k=13{:}24\) | RAW, 72 | 0.010959* | [-0.003088, 0.073320] | 0.487751 | Compression not supported |
| \(k=25{:}36\) | db4 wavelet, \(B=4\) | 0.039300 | [0.019130, 0.091021] | 0.019698 | Supported |

\* Effect corresponds to the tested compact candidate; RAW is retained because compression was not supported.

That footnote is essential.

Without it, the table could incorrectly imply that the reported effect belongs to RAW.

---

# 12. Main Table 3 — Optional latent-model comparison

Table 3 should appear in the main manuscript only if Figure 3 cannot communicate the model comparison adequately.

Otherwise:

\[
\boxed{
\text{MOVE TABLE 3 TO SUPPLEMENT}
}
\]

The paper should not become a latent-model benchmark paper.

---

# 13. Supplementary figures

Suggested supplementary figure architecture:

## Figure S1

Identity reconstruction and grouped-fold audit.

## Figure S2

Complete candidate radial-representation grid.

## Figure S3

Full bootstrap distributions.

## Figure S4

Permutation/max-statistic null distributions.

## Figure S5

Sensitivity across radial coefficient counts.

## Figure S6

Exact real/complex packing audit.

## Figure S7

Complete latent-model validation.

## Figure S8

Repeated grouped-CV sensitivity.

## Figure S9

Isomap geometry details.

## Figure S10

Principal-curve stability.

## Figure S11

Diffusion-map audit.

## Figure S12

All 64 PCA radial-harmonic energy maps.

## Figure S13

PC-specific harmonic localization.

## Figure S14

PC-specific radial localization.

The exact number may be reduced during journal formatting.

---

# 14. Supplementary tables

## Table S1

Dataset identity structure.

## Table S2

Fold-by-fold garment-identity counts.

## Table S3

Complete radial compression candidates.

## Table S4

Bootstrap statistics.

## Table S5

FWER-controlled permutation results.

## Table S6

Frozen representation block dimensions.

## Table S7

Latent-model hyperparameters.

## Table S8

Complete latent-model performance.

## Table S9

Geometry-audit statistics.

## Table S10

PC-specific radial/harmonic localization.

---

# 15. Figure evidence classes

Every figure must declare its evidence type internally during manuscript development.

| Figure | Evidence class |
|---|---|
| Figure 1 | M — mathematical / construction |
| Figure 2 | I — inferential |
| Figure 3 | I + D/Q — inferential + geometric qualification |
| Figure 4 | M + D — construction + descriptive |

This prevents descriptive figures from accidentally acquiring inferential language.

---

# 16. Figure prominence

Recommended manuscript visual prominence:

\[
\boxed{
F2 > F4 > F1 > F3
}
\]

where:

### Figure 2

carries the primary contribution.

### Figure 4

shows scientific interpretability.

### Figure 1

teaches the representation.

### Figure 3

defends the latent-model choice.

Figure 3 should not visually dominate Figures 2 or 4.

---

# 17. Main-text versus supplement rule

A result stays in the main paper only if it directly answers:

\[
RQ1,\ RQ2,\ RQ3,\ \text{or }RQ4.
\]

Otherwise:

\[
\boxed{
\text{SUPPLEMENT}
}
\]

Examples:

### Main text

- primary compression inference;
- frozen hybrid representation;
- PCA/nonlinear conclusion;
- retained morphology localization.

### Supplement

- every Isomap neighborhood setting;
- every principal-curve initialization;
- every diffusion-map parameter;
- all 64 PC maps;
- full permutation diagnostics;
- packing-lineage debugging.

---

# 18. Visual overclaim guards

## Never depict discarded coefficients as

- noise;
- irrelevant;
- error;
- nuisance.

Use:

> coefficients not retained under the evidence-supported compact representation.

---

## Never label outer radial zone as

- contour;
- boundary;
- silhouette;
- hem;
- sleeve;
- garment edge.

Use:

> outer radial zone.

---

## Never label PCA components as

- sleeve PC;
- waist PC;
- silhouette PC;
- style PC.

Unless independently annotated and validated.

Use:

> PC1, PC2, etc.

---

## Never visually present PCA as

\[
\text{linear truth}.
\]

It is:

> the validated practical latent baseline.

---

# 19. Figure reproducibility rule

Every quantitative figure must be generated directly from frozen machine-readable result objects.

No value should be manually typed into plotting code when the corresponding frozen object exists.

Required provenance:

\[
\text{frozen object}
\rightarrow
\text{figure dataframe}
\rightarrow
\text{plot}
\rightarrow
\text{export}.
\]

Each figure-generation cell/script should print:

- source object names;
- source dimensions;
- numerical values plotted;
- output filename;
- checksum if practical.

---

# 20. Export contract

Final figures should be exported in publication-ready formats.

Preferred:

- PDF or SVG for vector plots;
- high-resolution PNG only where raster content is required.

Keep text editable wherever possible.

Each final figure should have a deterministic filename:

```text
Fig01_Representation
Fig02_Compression_Inference
Fig03_Latent_Validation
Fig04_Morphology_Localization