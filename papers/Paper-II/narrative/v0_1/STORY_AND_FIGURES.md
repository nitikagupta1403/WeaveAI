# Paper II: a simpler story

Editorial draft. Scientific source: v0_7_FINAL_AUDITED at the existing evidence freeze. This folder changes exposition; it does not replace the frozen manuscript or submission package.

## The single thread

**Turn a sketch into a structured description, check what that description measures, and keep only the complexity that the evidence supports.**

The reader should understand the sketch-to-field construction before encountering selection rules, model comparisons, or audit terminology. Every new mathematical object answers a visible question about the same drawing.

## Proposed main-paper structure

1. **Introduction: what should a compact sketch description preserve?** Establish the problem with one sketch. Introduce the three decisions: coordinates, radial detail, latent summary. End with the study's concrete contribution and scope.
2. **From a sketch to a radial–harmonic field.** Define distance and angle around the ink centroid. Unroll the shells into an angular distribution. Show how Fourier modes describe angular variation at each distance. Introduce one symbol at a time. Explain that harmonics describe angular scale, not named garment parts.
3. **Does the surrounding frame change the description?** Show the same pixels inside larger canvases, then the spectral change and object-relative control. Explain the mechanism before the population result. Report the full dataset and category-level inference once. State that this audit followed the original selection study.
4. **How much radial detail should each harmonic band retain?** Describe the historical, already-frozen selection design. Show the selected allocation, its held-out evidence, and coefficient count. Include the competitive uniform RAW42 baseline in the same results display. The outcome is a conditional allocation, not a performance breakthrough.
5. **A compact summary that can be mapped back.** Explain PCA's inverse path to the retained radial–harmonic field. Briefly state that the tested AE/VAE comparisons did not establish an advantage. Show an archived PCA direction only when its exact coefficients and inverse transform are available.
6. **Discussion.** One short synthesis, one focused limitations paragraph, one next-experiment paragraph. Avoid repeating exclusions throughout the paper.

Working prose budget: approximately 5,000–6,000 words excluding references and supplementary methods. This is an editorial target, not a verified journal limit. Keep methods needed to understand or reproduce the central comparison in the main text; move implementation detail, full candidate grids, audit chronology, and extended diagnostics to supplementary material with explicit pointers.

## Figure storyboard

| Figure | Reader's question | Panels and intended message | Evidence/source rule |
|---|---|---|---|
| 1. One sketch, two coordinates | How does a drawing become a harmonic field? | Same drawing → centre, radius and angle → unrolled shell distributions → one shell's angular signal → its harmonic amplitudes → radial–harmonic field. | Prototype supplied here from archived S01, row 781, support 1.0. Deterministic first sentinel, illustrative only. |
| 2. Same sketch, larger frame | Can blank surrounding space change the measurement? | Same archived pixels at support 1 and 3; raster-relative versus object-relative field; paired spectral changes. | Reuse the same S01 across the teaching sequence. Show actual archived controls. Do not present its trajectory as the population result. |
| 3. The effect across garments | Is the example a dataset-wide finding? | Category medians with uncertainty where available; all four bands; low/high-mid/high directional inference distinguished from descriptive mid. | Frozen primary 2,300-sketch audit, category-level joint sign-flip results. No new statistics without a recorded analysis. |
| 4. Where to keep radial detail | Must every angular scale use the same encoding? | Four-band allocation diagram, held-out effects with intervals, coefficient budget, full/hybrid/RAW42 descriptive retrieval comparison. | Historical selected DCT4/raw72/raw72/db4-4; selection chronology and confirmatory versus descriptive endpoints labelled. |
| 5. A latent direction mapped back | What does a compact coordinate change in the representation? | One archived PCA direction → inverse radial–harmonic change → energy localized by radius and harmonic. | Retained-subspace inverse only. No invented garment reconstruction or sleeve/hem interpretation. Await exact archived coefficient provenance before rendering. |

Each caption begins with the visual action and finding. Technical qualifications appear once where they affect reading. Consistent colours mark the same radius or harmonic across panels; no decorative garment-part labels.

## What moves out of the main narrative

- Detailed preprocessing localization, observational frame descriptors, replay checks and complete intervention manifests: supplementary audit methods.
- Candidate family/budget grids, tie rules, full multiplicity details and all latent comparisons: supplementary selection methods and results, with concise main-text methods and decisive results retained.
- Quadratic pairwise relation analysis: supplementary secondary analysis; distinguish detectable nonlinearity from model utility in the main discussion.
- Repository freeze IDs, package chronology and reviewer-objection responses: reproducibility record rather than recurring narrative.

## Claims to preserve exactly

The support audit was later than historical model selection. The object-relative construction is a matched control. The hybrid reduces coefficients by 41.98%; RAW42 is competitive. Unsupported compression in the tested intermediate bands is not proof of incompressibility. No nonlinear superiority or equivalence was established. Inverse localization concerns the retained field, not semantic garment parts or lossless recovery of the original sketch.

## Next editorial pass

After reviewing this opening and Figure 1, write Sections 2–5 against the existing results, build Figures 2–4 from frozen arrays, then assemble a shorter full manuscript. Check every number and inference against the frozen source before producing a new Word/PDF package.
