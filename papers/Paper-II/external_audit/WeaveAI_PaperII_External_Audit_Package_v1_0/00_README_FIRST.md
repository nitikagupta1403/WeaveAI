# WeaveAI Paper II — External Audit Package v1.0

## Goal

Use this package for two independent pre-submission audits:

1. **ChatGPT Deep Research** — literature-backed adversarial review
2. **Gemini** — independent second-opinion audit

Do not ask either reviewer to rewrite the paper first. The first job is to find scientific, statistical, novelty, provenance, reference, and presentation failures.

## Recommended workflow

### Deep Research
Upload this package (or the files inside it) and paste:

`05_prompts/01_DEEP_RESEARCH_EXTERNAL_AUDIT_PROMPT.md`

Also tell it to follow:

`05_prompts/00_COMMON_AUDIT_RUBRIC_AND_OUTPUT_SCHEMA.md`

### Gemini
Upload the same package and paste:

`05_prompts/02_GEMINI_INDEPENDENT_AUDIT_PROMPT.md`

Again require the common rubric.

### After both audits
Bring both outputs back into the WeaveAI master/research-strategy chat and use:

`05_prompts/03_AUDIT_RECONCILIATION_PROMPT.md`

## File hierarchy

- `01_manuscript/` — current assembled manuscript candidate
- `02_figures/` — Figures 1–5, captions, figure-specific claim audits
- `03_frozen_sources/` — frozen manuscript-source/reconciliation layer
- `04_internal_audits/` — prior internal checks; reviewers must challenge them
- `05_prompts/` — audit prompts, rubric, and claim-boundary aid

## Important review instruction

The external reviewers should distinguish:
- frozen project evidence;
- manuscript interpretation;
- reviewer inference;
- independent literature evidence.

Do not permit external reviewers to silently “fix” or recompute frozen results.

## Current scientific hierarchy

representation construction  
→ representation validity  
→ representation selection  
→ latent validation  
→ morphology interpretation

## Package status

This is an **audit package**, not a submission package.
