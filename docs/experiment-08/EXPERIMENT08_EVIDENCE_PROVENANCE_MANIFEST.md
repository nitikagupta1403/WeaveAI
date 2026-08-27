# Experiment 08 Evidence and Provenance Manifest

## 1. Purpose

This manifest provides the public evidence map for CLO-SKET Experiment 08.

It distinguishes:

1. frozen / pre-outcome inputs and controls;
2. post-outcome exploratory evidence;
3. superseded or invalid historical inference;
4. governance and provenance records.

This classification is part of the scientific record. Files listed as
post-outcome or exploratory must not be interpreted as confirmatory evidence.

---

## 2. Frozen experiment status

Final Experiment 08 scientific status:

- mechanical validity gate: **FAIL**
- Experiment 08 status: **EXPLORATORY / POST-OUTCOME**
- confirmatory RA14 claim permitted: **NO**
- corrected compactness non-inferiority: **FALSE**
- failed mechanical gate restored by later diagnostics: **NO**

The frozen mechanical gate was not reopened or replaced by later analyses.

---

## 3. Frozen / pre-outcome foundations

These artifacts define or preserve inputs, grouping, representations,
environment, or analysis specifications that existed before predictive
outcome interpretation.

### Core implementation and locks

| Artifact | SHA-256 | Role |
|---|---|---|
| `papers/CLO-SKET/Codes_paper_I/Experiment_08/preflight.py` | `00068f0d79dcbd1c304ff4e6edd09e4ead3f66c44e57304d50069c49ea9a72a7` | Authoritative row/fold validation and identity-override application |
| `papers/CLO-SKET/Codes_paper_I/Experiment_08/run_mechanical_validation.py` | `ef4d0f54baa6a6a488da9523f2ef007960e1f7d7cfe15704c74d16ef8732c0db` | Frozen mechanical-validation implementation |
| `papers/CLO-SKET/Codes_paper_I/Experiment_08/run_primary_comparison.py` | `9a51ee3cf58dcaaa5a4a0a4f89d746be81008349c861ee39565c22d060347daf` | Frozen primary predictive-comparison implementation |
| `papers/CLO-SKET/Codes_paper_I/Experiment_08/experiment08_ra14_manifest.json` | `8e6b2cfabcd8724ef18cddd8ed90ab22288dbed34c232bece180f5307d3acd94` | RA14 feature provenance lock |
| `papers/CLO-SKET/Codes_paper_I/Experiment_08/experiment08_dinov2_feature_lock.json` | `c29f45fd827e0507d72014396693386aebd74361aa150c92e90c05f1fedaf4a4` | DINOv2 feature provenance lock |
| `papers/CLO-SKET/Codes_paper_I/Experiment_08/requirements-lock.txt` | `b54435cb17ec38d6b1bde18b6116f996632311961ac94dfdeb8ed2175290a079` | Frozen Python environment lock |

---

## 4. Mechanical-validation evidence

### Frozen gate evidence

| Artifact | SHA-256 |
|---|---|
| `experiment08_mechanical_analytic.csv` | `78a5adbd3411f71411c427f3060ec2e95b21253b150cc4941341968b1fdfae3c` |
| `experiment08_mechanical_validation.csv` | `3a51a9045a70bfcd87ce9a96756385e25db9e0908b854bc66a5a515edf45ca71` |
| `experiment08_mechanical_summary.json` | `f4391a2595bcf6a37fb50d6c597a11065a8d4dcdf9c12d79b58d489ea8b0d74d` |

Interpretation:

- analytic rotation validation passed;
- raster axial-angle validation passed;
- raster harmonic-magnitude P95 criterion failed;
- therefore the frozen overall mechanical gate is **FAIL**.

Passing subcomponents do not override the failed gate.

### Post-outcome mechanical sensitivity diagnostics

| Artifact | SHA-256 |
|---|---|
| `experiment08_mechanical_r2_strata.csv` | `2136923ab6691b12bb9df0ac10ea2c1b144aa51e9f1f0344a508cf5670ecf68b` |
| `experiment08_mechanical_sensitivity_observations.csv` | `047272e1402e43dbb90a11276c7e6811bc9ebce75c41b9f271fff6d775eaa5df` |
| `experiment08_mechanical_sensitivity_regression.csv` | `eef7073fb18c04b2e3b8438294dfcdd0b3194c386b96b443902ad1a4004cf5b3` |
| `experiment08_mechanical_sensitivity_strata.csv` | `a09a4c64a05439a42d973bec56cda40a5329a0a6cf0e3491c57710c799e0ac3e` |
| `experiment08_mechanical_sensitivity_summary.json` | `57287fc30326d6a1f8a1cbbdc60da1a5a2ee95146908a6a374ba67915ddfd719` |

Status:

**POST-OUTCOME DIAGNOSTIC ONLY.**

These files explain sensitivity of raster harmonic magnitude, including
conditioning with respect to low `R2`, but they do not revise, replace,
or rescue the frozen mechanical gate.

---

## 5. Primary predictive evidence

| Artifact | SHA-256 |
|---|---|
| `experiment08_fold_metrics.csv` | `222b75243b1fc67cbc41516ac7eb35cdcb5f56298b485afd308e62c5c637085e` |
| `experiment08_oof_predictions.csv` | `62e3a5608441428f0c0c8ba1b9ade86b5dacbfa37dbe7a6368a58c317c95be49` |
| `experiment08_primary_results.csv` | `1dfc6050df1ecaa11fb108a3f4e0d3d14106000fcb40cff1d9d136c452f302fe` |
| `experiment08_primary_point_estimate.json` | `06d252e9816d9c72340bc858a8f947356f2377e49f6b18fa8037dbb4fae192b9` |
| `experiment08_identity_bootstrap.csv` | `1bf19ce0559bd46fcf4da7e529e6e107ffc57b094cfcc27475b176b289c09077` |
| `experiment08_identity_bootstrap_summary.csv` | `28f32c907ad60844d3e0f2ced361119affb88bc31d573d6aabb8d0aca2e28639` |

Observed frozen-partition primary result:

- `F1(L) = 0.7380200305882273`
- `F1(L+G) = 0.7389666827704796`
- `Delta_G|L = +0.0009466521822523166`

The identity bootstrap for the primary additive comparison is retained as
valid computational evidence.

However, because predictive analysis proceeded after failure of the frozen
mechanical gate, these predictive results are classified as:

**POST-OUTCOME / EXPLORATORY**

and not confirmatory evidence of RA14 validity or additive utility.

---

## 6. Secondary morphology / compactness evidence

Historical secondary morphology evidence remains in the repository for
auditability:

| Artifact | SHA-256 |
|---|---|
| `experiment08_secondary_morphology_fold_metrics.csv` | `7bb10b39d059bde0b36a34529c6881df585320b1ca0f3faaa1654b11c4a135e0` |
| `experiment08_secondary_morphology_oof_predictions.csv` | `12ed9c7d15632d137f06a3dbd575257f5fb4afc7c0d53d5d92572a678f7807af` |
| `experiment08_secondary_morphology_results.csv` | `372ee0113c59135ec593900e684ea049ce09d4b9b7d0f1002852830ce0ebe44c` |
| `experiment08_secondary_morphology_point_estimate.json` | `70f11e02d28853e561d1162b18d5e26175f845787b5bc36ae8f6d35774774c13` |
| `experiment08_secondary_morphology_bootstrap.csv` | `b9c732430735a0bf2d16cee62be234135ae76d167a2e847256d99b93c2ab00cb` |
| `experiment08_secondary_morphology_bootstrap_summary.csv` | `fdd7b0a42916b077f3d4af2a481a250fd9b70d538fa439eef1fae86af6bc1000` |

The historical compactness bootstrap implementation destroyed bootstrap
multiplicity by deduplicating identities sampled with replacement.

Therefore:

- historical compactness bootstrap confidence intervals are **INVALID**;
- historical non-inferiority inference derived from that bootstrap is
  **INVALID / SUPERSEDED**;
- the historical point estimate is not invalidated solely by this bootstrap
  defect.

The corrected multiplicity-preserving implementation is:

`papers/CLO-SKET/Codes_paper_I/Experiment_08/run_compactness_analysis.py`

SHA-256:

`b66f5768d24101ea3d7ca1f7ebc65cde9e9b9ab0ea5a85e563334d687191971b`

Corrected evidence:

| Artifact | SHA-256 |
|---|---|
| `experiment08_compactness_corrected_bootstrap.json` | `9f3ea226255b7516a3591e21189f1c78eec306c0dbb76f732e1b7f1ffbe37b12` |

Corrected result:

- `D_G,L14 = -0.49330945434360446`
- paired 95% bootstrap CI:
  `[-0.5322598503022689, -0.45316390290724373]`
- non-inferiority margin: `-0.02`
- corrected non-inferiority result: **FALSE**

This corrected analysis remains **POST-OUTCOME / EXPLORATORY** and does not
restore mechanical validity or confirmatory status.

Historical implementation chronology includes:

- `e9e4f220c9d036e05a0de88adad1bda94830c87f`
  — first compactness bootstrap multiplicity fix;
- `bce2bb7`
  — retained corrected multiplicity-preserving implementation;
- `41ca373`
  — corrected compactness evidence commit.

---

## 7. Prospectively specified post-outcome predictive controls

These controls were authorized only after Experiment 08 had already become
post-outcome / exploratory.

Chronology:

1. `6e62d94d7a29088f92ec0c6d617bbf265d2810c1`
   — predictive-controls amendment;
2. `7b4b283f0070b67817c71982526b3ed64034be4e`
   — structural clarification;
3. `dcc5a29b4bcfc5b522b6b127d370e9ad92eaacdc`
   — implementation committed before execution;
4. `73eaa1a51dc9840884148b93ec6c2a470953e2af`
   — correspondence evidence;
5. `17c33820f1d79392de24bd02b0dbef7bb12eab68`
   — repeated grouped-partition evidence.

Runner:

`papers/CLO-SKET/Codes_paper_I/Experiment_08/run_post_outcome_predictive_controls.py`

SHA-256:

`3cfe4fa025990f52be6ec04af8e5ba7b55b3ba4914759970d168d331742e2279`

### 7.1 Correspondence permutation control

| Artifact | SHA-256 |
|---|---|
| `experiment08_correspondence_permutation.csv` | `1ff1e76a054ae08a3e0cd8bd8f8fa89514887e134ab65ab452acb1c384ccb049` |
| `experiment08_correspondence_permutation_summary.json` | `bd123a3eb2795712c006a3a9e84dfa69702d228a9de4c5236e833f31a95c4e48` |

Design:

- 1,000 permutations;
- within `(category, identity_block_size)` strata;
- 228 permutation-eligible garment identities;
- 2 structurally fixed unequal-size identities;
- DINOv2, labels, folds, and row order held fixed.

Observed result:

- observed `Delta_G|L = +0.0009466521822523166`
- permutation mean = `+0.013596323290899682`
- permutation median = `+0.013688493815160296`
- empirical 2.5--97.5% range =
  `[+0.005085149860362126, +0.021671779289126402]`
- prespecified upper-tail empirical probability =
  `0.999000999000999`

Interpretation boundary:

The control does not support a claim that the observed additive RA14 effect
depends on preserving correct garment-instance correspondence.

Because permutation was performed within category, this result must not be
interpreted as a test that removes all category-associated information from
RA14.

### 7.2 Repeated grouped-partition control

| Artifact | SHA-256 |
|---|---|
| `experiment08_repeated_grouped_partitions.csv` | `fe44c90436005164dc1be6a865301f3ca84fc3dcc09b90868edd3eb79a8b6d1f` |
| `experiment08_repeated_grouped_partitions_summary.json` | `d328c7ff66954ae51e34fb5b44069e0d76f913f0f8790c1c22c28740f44f5544` |

Design:

- 20 additional partitions;
- seeds `20260823` through `20260842`;
- `StratifiedGroupKFold`;
- 5 folds;
- category stratification;
- garment identity grouping;
- no outcome-dependent partition acceptance, rejection, or repair.

All 20 partitions were unique and satisfied identity-separation constraints.

Primary delta distribution:

- mean = `+0.003927456181713002`
- median = `+0.002580754931087559`
- minimum = `-0.00581427160322634`
- maximum = `+0.0140545603514044`
- empirical 2.5--97.5% range =
  `[-0.004329725078960567, +0.01325764759058405]`
- positive repeats = `17 / 20`

Interpretation boundary:

The additive RA14 effect is small and generally positive across these
partitions but is partition-sensitive and crosses zero.

This control does not establish a robust fixed additive gain and does not
restore confirmatory status.

---

## 8. Governance and provenance records

| Record | SHA-256 |
|---|---|
| `docs/experiment-08/EXPERIMENT08_DECISION_RECORD.md` | `3d9716af0eff77e84829c167c3b3755578272783a0db9389f97f0bc154daffb6` |
| `docs/experiment-08/post-outcome-mechanical-sensitivity-amendment.md` | `879f530cf4f3c40bb47292e24db84ad44abe21d0001e0f72278c71c2f235028d` |
| `docs/experiment-08/compactness-bootstrap-correction-record.md` | `fa836fcb40ca5a65029ab591fe02a489c52e0e889e0ab42a70e5a2e886087ad5` |
| `docs/experiment-08/post-outcome-predictive-controls-amendment.md` | `6cbbfb4c646cfa9d595b54e9ad0aed150de6f7864bda5c8aebc641eccc837fe8` |
| `docs/experiment-08/post-outcome-predictive-controls-clarification.md` | `23c1566e3da092ecbbc6c5e5ce6213e82a4278d01f9513d79b4abc6e7ef2bec1` |

These records define the interpretation boundary for Experiment 08 and take
precedence over any earlier wording that could imply confirmatory status.

---

## 9. Supersession and non-rescue rules

The following rules apply to all public interpretation of Experiment 08:

1. The frozen mechanical gate remains **FAIL**.
2. No post-outcome diagnostic rescues or replaces that gate.
3. Predictive results produced after the failed gate are exploratory only.
4. Historical compactness bootstrap intervals and non-inferiority inference
   from the multiplicity-destroying implementation are invalid and superseded.
5. The corrected compactness result does not support non-inferiority.
6. The correspondence control does not support garment-instance-specific
   dependence of the observed additive RA14 contribution.
7. Repeated grouped partitions show a small, usually positive but
   partition-sensitive additive effect.
8. No Experiment 08 evidence supports a confirmatory RA14 validation claim.
9. No further predictive analysis is authorized without a separately committed
   prospective amendment.

---

## 10. Manifest provenance

Manifest source branch:

`codex/paper-i-ivc-submission-blockers`

Evidence state inventoried at:

`17c33820f1d79392de24bd02b0dbef7bb12eab68`

The SHA-256 values above were recomputed from the local clean checkout at that
commit before this manifest was written.

