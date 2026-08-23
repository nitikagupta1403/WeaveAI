# CLO-SK Benchmark Analysis — Complete Summary

## Paper I — Learning the Semantic Language of Fashion Sketches

---

## 1. Purpose

This document consolidates the complete benchmark analysis performed on
the CLO-SK garment-sketch corpus.

The benchmark was designed to evaluate whether frozen symbolic primitives
and their derived representations capture structured information in
fashion sketches.

The analysis evaluates:

- representation integrity
- geometric representation
- primitive sequences
- family sequences
- primitive sets
- identity consistency
- category information
- cross-sketcher retrieval
- sequence diversity and collisions
- primitive assignment stability
- primitive–geometry associations
- primitive morphology profiles

No representation-learning or prototype optimization was performed during
the benchmark analysis.

The primitive vocabulary remained frozen throughout the analysis.

---

# 2. Benchmark Population

The final locked benchmark contains:

| Property | Value |
|---|---:|
| Images | **2,299** |
| Garment identities | **230** |
| Categories | **23** |
| Sketchers | **12** |
| Transferred events | **12,024** |
| Frozen primitives | **12** |
| Frozen primitive families | **4** |

### Sketches per garment identity

| Number of sketches | Identities |
|---:|---:|
| 9 | 4 |
| 10 | 223 |
| 11 | 3 |

Every benchmark image has a valid identity, category, sketcher, primitive
sequence, and family sequence.

---

# 3. Representation Construction

The representation construction was independently verified.

### Integrity results

- 2,299 / 2,299 image representations constructed
- 230 / 230 identities represented
- 23 / 23 categories represented
- 2,299 / 2,299 primitive sequences present
- 2,299 / 2,299 family sequences present
- No missing primitive sequences
- No missing family sequences

### Event consistency

Total transferred events:

**12,024**

Total primitive sequence elements:

**12,024**

Total family sequence elements:

**12,024**

Therefore:

> Every primitive sequence and every family sequence has exactly the same
> number of elements as its corresponding event count.

Primitive-length mismatch:

**0**

Family-length mismatch:

**0**

This establishes that the sequence representations are complete with
respect to the transferred event stream.

---

# 4. Sequence Length Distribution

Primitive sequence lengths:

| Statistic | Value |
|---|---:|
| Mean | 5.230 |
| Median | 4 |
| Standard deviation | 3.062 |
| Minimum | 1 |
| Maximum | 23 |

Family sequence lengths have the same distribution because each primitive
has exactly one corresponding family assignment.

Thus:

> Primitive and family sequences preserve the full event count of every
> benchmark image.

---

# 5. Raw Geometry Representation

A raw geometry signature was constructed independently for all 2,299
benchmark images.

### Verification

- Expected images: 2,299
- Signatures constructed: 2,299
- Failures: 0
- All keys represented: Yes

Raw signature length:

| Statistic | Value |
|---|---:|
| Mean | 609.04 |
| Median | 646 |
| Standard deviation | 258.50 |
| Minimum | 113 |
| Maximum | 1,466 |

The raw geometry representation was therefore locked before retrieval
evaluation.

---

# 6. Retrieval Benchmark

The first retrieval benchmark compared three representations:

1. Raw geometry
2. Primitive sequence
3. Family sequence

A later cross-sketcher benchmark additionally evaluated:

4. Primitive set

The benchmark used:

- 2,299 query images
- 2,299 benchmark images
- 2,298 candidates per query in the unrestricted retrieval population
- cross-sketcher retrieval with same-sketcher candidates excluded

The retrieval metrics were:

- Recall@1
- Recall@5
- Recall@10
- Recall@20
- Mean Reciprocal Rank (MRR)

---

# 7. Overall Retrieval Results

## 7.1 Unrestricted retrieval

| Representation | R@1 | R@5 | R@10 | R@20 | MRR |
|---|---:|---:|---:|---:|---:|
| Raw geometry | **0.174859** | **0.355372** | **0.470639** | **0.597651** | **0.269714** |
| Primitive sequence | 0.019574 | 0.076120 | 0.115702 | 0.201827 | 0.058956 |
| Family sequence | 0.013049 | 0.053502 | 0.086559 | 0.158765 | 0.045531 |

Raw geometry substantially outperformed the symbolic representations.

---

# 8. Cross-Sketcher Retrieval Population

A separate cross-sketcher population was constructed to test whether
representations generalize across different sketchers.

### Population

- Images: **2,299**
- Identities: **230**
- Sketchers: **12**

Every query had at least one positive cross-sketcher candidate.

### Cross-sketcher positive candidates

| Statistic | Value |
|---|---:|
| Mean | 8.995 |
| Minimum | 8 |
| Maximum | 10 |

Queries with zero cross-sketcher positives:

**0**

The cross-sketcher population was therefore locked before ranking.

---

# 9. Cross-Sketcher Retrieval Results

The final four-way comparison was:

| Representation | R@1 | R@5 | R@10 | R@20 | MRR |
|---|---:|---:|---:|---:|---:|
| Raw geometry | **0.190953** | **0.387125** | **0.505002** | **0.628969** | **0.291916** |
| Primitive sequence | 0.023054 | 0.081340 | 0.137016 | 0.232710 | 0.065499 |
| Primitive set | 0.019139 | 0.069161 | 0.114833 | 0.217051 | 0.059156 |
| Family sequence | 0.016094 | 0.059591 | 0.097869 | 0.172684 | 0.050616 |

### Interpretation

Raw geometry provides the strongest retrieval performance.

Primitive sequence, primitive set, and family sequence all perform
substantially worse for sketch-level retrieval.

Therefore:

> The symbolic representation does not preserve all of the visual
> information required for strong image-level retrieval.

This is an important negative result and should be retained in the
scientific interpretation.

---

# 10. Sequence Diversity

Primitive and family sequence diversity were evaluated independently.

### Primitive sequences

- Total images: 2,299
- Unique primitive sequences: **1,463**
- Uniqueness fraction: **0.636**

### Family sequences

- Unique family sequences: **773**
- Uniqueness fraction: **0.336**

Thus, primitive sequences retain considerably more variation than family
sequences.

---

# 11. Sequence Collapse

Primitive sequences occurring more than once:

**163**

Family sequences occurring more than once:

**199**

Examples of frequently repeated primitive sequences included:

- `(2, 6)` — 131 occurrences
- `(1, 6)` — 88
- `(2, 10)` — 69
- `(2, 11)` — 59
- `(1, 10)` — 49

Frequently repeated family sequences included:

- `('A', 'A')` — 132
- `('B', 'A')` — 119
- `('A', 'C')` — 119
- `('A', 'B')` — 95
- `('B', 'B')` — 79

This demonstrates that the symbolic representation is not an image
identifier. Multiple images share the same symbolic patterns.

---

# 12. Within-Identity Consistency

Primitive and family representations were evaluated for consistency
within each garment identity.

## Primitive sequence consistency

Mean modal-sequence fraction:

**0.169640**

Median:

**0.100000**

Maximum:

**0.700000**

## Family sequence consistency

Mean modal-sequence fraction:

**0.207466**

Median:

**0.200000**

Maximum:

**0.700000**

No garment identity had all of its sketches represented by a single
primitive sequence.

No garment identity had all of its sketches represented by a single
family sequence.

Therefore:

> Symbolic representations show some regularity within garment identity,
> but they are not invariant across all sketches of the same garment.

---

# 13. Cross-Identity Sequence Collisions

Primitive sequences shared by more than one garment identity:

**160**

Family sequences shared by more than one garment identity:

**198**

This further demonstrates that symbolic sequences are not unique garment
identifiers.

The representation contains reusable patterns across identities.

---

# 14. Primitive-Set Stability

Primitive-set similarity was evaluated using Jaccard similarity.

## Within identity

Mean Jaccard:

**0.326304**

Median:

**0.333333**

## Between identity

Mean Jaccard:

**0.240908**

Median:

**0.222222**

### Separation

Mean within-between difference:

**0.085396**

Thus:

> Sketches belonging to the same garment identity have greater primitive-set
> similarity on average than sketches belonging to different identities.

However, the separation is modest.

This supports identity-associated regularity without demonstrating
identity-specific symbolic invariance.

---

# 15. Primitive Assignment Stability

Within-identity and between-identity primitive-set comparisons were based
on:

- 2,299 image representations
- 10,340 within-identity pairs
- 10,340 between-identity pairs

No empty primitive sets were present.

The result provides evidence of modest identity-associated primitive
stability while retaining substantial overlap between identities.

---

# 16. Category Information

Primitive-frequency representations were evaluated for category prediction.

The benchmark contained:

**23 categories**

Observed accuracy:

**9.13%**

Uniform 23-category baseline:

**4.35%**

Observed accuracy was approximately:

**2.1 × the uniform baseline**

Therefore:

> Primitive usage contains category-associated information above the
> uniform baseline.

However, the accuracy remains low in absolute terms.

The result should therefore be interpreted as evidence of category-related
information rather than strong category classification.

---

# 17. Primitive–Independent Geometry Associations

Primitive fractions were tested against independently measured geometry
variables.

The two geometry variables were:

1. `signature_length`
2. `foreground_fraction`

A total of:

**24 association tests**

were performed.

Spearman correlation was used and multiple testing was controlled using
FDR correction.

### Results

FDR-significant associations:

**20 / 24**

Maximum absolute Spearman correlation:

**|rho| = 0.316816**

The strongest association was:

- Primitive: **P3**
- Geometry: **signature_length**
- rho: **0.316816**
- FDR q-value: **2.19 × 10^-53**

Other strong associations included:

- P7 — signature length: rho = 0.307522
- P8 — signature length: rho = 0.294624
- P5 — signature length: rho = 0.248724
- P0 — signature length: rho = 0.224429
- P4 — signature length: rho = 0.219256

Several primitive fractions also showed significant associations with
foreground fraction.

---

# 18. Primitive-Wise Geometry Summary

The strongest geometry association for each primitive was:

| Primitive | Strongest geometry | rho | FDR q |
|---|---|---:|---:|
| P0 | signature length | +0.224 | 5.89e-27 |
| P1 | signature length | -0.045 | 3.90e-02 |
| P2 | signature length | -0.141 | 2.36e-11 |
| P3 | signature length | +0.317 | 2.19e-53 |
| P4 | signature length | +0.219 | 8.04e-26 |
| P5 | signature length | +0.249 | 5.60e-33 |
| P6 | foreground fraction | +0.172 | 3.39e-16 |
| P7 | signature length | +0.308 | 1.81e-50 |
| P8 | signature length | +0.295 | 2.30e-46 |
| P9 | signature length | +0.165 | 4.66e-15 |
| P10 | foreground fraction | +0.037 | 8.87e-02 |
| P11 | signature length | +0.110 | 1.99e-07 |

P10 showed no FDR-significant independent geometry association.

This indicates that geometry associations are primitive-specific rather
than uniform across the entire primitive vocabulary.

---

# 19. Primitive Morphology Profiles

Each primitive was assigned a morphology profile based on its weighted
association with:

- signature length
- foreground fraction

All:

**12 / 12**

primitive profiles were successfully constructed.

### Mean pairwise profile distance

**1.764148**

### Median pairwise profile distance

**1.497015**

### Minimum pairwise profile distance

**0.177459**

### Maximum pairwise profile distance

**4.373113**

The most separated primitive profiles were:

1. P6 vs P7 — 4.373
2. P6 vs P8 — 4.252
3. P4 vs P6 — 4.110
4. P3 vs P6 — 3.885
5. P5 vs P6 — 3.663

Therefore:

> The frozen primitives occupy heterogeneous regions of the measured
> morphology space.

This provides convergent evidence with the primitive–geometry correlation
analysis.

---

# 20. What the Benchmark Demonstrates

The benchmark provides evidence for several properties of the symbolic
representation.

### 20.1 Complete symbolic representation

The full benchmark was represented without missing images, identities,
events, or sequences.

### 20.2 Structured variation

Primitive usage is not uniformly distributed and contains repeated,
reusable patterns.

### 20.3 Category-associated information

Primitive-frequency representations perform above the uniform category
baseline.

### 20.4 Identity-associated regularity

Within-identity primitive-set similarity exceeds between-identity
similarity.

### 20.5 Morphology-associated structure

Primitive usage shows statistically significant associations with
independently measured geometry.

### 20.6 Primitive-specific morphology

Different primitives occupy different morphology-associated profiles.

---

# 21. What the Benchmark Does NOT Demonstrate

The benchmark does **not** establish that:

- each primitive corresponds to a specific human-interpretable garment part;
- primitive P0–P11 have independently validated semantic names;
- the primitive sequence is a complete grammar of fashion sketches;
- symbolic representations preserve complete visual information;
- primitive sequences uniquely identify garments;
- family-level abstraction improves retrieval;
- symbolic representations outperform raw geometry for image retrieval;
- the representation captures human semantic understanding;
- the discovered symbolic system constitutes a complete language.

These claims require additional evidence beyond the current benchmark.

---

# 22. Central Negative Result

The most important limitation is the retrieval comparison.

Raw geometry consistently outperforms symbolic representations.

For cross-sketcher R@1:

- Raw geometry: **19.10%**
- Primitive sequence: **2.31%**
- Primitive set: **1.91%**
- Family sequence: **1.61%**

This indicates that symbolic abstraction discards information that remains
useful for direct image-level retrieval.

This should be treated as an informative scientific result rather than
as a failure of the benchmark.

---

# 23. Convergent Evidence

No single experiment is sufficient to establish structured symbolic
organization.

The evidence instead converges across several independent analyses:

1. Complete primitive representation
2. Above-baseline category information
3. Within-identity primitive-set similarity
4. Cross-identity sequence reuse
5. Primitive–geometry associations
6. Primitive morphology profile separation

The convergence of these analyses provides stronger evidence than any
single metric.

---

# 24. Overall Scientific Interpretation

The benchmark supports the following conservative conclusion:

> **Garment sketches exhibit measurable structured organization that can
> be represented using a finite vocabulary of frozen symbolic primitives.
> These representations contain category-associated information, exhibit
> modest within-identity regularity, and show systematic associations with
> independently measured geometric properties. However, the symbolic
> representations do not preserve the full visual information required
> for strong sketch-level retrieval, and the current benchmark does not
> establish human-interpretable semantics for individual primitives.**

The appropriate scientific interpretation is therefore not that the system
has already learned a complete semantic language of fashion sketches.

Rather:

> **The benchmark provides evidence that garment sketches contain
> computationally measurable symbolic structure whose properties can be
> independently characterized.**

---

# 25. Evidence Boundary for Paper I

## Supported

- Finite primitive vocabulary
- Complete symbolic representation
- Category-associated primitive information
- Modest identity-associated primitive-set regularity
- Primitive-specific morphology associations
- Heterogeneous primitive morphology profiles

## Supported with qualification

- Structured symbolic organization
- Identity-related symbolic regularity
- Morphology-associated primitive organization
- "Semantic language" as a research framework/hypothesis

## Not supported

- Complete fashion-sketch grammar
- Human semantic interpretation of individual primitives
- Unique garment identity from symbolic sequences
- Full preservation of visual information
- Superiority over raw geometry
- Human-level semantic understanding

---

# 26. Final Benchmark Status

| Component | Status |
|---|---|
| Benchmark population | **LOCKED** |
| Representation construction | **LOCKED** |
| Raw geometry signatures | **LOCKED** |
| Retrieval rankings | **LOCKED** |
| Retrieval metrics | **COMPUTED** |
| Cross-sketcher population | **LOCKED** |
| Cross-sketcher rankings | **LOCKED** |
| Cross-sketcher metrics | **COMPUTED** |
| Sequence diagnostics | **COMPUTED** |
| Primitive-set stability | **COMPUTED** |
| Category information | **COMPUTED** |
| Primitive–geometry associations | **COMPUTED** |
| Primitive morphology profiles | **COMPUTED** |
| Evidence consolidation | **LOCKED** |

---

# 27. Final Position

**The benchmark analysis is complete.**

The results should now be treated as a fixed evidence base for Paper I.

No further exploratory benchmark diagnostics are required unless a
specific reviewer question, hypothesis, or paper-writing requirement
identifies a missing analysis.

The next stage is therefore:

> **Evidence → Scientific claims → Figures/Tables → Paper I manuscript**