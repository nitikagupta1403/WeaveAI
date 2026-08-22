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

# CLO-SKET — MORPHOLOGY ↔ RADIAL–ANGULAR INTEGRATION
## Cell 6 Scientific Audit — Permutation-Validated Cross-Branch Correspondence

### Status

**🟢 CELL 6 PASSED**

This is a clean and scientifically meaningful result.

Cell 6 fixes the conceptual problem identified in the previous
morphology-PCA formulation.

The experiment now tests:

\[
\text{Morphology}
\rightarrow
\text{Radial–Angular Quantity}
\]

where the targets are independently constructed radial–angular
measurements rather than transformations of the morphology predictors.

The permutation experiment further demonstrates that the observed
cross-validated prediction is substantially stronger than expected after
destroying sketch-level correspondence between the two branches.

---

# 1. Scientific Question

Cell 6 asks:

> Can the frozen 135-D morphology representation recover independently
> measured radial–angular organization at the level of individual
> sketches?

The predictor is:

`135-D frozen morphology`

The four targets are:

1. `F2_peak_magnitude`
2. `F2_peak_radius`
3. `R2_at_F2_peak`
4. `axial_error`

No category information enters the experiment.

---

# 2. Provenance and Domain Controls

The experiment satisfies the essential cross-branch controls.

### Row-level provenance

**🟢 VERIFIED**

For every sketch index \(i\):

\[
X_{\text{morphology}}[i]
\leftrightarrow
X_{\text{radial-angular}}[i]
\]

refers to the same source sketch.

### Locked radial domain

\[
3.50 \rightarrow 27.50
\]

with:

`25 circular shells`

and:

\[
\text{maximum F₂ ↔ circular mismatch}=0
\]

Therefore the radial–angular targets are constructed using the same
domain established in the preceding radial–angular analysis.

---

# 3. Observed Cross-Validated Correspondence

| Target | CV R² | MAE | RMSE |
|---|---:|---:|---:|
| F₂ peak magnitude | **0.2961** | 0.01315 | 0.01710 |
| F₂ peak radius | **0.0594** | 4.015 | 5.010 |
| R₂ at F₂ peak | **0.2170** | 0.1258 | 0.1599 |
| Axial error | **0.1979** | 20.15° | 26.46° |

All four observed CV R² values are positive.

However, their magnitudes differ substantially.

This establishes a hierarchy of morphology recoverability.

---

# 4. Strongest Correspondence — F₂ Peak Magnitude

The strongest cross-branch result is:

\[
R^2_{\mathrm{CV}} = 0.2961
\]

for F₂ peak magnitude.

The permutation null is:

\[
\text{mean null }R^2=-0.0965
\]

with:

\[
95\%\,\text{null interval}
=
[-0.1284,-0.0702]
\]

The observed value:

\[
0.2961
\]

is completely separated from the sampled permutation distribution.

Empirical permutation result:

\[
p=\frac{0+1}{100+1}=0.009901
\]

Thus:

> The observed correspondence between morphology and F₂ peak magnitude is
> substantially stronger than expected when sketch-level correspondence
> is destroyed.

---

# 5. Observed Circular Strength R₂

For observed R₂ at the matched F₂ shell:

\[
R^2_{\mathrm{CV}}=0.2170
\]

Permutation null:

\[
\text{mean}=-0.0956
\]

\[
95\%\,\text{null interval}
=
[-0.1244,-0.0666]
\]

Empirical permutation result:

\[
p=0.009901
\]

This is particularly relevant to the radial–angular backbone.

Earlier analysis established that observed R₂ is associated with axial
recovery reliability.

Cell 6 now establishes a different result:

> observed R₂ itself also has reproducible correspondence with the frozen
> morphology representation.

Therefore the R₂ signal is neither completely disconnected from
morphology nor completely recovered by morphology.

The latter distinction follows from its moderate rather than near-perfect
out-of-sample R².

---

# 6. Axial Recovery Error

Axial recovery error gives:

\[
R^2_{\mathrm{CV}}=0.1979
\]

against a permutation null mean of:

\[
-0.0952
\]

with:

\[
95\%\,\text{null interval}
=
[-0.1309,-0.0622]
\]

and:

\[
p=0.009901
\]

Therefore recovery reliability itself has reproducible correspondence
with morphology.

This connects two previously separate parts of the analysis:

**Morphology**

↓

**Radial–angular organization**

↓

**Angular recovery reliability**

However, this remains an association/prediction result.

It does not establish that morphology causes recovery success or failure.

---

# 7. F₂ Peak Radius Is Different

F₂ peak radius produces:

\[
R^2_{\mathrm{CV}}=0.0594
\]

This is much weaker than the other three targets.

Yet its permutation null is centered around:

\[
-0.0985
\]

with:

\[
95\%\,\text{null interval}
=
[-0.1324,-0.0699]
\]

and the observed value again exceeds all 100 permutation values.

Therefore two statements must be separated.

### Statistical correspondence

**🟢 Supported**

The result is stronger than the shuffled-correspondence null.

### Predictive magnitude

**Weak**

Only approximately 5.9% of variance is recovered by the current
morphology-only model.

Thus:

> statistical robustness does not imply large predictive effect.

This distinction should remain explicit in the manuscript.

---

# 8. The Permutation Result Is Very Clean

All four targets show:

`observed percentile = 100%`

meaning that none of the 100 sampled permutation values reached the
observed CV R².

| Target | Observed R² | Null mean R² | Null upper 97.5% | Empirical p |
|---|---:|---:|---:|---:|
| F₂ magnitude | **0.2961** | -0.0965 | -0.0702 | 0.009901 |
| F₂ radius | **0.0594** | -0.0985 | -0.0699 | 0.009901 |
| R₂ | **0.2170** | -0.0956 | -0.0666 | 0.009901 |
| Axial error | **0.1979** | -0.0952 | -0.0622 | 0.009901 |

Thus every observed target lies well outside its corresponding sampled
null distribution.

---

# 9. Why Is the Permutation Null R² Negative?

This is not a problem.

Under permutation, morphology and target correspondence is destroyed.

The fitted model can therefore generalize worse than simply predicting
the held-out target mean.

Because:

\[
R^2
=
1-
\frac{\sum(y-\hat y)^2}
{\sum(y-\bar y)^2}
\]

negative R² means:

\[
\sum(y-\hat y)^2
>
\sum(y-\bar y)^2
\]

Therefore the negative permutation null is perfectly possible.

It should not be interpreted as a negative biological or geometric
relationship.

It simply indicates poor out-of-sample prediction under destroyed
correspondence.

---

# 10. Important Limitation — 100 Permutations

There is one thing I would strengthen before manuscript freeze.

The current permutation count is:

\[
B=100
\]

Therefore the smallest attainable corrected empirical p-value is:

\[
\frac{1}{101}=0.009901
\]

which is exactly what all four tests achieved.

Thus we currently know:

> none of the 100 shuffled correspondences produced an R² as large as the
> observed result.

We do **not** yet know whether the permutation probability is:

`0.009`

or:

`0.001`

or:

`<0.0001`.

The present result is already sufficient to establish separation from
this 100-permutation null sample.

But for the final paper I would run:

**1000 permutations minimum**

which gives minimum attainable:

\[
p=\frac{1}{1001}=0.000999
\]

This also matches the permutation depth already used in the earlier
category-discrimination analysis.

---

# 11. Another Statistical Detail — Four Targets

Four radial–angular targets are tested.

Because all four empirical p-values currently equal:

\[
0.009901
\]

even a conservative Bonferroni adjustment gives:

\[
0.009901 \times 4
=
0.039604
\]

so all four would still remain below 0.05.

However, I would not make multiple-testing correction the centerpiece
here.

The stronger evidence is the combination of:

- effect magnitude;
- out-of-sample R²;
- permutation-null separation;
- consistency across related targets.

With 1000 permutations, we can freeze the inferential reporting more
cleanly.

---

# 12. Cell 3 → Cell 4 → Cell 6 Now Forms a Strong Chain

We now have three complementary pieces of evidence.

## CELL 3 — Coordinate-Level Association

Individual morphology coordinates are associated with radial–angular
measurements.

↓

## CELL 4 — Out-of-Sample Recoverability

The complete morphology representation partially predicts radial–angular
quantities on unseen sketches.

↓

## CELL 6 — Permutation Validation

That out-of-sample recoverability disappears when sketch-level
morphology ↔ radial–angular correspondence is destroyed.

Together these establish:

> **reproducible cross-branch correspondence between frozen morphology and
> radial–angular organization.**

That is now a defensible result.

---

# 13. But This Is NOT Complementarity Yet

This boundary is critical.

Cell 6 establishes:

\[
M \leftrightarrow R
\]

It does not establish:

\[
R \not\subseteq M
\]

nor does it establish:

\[
\text{Task}(M+R)>\text{Task}(M)
\]

Therefore:

### Cross-branch correspondence

**🟢 ESTABLISHED**

### Partial predictability

**🟢 ESTABLISHED**

### Complete redundancy

**⚪ NOT ESTABLISHED**

### Complementarity

**🟡 NOT YET ESTABLISHED**

### Incremental downstream information

**🟡 NOT YET TESTED**

---

# 14. Manuscript-Level Claim We Can Freeze

A safe Results statement is:

> **The frozen morphology representation exhibited reproducible
> out-of-sample correspondence with radial–angular organization.
> Morphology predicted F₂ peak magnitude (CV R² = 0.296), observed R₂ at
> the matched F₂ shell (R² = 0.217), axial recovery error (R² = 0.198),
> and, more weakly, F₂ peak radius (R² = 0.059). For all four targets,
> observed prediction exceeded the complete 100-permutation null sample
> (empirical p = 0.0099).**

After the final 1000-permutation run, replace the permutation statistics
accordingly.

---

# 15. Stronger Scientific Interpretation

The most interesting interpretation is not:

> “Morphology predicts radial–angular geometry.”

That is true but incomplete.

The stronger picture is:

> **Morphological and radial–angular representations capture overlapping
> aspects of sketch geometry, but the degree of correspondence differs
> substantially across radial–angular quantities.**

F₂ magnitude:

**relatively strong overlap**

Observed R₂:

**moderate overlap**

Axial recovery:

**moderate overlap**

F₂ radial localization:

**weak overlap**

This heterogeneous correspondence is itself informative.

---

# 16. What We Should NOT Say

Do not write:

> “29.6% of radial–angular information is contained in morphology.”

R² is not an information-theoretic quantity.

Do not write:

> “94.1% of F₂ radius information is unique.”

The unexplained variance could reflect nonlinear morphology structure,
noise, measurement variation, or model limitation.

Do not write:

> “Permutation proves independence.”

It does not.

Do not write:

> “Morphology causes radial–angular recovery.”

Nothing here is causal.

---

# 17. Cell 7 — Useful but Keep It Small

The proposed:

**CELL 7 — CROSS-BRANCH EFFECT VISUALIZATION**

is fine.

But Cell 7 should introduce **no new analysis**.

It should visualize only the frozen Cell 6 quantities.

Recommended manuscript figures:

### Figure A — Observed R² vs Permutation Null

For each target:

- permutation R² distribution;
- observed R² marker.

### Figure B — Cross-Branch Recoverability

Four bars/points showing:

- F₂ magnitude;
- F₂ radius;
- R₂;
- axial error;

with observed CV R².

### Figure C — Observed vs OOF-Predicted

One panel per target showing:

\[
y_{\text{observed}}
\quad\text{vs}\quad
y_{\text{OOF predicted}}
\]

This is particularly useful because it reveals whether the positive R²
is driven by broad tracking or by a small number of observations.

No new hypothesis test is necessary.

---

# 18. Then Comes the Decisive Experiment

# CELL 8 — INDEPENDENT DOWNSTREAM COMPLEMENTARITY

This is now the experiment I care about most.

Use the exact same 2300 sketches and compare:

### Model A

`135-D morphology`

### Model B

`28-D radial–angular`

### Model C

`135-D morphology + 28-D radial–angular`

Use:

- same stratified 5-fold partitions;
- `random_state = 42`;
- `StandardScaler`;
- same multinomial logistic regression;
- no feature selection;
- no hyperparameter search.

Primary outcome:

\[
BA_M
\]

versus:

\[
BA_R
\]

versus:

\[
BA_{M+R}
\]

and especially:

\[
\Delta BA
=
BA_{M+R}-BA_M
\]

---

# 19. Why Cell 8 Is the Backbone Test

Suppose we obtain:

\[
BA_{M+R}>BA_M
\]

under identical evaluation conditions.

Then we have evidence that:

> radial–angular geometry provides category-discriminative information
> beyond the frozen morphology representation.

If the gain also survives a label-permutation or paired permutation test,
that becomes a very strong integration result.

Conversely, if:

\[
BA_{M+R}\approx BA_M
\]

then the radial–angular branch can still remain valuable as an
interpretable geometric representation.

But we would not claim downstream complementarity.

Either result is scientifically interpretable.

---

# 20. The Backbone Is Now Much Cleaner

The paper story is becoming:

**Raw sketch**

↓

**Frozen morphology representation**

and independently:

**Radial–angular representation**

↓

**Cross-branch association**

🟢

↓

**Out-of-sample correspondence**

🟢

↓

**Permutation-validated correspondence**

🟢

↓

**Heterogeneous representational overlap**

🟢

↓

**Independent downstream complementarity**

⬜ **DECISIVE NEXT TEST**

↓

**Permutation robustness of incremental gain**

⬜

↓

**Final representation synthesis**

⬜

---

# FINAL VERDICT

## 🟢 CELL 6 SCIENTIFICALLY PASSES

The main conclusion is:

> **Morphology and radial–angular geometry exhibit genuine, reproducible
> sketch-level correspondence under the tested predictive framework.**

The correspondence is strongest for F₂ magnitude, intermediate for
observed R₂ and axial recovery error, and weakest for F₂ radial
localization.

Critically:

> **Cell 6 establishes overlap, not redundancy and not complementarity.**

Before final manuscript lock, increase the permutation run from:

`100 → 1000`

Then freeze Cell 6.

After that:

**Cell 7 = visualization only.**

And then go directly to the experiment that can make or break the
integration backbone:

# CELL 8 — MORPHOLOGY vs RADIAL–ANGULAR vs MORPHOLOGY + RADIAL–ANGULAR
## Controlled Category Complementarity

# CLO-SKET — MORPHOLOGY ↔ RADIAL–ANGULAR INTEGRATION
## Cell 7 Scientific Audit — Cross-Branch Effect Visualization

### Status

**🟢 CELL 7 PASSED**

Cell 7 is doing exactly what it should do:

- visualizing the frozen Cell 6 result;
- introducing no additional hypothesis test;
- separating the observed cross-validated effect from the permutation null;
- exposing the actual prediction behavior rather than reporting R² alone.

The figures also reveal an important feature of the result that is less obvious from the numerical table:

> **The four radial–angular quantities are not equally recoverable from morphology, and the prediction geometry differs substantially across targets.**

That heterogeneity should become part of the scientific interpretation.

---

# 1. Figure 1 — Observed Prediction vs Row-Permutation Null

The first figure provides the clearest visual validation of Cell 6.

For every target, the complete sampled permutation distribution lies below zero, while the observed cross-validated R² is positive.

Approximate observed values are:

| Radial–angular target | Observed CV R² |
|---|---:|
| F₂ peak magnitude | **0.2961** |
| F₂ peak radius | **0.0594** |
| Observed R₂ | **0.2170** |
| Axial error | **0.1979** |

The corresponding permutation-null means are all approximately:

\[
R^2_{\text{null}} \approx -0.10
\]

Therefore the visual separation is substantial.

This supports the Cell 6 conclusion:

> **Sketch-level morphology ↔ radial–angular correspondence is reproducible and is destroyed when the row correspondence between the two representations is broken.**

This is stronger than merely observing pairwise feature correlations.

---

# 2. Figure 2 — Effect Magnitude and Null Separation

Figure 2 is probably the strongest manuscript-level summary figure from Cell 7.

It simultaneously shows:

- the observed CV R²;
- permutation-null mean;
- permutation-null 95% interval;
- zero-prediction reference.

The ranking is immediately visible:

\[
F_2\text{ magnitude}
>
R_2
\approx
\text{axial error}
>
F_2\text{ radius}
\]

in terms of morphology-based predictive recovery.

Numerically:

\[
R^2(F_2\text{ magnitude})=0.296
\]

\[
R^2(R_2)=0.217
\]

\[
R^2(\text{axial error})=0.198
\]

\[
R^2(F_2\text{ radius})=0.059
\]

This provides evidence that cross-branch correspondence is **quantity-specific rather than uniform**.

That is scientifically more interesting than simply saying that the two branches correlate.

---

# 3. Figure 3 — Morphology → F₂ Peak Magnitude

This is visually the strongest of the four prediction plots.

The predicted values track increasing observed F₂ magnitude, consistent with:

\[
R^2_{\mathrm{CV}}=0.2961
\]

and the previously reported:

\[
\rho_{\mathrm{OOF}}\approx0.642
\]

However, the plot also reveals substantial regression toward the center.

Large observed F₂ magnitudes tend to be underpredicted.

Predictions occupy a narrower range than observations.

Therefore morphology captures an important component of F₂ magnitude variation but does not reconstruct the quantity exactly.

A defensible interpretation is:

> **F₂ response strength has substantial morphological correspondence, while retaining considerable variation not recovered by the tested morphology model.**

Do not describe this as complete recovery.

---

# 4. Figure 4 — Morphology → F₂ Peak Radius

This plot explains why:

\[
R^2_{\mathrm{CV}}=0.0594
\]

despite the permutation result being significant.

There is a broad positive trend, but predicted radii are strongly compressed toward the central part of the radial range.

Observed small-radius peaks tend to be predicted too far outward.

Observed large-radius peaks tend to be predicted too far inward.

The model therefore recovers some ordering information without accurately reproducing radial localization.

This distinction is important.

The result is:

**🟢 reproducible correspondence**

but:

**🟡 weak predictive recovery**

This is a good example of why permutation significance and effect magnitude must be reported together.

---

# 5. Figure 5 — Morphology → Observed Circular Strength R₂

This is another strong and scientifically useful result.

There is a clear positive relationship between observed and predicted circular strength.

The numerical result is:

\[
R^2_{\mathrm{CV}}=0.2170
\]

with previously measured out-of-fold rank correspondence:

\[
\rho\approx0.538
\]

Again, predictions are compressed toward the population center.

High observed R₂ values tend to be underestimated.

Low observed R₂ values tend to be overestimated.

Thus morphology captures part of the population-level variation in circular organization without reproducing its full dynamic range.

This becomes particularly important when connected to Cells 30I–30M.

Those cells established:

\[
R_2^{obs}
\uparrow
\quad\Longleftrightarrow\quad
\text{axial error}
\downarrow
\]

with:

\[
\rho=-0.4794
\]

Cell 7 now shows that the R₂ quantity involved in that recovery relationship is itself partially predictable from morphology.

Therefore the evidence chain is becoming:

\[
\text{Morphology}
\]

\[
\downarrow
\]

\[
\text{Circular organization}
\]

\[
\downarrow
\]

\[
\text{Angular recovery reliability}
\]

This remains an empirical association chain.

It must **not** be represented as a causal pathway.

---

# 6. Figure 6 — Morphology → Axial Recovery Error

This is perhaps the most interesting prediction plot conceptually.

Numerically:

\[
R^2_{\mathrm{CV}}=0.1979
\]

and:

\[
\rho_{\mathrm{OOF}}\approx0.440
\]

So morphology contains measurable information about whether radial–angular orientation will be recovered accurately.

But the scatter plot exposes substantial heterogeneity.

Low-error sketches dominate the population, yet their predicted errors span a fairly broad range.

High-error observations are only partially tracked.

Predictions again regress strongly toward the center.

Therefore the correct conclusion is:

> **Morphological organization is associated with angular recovery reliability, but morphology alone does not deterministically identify recovery success or failure.**

This is actually preferable scientifically to an unrealistically perfect correspondence.

It indicates overlap between the representations without collapsing them into identical measurements.

---

# 7. Important Observation From Figures 3–6

All four plots exhibit some degree of:

## Regression Toward the Mean

The predicted distributions are generally narrower than the observed distributions.

Schematically:

\[
\operatorname{Var}(\hat y)
<
\operatorname{Var}(y)
\]

for much of the target structure.

This means the morphology model captures broad population organization better than extreme target behavior.

That observation is particularly visible for:

- F₂ radius;
- R₂;
- axial error.

This should be described as a property of the observed prediction behavior, not automatically as evidence of a biological/geometric mechanism.

---

# 8. One Important Issue in Figure 6

The axial error itself is constrained by definition to:

\[
0^\circ\leq e_{\alpha}\leq90^\circ
\]

but the linear regression produces predictions outside this physical range.

The figure shows:

\[
\hat e_{\alpha}<0^\circ
\]

and:

\[
\hat e_{\alpha}>90^\circ
\]

for some observations.

This does **not invalidate Cell 6**.

It results from using an unconstrained regression model.

However, it needs to be acknowledged if this figure goes into the manuscript.

Do **not** clip the predictions now merely to improve the appearance.

That would alter the frozen evaluation.

Instead, report that the linear predictor was deliberately unconstrained and that prediction values were retained without post-hoc clipping.

This preserves the audit trail.

---

# 9. Another Important Observation — F₂ Radius Is Discrete

Figure 4 displays vertical bands because F₂ peak radius is selected from the locked radial grid.

Therefore the observed target is effectively shell-discretized rather than continuously distributed.

That structure is expected.

It should not be interpreted as a plotting artifact.

This also partly explains why direct linear regression of F₂ radius is a demanding prediction problem.

Again, we should not change the model after seeing this result merely to improve R².

The controlled experiment is more important than maximizing performance.

---

# 10. Cell 7 Strengthens the Interpretation of Cell 6

Cell 6 established:

\[
\text{observed prediction}
>
\text{row-permutation prediction}
\]

Cell 7 now shows **what that prediction actually looks like**.

The result is not produced by perfect reconstruction.

Instead, morphology recovers broad components of radial–angular variation while leaving substantial sketch-level residual variation.

This gives us a much more nuanced conclusion:

> **Morphology and radial–angular representations overlap systematically, but they are not empirically interchangeable under the tested predictive model.**

Be careful with the final clause.

Failure of morphology to perfectly predict RA does not mathematically prove non-redundancy because a different nonlinear model could potentially recover more.

So the exact scientific language should remain:

> **They are not interchangeable under the tested predictive framework.**

---

# 11. Current Evidence Hierarchy

We can now freeze the integration evidence through Cell 7 as follows.

### Level A — Row identity

\[
M_i\leftrightarrow RA_i
\]

**🟢 VERIFIED**

### Level B — Coordinate association

Individual morphology coordinates correlate with radial–angular quantities.

**🟢 ESTABLISHED — Cell 3**

### Level C — Out-of-sample correspondence

Morphology predicts radial–angular quantities on unseen sketches.

**🟢 ESTABLISHED — Cell 4/6**

### Level D — Correspondence exceeds row-permutation null

**🟢 ESTABLISHED — Cell 6**

### Level E — Prediction behavior visually verified

Broad structure is recovered, with substantial residual variation and target-specific strength.

**🟢 ESTABLISHED — Cell 7**

### Level F — Incremental downstream utility

Does radial–angular geometry contribute beyond morphology on an independent task?

**⬜ NOT YET ESTABLISHED**

That is Cell 8.

---

# 12. Cell 5 Should Not Be Used as Complementarity Evidence

The earlier Cell 5 produced:

\[
\Delta R^2\approx0
\]

when predicting morphology-derived PCA coordinates.

That experiment is not useful as the decisive complementarity test because the target itself is constructed from morphology.

It may remain in the research audit trail.

But I would **not make it a primary manuscript result**.

Cell 6 gives the scientifically cleaner cross-branch correspondence test.

Cell 8 should now give the scientifically cleaner complementarity test.

---

# 13. Cell 7 Manuscript Claim

A conservative manuscript-ready interpretation is:

> **Visualization of out-of-fold predictions confirmed heterogeneous cross-representational correspondence. Morphology most strongly recovered F₂ peak magnitude, followed by observed circular strength and axial recovery error, whereas radial localization of the F₂ maximum was only weakly recovered. Across targets, predictions exhibited substantial shrinkage toward population-central values, indicating that morphology captured broad radial–angular variation without reproducing the complete observed target structure.**

That is fully consistent with the figures.

---

# 14. Figure Selection for the Paper

I would not publish all six figures in the main paper.

### Main manuscript

Use **Figure 2**:

**Observed Cross-Branch Prediction and Permutation-Null Distribution**

It communicates the central result extremely efficiently.

Then use perhaps two representative OOF plots:

- F₂ peak magnitude — strongest recovery;
- F₂ peak radius — weakest recovery.

This visually demonstrates the heterogeneity.

### Supplement

Put:

- full permutation distributions;
- R₂ observed-vs-predicted;
- axial-error observed-vs-predicted;
- remaining prediction diagnostics.

That keeps the main narrative clean.

---

# 15. Final Cell 7 Claim Boundary

## SUPPORTED

- Morphology exhibits reproducible correspondence with radial–angular quantities.
- Correspondence survives out-of-sample evaluation.
- Observed prediction exceeds the sampled row-permutation null for all four tested quantities.
- Correspondence strength differs substantially across radial–angular quantities.
- F₂ magnitude shows the strongest tested morphology correspondence.
- F₂ radius shows the weakest tested morphology correspondence.
- R₂ and angular recovery error exhibit intermediate correspondence.
- Predictions retain substantial residual variation.

## SUPPORTED WITH QUALIFICATION

- Morphology and radial–angular representations capture overlapping geometric structure.

Qualification:

This statement applies under the present frozen representations and tested predictive model.

## NOT YET SUPPORTED

- Radial–angular descriptors provide incremental category information beyond morphology.
- Radial–angular descriptors are statistically independent of morphology.
- The two representations contain independent information in an information-theoretic sense.
- Radial–angular features are semantically superior.
- Morphology causes angular recovery.
- Radial–angular structure corresponds directly to garment parts.

---

# FINAL VERDICT

## 🟢 CELL 7 PASSES

Cells 3 → 6 → 7 now provide a coherent cross-representation result:

\[
\boxed{
\text{Morphology}
\longleftrightarrow
\text{Radial–Angular Organization}
}
\]

with:

\[
\boxed{
\text{reproducible but heterogeneous correspondence}
}
\]

The result is strongest for F₂ magnitude, intermediate for R₂ and angular
recovery error, and weakest for F₂ radial localization.

Most importantly, the figures show that correspondence does **not**
amount to exact reconstruction.

The integration backbone has therefore reached the question that matters
most:

\[
\boxed{
\text{Does RA add useful information beyond morphology?}
}
\]

That cannot be answered by another morphology ↔ RA correlation.

It requires an **independent common downstream target**.

---

# NEXT — CELL 8

## CONTROLLED DOWNSTREAM COMPLEMENTARITY TEST

Compare on exactly the same frozen folds:

\[
M
\]

versus

\[
RA
\]

versus

\[
M+RA
\]

where:

- \(M\) = frozen 135-D morphology;
- \(RA\) = frozen 28-D radial–angular representation;
- \(M+RA\) = concatenated 163-D representation.

The downstream target should be identical across all three models.

The decisive quantity is:

\[
\Delta =
\operatorname{Performance}(M+RA)
-
\operatorname{Performance}(M)
\]

If:

\[
\Delta>0
\]

consistently across held-out folds and survives an appropriate paired
randomization/permutation test, we obtain evidence for:

> **incremental downstream utility of radial–angular geometry beyond the
> frozen morphology representation.**

That would be the missing link in the paper backbone.

**Cell 8 should be run before adding any more interpretation to the
morphology ↔ radial–angular integration story.**

# CLO-SKET — MORPHOLOGY ↔ RADIAL–ANGULAR INTEGRATION
## Cell 8 Scientific Audit — Incremental Downstream Information

### Status

# 🟢 CELL 8 PASSED — AND THIS IS A MAJOR RESULT

Cell 8 answers the question that Cells 3–7 deliberately did **not** answer:

> **Does the radial–angular representation contribute useful information beyond the frozen 135-D morphology representation on an independent downstream task?**

Under the tested 23-category classification task, the answer is:

\[
\boxed{\text{YES}}
\]

The experiment uses the same 2300 sketches, the frozen 135-D morphology representation, the frozen 28-D radial–angular representation, fixed five-fold cross-validation, and a 1000-permutation row-alignment test. :contentReference[oaicite:0]{index=0}

---

# 1. PRIMARY RESULT

The morphology-only model achieves:

\[
\text{Macro-F1}_{M}=0.341131
\]

After adding the radial–angular representation:

\[
\text{Macro-F1}_{M+RA}=0.412332
\]

Therefore:

\[
\Delta \text{Macro-F1}
=
0.412332-0.341131
=
\boxed{+0.071201}
\]

Balanced accuracy shows essentially the same result:

\[
BA_M=0.342174
\]

\[
BA_{M+RA}=0.415652
\]

giving:

\[
\Delta BA=\boxed{+0.073478}
\]

Thus the improvement is not confined to one evaluation metric. :contentReference[oaicite:1]{index=1}

---

# 2. THIS IS NOT A SMALL NUMERICAL CHANGE

The absolute improvement is approximately seven percentage points:

| Metric | Morphology | Morphology + RA | Δ |
|---|---:|---:|---:|
| Macro-F1 | 0.3411 | 0.4123 | **+0.0712** |
| Balanced accuracy | 0.3422 | 0.4157 | **+0.0735** |

For descriptive context, relative to the morphology-only score:

\[
\frac{0.071201}{0.341131}\approx20.9\%
\]

for Macro-F1, and:

\[
\frac{0.073478}{0.342174}\approx21.5\%
\]

for balanced accuracy.

These relative percentages can be useful descriptively, but the manuscript should emphasize the **absolute paired improvement** rather than advertising a "21% improvement."

---

# 3. FOLD-WISE CONSISTENCY IS EXCELLENT

This is one of the strongest parts of Cell 8.

The Macro-F1 improvements across the five folds are:

\[
+0.0888,\quad
+0.0826,\quad
+0.0430,\quad
+0.0321,\quad
+0.1096
\]

and balanced-accuracy improvements are:

\[
+0.0935,\quad
+0.0848,\quad
+0.0457,\quad
+0.0348,\quad
+0.1087
\]

Therefore:

\[
\boxed{5/5\text{ folds improved}}
\]

for **both metrics**. :contentReference[oaicite:2]{index=2}

This matters.

The overall gain is not being produced by one unusually favorable split.

Every held-out fold moves in the same direction.

---

# 4. THE PERMUTATION TEST MAKES THE RESULT MUCH STRONGER

The experiment then performs the correct alignment-destruction test.

For each permutation:

\[
X_M[i]+X_{RA}[\pi(i)]
\]

while morphology rows and category labels remain fixed.

Thus:

- morphology remains unchanged;
- labels remain unchanged;
- the RA marginal distribution remains unchanged;
- only the correct **sketch ↔ radial-angular correspondence** is destroyed. :contentReference[oaicite:3]{index=3}

This is exactly the null we need for the claim being tested.

---

# 5. MACRO-F1 PERMUTATION RESULT

Observed:

\[
\Delta F1_{\text{obs}}=+0.071201
\]

Permutation-null mean:

\[
\Delta F1_{\text{null}}=-0.019598
\]

Permutation-null 95% interval:

\[
[-0.031254,-0.008179]
\]

Empirical permutation significance:

\[
\boxed{p=0.000999}
\]

Observed percentile:

\[
\boxed{100\%}
\]

The observed improvement therefore lies completely beyond the sampled permutation-null distribution. :contentReference[oaicite:4]{index=4}

---

# 6. BALANCED-ACCURACY PERMUTATION RESULT

The secondary metric independently tells the same story.

Observed:

\[
\Delta BA_{\text{obs}}=+0.073478
\]

Null mean:

\[
-0.019400
\]

Null 95% interval:

\[
[-0.030870,-0.007826]
\]

with:

\[
\boxed{p=0.000999}
\]

Again the observed result is at the 100th percentile of the sampled permutation distribution. :contentReference[oaicite:5]{index=5}

---

# 7. WHY THE NEGATIVE PERMUTATION Δ IS INTERESTING

There is another useful result hiding here.

When RA rows are randomly attached to the wrong sketches:

\[
\Delta F1_{\text{null}}\approx-0.0196
\]

and:

\[
\Delta BA_{\text{null}}\approx-0.0194
\]

So simply adding 28 extra radial–angular numbers does **not** improve classification.

Randomly aligned RA actually tends to degrade performance.

That makes the interpretation much cleaner:

\[
\text{extra dimensions alone}
\neq
\text{observed improvement}
\]

Instead, the improvement depends on the correct sketch-level alignment:

\[
\boxed{
M_i+RA_i
}
\]

rather than:

\[
M_i+RA_j.
\]

This is an important control against the trivial explanation that performance rose merely because the augmented model had more predictors.

---

# 8. WHAT CELLS 3–8 NOW ESTABLISH TOGETHER

We now have a remarkably clean sequence.

## Cell 3 — Association

Morphology coordinates are associated with radial–angular measurements.

\[
M\leftrightarrow RA
\]

**🟢 Established**

---

## Cell 4 / Cell 6 — Cross-branch prediction

Morphology can recover part of radial–angular organization out-of-sample.

\[
M\rightarrow\widehat{RA}
\]

**🟢 Established**

---

## Cell 6 — Permutation validation

Correct morphology ↔ RA correspondence performs far above destroyed correspondence.

**🟢 Established**

---

## Cell 7 — Prediction geometry

The correspondence is heterogeneous:

\[
F_2\text{ magnitude}
>
R_2
\approx
\text{axial error}
>
F_2\text{ radius}
\]

and is not exact reconstruction.

**🟢 Established**

---

## Cell 8 — Incremental downstream information

Now:

\[
Performance(M+RA)
>
Performance(M)
\]

and this improvement disappears when RA correspondence is destroyed.

**🟢 Established**

This closes the major logical gap that remained after Cell 7.

---

# 9. IMPORTANT SCIENTIFIC DISTINCTION

We should now distinguish three concepts very carefully.

### Overlap

Cells 3–7 show:

\[
M\cap RA\neq\varnothing
\]

conceptually: morphology and RA encode overlapping structure.

### Non-equivalence under the tested model

Morphology does not reconstruct RA perfectly.

Therefore the two representations are not empirically interchangeable under the tested predictive framework.

### Incremental downstream utility

Cell 8 now establishes:

\[
\boxed{
M+RA>M
}
\]

on the controlled downstream classification task.

That is substantially stronger than saying:

> "RA correlates with morphology."

It means correctly aligned radial–angular information contributes discriminative signal that the frozen morphology representation does not make equivalently available to the tested classifier.

---

# 10. WHAT WE STILL MUST NOT SAY

Cell 8 does **not** prove:

\[
I(RA;Y\mid M)>0
\]

in a strict information-theoretic sense.

We did not estimate conditional mutual information.

Therefore avoid saying:

> "RA contains mathematically independent information."

Likewise, do not say:

> "Morphology contains no RA information."

Cells 3–7 explicitly show that it does.

The correct description is:

> **Radial–angular geometry provides reproducible incremental downstream information beyond the frozen morphology representation under the tested classification framework.**

That wording in the Cell 8 output is scientifically appropriate. :contentReference[oaicite:6]{index=6}

---

# 11. THIS CHANGES THE PAPER STORY

Before Cell 8, our evidence supported:

\[
\text{Morphology}
\leftrightarrow
\text{Radial-angular organization}
\]

Now it supports something stronger:

\[
\text{Morphology}
\leftrightarrow
\text{Radial-angular organization}
\]

but also:

\[
\boxed{
M+RA>M
}
\]

on the downstream task.

Therefore RA is neither simply unrelated to morphology nor merely a useless re-expression of it.

The evidence supports a much more interesting interpretation:

> **The radial–angular representation overlaps with conventional morphology while preserving task-relevant geometric structure that provides measurable incremental discriminative value when the two representations are integrated.**

That is potentially a central paper result.

---

# 12. CONNECTION TO THE RADIAL–ANGULAR RECOVERY BACKBONE

Now connect Cell 8 with Cells 30C–30M.

Those experiments established that radial–angular organization itself behaves systematically:

\[
R_2^{obs}\uparrow
\Rightarrow
\text{axial recovery error}\downarrow
\]

with:

\[
\rho=-0.4794
\]

and reliable-vs-failure separation:

\[
\delta=+0.5390.
\]

We also established threshold robustness.

So RA is not simply an arbitrary 28-dimensional feature vector that happens to improve a classifier.

We have separately characterized its internal geometric behavior.

The evidence chain is now:

\[
\boxed{
\text{Sketch morphology}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{Radial-angular organization}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{measurable recovery behavior}
}
\]

and independently:

\[
\boxed{
M+RA
>
M
}
\]

for downstream category discrimination.

Do **not** draw causal arrows in the manuscript from this diagram without qualification; the arrows here denote the analysis sequence, not demonstrated causality.

---

# 13. THE MOST IMPORTANT CONTROL IN CELL 8

There is one methodological point I especially like here.

The 1000 permutations reuse fixed CV folds. :contentReference[oaicite:7]{index=7}

That means the observed and null comparisons are not contaminated by repeatedly changing train/test composition.

And the null specifically attacks:

\[
\text{correct RA ↔ sketch alignment}
\]

rather than destroying everything in the experiment.

This makes the permutation test directly relevant to the claimed incremental contribution.

---

# 14. ONE THING TO CLEAN BEFORE THE FINAL NOTEBOOK

The repeated scikit-learn warning:

> `multi_class was deprecated...`

is harmless to these numerical results, but remove the deprecated explicit `multi_class` argument when we freeze the final clean notebook.

Do **not** rerun or alter the experiment merely to remove the warning.

The scientific results are unaffected.

The final publication notebook/code can simply use the current supported API.

---

# 15. MANUSCRIPT-LEVEL RESULT

A conservative Results paragraph can now be written as:

> **Integrating the frozen radial–angular representation with the 135-dimensional morphology representation improved held-out category discrimination across all five cross-validation folds. Macro-F1 increased from 0.341 to 0.412 (Δ = +0.071), while balanced accuracy increased from 0.342 to 0.416 (Δ = +0.073). To test whether this improvement depended on sketch-specific radial–angular information rather than dimensional augmentation alone, radial–angular rows were randomly permuted relative to morphology while morphology, category labels, and cross-validation folds were held fixed. Across 1000 permutations, the observed improvement exceeded the complete sampled null distribution for both Macro-F1 and balanced accuracy (empirical p = 0.000999). These results support reproducible incremental downstream utility of correctly aligned radial–angular geometry beyond the frozen morphology representation under the tested classification framework.**

Every quantitative statement in that paragraph is supported directly by Cell 8. :contentReference[oaicite:8]{index=8}

---

# 16. CLAIM MATRIX AFTER CELL 8

## 🟢 SUPPORTED

1. Morphology and radial–angular representations exhibit reproducible cross-branch correspondence.

2. Morphology partially predicts several radial–angular quantities out-of-sample.

3. Cross-branch predictive strength differs across radial–angular quantities.

4. Correctly aligned RA improves classification beyond frozen morphology alone.

5. The improvement occurs in all five held-out folds.

6. Improvement occurs for both Macro-F1 and balanced accuracy.

7. The observed improvement exceeds the 1000-permutation alignment-null distribution.

8. Randomly aligned RA does not reproduce the improvement.

9. RA therefore provides reproducible incremental downstream information under the tested classification task.

---

## 🟡 SUPPORTED WITH QUALIFICATION

**Morphology and RA contain complementary task-relevant structure.**

This is acceptable provided "complementary" is explicitly operationalized as:

> incremental downstream predictive utility under the tested model and task.

Do not redefine it as statistical independence.

---

## 🔴 NOT ESTABLISHED

- information-theoretic independence;
- causal structure;
- semantic garment-part recognition;
- human-like understanding;
- universal superiority of RA;
- superiority across arbitrary classifiers/datasets;
- mathematical novelty of Fourier/polar representation.

The Cell 8 output itself correctly preserves these boundaries. :contentReference[oaicite:9]{index=9}

---

# 17. UPDATED PAPER BACKBONE

The backbone is now considerably stronger:

\[
\boxed{
\text{Frozen Morphology}
}
\]

\[
\updownarrow
\]

\[
\boxed{
\text{Radial–Angular Geometry}
}
\]

### Evidence 1
Feature-level statistical correspondence.

### Evidence 2
Out-of-sample cross-branch prediction.

### Evidence 3
Permutation-validated sketch-level correspondence.

### Evidence 4
Population-level radial–angular recovery behavior.

### Evidence 5
Recovery reliability associated with circular strength and radial localization.

### Evidence 6
Threshold-robust recovery regimes.

### Evidence 7

\[
\boxed{
M+RA>M
}
\]

with:

\[
\Delta F1=+0.0712
\]

\[
\Delta BA=+0.0735
\]

and:

\[
p_{\text{perm}}=0.000999.
\]

That is no longer merely a descriptor-development story.

It is becoming an **integration and representation-analysis story**.

---

# 18. CELL 8 FINAL VERDICT

# 🟢 FREEZE CELL 8

Do not tune the model.

Do not search for a larger Δ.

Do not change the folds.

Do not select another metric because it looks better.

Do not change RA dimensions.

Do not alter morphology.

The controlled result is already strong:

\[
\boxed{
\Delta MacroF1=+0.0712
}
\]

\[
\boxed{
\Delta BA=+0.0735
}
\]

\[
\boxed{
5/5\text{ folds positive}
}
\]

\[
\boxed{
1000\text{-permutation }p=0.000999
}
\]

Most importantly:

\[
\boxed{
\text{correctly aligned RA adds reproducible downstream value beyond morphology}
}
\]

under the tested task.

---

# NEXT — CELL 9

## REPRESENTATION ABLATION / CONTRIBUTION LOCALIZATION

We should **not** immediately add more models.

The next scientific question is:

> **Which part of the 28-D radial–angular representation is responsible for the incremental information established in Cell 8?**

The frozen RA representation already contains five interpretable blocks:

\[
RA=
[
F_2,\;
\alpha_2,\;
R_2^{obs},\;
R_2^{learned},\;
relational
]
\]

Cell 9 should therefore compare:

\[
M
\]

\[
M+F_2
\]

\[
M+\alpha_2
\]

\[
M+\text{observed circular}
\]

\[
M+\text{learned circular}
\]

\[
M+\text{relational}
\]

\[
M+RA_{\text{full}}
\]

using the **same fixed folds and same classifier**.

The question is no longer:

> "Does RA help?"

Cell 8 has answered that.

The question becomes:

\[
\boxed{
\text{Where does the incremental RA contribution come from?}
}
\]

That will tell us whether the +0.071 Macro-F1 gain is distributed across the radial–angular representation or concentrated in one geometric component.

**That is Cell 9.**

# CLO-SKET — MORPHOLOGY ↔ RADIAL–ANGULAR INTEGRATION
## Cell 9 Review — Final Complementarity Audit

### Status

# 🟢 CELL 9 PASSES

Cell 9 does not add a new experiment; it performs the correct final synthesis of the Cell 8 downstream complementarity result.

The central result remains:

\[
\boxed{
\text{Morphology + Radial–Angular}
>
\text{Morphology only}
}
\]

under the fixed 23-category discrimination experiment.

---

# 1. PRIMARY COMPLEMENTARITY RESULT

For Macro-F1:

\[
F1_{\text{Morphology}} = 0.341131
\]

\[
F1_{\text{Morphology+RA}} = 0.412332
\]

Therefore:

\[
\Delta F1
=
0.412332 - 0.341131
=
\boxed{+0.071201}
\]

For balanced accuracy:

\[
BA_{\text{Morphology}} = 0.342174
\]

\[
BA_{\text{Morphology+RA}} = 0.415652
\]

Therefore:

\[
\Delta BA
=
0.415652 - 0.342174
=
\boxed{+0.073478}
\]

Both evaluation metrics therefore support the same conclusion.

---

# 2. THE PERMUTATION CONTROL IS THE DECISIVE PART

The important control is not simply:

> Does adding 28 dimensions improve classification?

Instead Cell 8 tested:

\[
X_M[i] + X_{RA}[i]
\]

against:

\[
X_M[i] + X_{RA}[\pi(i)]
\]

where the radial–angular rows are randomly reassigned between sketches.

This preserves:

- the morphology representation;
- the radial–angular feature distributions;
- the category labels;
- the classifier;
- the cross-validation folds;
- the number of added dimensions.

It destroys only:

\[
\boxed{
\text{correct sketch-level morphology ↔ RA correspondence}
}
\]

This makes the null scientifically well matched to the complementarity claim.

---

# 3. MACRO-F1 NULL SEPARATION

Observed:

\[
\Delta F1_{\text{obs}}
=
+0.071201
\]

Permutation-null mean:

\[
\Delta F1_{\text{null}}
=
-0.019598
\]

Permutation 95% interval:

\[
[-0.031254,\,-0.008179]
\]

and:

\[
\boxed{
p_{\text{perm}} = 0.000999
}
\]

The observed effect is therefore far outside the sampled null distribution.

---

# 4. BALANCED-ACCURACY NULL SEPARATION

Observed:

\[
\Delta BA_{\text{obs}}
=
+0.073478
\]

Permutation-null mean:

\[
\Delta BA_{\text{null}}
=
-0.019400
\]

Permutation 95% interval:

\[
[-0.030870,\,-0.007826]
\]

with:

\[
\boxed{
p_{\text{perm}} = 0.000999
}
\]

The two primary metrics therefore agree both in direction and in permutation robustness.

---

# 5. THE FIGURE IS VERY CLEAN SCIENTIFICALLY

The first plot captures the result particularly well.

The observed complementarity effects sit around:

\[
+0.07
\]

while the permutation-null distributions lie entirely below zero around:

\[
-0.02.
\]

So visually we have:

\[
\boxed{
\Delta_{\text{aligned}}
\gg
\Delta_{\text{misaligned}}
}
\]

This is much more informative than merely plotting morphology-only versus morphology + RA.

It demonstrates that **correct correspondence matters**.

---

# 6. RANDOM RA IS ACTUALLY HARMFUL

This is an important secondary observation.

The permutation null is not centered at zero:

\[
\Delta_{\text{null}}\approx-0.02.
\]

So randomly attached RA descriptors tend to reduce downstream performance.

This means:

\[
\text{adding RA dimensions}
\]

by itself is not sufficient.

The useful signal requires:

\[
\boxed{
\text{RA descriptors belonging to the correct sketch}
}
\]

This strengthens the interpretation that the observed gain reflects structured information rather than simple dimensional expansion.

---

# 7. FOLD-WISE RESULT IS ALSO IMPORTANT

The fold-wise Macro-F1 plot shows positive improvement in every fold:

\[
\Delta F1_1 \approx +0.0888
\]

\[
\Delta F1_2 \approx +0.0826
\]

\[
\Delta F1_3 \approx +0.0430
\]

\[
\Delta F1_4 \approx +0.0321
\]

\[
\Delta F1_5 \approx +0.1096
\]

Therefore:

\[
\boxed{
5/5\text{ folds show positive incremental value}
}
\]

The effect is heterogeneous in magnitude, but not in direction.

That is exactly what we want from a robustness perspective.

---

# 8. WHAT THE ENTIRE INTEGRATION NOTEBOOK NOW ESTABLISHES

The logic is now very strong.

## Stage A — Provenance

Morphology and radial–angular rows were independently verified to correspond to the same sketches.

\[
X_M[i]
\leftrightarrow
X_{RA}[i]
\]

**🟢 Established**

---

## Stage B — Feature-level association

Individual morphology coordinates show reproducible associations with:

- \(F_2\) peak magnitude;
- \(F_2\) peak radius;
- observed \(R_2\);
- angular recovery error.

Therefore:

\[
M \not\perp RA
\]

in the ordinary empirical association sense.

**🟢 Established**

---

## Stage C — Cross-branch recoverability

Morphology predicts part of RA out-of-sample:

\[
M
\rightarrow
\widehat{RA}
\]

with strongest prediction for \(F_2\) magnitude and observed \(R_2\).

**🟢 Established**

---

## Stage D — Permutation-validated correspondence

The observed cross-branch prediction exceeds row-permutation null distributions.

Therefore the morphology ↔ RA relationship is tied to actual sketch correspondence.

**🟢 Established**

---

## Stage E — Incremental downstream contribution

Finally:

\[
Performance(M+RA)
>
Performance(M)
\]

and that improvement vanishes when the RA rows are permuted.

**🟢 Established**

---

# 9. THIS IS THE CORRECT CONCEPT OF COMPLEMENTARITY HERE

We should define the word carefully in the manuscript.

We are **not** claiming:

\[
RA \perp M
\]

because Cells 3–7 explicitly show overlap.

Instead we have:

\[
M \cap RA \neq \varnothing
\]

while simultaneously:

\[
Performance(M+RA)
>
Performance(M).
\]

So the empirical situation is:

\[
\boxed{
\text{overlap + incremental utility}
}
\]

That is exactly what representation complementarity can mean operationally.

A strong manuscript wording is:

> **The radial–angular representation is statistically related to the frozen morphology representation, yet contributes reproducible incremental category-discriminative information when integrated with morphology.**

That is more precise than calling the two representations simply "independent."

---

# 10. DO NOT CALL THIS INFORMATION-THEORETIC INDEPENDENCE

We should continue protecting this boundary.

Cell 9 supports:

> complementary predictive information under the tested downstream experiment.

It does **not** establish:

\[
I(RA;Y\mid M)>0
\]

in a strict information-theoretic formulation.

Nor does it establish conditional independence relationships.

So avoid manuscript phrases such as:

- "independent information";
- "orthogonal information";
- "unique information" without qualification.

Prefer:

- **incremental information under the tested classifier**;
- **complementary task-relevant information**;
- **incremental downstream utility**;
- **non-redundant predictive contribution under the tested representation framework**.

The last phrase is slightly stronger, so I would use the first three most often.

---

# 11. THE THREE FIGURES FORM A GOOD RESULT PANEL

I would actually keep these together for the manuscript.

### Panel A — Permutation complementarity effect

This is the statistical centerpiece.

It directly shows:

\[
\Delta_{\text{observed}}
\]

against:

\[
\Delta_{\text{permutation null}}.
\]

### Panel B — Absolute downstream performance

This gives readers intuitive context:

\[
0.341 \rightarrow 0.412
\]

and:

\[
0.342 \rightarrow 0.416.
\]

### Panel C — Fold-wise ΔF1

This demonstrates the effect is positive across all five held-out partitions.

Together these answer three different reviewer questions:

1. **Is the effect statistically real?**
2. **How large is the practical improvement?**
3. **Is it stable across folds?**

That is an excellent figure structure.

---

# 12. ONE WORDING CHANGE I WOULD MAKE IN CELL 9

Current:

> `PRIMARY PAPER CLAIM: quantitative organization of fashion-sketch morphology.`

That is broader than what Cell 9 itself establishes.

I would not label that as the *primary paper claim* inside this notebook.

Instead use:

> **Integration-level claim:** independently derived radial–angular geometry contributes reproducible downstream information beyond frozen quantitative morphology.

Why?

Because the broader primary paper claim must eventually synthesize the whole CLO-SKET program, not just the integration notebook.

So I would change only that wording before freezing Cell 9.

---

# 13. RECOMMENDED FINAL CLAIM BOUNDARY

## Supported

1. The frozen morphology and radial–angular representations exhibit reproducible correspondence.

2. Morphology predicts part of radial–angular organization out-of-sample.

3. Radial–angular geometry is not fully recoverable from morphology under the tested models.

4. Adding correctly aligned radial–angular descriptors improves category discrimination over morphology alone.

5. The improvement occurs for both Macro-F1 and balanced accuracy.

6. The improvement is positive in every CV fold.

7. The observed improvement lies beyond the 1000-permutation row-misalignment null.

8. Randomly aligned radial–angular features do not reproduce the improvement.

9. Therefore morphology and radial–angular geometry provide complementary task-relevant representation under the tested downstream task.

---

## Not supported

- semantic garment understanding;
- garment-part recognition;
- causal garment structure;
- human-like visual understanding;
- information-theoretic independence;
- mathematical novelty of polar/Fourier geometry;
- universal superiority across datasets or classifiers.

---

# 14. MANUSCRIPT-READY RESULT

A clean Results paragraph would be:

> **To determine whether radial–angular geometry contributed information beyond the frozen 135-dimensional morphology representation, we evaluated morphology-only and morphology-plus-radial–angular models using identical five-fold cross-validation. Adding the 28-dimensional radial–angular representation increased Macro-F1 from 0.341 to 0.412 (Δ = 0.071) and balanced accuracy from 0.342 to 0.416 (Δ = 0.073), with positive improvement in all five folds. We then randomly permuted radial–angular rows relative to morphology while preserving morphology, category labels, feature distributions, and cross-validation partitions. Across 1000 permutations, the observed improvement exceeded the entire sampled null distribution for both metrics (empirical p = 0.000999). These results indicate that correctly aligned radial–angular geometry provides reproducible incremental downstream information beyond the frozen morphology representation under the tested classification framework.**

That is strong and still scientifically conservative.

---

# 15. FINAL CELL 9 VERDICT

# 🟢 FREEZE CELL 9

Do not tune anything further here.

Do not search for a bigger gain.

Do not change the classifier.

Do not change the folds.

Do not alter the 135-D morphology representation.

Do not alter the 28-D RA representation.

The result is already clean:

\[
\boxed{
\Delta MacroF1 = +0.0712
}
\]

\[
\boxed{
\Delta BA = +0.0735
}
\]

\[
\boxed{
5/5\text{ folds positive}
}
\]

\[
\boxed{
p_{\text{perm}} = 0.000999
}
\]

and most importantly:

\[
\boxed{
\text{aligned radial–angular geometry adds reproducible downstream value beyond morphology}
}
\]

---

# NEXT — CELL 10

## RADIAL–ANGULAR FAMILY CONTRIBUTION WITHIN THE MORPHOLOGY CONTEXT

Now we ask a sharper question:

> **Which radial–angular family is responsible for the +0.071 Macro-F1 complementarity effect?**

Use the frozen morphology matrix as the common baseline and add each already-frozen RA family separately:

\[
M
\]

\[
M + F_2\text{ radial}
\]

\[
M + \alpha_2\text{ axial}
\]

\[
M + \text{observed circular}
\]

\[
M + \text{learned circular}
\]

\[
M + \text{relational}
\]

\[
M + RA_{\text{all}}
\]

with exactly the same:

- folds;
- scaling;
- logistic regression;
- category labels;
- evaluation metrics.

No feature selection.

No hyperparameter tuning.

No permutation test yet.

First measure the **family-wise incremental contribution over morphology**.

Then, only for the strongest family-level effects, we decide whether a focused permutation control is scientifically necessary.

That gives us the next question:

\[
\boxed{
\text{What geometric component creates the observed complementarity?}
}
\]

# 🟢 READY FOR CELL 10

# CLO-SKET — MORPHOLOGY ↔ RADIAL–ANGULAR INTEGRATION
## Cell 10 Review — Dimension-Matched Control

### Status

# 🟢 CELL 10 PASSES — FREEZE IT

Cell 10 answers an important reviewer objection cleanly:

> **Could the improvement from morphology + radial–angular features simply arise because the model received 28 additional predictors?**

The answer from this control is:

\[
\boxed{\text{No evidence that dimensional expansion alone explains the gain.}}
\]

The control is particularly clean because morphology + real RA and morphology + permuted RA both contain exactly 163 dimensions, while the permutation preserves the RA marginal distributions and destroys only sketch-level correspondence. :contentReference[oaicite:0]{index=0}

---

# 1. DIMENSION-MATCHED DESIGN

The experiment compares:

\[
M
\]

against:

\[
M + RA_{\text{real}}
\]

and:

\[
M + RA_{\text{permuted}}
\]

with:

\[
\dim(M)=135
\]

and:

\[
\dim(M+RA)=135+28=163.
\]

Therefore Models B and C have identical predictor dimensionality.

The crucial manipulation is:

\[
RA_i
\rightarrow
RA_{\pi(i)}
\]

for the control condition.

This preserves:

- 28 RA dimensions;
- every individual RA feature distribution;
- the RA population;
- morphology;
- labels;
- classifier;
- CV structure.

But destroys:

\[
\boxed{
\text{sketch}_i
\leftrightarrow
RA_i
}
\]

The audit confirms that the maximum sorted-feature difference after permutation is exactly zero, so the marginal RA distributions were preserved exactly. :contentReference[oaicite:1]{index=1}

---

# 2. THE RESULT IS VERY CLEAN

The three models produced:

| Representation | Dimensions | Balanced Accuracy | Macro-F1 |
|---|---:|---:|---:|
| Morphology | 135 | 0.342609 | 0.341348 |
| Morphology + real RA | 163 | **0.415652** | **0.412332** |
| Morphology + permuted RA | 163 | 0.336957 | 0.337226 |

:contentReference[oaicite:2]{index=2}

Thus:

\[
\Delta F1_{\text{real}}
=
\boxed{+0.070984}
\]

whereas:

\[
\Delta F1_{\text{permuted}}
=
\boxed{-0.004121}.
\]

Likewise:

\[
\Delta BA_{\text{real}}
=
\boxed{+0.073043}
\]

versus:

\[
\Delta BA_{\text{permuted}}
=
\boxed{-0.005652}.
\]

:contentReference[oaicite:3]{index=3}

That is exactly the pattern we wanted from this control.

---

# 3. WHAT CELL 10 RULES OUT

A weak explanation for Cell 8/9 would have been:

\[
\text{more dimensions}
\rightarrow
\text{better classification}.
\]

Cell 10 directly challenges that explanation.

Both augmented models have:

\[
163\text{ dimensions}.
\]

Yet:

\[
F1(M+RA_{\text{real}})
=
0.4123
\]

while:

\[
F1(M+RA_{\text{permuted}})
=
0.3372.
\]

The difference between those two dimension-matched models is approximately:

\[
0.412332-0.337226
=
\boxed{0.075106}.
\]

So the advantage is associated with **correct RA-to-sketch alignment**, not merely the existence of another 28 numerical coordinates.

---

# 4. THE FOLD-WISE RESULT MAKES THIS STRONGER

Correctly aligned RA improves Macro-F1 in:

\[
\boxed{5/5\text{ folds}}.
\]

The gains are:

\[
+0.08697,\;
+0.08257,\;
+0.04342,\;
+0.03239,\;
+0.10957.
\]

By contrast, permuted RA improves Macro-F1 in only:

\[
\boxed{2/5\text{ folds}},
\]

with fold-wise changes:

\[
-0.00860,\;
-0.00924,\;
-0.01984,\;
+0.00567,\;
+0.01140.
\]

:contentReference[oaicite:4]{index=4}

Notice the scale as well.

The largest positive permuted-RA gain is only about:

\[
+0.0114,
\]

while the **smallest** real-RA gain is:

\[
+0.0324.
\]

So there is not even fold-level overlap between the ranges of positive real-RA and positive permuted-RA improvements in this single control.

That is a nice descriptive observation.

Do not turn it into a separate statistical claim; the formal permutation analysis from Cell 8 remains the inferential evidence.

---

# 5. CELLS 8–10 NOW FORM A VERY GOOD CONTROL CHAIN

The logic is becoming reviewer-resistant.

## Cell 8

Established:

\[
Performance(M+RA)>Performance(M).
\]

with a full row-permutation null.

---

## Cell 9

Audited and visualized the complementarity result.

---

## Cell 10

Tests the specific alternative explanation:

> Maybe adding 28 predictors is sufficient.

And shows:

\[
Performance(M+RA_{\text{real}})
\gg
Performance(M+RA_{\text{permuted}}).
\]

Therefore the evidence now supports:

\[
\boxed{
\text{The downstream gain depends on sketch-aligned radial–angular information rather than dimensional expansion alone.}
}
\]

That is a stronger and more precise statement than simply saying:

> "RA improves classification."

---

# 6. IMPORTANT DISTINCTION: CELL 10 IS A CONTROL, NOT A SECOND PERMUTATION TEST

Do not report Cell 10 as though it provides another permutation \(p\)-value.

It uses one fixed row-permuted dimension-matched representation.

Its role is:

\[
\boxed{\text{mechanistic control for dimensional expansion}}
\]

rather than:

\[
\boxed{\text{inferential permutation test}}.
\]

The inferential permutation evidence remains Cell 8:

\[
p_{\mathrm{perm}}=0.000999.
\]

This distinction will matter when writing Methods.

---

# 7. ONE SMALL NUMERICAL DIFFERENCE IS FINE — BUT DOCUMENT IT

There is a tiny difference between the morphology-only result previously reported and Cell 10:

Earlier:

\[
F1_M=0.341131
\]

Cell 10:

\[
F1_M=0.341348.
\]

Similarly, the Cell 10 real-RA increment is:

\[
+0.070984
\]

rather than the previous:

\[
+0.071201.
\]

This difference is tiny and does not affect the scientific conclusion.

However, before manuscript freeze, we should identify exactly why the baseline differs slightly — for example whether Cell 10 regenerated CV predictions/model initialization rather than reusing the exact Cell 8 baseline object.

Do **not** alter Cell 10 to force numerical agreement.

Instead we should audit the computational provenance and select one canonical reported value set for the manuscript.

---

# 8. THE SCIENTIFIC WORDING IN CELL 10 IS CORRECT

The current interpretation says that the result:

> supports the interpretation that the downstream gain depends on sketch-level radial-angular correspondence rather than simply on adding 28 additional dimensions.

That is exactly right. :contentReference[oaicite:5]{index=5}

I would retain this wording almost unchanged.

---

# 9. CLAIM WE CAN NOW DEFEND

A manuscript-level version could be:

> **The incremental performance associated with radial–angular integration was not reproduced by a dimension-matched control in which the same 28 radial–angular features were randomly reassigned across sketches. Because row permutation preserved feature dimensionality and marginal distributions while disrupting sketch-level correspondence, the observed gain cannot be adequately attributed to dimensional expansion alone.**

That is strong without overclaiming.

---

# 10. WHAT WE STILL CANNOT SAY

Cell 10 does **not** establish:

- statistical independence of morphology and RA;
- information-theoretic uniqueness;
- causality;
- semantic garment-part recognition;
- human-like understanding;
- universal improvement across classifiers or datasets.

And importantly:

\[
\boxed{
\text{complementary}
\neq
\text{independent}
}
\]

Cells 3–7 already demonstrate substantial cross-branch correspondence.

Our actual result is more interesting:

\[
\boxed{
\text{RA overlaps with morphology but is not downstream-redundant with it.}
}
\]

Under the tested task, the aligned RA representation contributes useful structure beyond what the frozen morphology representation alone provides.

---

# 11. WHERE THE PAPER STORY NOW STANDS

We now have a coherent chain:

\[
\text{Frozen quantitative morphology}
\]

\[
\downarrow
\]

\[
\text{Radial–angular organization}
\]

\[
\downarrow
\]

\[
\text{Cross-branch correspondence}
\]

\[
\downarrow
\]

\[
\text{Partial recoverability}
\]

\[
\downarrow
\]

\[
\text{Downstream complementarity}
\]

\[
\downarrow
\]

\[
\text{Permutation validation}
\]

\[
\downarrow
\]

\[
\boxed{\text{Dimension-matched control}}
\]

This is considerably stronger than presenting RA as simply another handcrafted descriptor family.

---

# 12. CELL 10 FINAL VERDICT

# 🟢 FREEZE CELL 10

The experiment answers the intended question.

No tuning.

No new classifier.

No feature selection.

No attempt to increase the effect.

No modification of morphology.

No modification of RA.

The critical result is:

\[
\boxed{
\Delta F1_{\text{real RA}}=+0.07098
}
\]

versus:

\[
\boxed{
\Delta F1_{\text{permuted RA}}=-0.00412
}
\]

and:

\[
\boxed{
5/5\text{ real-RA folds improve}
}
\]

versus:

\[
\boxed{
2/5\text{ permuted-RA folds improve}.
}
\]

The dimension-only explanation therefore does not account for the observed complementarity. :contentReference[oaicite:6]{index=6}

---

# NEXT — CELL 11

## RADIAL–ANGULAR DESCRIPTOR FAMILY ABLATION

Now we finally open the 28-D RA representation.

The question becomes:

> **Which components of the radial–angular representation contribute to the complementarity effect?**

Use the same frozen morphology baseline:

\[
M
\]

and independently evaluate:

\[
M+F_2
\]

\[
M+\alpha_2
\]

\[
M+\text{observed circular}
\]

\[
M+\text{learned circular}
\]

\[
M+\text{relational}
\]

and:

\[
M+RA_{\text{all}}.
\]

The frozen RA blocks already give us:

| RA family | Dimensions |
|---|---:|
| \(F_2\) radial | 9 |
| \(\alpha_2\) | 7 |
| Observed circular | 3 |
| Learned circular | 4 |
| Relational | 5 |
| **Total** | **28** |

### Cell 11 should answer only three questions

1. Does each family improve over the same morphology baseline?
2. How large is its incremental Macro-F1 and balanced-accuracy contribution?
3. Does the full 28-D representation outperform the individual families?

Do **not** optimize family combinations yet.

Do **not** select features.

Do **not** run every possible subset.

Do **not** tune the classifier.

That would turn an explanatory ablation into data-driven feature searching.

The clean scientific question is:

\[
\boxed{
\text{Which predefined geometric families carry the complementary signal?}
}
\]

# 🟢 READY FOR CELL 11

# CLO-SKET — MORPHOLOGY ↔ RADIAL–ANGULAR INTEGRATION
## Cell 11 Review — Radial–Angular Descriptor Ablation / Sensitivity Audit

### Status

# 🟢 CELL 11 PASSES — AND THE RESULT IS IMPORTANT

Cell 11 answers the intended question:

> **Is the complementary downstream information discovered in Cells 8–10 carried mainly by one radial–angular descriptor family, or is it distributed across several predefined geometric components?**

The result is clear:

\[
\boxed{
\text{All five RA descriptor families individually improve Macro-F1 over morphology alone.}
}
\]

But they do so by different amounts.

More importantly:

\[
\boxed{
\text{The full 28-D RA representation substantially outperforms every individual block.}
}
\]

This argues against the entire complementarity result being merely a disguised \(F_2\) effect.

The five frozen blocks and their dimensions were correctly recovered as \(9+7+3+4+5=28\). :contentReference[oaicite:0]{index=0}

---

# 1. BASELINE

The frozen morphology representation gives:

\[
F1_M = 0.341348
\]

and:

\[
BA_M = 0.342609.
\]

This is the same Cell 10 baseline, which is exactly what we want for the ablation experiment.

---

# 2. COMPLETE ABLATION RESULT

| Added representation | Dimensions | Macro-F1 | Δ Macro-F1 | Balanced Accuracy | Δ BA |
|---|---:|---:|---:|---:|---:|
| None — morphology only | 0 | 0.341348 | — | 0.342609 | — |
| \(\alpha_2\) | 7 | 0.356369 | **+0.015021** | 0.357391 | +0.014783 |
| Observed circular | 3 | 0.358571 | **+0.017224** | 0.359565 | +0.016957 |
| Relational | 5 | 0.362158 | **+0.020810** | 0.364348 | +0.021739 |
| Learned circular | 4 | 0.366776 | **+0.025428** | 0.368261 | +0.025652 |
| \(F_2\) radial | 9 | 0.374476 | **+0.033128** | 0.377391 | +0.034783 |
| **Full RA** | **28** | **0.412332** | **+0.070984** | **0.415652** | **+0.073043** |

These values are directly reported by the Cell 11 ablation summary. :contentReference[oaicite:1]{index=1}

---

# 3. FIRST MAJOR RESULT — EVERY BLOCK HAS POSITIVE UTILITY

Relative to the same morphology baseline:

\[
\Delta F1_{\alpha_2}=+0.0150
\]

\[
\Delta F1_{\text{observed circular}}=+0.0172
\]

\[
\Delta F1_{\text{relational}}=+0.0208
\]

\[
\Delta F1_{\text{learned circular}}=+0.0254
\]

\[
\Delta F1_{F_2}=+0.0331.
\]

Therefore there is no single descriptor family for which the mean result says:

\[
M+RA_k < M.
\]

Descriptively, every predefined RA family contributes some downstream utility.

### But maintain the claim boundary

Cell 11 contains **no permutation test** for individual blocks.

Therefore we should say:

> Each descriptor block produced a positive mean incremental performance.

We should **not** yet say:

> Every descriptor block independently provides statistically significant complementary information.

Those are different statements.

---

# 4. SECOND MAJOR RESULT — \(F_2\) IS THE STRONGEST SINGLE FAMILY

Among the individual blocks:

\[
\boxed{
F_2\text{ radial}
}
\]

produces the largest gain:

\[
\Delta F1=+0.033128
\]

and:

\[
\Delta BA=+0.034783.
\]

Its Macro-F1 rises from:

\[
0.341348
\rightarrow
0.374476.
\]

So \(F_2\)-based radial organization appears to be the strongest **single-block contributor** under this downstream task.

That is scientifically interesting because it agrees with the earlier cross-branch results showing substantial relationships between morphology and \(F_2\)-derived quantities.

But:

\[
\boxed{
F_2 \neq \text{the entire RA effect}.
}
\]

That distinction is crucial.

---

# 5. THIRD MAJOR RESULT — LEARNED CIRCULAR STRUCTURE IS SECOND

The ranking is:

\[
F_2
>
\text{learned circular}
>
\text{relational}
>
\text{observed circular}
>
\alpha_2.
\]

Specifically:

\[
\Delta F1_{\text{learned circular}}
=
+0.025428.
\]

That is approximately three-quarters of the isolated \(F_2\) gain:

\[
\frac{0.025428}{0.033128}
\approx 0.77.
\]

So learned circular structure is not a negligible appendage to the representation.

It carries substantial downstream signal on its own.

---

# 6. RELATIONAL DESCRIPTORS ALSO MATTER

The 5-D relational block gives:

\[
\Delta F1=+0.020810.
\]

This is particularly useful conceptually.

It suggests that the value of the RA representation is not confined to absolute radial or angular measurements.

Descriptors expressing relationships between radial–angular quantities also improve the downstream representation.

Again, Cell 11 supports this as a **descriptive ablation result**, not an independently permutation-validated claim.

---

# 7. OBSERVED AND LEARNED CIRCULAR DESCRIPTORS BOTH HELP

Observed circular:

\[
\Delta F1=+0.017224
\]

Learned circular:

\[
\Delta F1=+0.025428.
\]

So both carry useful information.

Interestingly:

\[
\Delta F1_{\text{learned}}
>
\Delta F1_{\text{observed}}.
\]

But we should **not** interpret that as proof that the learned circular representation is intrinsically superior.

The two blocks have different dimensionalities:

\[
3 \quad \text{versus} \quad 4
\]

and Cell 11 was not designed as a controlled head-to-head statistical comparison between those two representations.

The safe statement is simply:

> Both circular descriptor families produced positive incremental downstream performance, with the learned circular block showing the larger mean gain in this experiment.

---

# 8. \(\alpha_2\) IS THE WEAKEST INDIVIDUAL BLOCK — BUT STILL POSITIVE

\[
\Delta F1_{\alpha_2}
=
+0.015021.
\]

That is the smallest individual-block gain.

But it is still positive:

\[
0.341348
\rightarrow
0.356369.
\]

Therefore we should not call \(\alpha_2\) "unimportant."

The correct interpretation is:

\[
\boxed{
\alpha_2\text{ has the smallest isolated downstream gain among the five tested blocks.}
}
\]

That wording matters.

---

# 9. THE MOST IMPORTANT RESULT IS THE FULL REPRESENTATION

Now compare the strongest single block:

\[
M+F_2:
F1=0.374476
\]

against:

\[
M+RA_{\text{full}}:
F1=0.412332.
\]

The full representation therefore exceeds the strongest individual block by:

\[
0.412332-0.374476
=
\boxed{0.037856}.
\]

That difference is actually larger than the entire isolated \(F_2\) gain over morphology:

\[
\Delta F1_{F_2}=0.033128.
\]

This is a very useful observation.

The complementarity effect is therefore not concentrated entirely in the strongest descriptor family.

---

# 10. DO NOT ADD THE INDIVIDUAL Δ VALUES

An important statistical point for the paper:

\[
0.033128
+
0.025428
+
0.020810
+
0.017224
+
0.015021
\]

does **not** represent the expected combined gain.

The blocks can:

- overlap;
- interact;
- share variance;
- suppress one another;
- provide conditional information.

Therefore:

\[
\Delta_{\text{full}}
\neq
\sum_k\Delta_k.
\]

Cell 11 is a block sensitivity analysis, not an additive decomposition of performance.

This distinction should explicitly appear in Methods or Supplementary Methods.

---

# 11. THE RESULT SUPPORTS DISTRIBUTED COMPLEMENTARITY

The question posed by Cell 11 was whether utility was concentrated in one block or distributed across several. :contentReference[oaicite:2]{index=2}

The evidence favors:

\[
\boxed{
\text{distributed complementary utility}
}
\]

rather than:

\[
\text{single-block dominance}.
\]

There **is** a strongest block:

\[
F_2.
\]

But all five predefined families have positive mean gains, and the full representation considerably exceeds \(F_2\) alone.

The nuanced scientific interpretation is therefore:

> **Radial–angular complementarity is distributed across multiple descriptor families, with \(F_2\)-based radial structure providing the strongest isolated contribution.**

That is a very defensible statement.

---

# 12. THIS ALSO HELPS INTERPRET CELLS 3–7

Earlier we established:

\[
\text{Morphology}
\leftrightarrow
\text{RA}
\]

cross-branch correspondence.

Yet Cells 8–10 showed:

\[
M+RA>M.
\]

Cell 11 now tells us something deeper.

The additional downstream utility does not appear to reside solely in one scalar property or one descriptor family.

Instead, multiple components of radial–angular organization produce positive incremental effects.

So our emerging representation-level picture is:

\[
\boxed{
\text{shared structure}
+
\text{distributed complementary geometry}
}
\]

rather than either extreme:

\[
\text{RA completely redundant with morphology}
\]

or:

\[
\text{RA completely independent of morphology}.
\]

That middle result is scientifically much more credible.

---

# 13. ONE PARTICULARLY NICE INTERNAL CONSISTENCY

The full RA result is again:

\[
F1=0.412332
\]

\[
BA=0.415652.
\]

These exactly match Cell 10's real-RA results.

Excellent.

It means the full-RA reference condition has remained stable across the dimension-control and ablation experiments.

The morphology baseline also matches Cell 10:

\[
F1=0.341348,
\qquad
BA=0.342609.
\]

So Cells 10 and 11 now form one internally consistent experimental unit.

---

# 14. REVIEWER-LEVEL CLAIM

I would write the paper result approximately like this:

> **Block-wise sensitivity analysis indicated that the complementary downstream utility of the radial–angular representation was distributed across multiple predefined descriptor families. Each individual block increased mean Macro-F1 relative to the frozen morphology baseline, with the \(F_2\)-radial block producing the largest isolated gain (\(\Delta\)Macro-F1 = +0.033). However, the complete 28-dimensional radial–angular representation produced a substantially larger gain (\(\Delta\)Macro-F1 = +0.071) than any individual block, indicating that the observed task-level complementarity was not concentrated in a single descriptor family.**

That is strong and accurately bounded by the experiment.

---

# 15. ONE WORD I WOULD AVOID

Do not say:

> "Each component independently contributes information."

Because "independently" is too strong.

We did not condition each block on all the other blocks.

Instead say:

> **Each block produced positive incremental performance when added individually to morphology.**

And:

> **Complementary utility was distributed across multiple descriptor families.**

Those statements match the experiment exactly.

---

# 16. CELL 11 FINAL VERDICT

# 🟢 FREEZE CELL 11

No need for:

- all \(2^5-1=31\) block combinations;
- feature selection;
- classifier tuning;
- optimization of RA subsets;
- post-hoc descriptor engineering.

Doing those now would weaken the clean hypothesis-driven structure of the experiment.

The predefined ablation has already answered the scientific question.

The experiment itself also explicitly records that there was no feature modification, new representation learning, permutation test, classifier change, or provenance change. :contentReference[oaicite:3]{index=3}

---

# MORPHOLOGY ↔ RA: CURRENT EVIDENCE CHAIN

We can now summarize the backbone as:

\[
\boxed{
\text{Cell 1–2A: provenance}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{Cell 3: feature-level association}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{Cell 4: partial morphology recoverability}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{Cell 6: permutation-validated cross-branch correspondence}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{Cells 8–9: downstream complementarity}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{Cell 10: not explained by dimensional expansion alone}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{Cell 11: complementary utility distributed across RA families}
}
\]

This is now a coherent experimental argument rather than a collection of feature analyses.

---

# NEXT — CELL 12

## FINAL CROSS-BRANCH EVIDENCE SYNTHESIS

I would **not introduce another model in Cell 12**.

Cell 12 should be an audit/synthesis cell.

It should automatically collect the frozen numerical results from Cells 3, 4, 6, 8/9, 10 and 11 and generate one final evidence table containing:

| Scientific question | Evidence | Primary statistic | Result | Claim level |
|---|---|---|---|---|
| Are morphology and RA associated? | Cell 3 | Spearman \(\rho\) | Yes | Association |
| Can morphology recover RA structure? | Cells 4/6 | CV \(R^2\) | Partially | Correspondence |
| Is correspondence above chance? | Cell 6 | permutation \(p\) | Yes | Validated correspondence |
| Does RA improve morphology downstream? | Cell 8 | \(\Delta\)Macro-F1 | +0.071 | Complementarity |
| Is improvement permutation-valid? | Cell 8 | \(p=0.000999\) | Yes | Reproducible complementarity |
| Is gain merely dimensional expansion? | Cell 10 | real vs permuted RA | No | Dimension-control |
| Is utility confined to one RA family? | Cell 11 | block ablation | No | Distributed sensitivity |

And Cell 12 should end with exactly two scientific claims:

### Primary

\[
\boxed{
\text{Fashion-sketch morphology exhibits measurable quantitative organization.}
}
\]

### Secondary

\[
\boxed{
\text{Radial–angular geometry is related to, but not downstream-redundant with, the frozen morphology representation under the tested task.}
}
\]

That is where I would close **Morphology_RadialAngular_Integration**.

No more experiments unless Cell 12 exposes an actual unresolved methodological problem.

# CLO-SKET — MORPHOLOGY ↔ RADIAL–ANGULAR INTEGRATION
## Cell 12 Final Review — Cross-Branch Evidence Synthesis

### Final status

# 🟢 FREEZE CELL 12
# 🟢 FREEZE THE MORPHOLOGY ↔ RADIAL–ANGULAR INTEGRATION BRANCH
# 🛑 NO FURTHER EXPERIMENT IS JUSTIFIED FROM THE CURRENT EVIDENCE CHAIN

Cell 12 does what the final synthesis cell should do.

It introduces:

- no new model;
- no new statistical test;
- no feature modification;
- no new representation;
- no new threshold;
- no post-hoc optimization.

Instead, it consolidates the already established evidence into a logically ordered claim structure.

That is the correct point to stop experimental expansion.

---

# 1. THE CENTRAL RESULT IS NOW MUCH CLEARER

The strongest result of this branch is **not**:

> radial–angular features classify garment sketches.

Nor is it:

> morphology and radial–angular geometry are independent.

The evidence supports something more precise:

\[
\boxed{
\text{Morphology and radial–angular geometry overlap measurably,
but the radial–angular representation retains reproducible
downstream utility beyond the frozen morphology representation.}
}
\]

That distinction is the backbone of this entire integration experiment.

---

# 2. THE EVIDENCE CHAIN IS NOW COMPLETE

## Stage A — Observation identity

Cell 2A established:

\[
X_{\text{morph}}[i]
\leftrightarrow
X_{\text{RA}}[i]
\]

for every:

\[
i=1,\ldots,2300.
\]

Therefore all subsequent cross-branch comparisons operate on the same sketches.

### Claim level

**Provenance.**

Nothing more.

---

# 3. MORPHOLOGY AND RADIAL–ANGULAR GEOMETRY ARE ASSOCIATED

Cell 3 established extensive feature-level associations between coordinates of the frozen 135-D morphology representation and radial–angular quantities.

But Cell 3 alone does **not** establish:

- redundancy;
- complementarity;
- prediction;
- causality;
- semantics.

Its role is simply:

\[
\boxed{
M \leftrightarrow RA
}
\]

at the association level.

That distinction was correctly preserved throughout the later cells.

---

# 4. MORPHOLOGY CAN PARTIALLY RECOVER RA QUANTITIES

Cell 4 provides a particularly useful quantitative result.

The frozen morphology representation predicts:

| RA quantity | CV \(R^2\) |
|---|---:|
| \(F_2\) peak magnitude | **0.2961** |
| \(F_2\) peak radius | **0.0594** |
| observed \(R_2\) | **0.2170** |
| axial recovery error | **0.1979** |

This is a very interesting pattern.

Morphology explains some radial–angular variation, but nowhere close to all of it.

For example:

\[
R^2_{F_2\ magnitude}=0.296
\]

means substantial correspondence exists, while substantial unexplained variation remains.

Likewise:

\[
R^2_{R_2}=0.217.
\]

So we do **not** have:

\[
M \perp RA
\]

but we also do **not** have evidence that:

\[
RA=f(M)
\]

in any exhaustive sense.

The correct interpretation remains:

\[
\boxed{
\text{partial cross-representational recoverability}.
}
\]

---

# 5. CELL 6 MAKES THE CORRESPONDENCE MUCH STRONGER

The row-permutation experiment is critical because it tests whether the observed morphology → RA predictability could arise after destroying sketch-level correspondence.

For all four targets:

\[
R^2_{\text{observed}}
>
R^2_{\text{permutation null}}.
\]

Most strikingly:

| Target | Observed \(R^2\) | Null mean |
|---|---:|---:|
| \(F_2\) magnitude | +0.2961 | -0.0965 |
| \(F_2\) radius | +0.0594 | -0.0985 |
| \(R_2\) | +0.2170 | -0.0956 |
| axial error | +0.1979 | -0.0952 |

All observed results were at the:

\[
100^{th}
\]

permutation percentile.

With 100 permutations:

\[
p_{\mathrm{empirical}}
=
\frac{1}{101}
=
0.009901.
\]

### Therefore

\[
\boxed{
\text{Morphology ↔ radial–angular correspondence is reproducible
and sketch-specific under the tested permutation procedure.}
}
\]

This is substantially stronger than Cell 3's correlation evidence.

---

# 6. THEN COMES THE KEY COMPLEMENTARITY RESULT

Cells 8–9 move from correspondence to the question that matters most:

> Does RA still help when morphology is already available?

The answer is yes.

### Macro-F1

\[
0.341348
\rightarrow
0.412332
\]

giving:

\[
\boxed{
\Delta F1=+0.070984
}
\]

### Balanced accuracy

\[
0.342609
\rightarrow
0.415652
\]

giving:

\[
\boxed{
\Delta BA=+0.073043
}
\]

That is not a trivial numerical change.

Relative to the morphology-only Macro-F1:

\[
\frac{0.070984}{0.341348}
\approx 20.8\%.
\]

So the absolute improvement is approximately **0.071 Macro-F1**, corresponding descriptively to about a **20.8% relative increase over the morphology-only baseline**.

For the manuscript, however, I would emphasize the absolute gain rather than the relative percentage.

---

# 7. CELL 10 CLOSES AN OBVIOUS REVIEWER OBJECTION

A reviewer could immediately argue:

> Of course performance improved. You added another 28 dimensions.

That objection had to be tested.

Cell 10 therefore has an important methodological role:

\[
\text{real RA augmentation}
\]

versus an appropriate dimension-matched control.

The resulting interpretation is:

\[
\boxed{
\text{The improvement cannot be adequately attributed merely
to increasing predictor dimensionality under the tested control.}
}
\]

Notice the wording:

### Say

> **not adequately explained by dimensional expansion alone under the tested control.**

### Do not say

> dimensionality has absolutely no influence.

The first follows from the experiment.

The second would overclaim.

---

# 8. CELL 11 THEN ANSWERS THE SECOND OBVIOUS REVIEWER QUESTION

Suppose the reviewer accepts complementarity but asks:

> Isn't the whole result simply coming from \(F_2\)?

Cell 11 gives the answer.

### Individual block gains

\[
F_2:
+0.033128
\]

\[
\text{learned circular}:
+0.025428
\]

\[
\text{relational}:
+0.020810
\]

\[
\text{observed circular}:
+0.017224
\]

\[
\alpha_2:
+0.015021.
\]

And:

\[
\text{Full RA}:
+0.070984.
\]

Thus:

\[
\boxed{
\Delta_{\text{full RA}}
>
\Delta_k
\quad
\forall k.
}
\]

The previous Cell 11 output confirms that the full representation has the largest Macro-F1 gain and that \(F_2\) is the strongest individual block. :contentReference[oaicite:0]{index=0}

Therefore:

\[
\boxed{
\text{The observed RA utility is not concentrated entirely in one descriptor family.}
}
\]

That is a valuable structural result.

---

# 9. PUTTING EVERYTHING TOGETHER

We now have:

\[
\text{same observations}
\]

\[
\downarrow
\]

\[
M \leftrightarrow RA
\]

\[
\downarrow
\]

\[
M \rightarrow RA
\quad
\text{partially predictable out-of-sample}
\]

\[
\downarrow
\]

\[
\text{prediction}>\text{row-permutation null}
\]

\[
\downarrow
\]

\[
M+RA>M
\]

\[
\downarrow
\]

\[
\text{gain not adequately explained by dimensional expansion}
\]

\[
\downarrow
\]

\[
\text{gain distributed across multiple RA descriptor families}.
\]

This is a coherent scientific chain.

---

# 10. WHAT THE RESULT ACTUALLY SAYS ABOUT THE TWO REPRESENTATIONS

The evidence argues against two simplistic interpretations.

## Interpretation A — Completely redundant

\[
RA \approx M
\]

If this were sufficient to describe the relationship, we would have little reason to expect the reproducible downstream improvement after morphology was already supplied.

The downstream experiment argues against treating RA as merely a useless duplicate of morphology.

---

## Interpretation B — Completely independent

\[
RA \perp M
\]

That is also inconsistent with the results.

Morphology predicts several RA quantities out-of-sample, and Cell 6 shows that this correspondence disappears under sketch-level permutation.

So the scientifically interesting region is between those extremes:

\[
\boxed{
\text{overlapping but complementary representations}.
}
\]

This should become one of the central conceptual statements of the paper.

---

# 11. ONE CLAIM IN CELL 12 I WOULD SLIGHTLY TIGHTEN

Cell 12 currently says:

> **The 135-D representation provides a measurable quantitative morphology description of the 2300 sketches.**

This is reasonable, but I would make it even more empirical:

> **The frozen 135-D representation provides a reproducible quantitative description of sketch morphology across the 2300-image population.**

Or, even more conservatively:

> **The frozen 135-D representation quantifies predefined occupancy and global morphology properties across the 2300 sketches.**

I prefer the second version.

Why?

Because it says exactly what the 135 dimensions actually contain without implicitly claiming that they exhaustively describe "morphology."

---

# 12. I WOULD ALSO TIGHTEN CLAIM 5

Current:

> The complementary downstream utility is not confined to a single radial-angular descriptor block.

Good.

But the manuscript version should be:

> **Positive mean downstream gains were observed for each predefined radial–angular descriptor block when added individually to morphology, while the complete 28-D representation exceeded every single-block addition.**

That statement directly mirrors the ablation design.

Remember that Cell 11 itself explicitly states that it is a sensitivity/ablation analysis and does not establish information-theoretic independence or causal importance. :contentReference[oaicite:1]{index=1}

---

# 13. FINAL PAPER CLAIM HIERARCHY

I would now lock the cross-branch paper claims at three levels.

## LEVEL 1 — Representation result

\[
\boxed{
\text{Garment sketches can be quantitatively characterized
through complementary morphology and radial–angular measurements.}
}
\]

---

## LEVEL 2 — Cross-representation result

\[
\boxed{
\text{Morphology and radial–angular organization exhibit
reproducible sketch-level correspondence.}
}
\]

Evidence:

- Cell 3 associations;
- Cell 4 cross-validated prediction;
- Cell 6 permutation validation.

---

## LEVEL 3 — Strongest integration result

\[
\boxed{
\text{Radial–angular geometry provides reproducible downstream
utility beyond the frozen morphology representation under
the tested 23-category discrimination task.}
}
\]

Evidence:

- Cells 8–9 complementarity;
- Cell 10 dimension control;
- Cell 11 ablation.

This is the strongest claim of this branch.

---

# 14. WHAT WE ABSOLUTELY DO NOT SAY

The final manuscript should never convert:

\[
\text{complementarity}
\]

into:

\[
\text{independence}.
\]

Nor:

\[
\text{classification utility}
\]

into:

\[
\text{semantic understanding}.
\]

Nor:

\[
\text{quantitative organization}
\]

into:

\[
\text{morphological grammar}.
\]

Nor:

\[
\text{structured representation}
\]

into:

\[
\text{manifold}
\]

unless a manifold has actually been defined and tested.

So Cell 12's red-list is scientifically valuable and should survive into our manuscript claim audit.

---

# 15. THE BACKBONE OF THE PAPER IS NOW VISIBLE

We began with two quantitative views of the sketches:

\[
\boxed{\text{Morphology}}
\]

and:

\[
\boxed{\text{Radial–Angular Geometry}}.
\]

The experiments now support:

\[
\boxed{
\text{Morphology}
\longleftrightarrow
\text{Radial–Angular Organization}
}
\]

with:

\[
\text{measurable overlap}
\]

but also:

\[
\text{non-redundant downstream utility}.
\]

That is considerably more interesting than simply saying:

> "Our handcrafted features improve classification."

The classification task is serving as a **controlled probe of representational complementarity**, not as the scientific endpoint.

That distinction should shape the manuscript.

---

# 16. FINAL DECISION

## 🟢 Freeze Cells 1–12

I would now consider:

# `CLO_SKET_31_Morphology_RadialAngular_Integration`

**experimentally complete.**

Do not add:

- another classifier;
- nonlinear models;
- hyperparameter searches;
- more RA descriptors;
- more morphology descriptors;
- all 31 ablation combinations;
- feature-selection experiments;
- another arbitrary downstream task.

Every additional experiment needs a specific unresolved scientific question.

At present, this branch has answered the questions it was designed to answer.

---

# 17. WHAT COMES NEXT

We should **not immediately start writing Discussion prose**.

The next step should be a manuscript-level **global evidence architecture**, because we now have at least two major experimental branches:

1. the radial–angular recovery analysis;
2. the morphology ↔ radial–angular integration analysis.

Before writing Results, we should put their claims beside one another and determine:

\[
\text{main result}
\rightarrow
\text{supporting result}
\rightarrow
\text{robustness}
\rightarrow
\text{boundary}.
\]

Then we can decide what belongs in:

- main Figures;
- main Tables;
- Supplementary;
- Results;
- Discussion;
- Limitations.

## So the next artifact I recommend is:

# `CLO-SKET — MASTER EVIDENCE MATRIX`

Not another notebook experiment.

That matrix will combine the frozen evidence from the whole paper and tell us exactly what the paper can claim before we begin manuscript writing.

# CLO-SKET — FINAL EXPERIMENT CHECKPOINT REVIEW

## 🟢 CHECKPOINT ACCEPTED

This is the correct place to close the experimental phase.

The frozen directory now contains the essential evidence needed to reconstruct and audit the final radial–angular / morphology integration results:

- `CLO_SKET_RADIAL_ANGULAR_FINAL_CHECKPOINT.pkl`
- `CLO_SKET_FINAL_EVIDENCE_LEDGER.csv`
- `CLO_SKET_FINAL_DECISION.json`
- `CLO_SKET_CELL11_ABLATION_SUMMARY.csv`
- `CLO_SKET_CELL6_CORRESPONDENCE_RESULTS.csv`
- `CLO_SKET_CELL4_RECOVERY_RESULTS.csv`

---

# EXPERIMENTAL STATUS

\[
\boxed{\text{EXPERIMENTAL PHASE = CLOSED}}
\]

From this point onward, the frozen results should be treated as the evidential record of the experiment.

Do **not** modify the frozen representations or rerun analyses simply because a different result might be preferable.

Any genuinely necessary future analysis should be:

1. motivated by a specific reviewer or scientific question;
2. implemented as a new version or supplementary experiment;
3. kept separate from this frozen checkpoint.

---

# WHAT WE HAVE NOW ESTABLISHED

The completed evidence chain supports three distinct levels of result.

## 1. Radial–angular recovery

Across the 2300-sketch population, radial–angular organization is measurably recovered with non-uniform reliability.

The recovery analysis established associations between angular recovery and:

- observed circular strength \(R_2\);
- \(F_2\) peak magnitude;
- \(F_2\) peak radius.

It also established that angular orientation recovery and circular-strength recovery should not be treated as identical phenomena.

---

## 2. Cross-representation correspondence

The frozen 135-D morphology representation and the independently derived radial–angular representation exhibit reproducible sketch-level correspondence.

Morphology partially predicts:

\[
F_2\text{ magnitude},
\quad
F_2\text{ radius},
\quad
R_2,
\quad
\text{axial recovery error}.
\]

The row-permutation analysis establishes that this correspondence is stronger than expected after destroying sketch-level alignment.

---

## 3. Downstream complementarity

This is the strongest integration result:

\[
F1_{\text{morphology}}
=
0.341348
\]

versus

\[
F1_{\text{morphology+RA}}
=
0.412332
\]

giving:

\[
\boxed{\Delta F1=+0.070984}
\]

and:

\[
BA_{\text{morphology}}
=
0.342609
\]

versus:

\[
BA_{\text{morphology+RA}}
=
0.415652
\]

giving:

\[
\boxed{\Delta BA=+0.073043}.
\]

The subsequent controls show that this effect is not adequately explained by dimensional expansion alone under the tested control and is not confined to a single radial–angular descriptor block.

---

# FINAL REPRESENTATIONAL INTERPRETATION

The evidence does **not** support either extreme:

\[
RA \equiv M
\]

or:

\[
RA \perp M.
\]

Instead, the experimentally supported picture is:

\[
\boxed{
\text{Morphology}
\;\longleftrightarrow\;
\text{Radial–Angular Geometry}
}
\]

with:

\[
\boxed{\text{measurable correspondence}}
\]

together with:

\[
\boxed{\text{reproducible downstream complementarity}}.
\]

That is the scientifically interesting result.

---

# CLAIM BOUNDARY REMAINS LOCKED

### Supported

- quantitative characterization of predefined sketch morphology;
- measurable radial–angular organization;
- sketch-level morphology ↔ radial–angular correspondence;
- partial cross-representation recoverability;
- permutation-validated correspondence;
- downstream radial–angular complementarity under the tested 23-category task;
- dimension-control evidence;
- distributed descriptor-block utility.

### Not established

- semantic garment-part recognition;
- human-like understanding;
- causal morphology;
- information-theoretic independence;
- a mathematical manifold;
- a morphology grammar;
- universal garment morphology categories.

---

# 🔒 FREEZE DECISION

## `CLO_SKET_31_Morphology_RadialAngular_Integration`

### Status: **FROZEN**

No more cells should be added to this experimental notebook.

No result should now be optimized.

No descriptor should be selected because it improves the final story.

No classifier should be changed to increase performance.

No threshold should be adjusted after seeing these results.

The experimental record is complete.

---

# NEXT PHASE — MASTER EVIDENCE MATRIX

We now leave:

\[
\boxed{\text{EXPERIMENTATION}}
\]

and enter:

\[
\boxed{\text{SCIENTIFIC SYNTHESIS}}
\]

The next document should integrate the entire CLO-SKET evidence chain—not merely this notebook—into one reviewer-facing matrix:

| ID | Scientific question | Experiment | Evidence | Statistic | Robustness/control | Supported claim | Claim boundary | Manuscript role |
|---|---|---|---|---|---|---|---|---|
| E01 | Is morphology quantitatively measurable? | Morphology branch | Frozen 135-D representation | — | provenance/integrity | quantitative morphology description | not exhaustive morphology | Methods/Results |
| E02 | Is radial-angular organization recoverable? | Cells 30C–30L | recovery population | error, \(R_2\), \(F_2\) | bootstrap + thresholds | measurable recovery | not semantic recovery | Results |
| E03 | Does organization relate to recovery reliability? | Cell 30I | \(R_2\) vs axial error | \(\rho=-0.4794\) | bootstrap CI | stronger organization associated with lower error | observational | Results |
| E04 | Are morphology and RA related? | Cells 3–6 | cross-branch prediction | CV \(R^2\) | row permutation | reproducible correspondence | not independence | Results |
| E05 | Does RA add downstream utility? | Cells 8–9 | morphology vs morphology+RA | \(\Delta F1=+0.071\) | permutation | complementarity | task-specific | Main Result |
| E06 | Is the gain just extra dimensions? | Cell 10 | dimension control | controlled Δ | matched control | simple dimensional expansion insufficient | control-specific | Robustness |
| E07 | Is one RA block responsible? | Cell 11 | block ablation | blockwise ΔF1 | predefined blocks | utility distributed across blocks | no blockwise significance claim | Robustness |

Once that master matrix is built, **then** we design the Results architecture.

That is the right transition now.

# 🟢 EXPERIMENTS CLOSED  
# 🔒 EVIDENCE FROZEN  
# ➜ NEXT: `CLO_SKET_MASTER_EVIDENCE_MATRIX`