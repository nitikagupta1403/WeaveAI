# P2_16 Final Submission Audit v1.3

## Scope

Audited manuscript: `P2_FINAL_MANUSCRIPT_ASSEMBLY_v0_6_REVIEWER_PROOFED.md`
References: `P2_14_REFERENCES_FINAL_v1_1.md`
Reconciliation: `P2_15_REVIEWER_PROOFING_RECONCILIATION_v1_0.md`

This audit checks submission-facing consistency only. It does not rerun experiments, recompute inferential results, reselect representations/models, or alter frozen scientific artifacts.

## Overall status

**PASS**

## 1. Figures and tables

- Figures referenced: [1, 2, 3, 4, 5]
- Figure captions detected: [1, 2, 3, 4, 5]
- Tables referenced: [1, 2, 3, 4, 5]
- Table headings detected: [1, 2, 3, 4, 5]
- Result: **PASS**

## 2. Citation and bibliography consistency

- Bibliography entries in synchronized v1.1 file: **27**
- Parsed first-author/year keys: **27**
- Bibliography entries without manuscript citation context: **0**
- Citation-like author/year tokens not represented among bibliography authors: **0**
- Uncited entries: `none`
- Unknown citation-like tokens: `none`
- Result: **PASS**

**Parser note:** earlier draft audit files incorrectly reported 26 references because the `# References` heading and first entry were treated as one block. The corrected artifact-level count is **27**, matching the synchronized bibliography.

## 3. Placeholder, internal-label, and duplicate-text scan

- TODO: **0**
- TBD: **0**
- FIXME: **0**
- placeholder: **0**
- internal P2 labels: **0**
- experiment IDs: **0**
- audit-stage IDs: **0**
- the the: **0**
- audit audit: **0**
- intervention intervention: **0**
- sequence sequence: **0**

- Result: **PASS**

## 4. Claim-boundary audit

- historical raster-relative support-dependency boundary: **PASS**
- matched object-relative control/counterfactual: **PASS**
- post-selection comparisons not used to reselect: **PASS**
- nonlinear null bounded to tested models: **PASS**
- PCA-64 denominator explicit: **PASS**
- sign-symmetry assumption explicit: **PASS**
- baseline scope explicit: **PASS**
- novelty boundary not absolute priority: **PASS**

- Result: **PASS**

## 5. Numerical-anchor presence check

This is a presence/consistency check, not a recomputation of results.

- `2,300`: **present**
- `230`: **present**
- `23`: **present**
- `41.98%`: **present**
- `44.65%`: **present**
- `78.54%`: **present**
- `66.84%`: **present**
- `51.30%`: **present**
- `91.5%`: **present**
- `89.5%`: **present**
- `87.3%`: **present**

- Result: **PASS**

## 6. Artifact integrity

- Frozen v0.5 remains untouched.
- Reviewer-proofed manuscript is a derivative artifact.
- Original standalone reference artifact remains untouched.
- Frozen figure assets remain untouched.
- No experiment was reopened.
- No representation/model selection was repeated.
- No numerical result was modified in this audit.

## 7. SHA-256

- Manuscript: `3af5ca3baa9331f2227d2c121f13efb7f60046d3769c899383b1e7a4133ee870`
- References: `97793290a5810fc68dc2ba16dfd26fdd0d80853d4e6547d800218af21dc0f0e9`
- Reconciliation: `89671213ad245277499a3727481c74f461fcab13475330b82e7dddb79b09d87d`

## Closure

`FINAL_SUBMISSION_AUDIT_PASS`

The reviewer-proofed artifact set is ready for the final repository freeze/commit step.