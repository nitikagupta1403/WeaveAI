# Paper II Figure–Table Architecture Reconciliation v1.0

## Decision

The pre-audit figure blueprint is no longer sufficient as the final submission figure plan because it places representation selection before the later representation-validity result.

The reconciled manuscript requires the visual evidence order:

\[
\boxed{
\text{representation construction}
\rightarrow
\text{representation validity}
\rightarrow
\text{representation selection}
\rightarrow
\text{latent validation}
\rightarrow
\text{morphology interpretation}
}
\]

## Recommended main figures

### Figure 1 — Radial–angular Fourier morphology representation
Purpose: define \(P(\theta\mid r)\), \(F_k(r)\), and the prespecified harmonic bands.  
Evidence role: mathematical / descriptive.  
Status: manuscript caption now inserted.

### Figure 2 — Raster-support dependence of the measurement system
Purpose: show the controlled same-pixel support intervention and the matched object-relative control.

Recommended panels:
- A: same garment patch embedded at selected support levels \(s\);
- B: raster-relative versus object-relative coordinate construction;
- C: population median band-fraction trajectories across \(s\);
- D: endpoint category effects / exact max-\(T\) inference for low, high-mid, and high;
- E: explicit distinction between broad endpoint concordance and non-universal per-image monotonicity.

Central caption claim:
> With garment pixels held fixed, enlarging surrounding raster support systematically redistributed angular spectral allocation in the raster-relative representation, whereas the matched object-relative control remained numerically invariant under the same intervention.

Do not claim that padding creates frequency content or that support explains all preprocessing effects.

### Figure 3 — Evidence-controlled harmonic-dependent radial representation
Purpose: retain the original representation-selection result as a separate inferential contribution.

Recommended panels:
- A: candidate radial encodings by harmonic band;
- B: identity-disjoint validation design;
- C: band-specific held-out effects and bootstrap intervals;
- D: multiplicity-controlled decisions;
- E: resulting DCT/raw/raw/db4 hybrid and dimensionality reduction.

Central caption claim:
> Support for the tested compact radial encodings differed across angular harmonic bands, yielding a heterogeneous radial representation while preserving complete radial structure where compression was not supported.

### Figure 4 — Nonlinear latent-model validation
Purpose: distinguish nonlinear structure from validated nonlinear-model utility.

Recommended panels:
- A: AE/VAE versus same-dimensional PCA contrasts;
- B: adjusted inferential outcomes;
- C: supported quadratic pairwise relation;
- D: local-dimensionality diagnostic, explicitly descriptive.

Central caption claim:
> Detectable nonlinear predictive structure did not establish a multiplicity-controlled task advantage for the tested nonlinear latent encoders.

### Figure 5 — Exact latent-to-radial-harmonic morphology localization
Purpose: show mathematical traceability of retained PCA variation.

Recommended panels:
- A: exact inverse-mapping chain;
- B: selected PC energy maps;
- C: harmonic-band localization;
- D: radial-zone localization;
- E: 3×4 joint radial × harmonic matrix.

Required caption denominator:
> all localization percentages refer to variance-weighted mapped morphology energy within the retained PCA-64 subspace, which accounts for 44.65% of standardized representation variance.

Do not describe outer-radial localization as garment boundary or silhouette and do not claim radial × harmonic interaction.

## Main tables

The reconciled Results currently contain five tables:

1. controlled support-enlargement trajectories;
2. confirmatory radial-representation decisions;
3. whole-representation descriptive sensitivity;
4. nonlinear latent-model contrasts;
5. retained PCA-64 radial-harmonic localization.

This numbering is coherent with the reconciled Results sequence and should be retained.

## Figure numbering consequence

The old four-figure blueprint should be treated as historical planning, not final submission architecture.

The final main-text visual plan should use **five figures**, because representation validity is now a distinct scientific layer rather than being folded into representation selection.

No frozen numerical artifact is changed by this figure-plan amendment.
