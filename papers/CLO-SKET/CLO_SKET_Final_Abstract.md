# Abstract

Garment sketches encode silhouette, proportion, and directional organization through sparse visual structure, yet predictive improvement from combining geometric representations does not establish that their information is specific to the same garment instance. We introduce a compact axial–radial representation of garment-sketch geometry and evaluate both its incremental predictive utility and the stronger requirement of garment-level correspondence.

Using all 2,300 CLO-SKET sketches from 23 categories and 230 recovered garment identities, foreground evidence was represented by centroid-relative radial shells and their second circular harmonic. Eight radial descriptors of harmonic magnitude and six axial-safe orientation descriptors formed a 14-dimensional representation. Evaluation used category-balanced, garment-identity-disjoint validation with a frozen 135-dimensional morphology baseline and a fixed classifier.

Morphology alone achieved pooled out-of-fold macro-F1 of 0.2978, whereas morphology augmented with axial–radial geometry achieved 0.3358, yielding \(\Delta F_1=+0.0380\). Balanced accuracy increased by \(+0.0378\). A category-stratified garment-identity bootstrap gave a 95% interval of \([+0.0202,+0.0559]\) for the macro-F1 increment, and the effect remained positive across all 10 repeated grouped partitions. Ablation localized most direct predictive value to the radial block.

A category-preserving identity-block permutation provided a stronger test of correspondence. Across 2,000 permutations that disrupted 97.39% of exact garment-level alignment while retaining category and block-size structure, the correctly aligned increment was not exceptional (\(p=0.763\) for macro-F1; \(p=0.730\) for balanced accuracy).

The axial–radial representation therefore provides reproducible incremental predictive utility beyond morphology, but the evidence does not support uniquely paired garment-level complementarity. The study demonstrates the value of identity-aware validation for distinguishing predictive increment from instance-specific correspondence.

**Keywords:** garment sketch; shape representation; axial geometry; Fourier descriptor; grouped validation; representation correspondence

## Highlights

- A 14-D axial–radial representation captures explicit garment-sketch geometry
- Complete garment identities are withheld throughout model validation
- Axial–radial geometry improves macro-F1 beyond frozen morphology
- The predictive increment remains positive across 10 grouped partitions
- Correct garment pairing is not supported by the alignment permutation
