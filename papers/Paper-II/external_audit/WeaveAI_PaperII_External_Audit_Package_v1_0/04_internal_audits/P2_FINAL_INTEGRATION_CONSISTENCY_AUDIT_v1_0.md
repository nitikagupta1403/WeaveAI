# Paper II Final Integration Consistency Audit v1.0

**Scope:** freeze-ready P2_08 through P2_12  
**Freeze commit:** `6cab3daebf0ce56b93c3ab221c9d4a7b4bf23981`

## Overall decision

\[
\boxed{\text{PASS WITH FOUR INTEGRATION CLEANUPS BEFORE ASSEMBLY}}
\]

The five frozen manuscript-facing sections are scientifically aligned. No contradiction was found in the governing hierarchy:

\[
\text{representation validity}
\rightarrow
\text{representation allocation}
\rightarrow
\text{latent interpretation}.
\]

The historical raster-relative selection remains frozen; the object-relative construction remains a matched control; 05J remains associational; 05K remains the controlled intervention.

The remaining issues are editorial/integration issues rather than new scientific problems.

---

## Cleanup 1 — unify paper naming

Across the files, the title line alternates between `Paper 2` and `Paper II`.

### Action

Use **Paper II** consistently in the assembled manuscript and keep `P2_08`–`P2_12` only as internal governance filenames.

---

## Cleanup 2 — remove internal freeze/governance language from submission-facing prose

The freeze-ready source files intentionally contain internal phrases such as:

- “historical”
- “frozen”
- “freeze-ready”
- “reconciled with P2_13”
- “05F–05K”
- “P2_13”
- “historical hybrid”

These are appropriate in governance artifacts but not all belong in the journal manuscript.

### Action

During assembly, preserve the scientific chronology but convert internal labels to manuscript-facing language.

Example:

> “The representation-selection analysis had already been frozen under the historical raster-relative coordinate system”

should become manuscript-facing prose such as:

> “The representation-selection analysis was conducted under the raster-relative coordinate system before the subsequent support-dependence audit.”

Do not remove chronology; remove internal project language.

---

## Cleanup 3 — harmonize object-relative terminology

The same control is described as:

- “matched object-relative construction”
- “object-relative comparator”
- “object-relative control”
- “matched counterfactual”

These are scientifically compatible, but a paper should use one dominant term.

### Recommended manuscript term

> **matched object-relative control**

First use:

> “a matched object-relative control”

Later uses:

> “the object-relative control”

Avoid switching between “comparator,” “construction,” and “counterfactual” unless the distinction is needed.

---

## Cleanup 4 — figure/table numbering must be rebuilt only after final assembly

The source sections contain figure/table references inherited from the pre-reconciliation manuscript. Because the Results now begins with the 05F–05K validity audit, previous figure/table numbering is no longer guaranteed to be correct.

### Action

Do **not** manually patch individual figure/table numbers now.

After Methods–Results–Discussion–Introduction are assembled into one manuscript:

1. create the final figure order;
2. create the final table order;
3. renumber all in-text references once;
4. verify every referenced figure/table exists exactly once.

This is the main mechanical task still open.

---

# Cross-section consistency checks

## Methods ↔ Results

PASS.

Methods defines the representation-validity audit before the historical band-selection procedure; Results reports the same order.

The inferential families remain separate:

- 05K exact \(2^{23}\) category-level max-\(T\);
- original band-selection multiplicity-controlled inference;
- latent-model fold-level exact sign-flip sensitivity.

No inferential family is substituted for another.

## Results ↔ Discussion

PASS.

Discussion does not strengthen 05J beyond association and does not turn 05K into a complete preprocessing mechanism.

The Results distinction between broad endpoint concordance and non-universal per-image monotonicity is preserved in Discussion.

## Discussion ↔ Introduction / Related Work

PASS.

The Discussion claim:

> normalization mathematics is prior art; the controlled audit design is the contribution

matches the Related Work novelty boundary.

The object-relative control is not presented as a new normalization invention.

## Introduction ↔ Abstract

PASS.

Both use the same manuscript hierarchy:

1. audit the measurement frame;
2. allocate representation complexity with evidence;
3. retain mathematical traceability.

The Abstract does not claim absolute literature priority.

## Historical hybrid consistency

PASS.

Across the scientific sections, the historical hybrid remains:

\[
\mathrm{DCT}_4/
\mathrm{RAW}_{72}/
\mathrm{RAW}_{72}/
\mathrm{db4}_4.
\]

No section claims that the hybrid was reselected under object-relative coordinates.

## Whole-representation baseline boundary

PASS.

The manuscript preserves the important reviewer-facing fact that uniform RAW42 is very close in MRR to the hybrid.

The contribution is not framed as retrieval-score superiority.

## Latent-model boundary

PASS.

AE/VAE non-superiority is not equated with linear geometry.

The supported quadratic relation is not used to retrospectively select a nonlinear encoder.

## Morphology-localization boundary

PASS.

The 44.65% PCA-64 denominator is preserved.

Radial zones and harmonic bands remain mathematical coordinates, not semantic garment parts.

---

# Recommended manuscript-facing terminology lock

Use the following phrases consistently in the assembled paper:

| Concept | Preferred manuscript term |
|---|---|
| historical measurement system | raster-relative radial-angular representation |
| 05K comparator | matched object-relative control |
| support effect | raster-support dependence |
| 05J evidence | population association |
| 05K evidence | controlled same-pixel support intervention |
| original hybrid | evidence-controlled heterogeneous radial-spectral representation |
| latent inverse | exact radial-harmonic traceability |
| negative compression result | compression not supported under the tested design |

Avoid manuscript-facing use of internal labels `05F`, `05G`, `05J`, `05K`, `P2_13`, `freeze-ready`, and Git/repository terminology except in supplementary provenance material.

---

# Final assembly order

Recommended journal order:

\[
\boxed{
\text{Title}
\rightarrow
\text{Abstract}
\rightarrow
\text{Introduction}
\rightarrow
\text{Related Work}
\rightarrow
\text{Methods}
\rightarrow
\text{Results}
\rightarrow
\text{Discussion}
}
\]

The scientific logic inside that conventional article order should remain:

\[
\boxed{
\text{representation validity}
\rightarrow
\text{representation selection}
\rightarrow
\text{latent validation}
\rightarrow
\text{traceable morphology interpretation}.
}
\]

---

# Final decision

\[
\boxed{
\text{NO SCIENTIFIC CONTRADICTION FOUND ACROSS P2\_08–P2\_12}
}
\]

The remaining work is manuscript assembly, terminology normalization, and final figure/table/reference reconciliation.

No new experiment is required before that step.
