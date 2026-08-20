# CLO-SKET — MORPHOLOGY–RADIAL–ANGULAR INTEGRATION
## Backbone Reconstruction and Results Audit

### Purpose

Before proceeding to literature-based novelty verification, we return to the
core experimental backbone of CLO-SKET:

**Morphology → radial structure → angular organization → integrated representation**

The objective is to reconstruct the evidence already produced by the
`Morphology_RadialAngular_Integration` analysis and determine exactly what the
integrated representation contributed.

This is an **audit of frozen results**.

No model will be retrained.

No feature will be modified.

No new representation will be introduced.

---

## 1. Available Runtime Backups

Two runtime backups are available.

### Initial radial–angular runtime

`CLO_SKET_runtime_backup.pkl`

Contains **22 objects**, including:

- full radial F₂ magnitude and complex fields
- F₂ phase
- F₂ radial descriptors
- radial peak location and magnitude
- radial extent / onset / termination
- radial concentration and spread
- radial angular orientation
- conditional angular distributions
- image paths and category labels

Important population dimensions:

- sketches: **2300**
- full radial bins: **72**
- circular-analysis shells: **25**
- angular bins: **72**

---

### Post-Cell-25 runtime

`CLO_SKET_runtime_backup_AFTER_CELL25.pkl`

Contains **44 objects** and preserves the integrated representation and
classification/permutation results.

This backup contains the principal objects required for reconstruction.

---

## 2. Frozen Representation Blocks

The post-Cell-25 runtime contains the following feature blocks.

### Radial F₂ representation

`X_F2_radial`

Shape:

**2300 × 9**

This represents the frozen radial morphology baseline.

---

### Axial angular representation

`X_alpha2`

Shape:

**2300 × 7**

This contains the reduced axial-orientation descriptors derived from the
second angular mode.

---

### Observed circular organization

`X_observed_circular`

Shape:

**2300 × 3**

This represents measured circular organization from the observed
radial–angular field.

---

### Learned circular organization

`X_learned_circular`

Shape:

**2300 × 4**

This contains descriptors derived from the learned circular field.

---

### Relational representation

`X_relational`

Shape:

**2300 × 5**

This block represents relationships between components of the
radial–angular representation rather than an isolated measurement family.

---

## 3. Canonical Integrated Representation

The frozen integrated feature matrix is:

`X_canonical`

with shape:

**2300 × 28**

Therefore the canonical CLO-SKET representation contains **28 features per
sketch**.

The runtime inventory establishes the existence of the following constituent
blocks:

| Feature block | Dimensions |
|---|---:|
| F₂ radial | 9 |
| α₂ axial | 7 |
| Observed circular | 3 |
| Learned circular | 4 |
| Relational | 5 |
| **Canonical total** | **28** |

The dimensional accounting is exact:

**9 + 7 + 3 + 4 + 5 = 28**

This provides an important structural audit of the frozen canonical
representation.

---

## 4. Observed and Learned Radial–Angular Fields

The post-Cell-25 runtime also preserves the population-level fields:

- `C2_obs` — **2300 × 25**
- `C2_hat_field` — **2300 × 25**
- `R2_obs` — **2300 × 25**
- `R2_hat_field` — **2300 × 25**
- `S2_obs` — **2300 × 25**
- `S2_hat_field` — **2300 × 25**
- `mu2_obs_deg` — **2300 × 25**
- `mu2_hat_field_deg` — **2300 × 25**

These objects are particularly important because they connect the original
integration analysis to the later population-level recovery analysis in
Cells 30C–30M.

Thus the recovery analysis is not based on a newly introduced representation.

It interrogates fields already present in the frozen post-Cell-25 runtime.

---

## 5. Frozen Experimental Results

The backup contains:

`cell24_results`

Shape:

**11 × 8**

and:

`cell24_incremental`

Shape:

**10 × 3**

These should contain the controlled comparison of representation variants
and the incremental contribution analysis.

The backup additionally contains:

`cell25_permutation_summary`

Shape:

**6 × 9**

This should contain the permutation-based statistical validation of the
classification/discrimination results.

These are the primary objects that must now be inspected.

---

# BACKBONE AUDIT QUESTIONS

The reconstruction will answer five questions.

## Q1 — Baseline

What discrimination performance was achieved using the frozen
**F₂ radial morphology representation alone**?

---

## Q2 — Integration

What changed when axial and circular organization were added to the radial
representation?

The comparison must be made using the existing frozen experimental results,
not by retraining a classifier.

---

## Q3 — Incremental contribution

Which representation blocks produced measurable incremental changes?

Particular attention should be paid to:

- α₂ axial information
- observed R₂ / circular organization
- learned circular organization
- relational features

---

## Q4 — Statistical validation

Were the integrated-representation results distinguishable from the
permutation/null distributions already computed in Cell 25?

---

## Q5 — Connection to recovery analysis

Do the original integration results and the later Cells 30C–30M support a
coherent evidence chain?

The candidate chain is:

**radial morphology**

↓

**axial / circular organization**

↓

**canonical integrated representation**

↓

**controlled category discrimination**

↓

**observed-versus-learned radial–angular recovery**

↓

**recovery reliability**

↓

**failure-regime characterization**

This chain must be demonstrated from the frozen evidence rather than assumed.

---

# IMPORTANT CLAIM BOUNDARY

At this stage we do **not** claim that:

- the 28-dimensional representation is mathematically novel;
- Fourier shape analysis is novel;
- radial–angular analysis is novel;
- axial doubled-angle representation is novel;
- the representation identifies semantic garment parts;
- classification performance demonstrates visual understanding.

The present objective is narrower:

> Determine what empirical contribution the integrated radial–angular
> representation made relative to the frozen morphology baseline, and
> determine whether that contribution is consistent with the later
> population-level recovery evidence.

---

# NEXT COMPUTATIONAL STEP

Inspect only the preserved result objects:

`cell24_results`

`cell24_incremental`

`cell25_permutation_summary`

and, if necessary, their column names / indices.

**Do not retrain anything.**

**Do not recompute features.**

**Do not overwrite the frozen runtime.**

The immediate goal is to recover the original backbone results exactly as
they were produced.

# CLO-SKET — MORPHOLOGY ↔ RADIAL–ANGULAR INTEGRATION
## Cell 1 Scientific Audit — Frozen Morphology Branch

### Status

**CELL 1 PASSED.**

The morphology branch has been loaded from a frozen artifact and its
identity has been verified independently before any radial–angular
integration is performed.

---

## 1. Population

The frozen morphology representation contains:

- **2300 sketches**
- **135 quantitative morphology features**
- `float32` representation
- all values finite

Therefore the morphology population has the same population size as the
previous CLO-SKET radial–angular experiments:

**N = 2300**

Population size alone does not yet establish row-wise sketch identity.

That must be verified in Cell 2.

---

## 2. Morphology Representation

The frozen matrix is:

`X_raw`

with shape:

**2300 × 135**

The 135 dimensions have an explicit block structure:

| Morphology block | Features |
|---|---:|
| Horizontal occupancy | 64 |
| Vertical occupancy | 64 |
| Global descriptors | 7 |
| **Total** | **135** |

The dimensional accounting is exact:

**64 + 64 + 7 = 135**

---

## 3. Image-Derivation Provenance

According to the preserved metadata, the morphology representation was
derived using:

- grayscale images
- intensity normalization by division by 255
- foreground threshold `< 0.8`
- canonical spatial size `64 × 64`

This establishes the preprocessing provenance of the frozen morphology
branch.

No additional transformation was introduced in Cell 1.

---

## 4. Artifact Integrity

The saved SHA-256 hash is:

`66ae04156ee3fbf3f2605f382a16fc41cf19af34b50e59dd43f6c9427d96b2ee`

The hash calculated from the currently loaded artifact is identical.

Therefore:

**saved SHA-256 = current SHA-256**

and the frozen morphology matrix passes an exact binary-integrity check.

This is stronger than merely reproducing the expected matrix dimensions.

---

## 5. Experimental Independence at Entry

Importantly, Cell 1 has not used:

- radial F₂ quantities
- α₂ orientation quantities
- R₂ circular-strength quantities
- learned circular fields
- category labels

Thus the morphology branch enters the integration experiment as an
independently loaded frozen representation.

This is methodologically important because the later comparison should not
begin from a morphology representation reconstructed using information from
the radial–angular branch.

---

# CELL 1 EVIDENCE

Cell 1 currently establishes:

> A frozen 135-dimensional quantitative morphology representation exists
> for all 2300 CLO-SKET sketches, with verified feature structure,
> preprocessing provenance, numerical validity, and exact artifact
> integrity.

It does **not yet establish** that the 2300 morphology rows correspond
exactly, in the same order, to the 2300 radial–angular rows.

---

# CRITICAL NEXT TEST

Before examining classification, correlations, feature relationships, or
integration performance, the two branches must be aligned at the
**individual-sketch level**.

The next question is therefore not:

> Does morphology correlate with radial–angular organization?

It is first:

> Does morphology row `i` correspond to radial–angular row `i` for every
> one of the 2300 sketches?

This must be demonstrated from provenance identifiers such as image paths,
filenames, stable sketch IDs, or equivalent frozen metadata.

Matching only:

**2300 morphology sketches = 2300 radial–angular sketches**

is insufficient evidence of alignment.

---

# BACKBONE STATUS AFTER CELL 1

Current experimental structure:

**Frozen sketch population**

↓

**135-D morphology representation**

- 64 horizontal occupancy
- 64 vertical occupancy
- 7 global descriptors

↓

**SHA-256 verified**

↓

**No radial–angular information introduced**

↓

### NEXT

**Cross-branch population and provenance alignment**

↓

*Only after exact alignment is established:*

**Morphology ↔ radial–angular integration**

---

# CLAIM BOUNDARY

### Supported after Cell 1

- The morphology artifact contains 2300 observations.
- It contains exactly 135 features.
- The 135 features follow the documented 64 + 64 + 7 structure.
- The matrix is finite.
- The frozen artifact passes exact SHA-256 verification.
- Cell 1 performs no radial–angular recomputation.
- Cell 1 uses no category information.

### Not yet supported

- Exact row-wise correspondence with the radial–angular population.
- Statistical association between morphology and radial–angular structure.
- Complementarity between morphology and radial–angular information.
- Improvement from integrating the two representations.
- Category-discriminative benefit of integration.
- Any causal relationship between morphology and radial–angular organization.
- Any semantic interpretation of the morphology or angular components.

---

# DECISION

**Do not perform integration yet.**

Proceed to:

## CELL 2 — CROSS-BRANCH POPULATION / PROVENANCE ALIGNMENT

Required evidence:

1. Load the frozen radial–angular population identity.
2. Recover its sketch identifiers / image paths.
3. Recover the corresponding morphology population identifiers.
4. Normalize identifiers only if required for path-format differences.
5. Test exact one-to-one population membership.
6. Test exact row-wise ordering.
7. Report missing identifiers.
8. Report duplicate identifiers.
9. Report reordered identifiers, if any.
10. Save an explicit alignment audit object.

No feature analysis.

No classifier.

No statistical association test.

No representation modification.

No category-based selection.

# CLO-SKET — MORPHOLOGY ↔ RADIAL–ANGULAR INTEGRATION
## Cell 1B Scientific Audit — Frozen Radial–Angular Branch Restored

### Status

**CELL 1B PASSED.**

The frozen radial–angular branch has been restored from the
post-Cell-25 runtime backup without recomputing the representation.

---

## 1. Restored Radial–Angular Objects

The following sketch-level objects are available:

| Object | Shape |
|---|---:|
| `F2_mag` | `(2300, 72)` |
| `R2_obs` | `(2300, 25)` |
| `R2_hat_field` | `(2300, 25)` |
| `mu2_obs_deg` | `(2300, 25)` |
| `mu2_hat_field_deg` | `(2300, 25)` |
| `image_paths` | `(2300,)` |

Every restored object contains exactly:

**N = 2300 sketches**

Therefore the radial–angular branch is internally population-consistent.

---

## 2. Representation Structure

The restored branch contains two different radial resolutions.

### F₂ representation

`F2_mag`

has:

**72 radial bins per sketch**

This is the full F₂ radial representation.

### Circular representation

The observed and learned circular fields:

- `R2_obs`
- `R2_hat_field`
- `mu2_obs_deg`
- `mu2_hat_field_deg`

contain:

**25 established circular-analysis shells per sketch**

This preserves the radial-domain structure established in the previous
radial–angular analysis.

---

## 3. Provenance Anchor

The restored object:

`image_paths`

contains one image reference for each of the 2300 radial–angular
observations.

This is important because population size alone cannot establish
cross-branch correspondence.

`image_paths` provides a potential provenance key for determining whether:

**morphology row i ↔ radial–angular row i**

for every sketch.

---

## 4. No Reconstruction

Cell 1B does **not** recompute:

- F₂
- R₂
- μ₂
- learned circular fields
- morphology features

The existing frozen radial–angular objects are restored directly from the
saved runtime backup.

Therefore the integration experiment can continue from the previously
established representation rather than generating a new version of it.

---

# CURRENT TWO-BRANCH STATE

We now have:

## Branch A — Morphology

`X_raw`

**2300 × 135**

composed of:

- 64 horizontal occupancy features
- 64 vertical occupancy features
- 7 global morphology descriptors

and verified by the frozen artifact SHA-256.

---

## Branch B — Radial–Angular

Restored sketch-level geometry:

- `F2_mag`
- `R2_obs`
- `R2_hat_field`
- `mu2_obs_deg`
- `mu2_hat_field_deg`
- `image_paths`

with:

**N = 2300**

---

# CRITICAL SCIENTIFIC STATUS

The two branches have the same population size:

**2300 morphology observations**

and

**2300 radial–angular observations**

but this does **not yet prove cross-branch identity**.

At this stage we know:

`N_morphology = N_radial-angular = 2300`

We do **not yet know**:

`morphology[i] == radial-angular[i]`

for all:

`i = 0, ..., 2299`

That distinction is critical.

A row-order mismatch would invalidate sketch-level integration even though
both matrices contain exactly 2300 observations.

---

# REQUIRED NEXT STEP

## CELL 2 — CROSS-BRANCH POPULATION / PROVENANCE ALIGNMENT

Cell 2 must establish:

1. the provenance identifier available for the morphology branch;
2. the provenance identifier available for the radial–angular branch;
3. uniqueness of identifiers within each branch;
4. population-set equality;
5. missing sketches in either branch;
6. duplicate sketches in either branch;
7. exact row-wise ordering;
8. whether any reindexing is required;
9. a deterministic alignment map if ordering differs;
10. a frozen alignment audit for all subsequent experiments.

The preferred identity hierarchy is:

**stable sketch ID**

↓

**canonical relative image path**

↓

**normalized filename/category identifier**

Only the minimum normalization required to reconcile storage-path
differences should be applied.

---

# HARD GATE

No morphology ↔ radial–angular statistical analysis should begin until
Cell 2 passes.

Specifically, do **not yet** run:

- morphology–F₂ correlations
- morphology–R₂ associations
- morphology–μ₂ associations
- CCA
- PCA integration
- feature-family discrimination
- combined classification
- ablation
- permutation testing
- category analysis

The first requirement is exact sample identity.

---

# EXPERIMENTAL CHAIN

**Frozen 135-D morphology**

↓

**SHA-256 verified**

+

**Frozen radial–angular representation**

↓

**2300-sketch population restored**

↓

### CELL 2

**Cross-branch provenance alignment**

↓

**Exact sketch-level identity lock**

↓

### THEN

**Morphology ↔ radial–angular relationship analysis**

---

# CLAIM BOUNDARY

### Supported

- Both branches contain 2300 observations.
- The morphology representation is frozen.
- The radial–angular representation has been restored.
- Radial–angular image references are available.
- No integration analysis has yet been performed.

### Not yet supported

- Exact row-wise correspondence between branches.
- Morphology–radial association.
- Morphology–angular association.
- Complementarity of the two representations.
- Redundancy of the two representations.
- Category-discriminative benefit of their integration.
- Any causal or semantic relationship.

---

## Decision

**CELL 1B PASSED.**

Proceed to:

# CELL 2 — CROSS-BRANCH POPULATION / PROVENANCE ALIGNMENT

The experiment remains behind the alignment hard gate until exact
sketch-level correspondence is demonstrated.

# CLO-SKET — MORPHOLOGY ↔ RADIAL–ANGULAR INTEGRATION
## Cell 2 Scientific Audit — Cross-Branch Population / Provenance Alignment

### Status

**POPULATION COMPATIBILITY: PASSED**

**ROW-LEVEL PROVENANCE: NOT YET INDEPENDENTLY VERIFIED**

Cell 2 establishes that the frozen morphology branch and the restored
radial–angular branch are compatible at the population and dimensional
levels.

It does **not** yet establish independent row-wise identity.

---

## 1. Cross-Branch Population Compatibility

Both branches contain exactly:

**N = 2300 sketches**

### Morphology branch

| Object | Shape |
|---|---:|
| `X_raw` | `(2300, 135)` |
| `horizontal_occupancy` | `(2300, 64)` |
| `vertical_occupancy` | `(2300, 64)` |
| `global_descriptors` | `(2300, 7)` |

### Radial–angular branch

| Object | Shape |
|---|---:|
| `F2_mag` | `(2300, 72)` |
| `R2_obs` | `(2300, 25)` |
| `R2_hat_field` | `(2300, 25)` |
| `mu2_obs_deg` | `(2300, 25)` |
| `mu2_hat_field_deg` | `(2300, 25)` |
| `image_paths` | `(2300,)` |

Thus:

`N_morphology = N_radial-angular = 2300`

This establishes **population compatibility**.

---

## 2. Morphology Representation Integrity

The frozen morphology matrix retains the expected decomposition:

**64 horizontal occupancy**

+

**64 vertical occupancy**

+

**7 global descriptors**

=

**135 morphology features**

All morphology quantities required for the integration experiment are
numerically finite.

---

## 3. Radial–Angular Representation Integrity

The restored radial–angular branch retains:

- full 72-bin F₂ radial magnitude profiles;
- 25-shell observed circular-strength fields;
- 25-shell learned circular-strength fields;
- 25-shell observed axial orientations;
- 25-shell learned axial orientations.

All required numerical arrays are finite.

Therefore there is no dimensional or numerical barrier to subsequent
cross-branch analysis.

---

## 4. Radial–Angular Provenance

The radial–angular branch contains:

**2300 image references**

with:

- 2300 unique references;
- 0 duplicates;
- 0 empty references.

Thus the radial–angular population possesses a complete sketch-level
provenance key.

---

# 5. Remaining Provenance Gap

The currently loaded frozen morphology artifacts do **not** provide an
independent morphology-side image-path array.

Therefore Cell 2 cannot currently test:

`morphology_image_path[i] == radial_angular_image_path[i]`

for every:

`i = 0, ..., 2299`

This means that:

**population compatibility has been demonstrated**

but:

**independent row-level provenance has not yet been demonstrated**

These are not equivalent statements.

---

# 6. Why This Matters

Any subsequent analysis such as:

`Morphology[i] ↔ RadialAngular[i]`

requires both feature representations to describe the **same sketch**.

If one branch were reordered relative to the other, then:

- cross-branch correlations;
- canonical correlations;
- regression;
- redundancy analysis;
- complementarity analysis;
- integrated classification;

could all produce invalid scientific results.

Therefore population-size equality alone is not sufficient justification
for integration.

---

# 7. Important Provenance Clue

The morphology metadata contains the following fields:

- `dataset`
- `source`
- `representation`
- `purpose`
- `image_processing`
- `downstream_processing`
- `n_observations`
- `n_features`
- `matrix_dtype`
- `sha256`

The next provenance investigation should therefore examine:

**`source`**

and:

**`downstream_processing`**

together with the notebook/code that originally generated the frozen
2300 × 135 matrix.

The objective is to determine whether `X_raw` was generated directly from
the same ordered sketch list represented by the restored `image_paths`.

---

# 8. Scientific Claim Boundary

## Supported

- Both branches contain 2300 observations.
- Both branches are dimensionally valid.
- All required numerical arrays are finite.
- The morphology matrix retains its frozen 135-D structure.
- The radial–angular branch has 2300 unique image references.
- No cross-branch association analysis has yet been performed.

## Not yet supported

- Exact morphology ↔ radial–angular row identity.
- Morphology ↔ F₂ association.
- Morphology ↔ R₂ association.
- Morphology ↔ axial-orientation association.
- Redundancy between the two representations.
- Complementarity between the two representations.
- Integrated category-discrimination improvement.
- Any causal or semantic interpretation.

---

# 9. Integration Hard Gate

The integration experiment remains behind the following gate:

**Frozen morphology**

+

**Frozen radial–angular representation**

↓

**Population compatibility**

✓ PASSED

↓

**Independent row-level provenance**

⚠ NOT YET VERIFIED

↓

**Morphology ↔ radial–angular integration**

**BLOCKED UNTIL PROVENANCE IS RESOLVED**

---

# NEXT

## CELL 2B — MORPHOLOGY ROW-PROVENANCE RECOVERY

Cell 2B should search the existing frozen artifacts and generation
provenance for evidence of morphology row ordering.

The search should proceed conservatively:

1. inspect morphology metadata fields in full;
2. inspect the frozen artifact directory for manifest / path / ID files;
3. inspect existing notebook objects for morphology-side paths or IDs;
4. inspect the morphology-generation code only if necessary;
5. determine how the 2300 morphology rows were ordered;
6. compare that ordering against radial–angular `image_paths`;
7. test uniqueness and one-to-one membership;
8. test exact row-wise correspondence;
9. construct an alignment map only if required;
10. freeze the resulting provenance evidence.

No statistical integration should be performed during this recovery step.

---

## Decision

**Do not run Cell 3 yet.**

Proceed to:

# CELL 2B — MORPHOLOGY ROW-PROVENANCE RECOVERY

Only after this gate passes should the backbone experiment begin:

**135-D morphology**

↕

**radial–angular organization**

# CLO-SKET — MORPHOLOGY ↔ RADIAL–ANGULAR INTEGRATION
## Cell 2A Scientific Audit — Cross-Branch Provenance Resolution

### Status

**🟢 ROW-LEVEL PROVENANCE VERIFIED**

Cell 2A resolves the critical alignment uncertainty identified in Cell 2.

The morphology branch and radial–angular branch are not merely equal in
population size.

Their sketch-level path sequences match **exactly in row order**.

---

## 1. Morphology Provenance

The frozen morphology representation was:

> reconstructed directly from source TIFFs

with:

- no standardization;
- no PCA;
- no clustering;
- no KDE;
- no basin assignment.

The preserved representation contains:

- 64 horizontal occupancy features;
- 64 vertical occupancy features;
- 7 global descriptors;

for a total of:

**135 raw canonical morphology features**

across:

**2300 sketches**

The frozen morphology artifact remains identified by SHA-256:

`66ae04156ee3fbf3f2605f382a16fc41cf19af34b50e59dd43f6c9427d96b2ee`

---

## 2. Independent Morphology-Side Path Recovery

Cell 2A recovered the morphology-side object:

`paths`

with shape:

`(2300,)`

The radial–angular branch independently contains:

`image_paths`

with shape:

`(2300,)`

This provides sketch-level identifiers on both sides of the integration.

---

## 3. Cross-Branch Identity Test

Two distinct provenance conditions were tested.

### Population membership

The two path collections contain the same path set:

**Same path set = True**

Therefore neither branch contains a sketch absent from the other branch.

### Row ordering

The paths were then compared position by position:

**Exact row-order match = True**

Therefore, for every observation index:

`i = 0, ..., 2299`

the following correspondence holds:

`paths[i] == image_paths[i]`

and consequently:

`X_raw[i]`

corresponds to the same source sketch as:

- `F2_mag[i]`
- `R2_obs[i]`
- `R2_hat_field[i]`
- `mu2_obs_deg[i]`
- `mu2_hat_field_deg[i]`

---

# 4. Why This Is Stronger Than the Cell 2 Result

Cell 2 established only:

`N_morphology = N_radial-angular = 2300`

That demonstrated population compatibility but could not exclude a
permutation of rows.

Cell 2A now establishes:

`paths[i] = image_paths[i]`

for all 2300 observations.

Thus the integration is supported by **direct row-level provenance**, not
by population-size inference.

No reindexing or alignment map is required.

---

# 5. Cross-Branch Alignment Lock

The following relationship can now be frozen:

**Source TIFF sketch i**

↓

### Morphology branch

`X_raw[i, :]`

135-D morphology

and simultaneously:

### Radial–angular branch

`F2_mag[i, :]`

`R2_obs[i, :]`

`R2_hat_field[i, :]`

`mu2_obs_deg[i, :]`

`mu2_hat_field_deg[i, :]`

Therefore both branches describe the **same individual sketch at the same
row index**.

---

# 6. Provenance Limitation

No explicit independent metadata describing the historical sorting rule was
found.

However, this does not prevent the present row-level identity test because
both independently recovered path arrays are available and their current
sequences match exactly.

The appropriate claim is therefore:

> The frozen morphology and restored radial–angular representations exhibit
> exact sketch-level path correspondence across all 2300 observations.

It is unnecessary to claim that the original sorting algorithm itself has
been independently reconstructed.

---

# 7. Scientific Claim Boundary

## Supported

- Both branches contain exactly 2300 sketches.
- Both branches contain the same sketch-path population.
- Morphology-side paths are unique at the population level represented here.
- Radial–angular paths contain 2300 unique references.
- Cross-branch path sets are identical.
- Cross-branch row ordering is identical.
- `X_raw[i]` and radial–angular observation `i` correspond to the same sketch.
- No reindexing is required before integration.

## Not Yet Supported

- Statistical dependence between morphology and F₂.
- Statistical dependence between morphology and R₂.
- Morphology–orientation relationships.
- Redundancy between morphology and radial–angular geometry.
- Complementarity between the two representations.
- Whether one representation predicts the other.
- Whether combining the representations improves category discrimination.
- Causal relationships.
- Semantic garment-part interpretation.

---

# 8. Integration Hard Gate

The integration gate can now be opened.

Previous state:

**Population compatibility**

🟢 PASSED

↓

**Independent row-level provenance**

🟡 UNRESOLVED

Current state:

**Population compatibility**

🟢 PASSED

↓

**Same sketch population**

🟢 PASSED

↓

**Exact row-order identity**

🟢 PASSED

↓

**Cross-branch alignment**

# 🔓 VERIFIED

↓

**Morphology ↔ radial–angular analysis permitted**

---

# 9. Important Experimental Principle for the Next Phase

Now that alignment is proven, we should still avoid jumping directly to
category classification.

The scientific backbone should first ask a more fundamental question:

> **What information about radial–angular organization is already contained
> in the 135-D morphology representation, and what information remains
> distinct?**

This separates the representation question from the later category-label
question.

---

# NEXT EXPERIMENTAL PHASE

## CELL 3 — MORPHOLOGY ↔ RADIAL–ANGULAR ASSOCIATION AUDIT

The first integration analysis should remain completely **label-free**.

The analysis should distinguish several targets rather than collapsing the
radial–angular branch into one arbitrary quantity.

### Morphology

`X_raw`

**2300 × 135**

### Radial structure

F₂-derived quantities describing:

- magnitude;
- radial localization;
- spread;
- concentration;
- support;
- peak structure.

### Axial structure

α₂-derived quantities describing:

- axial orientation;
- coherence;
- persistence;
- orientation drift.

### Circular organization

Observed R₂ quantities describing:

- circular-strength magnitude;
- radial variation in circular strength.

### Learned circular organization

Learned R₂ quantities describing the population-predicted circular field.

---

# CIRCULAR-STATISTICS PROTECTION

Axial orientations must **not** be entered into ordinary linear association
analysis as raw degree values.

For an axial orientation:

`α ≡ α + 180°`

Therefore orientation quantities must be represented using:

`cos(2α)`

and:

`sin(2α)`

or evaluated using an explicitly axial circular association measure.

R₂, F₂ magnitude, radial position, concentration, persistence, and other
non-angular scalar quantities may be treated using appropriate ordinary
scalar statistics.

---

# CELL 3 SHOULD ANSWER

### Question 1

How strongly is morphology associated with **radial F₂ geometry**?

### Question 2

How strongly is morphology associated with **axial organization**?

### Question 3

How strongly is morphology associated with **observed circular strength**?

### Question 4

How strongly is morphology associated with the **learned circular
representation**?

### Question 5

Are the strongest relationships concentrated in particular morphology
blocks:

- horizontal occupancy;
- vertical occupancy;
- global morphology;

or distributed across the representation?

---

# IMPORTANT

Cell 3 should be an **association / redundancy audit**, not yet a
category-discrimination experiment.

No category labels.

No category-based feature selection.

No classifier.

No optimization against garment classes.

No semantic interpretation.

This preserves the experimental logic:

**raw sketch**

↓

**morphology representation**

+

**radial–angular representation**

↓

**exact row-level provenance**

↓

# label-free cross-representation association

↓

**redundancy / complementarity characterization**

↓

*only later*

**controlled category discrimination**

---

## Decision

**🟢 CELL 2A PASSED**

The provenance hard gate is resolved.

# Proceed to CELL 3 — MORPHOLOGY ↔ RADIAL–ANGULAR ASSOCIATION AUDIT

# CLO-SKET — MORPHOLOGY ↔ RADIAL–ANGULAR INTEGRATION
## Cell 3 Scientific Audit — 135-D Morphology ↔ Radial–Angular Feature Associations

### Status

**🟢 CELL 3 PASSED**

Cell 3 provides the first direct, label-free evidence that the frozen
135-dimensional morphology representation and the radial–angular
representation are statistically related at the individual-sketch level.

Because Cell 2A established exact row-wise provenance, these associations
are evaluated between measurements derived from the **same 2300 sketches**.

---

# 1. Experimental Question

Cell 3 asks:

> Are coordinates of the frozen morphology representation associated with
> independently derived radial–angular measurements?

Four radial–angular targets were examined:

1. `F2_peak_magnitude`
2. `F2_peak_radius`
3. `R2_observed_at_F2_peak`
4. `axial_error_at_F2_peak`

The analysis remains completely **category-label free**.

---

# 2. Domain Consistency

The radial–angular targets were derived within the previously locked
circular-analysis domain.

**Radial domain:**

`3.50 → 27.50`

**Circular shells:**

`25`

All 2300 F₂ peaks were identified inside this domain.

The maximum mismatch between the selected F₂ peak radius and its matched
circular shell was:

`0.000000`

Therefore the morphology associations are evaluated against
domain-consistent radial–angular quantities.

---

# 3. Population-Level Target Summary

| Target | Population median |
|---|---:|
| F₂ peak magnitude | 0.039141 |
| F₂ peak radius | 21.500000 |
| Observed R₂ at F₂ peak | 0.436421 |
| Axial recovery error | 6.132369° |

All target quantities are finite across:

**N = 2300 sketches**

---

# 4. Primary Association Result

The four targets show markedly different levels of association with the
135-D morphology representation.

| Target | FDR-significant morphology features | Median \|ρ\| | Maximum \|ρ\| |
|---|---:|---:|---:|
| F₂ peak magnitude | 126 / 135 | 0.2173 | **0.5469** |
| F₂ peak radius | 93 / 135 | 0.0979 | **0.3537** |
| Observed R₂ at F₂ peak | 106 / 135 | 0.1315 | **0.3944** |
| Axial recovery error | 90 / 135 | 0.0871 | **0.2171** |

The strongest coordinate-level association therefore occurs for:

**morphology ↔ F₂ peak magnitude**

while:

**morphology ↔ axial recovery error**

is substantially weaker at the individual-feature level.

---

# 5. F₂ Peak Magnitude

The strongest observed association is:

`horizontal_occupancy_50`

with:

**Spearman ρ = −0.5469**

and:

**FDR q = 1.792 × 10⁻¹⁷⁷**

Several neighboring horizontal occupancy coordinates show similarly strong
associations:

- `horizontal_occupancy_51`: ρ = −0.5370
- `horizontal_occupancy_49`: ρ = −0.5307
- `horizontal_occupancy_52`: ρ = −0.5083
- `horizontal_occupancy_48`: ρ = −0.4960
- `horizontal_occupancy_53`: ρ = −0.4853

Two global descriptors also appear among the strongest associations:

- `symmetry`: ρ = +0.4840
- `foreground_fraction`: ρ = −0.4707

This provides strong evidence that F₂ magnitude is related to measurable
properties already represented in the frozen morphology coordinates.

---

# 6. F₂ Peak Radius

F₂ radial localization shows weaker but still systematic morphology
association.

The strongest feature is:

`horizontal_occupancy_45`

with:

**Spearman ρ = +0.3537**

The strongest associations are concentrated primarily among neighboring
horizontal occupancy coordinates.

At the block level:

| Morphology block | Median \|ρ\| | Maximum \|ρ\| | FDR significant |
|---|---:|---:|---:|
| Horizontal occupancy | 0.0891 | **0.3537** | 42 / 64 |
| Vertical occupancy | 0.1026 | 0.1646 | 46 / 64 |
| Global descriptors | 0.0798 | 0.2261 | 5 / 7 |

Thus radial localization is associated with morphology, but substantially
less strongly than F₂ peak magnitude.

---

# 7. Observed Circular Strength R₂

Observed circular organization at the matched F₂ peak shell also exhibits
systematic morphology association.

The strongest relationship is:

`horizontal_occupancy_44`

with:

**Spearman ρ = +0.3944**

Several horizontal and vertical occupancy coordinates appear among the
largest associations.

Block-level results are:

| Morphology block | Median \|ρ\| | Maximum \|ρ\| | FDR significant |
|---|---:|---:|---:|
| Horizontal occupancy | 0.1303 | **0.3944** | 52 / 64 |
| Vertical occupancy | 0.1315 | **0.3379** | 50 / 64 |
| Global descriptors | 0.0863 | 0.2851 | 4 / 7 |

Therefore observed R₂ is not statistically isolated from the morphology
representation.

There is measurable shared structure between the two branches.

---

# 8. Axial Recovery Error

Axial recovery error shows the weakest coordinate-level relationships of
the four targets.

The largest absolute association is approximately:

**|ρ| = 0.2171**

for:

`vertical_occupancy_32`

with:

**ρ = −0.2171**

The block structure is particularly informative:

| Morphology block | Median \|ρ\| | Maximum \|ρ\| | FDR significant |
|---|---:|---:|---:|
| Horizontal occupancy | 0.0527 | 0.1874 | 36 / 64 |
| Vertical occupancy | **0.1284** | **0.2171** | 49 / 64 |
| Global descriptors | 0.0875 | 0.1162 | 5 / 7 |

Unlike F₂ magnitude and F₂ radius, axial recovery error shows relatively
greater association with the **vertical occupancy block**.

This is a useful empirical observation but should not yet be given a
semantic interpretation.

---

# 9. Multiple-Comparison Protection

For each radial–angular target, 135 morphology coordinates were evaluated.

Benjamini–Hochberg FDR correction was applied separately within each target.

Therefore the reported significant-feature counts refer to:

**FDR-controlled coordinate-wise associations**

rather than uncorrected individual p-values.

However, the very large number of significant coordinates should not be
interpreted as 126, 106, or 90 independent discoveries.

The occupancy representation contains neighboring spatial coordinates that
are likely internally correlated.

Consequently:

**number of significant features ≠ number of independent morphology effects**

Effect magnitude and block structure are more informative than significance
counts alone.

---

# 10. First Important Backbone Result

Cell 3 establishes something stronger than simple dimensional compatibility:

> The morphology and radial–angular branches contain measurable shared
> statistical structure.

This is especially clear for:

**F₂ peak magnitude**

and:

**observed R₂ at the F₂ peak shell.**

However, the strength of association differs substantially across
radial–angular quantities.

A useful empirical ordering from the present coordinate-wise audit is:

**F₂ peak magnitude**

↓

**observed R₂**

↓

**F₂ peak radius**

↓

**axial recovery error**

when judged by the maximum observed absolute Spearman association.

This ordering is descriptive and should not be interpreted as a formal
ranking of overall representational dependence.

---

# 11. What Cell 3 Does NOT Establish

This distinction is critical.

Association does not tell us whether the radial–angular representation is
fully recoverable from morphology.

For example:

`ρ(morphology feature, F₂) ≠ 0`

does **not** imply:

`F₂ contains no additional information`

Similarly, weak coordinate-wise correlations do not prove complementarity,
because information may be distributed across combinations of morphology
coordinates.

Therefore Cell 3 cannot yet answer the central integration question:

> Does the radial–angular branch contain information that is not recoverable
> from the frozen 135-D morphology representation?

That requires a conditional / incremental analysis.

---

# 12. Scientific Claim Boundary

## Supported

1. Morphology coordinates are systematically associated with F₂ peak
   magnitude.

2. Morphology coordinates are associated with F₂ radial localization.

3. Morphology coordinates are associated with observed R₂ at the matched
   F₂ peak shell.

4. Morphology coordinates are associated with axial recovery error.

5. Association magnitude differs across radial–angular targets.

6. F₂ peak magnitude exhibits the strongest individual morphology
   association among the four evaluated targets.

7. Axial recovery error exhibits weaker coordinate-wise associations than
   the other evaluated quantities.

8. Different morphology blocks exhibit different association patterns.

---

## Not Yet Supported

1. The two representations are redundant.

2. The two representations are complementary.

3. Morphology predicts radial–angular geometry out of sample.

4. Radial–angular geometry contributes information beyond morphology.

5. Radial–angular features improve category discrimination beyond
   morphology.

6. Morphology causes radial–angular organization.

7. Individual occupancy coordinates correspond to semantic garment parts.

8. Any observed association represents human-like garment understanding.

---

# 13. Backbone Interpretation

The integration experiment has now progressed through three distinct
evidence levels:

**Frozen morphology integrity**

↓

**Exact sketch-level provenance**

↓

**Cross-representation statistical association**

🟢 ESTABLISHED

The next level is more demanding:

**conditional / incremental information**

---

# CRITICAL NEXT EXPERIMENT

## CELL 4 — RADIAL–ANGULAR INFORMATION BEYOND 135-D MORPHOLOGY

Cell 4 should not merely compute more pairwise correlations.

The central question should be:

> **How much of each radial–angular target can be recovered from morphology
> alone under out-of-sample validation?**

and then:

> **What radial–angular structure remains unexplained by morphology?**

This requires strict cross-validation because fitting 135 predictors to
2300 observations and evaluating them on the same data would exaggerate
recoverability.

---

# Recommended Cell 4 Structure

For each radial–angular target:

### Scalar targets

- F₂ peak magnitude
- F₂ peak radius
- observed R₂ at F₂ peak
- axial recovery error

evaluate:

**Morphology → target**

using grouped/frozen cross-validation.

Report:

- cross-validated R²;
- RMSE;
- MAE;
- null/baseline performance.

---

## Morphology Block Ablation

Evaluate separately:

**Horizontal occupancy only**

**Vertical occupancy only**

**Global descriptors only**

**ALL 135 morphology features**

This will determine whether cross-branch recoverability is concentrated in
one morphology block or distributed across them.

---

# Important Methodological Constraint

Cell 4 should use a **fixed predictive model**.

No target-specific hyperparameter search.

No category labels.

No feature selection based on target performance.

No training-set evaluation presented as evidence.

The purpose is not to maximize prediction accuracy.

The purpose is to quantify:

> **out-of-sample information shared between morphology and radial–angular
> geometry.**

---

# Why Cell 4 Matters for the Paper

Cell 3 says:

> **The representations are associated.**

Cell 4 can potentially say:

> **Some radial–angular quantities are substantially recoverable from
> morphology, while others retain structure not captured by the frozen
> morphology representation.**

Only after that can we scientifically justify testing:

> **Does adding radial–angular information to morphology improve controlled
> category discrimination?**

That later experiment would provide the actual **complementarity test**.

---

# CURRENT BACKBONE STATUS

**135-D frozen morphology**

↓

**Exact provenance alignment**

↓

**Morphology ↔ radial–angular association**

### 🟢 ESTABLISHED

↓

**Cross-validated radial–angular recoverability from morphology**

### ← NEXT

↓

**Residual / incremental radial–angular information**

↓

**Controlled morphology + radial–angular integration**

↓

**Permutation robustness**

↓

**Ablation**

↓

**Final contribution synthesis**

---

## Decision

**🟢 CELL 3 PASSED**

The results justify continuing the morphology ↔ radial–angular integration
experiment.

Proceed to:

# CELL 4 — CROSS-VALIDATED RADIAL–ANGULAR RECOVERABILITY FROM MORPHOLOGY

# CLO-SKET — MORPHOLOGY ↔ RADIAL–ANGULAR INTEGRATION
## Cell 4 Scientific Audit — Cross-Validated Morphology → Radial–Angular Information

### Status

**🟢 CELL 4 PASSED**

Cell 4 provides the first out-of-sample estimate of how much of the
radial–angular representation is recoverable from the frozen
135-dimensional morphology representation.

This is substantially stronger evidence than Cell 3.

Cell 3 established:

> morphology and radial–angular quantities are statistically associated.

Cell 4 now establishes:

> morphology contains measurable predictive information about each of the
> four radial–angular quantities, but substantial variation remains
> unexplained.

The analysis remains:

- sketch aligned;
- category-label free;
- domain locked;
- strictly out-of-sample;
- based on the frozen 135-D morphology representation.

---

# 1. Experimental Question

The central question is:

> How much radial–angular information can be recovered from morphology
> alone?

Four targets were evaluated:

1. `F2_peak_magnitude`
2. `F2_peak_radius`
3. `R2_at_F2_peak`
4. `axial_error`

The predictors were the complete frozen:

`2300 × 135`

morphology matrix.

---

# 2. Experimental Controls

The analysis preserves the previously established radial domain:

`3.50 → 27.50`

with:

`25 circular shells`

and exact:

`F₂ ↔ circular-shell matching`

Maximum mismatch:

`0.000000`

Cross-validation was:

- 5-fold;
- shuffled;
- `random_state = 42`;
- strictly out-of-sample.

Therefore the reported prediction statistics are not training-set fit
statistics.

---

# 3. Primary Result

| Radial–angular target | CV R² | OOF Spearman ρ | Interpretation |
|---|---:|---:|---|
| F₂ peak magnitude | **0.2961** | **0.6415** | strongest morphology recoverability |
| R₂ at F₂ peak | **0.2170** | **0.5377** | substantial shared structure |
| Axial error | **0.1979** | **0.4400** | measurable but incomplete recoverability |
| F₂ peak radius | **0.0594** | **0.3417** | weak variance recovery |

The result is therefore not uniform across the radial–angular
representation.

---

# 4. F₂ Peak Magnitude

Morphology predicts F₂ peak magnitude with:

**CV R² = 0.2961**

**Spearman ρ = 0.6415**

**MAE = 0.01315**

**RMSE = 0.01710**

Thus approximately:

**29.6% of the variance**

is recovered by the present morphology-only model under cross-validation.

This is the strongest recoverability result among the four evaluated
targets.

This agrees with Cell 3, where F₂ peak magnitude also exhibited the
strongest coordinate-level morphology associations.

The two experiments therefore provide convergent evidence that:

> F₂ magnitude and the frozen morphology representation share substantial
> measurable structure.

However:

**70.4% of variance remains in the cross-validated residual.**

Therefore the result does not support complete redundancy.

---

# 5. Observed R₂ at the F₂ Peak

Morphology predicts observed circular strength with:

**CV R² = 0.2170**

**Spearman ρ = 0.5377**

**MAE = 0.1258**

**RMSE = 0.1599**

Approximately:

**21.7% of observed R₂ variance**

is recovered under the present morphology-only model.

This is an important result for the paper backbone.

Cell 3 showed substantial morphology ↔ R₂ associations.

Cell 4 now demonstrates that those associations translate into
out-of-sample predictive information.

However:

**78.3% of R₂ variance remains in the CV residual.**

Therefore observed circular strength is related to morphology but is not
fully captured by the frozen 135-D representation under this model.

---

# 6. Axial Recovery Error

Morphology predicts axial recovery error with:

**CV R² = 0.1979**

**Spearman ρ = 0.4400**

**MAE = 20.15°**

**RMSE = 26.46°**

This is scientifically interesting.

Cell 3 showed relatively weak individual-coordinate associations with
axial error:

`maximum |ρ| = 0.2171`

Yet the complete 135-D morphology representation achieves:

`OOF Spearman ρ = 0.4400`

and:

`CV R² = 0.1979`

This suggests that information associated with recovery reliability is
not concentrated in a single morphology coordinate.

Instead, the morphology representation collectively contains information
about axial recovery behavior.

This is compatible with a distributed morphology signal.

It does not prove one.

---

# 7. F₂ Peak Radius

F₂ peak radius is clearly the least well recovered target in terms of
variance explained.

Results:

**CV R² = 0.0594**

**Spearman ρ = 0.3417**

**MAE = 4.02 radial units**

**RMSE = 5.01 radial units**

Only approximately:

**5.9% of variance**

is recovered by the present morphology-only model.

Thus morphology contains some monotonic information about radial
localization, as indicated by the positive Spearman association, while
recovering relatively little of its absolute variance.

This distinction is important.

A moderate rank correlation does not imply strong quantitative prediction.

---

# 8. Recoverability Hierarchy

By cross-validated variance recovery:

**F₂ peak magnitude**

`R² = 0.296`

↓

**Observed R₂**

`R² = 0.217`

↓

**Axial recovery error**

`R² = 0.198`

↓

**F₂ peak radius**

`R² = 0.059`

This is currently the clearest quantitative description of cross-branch
overlap.

---

# 9. Cell 3 + Cell 4 Convergence

The first two cross-branch experiments now form a coherent evidence chain.

## Cell 3 — Association

Morphology coordinates are associated with radial–angular quantities.

## Cell 4 — Recoverability

Those relationships contain enough joint information to produce
out-of-sample prediction above the mean-prediction baseline for all four
targets.

Together:

> The morphology and radial–angular representations are neither
> statistically independent nor trivially identical.

They exhibit **partial representational overlap**.

That is the strongest wording currently justified.

---

# 10. Residual Structure

Cross-validated residual variance remains substantial:

| Target | Explained variance | Residual variance fraction |
|---|---:|---:|
| F₂ peak magnitude | 29.61% | **70.39%** |
| F₂ peak radius | 5.94% | **94.06%** |
| R₂ at F₂ peak | 21.70% | **78.30%** |
| Axial error | 19.79% | **80.21%** |

This is exactly why Cell 5 matters.

The residual variation is large.

But:

> **large residual variance is not yet evidence of complementary
> information.**

Residual variance can contain:

- nonlinear morphology information missed by the current model;
- noise;
- measurement uncertainty;
- representation-specific information;
- genuinely complementary radial–angular structure.

Cell 4 alone cannot distinguish these possibilities.

---

# 11. Residual ↔ Morphology Audit

Residual correlations with individual morphology coordinates are much
smaller than the original Cell 3 associations.

Maximum residual associations are approximately:

| Target | Maximum residual \|ρ\| |
|---|---:|
| F₂ peak magnitude | 0.140 |
| F₂ peak radius | 0.112 |
| R₂ at F₂ peak | 0.109 |
| Axial error | **0.063** |

This reduction is encouraging.

In particular, axial-error residuals exhibit only very weak remaining
coordinate-wise morphology association.

However, these residual correlations were reported with raw p-values.

Given 135 residual-feature comparisons per target, we should **not use
their p-values as manuscript evidence without multiple-comparison
correction**.

For now the scientifically useful quantity is the small effect magnitude,
not nominal significance.

---

# 12. One Important Statistical Caution

The phrase:

> “variance explained by morphology”

should be qualified in the manuscript.

The current R² values quantify variance recovered by the **specific
morphology-only predictive model used in Cell 4**.

They do not establish the maximum information theoretically recoverable
from the 135-D morphology representation.

Therefore write:

> “The morphology-only model recovered 29.6% of F₂ peak-magnitude
> variance…”

rather than:

> “Morphology contains only 29.6% of F₂ information.”

The second statement would be too strong.

---

# 13. Another Important Point — Model Identity Must Be Locked

Before Cell 4 becomes manuscript-frozen, the exact regression estimator
used for morphology → target prediction must be explicitly recorded.

The output currently locks:

- CV folds;
- shuffle;
- random state;
- predictor matrix;
- targets;

but the displayed audit does not state the regression estimator.

For reproducibility, we need to freeze:

- estimator;
- regularization, if any;
- intercept handling;
- scaling;
- all estimator parameters.

This does **not** invalidate Cell 4.

It is a reproducibility item that should be recorded before final freeze.

---

# 14. What We Can Now Claim

## Supported

1. The frozen morphology representation contains out-of-sample predictive
   information about all four evaluated radial–angular quantities.

2. F₂ peak magnitude is the most recoverable target under the current
   morphology-only model.

3. Observed R₂ is partially recoverable from morphology.

4. Axial recovery error is partially recoverable from morphology.

5. F₂ peak radius shows comparatively weak variance recovery.

6. Substantial cross-validated residual variation remains for every target.

7. Morphology and radial–angular geometry therefore exhibit partial
   representational overlap.

---

# 15. What We Still Cannot Claim

## Not Yet Supported

1. Radial–angular information is complementary to morphology.

2. Radial–angular information improves category discrimination beyond
   morphology.

3. The residuals represent novel geometric information.

4. Residual variation is independent of morphology.

5. The two representations encode different semantic garment properties.

6. Radial–angular geometry causes classification improvement.

7. The linear-model residual is equivalent to morphology-independent
   information.

---

# 16. Most Important Scientific Result So Far

The backbone is becoming much clearer.

We do **not** have:

> morphology versus an unrelated radial descriptor.

We have:

> two representations with measurable but incomplete overlap.

That distinction is important.

The strongest current integration statement is:

> **The frozen morphology representation partially recovers radial–angular
> organization out of sample, but substantial radial–angular variation
> remains unexplained by the morphology-only model.**

This is rigorous and fully supported by Cell 4.

---

# 17. Critical Design of Cell 5

## CELL 5 — RESIDUAL / COMPLEMENTARITY TEST

Cell 5 must be handled carefully.

A simple test such as:

`correlate Cell-4 residuals with category labels`

would not be sufficient.

And generating residuals from one global model fitted to all 2300 samples
would introduce leakage.

The Cell 4 residuals are useful precisely because they are
**out-of-fold residuals**.

We should preserve that structure.

---

# 18. Primary Cell 5 Question

Cell 5 should ask:

> Does radial–angular variation not recovered by morphology retain
> systematic information?

There are two scientifically distinct versions of this question.

### 5A — Representation-Level Residual Structure

Test whether residual radial–angular quantities retain systematic
cross-target structure.

For example:

`residual F₂ magnitude`

↔

`residual R₂`

↔

`residual axial error`

This remains completely category-label free.

This tells us whether unexplained radial–angular variation is internally
structured rather than behaving like arbitrary independent residual noise.

---

### 5B — Category Complementarity

Only after 5A should we introduce category labels and ask the stronger
downstream question:

> Does adding radial–angular information improve category discrimination
> beyond the complete morphology representation?

This is the actual task-level complementarity test.

---

# 19. Recommended Evidence Chain

The cleanest scientific sequence is now:

**CELL 1**

Frozen 135-D morphology

↓

**CELL 2 / 2A**

Exact population and row provenance

↓

**CELL 3**

Cross-branch feature association

↓

**CELL 4**

Cross-validated morphology → radial–angular recoverability

↓

# **CELL 5A**
## Residual radial–angular structure

↓

# **CELL 5B**
## Controlled morphology + radial–angular complementarity

↓

**CELL 6**

Permutation robustness of incremental gain

↓

**CELL 7**

Feature-family ablation

↓

**CELL 8**

Final integration synthesis

---

# 20. Cell 5A Decision Rule

If the out-of-fold radial–angular residuals retain reproducible internal
structure:

> radial–angular organization contains structured variation not captured by
> the current morphology-only model.

Notice the wording:

**“not captured by the current morphology-only model”**

not:

**“information absent from morphology.”**

That distinction protects the paper from overclaiming.

---

# 21. Cell 5B Decision Rule

The strongest complementarity evidence would be:

`Morphology`

versus:

`Morphology + radial–angular`

using:

- identical CV splits;
- identical classifier;
- identical preprocessing;
- no hyperparameter search;
- no category-based feature selection.

Then calculate:

`ΔBA = BA(Morphology + radial–angular) − BA(Morphology)`

and subsequently test that ΔBA against a permutation null.

If:

`ΔBA > 0`

and survives the permutation test,

then we finally have evidence that:

> radial–angular geometry provides category-discriminative information
> beyond that captured by the frozen morphology representation.

That would be a major backbone result.

---

# CURRENT BACKBONE STATUS

**Frozen 135-D morphology**

🟢

↓

**Exact sketch-level provenance**

🟢

↓

**Morphology ↔ radial–angular association**

🟢

↓

**Out-of-sample radial–angular recoverability**

🟢

↓

**Partial representational overlap**

🟢

↓

**Structured residual information**

⬜ NEXT

↓

**Task-level complementarity**

⬜

↓

**Permutation validation**

⬜

↓

**Final integration claim**

⬜

---

# DECISION

## 🟢 CELL 4 PASSED

The result is scientifically useful and advances the integration backbone.

The key result is not simply that morphology predicts radial–angular
quantities.

The important result is:

> **Recoverability is partial and heterogeneous: F₂ magnitude is relatively
> well captured, observed R₂ and axial recovery error are moderately
> captured, while F₂ radial localization remains weakly recovered by the
> present morphology-only model.**

Proceed to:

# CELL 5A — CROSS-VALIDATED RESIDUAL RADIAL–ANGULAR STRUCTURE AUDIT

# CLO-SKET — MORPHOLOGY ↔ RADIAL–ANGULAR INTEGRATION
## Cell 5 Scientific Audit — Incremental Information Beyond 135-D Morphology

### Status

**🔴 CELL 5, AS CURRENTLY FORMULATED, DOES NOT TEST THE INTENDED QUESTION**

The numerical result is essentially:

> **ΔR² = 0**

but there is a more fundamental issue than the null result.

The experiment contains a **self-prediction construction**.

The baseline predictors are:

`135-D morphology`

while the targets are:

`PCA coordinates derived from that same 135-D morphology`.

Therefore the morphology-only model is being asked to predict a
transformation of information already present in its own input.

This explains the near-perfect recovery of the leading PCs:

| PC | Morphology-only R² | Morphology + RA R² | ΔR² |
|---:|---:|---:|---:|
| 1 | 0.999860 | 0.999860 | ~0 |
| 2 | 0.995814 | 0.995814 | ~0 |
| 3 | 0.992665 | 0.992665 | ~0 |
| 4 | 0.976102 | 0.976103 | ~0 |

The experiment therefore cannot be used as the primary test of whether
radial–angular geometry contains information complementary to morphology.

---

# 1. Why the Near-Perfect R² Occurs

PCA defines each morphology PC as a linear transformation of the
morphology vector:

\[
z_k = \mathbf{x}^{T}\mathbf{w}_k
\]

where:

- \(\mathbf{x}\) is the 135-D morphology vector;
- \(\mathbf{w}_k\) is the PCA loading vector;
- \(z_k\) is the corresponding PC score.

The baseline model receives \(\mathbf{x}\) itself.

It is therefore being asked to learn:

\[
\mathbf{x}
\rightarrow
\mathbf{x}^{T}\mathbf{w}_k
\]

which is essentially the transformation used to construct the target.

For a sufficiently appropriate linear predictor, this mapping is nearly
deterministic.

Consequently:

> the extremely high R² for the leading morphology PCs is expected from
> the experimental construction.

It should not be interpreted as evidence that radial–angular information
is redundant.

---

# 2. The Fold-Wise PCA Does Not Solve This Problem

It was correct to fit PCA using only the training fold.

That protects against:

**test-set leakage during PCA estimation.**

However, it does not remove the deeper problem.

For each test observation:

- its 135 morphology coordinates are given to the predictor;
- its target PC score is calculated from those same 135 coordinates using
  the training-fold PCA transformation.

Thus the target remains a deterministic transformation of the predictor
space.

So:

> **there is no conventional train/test leakage, but there is target-input
> circularity for the scientific question being asked.**

That distinction should be explicitly recorded.

---

# 3. Therefore the Current ΔR² ≈ 0 Has a Narrow Meaning

The observed result is:

**Mean morphology-only R² = 0.4653**

**Mean morphology + RA R² = 0.4653**

**Mean ΔR² ≈ 0**

**Median ΔR² ≈ 0**

with individual changes on the order of approximately:

\[
10^{-6}
\]

This establishes only that:

> radial–angular descriptors do not improve reconstruction of morphology
> PCA coordinates when the complete morphology vector used to construct
> those coordinates is already supplied to the model.

That result is mathematically unsurprising.

It does **not** establish that radial–angular descriptors contain no
complementary information.

---

# 4. Why the Mean R² = 0.4653 Is Also Misleading

The average is strongly affected by highly heterogeneous PC behavior.

For example:

`PC7 R² = -1.3544`

while:

`PC1 R² = 0.9999`

A simple mean across PCs therefore mixes:

- almost deterministic leading-PC reconstruction;
- moderately recoverable PCs;
- poorly recoverable PCs;
- a PC performing substantially below the mean-prediction baseline.

Furthermore, the first ten PCs retain only approximately:

`58.3%–58.5%`

of morphology variance within folds.

Therefore the mean PC-level R² should not be treated as a single
representation-level measure of morphology reconstruction.

---

# 5. Cell 5 Does NOT Overturn Cell 4

This is important.

Cell 4 asked:

> **Can morphology predict radial–angular quantities?**

That is a legitimate cross-representation question:

\[
M \rightarrow R
\]

where:

- \(M\) = morphology;
- \(R\) = radial–angular quantity.

Cell 5 instead asks:

\[
[M,R] \rightarrow PCA(M)
\]

versus:

\[
M \rightarrow PCA(M)
\]

But because \(PCA(M)\) is generated from \(M\), the baseline already
contains the information required to construct its target.

Therefore Cell 5 cannot determine whether the unexplained radial–angular
variation discovered in Cell 4 is complementary.

---

# 6. What Cell 4 Actually Established

Cell 4 remains scientifically informative:

| Radial–angular target | Morphology-only CV R² |
|---|---:|
| F₂ peak magnitude | **0.2961** |
| F₂ peak radius | **0.0594** |
| Observed R₂ | **0.2170** |
| Axial error | **0.1979** |

Thus substantial radial–angular variance remained unexplained by the
tested morphology model:

| Target | Approx. residual variance |
|---|---:|
| F₂ peak magnitude | **70.4%** |
| F₂ peak radius | **94.1%** |
| Observed R₂ | **78.3%** |
| Axial error | **80.2%** |

The unresolved question remains:

> Is this residual variation structured and scientifically useful, or is
> it merely model misspecification/noise?

Cell 5 as currently designed cannot answer that.

---

# 7. Correct Scientific Interpretation of Current Cell 5

## Supported

The current experiment supports:

> Addition of the compact 28-D radial–angular representation produces
> essentially no incremental improvement in predicting morphology-derived
> PCA coordinates when the complete 135-D morphology representation is
> already included as a predictor.

That is all.

---

# 8. Claims That Are NOT Supported

The current experiment does **not** support:

- radial–angular geometry is redundant with morphology;
- radial–angular geometry contains no unique information;
- morphology completely explains radial–angular structure;
- the two representations are equivalent;
- radial–angular descriptors cannot improve category discrimination;
- radial–angular descriptors provide no complementary information;
- Cell 4 residual variation is noise.

These claims would exceed the experiment.

---

# 9. Important Decision About Cell 6

## 🔴 DO NOT RUN THE PLANNED PERMUTATION TEST ON THIS ΔR²

A permutation test would answer whether the approximately zero increment
from this particular self-reconstruction setup differs from an appropriate
null.

But the scientific target itself is not the complementarity question we
care about.

Permutation testing cannot repair an experimental estimand that does not
represent the intended scientific question.

Therefore:

> **Do not spend computation validating the current Cell 5 ΔR².**

We should redesign Cell 5 first.

---

# 10. What We Actually Need to Test

The paper's backbone requires two different complementarity questions.

## Question A — Representation-Level Complementarity

> Does the radial–angular branch contain structured variation not captured
> by morphology under an out-of-sample mapping?

This remains category-label free.

## Question B — Task-Level Complementarity

> Does radial–angular geometry improve category discrimination beyond
> morphology?

This introduces category labels only after the representation-level audit.

These should not be conflated.

---

# 11. Correct Replacement: Cell 5A

# CELL 5A — CROSS-VALIDATED RESIDUAL RADIAL–ANGULAR STRUCTURE

Use the out-of-fold residuals already generated in Cell 4:

\[
e_R = R - \hat{R}(M)
\]

for:

- F₂ peak magnitude;
- F₂ peak radius;
- observed R₂;
- axial error.

Then determine whether these residual quantities exhibit reproducible
structure.

The question becomes:

> After removing the component predictable from morphology under the
> current out-of-sample model, does the remaining radial–angular variation
> exhibit systematic relationships?

---

# 12. Cell 5A Primary Tests

Construct the four OOF residual vectors:

`e_F2_magnitude`

`e_F2_radius`

`e_R2`

`e_axial_error`

Then compute the complete residual association matrix using:

**Spearman ρ**

with:

**bootstrap 95% confidence intervals**

and appropriate:

**multiple-comparison correction.**

The important comparisons include:

\[
e_{R2}
\leftrightarrow
e_{\text{axial error}}
\]

\[
e_{F2 magnitude}
\leftrightarrow
e_{\text{axial error}}
\]

\[
e_{F2 radius}
\leftrightarrow
e_{\text{axial error}}
\]

and the remaining residual pairs.

---

# 13. Why This Test Matters

Suppose the original relationship:

\[
R_2 \leftrightarrow \text{axial error}
\]

exists only because both quantities reflect morphology.

Then after morphology prediction is removed, we would expect the residual
association to collapse substantially.

But suppose:

\[
e_{R2}
\leftrightarrow
e_{\text{axial error}}
\]

remains reproducibly associated.

Then we can say:

> **The radial–angular relationship is not fully accounted for by the
> component recoverable from the tested morphology model.**

That would be a genuinely interesting representation-level result.

Still, we should not call it strict statistical independence from
morphology.

---

# 14. Stronger Version of Cell 5A

There is one additional robustness test worth adding.

Cell 4 appears to use one particular morphology → radial–angular
predictor.

If that predictor is linear, residual variation may simply reflect
nonlinear morphology information.

Therefore Cell 5A should ideally compare:

### Model 1
A simple/linear morphology predictor.

### Model 2
A controlled nonlinear morphology predictor.

Not for optimization.

Not for leaderboard performance.

But as a **sensitivity analysis**.

If substantial radial–angular residual structure survives both, the
complementarity argument becomes much stronger.

---

# 15. Then Cell 5B — The Decisive Downstream Test

After Cell 5A, perform:

# CONTROLLED CATEGORY COMPLEMENTARITY

Compare:

### Morphology only

\[
M
\]

against:

### Radial–angular only

\[
R
\]

and:

### Morphology + radial–angular

\[
[M,R]
\]

using exactly the same:

- 5 stratified folds;
- random state;
- classifier;
- scaling protocol;
- no hyperparameter search;
- no feature selection.

Primary statistic:

\[
\Delta BA =
BA(M+R)-BA(M)
\]

This directly answers:

> Does radial–angular geometry contribute category-discriminative
> information beyond morphology?

---

# 16. This Will Give Us the Important 3-Way Result

There are several scientifically meaningful possibilities.

### Scenario 1

`Morphology + RA > Morphology`

Then radial–angular geometry has downstream complementary value.

### Scenario 2

`Morphology + RA ≈ Morphology`

but Cell 5A residual structure survives.

Then radial–angular geometry contains representation-level structure that
does not materially improve this particular category task.

### Scenario 3

Both residual structure and category gain disappear.

Then the radial–angular branch may primarily be an interpretable
re-expression of morphology.

### Scenario 4

Category gain survives strongly even though cross-representation overlap
is substantial.

This would be particularly interesting:

> partially overlapping representations can still contain useful
> task-specific complementary information.

---

# 17. One More Important Audit Before Continuing

Cell 4's exact estimator still needs to be printed and frozen.

Before Cell 5A, record:

```text
Estimator class
Estimator parameters
Scaling
Regularization
Multi-output strategy
Random state, if applicable