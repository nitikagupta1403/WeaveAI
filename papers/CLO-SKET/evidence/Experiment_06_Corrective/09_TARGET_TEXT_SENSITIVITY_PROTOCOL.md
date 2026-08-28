# Experiment 06 Corrective Reanalysis
## Post-outcome target-text sensitivity protocol

### Status

This protocol is frozen after completion of the target-text leakage audit and
before computation of the target-text sensitivity result.

This analysis is a post-outcome sensitivity check. It is not a new
confirmatory experiment and does not replace or reset the inferential status
of the frozen corrective Experiment 06 result.

### Trigger

The frozen review of all 2,300 CLEAN images identified exactly two images with
visible text exactly matching the target garment category:

- row 320: `Cardigan/2-1.tif`
  - corrected garment identity: `Cardigan__G02`
  - corrected fold: 0
  - CLEAN image: `images/0320.png`

- row 2020: `Tunic/2_1.tif`
  - corrected garment identity: `Tunic__G02`
  - corrected fold: 0
  - CLEAN image: `images/2020.png`

No PARTIAL_OR_ABBREVIATED or AMBIGUOUS cases were identified.

### Frozen sensitivity intervention

The sensitivity analysis will exclude exactly these two corrected garment
identities:

- `Cardigan__G02`
- `Tunic__G02`

Exclusion is performed at the garment-identity level rather than by deleting
only the two individual images. No other garment identity, sketch, category,
fold, feature, or observation may be excluded on the basis of the sensitivity
result.

The frozen CLEAN images themselves will not be edited or sanitized.

### Frozen analysis

Apart from exclusion of the two identities above, the sensitivity analysis
must reuse the locked corrective Experiment 06 analysis specification,
including the existing garment-identity split/fold assignments for retained
identities, feature representation, estimator specification, preprocessing,
hyperparameters, evaluation metrics, and uncertainty/inference machinery.

No model selection, tuning, alternative feature construction, alternative
fold construction, or outcome-contingent modification is permitted.

### Interpretation

The sensitivity result will be reported descriptively and transparently
relative to the frozen corrective Experiment 06 result.

No new confirmatory claim will be made from this analysis.

If the incremental predictive result remains materially similar after removal
of the two affected identities, this will be reported as evidence that the
observed corrective Experiment 06 increment is not materially attributable to
those two identified target-text cases.

If the increment is substantially attenuated or collapses, that outcome will
also be reported without further outcome-driven rescue analysis.

The numerical result of this sensitivity analysis must not be used to redefine
this protocol.
