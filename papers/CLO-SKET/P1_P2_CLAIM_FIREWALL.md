# CLO-SKET PAPER 1 ↔ PAPER 2 CLAIM FIREWALL

**File:** `P1_P2_CLAIM_FIREWALL.md`  
**Status:** FROZEN CLAIM-GOVERNANCE DOCUMENT  
**Scope:** CLO-SKET Paper 1 and CLO-SKET Paper 2  
**Purpose:** Prevent scientific claim duplication, contribution ambiguity, salami-slicing concerns, and accidental strengthening of evidence across the two manuscripts.

---

# 1. Purpose

CLO-SKET Paper 1 and Paper 2 are scientifically related studies built from the same underlying garment-sketch dataset and a common radial-angular mathematical substrate.

The purpose of this document is **not** to make the papers appear artificially unrelated.

The purpose is to ensure that:

1. shared mathematical foundations are stated transparently;
2. methodological lineage is clear;
3. each paper owns a distinct scientific question;
4. each primary contribution appears in only one paper;
5. results from one paper are not used to strengthen claims in the other;
6. shared terminology does not create the appearance of duplicate novelty;
7. negative results and inferential boundaries remain attached to the paper that established them;
8. future manuscript edits cannot accidentally collapse the two papers into one apparent contribution.

This file is therefore the authoritative claim firewall for both manuscripts.

---

# 2. Firewall tags

Every potentially overlapping statement should be classified using one of the following tags.

## SAFE SHARED FOUNDATION

Material required to describe the common dataset, mathematical substrate, or validation structure.

It may appear in both papers provided that it is **not independently claimed as novelty in both**.

Examples:

- CLO-SKET dataset structure;
- garment identities;
- radial-angular coordinates;
- shell-conditioned angular distributions;
- shell-wise Fourier transformation;
- garment-identity-disjoint validation.

---

## PAPER-1 ONLY

Scientific questions, methods, results, interpretations, or contributions whose ownership belongs exclusively to Paper 1.

Paper 2 may cite Paper 1 where necessary but must not independently claim these contributions.

---

## PAPER-2 ONLY

Scientific questions, methods, results, interpretations, or contributions whose ownership belongs exclusively to Paper 2.

Paper 1 must not use these results to strengthen or retrospectively motivate its claims.

---

## REWORD

Scientifically legitimate shared material whose current wording creates contribution ambiguity.

The underlying material may remain, but novelty language must be changed.

---

## REMOVE

A statement that would duplicate the other paper's contribution, misrepresent methodological ownership, or create an unsupported cross-paper inference.

Such a statement should not appear in that manuscript.

---

# 3. Scientific identity of the two papers

## 3.1 Paper 1

### Primary scientific question

> What exactly does an explicit second-harmonic radial-angular measurement of a garment sketch contain, how valid is it, and what are its mathematical, numerical, transformation, coordinate, and statistical limits?

### Paper 1 ownership

\[
\boxed{
\text{explicit measurement}
+
F_2\text{ axial geometry}
+
14D
+
\text{rigid-image transformation audit}
+
\text{reconstruction}
+
\text{coordinate dependence}
+
\text{sensitivity}
+
\text{phase conditioning}
}
\]

Paper 1 is fundamentally a **measurement and validation paper**.

Its central object is the explicitly defined second-harmonic radial-angular representation and the examination of its mathematical and inferential properties.

---

## 3.2 Paper 2

### Primary scientific question

> Given the full radial-harmonic field, should radial structure be represented identically at every angular harmonic scale?

### Paper 2 ownership

\[
\boxed{
\text{full harmonic field}
+
\text{bandwise radial representation selection}
+
\text{hybrid compression}
+
\text{latent geometry}
+
\text{spectral localization}
}
\]

Paper 2 is fundamentally a **representation-selection and latent-geometry paper**.

Its central object is not the introduction of radial-angular measurement itself, but the question of how the radial dimension of the full angular-harmonic field should be represented across harmonic scales.

---

# 4. Shared scientific substrate

The following material is explicitly designated:

\[
\boxed{\text{SAFE SHARED FOUNDATION}}
\]

and may appear in both papers.

| Shared element | Status | Rule |
|---|---|---|
| CLO-SKET dataset | SAFE SHARED FOUNDATION | May be described in both |
| 2,300 sketches | SAFE SHARED FOUNDATION | Dataset fact |
| 23 garment categories | SAFE SHARED FOUNDATION | Dataset fact |
| 230 recovered garment identities | SAFE SHARED FOUNDATION | May be used in both |
| repeated sketches per garment identity | SAFE SHARED FOUNDATION | Required dependency structure |
| centroid-relative polar geometry | SAFE SHARED FOUNDATION | Common measurement substrate |
| radial coordinate \(r\) | SAFE SHARED FOUNDATION | Common coordinate |
| angular coordinate \(\theta\) | SAFE SHARED FOUNDATION | Common coordinate |
| radial-angular field | SAFE SHARED FOUNDATION | Common substrate |
| conditional angular distribution \(P(\theta\mid r)\) | SAFE SHARED FOUNDATION | Must not be claimed as independent P2 novelty |
| shell-wise angular Fourier transformation | SAFE SHARED FOUNDATION | Common mathematical operation |
| complex harmonic \(F_k(r)\) | SAFE SHARED FOUNDATION | General notation |
| 72 radial shells | SAFE SHARED FOUNDATION | Shared implementation structure |
| 72 angular bins | SAFE SHARED FOUNDATION | Shared implementation structure |
| garment-identity-disjoint validation principle | SAFE SHARED FOUNDATION | May appear in both |
| category-aware grouped validation | SAFE SHARED FOUNDATION | May appear in both where applicable |
| dependency-aware uncertainty | SAFE SHARED FOUNDATION | Implementation may differ by analysis |

Shared foundation does **not** imply shared novelty.

The papers may use the same substrate while asking different scientific questions.

---

# 5. Ownership matrix

## 5.1 Representation and harmonic analysis

| Claim / method | Paper 1 | Paper 2 | Firewall |
|---|---:|---:|---|
| radial-angular sketch geometry | ✓ | ✓ | SAFE SHARED FOUNDATION |
| \(P(\theta\mid r)\) | ✓ | ✓ | SAFE SHARED FOUNDATION |
| shell-wise Fourier moments | ✓ | ✓ | SAFE SHARED FOUNDATION |
| explicit second-harmonic focus | ✓ | — | PAPER-1 ONLY |
| axial interpretation of \(m=2\) | ✓ | — | PAPER-1 ONLY |
| \(m=2\) as lowest non-zero axial harmonic | ✓ | — | PAPER-1 ONLY |
| \(F_2=C_2-iS_2\) as primary measurement | ✓ | — | PAPER-1 ONLY |
| \(R_2=|F_2|\) as primary magnitude field | ✓ | — | PAPER-1 ONLY |
| axial orientation from \(F_2\) | ✓ | — | PAPER-1 ONLY |
| 14-dimensional explicit representation | ✓ | — | PAPER-1 ONLY |
| eight radial \(F_2\) descriptors | ✓ | — | PAPER-1 ONLY |
| six axial-safe descriptors | ✓ | — | PAPER-1 ONLY |
| full positive harmonic field \(k=1{:}36\) as primary object | — | ✓ | PAPER-2 ONLY |
| harmonic-band partition | — | ✓ | PAPER-2 ONLY |
| band-conditioned radial representation | — | ✓ | PAPER-2 ONLY |

---

## 5.2 Validation and reconstruction

| Claim / method | Paper 1 | Paper 2 | Firewall |
|---|---:|---:|---|
| garment-identity-disjoint validation | ✓ | ✓ | SAFE SHARED FOUNDATION |
| zero identity overlap | ✓ | ✓ | SAFE SHARED FOUNDATION |
| category-balanced grouped validation | ✓ | ✓ | SAFE SHARED FOUNDATION |
| reconstruct \(C_2,S_2\) from \([r,R_2]\) | ✓ | — | PAPER-1 ONLY |
| magnitude-only phase reconstruction experiment | ✓ | — | PAPER-1 ONLY |
| whole-field \(R_2\) reconstruction | ✓ | — | PAPER-1 ONLY |
| peak-shell reconstruction | ✓ | — | PAPER-1 ONLY |
| image-level vs identity-level validation sensitivity | ✓ | — | PAPER-1 ONLY |
| band-specific compression validation | — | ✓ | PAPER-2 ONLY |
| representation-selection inference | — | ✓ | PAPER-2 ONLY |
| FWER-controlled band decisions | — | ✓ | PAPER-2 ONLY |

---

## 5.3 Transformation behavior, coordinate dependence, and robustness

| Claim / method | Paper 1 | Paper 2 | Firewall |
|---|---:|---:|---|
| rigid-image raster rotation control of the final 14-D representation | ✓ | — | PAPER-1 ONLY |
| empirical invariance of radial-magnitude quantities over tested rigid rotations | ✓ | — | PAPER-1 ONLY |
| \(R(2\phi)\) equivariance of doubled-angle axial orientation pairs | ✓ | — | PAPER-1 ONLY |
| invariant-scalar treatment of axial coherence and orientation drift | ✓ | — | PAPER-1 ONLY |
| rigid-image rotation numerical perturbation / interpolation effects | ✓ | — | PAPER-1 ONLY |
| global analytic rotation control | ✓ | — | PAPER-1 ONLY |
| identity-randomized rotation | ✓ | — | PAPER-1 ONLY |
| canonical image-frame dependence | ✓ | — | PAPER-1 ONLY |
| \(C_2/S_2\) error coordinate dependence | ✓ | — | PAPER-1 ONLY |
| descriptor threshold sensitivity | ✓ | — | PAPER-1 ONLY |
| concentration-width sensitivity | ✓ | — | PAPER-1 ONLY |
| angular-resolution sensitivity | ✓ | — | PAPER-1 ONLY |
| radial-resolution sensitivity | ✓ | — | PAPER-1 ONLY |
| radial-domain sensitivity | ✓ | — | PAPER-1 ONLY |
| peak-radius boundary sensitivity | ✓ | — | PAPER-1 ONLY |

**Interpretation lock:** the rigid-image raster control and the analytic/randomized rotation controls answer different questions and must not be collapsed into one generic “rotation robustness” claim. The rigid-image control evaluates the transformation behavior of the final 14-D representation under the tested image-domain perturbations. The analytic and garment-identity-randomized controls evaluate coordinate-frame dependence of the reconstruction experiment.

---

## 5.4 Phase-error geometry

| Claim / method | Paper 1 | Paper 2 | Firewall |
|---|---:|---:|---|
| perturbation equation for axial phase | ✓ | — | PAPER-1 ONLY |
| \(1/(2R_2)\) phase conditioning | ✓ | — | PAPER-1 ONLY |
| \(R_2\)-error association | ✓ | — | PAPER-1 ONLY |
| Cartesian perturbation association | ✓ | — | PAPER-1 ONLY |
| combined conditioning quantity | ✓ | — | PAPER-1 ONLY |
| garment-level phase-error association | ✓ | — | PAPER-1 ONLY |

---

## 5.5 Compression and hybrid representation

| Claim / method | Paper 1 | Paper 2 | Firewall |
|---|---:|---:|---|
| test radial compression by harmonic band | — | ✓ | PAPER-2 ONLY |
| DCT candidate representation | — | ✓ | PAPER-2 ONLY |
| wavelet candidate representation | — | ✓ | PAPER-2 ONLY |
| RAW radial preservation | — | ✓ | PAPER-2 ONLY |
| \(k=1{:}4\rightarrow DCT_4\) | — | ✓ | PAPER-2 ONLY |
| \(k=5{:}12\rightarrow RAW_{72}\) | — | ✓ | PAPER-2 ONLY |
| \(k=13{:}24\rightarrow RAW_{72}\) | — | ✓ | PAPER-2 ONLY |
| \(k=25{:}36\rightarrow db4_4\) | — | ✓ | PAPER-2 ONLY |
| 2592 → 1504 complex coefficients | — | ✓ | PAPER-2 ONLY |
| 41.98% coefficient reduction | — | ✓ | PAPER-2 ONLY |
| 3008-dimensional real packing | — | ✓ | PAPER-2 ONLY |

---

## 5.6 Latent representation and geometry

| Claim / method | Paper 1 | Paper 2 | Firewall |
|---|---:|---:|---|
| PCA representation | — | ✓ | PAPER-2 ONLY |
| PCA-64 | — | ✓ | PAPER-2 ONLY |
| nonlinear latent-model comparison | — | ✓ | PAPER-2 ONLY |
| Isomap geometry | — | ✓ | PAPER-2 ONLY |
| principal curves | — | ✓ | PAPER-2 ONLY |
| diffusion-map sensitivity | — | ✓ | PAPER-2 ONLY |
| inverse PCA perturbation mapping | — | ✓ | PAPER-2 ONLY |
| \(\Delta F_j(r,k)\) | — | ✓ | PAPER-2 ONLY |
| sign-invariant morphology energy | — | ✓ | PAPER-2 ONLY |
| radial-harmonic latent localization | — | ✓ | PAPER-2 ONLY |

---

# 6. Numerical-result ownership

## 6.1 PAPER-1 ONLY numerical results

The following numbers belong exclusively to Paper 1's evidentiary chain.

Examples include:

\[
R_2\text{ whole-field RMSE}=0.145610
\]

\[
R_2\text{ whole-field Pearson }r=0.926390
\]

\[
R_2\text{ peak-shell RMSE}=0.148303
\]

\[
R_2\text{ peak-shell Pearson }r=0.810543
\]

\[
\text{median peak-shell axial error}=4.104^\circ
\]

and

\[
\text{identity-randomized median axial error}=44.675^\circ.
\]

Paper 1 also exclusively owns the rigid-image rotation-control results over \(\pm5^\circ\), \(\pm10^\circ\), and \(\pm20^\circ\), including the observed radial-magnitude perturbations, the decoded axial shifts, the \(R(2\phi)\) transformation audit, and the reported upper-tail equivariance errors (including the approximately \(4.87^\circ\) peak-orientation and \(0.85^\circ\) magnitude-weighted-orientation maxima across the tested conditions).

Paper 1 also exclusively owns numerical findings concerning:

- descriptor robustness;
- radial-domain boundary occupancy;
- peak-radius sensitivity;
- harmonic-order controls;
- garment-level axial-error associations;
- Cartesian perturbation associations;
- phase-conditioning associations.

These values must not be imported into Paper 2 to strengthen its representation-selection argument.

---

## 6.2 PAPER-2 ONLY numerical results

Paper 2 exclusively owns the band-specific representation-selection results, including the inferential decisions for:

\[
k=1{:}4,
\]

\[
k=5{:}12,
\]

\[
k=13{:}24,
\]

and

\[
k=25{:}36.
\]

Paper 2 also exclusively owns:

\[
2592\rightarrow1504
\]

complex coefficients,

\[
41.98\%
\]

coefficient reduction,

\[
3008
\]

real dimensions,

\[
PCA_{64}=44.65\%
\]

of standardized representation variance,

and retained-subspace localization results including:

\[
78.54\%
\]

intermediate-harmonic mapped morphology energy,

\[
66.84\%
\]

outer-radial mapped morphology energy,

and

\[
51.30\%
\]

joint outer-radial × intermediate-harmonic localization.

These values must not be imported into Paper 1 as retrospective justification for the 14-dimensional \(F_2\) representation.

---

# 7. Prohibited cross-paper claims

The following statements are prohibited.

---

## 7.1 Prohibited in Paper 2

Paper 2 must **not** claim:

> We introduce a radial-angular representation of garment sketches.

**Reason:** Paper 1 owns the explicit radial-angular measurement contribution.

---

Paper 2 must **not** claim:

> We introduce the conditional angular representation \(P(\theta\mid r)\).

**Reason:** This is shared substrate whose methodological ownership is already established in Paper 1.

---

Paper 2 must **not** claim:

> We introduce Fourier analysis of radial-angular garment morphology.

**Reason:** Too broad and overlaps directly with Paper 1.

---

Paper 2 must **not** claim:

> We establish the second harmonic as the appropriate representation of garment orientation.

**Reason:** PAPER-1 ONLY.

---

Paper 2 must **not** independently claim that the 14-dimensional Paper-1 representation is invariant/equivariant under rigid image rotation, or reproduce the \(R(2\phi)\) audit or its numerical transformation-error results as Paper-2 evidence.

If transformation behavior must be mentioned for lineage, Paper 2 should cite Paper 1 and state it only as prior validation of the shared measurement lineage.

---

Paper 2 must **not** claim:

> The radial-angular representation is robust to coordinate transformation or numerical perturbation.

unless the statement explicitly cites Paper 1 and is clearly background rather than a Paper 2 result. Even with citation, avoid broad “robust” wording: Paper 1 supports transformation behavior only over the tested rigid rotations and explicitly does not establish arbitrary transformation robustness.

---

Paper 2 must **not** use Paper 1's strong \(F_2\) reconstruction performance as evidence that its hybrid representation is valid.

The two analyses answer different questions.

---

Paper 2 must **not** imply:

\[
\text{P1 reconstruction success}
\Rightarrow
\text{P2 compression validity}.
\]

No such inference was tested.

---

Paper 2 must **not** imply that intermediate harmonic bands resisted compression **because** they contained most retained PCA morphology energy.

The compression and localization analyses are distinct.

---

Paper 2 must **not** claim that:

- intermediate harmonics are mathematically incompressible;
- high harmonics are noise;
- discarded coefficients are irrelevant;
- PCA proves garment morphology is linear;
- outer radial position means garment boundary;
- PCA axes are semantic garment factors.

---

## 7.2 Prohibited in Paper 1

Paper 1 must **not** claim:

> The radial-angular representation provides an optimally compressed spectral representation.

**Reason:** Compression belongs to Paper 2.

---

Paper 1 must **not** claim:

> Different harmonic scales require different radial representations.

**Reason:** This is the central Paper 2 result.

---

Paper 1 must **not** use:

\[
DCT_4/RAW_{72}/RAW_{72}/db4_4
\]

as retrospective justification for choosing \(m=2\).

---

Paper 1 must **not** use the Paper 2 result

\[
78.54\%
\]

of retained PCA morphology energy in \(k=5{:}24\) to make claims about the relative importance of \(F_2\).

---

Paper 1 must **not** claim that its 14-dimensional representation is superior to the full-harmonic representation.

The representations answer different scientific questions and were not tested as interchangeable competitors.

---

Paper 1 must **not** claim:

- harmonic-band-dependent compressibility;
- evidence-selected hybrid spectral compression;
- nonlinear latent-model inferiority;
- PCA as the optimal garment latent space;
- radial-harmonic PCA localization.

These belong to Paper 2.

---

# 8. Approved vocabulary

Vocabulary is intentionally separated so that contribution ownership remains clear even when the papers share mathematics.

---

## 8.1 Preferred Paper 1 vocabulary

Use preferentially:

- **explicit radial-angular measurement**
- **explicit geometric measurement framework**
- **second-harmonic radial-angular representation**
- **14-dimensional radial-angular representation**
- **second-harmonic magnitude**
- **axial orientation**
- **axial-safe descriptors**
- **shell-conditioned angular distribution**
- **rigid-image rotation control**
- **invariant/equivariant transformation behavior**
- **doubled-angle equivariance**
- **\(R(2\phi)\) action**
- **tested rigid rotations**
- **coordinate-frame dependence**
- **magnitude-only reconstruction**
- **phase reconstruction**
- **analytic rotation control**
- **descriptor sensitivity**
- **radial-domain sensitivity**
- **phase-conditioning geometry**
- **garment-identity-disjoint reconstruction**
- **dependency-aware inference**
- **measurement assumptions**
- **measurement limits**
- **geometric interpretability**

### Preferred Paper 1 verbs

- measure
- define
- construct
- characterize
- reconstruct
- validate
- test
- quantify
- constrain
- expose
- evaluate sensitivity
- establish dependence

---

## 8.2 Preferred Paper 2 vocabulary

Use preferentially:

- **full radial-harmonic field**
- **full-harmonic radial-function formulation**
- **harmonic-conditioned radial representation**
- **band-specific radial representation**
- **evidence-selected hybrid representation**
- **radial representation requirement**
- **harmonic-scale-dependent representation**
- **representation-selection inference**
- **compression support**
- **preservation where compression is unsupported**
- **hybrid radial-spectral representation**
- **latent representation**
- **latent geometry**
- **nonlinear geometry characterization**
- **PCA retained subspace**
- **inverse spectral mapping**
- **mapped morphology energy**
- **radial-harmonic localization**
- **retained-subspace morphology**

### Preferred Paper 2 verbs

- retain
- partition
- compare
- select
- compress
- preserve
- evaluate
- localize
- map
- characterize
- test representation requirements
- establish support

---

# 9. Vocabulary requiring caution

The following terms may appear in either manuscript only when context makes ownership unambiguous:

- radial-angular representation;
- Fourier representation;
- spectral representation;
- interpretable representation;
- morphology representation;
- geometric representation;
- harmonic representation;
- rotation robustness;
- rotation invariance.

In Paper 2, avoid using these broad phrases alone as novelty statements.

For example:

### Avoid in Paper 2

> We introduce an interpretable radial-angular representation.

### Prefer

> We evaluate radial representation requirements across the full angular-harmonic field.

or

> We construct an evidence-selected hybrid radial-spectral representation from the shared shell-conditioned harmonic field.

For Paper 1, prefer **“intended invariant/equivariant transformation behavior over the tested rigid rotations”** over unqualified claims of “rotation invariance” or “rotation robustness.”

---

# 10. Required Paper 2 revision

## CURRENT WORDING

> **Contribution 1 — Conditional radial-angular spectral representation**

and wording of the form:

> We formulate sketch morphology as
>
> \[
> P(\theta\mid r)
> \rightarrow
> F_k(r).
> \]

### FIREWALL STATUS

\[
\boxed{\text{REWORD — REQUIRED}}
\]

### Reason

This wording makes Paper 2 appear to claim independent ownership of the radial-angular Fourier construction already central to Paper 1.

The mathematics may remain.

The novelty claim must change.

---

## APPROVED REPLACEMENT

### Contribution 1 — Full-harmonic radial-function formulation for representation selection

> Starting from the shell-conditioned radial-angular field, we retain the positive angular harmonics as explicit radial functions
>
> \[
> F_k(r),
> \qquad
> k=1,\ldots,36,
> \]
>
> enabling radial representation to be evaluated conditionally on angular harmonic scale.

The conceptual transition should therefore be:

\[
\underbrace{
P(\theta\mid r)
\rightarrow
F_k(r)
}_{\text{shared measurement substrate}}
\]

followed by

\[
\underbrace{
F_k(r)
\rightarrow
\text{harmonic bands}
\rightarrow
\text{bandwise representation testing}
\rightarrow
\text{evidence-selected hybrid encoding}
}_{\text{Paper 2 contribution}}.
\]

This wording is the approved firewall formulation.

---

# 11. Paper 1 contribution lock

Paper 1 may claim contributions in the following form:

1. an explicit second-harmonic radial-angular measurement of garment-sketch geometry;
2. a mathematically justified axial interpretation of \(m=2\);
3. a non-redundant 14-dimensional radial and axial descriptor representation;
4. a rigid-image rotation audit of the final 14-dimensional representation, separating approximately invariant scalar/magnitude behavior from \(R(2\phi)\)-equivariant doubled-angle orientation coordinates over the tested rotations;
5. garment-identity-disjoint reconstruction of the observed second-harmonic field;
6. separate global analytic and identity-randomized rotation controls establishing coordinate-frame dependence of the reconstruction experiment;
7. numerical and radial-domain sensitivity analysis;
8. perturbation-theoretic analysis of axial phase error;
9. garment-identity-aware uncertainty and association analysis.

Paper 1 must keep these claims narrow.

It does **not** claim:

- exact raster-level rotation invariance;
- robustness to arbitrary transformations or rotations outside the tested range;
- semantic garment understanding;
- optimal spectral compression;
- universal harmonic superiority;
- universal radial domains;
- complete angular-density reconstruction;
- latent garment factors;
- a universal garment morphology manifold.

---

# 12. Paper 2 contribution lock

Paper 2 may claim contributions in the following form:

1. extension of the shared radial-angular substrate to an explicitly retained full positive harmonic field \(F_k(r)\), \(k=1,\ldots,36\), for representation-selection analysis;
2. harmonic-band-specific testing of radial representation requirements;
3. inferential selection of compact versus preserved radial structure;
4. an evidence-selected DCT/raw/raw/wavelet hybrid representation;
5. multiplicity-controlled comparison of nonlinear latent alternatives against PCA;
6. characterization of nonlinear geometry without claiming a canonical nonlinear manifold;
7. exact inverse mapping of retained PCA perturbations into radial-harmonic coordinates;
8. descriptive radial-harmonic localization of retained PCA morphology.

Paper 2 does **not** claim:

- invention of radial-angular garment measurement;
- invention of shell-conditioned angular Fourier analysis;
- second-harmonic axial validation;
- rigid-image invariance/equivariance validation of the 14-D Paper-1 representation;
- semantic garment factors;
- universal optimal compression;
- mathematical incompressibility of intermediate harmonics;
- general inferiority of nonlinear models;
- complete representation of garment morphology.

---

# 13. Cross-paper inference firewall

Results may not be chained across papers unless the logical connection is independently tested.

The following forms are prohibited:

\[
P1_A
\Rightarrow
P2_B
\]

or

\[
P2_B
\Rightarrow
P1_A
\]

merely because both derive from the same radial-angular field.

Specifically:

\[
\text{strong }F_2\text{ reconstruction}
\nRightarrow
\text{valid hybrid compression}
\]

\[
\text{P1 rigid-image equivariance/invariance audit}
\nRightarrow
\text{P2 full-harmonic compression validity}
\]

\[
\text{band-dependent compression}
\nRightarrow
m=2\text{ is optimal}
\]

\[
78.54\%\text{ intermediate-harmonic PCA energy}
\nRightarrow
\text{intermediate bands resisted compression}
\]

\[
41.98\%\text{ coefficient reduction}
\nRightarrow
41.98\%\text{ redundancy removed}
\]

and

\[
\text{nonlinear geometry}
\nRightarrow
\text{nonlinear predictive advantage}.
\]

Each paper must preserve the evidence class of its own analysis.

---

# 14. Shared-data disclosure principle

Because both papers use CLO-SKET and share part of the mathematical preprocessing lineage, this relationship should be disclosed rather than obscured.

Where journal policy permits or requires, the manuscripts should make clear that:

1. the studies use the same underlying CLO-SKET dataset;
2. they address different scientific questions;
3. Paper 1 concerns explicit second-harmonic measurement, transformation behavior, reconstruction, and validation;
4. Paper 2 concerns representation requirements across the full harmonic field and subsequent latent characterization;
5. shared preprocessing does not imply duplicated primary analyses or results.

The final wording should be adapted to the target journal's related-manuscript and prior-work policy.

---

# 15. Abstract firewall checklist

Before submission, verify that:

- [ ] P1 Abstract owns the 14-D representation.
- [ ] P1 Abstract owns \(m=2\) axial interpretation.
- [ ] P1 Abstract owns the rigid-image invariance/equivariance audit over the tested rotations.
- [ ] P1 Abstract keeps the rigid-image transformation audit distinct from analytic/randomized coordinate-frame controls.
- [ ] P1 Abstract owns reconstruction and coordinate-frame controls.
- [ ] P1 Abstract owns sensitivity and phase conditioning.
- [ ] P1 Abstract does not mention P2 compression findings.
- [ ] P2 Abstract does not claim invention of radial-angular measurement.
- [ ] P2 Abstract does not claim the P1 rigid-image rotation-control result as P2 evidence.
- [ ] P2 Abstract begins its novelty at the full harmonic field / representation-selection problem.
- [ ] P2 Abstract owns harmonic-band-dependent compression support.
- [ ] P2 Abstract owns the hybrid representation.
- [ ] P2 Abstract owns latent-model comparison and radial-harmonic localization.
- [ ] No numerical result is duplicated as a primary result across abstracts.

---

# 16. Introduction firewall checklist

- [ ] Shared substrate is described as background/methodological lineage.
- [ ] \(P(\theta\mid r)\) is not independently claimed as P2 novelty.
- [ ] P1 research questions concern measurement, transformation behavior, reconstruction, robustness limits, symmetry, and error geometry.
- [ ] P1 distinguishes rigid-image representation transformation behavior from analytic/randomized reconstruction coordinate dependence.
- [ ] P2 research questions concern harmonic-conditioned radial representation and latent structure.
- [ ] P1 contribution list contains no compression contribution.
- [ ] P2 contribution list contains no 14-D, axial-measurement, or rigid-image equivariance contribution.
- [ ] P2 Contribution 1 uses the approved revised wording.
- [ ] Neither manuscript describes itself as solving the other's central scientific question.

---

# 17. Methods firewall checklist

- [ ] Shared dataset details agree numerically.
- [ ] Garment-identity definitions agree.
- [ ] Shared radial-angular notation is compatible.
- [ ] Shared Fourier sign convention is compatible.
- [ ] Shared radial/angular grid specifications agree where the same objects are used.
- [ ] Shared methods are identified as shared foundation rather than duplicated novelty.
- [ ] P1 owns detailed \(F_2\)/14-D construction.
- [ ] P1 owns the rigid-image rotation/preprocessing control and \(R(2\phi)\) transformation audit.
- [ ] P1 owns reconstruction and analytic/randomized rotation methods.
- [ ] P1 owns sensitivity and phase-conditioning methods.
- [ ] P2 owns harmonic-band partition.
- [ ] P2 owns DCT/wavelet/raw candidate evaluation.
- [ ] P2 owns compression inference.
- [ ] P2 owns hybrid packing, PCA, nonlinear models, and inverse latent mapping.
- [ ] No method is described differently across manuscripts merely to disguise common provenance.

---

# 18. Results firewall checklist

- [ ] P1 rigid-image rotation-control results appear only as P1 primary evidence.
- [ ] P1 reconstruction results appear only as P1 primary evidence.
- [ ] P1 analytic/randomized rotation results appear only as P1 primary evidence.
- [ ] P1 sensitivity results appear only as P1 primary evidence.
- [ ] P1 phase-conditioning associations appear only as P1 primary evidence.
- [ ] P2 compression statistics appear only as P2 primary evidence.
- [ ] P2 hybrid dimensionality appears only as P2 primary evidence.
- [ ] P2 nonlinear-model results appear only as P2 primary evidence.
- [ ] P2 PCA localization percentages appear only as P2 primary evidence.
- [ ] No result from one paper is presented as independent confirmation of the other.
- [ ] Mathematical identities are never presented as independent empirical corroboration.

---

# 19. Discussion firewall checklist

- [ ] P1 discusses measurement validity rather than compression architecture.
- [ ] P1 discusses the intended invariant/equivariant structure over the tested rigid-image rotations without claiming exact or universal rotation invariance.
- [ ] P1 keeps rigid-image transformation validation distinct from reconstruction coordinate-frame dependence.
- [ ] P1 discusses coordinate dependence.
- [ ] P1 discusses numerical/domain sensitivity.
- [ ] P1 discusses phase-conditioning geometry.
- [ ] P2 discusses harmonic-dependent radial representation.
- [ ] P2 discusses preservation where compression support is absent.
- [ ] P2 distinguishes nonlinear geometry from nonlinear-model utility.
- [ ] P2 discusses retained-subspace localization without semantic overreach.
- [ ] P2 does not redefine the radial-angular substrate as its own methodological invention.
- [ ] P2 does not appropriate the P1 rigid-image rotation audit as a P2 contribution.
- [ ] P1 does not retrospectively use P2 to strengthen the \(m=2\) argument.
- [ ] Neither paper claims semantic garment understanding.

---

# 20. Conclusion firewall checklist

Paper 1's conclusion should terminate approximately at:

\[
\boxed{
\text{explicit measurement}
\rightarrow
\text{validated transformation/dependency structure}
\rightarrow
\text{known limits}
}
\]

Paper 2's conclusion should terminate approximately at:

\[
\boxed{
\text{harmonic-dependent radial requirements}
\rightarrow
\text{evidence-selected hybrid representation}
\rightarrow
\text{latent spectral organization}
}
\]

The conclusions must not converge into the same broad claim that:

> “We introduce a new radial-angular Fourier representation for garment sketches.”

That formulation is prohibited as a shared conclusion.

---

# 21. Final pre-submission firewall audit

Before either manuscript is submitted, perform a literal line-by-line search for the following phrases and inspect every occurrence:

- `we introduce`
- `we propose`
- `novel`
- `new representation`
- `radial-angular representation`
- `Fourier representation`
- `spectral representation`
- `interpretable representation`
- `our representation`
- `our framework`
- `first`
- `demonstrate`
- `establish`
- `show that`
- `optimal`
- `robust`
- `generalizable`
- `invariant`
- `equivariant`
- `rotation`
- `compress`
- `latent`
- `morphology`

Every occurrence must be checked against this firewall.

---

# 22. Reviewer simulation test

Before submission, the two manuscripts should pass the following test.

A reviewer reading both papers should be able to state:

### Paper 1

> This paper defines and stress-tests an explicit second-harmonic radial-angular measurement of repeated garment sketches, including its axial interpretation, rigid-image invariant/equivariant transformation behavior over tested rotations, reconstruction behavior, coordinate dependence, numerical sensitivity, and phase-error geometry.

### Paper 2

> This paper starts from the radial-harmonic field and asks a different question: whether radial representation requirements depend on angular harmonic scale, then constructs an inferentially selected hybrid representation and characterizes its retained latent geometry.

If a reviewer could instead summarize both as:

> These papers both introduce a radial-angular Fourier representation of CLO-SKET,

the firewall has failed.

---

# 23. Hard-stop rules

Manuscript editing must stop for review if any proposed revision does one of the following:

1. assigns the 14-D representation to Paper 2;
2. assigns the rigid-image invariance/equivariance audit of the 14-D representation to Paper 2;
3. assigns full-harmonic compression to Paper 1;
4. claims \(P(\theta\mid r)\rightarrow F_k(r)\) as independent novelty in both;
5. imports numerical primary results from one paper into the other's evidentiary argument;
6. uses P2 compression findings to retrospectively justify \(m=2\);
7. uses P1 reconstruction or rigid-image transformation findings to validate P2 compression;
8. converts a descriptive localization result into semantic interpretation;
9. converts unsupported compression into mathematical incompressibility;
10. converts nonlinear-model negative results into a general claim of linear morphology;
11. changes shared-method descriptions solely to conceal common methodological lineage.

Any such revision requires explicit firewall reassessment before acceptance.

---

# 24. Final claim lock

## PAPER 1

\[
\boxed{
\begin{aligned}
\text{CLO-SKET P1}
=&\
\text{explicit second-harmonic measurement}\\
&+\text{axial geometry}\\
&+\text{14D representation}\\
&+\text{rigid-image transformation audit}\\
&+\text{identity-disjoint reconstruction}\\
&+\text{coordinate-frame controls}\\
&+\text{numerical sensitivity}\\
&+\text{phase-conditioning analysis}.
\end{aligned}
}
\]

---

## PAPER 2

\[
\boxed{
\begin{aligned}
\text{CLO-SKET P2}
=&\
\text{full radial-harmonic field}\\
&+\text{harmonic-conditioned representation testing}\\
&+\text{evidence-selected hybrid compression}\\
&+\text{latent-model validation}\\
&+\text{radial-harmonic latent localization}.
\end{aligned}
}
\]

---

# 25. Final firewall statement

The two papers share:

\[
\boxed{
\text{dataset}
+
\text{radial-angular substrate}
+
\text{Fourier lineage}
+
\text{dependency-aware validation philosophy}
}
\]

but they do **not** share their primary scientific claim.

Their separation is:

\[
\boxed{
\textbf{Paper 1: What does the measurement mean, how does it transform, and when can it be trusted?}
}
\]

versus

\[
\boxed{
\textbf{Paper 2: How should the full harmonic field be represented across angular scales?}
}
\]

This distinction must remain invariant through all subsequent manuscript revisions.

---

# FIREWALL STATUS

\[
\boxed{
\textbf{P1 ↔ P2 CLAIM FIREWALL — FROZEN}
}
\]

**Mandatory outstanding action:** revise Paper 2 Contribution 1 according to Section 10 before final submission.

Any future change to either manuscript's contribution statement, primary research question, transformation claims, or interpretation of shared radial-angular methodology must be checked against this file before being accepted.