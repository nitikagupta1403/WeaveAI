# P2-R0-03 — Nyquist / Dimensionality Audit

**Status:** GREEN after accounting clarification  
**Scope:** Paper II positive-harmonic representation with 72 angular bins.

## Finding

With a real-valued angular input and an even angular grid of (N_	heta=72), the rFFT Nyquist harmonic is (k=36). Its Fourier coefficient is real-valued (up to floating-point roundoff), so the imaginary component is structurally zero.

The frozen Paper-II pipeline stores complex arrays and then packs each block as

[
[Re(operatorname{vec}A),Im(operatorname{vec}A)].
]

Therefore the previously reported real widths are exact **packed array widths**, but not all packed coordinates are independent.

## Accounting

### Full RAW72 field

Nominal spectral coefficient slots:

[
36	imes72=2592.
]

Packed real coordinates:

[
2	imes2592=5184.
]

The (72) imaginary coordinates for (k=36) are structurally zero, so

[
5184-72=5112
]

nonredundant real scalar coordinates remain.

### Frozen hybrid

Nominal spectral coefficient slots:

[
16+576+864+48=1504.
]

Packed real coordinates:

[
2	imes1504=3008.
]

The high-band db4 representation retains four radial coefficients for (k=36). Their imaginary components are structurally zero, so

[
3008-4=3004
]

nonredundant real scalar coordinates remain.

### Uniform B=42 baselines

Nominal spectral coefficient slots:

[
36	imes42=1512.
]

Packed real coordinates:

[
3024.
]

The (42) imaginary Nyquist coordinates are structurally zero, so

[
3024-42=2982
]

nonredundant real scalar coordinates remain.

## Reduction metrics

The frozen headline reduction remains correct as a **nominal spectral coefficient-slot** reduction:

[
1-rac{1504}{2592}=41.9753%approx41.98%.
]

The corresponding reduction in nonredundant real scalar coordinates is

[
1-rac{3004}{5112}=41.2363%approx41.24%.
]

The uniform (B=42) baselines are 0.532% larger than the hybrid by packed width (3024 vs 3008), but 0.732% smaller by nonredundant real-scalar count (2982 vs 3004).

## Scientific consequence

This is an accounting correction, not a change to the frozen representation arrays or inferential results. The structurally zero coordinates contribute no Euclidean distance, no variance, and no PCA signal. Retrieval rankings, compression decisions, latent-model comparisons, and inverse-mapping results are unchanged.

## Manuscript rule

Use:

- **nominal spectral coefficient slots** for 2592, 1504, and 1512;
- **packed real coordinates** for 5184, 3008, and 3024;
- **nonredundant real scalar coordinates** for 5112, 3004, and 2982.

Do not describe 3008 as 3008 independent real dimensions.
