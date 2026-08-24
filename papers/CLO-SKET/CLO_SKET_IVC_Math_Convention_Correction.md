# IVC Major-Revision Pass 01 — Angular sign and phase-reference correction

## Status

This note records the canonical mathematical convention to be used when rebuilding the IVC manuscript and supplement. It resolves two audit findings without changing any frozen Experiment 06 outcomes.

## 1. Axial-orientation sign under the adopted Fourier convention

The implementation and manuscript use the negative-exponential harmonic convention

\[
F_2(r)=\sum_k p(\theta_k\mid r)e^{-2\mathrm{i}\theta_k}
      =C_2(r)-\mathrm{i}S_2(r).
\]

Therefore

\[
\arg F_2(r)=\operatorname{atan2}(-S_2(r),C_2(r)),
\]

and the undirected axial orientation satisfying

\[
F_2(r)=R_2(r)e^{-2\mathrm{i}\alpha_2(r)}
\]

is

\[
\boxed{
\alpha_2(r)
=-\frac12\arg F_2(r)
=\frac12\operatorname{atan2}(S_2(r),C_2(r))
\pmod{\pi}
}.
\]

Accordingly, any wording that describes \(\alpha_2\) as \(+\tfrac12\arg F_2\) is incorrect under the adopted negative-exponential convention. The implementation-level formula \(\tfrac12\operatorname{atan2}(S_2,C_2)\) is consistent with the corrected expression above.

## 2. Angular-bin indexing and the fixed 2.5° reference offset

The angular histogram uses 72 equal-width bins over \([-\pi,\pi]\), so each bin spans

\[
\Delta_\theta=\frac{2\pi}{72}=5^\circ.
\]

The geometric center of bin \(k\) is

\[
\theta_k^{\mathrm{center}}
=-\pi+\left(k+\frac12\right)\Delta_\theta.
\]

The frozen FFT/index convention instead references the bin index phase

\[
\theta_k^{\mathrm{FFT}}
=-\pi+k\Delta_\theta,
\]

which is equivalent to the left bin edge for the even second harmonic. Hence

\[
\theta_k^{\mathrm{center}}
=\theta_k^{\mathrm{FFT}}+\frac{\Delta_\theta}{2}
=\theta_k^{\mathrm{FFT}}+2.5^\circ.
\]

For \(m=2\), the corresponding center-referenced harmonic is

\[
F_{2,\mathrm{center}}
=e^{-\mathrm{i}\Delta_\theta}F_{2,\mathrm{FFT}},
\]

so the axial orientation is shifted by exactly half a bin:

\[
\boxed{
\alpha_{2,\mathrm{center}}
=\alpha_{2,\mathrm{FFT}}+2.5^\circ
\pmod{180^\circ}
}.
\]

This is a fixed coordinate-reference offset, not a change in the measured second-harmonic magnitude.

## 3. What is and is not affected

The fixed 2.5° reference offset leaves \(R_2=|F_2|\) unchanged. It also leaves relative axial quantities invariant when the same reference is used on both terms, including orientation drift and imposed-rotation shift errors. The doubled-angle axial coordinates undergo a single global rotation of their two-dimensional coordinate frame; the frozen predictive analyses were trained and evaluated consistently in that same frame, so their reported classification metrics and Experiment 06 contrasts do not require recomputation solely because of this reporting correction.

Absolute orientation values, orientation labels in figures, and prose that interprets a particular numerical angle relative to geometric bin centers must, however, state the FFT/index reference or apply the +2.5° center-reference correction.

## 4. Canonical manuscript wording

Use the following formulation wherever the harmonic orientation is introduced:

> Under the adopted negative-exponential Fourier convention, \(F_2=C_2-\mathrm{i}S_2\), the axial orientation is \(\alpha_2=-\tfrac12\arg(F_2)=\tfrac12\operatorname{atan2}(S_2,C_2)\pmod{\pi}\). The frozen FFT implementation references angular-bin indices rather than geometric bin centers, producing a fixed 2.5° axial reference offset. Magnitudes and relative-angle analyses are unaffected; absolute orientations are reported relative to the implementation reference unless explicitly center-corrected.

## 5. Rebuild rule

When the submission manuscript is reassembled, this convention must be synchronized across the Abstract, Introduction, Methods, Results captions, Discussion, Supplementary Material, and all angle-bearing figures. The frozen numerical evidence bundle must not be modified merely to make the prose conform to a different post hoc angular reference.
