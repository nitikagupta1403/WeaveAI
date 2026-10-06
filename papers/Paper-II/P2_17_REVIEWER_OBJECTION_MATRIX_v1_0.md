# Paper II reviewer-objection matrix v1.0

Date: 2026-10-06. Review baseline: branch `paper-ii-05k-support-audit`, commit `057972b2dcbc7949bdc93b9266a875625ce530c5`.

Manuscript: [P2_FINAL_MANUSCRIPT_ASSEMBLY_v0_7_FINAL_AUDITED.md](P2_FINAL_MANUSCRIPT_ASSEMBLY_v0_7_FINAL_AUDITED.md). SHA-256: `3af5ca3baa9331f2227d2c121f13efb7f60046d3769c899383b1e7a4133ee870`.

This is a targeted review of six objections raised during publication-strategy discussion. It checks the actual manuscript responses against available archived evidence. It is not a new blind review, exhaustive literature search, experiment, statistical recomputation, or guarantee of editorial acceptance. Reviewer-response language below is an assessment based on this evidence, not an assertion that a reviewer has accepted the response.

## Decision

All six objections already have explicit manuscript responses. No scientific wording patch or v0.8 manuscript is justified solely by these six objections. Some underlying limitations remain open despite being accurately disclosed. No contradiction requiring scientific reopening was identified in this targeted review.

The objection matrix and its response notes are new artifacts. The v0.7 manuscript, historical manuscripts, figures, numerical results, selection decisions, and frozen reproducibility artifacts remain unchanged.

## Status definitions

- **Addressed in text:** the manuscript explicitly bounds or answers the objection.
- **Open evidence limitation:** the stronger claim would require additional empirical evidence.
- **Open editorial judgment:** the existing evidence cannot establish novelty sufficiency or journal significance by itself.
- **Optional copy edit:** a verified mechanical defect that does not change the scientific response.

## Matrix

| ID | Reviewer objection | Exact manuscript locations | Available supporting evidence | Assessment and remaining gap | Action now |
|---|---|---|---|---|---|
| RO-01 | Coordinate normalization and support sensitivity are already known. | §§2.1–2.5, 2.12, 3.4.4–3.4.7, 4.1, 5.2–5.3, 5.11. | Seven support levels; 2,300 fixed-pixel patches; 16,100 conditions; historical baseline replay; matched object-relative numerical invariance; three category-level directional endpoints with joint max-T inference. Sources E01–E03. | **Addressed in text; novelty significance remains an open editorial judgment.** The contribution is the controlled empirical audit and its consequences for this representation. Established normalization ingredients are acknowledged. A narrow literature-search boundary does not establish absolute historical priority. | Keep the explicit controlled-design distinction and qualified novelty statement. Do not claim normalization is new or that no prior study exists. No fresh literature-search verdict is issued here. |
| RO-02 | The hybrid was selected in a representation later shown to depend on support. | Abstract; §3.4.8; §§4.3, 5.4, 5.11–5.12. | Historical compression decisions are archived separately from the later support intervention. The hybrid remains DCT4/RAW72/RAW72/db4-wavelet4. Sources E01, E02, E04. | **Addressed in text; prospective object-relative selection remains an open evidence limitation.** Historical results are conditional on their coordinate system. Matched control invariance does not validate the historical hybrid as invariant, universally superior, or optimal. | Preserve chronology and the conditional claim. Do not replace the historical selection analysis. A prospective object-relative pipeline would be a separately designed study. |
| RO-03 | Uniform RAW42 is almost as good, so why use the hybrid? | §4.3, Table 3, Figure 3 caption, §5.7. | Full RAW72: MRR 0.819373, 2,592 complex coefficients; hybrid: 0.816766, 1,504; RAW42: 0.815896, 1,512. These are descriptive post-selection comparisons. Table 2 and E04 document the separate bandwise selection evidence. | **Addressed prominently; added operational value over RAW42 remains an open evidence limitation.** The hybrid-minus-RAW42 mean difference is only 0.000870. No confirmatory superiority, equivalence, or practical-benefit claim follows. | Keep Table 3 visible. Present bandwise allocation as the contribution. Do not claim the hybrid is necessary for competitive retrieval or that its dimensionality reduction is unique. |
| RO-04 | One garment dataset cannot establish broad applicability. | §§3.1, 5.11 first limitation, 5.12. | CLO-SKET: 2,300 sketches, 230 identities, 23 categories; complete identity separation is described in §§3.1 and 3.7. Source E04 documents historical grouped analyses. | **Addressed in text; external replication remains an open evidence limitation.** Identity-disjoint testing within CLO-SKET does not establish cross-dataset or cross-domain generalization. | Maintain dataset-qualified conclusions. Do not describe the selected band pattern as a universal property of garment or shape morphology. External replication belongs to a new protocol or a genuinely necessary later revision. |
| RO-05 | Five folds provide weak evidence about nonlinear models. | §§3.13–3.14, 4.4, Table 4, 5.8, 5.11. | Ten matched-dimensional contrasts; 32 exhaustive sign configurations; best mean gain VAE16–PCA16 = +0.014341, adjusted p = 0.2500; overlapping training portions explicitly disclosed. Frozen notebook execution 32 contains these anchors (E04). | **Addressed in text; power and model breadth remain open evidence limitations.** Failure to establish advantage is not evidence of equivalence, absence of benefit, or general PCA superiority. Conditional downstream validation is not untouched end-to-end pipeline validation. | Retain PCA as the practical baseline under present evidence. Do not invent a power estimate or add a generic rejection of AE/VAE. A stronger performance claim requires an appropriately designed comparison. |
| RO-06 | The latent localization does not identify meaningful garment parts. | §2.9, §§3.15–3.18, §§4.6–4.7 and Table 5, §§5.9–5.11. | Exact inverse mapping of retained PCA directions; sign-invariant energy; PCA64 retains 44.65% standardized variance; intermediate harmonics contain 78.54% of mapped energy within that retained subspace. Notebook execution 47 records the localization quantities and denominator (E04). | **Addressed in text; semantic validation remains an open evidence limitation.** Mathematical traceability is established for the represented subspace. It is not complete sketch reconstruction, semantic disentanglement, or a total-morphology percentage. | Keep the denominator explicit. Do not label radial/harmonic regions as sleeves, necklines, hems, or silhouette boundaries without annotated validation. |

## Evidence registry and inspection boundary

**E01 — Primary descriptor execution.** [P2_R0_05K4_B_report.json](reproducibility/frozen/05K4_B_Primary_Descriptor_Execution_v1_0/P2_R0_05K4_B_report.json). Directly inspected. The archive reports 2,300/2,300 historical baseline replays within tolerance, maximum band discrepancy 2.220446049250313e-16, and exact object-relative field and band invariance for all 16,100 conditions. The report also discloses that complete primary fields were not accumulated into a large archive. Numerical results were read, not recomputed.

**E02 — Primary intervention inference.** [P2_R0_05K4_C_report.json](reproducibility/frozen/05K4_C_Primary_Trajectory_Inference_v1_0/P2_R0_05K4_C_report.json). Directly inspected. All 23 category medians follow the specified direction for each of three tested bands. Exact max-T adjusted probabilities are approximately 1.43e-6 for low, 1.19e-7 for high-middle, and 1.19e-7 for high. The report explicitly excludes external-population generalization and a universal monotonic mechanism claim. Null sign symmetry remains an assumption; exact enumeration does not remove it.

**E03 — Evidence-chain synthesis.** [P2_R0_05K4_D2_evidence_chain.csv](reproducibility/frozen/05K4_D2_Result_Evidence_Synthesis_v1_0/P2_R0_05K4_D2_evidence_chain.csv). Directly inspected. It separates preprocessing localization, geometric diagnostics, observational support–spectral association, controlled calibration, primary intervention inference, and matched control. It does not license a complete causal explanation of natural RAW-to-CROP processing.

**E04 — Historical executed analysis and evidence ledger.** [Frozen executed notebook](reproducibility/provenance/CLO_SKET_Probabilistic_Fourier_Morphology_FROZEN_EXECUTED.ipynb) and [P2_02_EVIDENCE_LEDGER.md](P2_02_EVIDENCE_LEDGER.md). Selected archived outputs were inspected without executing cells. Notebook absolute cell-array positions 21–22 (zero-based; executions 24–25) contain the bandwise effect anchors 0.059306 and 0.039300. Position 27 (execution 32) contains the nonlinear-comparison anchors +0.01434125, adjusted p 0.250000, and 32 sign configurations. Position 37 (execution 47) contains 78.54%, 51.30%, and the 44.65% retained-variance boundary. No complete notebook replay or independent rederivation was performed. Table 3 is the directly inspected source for the post-selection whole-representation values here; its raw result arrays were not independently recovered or rerun in this review.

**E05 — Existing claim reconciliation.** [P2_15_REVIEWER_PROOFING_RECONCILIATION_v1_1.md](P2_15_REVIEWER_PROOFING_RECONCILIATION_v1_1.md). Directly inspected. The prior proofing pass already covers novelty boundaries, held-out separation, post-selection sensitivity, nonlinear scope, retained-subspace denominator, and baseline scope. Repeating these paragraphs would not resolve remaining evidence limitations.

## Exact passage anchors and response notes

### RO-01: novelty

Section 2.5 states: “This is a literature-search boundary, not a claim of absolute priority.” Section 5.3 explicitly identifies the experimental distinction and warns against presenting the result as ordinary zero-padding creating garment frequency content.

Defensible response: established Fourier descriptors and normalization motivate the audit. The specific test holds the garment patch fixed, changes only surrounding support, recomputes the historical field, evaluates predefined spectral endpoints, and checks a matched object-relative construction. Its novelty and importance must be judged at that level. The present matrix does not independently establish the absence of prior art.

### RO-02: chronology and conditional selection

Section 3.4.8 states: “The support audit was a later representation-validity analysis.” It lists the unchanged bands, budgets, admissibility rule, held-out statistic, hybrid, and latent-model decision. Section 5.12 calls prospective object-relative selection future work.

Defensible response: the paper characterizes a dependency of the historical measurement system and reports the original selection results conditional on that system. It does not claim the support audit preceded or validated invariant compression selection. The limitation concerns transfer of those decisions, not an established contradiction in the within-system results.

### RO-03: practical utility

Section 5.7 states: “The hybrid should not be presented as a retrieval-performance breakthrough or as proof that heterogeneous encoding is uniquely necessary for competitive retrieval.” Table 3 makes RAW42 visible alongside the hybrid and full reference.

Defensible response: the method yields evidence-controlled band decisions under a specified selection endpoint. The descriptive retrieval comparison does not establish superiority over RAW42. Similar aggregate retrieval scores do not establish identical represented content, but this study also does not establish that any content difference produces an added practical benefit. Do not use that untested possibility as a rebuttal claim.

### RO-04: generalization

Section 5.11 states: “First, the empirical results are currently specific to CLO-SKET.” Section 5.12 requests external replication of both support dependence and harmonic-dependent selection.

Defensible response: the study provides within-corpus controlled evidence and identity-disjoint evaluation. Generalization across datasets, sketch styles, categories outside the corpus, and domains remains untested. The limitation is acknowledged, not solved by sample size alone.

### RO-05: nonlinear comparison

Section 4.4 explicitly reports the 32 sign configurations and overlapping training portions. Section 5.8 states that the downstream comparison “is not an untouched end-to-end validation of representation selection followed by latent-model selection.”

Defensible response: the evidence did not authorize replacing the practical PCA baseline under the tested configurations. Positive observed gains, including VAE16, remain visible. Lack of adjusted significance cannot establish equivalence or exclude useful effects. Broader architectures, larger independent evaluation, or a prospective power analysis would address a different and stronger claim.

### RO-06: semantic interpretation

Section 5.9 states: “This construction does not make PCA components semantic factors.” Section 5.10 states that the localization quantities are “not percentages of total garment morphology.”

Defensible response: exact traceability applies to retained latent perturbations in explicit representation coordinates. Semantic validity and reconstruction of omitted information are separate questions. Annotation-based validation would be required before assigning garment-part meanings.

## Residual issues and revision decision

| Residual issue | Type | Decision |
|---|---|---|
| Is the controlled audit sufficiently novel and consequential for the venue? | Editorial/literature judgment | Keep the qualified contribution; do not treat an internal PASS as novelty certification. |
| Does heterogeneous allocation offer practical benefits over RAW42? | Empirical | Open; no such advantage is claimed. |
| Does the selected hybrid transfer to object-relative coordinates? | Empirical | Open; requires prospective selection rather than substitution. |
| Do effects and selection patterns replicate externally? | Empirical | Open; explicitly bounded to current data. |
| Could other nonlinear models or a stronger design outperform PCA? | Empirical | Open; current null is configuration- and design-conditional. |
| Do localized latent directions correspond to garment attributes? | Empirical | Open; no semantic labels assigned. |

No six-objection-driven scientific patch is recommended. A v0.8 should not be created merely to repeat qualifications already present. Two optional mechanical defects were directly verified: the §3.3 heading occurs twice consecutively, and §3.4.7 begins “Primary the controlled ...”. These may be corrected in a later separately versioned formatting copy; they do not require experimental reopening and do not alter the frozen audit verdict.

## Artifact reconciliation and verification

- The final-audited manuscript and previously frozen submission-candidate manuscript are byte-identical with SHA-256 `3af5ca3baa9331f2227d2c121f13efb7f60046d3769c899383b1e7a4133ee870`.
- The embedded bibliography has **27 entries**, counted directly. Earlier 26-entry summaries were parser errors; the current audit records the correction.
- Both formerly unavailable companions are now present at the baseline commit: references v1.1 SHA-256 `97793290a5810fc68dc2ba16dfd26fdd0d80853d4e6547d800218af21dc0f0e9`; reconciliation v1.0 SHA-256 `89671213ad245277499a3727481c74f461fcab13475330b82e7dddb79b09d87d`.
- References v1.2 SHA-256 `b9d45a68a506fdd1d1a7db8eb8d1d403bcd18bc408fa204537dfc9b30bc48b81` matches the manuscript's complete `# References` section byte-for-byte. Historical notes about extraction defects are not used as a substitute for the present file comparison.
- The existing audit v1.3 names v0.6 as its target; the present matrix explicitly names and hash-pins v0.7. Neither existing audit is rewritten.
- Manuscript section references, linked local evidence files, selected numerical anchors, and companion hashes were checked. No new experiment, reselection, retuning, numerical-result amendment, semantic annotation, or external literature verification was performed.

Next: use these bounded response notes in submission packaging and any actual reviewer response. Reopen scientific work only for a demonstrated contradiction or a stronger claim that the authors decide must be established.
