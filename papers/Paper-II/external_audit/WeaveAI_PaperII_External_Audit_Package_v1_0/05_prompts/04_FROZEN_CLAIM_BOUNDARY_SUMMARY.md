# Frozen Claim Boundary Summary — External Audit Aid

This summary exists to help reviewers test manuscript drift. It does not replace the frozen source files.

## Representation validity

Allowed:
- Under the tested historical raster-relative radial–angular representation, surrounding raster support is a demonstrated dependency of angular spectral allocation.
- With garment pixels held fixed, support enlargement produces broad category-consistent endpoint redistribution toward lower angular bands and away from high-middle/high bands.
- The matched object-relative control is numerically invariant under the same same-pixel support intervention.

Not allowed:
- support explains every RAW→CROP effect;
- padding creates garment frequency content;
- every image changes monotonically;
- object-relative coordinates are universally superior;
- generic Fourier support sensitivity is new.

## Representation selection

Allowed:
- Evidence for tested radial compression differs across harmonic scale under the frozen identity-disjoint design.
- Frozen hybrid: DCT4 / RAW72 / RAW72 / db4-wavelet4.
- Unsupported bands retain full radial structure.

Not allowed:
- unsupported bands are intrinsically incompressible;
- hybrid is a major retrieval-performance breakthrough;
- object-relative control retroactively validates or replaces the historical hybrid.

Reviewer-facing sensitivity:
- hybrid MRR = 0.816766;
- uniform RAW42 MRR = 0.815896.

## Latent validation

Allowed:
- No tested AE/VAE representation established a multiplicity-controlled advantage over same-dimensional PCA.
- A fixed quadratic audit detected nonlinear pairwise predictability.

Not allowed:
- morphology space is globally linear;
- PCA is universally superior;
- nonlinear models are generally inferior;
- pairwise nonlinear predictability proves manifold curvature.

## Morphology localization

All localization is conditional on the retained PCA-64 subspace:
- PCA-64 standardized variance = 44.65%;
- intermediate harmonics k=5:24 = 78.54%;
- outer radial zone = 66.84%;
- outer × intermediate joint localization = 51.30%.

Not allowed:
- semantic garment-part interpretation from radial/harmonic coordinates;
- radial×harmonic enrichment/interaction claim without a test;
- percentages interpreted as fractions of total garment morphology.

## Novelty boundary

Safe:
- normalization mathematics is prior art;
- Fourier/polar/radial-angular shape representation is prior art;
- the contribution is a controlled representation-validity audit plus evidence-controlled allocation of representation complexity;
- “we did not identify a direct precedent in the reviewed/searched literature…”

Unsafe:
- “first-ever”;
- “no prior paper exists”;
- novelty based on Fourier transforms, polar coordinates, normalization, PCA inversion, or fashion-domain transfer alone.
