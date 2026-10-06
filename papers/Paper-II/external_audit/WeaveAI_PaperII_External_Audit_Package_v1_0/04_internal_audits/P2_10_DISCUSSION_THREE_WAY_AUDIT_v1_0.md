# P2_10 Discussion Three-Way Audit v1.0

**Audited file:** `P2_10_DISCUSSION_RECONCILED_v1_0.md`

**Against:**
1. `P2_02_EVIDENCE_LEDGER.md`
2. `P2_13_05K_SUPPORT_DEPENDENCE_AND_CLAIM_RECONCILIATION_v1_0.md`
3. frozen 05K D1/D2/D3 claim boundaries

## Overall decision

\[
\boxed{\text{PASS WITH TWO REQUIRED WORDING EDITS}}
\]

The Discussion is scientifically aligned with the frozen evidence and the P2_13 claim hierarchy. Two wording changes are required before freeze to prevent overstatement.

---

## Required edit 1 — avoid “removed” language for the tested support dependency

Current wording in Section 5.1:

> “A matched object-relative construction removed that tested dependency.”

This is close to the frozen claim, but “removed” can read as a general method claim.

### Replace with

> “A matched object-relative construction was numerically invariant under that same support intervention.”

### Reason

This keeps the object-relative field in its proper role as a matched control/counterfactual, not as a claimed universally support-invariant solution.

---

## Required edit 2 — tighten the future-work statement around 05H2

Current wording in Section 5.12:

> “The 05H2 audit already showed that support for compression redistributes under object-relative normalization rather than simply reproducing the historical high-band result.”

This is directionally correct but could be read as if 05H2 established a new final representation recommendation.

### Replace with

> “The 05H2 audit showed that the pattern of band-wise compression support differs under the tested object-relative construction and therefore should not be used as a retrospective substitute for the historical hybrid.”

### Reason

This more directly preserves the anti-retroactive-selection boundary.

---

# Cross-checks that passed

## 1. Representation-validity hierarchy

PASS.

The Discussion now begins with representation validity before representation allocation and latent interpretation.

This matches P2_13.

## 2. 05F / 05G / 05J / 05K evidential separation

PASS.

The Discussion correctly distinguishes:

- 05F as localization;
- 05G/05J as association;
- 05K as controlled same-pixel intervention.

No complete preprocessing mechanism is claimed.

## 3. Bicubic-resampling boundary

PASS.

The earlier bicubic-resampling suspicion is correctly described as falsified rather than retained as mechanism.

## 4. Same-pixel support intervention

PASS.

The Discussion correctly characterizes 05K as changing surrounding support while preserving the garment rectangle and excluding resize/interpolation/etc.

## 5. 05K causal scope

PASS.

The text uses the allowed narrow statement that raster support is a demonstrated dependency of angular spectral allocation under the historical raster-relative representation.

It does not generalize to all Fourier descriptors.

## 6. Object-relative comparator

PASS after Required edit 1.

It is treated as a matched counterfactual rather than a novel normalization invention.

## 7. Prior-art boundary

PASS.

The Discussion explicitly concedes prior art for:

- Fourier descriptors;
- EFD;
- polar/radial-angular descriptors;
- ART;
- Zernike normalization;
- translation/rotation/scale normalization;
- window/support theory;
- zero-padding;
- crop sensitivity.

## 8. Novelty language

PASS.

The Discussion uses:

> “we did not identify a direct precedent in the reviewed literature”

rather than claiming absolute priority.

## 9. Zero-padding distinction

PASS.

The text does not claim padding creates low-frequency garment information and correctly places the effect in coordinate remapping.

## 10. Historical hybrid

PASS.

The original frozen hybrid remains:

\[
\mathrm{DCT}_4/
\mathrm{RAW}_{72}/
\mathrm{RAW}_{72}/
\mathrm{db4}_4.
\]

The Discussion explicitly states that 05K does not retroactively invalidate or replace it.

## 11. Compression-claim boundary

PASS.

The Discussion preserves:

\[
\text{compress where supported; preserve otherwise}
\]

without calling non-supported bands mathematically incompressible.

## 12. Uniform RAW42 baseline

PASS.

The competitive uniform RAW42 baseline remains visible, preventing a performance-breakthrough claim.

## 13. Nonlinear-model boundary

PASS.

The Discussion correctly distinguishes lack of validated AE/VAE advantage from absence of nonlinear structure.

## 14. Morphology-localization boundary

PASS.

The Discussion preserves the strict PCA-64 denominator and avoids semantic interpretation of radial zones/harmonic bands.

## 15. Future-work chronology

PASS after Required edit 2.

Future object-relative re-selection is correctly framed as a new prospective study rather than a retroactive change to Paper II.

---

# Freeze decision

After the two required edits:

\[
\boxed{\text{P2\_10 DISCUSSION = FREEZE-READY}}
\]

No additional analysis is required for this reconciliation.
