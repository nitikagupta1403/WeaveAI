# CLO-SKET — Image and Vision Computing Submission Package

## Canonical manuscript sources

The submission manuscript is assembled from the following seven canonical scientific section files, in this order:

1. `CLO_SKET_IVC_Abstract.md`
2. `CLO_SKET_IVC_Introduction.md`
3. `CLO_SKET_IVC_Related_Work.md`
4. `CLO_SKET_IVC_Methods.md`
5. `CLO_SKET_IVC_Results.md`
6. `CLO_SKET_IVC_Discussion.md`
7. `CLO_SKET_IVC_Conclusion.md`

The standalone `CLO_SKET_IVC_*_Experiment_07.md` fragments are retained for provenance and historical comparison only and are not assembler inputs. `CLO_SKET_IVC_References.md` is appended separately from the canonical bibliography data in `CLO_SKET_References.bib`.

Canonical bibliography data: `CLO_SKET_References.bib`. Submission-formatted references: `CLO_SKET_IVC_References.md`.

## Deterministic assembly

From the repository root, run:

```bash
python papers/CLO-SKET/assemble_ivc_manuscript.py
```

This writes:

`papers/CLO-SKET/CLO_SKET_IVC_Manuscript.md`

The generated master must not become an independent scientific source. Scientific edits belong in the canonical section files above; rebuild the master after any approved change.

## Figure package

The active artwork directory is `papers/CLO-SKET/figures/`.

The main manuscript uses three figures:

1. `Figure_1_Radial_Angular_Construction.png`
2. `Figure_2_Provenance_Locked_14D_Representation.png`
3. `Figure_3_Rigid_Rotation_Control.png`

The Supplementary Material uses six figures, numbered independently as S1–S6:

- S1 → `Figure_1_Radial_Angular_Construction.png`
- S2 → `Figure_2_Provenance_Locked_14D_Representation.png`
- S3 → `Figure_3_Rigid_Rotation_Control.png`
- S4 → `Figure_4_Identity_Disjoint_Reconstruction_Validation.png`
- S5 → `Figure_5_Garment_Identity_Inference.png`
- S6 → `Figure_6_Bootstrap_Permutation_Inference.png`

The shared files for S1–S3 intentionally reuse the corresponding main-manuscript artwork; supplementary numbering refers to their placement in the Supplementary Material rather than to separate image files.

## Submission extras

`CLO_SKET_IVC_Highlights.md` contains the five journal Highlights for separate upload. Each bullet is constrained to the current manuscript claim boundaries and to the Elsevier 85-character limit.

No graphical abstract is included in the current submission package.

## Reproducibility package

Code is maintained under `papers/CLO-SKET/Codes_paper_I/`. The code README and `CLO_SKET_Availability_and_Reproducibility.md` define the intended execution and reproducibility boundary.

## Confirmed front/back matter

The generated manuscript contains the confirmed single-author identity, independent-researcher affiliation, corresponding-author email, funding statement, competing-interest declaration, CRediT roles, acknowledgements, ethics statement, and transparent ChatGPT/Codex writing-assistance disclosure.

## Submission freeze rule

The scientific body, numerical results, figure numbering, identity-aware inference design, rotation-control interpretation, and manuscript claim boundaries are treated as frozen. Journal-formatting edits may alter presentation but must not silently change scientific meaning.
