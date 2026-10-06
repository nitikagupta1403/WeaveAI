# P2_08 Methods Three-Way Audit v1.0

**Audited file:** `P2_08_METHODS_RECONCILED_v1_0.md`

**Against:**
1. `P2_02_EVIDENCE_LEDGER.md`
2. `P2_13_05K_SUPPORT_DEPENDENCE_AND_CLAIM_RECONCILIATION_v1_0.md`
3. frozen 05K D1/D2/D3 evidence/claim boundaries already incorporated into P2_13

## Overall decision

\[
\boxed{\text{PASS WITH TWO REQUIRED EDITS}}
\]

No frozen numerical result or model-selection decision was contradicted. The reconciled Methods preserve the historical raster-relative normalization, the band-selection procedure, the latent-analysis boundary, and the 05K post-selection chronology.

Two edits are required before freeze.

---

## Required edit 1 — 05J q99 wording

Current wording in Section 3.4.3 calls

\[
\Delta(r_{q99}/R_{\mathrm{grid}})
\]

the **“principal support descriptor.”**

That is too strong because the 05J evidence establishes it as the **strongest observed descriptor among the audited support measures**, not as a prospectively designated primary endpoint.

### Replace with

> Among the audited support descriptors, the strongest population associations involved change in robust foreground radial extent relative to raster support,

followed by the same equation.

### Reason

This preserves the D1/D2/D3 boundary:

\[
05J=\text{association}
\]

and avoids retrospectively promoting an observed strongest descriptor into a prespecified primary variable.

---

## Required edit 2 — move the post hoc occupancy/radial-mass sensitivity

Current Section 3.3.1 is explicitly a **post hoc sensitivity analysis**, but it appears before the representation-validity audit and before the original representation-selection procedure.

That ordering weakens the new manuscript logic:

\[
\text{measurement}
\rightarrow
\text{validity audit}
\rightarrow
\text{selection}
\rightarrow
\text{sensitivity}
\rightarrow
\text{latent analysis}.
\]

### Required action

Move the existing occupancy/radial-mass completeness sensitivity unchanged to a new subsection:

`3.11.2 Occupancy and radial-mass completeness sensitivity`

immediately after the whole-representation baseline sensitivity.

No scientific wording inside the sensitivity analysis needs to change except internal section-number references if required.

---

## Cross-checks that passed

### Historical coordinate normalization

PASS.

The Methods correctly state that historical radial normalization uses the maximum centroid-relative radius over the **complete image grid**, not the farthest nonzero-ink pixel.

This is essential because 05K audits support dependence of that raster-relative coordinate system.

### 05F boundary

PASS.

05F is described as localization of where the preprocessing effect enters, not as a causal-mechanism proof.

### 05G boundary

PASS.

The candidate descriptor audit remains associational.

### 05J boundary

PASS after Required edit 1.

The Methods explicitly retain:

\[
\text{association}\neq\text{causation}.
\]

### 05K intervention

PASS.

The Methods preserve:

- same garment rectangle;
- support-only manipulation;
- no resize;
- no interpolation;
- no antialiasing;
- no contour retracing;
- no crop recomputation;
- no rethresholding;
- no post-padding resize.

### 05K directional predictions

PASS.

The predeclared directions are correctly stated as:

\[
\Delta\text{low}>0,
\qquad
\Delta\text{high-mid}<0,
\qquad
\Delta\text{high}<0.
\]

No primary directional claim is assigned to the mid band.

### 05K execution hierarchy

PASS.

The Methods preserve:

\[
10\text{ sentinels}
\rightarrow
230\text{ calibration sketches}
\rightarrow
2300\text{ primary sketches}.
\]

### 05K inference

PASS.

The Methods correctly state:

- 23 category effects;
- endpoint \(s=3\) versus \(s=1\);
- exact \(2^{23}\) category sign assignments;
- joint signs across the three directional bands;
- studentized max-\(T\) FWER control.

### Object-relative comparator

PASS.

It is described as a matched control rather than a novel descriptor claim.

### Chronology / anti-retroactive-selection boundary

PASS.

The Methods explicitly state that 05F–05K were later audits and did not alter:

- harmonic bands;
- coefficient budgets;
- \(Q_c\ge0.95\);
- \(S_g\);
- band-selection inference;
- frozen hybrid;
- PCA/AE/VAE selection.

### Frozen hybrid

PASS.

The representation remains:

\[
\mathrm{DCT}_4/
\mathrm{RAW}_{72}/
\mathrm{RAW}_{72}/
\mathrm{db4}_4.
\]

### Negative inferential boundaries

PASS.

The Methods do not equate non-support for compression with incompressibility and do not equate failure of AE/VAE superiority with linear geometry.

### Retrieval wording

PASS.

The earlier misleading “ten candidate garment identities per query” wording has been corrected to the actual frozen partition structure:

\[
8\text{ train identities/category/fold}
\]

and

\[
2\text{ held-out identities/category/fold}.
\]

### Sensitivity analyses

PASS after Required edit 2.

They remain explicitly post-selection and do not reopen the primary representation-selection procedure.

---

## Freeze decision

After the two required edits:

\[
\boxed{\text{P2\_08 METHODS = FREEZE-READY}}
\]

No additional experiment is required for the Methods reconciliation.
