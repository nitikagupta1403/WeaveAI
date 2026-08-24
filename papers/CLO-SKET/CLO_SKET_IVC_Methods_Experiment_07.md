## 3.28 Secondary conventional-image-descriptor baseline (Experiment 07)

To address the reviewer-facing question of whether the compact axial–radial representation adds predictive information beyond a conventional image descriptor, a secondary post-audit baseline was frozen before any Experiment 07 outcome was computed. This analysis did not alter Experiment 06, its features, folds, estimator, or claims.

The conventional descriptor was histogram of oriented gradients (HOG). Each native grayscale TIFF sketch was converted to an aspect-ratio-preserving 256×256 representation by isotropic bilinear resizing followed by centered white padding; images were not geometrically stretched. Pixel values were scaled to [0,1]. HOG used 9 orientations, 16×16-pixel cells, 2×2-cell blocks, L2-Hys block normalization, `transform_sqrt=False`, `feature_vector=True`, and no channel axis, producing 8,100 features per sketch. No HOG hyperparameter search, PCA, feature selection, augmentation, or outcome-dependent preprocessing was performed.

The exact 2,300×14 axial–radial matrix, category labels, garment identities, and row-level fold assignment were recovered from the frozen Experiment 06 checkpoint. The checkpoint fold map was adopted as authoritative because it reproduced the locked Experiment 06 pooled results to numerical precision: morphology macro-F1 0.297788 and balanced accuracy 0.298261; morphology plus the complete axial–radial block macro-F1 0.335765 and balanced accuracy 0.336087. The authoritative Experiment 07 test-fold sizes were 459, 460, 462, 460, and 459 sketches, with 46 held-out garment identities per fold, 184 training identities, and zero train/test garment-identity overlap in every fold.

Row order was bridged independently to the archived runtime image paths. Category labels matched exactly; the eight-dimensional radial block reproduced the archived runtime radial matrix exactly; and the six-dimensional axial block reproduced the archived runtime axial descriptors exactly. The frozen HOG matrix had shape 2,300×8,100, contained only finite values, and was hashed before classification.

Two feature sets were then evaluated under the same fold-local preprocessing and classifier specification used in Experiment 06:

\[
\mathrm{HOG}_{8100}
\]

and

\[
\mathrm{HOG}_{8100}\oplus\mathbf z_{RA,14}.
\]

For each fold, `StandardScaler` was fitted on the training partition only, followed by `LogisticRegression` with L2 penalty, \(C=1.0\), `solver=lbfgs`, `max_iter=5000`, `class_weight=None`, and `random_state=20260820`. The primary Experiment 07 contrast was pooled out-of-fold macro-F1 for HOG+RA14 minus HOG; balanced accuracy was secondary. No model or descriptor setting was changed after outcomes were observed.

Uncertainty for the final HOG+RA14-minus-HOG contrast was quantified without model refitting by a paired bootstrap over the 230 garment identities. Complete garment identities were sampled with replacement for 5,000 replicates using seed 20260820, and all sketches and both paired out-of-fold prediction sets for a sampled identity were retained together. Percentile 95% intervals were defined by the 2.5th and 97.5th percentiles of the paired metric-difference distribution. Because an unrestricted identity bootstrap can omit all true examples of a category in occasional replicates, these intervals are reported as identity-level paired bootstrap intervals rather than as a separate permutation test.

Experiment 07 is interpreted strictly as a secondary conventional-descriptor comparator. It tests whether the explicit 14-dimensional axial–radial representation supplies measurable incremental predictive benefit after a high-dimensional local-gradient representation is already present; it is not a new primary hypothesis and does not replace the prespecified Experiment 06 comparison against morphology.
