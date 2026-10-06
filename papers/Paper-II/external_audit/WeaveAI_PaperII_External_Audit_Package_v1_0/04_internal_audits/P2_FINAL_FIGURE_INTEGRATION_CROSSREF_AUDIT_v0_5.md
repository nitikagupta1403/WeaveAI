# Paper II final figure integration and cross-reference audit v0.5

## Decision

**FIGURES 1–5 AND TABLES 1–5 INTEGRATED — CROSS-REFERENCE PASS**

## Figure integration

- In-text figure references present: [1, 2, 3, 4, 5]
- Figure captions present: [1, 2, 3, 4, 5]
- Embedded image references present: [1, 2, 3, 4, 5]
- Figure assets exist: {1: True, 2: True, 3: True, 4: True, 5: True}
- Stale “about here” placeholders: None

## Table integration

- Main table captions present: [1, 2, 3, 4, 5]

## Placement logic

- Figure 1 follows the Methods definition of the radial–angular conditional field and precedes the angular-Fourier formalism.
- Figure 2 follows the controlled same-pixel support-dependence result and precedes the historical representation-selection results.
- Figure 3 follows the band-specific representation-selection and whole-representation sensitivity evidence and precedes nonlinear latent-model validation.
- Figure 4 follows nonlinear latent-model validation and precedes morphology localization.
- Figure 5 follows exact retained-subspace morphology localization and precedes the Results synthesis.

This preserves the governing scientific order:

representation construction → representation validity → representation selection → latent validation → morphology interpretation.

## Submission-facing hygiene

Internal-label counts:
- P2 labels: 0
- 05 audit IDs: 0
- “freeze-ready”: 0

The markdown image links use relative filenames so the manuscript and figure assets can live in the same manuscript/submission directory without local-machine paths.

## Remaining open items

1. Journal-specific formatting remains open.
2. Final copyedit/proofread remains open.
3. If a journal requires figures uploaded separately rather than inline, retain the captions in the manuscript and remove only the image-link lines during submission formatting.
4. No numerical or scientific result was re-estimated in this integration pass.

## SHA-256

Manuscript v0.5: `3283976f0493bdfe3238d6d29c79fc8793e3ddfbb961b56a2b46fa5f3942ba99`
