# Experiment 06 Corrective Reanalysis

This directory contains the prospective corrective workflow for CLO-SKET Paper I Experiment 06.

The audited submission candidate at commit `60063623eedde05ed7c351c3c947a605f6be5344` is immutable historical provenance. Corrective work occurs only on the dedicated corrective lineage.

## Governance order

1. Freeze the prospective corrective protocol.
2. Build and verify the corrected 2,300-row identity/fold map.
3. Complete and freeze annotation-control artifacts for all 2,300 images.
4. Freeze the executable feature-generation/model-fitting pipeline and environment.
5. Commit a machine-generated pre-outcome checkpoint stating that no corrected predictive outcome has been computed.
6. Only then compute the prespecified RAW diagnostic and CLEAN confirmatory Experiment-06 outcomes.

## Phase 1A — corrected identity map

Run from the repository root:

```bash
python papers/CLO-SKET/Codes_paper_I/Experiment_06_Corrective/01_build_corrected_identity_map.py
```

The script reads only:

- `papers/CLO-SKET/evidence/Experiment_07/experiment07_row_map.csv`
- `papers/CLO-SKET/Codes_paper_I/Experiment_08/experiment08_identity_overrides.json`

It applies only the authoritative pre-outcome identity overrides already deposited by Experiment 08. It performs no heuristic identity reassignment and no predictive analysis.

Expected outputs are written to `papers/CLO-SKET/evidence/Experiment_06_Corrective/`:

- `experiment06_corrected_identity_map.csv` — complete 2,300-row historical/corrected map;
- `experiment06_corrected_identity_fold_map.csv` — corrected identity-level fold map;
- `experiment06_corrected_fold_summary.csv` — fold-level row/identity counts and overlap check;
- `experiment06_identity_preflight.json` — hashes, invariant checks, and explicit pre-outcome stop statement.

The preflight fails rather than silently proceeding if any locked invariant is violated, including row count, identity count, category balance, corrected-identity fold integrity, declared override consistency, or zero corrected train/test identity overlap.

## Critical stop rule

A successful Phase-1A identity preflight does **not** authorize corrected Experiment-06 outcome computation. Annotation-control artifacts and the remaining pre-outcome implementation/environment checkpoint must still be completed and committed first.
