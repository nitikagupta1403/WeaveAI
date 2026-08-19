# CLO-SKET — Figures and Tables

## Purpose

This document defines the final manuscript figures and tables.

The objective is to present the evidence chain compactly:

    quantitative morphology
            ↓
    morphology organization
            ↓
    radial-angular correspondence
            ↓
    downstream complementarity
            ↓
    controls

Notebook figures are implementation/debugging outputs.

Only figures that communicate a scientific result to the reader should
enter the manuscript.

---

# Figure 1 — CLO-SKET Representation Overview

## Purpose

Introduce the complete computational representation pipeline.

## Content

Show:

    source garment sketch
          ↓
    grayscale / normalization
          ↓
    thresholded binary representation
          ↓
    64 × 64 canonical image
          ↓
    horizontal occupancy (64)
    vertical occupancy (64)
    global descriptors (7)
          ↓
    135-D morphology representation

In parallel:

    same canonical sketch
          ↓
    radial-angular analysis
          ↓
    28-D radial-angular representation

The figure should visually establish that the two branches are
different coordinate descriptions of the same sketch population.

## Important

Do NOT present this as:

    two independent datasets

They originate from the same sketch images.

Use:

    independently constructed representations

---

# Figure 2 — Quantitative Morphology Organization

## Purpose

Demonstrate that the 135-D morphology representation contains
reproducible quantitative organization.

## Recommended panels

### Panel A

PCA projection of morphology observations.

### Panel B

Neighborhood / graph organization.

### Panel C

Density-defined morphology organization.

### Panel D

Permutation-based locality control.

## Message

The morphology representation exhibits reproducible geometric
organization.

## Avoid

Do not label PCA regions as semantic garment classes unless directly
validated.

---

# Figure 3 — Morphology Coordinate Structure

## Purpose

Show that the explicit occupancy representation retains spatial
structure.

## Candidate visualization

Plot the ordered horizontal and vertical occupancy profiles for
representative sketches.

Show:

    sketch image
        +
    horizontal occupancy profile
        +
    vertical occupancy profile.

## Scientific purpose

Make the 135-D representation interpretable to the reader.

This figure answers:

> What does a morphology coordinate actually mean?

---

# Figure 4 — Morphology ↔ Radial–Angular Correspondence

## Purpose

Show the relationship between the two representations.

## Recommended panels

For the four radial-angular targets:

1. F₂ peak magnitude;
2. F₂ peak radius;
3. R₂ at F₂ peak;
4. axial angular error.

Plot:

    observed target
          vs
    cross-validated morphology prediction.

Include the corresponding CV R².

## Important

Predictions must be held-out predictions.

Do not plot in-sample fitted values.

## Message

Morphology contains recoverable information about independently
constructed radial-angular geometry.

---

# Figure 5 — Permutation-Validated Correspondence

## Purpose

Visually demonstrate that the morphology ↔ radial-angular relationship
depends on true sketch-level correspondence.

## Recommended visualization

For each target:

    observed CV R²
          vs
    permutation-null distribution.

Mark the observed value separately.

The null should be described as:

    row-permutation null

not as:

    confidence interval.

## Message

The observed correspondence exceeds the specified permutation null.

## Important

The current analysis uses:

    100 permutations.

Therefore the figure should not visually imply a highly resolved
probability distribution.

---

# Figure 6 — Downstream Complementarity

## Purpose

This is the key performance figure.

## Recommended visualization

Compare:

    morphology-only

against:

    morphology + radial-angular

for:

    Macro-F1
    Balanced Accuracy.

Show:

    morphology-only
          ↓
    morphology + RA

with the absolute improvement.

## Current values

Macro-F1:

    0.341348 → 0.412332
    Δ = +0.070984

Balanced Accuracy:

    0.342609 → 0.415652
    Δ = +0.073043

## Message

The radial-angular representation provides additional task-level
utility beyond morphology.

---

# Figure 7 — Dimension-Matched Control

## Purpose

Address the strongest alternative explanation:

> Does the radial-angular representation help merely because it adds
> more dimensions?

## Visualization

Compare:

    aligned radial-angular addition

against:

    dimension-matched row-permuted addition.

Show the distribution of Δ performance for the null and the observed
aligned improvement.

## Message

The observed improvement is not adequately explained by dimensional
expansion alone under the tested control.

---

# Figure 8 — Descriptor Ablation

## Purpose

Show whether the downstream utility is concentrated in one
radial-angular descriptor block.

## Visualization

Bar plot:

    morphology only
    + F₂ radial
    + α₂
    + observed circular
    + learned circular
    + relational
    + full RA

Use Macro-F1 as the primary metric.

Balanced accuracy may be included as a secondary panel only if needed.

## Current values

| Representation | Macro-F1 |
|---|---:|
| Morphology only | 0.341348 |
| + F₂ radial | 0.374476 |
| + α₂ | 0.356369 |
| + observed circular | 0.358571 |
| + learned circular | 0.366776 |
| + relational | 0.362158 |
| + full RA | 0.412332 |

## Message

The full radial-angular representation provides the largest observed
gain among the tested configurations.

## Claim boundary

Do not say that every block is independently significant.

The ablation is descriptive unless block-specific significance tests
are performed.

---

# Figure 9 — Evidence Chain Summary

## Purpose

Optional conceptual summary figure.

Show:

    135-D morphology
          │
          ├── organization
          │
          ├── association
          │
          └── predicts RA
                    │
                    ↓
             28-D radial-angular
                    │
                    ↓
            downstream improvement
                    │
                    ↓
             dimension-matched
                 control
                    │
                    ↓
              complementarity

## Important

This should be a conceptual evidence diagram, not a statistical
result figure.

---

# Table 1 — Representation Definition

| Representation | Dimensions | Components |
|---|---:|---|
| Morphology | 135 | 64 horizontal + 64 vertical + 7 global |
| Radial-angular | 28 | 9 F₂ radial + 7 α₂ + 3 observed circular + 4 learned circular + 5 relational |
| Combined | 163 | 135 morphology + 28 radial-angular |

This table establishes the representation vocabulary used throughout
the paper.

---

# Table 2 — Morphology Organization Evidence

Summarize the major morphology-space analyses.

Columns:

    Analysis
    Question
    Statistic
    Null / control
    Result
    Interpretation

The table should not list every individual statistical test.

Its purpose is to demonstrate convergence across independent analyses.

---

# Table 3 — Morphology → Radial-Angular Recovery

| Target | CV R² | MAE | RMSE | Spearman ρ |
|---|---:|---:|---:|---:|
| F₂ peak magnitude | 0.2961 | 0.0131 | 0.0171 | 0.6415 |
| F₂ peak radius | 0.0594 | 4.0152 | 5.0096 | 0.3417 |
| R₂ at F₂ peak | 0.2170 | 0.1258 | 0.1599 | 0.5377 |
| Axial angular error | 0.1979 | 20.1515 | 26.4623 | 0.4400 |

This is likely one of the core manuscript tables.

---

# Table 4 — Permutation-Validated Correspondence

| Target | Observed R² | Null mean | Null 95% interval | Empirical p |
|---|---:|---:|---:|---:|
| F₂ peak magnitude | 0.2961 | −0.0965 | [−0.1284, −0.0702] | 0.0099 |
| F₂ peak radius | 0.0594 | −0.0985 | [−0.1324, −0.0699] | 0.0099 |
| R₂ at F₂ peak | 0.2170 | −0.0956 | [−0.1244, −0.0666] | 0.0099 |
| Axial angular error | 0.1979 | −0.0952 | [−0.1309, −0.0622] | 0.0099 |

Caption must state:

    100 permutations, +1 empirical p-value correction.

---

# Table 5 — Downstream Complementarity

| Representation | Macro-F1 | Balanced Accuracy |
|---|---:|---:|
| Morphology only | 0.341348 | 0.342609 |
| Morphology + RA | 0.412332 | 0.415652 |
| Improvement | +0.070984 | +0.073043 |

Add permutation-null information beneath or beside the table:

    Macro-F1 null mean Δ = −0.020368
    Macro-F1 null 95% interval = [−0.031142, −0.010537]
    empirical p = 0.009901

---

# Table 6 — Descriptor Ablation

| Representation | BA | Macro-F1 | Δ Macro-F1 |
|---|---:|---:|---:|
| Morphology only | 0.342609 | 0.341348 | 0 |
| + F₂ radial | 0.377391 | 0.374476 | +0.033128 |
| + α₂ | 0.357391 | 0.356369 | +0.015021 |
| + observed circular | 0.359565 | 0.358571 | +0.017224 |
| + learned circular | 0.368261 | 0.366776 | +0.025428 |
| + relational | 0.364348 | 0.362158 | +0.020810 |
| + full RA | 0.415652 | 0.412332 | +0.070984 |

---

# Table 7 — Evidence Ledger

This may be supplementary rather than main-text material.

| Question | Analysis | Result | Claim boundary |
|---|---|---|---|
| Are representations aligned? | Provenance audit | Exact row-level match | Same-sketch correspondence |
| Are morphology coordinates associated with RA? | Spearman + FDR | Significant associations | Association only |
| Can morphology recover RA? | 5-fold CV | Positive CV R² | Overlap / recoverability |
| Is correspondence non-random? | Row permutation | Observed > null | Correspondence |
| Does RA improve downstream performance? | Complementarity test | Δ Macro-F1 +0.071 | Task-level utility |
| Is gain explained by dimensions alone? | Dimension-matched control | Observed > null | Not dimension count alone |
| Is utility concentrated in one block? | Ablation | Full RA > individual blocks | No concentration in one block |

---

# Main-Text Figure Budget

Recommended main-text figures:

    Figure 1 — Representation pipeline
    Figure 2 — Morphology organization
    Figure 3 — Morphology ↔ RA recovery
    Figure 4 — Permutation correspondence
    Figure 5 — Downstream complementarity + dimension control
    Figure 6 — Descriptor ablation

Everything else can move to Supplementary Material if space becomes
tight.

---

# Main-Text Table Budget

Recommended main-text tables:

    Table 1 — Representation definition
    Table 2 — Morphology organization evidence
    Table 3 — Morphology → RA recovery
    Table 4 — Downstream complementarity

Supplement:

    permutation details
    descriptor ablation
    feature-level association tables
    complete evidence ledger

---

# Figure Design Rules

All manuscript figures must follow these rules:

1. No unnecessary decorative elements.
2. Every axis must have units or an explicit metric.
3. Every abbreviation must be defined in the caption or Methods.
4. Observed values and null distributions must be visually distinct.
5. Do not use PCA plots as evidence of semantic categories.
6. Do not use density-region colors as if they represent known garment
   classes.
7. Do not imply uncertainty intervals when plotting permutation-null
   intervals.
8. All held-out prediction plots must use out-of-sample predictions.
9. Figure captions must state the relevant sample size and
   cross-validation design where applicable.
10. Statistical significance should never substitute for effect size.

---

# Caption Claim Rules

Captions should describe what is shown.

They should not contain unsupported interpretation.

Bad:

> "The radial-angular representation discovers the hidden semantic
> structure of fashion."

Good:

> "Cross-validated morphology predictions of four radial-angular
> quantities. Predictions are generated out-of-sample using five-fold
> cross-validation."

---

# Final Visualization Principle

The reader should be able to reconstruct the scientific argument from
the figures alone:

    explicit morphology
        ↓
    measurable organization
        ↓
    independent geometric description
        ↓
    reproducible correspondence
        ↓
    downstream complementarity
        ↓
    control against dimensional expansion

The figures should make this progression obvious without requiring
the reader to inspect the notebook.