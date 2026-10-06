# Prompt — Deep Research External Review / Audit

You are performing a **pre-submission adversarial scientific audit** of a research manuscript titled:

**“Auditing and Allocating Representation Complexity in Radial–Spectral Garment Morphology.”**

I have uploaded a package containing:
- the assembled manuscript;
- Figures 1–5;
- frozen manuscript-source sections;
- the support-dependence reconciliation;
- internal audit files;
- a common audit rubric and output schema.

## Your role

Act as a skeptical senior reviewer with expertise spanning:
- shape analysis and Fourier descriptors;
- image/signal representations;
- statistical inference and multiplicity control;
- machine learning evaluation;
- fashion/sketch retrieval;
- reproducibility and scientific claims.

Do **not** trust the internal audits merely because they say PASS. Treat them as material to challenge.

## Work in four phases

### Phase 1 — Blind manuscript review
First read the assembled manuscript and Figures 1–5 as if you were a journal reviewer.

Identify:
- scientific contribution;
- main inferential claims;
- novelty claims;
- weak reasoning;
- unclear conditioning;
- overstatement;
- underpowered or post-hoc analysis;
- missing baselines;
- potential leakage;
- hidden multiple-testing problems;
- figure/table inconsistencies.

Do not use the internal audits to excuse a problem.

### Phase 2 — Frozen-source reconciliation
Then compare the manuscript against the frozen source/reconciliation files.

Audit whether the assembled paper preserves:
- all numerical results;
- the original inferential conditioning;
- the identity-disjoint design;
- association vs controlled-intervention distinctions;
- the support-dependence claim boundary;
- the distinction between the historical raster-relative selection analysis and the later matched object-relative control;
- the PCA-64 denominator for morphology localization;
- the close whole-representation RAW42 baseline.

Flag any manuscript statement that is stronger than its source.

### Phase 3 — Independent Deep Research literature audit
Use current scholarly web research to challenge novelty and precedent.

Search broadly, not only fashion:
- Fourier shape descriptors;
- generic Fourier descriptors;
- angular-radial / polar shape descriptors;
- Zernike / ART / MPEG-7 shape descriptors;
- finite-window Fourier theory;
- cropping and support effects;
- zero-padding;
- digital invariance;
- object-centered / scale-normalized shape coordinates;
- sketch/fashion retrieval;
- representation sensitivity to canvas/raster support;
- same-object / same-pixel support manipulations.

The narrow 05K question is:

> With object pixels held fixed, does changing only surrounding 2-D raster support change a raster-relative radial–angular spectral representation, and does a matched object-relative control remove that dependency?

Do not classify generic scale invariance, cropping, DSP zero-padding, or windowing as a direct precedent unless the intervention genuinely matches.

For every important precedent:
- give full citation;
- link/DOI if available;
- state exactly what was manipulated;
- state whether object pixels were held fixed;
- state whether 2-D raster support changed independently;
- classify DIRECT / CLOSE-PARTIAL / GENERAL THEORY / DIFFERENT;
- explain what it does to the manuscript’s novelty boundary.

Do not conclude “no prior work exists.” Use language such as:
> “I did not locate a direct precedent in the searched literature…”

### Phase 4 — Submission-risk audit
Review:
- title and abstract;
- Introduction/Related Work;
- Methods;
- Results;
- Discussion;
- References;
- Figures 1–5;
- Tables 1–5.

Ask what a hostile reviewer could reasonably attack.

## Critical scientific facts that must be tested for consistency

Do not assume these are correct merely because they are listed; verify against the provided sources:

1. The historical raster-relative representation is support-dependent under the same-pixel support intervention.
2. The matched object-relative control is numerically invariant under that same intervention.
3. 05J is associational; 05K is a controlled intervention.
4. The original representation-selection result remains conditional on the historical raster-relative coordinate system.
5. The heterogeneous hybrid is DCT4 / RAW72 / RAW72 / db4-wavelet4.
6. The hybrid mean MRR is 0.816766 and uniform RAW42 is 0.815896; therefore this is not a performance-breakthrough paper.
7. No multiplicity-controlled AE/VAE advantage over PCA was established.
8. Detectable nonlinear predictive structure is not equivalent to validated nonlinear-model superiority.
9. Morphology localization is conditional on PCA-64, which retains 44.65% of standardized representation variance.
10. The 78.54%, 66.84%, and 51.30% morphology-localization quantities are descriptive within that retained subspace and do not establish semantic garment parts or radial×harmonic interaction.

## Statistical questions you must answer

- Is category-level sign-flip exchangeability defensible here?
- Is the max-T family-wise error procedure described and interpreted correctly?
- Is the identity bootstrap aligned with the sampling unit?
- Is the train-selection / held-out-confirmation separation adequate?
- Are post-selection whole-representation comparisons clearly labeled as sensitivity analyses rather than selection evidence?
- Is the fold-3 anomaly handled scientifically without data exclusion or retroactive tuning?
- Are CIs and p-values used outside the population/design on which they were computed?
- Are negative/null results given equal interpretive weight?

## Output

Follow `00_COMMON_AUDIT_RUBRIC_AND_OUTPUT_SCHEMA.md` exactly.

At the very end add:

### Deep Research search log
Give:
- search themes;
- databases/search engines used;
- important queries;
- date of search;
- papers considered DIRECT, CLOSE/PARTIAL, GENERAL THEORY, and DIFFERENT.

### Final recommendation
Choose one:
- submit as is;
- submit after minor revision;
- major revision before submission;
- do not submit in current form.

Be adversarial, precise, and evidence-based. Do not rewrite the paper merely to make it sound better. The purpose is to find what could still fail peer review.
