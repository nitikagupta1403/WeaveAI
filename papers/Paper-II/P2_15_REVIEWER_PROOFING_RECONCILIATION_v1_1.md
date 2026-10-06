# P2_15 Reviewer-Proofing Reconciliation v1.0

## Scope

This record documents the reviewer-proofing changes applied to:

`P2_FINAL_MANUSCRIPT_ASSEMBLY_v0_6_REVIEWER_PROOFED_r1.md`

derived from the frozen historical manuscript:

`P2_FINAL_MANUSCRIPT_ASSEMBLY_v0_5_FIGURES_INTEGRATED.md`

Historical source commit:

`23d0da8`

The frozen v0.5 manuscript and earlier scientific artifacts remain unchanged.

## Integrity lock

This reviewer-proofing pass made **no new experimental run, no representation reselection, no model reselection, no change to frozen numerical results, no change to reported tables, and no change to frozen figure assets**.

The purpose of the pass is limited to:
- clarification of statistical assumptions and inferential scope,
- clarification of train/held-out separation,
- clarification of post-selection sensitivity boundaries,
- tightening of novelty/prior-art language,
- clarification of denominator and model-scope wording,
- reviewer-facing transparency,
- copy-edit repair,
- standalone reference synchronization.

## Patch ledger

| # | Issue | Change applied | Rationale | Scientific effect |
|---|---|---|---|---|
| 1 | Abstract overstrength | “support a three-stage principle” softened to “motivate a three-stage analysis principle” | Avoids implying a universal methodological law | Clarification only |
| 2 | Related Work capitalization | Lowercase sentence opening corrected | Copy-edit quality | None |
| 3 | Novelty boundary | Added explicit literature-search boundary language and avoided absolute priority claims | Keeps novelty claim narrow and auditable | Clarification only |
| 4 | RAW→CROP interpretation | Reworded to state that most historical high-band change entered at the crop-only stage where raster support changed | Separates stage localization from causal attribution | Clarification only |
| 5 | Multiplicity / max-statistic wording | Clarified prespecified confirmatory families and joint category-level sign application | Makes family-wise control scope explicit | Clarification only |
| 6 | Bootstrap unit | Added that resampling occurred at garment-identity level within category and not independently by sketch | Makes experimental unit explicit | Clarification only |
| 7 | Train/held-out firewall | Added explicit statement that held-out identities did not affect family/budget choice, admissibility screening, or tie-breaking | Makes no-leakage design explicit | Clarification only |
| 8 | Post-selection sensitivity | Added statement that whole-representation comparisons were descriptive and not used to reselect the hybrid | Prevents sensitivity analysis from being misread as confirmatory selection | Clarification only |
| 9 | Fold 3 transparency | Added that the broader uplift fold was structurally audited, retained, and not excluded/retuned/reselected | Addresses possible post-hoc handling concern | Clarification only |
| 10 | Nonlinear-model scope | Added that the null result concerns the tested AE/VAE settings and does not imply generic PCA superiority | Prevents overgeneralization | Clarification only |
| 11 | PCA-64 denominator | Added that localization percentages are normalized within the retained PCA-64 subspace; retained 44.65% full-representation variance context | Prevents denominator ambiguity | Clarification only |
| 12 | Sign-flip assumption | Added explicit null sign-symmetry limitation and noted equal category variances are not required | States the actual inferential assumption | Clarification only |
| 13 | Baseline scope | Added that the study does not benchmark against modern learned retrieval systems because SOTA retrieval is not the study objective | Prevents unintended performance-positioning claim | Clarification only |
| 14 | Duplicate-text defects | Repaired duplicated words/phrases in Discussion | Submission-quality copy edit | None |
| 15 | Reference synchronization | Created `P2_14_REFERENCES_FINAL_v1_2.md` to match the bibliography actually used in v0.6 | Aligns standalone reference artifact with manuscript | None |

## Optional figure-side notes

No frozen figure asset was modified in this reviewer-proofing pass.

Previously considered in-panel notes for Figures 2–5 remain optional because the current captions already carry the relevant scientific boundaries. Any future figure-side changes must be versioned as new figure artifacts and must not overwrite frozen historical files.

## Artifact status

- Frozen manuscript v0.5: preserved unchanged.
- Reviewer-proofed manuscript v0.6: new submission-facing derivative.
- Original standalone references file: preserved unchanged.
- References v1.1: new synchronized derivative.
- Frozen figures: unchanged.
- New experiments: none.
- Reselection: none.
- Numerical result modifications: none.

## Claim hierarchy preserved

The reviewer-proofing pass preserves the manuscript’s scientific hierarchy:

1. **Representation validity precedes representation selection.**
2. **Under the tested historical raster-relative radial-angular representation, surrounding raster support is a demonstrated dependency of angular spectral allocation.**
3. **The matched object-relative construction is a control/counterfactual and is not a retroactive replacement for the historical selection analysis.**
4. **Representation complexity is allocated only where held-out evidence supports compression; absence of support preserves complete radial structure.**
5. **Whole-representation comparisons are descriptive post-selection sensitivity analyses, not confirmatory reselection evidence.**
6. **Detectable nonlinear structure does not by itself establish nonlinear latent-model advantage.**
7. **Latent localization is mathematical and does not establish semantic garment-part disentanglement.**
8. **The contribution is the controlled representation audit plus evidence-controlled allocation of representation complexity, not a new Fourier transform, normalization method, DCT, wavelet, PCA method, or nonlinear encoder.**

## Closure

Status:

`REVIEWER_PROOFING_RECONCILIATION_COMPLETE`

No scientific reopening was required.

The next required artifact is the final submission audit covering citations, references, figures, tables, cross-references, duplicate text, stale internal labels, placeholders, numerical consistency, and claim-boundary consistency.


## Audit correction recorded after v1.0

The final mechanical audit detected that the earlier standalone references derivative v1.1 omitted one bibliography entry, **An & Li (2014)**, even though the manuscript bibliography itself was complete. This was a reference-extraction artifact only; no manuscript scientific content was affected.

A corrected standalone references derivative was therefore created:

`P2_14_REFERENCES_FINAL_v1_2.md`

It contains 27 entries and matches the manuscript bibliography exactly.

Current reviewer-proofed manuscript SHA-256:

`3af5ca3baa9331f2227d2c121f13efb7f60046d3769c899383b1e7a4133ee870`

Current synchronized references SHA-256:

`b9d45a68a506fdd1d1a7db8eb8d1d403bcd18bc408fa204537dfc9b30bc48b81`

This correction preserves the frozen historical artifacts and does not alter any experiment, numerical result, model/representation selection, figure, or scientific claim.
