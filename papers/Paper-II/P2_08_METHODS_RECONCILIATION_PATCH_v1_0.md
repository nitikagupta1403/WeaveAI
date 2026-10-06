# CLO-SKET Paper II — P2_08 Methods Reconciliation Patch v1.0

**Status:** REVIEW PATCH — do not overwrite the historical `P2_08_METHODS_FINAL.md` until accepted.

**Basis:** current `P2_08_METHODS_FINAL.md` on branch `paper-ii-05k-support-audit` plus frozen `P2_13_05K_SUPPORT_DEPENDENCE_AND_CLAIM_RECONCILIATION_v1_0.md`.

**Purpose:** integrate the 05F–05K representation-validity audit into Methods without changing the frozen representation-selection, latent-model, or morphology-analysis procedures.

---

# 1. Governance rule

The 05F–05K audit was completed **after** the original representation-selection analysis and did not feed back into the frozen band selections.

For scientific exposition it should appear before representation selection because it evaluates the measurement system itself, but the Methods must state the chronology explicitly:

> The representation-validity audit reported below was performed after the original radial-representation selection had been frozen. It did not reopen candidate selection, alter harmonic-band boundaries, modify coefficient budgets, or change any downstream latent-model decision. It is presented before the representation-selection procedure because its purpose is to characterize the measurement behavior of the historical radial-angular coordinate system.

This sentence is mandatory.

---

# 2. Keep Sections 3.1–3.3, with one framing addition

The current Sections 3.1–3.3 should remain substantively unchanged.

The existing coordinate-normalization wording is important and should be preserved:

> `R_max` is the maximum centroid-relative radius over the **complete image grid**, not the farthest nonzero-ink pixel.

This is the historical raster-relative normalization whose support dependence is audited.

Immediately after the last paragraph of current Section 3.3, insert:

> Because this radial normalization is defined over the complete raster grid, its behavior under changes in surrounding image support was examined explicitly in a separate representation-validity audit. That audit is described next. The audit was conducted after the original representation-selection analysis had been frozen and did not alter the representation-selection procedure or its outcomes.

---

# 3. Insert new Section 3.4 — Representation-validity audit

## 3.4 Representation-validity audit of preprocessing and raster support

A separate post-selection audit examined whether the historical raster-relative radial-angular representation was sensitive to preprocessing changes that altered the observation frame. The audit was performed after the original band-wise representation-selection analysis had been frozen and did not reopen harmonic-band definitions, candidate families, coefficient budgets, training-fold selections, or held-out inferential decisions. It is presented here before representation selection because it evaluates the behavior of the measurement coordinate system itself.

The audit proceeded in four stages:

\[
05F
\rightarrow
05G
\rightarrow
05J
\rightarrow
05K.
\]

The stages served distinct purposes: preprocessing localization, candidate descriptor analysis, population association, and controlled same-pixel intervention.

### 3.4.1 Preprocessing localization (05F)

The historical RAW-to-CLEAN preprocessing chain was decomposed into controlled intermediate variants to localize where the previously observed spectral change entered.

The principal variants were:

- **TEXT_ONLY**: preserve the original raster geometry while blanking the frozen text boxes;
- **CROP_ONLY**: apply the frozen garment crop after grayscale/polarity handling, with no resize or padding;
- **LOCALIZE_ONLY**: apply the frozen localization pipeline including resize/pad but without text whitening;
- **CLEAN**: apply the complete historical cleaning pipeline.

The comparison was used only to localize the preprocessing stage at which spectral allocation changed. It was not used to reselect the radial representation or harmonic bands.

The crop-only construction preserved the pixel values of the frozen garment rectangle. Polarity handling was applied before cropping, matching the historical lineage.

### 3.4.2 Frame, centroid, and support descriptors (05G)

To distinguish candidate explanations for the RAW-to-CROP change, image-level descriptors were computed for the matched RAW and CROP_ONLY representations.

Integrity checks required:

\[
\texttt{raw\_garment\_array}
=
\texttt{crop\_array}
\]

exactly for the retained garment rectangle, zero centroid map-back error, and unchanged retained intensities.

Candidate descriptors included raster-relative support measures, crop-area measures, foreground fractions, radial extent relative to the raster grid, and border/gradient summaries.

The 05G analysis was associational. Descriptor association with spectral change was not treated as evidence that the descriptor was itself the causal mechanism.

### 3.4.3 Population support–spectral association audit (05J)

The population audit tested whether RAW-to-CROP changes in raster-relative support geometry were associated with changes in the four frozen angular-frequency band fractions.

Stable image provenance was joined using:

\[
\texttt{row\_index}
+
\texttt{relative\_path}
+
\texttt{category},
\]

rather than fold identifier, because the historical fold labels used by the relevant source tables were not fully aligned.

The primary support descriptor was the change in robust foreground radial extent relative to raster support,

\[
\Delta
\left(
\frac{r_{q99}}{R_{\mathrm{grid}}}
\right),
\]

with additional support and occupancy descriptors retained as secondary candidates.

Associations were evaluated with category-preserving permutation procedures using 10,000 permutations. False-discovery-rate control was applied across the prespecified association family. The analysis was explicitly interpreted as observational:

\[
\boxed{
\text{association}
\neq
\text{causation}.
}
\]

No 05J result was used to modify the frozen representation-selection decisions.

### 3.4.4 Controlled same-pixel raster-support intervention (05K)

The 05K intervention tested whether changing only the surrounding raster support altered spectral allocation when the garment pixel rectangle itself was unchanged.

For an original raster of height \(H\) and width \(W\), support scale levels were

\[
s\in
\{1.00,1.10,1.25,1.50,2.00,2.50,3.00\}.
\]

The enlarged dimensions were defined deterministically as

\[
H_s
=
H
+
2
\left\lceil
\frac{(s-1)H}{2}
\right\rceil,
\]

\[
W_s
=
W
+
2
\left\lceil
\frac{(s-1)W}{2}
\right\rceil.
\]

The complete frozen CROP_ONLY rectangle was copied into the enlarged raster using symmetric integer padding. The per-sketch background fill followed the frozen border-median rule used by the 05K materializer.

The intervention prohibited:

- garment resizing;
- interpolation;
- antialiasing;
- contour retracing;
- crop recomputation;
- rethresholding;
- square forcing;
- post-padding resizing.

Thus the treatment variable was surrounding raster support rather than garment geometry.

The support audit followed a frozen execution hierarchy:

\[
10\ \text{sentinels}
\rightarrow
230\ \text{calibration sketches}
\rightarrow
2300\ \text{primary sketches}.
\]

The sentinel stage was used for QA and visualization only. The calibration set contained one deterministic canonical sketch per garment identity. The primary analysis comprised all 2,300 sketches at all seven support levels.

Before the primary population analysis, the endpoint directional predictions were frozen:

\[
\Delta\text{low}>0,
\]

\[
\Delta\text{high-mid}<0,
\]

\[
\Delta\text{high}<0
\]

for support enlargement from \(s=1\) to \(s=3\). No primary directional claim was assigned to the mid band.

### 3.4.5 Matched object-relative control

A matched object-relative radial-angular field was computed from the same garment pixels using coordinates centered on the foreground and normalized by foreground-defined radial extent rather than complete raster-grid extent.

Its role was a matched control, not a newly proposed descriptor family.

For the same-pixel support intervention, the object-relative construction was required to remain invariant within numerical precision across support levels.

The historical raster-relative representation and the object-relative control were therefore evaluated under the same support manipulations.

### 3.4.6 Primary 05K inference

The primary endpoint was the category-level band-fraction change between:

\[
s=3
\quad\text{and}\quad
s=1.
\]

Inference was performed across the 23 garment categories.

All:

\[
2^{23}
\]

category sign assignments were enumerated exactly. The same category sign was applied jointly across the prespecified directional bands, preserving their within-category dependence.

A studentized maximum-\(T\) statistic was used to control family-wise error across the three directional endpoints:

- low;
- high-middle;
- high.

The 05K inference therefore asked whether the predeclared endpoint directions were supported at category level under the controlled support manipulation.

Per-image endpoint concordance and full seven-level monotonicity were retained as descriptive quantities and were not substituted for the category-level inferential endpoint.

### 3.4.7 Separation from the frozen representation-selection analysis

The support audit was a later representation-validity analysis.

It did **not**:

- alter the four harmonic bands;
- change the radial coefficient-budget grid;
- change the \(Q_c\ge0.95\) training admissibility rule;
- change the held-out \(S_g\) statistic;
- change the FWER-controlled band-selection inference;
- change the frozen hybrid descriptor;
- reopen PCA/AE/VAE model selection.

Accordingly, the original representation-selection results remain conditional on the historical raster-relative measurement system in which they were obtained.

---

# 4. Renumber the existing Methods sections after insertion

After inserting new Section 3.4, increment the old numbering by one:

- old 3.4 → new 3.5
- old 3.5 → new 3.6
- old 3.6 → new 3.7
- old 3.6.1 → new 3.7.1
- old 3.7 → new 3.8
- old 3.8 → new 3.9
- old 3.9 → new 3.10
- old 3.10 → new 3.11
- old 3.10.1 → new 3.11.1
- old 3.11 → new 3.12
- old 3.12 → new 3.13
- old 3.13 → new 3.14
- old 3.13.1–3.13.5 → new 3.14.1–3.14.5
- old 3.14 → new 3.15
- old 3.15 → new 3.16
- old 3.16 → new 3.17
- old 3.17 → new 3.18

Update all internal cross-references accordingly.

No scientific content in those sections should be changed except for the retrieval wording correction below and any references made necessary by renumbering.

---

# 5. Mandatory retrieval-wording correction

The current text in the old Section 3.6.1 states:

> “In CLO-SKET this yielded ten candidate garment identities per query.”

That wording is not correct for the frozen fold-based evaluation because each outer fold contains:

\[
8
\]

training identities per category and:

\[
2
\]

held-out identities per category.

Replace the opening paragraph of the renumbered Section 3.7.1 with:

> Category-restricted garment-identity prototype retrieval was used as an evaluation procedure, not as a learned classifier. For a query sketch \(q\) belonging to category \(c_q\), the candidate gallery consisted only of garment identities from the relevant evaluation partition within that category. Under the frozen five-fold identity split, each category contributed eight training identities and two held-out identities per fold. Training-only candidate screening therefore operated within the eight training identities per category, whereas outer held-out evaluation operated within the two test identities per category. No identity from the opposite partition entered the corresponding prototype gallery.

This preserves the actual fold package and removes the misleading “ten candidate identities per query” statement.

---

# 6. Preserve the representation-selection wording

The existing band-selection procedure should remain unchanged.

In particular, preserve:

\[
K_1=1{:}4,\quad
K_2=5{:}12,\quad
K_3=13{:}24,\quad
K_4=25{:}36
\]

and:

\[
B\in\{4,8,12,18,24,36,48,72\}.
\]

Preserve the training-only admissibility rule:

\[
Q_c
=
\frac{
\operatorname{MRR}_{c,\mathrm{train}}
}{
\operatorname{MRR}_{\mathrm{full},\mathrm{train}}
}
\ge0.95.
\]

Preserve the distinction that \(0.95\) is a design/admissibility threshold, not a calibrated non-inferiority margin.

Preserve the held-out category-controlled garment effect:

\[
S_g
=
\frac{B_g-W_g}{B_g}.
\]

Preserve the original category-cluster sign-flip FWER procedure used for band-selection inference.

The 05K exact \(2^{23}\) sign-flip analysis must **not** be substituted for the original representation-selection inference. They answer different questions.

---

# 7. Preserve post-selection sensitivity boundaries

The following existing analyses remain explicitly post-selection and should not be folded into primary representation selection:

- occupancy augmentation;
- radial-mass augmentation;
- whole-descriptor uniform-baseline sensitivity;
- latent PCA/AE/VAE comparisons;
- nonlinear predictive-structure characterization;
- neighborhood dimensionality diagnostic.

Where useful, add the sentence:

> This analysis did not reopen the previously frozen harmonic-band or radial-representation selections.

Do not convert these analyses into retrospective model selection.

---

# 8. Status line amendment

Replace the current status line:

> **FINAL METHODS ASSEMBLY: EVIDENCE-CONTROLLED REPRESENTATION + REPRODUCIBILITY LOCKED**

with:

> **METHODS RECONCILED WITH P2_13 v1.0: REPRESENTATION VALIDITY + EVIDENCE-CONTROLLED REPRESENTATION + REPRODUCIBILITY LOCKED**

Then retain:

> This Methods section is assembled from frozen mathematical and computational contracts. No new analysis is introduced here.

Add:

> The 05F–05K audit is reported as a later representation-validity analysis and did not alter the historical band-selection or latent-analysis decisions.

---

# 9. Scientific-order lock

The final Methods logic should read:

\[
\boxed{
\text{dataset}
\rightarrow
\text{radial-angular measurement}
\rightarrow
\text{measurement-validity audit}
\rightarrow
\text{evidence-controlled representation selection}
\rightarrow
\text{frozen hybrid}
\rightarrow
\text{latent validation}
\rightarrow
\text{latent interpretation}
}
\]

This is a narrative reordering for scientific clarity.

It must not be written in a way that implies the 05K audit prospectively determined the historical representation-selection procedure.

---

# 10. Claim-boundary checklist for P2_08

Before freezing the reconciled Methods, verify all of the following:

- [ ] Historical radius normalization is explicitly defined by the complete raster grid.
- [ ] Object-relative control is described as a control, not as a new method claim.
- [ ] 05F localizes the preprocessing effect; it does not establish cause.
- [ ] 05G/05J remain associational.
- [ ] 05K is described as a controlled same-pixel support intervention.
- [ ] No resize/interpolation is attributed to 05K.
- [ ] Endpoint predictions are identified as frozen before the primary population analysis.
- [ ] Sentinel/calibration/primary hierarchy is explicit.
- [ ] Primary 05K inference is category-level exact \(2^{23}\) joint sign-flip max-\(T\).
- [ ] Individual monotonicity is descriptive, not a primary inferential requirement.
- [ ] 05K did not reopen band selection.
- [ ] Retrieval gallery wording reflects 8 train / 2 held-out identities per category per fold.
- [ ] Sensitivity analyses remain sensitivity analyses.
- [ ] No “new Fourier transform,” “new normalization,” or “universally invariant representation” language appears.
- [ ] No historical provenance notebook or hash-locked artifact is rewritten.

---

# 11. Freeze recommendation

Do not overwrite the existing `P2_08_METHODS_FINAL.md` yet.

Create the reconciled candidate as:

`P2_08_METHODS_RECONCILED_v1_0.md`

Audit it against:

1. `P2_02_EVIDENCE_LEDGER.md`;
2. `P2_13_05K_SUPPORT_DEPENDENCE_AND_CLAIM_RECONCILIATION_v1_0.md`;
3. the frozen 05K D1/D2/D3 evidence chain;
4. the reproducibility/provenance boundary.

Only after that cross-check should it replace or supersede the earlier Methods assembly.
