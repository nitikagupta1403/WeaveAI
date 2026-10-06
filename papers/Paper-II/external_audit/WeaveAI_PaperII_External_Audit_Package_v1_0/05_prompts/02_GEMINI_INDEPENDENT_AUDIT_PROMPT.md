# Prompt — Gemini Independent Adversarial Audit

You are the **second independent reviewer** of a research manuscript. Your task is to audit it independently from any ChatGPT/OpenAI review.

The manuscript title is:

**“Auditing and Allocating Representation Complexity in Radial–Spectral Garment Morphology.”**

The uploaded package contains:
- the assembled manuscript;
- Figures 1–5;
- frozen source sections;
- support-dependence reconciliation;
- internal audits;
- a common review rubric.

## Independence rule

Do not defer to or repeat the internal audit conclusions.
Treat every internal “PASS” as an assertion that must be checked.

If your environment has web/scholar browsing, independently verify novelty, citations, and important technical precedent. If browsing is unavailable, clearly label literature conclusions as package-only and do not invent external verification.

## Audit sequence

### 1. Manuscript-only review
Read the assembled manuscript and figures first.

Identify all:
- unsupported claims;
- contradictions;
- statistical concerns;
- leakage risks;
- post-selection interpretation risks;
- missing baselines;
- novelty overclaim;
- numerical inconsistencies;
- figure/table problems;
- unclear denominators;
- wording that sounds stronger than the evidence.

### 2. Source reconciliation
Then compare against the frozen source files.

For each major manuscript claim, ask:
- where exactly is it supported?
- is the same population/design being referenced?
- is an association being turned into causation?
- is a sensitivity analysis being turned into model-selection evidence?
- is a matched control being turned into a retroactive replacement?
- is descriptive localization being turned into semantics?

### 3. Statistical audit
Audit especially:
- 23-category sign-flip exchangeability;
- exact \(2^{23}\) sign-flip enumeration;
- studentized max-T FWER control;
- identity-level bootstrap;
- 5 identity-disjoint folds;
- train-vs-held-out separation;
- multiplicity across compression families;
- nonlinear-model comparison family;
- handling of fold 3;
- post-selection whole-representation comparisons.

### 4. Novelty audit
If browsing is available, search broadly across shape analysis, signal processing, image preprocessing, computer vision, and sketch/fashion retrieval.

The narrow support-dependence novelty question is not:
“Does padding/cropping affect Fourier spectra?”

It is:

> Are there prior studies where object pixels are held fixed while only surrounding 2-D raster support changes, the representation/spectral allocation is recomputed, support dependence is quantified, and an object-relative/intrinsic matched control is used?

Classify each precedent:
DIRECT / CLOSE-PARTIAL / GENERAL THEORY / DIFFERENT.

Do not use absolute-priority language.

### 5. Figure audit
Independently inspect Figures 1–5.

Check:
- schematic vs empirical content;
- exact numerical consistency;
- axis/legend clarity;
- whether visual hierarchy overstates positive results;
- whether Figure 2 makes endpoint response look more monotonic than it is;
- whether Figure 3 visually oversells the hybrid despite RAW42 being nearly tied;
- whether Figure 4 confuses nonlinear structure with model utility;
- whether Figure 5 implies semantics or interaction not formally tested.

### 6. References
Check every citation you can:
- author/year/title;
- relevance to the sentence;
- missing close precedent;
- duplicate or uncited references.

## Critical boundaries to enforce

Flag any violation of these:
- no “new Fourier transform” claim;
- no generic-normalization novelty claim;
- no universal superiority claim;
- no performance-breakthrough framing;
- no claim that support fully explains RAW→CROP;
- no universal monotonicity claim;
- no “padding creates frequency content” language;
- no claim that PCA proves linear morphology;
- no generic inferiority claim for AE/VAE;
- no semantic garment-part interpretation from radial/harmonic bins;
- no first-ever claim.

## Output format

Follow `00_COMMON_AUDIT_RUBRIC_AND_OUTPUT_SCHEMA.md` exactly.

Then add:

### Gemini-specific dissent section
List any place where your conclusion differs from the internal audit files.

### Top 5 reviewer attacks
Write the five strongest objections a skeptical journal reviewer could raise, in order.

### Minimal rebuttal-ready fix
For each of those five attacks, state the smallest defensible manuscript change or additional clarification that would neutralize it without changing frozen results.

Do not praise the work unless the evidence warrants it. This is an adversarial audit, not an editing exercise.
