# Experiment 08 Post-Outcome Predictive Controls — Structural Clarification

**Date:** 2026-08-27
**Scope:** Paper I / CLO-SKET / Experiment 08
**Status:** Prospective clarification committed before control implementation or execution

## Purpose

The post-outcome predictive-controls amendment committed as `6e62d94` prespecified:

1. a correspondence-permutation control; and
2. a repeated identity-grouped partition control.

Before implementation, a structural audit identified unequal garment-identity block sizes in the already-frozen corrected Experiment 08 identity map.

This clarification resolves the resulting implementation ambiguity prospectively, before either control runner is implemented or executed.

No predictive outcome from either control has been computed or inspected.

---

## 1. Frozen structural fact

The corrected Experiment 08 map contains:

- 2,300 rows;
- 230 garment identities;
- 23 categories.

Identity row counts are:

- 228 identities with 10 rows;
- 1 identity with 9 rows;
- 1 identity with 11 rows.

The two non-modal identities are:

- `Jumpsuit__G02`: 9 rows;
- `Jumpsuit__G06`: 11 rows.

This imbalance is not introduced by the present analysis.

It is explicitly preserved in the pre-outcome identity-audit artifact:

`papers/CLO-SKET/Codes_paper_I/Experiment_08/experiment08_identity_overrides.json`

which records that the Jumpsuit 9/11 imbalance was retained because the available drawings visually support their existing garment-identity assignments and no reassignment was supported.

The frozen authoritative mapping must not be altered to force equal block sizes.

---

## 2. Clarified correspondence-permutation rule

The original correspondence-permutation design requires complete garment-identity RA14 blocks to be reassigned without dropping, duplicating, interpolating, or inventing row correspondences.

Because identity blocks have unequal sizes, permutation eligibility is therefore restricted to identities sharing both:

1. the same garment category; and
2. the same identity-block row count.

The permutation strata are thus defined by:

`(category, identity_block_size)`

### Permutation operation

For each of the 1,000 permutations:

- use the frozen seed sequence generated from master seed `20260822`;
- construct identity strata using `(category, identity_block_size)`;
- permute complete RA14 identity blocks only within their stratum;
- preserve the complete block every time it is reassigned;
- preserve the authoritative within-identity row order;
- define within-identity row order as ascending authoritative row index;
- write the reassigned RA14 block into the destination identity rows in that same order;
- leave DINOv2 features, labels, authoritative rows, and frozen fold assignments unchanged.

No row-level independent shuffling is permitted.

No block may be truncated.

No row may be duplicated.

No interpolation or nearest-neighbour matching is permitted.

No outcome-dependent matching rule is permitted.

### Singleton strata

A stratum containing only one garment identity cannot be permuted.

Such an identity remains fixed.

Under the frozen corrected Experiment 08 map:

- `Jumpsuit__G02` is the only 9-row Jumpsuit identity and remains structurally fixed;
- `Jumpsuit__G06` is the only 11-row Jumpsuit identity and remains structurally fixed.

All other identities belong to strata containing at least two identities and are eligible for permutation.

Therefore the structural counts are:

- permutation-eligible identities: `228`;
- structurally fixed identities: `2`.

These counts must be verified by the runner before any predictive computation.

### Per-permutation audit fields

For every permutation, record at minimum:

- permutation index;
- master seed;
- number of permutation-eligible identities;
- number of structurally fixed identities;
- number of identities actually reassigned to a different source identity;
- confirmation that all 2,300 destination rows were filled exactly once;
- confirmation that category was preserved;
- confirmation that block size was preserved;
- confirmation that the two singleton strata remained fixed.

A random permutation may contain ordinary permutation fixed points among otherwise eligible identities. Therefore:

`actually_reassigned_identities`

may be smaller than `228`.

This is distinct from the two identities that are structurally fixed because no same-size partner exists.

### Interpretation

The resulting correspondence permutation is a deliberately conservative control.

It destroys RA14 garment-identity correspondence wherever an exact whole-block permutation is mathematically defined while retaining the two unequal-sized singleton identity blocks unchanged.

Any interpretation must explicitly acknowledge that complete correspondence destruction is impossible for those two identities without altering the frozen data structure.

The test therefore evaluates dependence on correspondence among the permutation-eligible identity population and must not be described as a complete permutation of all 230 identities.

---

## 3. Clarified repeated grouped-partition algorithm

The 20 repeated grouped partitions will use exactly:

`sklearn.model_selection.StratifiedGroupKFold`

with:

- `n_splits=5`;
- `shuffle=True`;
- `random_state=seed`;
- stratification label `y = category`;
- grouping variable `groups = garment_id`.

Seeds remain exactly:

`20260823` through `20260842`, inclusive.

For each seed, call the same algorithm once and retain the generated partition without outcome-dependent acceptance, rejection, rerunning, or optimization.

### Required structural verification

Before fitting any model for a repeated partition, verify that:

- all 2,300 rows receive exactly one test-fold assignment;
- all 230 garment identities occur in exactly one test fold;
- no garment identity spans multiple folds;
- every train/test split has zero garment-identity overlap;
- exactly five folds are produced;
- all 23 categories are represented in the complete dataset;
- no partition is selected or discarded based on predictive performance.

The unequal 9/11 Jumpsuit identity sizes remain unchanged.

No balancing operation may split, duplicate, drop, or reassign rows between garment identities.

The grouped-stratification algorithm is used as generated for the specified seed; no manual post-hoc fold repair based on predictive outcomes is permitted.

---

## 4. Chronology and status

This clarification must be committed before implementation of either control runner.

Execution remains prohibited until the corresponding implementation has itself been committed.

The scientific status established by earlier Experiment 08 records remains unchanged:

- frozen RA14 mechanical-validity gate: FAIL;
- Experiment 08: EXPLORATORY / POST-OUTCOME;
- corrected compactness non-inferiority: FALSE;
- confirmatory RA14 claim permitted: NO.

This clarification resolves only implementation ambiguity in the two already-authorized exploratory controls.

It does not authorize any additional predictive analysis.
