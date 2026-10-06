# P2_16 Final Submission Audit v1.0

## Audit target

Submission candidate:

`P2_FINAL_MANUSCRIPT_ASSEMBLY_v0_7_SUBMISSION_CANDIDATE.md`

SHA-256:

`3af5ca3baa9331f2227d2c121f13efb7f60046d3769c899383b1e7a4133ee870`

Synchronized references:

`P2_14_REFERENCES_FINAL_v1_1.md`

SHA-256:

`97793290a5810fc68dc2ba16dfd26fdd0d80853d4e6547d800218af21dc0f0e9`

Reviewer-proofing reconciliation:

`P2_15_REVIEWER_PROOFING_RECONCILIATION_v1_0.md`

SHA-256:

`89671213ad245277499a3727481c74f461fcab13475330b82e7dddb79b09d87d`

## Scope

This audit is a final mechanical and claim-boundary review. It does **not** reopen experiments, alter frozen numerical results, reselect representations, retune models, or modify historical frozen artifacts.

## Results

| Audit item | Result | Notes |
|---|---|---|
| Figures | PASS | Figures 1–5 are referenced and captions for Figures 1–5 are present. |
| Tables | PASS | Tables 1–5 are referenced and headings for Tables 1–5 are present. |
| Placeholders | PASS | No TODO, TBD, FIXME, or placeholder markers found. |
| Internal research labels | PASS | No P2 internal experiment labels or EXP identifiers found in the submission candidate. |
| Duplicate assembly text | PASS | No residual `The the`, `audit audit`, `intervention intervention`, `sequence sequence`, or `decomposition decomposition` defects found. |
| Standalone bibliography | PASS | 26 reference entries parsed; all 26 have corresponding in-text use. |
| Citation scan | PASS WITH PARSER NOTE | Automated surname-year scan flagged several second/co-author surnames (e.g., Cadima, Fang, Giardina, Lafon, Lu, Welling) as if they were standalone citation keys. Manual interpretation shows these are components of valid multi-author references, not missing bibliography entries. |
| Abstract claim boundary | PASS | Uses “motivate a three-stage analysis principle,” avoiding a universal-law claim. |
| Novelty boundary | PASS | Literature-search boundary is explicit; no absolute-priority claim is made. |
| RAW→CROP interpretation | PASS | Stage localization is separated from causal support-dependence evidence. |
| Multiplicity scope | PASS | Prespecified confirmatory families are explicitly bounded. |
| Bootstrap unit | PASS | Garment identity within category is explicitly stated as the resampling unit. |
| Train/held-out firewall | PASS | Held-out identities are explicitly excluded from candidate/budget/admissibility/tie-breaking decisions. |
| Post-selection sensitivity | PASS | Whole-representation comparisons are explicitly descriptive and not used to reselect the hybrid. |
| Fold 3 handling | PASS | Retained without exclusion, retuning, or reselection after structural audit. |
| Nonlinear-model scope | PASS | No generic PCA-superiority claim. |
| PCA-64 denominator | PASS | Localization percentages are explicitly normalized within the retained PCA-64 subspace. |
| Sign-flip assumption | PASS | Null sign symmetry is stated as an inferential condition; equal variances are not asserted as required. |
| Baseline scope | PASS | Lack of modern learned retrieval baselines is explicitly bounded to the paper’s representation-audit objective. |
| Frozen-artifact integrity | PASS | No historical frozen artifact is altered by this audit. |
| New experiments / reselection | PASS | None performed. |

## Citation and reference reconciliation

The synchronized standalone bibliography contains **26 parsed reference entries**, and every parsed entry appears in the manuscript.

The automated citation scan produced apparent “missing” keys for several co-authors because the detector reads author pairs such as “Jolliffe & Cadima (2016)” as two possible surname-year keys. These are not missing references; they belong to bibliography entries already present under the first author. No genuine missing bibliography entry was established by the audit.

## Mechanical reconciliation note

An earlier audit pass exposed additional duplicated assembly phrases beyond the three initially identified during reviewer reconciliation. Those defects were mechanical only. The submission candidate was checked again after cleanup, and the targeted duplicate patterns now return zero matches.

No numerical value, inferential decision, representation choice, table result, or scientific conclusion was changed during that cleanup.

## Preserved scientific hierarchy

The final candidate preserves the following order:

1. representation validity precedes representation selection;
2. raster support is a demonstrated dependency of the tested historical raster-relative representation under the controlled same-pixel intervention;
3. the object-relative construction is a matched control/counterfactual, not a retroactive replacement for the historical selection analysis;
4. radial complexity is allocated only where held-out evidence supports compression;
5. whole-representation comparisons remain descriptive post-selection sensitivity analyses;
6. detectable nonlinear structure does not imply validated nonlinear-model advantage;
7. latent localization is mathematical, not semantic garment-part disentanglement;
8. the contribution is the controlled representation audit plus evidence-controlled complexity allocation, not invention of Fourier analysis, normalization, DCT, wavelets, PCA, or nonlinear encoders.

## Final verdict

`PASS_FOR_SUBMISSION_FREEZE`

No scientific reopening is required on the basis of this audit.

The next permitted step is a targeted repository freeze of the new submission-facing artifacts while preserving all historical frozen artifacts unchanged.
