# Experiment 08 Post-Outcome Predictive Controls Amendment

**Date:** 2026-08-27
**Scope:** Paper I / CLO-SKET / Experiment 08
**Status:** Prospective specification for post-outcome exploratory controls only

## Scientific boundary

Experiment 08 has already failed its frozen RA14 mechanical-validity gate.

Accordingly, the analyses authorized by this amendment are exploratory/post-outcome controls only. They cannot restore confirmatory status, rescue the failed mechanical gate, establish validated RA14 performance, or revise any previously frozen decision threshold.

This amendment authorizes exactly two additional controls:

1. correspondence permutation control;
2. repeated identity-grouped partition control.

No other predictive analysis is authorized.

---

## 1. Correspondence permutation control

### Purpose

The existing Experiment 08 runners verify deterministic row correspondence between authoritative rows, RA14 rows, and DINOv2 rows.

That structural correspondence check is necessary but does not test whether the observed RA14 predictive result depends on correct garment-to-feature correspondence.

This control will deliberately destroy RA14-to-garment correspondence while preserving the predictive pipeline.

### Frozen null operation

Within each category, complete recovered garment identities will be permuted.

For each permutation:

- the garment identity is the resampling/permutation unit;
- all rows belonging to a garment identity remain together;
- RA14 feature blocks are reassigned only among identities within the same category;
- DINOv2 features, labels, fold assignments, and authoritative row order remain unchanged;
- no row-level independent shuffling is permitted;
- no train/test information may be used to select the permutation.

This preserves category composition and within-identity row structure while destroying garment-specific RA14 correspondence.

### Primary estimand

The primary statistic is the pooled out-of-fold macro-F1 difference

`Delta_G|L = F1(L+G) - F1(L)`

computed using the same frozen classifier family, identity-disjoint folds, preprocessing rules, and fold-local fitting used in the original primary comparison.

### Permutation reference distribution

Number of permutations:

`1000`

Seed:

`20260822`

For each permutation, compute the full pooled out-of-fold primary statistic after applying the frozen correspondence-breaking operation.

The observed exploratory statistic is compared with the permutation distribution.

### Reporting

Report:

- observed `Delta_G|L`;
- number of permutations;
- seed;
- permutation mean;
- permutation median;
- permutation 2.5th and 97.5th percentiles;
- empirical upper-tail probability

`p_perm = (1 + count(T_perm >= T_obs)) / (1 + B)`

where `B = 1000`.

The empirical probability is descriptive/exploratory and must not be described as restoring confirmatory significance.

### Integrity rules

The control must verify before computing outcomes that:

- all 2,300 rows are present;
- all 230 garment identities are present;
- all 23 categories are present;
- original identity-disjoint fold assignments remain unchanged;
- permuted RA14 identity blocks stay within category;
- each identity block is used exactly once per permutation;
- no RA14 row is independently shuffled outside its complete identity block;
- DINOv2 correspondence is unchanged.

---

## 2. Repeated identity-grouped partition control

### Purpose

The frozen five-fold partition is retained as the canonical Experiment 08 partition.

This control evaluates whether the exploratory predictive contrast is unusually dependent on that single frozen identity partition.

It does not replace or average away the canonical frozen result.

### Partition generation

Generate:

`20`

additional five-fold identity-grouped partitions.

Seeds:

`20260823` through `20260842`, inclusive.

For every repeat:

- garment identity is the grouping unit;
- all rows from one garment identity must remain in exactly one fold;
- identities must not cross train/test boundaries;
- all 230 identities must appear exactly once in test across the five folds;
- category balance should be maintained deterministically as closely as possible using a prespecified grouped stratification procedure;
- the same partition-generation algorithm must be used for all 20 seeds;
- no generated partition may be accepted or rejected based on predictive outcomes.

### Representations

Evaluate only the already-defined primary representations:

- `L` = frozen DINOv2 representation;
- `G` = frozen RA14 representation;
- `L+G` = concatenated representation.

No new feature representation is authorized.

### Pipeline

For every repeat and fold:

- fit StandardScaler on training rows only where applicable;
- fit the frozen LogisticRegression specification on training rows only;
- apply fitted transformations/models to held-out rows only;
- preserve identity grouping;
- compute pooled out-of-fold predictions over all 2,300 rows.

No hyperparameter tuning is permitted.

### Primary statistic

For each repeated partition compute:

`Delta_G|L = F1(L+G) - F1(L)`

using pooled out-of-fold macro-F1.

### Secondary descriptive statistic

Also compute the corresponding pooled out-of-fold balanced-accuracy difference.

This secondary result is descriptive only.

### Reporting

Across the 20 repeated partitions report:

- all 20 primary `Delta_G|L` values;
- mean;
- median;
- minimum;
- maximum;
- standard deviation;
- 2.5th and 97.5th empirical percentiles;
- number of repeats with positive `Delta_G|L`;
- all 20 balanced-accuracy differences.

The original frozen five-fold result must be reported separately and must not be replaced by the repeated-partition average.

No threshold for success/failure is introduced.

---

## 3. Shared frozen model specification

The two controls must use the existing Experiment 08 predictive specification without modification:

- identity-disjoint evaluation;
- pooled out-of-fold macro-F1 as the primary metric;
- pooled out-of-fold balanced accuracy as secondary;
- training-fold-only fitting of scaling and any dimensionality transformation;
- frozen LogisticRegression family and hyperparameters;
- frozen representations and feature bytes;
- frozen label definitions;
- frozen authoritative row mapping.

No hyperparameter tuning, representation selection, threshold selection, sample filtering, or outcome-dependent branching is permitted.

---

## 4. Output files

The controls must write distinct evidence files and must not overwrite historical outputs.

Correspondence permutation outputs:

`papers/CLO-SKET/evidence/Experiment_08/experiment08_correspondence_permutation.csv`

`papers/CLO-SKET/evidence/Experiment_08/experiment08_correspondence_permutation_summary.json`

Repeated-partition outputs:

`papers/CLO-SKET/evidence/Experiment_08/experiment08_repeated_grouped_partitions.csv`

`papers/CLO-SKET/evidence/Experiment_08/experiment08_repeated_grouped_partitions_summary.json`

Each summary must record:

- amendment path;
- amendment commit;
- execution code commit;
- seeds;
- representation definitions;
- metric definitions;
- row count;
- garment-identity count;
- category count;
- output SHA-256 values where practical;
- explicit status `POST_OUTCOME_EXPLORATORY_ONLY`.

---

## 5. Chronology rule

This amendment must be committed before:

- implementation of either new control is committed;
- either control is executed;
- any outcome from either control is inspected.

Implementation may occur only after this amendment commit exists.

Execution may occur only after the implementation commit exists.

If an attempted execution fails before producing interpretable outcomes, that chronology must be recorded before retrying if the failure affects analysis logic or provenance.

---

## 6. Interpretation rule

These controls may be used only to characterize robustness and correspondence dependence of already-computed exploratory Experiment 08 results.

They may not be used to claim:

- restoration of RA14 mechanical validity;
- confirmatory additive value;
- confirmatory significance;
- validated garment-instance specificity;
- validated compactness;
- non-inferiority.

Null, weak, unstable, or adverse results must be retained and reported.

---

## 7. Original-result preservation

The following remain unchanged:

- frozen mechanical gate: FAIL;
- original primary exploratory point estimate;
- corrected compactness bootstrap result;
- corrected compactness non-inferiority result: FALSE;
- Experiment 08 overall status: EXPLORATORY / POST-OUTCOME.

No result produced under this amendment can alter those statuses.

---

## Authorization boundary

This amendment authorizes only:

1. the correspondence permutation control defined above;
2. the repeated identity-grouped partition control defined above.

Any additional predictive control or revised analysis requires another prospective amendment committed before implementation or execution.
