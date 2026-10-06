# Common External Audit Rubric and Output Schema

## Purpose

This package is for an independent adversarial review of WeaveAI Paper II. The reviewer must distinguish:

1. manuscript claims;
2. support from the frozen project sources;
3. external literature evidence;
4. reviewer inference.

Internal audit files are **not authoritative**. They are evidence of prior checking and should themselves be challenged.

## Severity scale

- **P0 — submission blocker:** invalidates a main claim, statistical inference, provenance, or reproducibility statement.
- **P1 — major:** material scientific/novelty/methodological problem requiring revision before submission.
- **P2 — moderate:** important clarification, missing citation, figure/table issue, or wording risk.
- **P3 — minor:** copyedit, notation, style, or non-material presentation issue.

## Required audit dimensions

A. Scientific question and contribution hierarchy  
B. Representation validity / support-dependence logic  
C. Statistical design and multiplicity control  
D. Identity-disjoint evaluation and leakage risk  
E. Representation-selection logic  
F. Whole-representation baseline interpretation  
G. Nonlinear latent-model claims  
H. Exact latent-to-morphology interpretation  
I. Novelty and prior-art boundary  
J. References and citation accuracy  
K. Figures/tables and numerical consistency  
L. Reproducibility / provenance / frozen-artifact discipline  
M. Writing, structure, and journal-facing language

## Mandatory output structure

### 1. Executive verdict
Choose exactly one:
- READY
- READY WITH MINOR REVISION
- MAJOR REVISION
- BLOCK / DO NOT SUBMIT

Then give 5–10 sentences explaining why.

### 2. Issue ledger
Use a table with:
`ID | Severity | Section/Figure/Table | Exact claim or wording | Problem | Evidence | Required fix`

Every P0/P1/P2 item must include an exact manuscript locator and a minimal corrective action.

### 3. Claim-support matrix
For every major contribution claim:
`Claim | Frozen source support | External literature support/contradiction | Status | Safe wording`

Status must be one of:
- supported
- supported with qualification
- unsupported
- contradicted
- cannot determine

### 4. Statistical audit
Explicitly address:
- exchangeability assumptions;
- category-level sign-flip inference;
- max-T / FWER control;
- identity bootstrap;
- train-selection vs held-out confirmation;
- post-selection whole-representation sensitivity;
- whether any p-value / CI is reused outside its conditioning;
- fold-composition anomaly handling;
- whether negative results are represented fairly.

### 5. Novelty / prior-art matrix
Classify each located precedent as:
- DIRECT
- CLOSE / PARTIAL
- GENERAL THEORY
- DIFFERENT / TERMINOLOGICAL NEAR-MISS

A DIRECT precedent for the 05K support audit should substantially match:
- object/foreground pixels held fixed;
- independent 2-D raster-support manipulation;
- no resize/interpolation required by the intervention;
- recomputed representation/spectral allocation;
- quantified support dependence;
- ideally a matched object-relative/intrinsic control.

Generic scale invariance, cropping, windowing, or zero-padding is **not automatically DIRECT**.

### 6. Figure/table audit
For Figures 1–5 and Tables 1–5:
- verify every shown number against manuscript/source;
- flag any visual implication stronger than the text;
- confirm schematic vs empirical content is clearly distinguished;
- verify denominators and uncertainty labels.

### 7. Reference audit
List:
- incorrect metadata;
- unsupported citations;
- missing key precedent;
- uncited references;
- places where a citation is too weak for the claim.

### 8. Minimal revision set
Return only the smallest set of changes required before submission.
Do not rewrite the paper wholesale unless necessary.

### 9. Reviewer confidence
For each P0/P1 issue, state confidence: high / medium / low and why.

## Non-negotiable interpretation boundaries to test, not assume

The manuscript should not claim:
- a new Fourier transform or new generic normalization method;
- universal descriptor superiority;
- a retrieval-performance breakthrough;
- that support explains all RAW→CROP effects;
- that every image changes monotonically with support;
- that padding creates garment frequency content;
- that PCA proves global linearity;
- that AE/VAE are inferior in general;
- that radial/harmonic coordinates are semantic garment parts;
- an absolute “first-ever” novelty claim.

The reviewer should flag the manuscript if it violates any of these.
