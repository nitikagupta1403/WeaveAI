# P2_09 Results Three-Way Audit v1.0

**Audited file:** `P2_09_RESULTS_RECONCILED_v1_0.md`

**Against:**
1. `P2_02_EVIDENCE_LEDGER.md`
2. `P2_13_05K_SUPPORT_DEPENDENCE_AND_CLAIM_RECONCILIATION_v1_0.md`
3. frozen 05K D1/D2/D3 claim boundaries

## Overall decision

\[
\boxed{\text{PASS WITH ONE REQUIRED WORDING EDIT}}
\]

The reconciled Results preserve the frozen historical numerical results, correctly separate association from controlled intervention, and do not retroactively modify the original representation-selection or latent-model decisions.

---

## Required edit — remove unsupported “mean” qualifier from 05F effect changes

Current wording:

> “For the high harmonic band, the **mean effect changes** were:”

The frozen 05F record supports the listed high-band effect changes, but the reconciliation should not add an aggregation label unless the source artifact explicitly defines those values as means.

### Replace with

> “For the high harmonic band, the frozen effect changes were:”

No numerical value changes.

---

# Cross-checks that passed

## 1. Representation-validity hierarchy

PASS.

The Results now place:

\[
05F\rightarrow05G\rightarrow05J\rightarrow05K
\]

before the original representation-selection results while explicitly preserving chronology: the support audit was completed later and did not determine the historical selections.

This is consistent with the P2_13 hierarchy:

\[
\text{representation validity}
\rightarrow
\text{representation selection}
\rightarrow
\text{latent interpretation}.
\]

## 2. 05F localization boundary

PASS after the wording edit above.

The Results state that most of the historical high-band change entered with cropping/new raster support and that the later resize/pad contribution was very small.

They correctly state that the earlier bicubic-resampling suspicion was falsified.

They do **not** claim that 05F established the causal mechanism of the crop-only change.

## 3. 05G boundary

PASS.

The Results preserve:

- exact garment-rectangle equality;
- zero centroid map-back error;
- unchanged retained intensities;
- support-related descriptors as the strongest surviving associations.

The text explicitly states that 05G remained associational and did not prove mechanism.

## 4. 05J boundary

PASS.

The Results correctly present the strongest audited support descriptor as an observed association rather than a prospectively primary variable.

They preserve the broad pattern:

\[
\text{crop-induced raster-relative tightening}
\Rightarrow
\text{low/mid}\downarrow,\;
\text{high-mid/high}\uparrow.
\]

They also preserve the required boundary:

\[
\boxed{\text{association}\neq\text{causation}}.
\]

The text does not claim that 05J explains all RAW-to-CROP change.

## 5. 05K controlled intervention

PASS.

The Results correctly state:

- same garment rectangle;
- only surrounding raster support manipulated;
- no resize/interpolation/antialiasing;
- seven support levels;
- 2,300 sketches × 7 support conditions;
- \(s=1\) replay integrity;
- matched object-relative invariance.

No generic claim about “padding changing Fourier content” is made.

## 6. Prespecified 05K predictions

PASS.

The Results preserve the frozen endpoint predictions:

\[
\Delta\text{low}>0,
\qquad
\Delta\text{high-mid}<0,
\qquad
\Delta\text{high}<0,
\]

with no primary directional claim for the mid band.

## 7. Broad endpoint response versus monotonicity

PASS.

The Results distinguish:

- high image-level endpoint concordance;
- 23/23 category-median direction concordance;

from the much weaker requirement of seven-level per-image monotonicity.

No universal monotonic law is claimed.

## 8. Exact category-level 05K inference

PASS.

The Results correctly report:

- 23 category effects;
- \(s=3\) versus \(s=1\);
- exact \(2^{23}\) joint sign assignments;
- common signs across the three directional bands;
- studentized max-\(T\) FWER control.

The low, high-middle, and high endpoint statistics and FWER probabilities are preserved.

## 9. 05K scientific claim boundary

PASS.

The Results use the permitted statement:

\[
\boxed{
\text{raster support is a demonstrated dependency of the historical representation}
}
\]

under the tested same-pixel intervention.

They also preserve the critical limitation that this does not fully explain every natural RAW-to-CROP difference.

## 10. Matched object-relative control

PASS.

The object-relative construction is presented as a matched control/counterfactual and not as a novel normalization method or universally superior representation.

## 11. Historical representation-selection results

PASS.

The frozen selections remain:

\[
\mathrm{DCT}_4/
\mathrm{RAW}_{72}/
\mathrm{RAW}_{72}/
\mathrm{db4}_4.
\]

The original inferential results are unchanged.

The text preserves the negative inferential boundary: failure to support compression is not proof of mathematical incompressibility.

## 12. Hybrid dimensionality

PASS.

The exact frozen dimensions remain:

\[
2592\rightarrow1504
\]

complex coefficients and

\[
3008
\]

packed real coordinates.

No claim that removed coefficients are noise is introduced.

## 13. Whole-representation sensitivity

PASS.

The Results accurately preserve the small difference between the hybrid and uniform RAW42:

\[
0.816766
\quad\text{vs}\quad
0.815896
\]

mean MRR.

The text does not frame the hybrid as a performance breakthrough and explicitly labels these comparisons as descriptive post-selection sensitivities.

## 14. Occupancy/radial-mass sensitivity

PASS.

These remain descriptive post-selection checks and do not reopen the frozen representation.

## 15. Latent-model boundary

PASS.

The Results correctly retain the narrow conclusion that tested AE/VAE models did not establish a multiplicity-controlled task advantage over same-dimensional PCA.

They do not claim PCA is universally superior or that the representation is globally linear.

## 16. Nonlinear-geometry boundary

PASS.

The supported quadratic pairwise relation is kept separate from model-family selection and is not relabeled as manifold curvature or evidence for a required nonlinear encoder.

## 17. Morphology-localization denominator

PASS.

The retained-subspace percentages are explicitly conditioned on the PCA-64 subspace, which accounts for 44.65% of standardized representation variance.

They are not described as percentages of total garment morphology.

---

# Freeze decision

After replacing “mean effect changes” with “frozen effect changes”:

\[
\boxed{\text{P2\_09 RESULTS = FREEZE-READY}}
\]

No additional analysis or experiment is required for this Results reconciliation.
