# P2-R0-03 — Nyquist / Dimensionality Audit

**Status:** GREEN — direct Nyquist and frozen db4 high-block checks verified  
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


## Computational verification performed before closure

Using the uploaded canonical runtime checkpoint with SHA-256

`4e7d6ea942b3fd4b506c330f624178e154022683756e6edcffcf7aa65bd69f9f`,

the following checks were executed directly on `conditional_angular`:

- shape: `(2300, 72, 72)`;
- dtype: real-valued `float64`;
- recomputed `np.fft.rfft(..., axis=-1)` shape: `(2300, 72, 37)`;
- `max(abs(Im(F[...,36]))) = 0.0`;
- `max(abs(Im(F[...,35]))) = 0.9142568589369724`, confirming that the zero imaginary component is specific to the Nyquist bin rather than a general artifact;
- packing the complete non-DC field into 5184 real coordinates gives exactly 72 zero-variance coordinates;
- those 72 coordinates are exactly the final 72 packed imaginary coordinates, corresponding to the 72 radial samples of `k=36`;
- `StandardScaler` maps all 72 coordinates to exact zeros and reports exactly 72 zero-variance features.

The saved executed downstream notebook independently reports `Zero-IQR dimensions: 72` for the full 5184-coordinate shared geometry, consistent with the direct checkpoint audit.

### Closure check — PASSED

The frozen Cell-14 high-band wavelet construction was rerun from the canonical checkpoint using the preserved settings:

- wavelet: `db4`
- signal length: `72`
- DWT level: `3`
- boundary mode: `periodization`
- retained budget: `4`

Observed outputs:

- `high_complex.shape == (2300, 12, 72)`
- `Z_high_WAV4.shape == (2300, 12, 4)`
- `max |Im F36| = 0.0`
- `max |Im F35| = 0.914256858937`
- `max |Nyquist wavelet imag| = 0.0`
- `nonzero Nyquist imag count = 0`
- `max |Nyquist wavelet real| = 1.838485670885`

Thus the `k=36` compressed coefficients are demonstrably real-valued in the frozen pipeline, while the neighboring harmonic remains genuinely complex. The four packed imaginary coordinates associated with compressed `k=36` are therefore structurally redundant.

**Final audit status: GREEN.**
