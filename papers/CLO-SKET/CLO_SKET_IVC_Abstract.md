# Abstract

Garment sketches encode more than global outline shape: their foreground evidence is distributed across radial position and undirected orientation. We capture this structure with a compact 14-dimensional axial–radial representation derived from shell-conditioned second-harmonic magnitude and doubled-angle axial orientation.

We evaluate the representation on all 2,300 CLO-SKET sketches from 23 garment categories while treating the 230 recovered source garments—not individual image files—as the unit of validation. In the corrective annotation-controlled Experiment 06 analysis, a frozen 135-dimensional morphology representation achieved macro-F1 0.2714 and balanced accuracy 0.2730. Adding the frozen axial–radial representation increased performance to 0.3143 and 0.3157, corresponding to gains of +0.0428 and +0.0426. Category-stratified garment-identity bootstrap intervals excluded zero, and the macro-F1 increment remained positive across all 10 repeated grouped partitions.

Predictive improvement alone does not determine whether the added information is tied to the exact same garment instance. In 2,000 within-category identity-block permutations preserving category and block-size structure, the correctly aligned corrective increment was not exceptional (empirical \(p=0.723\) for macro-F1 and \(p=0.686\) for balanced accuracy). The evidence therefore supports reproducible incremental predictive utility beyond morphology, but not uniquely garment-specific complementarity.

A post-outcome audit of the frozen CLEAN image field identified two images containing exact target-category text. In a separately frozen sensitivity analysis excluding the two affected garment identities, the macro-F1 increment remained +0.0364; all 5,000 identity-bootstrap replicates and all 10 repeated grouped partitions remained positive. This sensitivity is descriptive post-outcome evidence and does not replace the corrective confirmatory result. A subsequent fresh Experiment-08 reproducibility audit also failed its prespecified raster harmonic-magnitude mechanical gate, so later Experiment-08 learned-feature comparisons remain post-outcome and exploratory.

The overall contribution is both representational and methodological: an explicit axial–radial description of garment-sketch geometry together with an identity-aware evaluation framework that separates predictive increment from instance-specific correspondence.

**Keywords:** garment sketches; axial–radial geometry; second harmonic; morphology; grouped cross-validation; identity-aware validation
