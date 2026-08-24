## 4.21 Conventional HOG baseline showed negligible incremental benefit from RA14

The frozen conventional-image-descriptor baseline substantially outperformed the lower-dimensional morphology baseline on the same garment-identity-disjoint folds. HOG alone achieved pooled out-of-fold macro-F1

\[
0.648242
\]

and balanced accuracy

\[
0.650435.
\]

Appending the unchanged 14-dimensional axial–radial representation yielded macro-F1

\[
0.649135
\]

and balanced accuracy

\[
0.651304.
\]

The resulting secondary contrasts were therefore

\[
\Delta_{\mathrm{HOG}+RA}^{F_1}
=
+0.000894
\]

and

\[
\Delta_{\mathrm{HOG}+RA}^{BA}
=
+0.000870.
\]

Fold-level macro-F1 values for HOG were 0.637525, 0.661015, 0.615841, 0.660780, and 0.643949; the corresponding HOG+RA14 values were 0.637661, 0.656870, 0.621629, 0.663732, and 0.644240. Thus, the very small pooled positive contrast was not uniformly positive across folds.

A paired bootstrap over complete garment identities used 5,000 replicates without refitting either model. For macro-F1, the bootstrap mean contrast was +0.000961 with percentile 95% identity-level interval

\[
[-0.002152,\,+0.004342],
\]

and 72.82% of replicates were positive. For balanced accuracy, the bootstrap mean contrast was +0.000912 with interval

\[
[-0.002238,\,+0.004272],
\]

and 71.10% of replicates were positive.

**Table 14. Secondary conventional HOG baseline under the authoritative Experiment 06 garment-identity folds.**

| Feature set | Dimensions | Macro-F1 | Balanced accuracy |
|---|---:|---:|---:|
| HOG | 8,100 | 0.648242 | 0.650435 |
| HOG + RA14 | 8,114 | 0.649135 | 0.651304 |

**Table 15. Paired garment-identity bootstrap for the HOG+RA14-minus-HOG contrast.**

| Metric | Observed \(\Delta\) | Bootstrap mean \(\Delta\) | 95% identity-level interval | Positive replicates |
|---|---:|---:|---:|---:|
| Macro-F1 | +0.000894 | +0.000961 | [−0.002152, +0.004342] | 3641 / 5000 |
| Balanced accuracy | +0.000870 | +0.000912 | [−0.002238, +0.004272] | 3555 / 5000 |

Both intervals included zero. Experiment 07 therefore provides no clear evidence that appending the compact axial–radial vector yields additional predictive benefit once the high-dimensional HOG descriptor is already present. This negative result is retained without changing the HOG configuration, axial–radial representation, classifier, or validation design.

The result does not contradict Experiment 06. Rather, it shows that the incremental value of the axial–radial representation is baseline-dependent: the same 14 coordinates produced a substantially larger gain when appended to the frozen 135-dimensional morphology representation, whereas their additional contribution over HOG was negligible under the tested protocol.

---
