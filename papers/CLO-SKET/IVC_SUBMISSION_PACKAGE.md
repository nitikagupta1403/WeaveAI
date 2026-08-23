# CLO-SKET — Image and Vision Computing Submission Package

## Canonical manuscript sources

The submission manuscript is assembled from the following frozen scientific sources, in this order:

1. `CLO_SKET_Final_Abstract.md`
2. `CLO_SKET_Final_Introduction.md`
3. `CLO_SKET_Final_Related_Work.md`
4. `CLO_SKET_Final_Methods.md`
5. `CLO_SKET_Final_Results.md`
6. `CLO_SKET_Final_Discussion.md`
7. `CLO_SKET_Final_Conclusion.md`
8. `CLO_SKET_Availability_and_Reproducibility.md`

Canonical bibliography: `CLO_SKET_References.bib`.

## Deterministic assembly

From the repository root, run:

```bash
python papers/CLO-SKET/assemble_ivc_manuscript.py
```

This writes:

`papers/CLO-SKET/CLO_SKET_IVC_Manuscript.md`

The generated master must not become an independent scientific source. Scientific edits belong in the canonical section files above; rebuild the master after any approved change.

## Figure package

The final manuscript figure directory is `papers/CLO-SKET/figures/` and uses the locked sequence:

1. `Figure_1_Radial_Angular_Construction.png`
2. `Figure_2_Provenance_Locked_14D_Representation.png`
3. `Figure_3_Rigid_Rotation_Control.png`
4. `Figure_4_Identity_Disjoint_Reconstruction_Validation.png`
5. `Figure_5_Garment_Identity_Inference.png`
6. `Figure_6_Bootstrap_Permutation_Inference.png`

## Reproducibility package

Code is maintained under `papers/CLO-SKET/Codes_paper_I/`. The code README and `CLO_SKET_Availability_and_Reproducibility.md` define the intended execution and reproducibility boundary.

## Front/back matter still requiring author confirmation

Before journal upload, complete only with verified information:

- final title;
- complete author list and order;
- affiliations;
- corresponding-author email/address;
- funding statement;
- competing-interests declaration;
- CRediT author contributions;
- acknowledgements, if applicable;
- any journal-required ethics declaration, if applicable.

Do not infer or fabricate these fields.

## Submission freeze rule

The scientific body, numerical results, figure numbering, identity-aware inference design, rotation-control interpretation, and manuscript claim boundaries are treated as frozen. Journal-formatting edits may alter presentation but must not silently change scientific meaning.
