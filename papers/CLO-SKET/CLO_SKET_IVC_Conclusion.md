# 6. Conclusion

This study introduces a compact, explicit axial–radial representation of garment-sketch geometry and tests whether it contributes predictive information beyond a frozen morphology representation under garment-identity-disjoint validation. The 14-dimensional representation comprises eight radial descriptors of second-harmonic magnitude and six axial-safe orientation descriptors. Its construction follows directly from the geometry of undirected orientation: because an axial direction satisfies \(\theta\equiv\theta+\pi\), the second angular harmonic is the lowest non-zero Fourier order compatible with that symmetry.

The primary Experiment 06 result is a reproducible incremental predictive effect. Under the locked five-fold grouped evaluation, morphology alone achieved macro-F1 \(0.297788\) and balanced accuracy \(0.298261\), whereas morphology augmented with the complete axial–radial representation achieved macro-F1 \(0.335765\) and balanced accuracy \(0.336087\). The corresponding increments were

\[
\Delta F_1=+0.037977
\]

and

\[
\Delta BA=+0.037826.
\]

Category-stratified garment-identity bootstrap intervals excluded zero for both metrics: \([+0.020242,+0.055852]\) for macro-F1 and \([+0.020000,+0.056239]\) for balanced accuracy. The effect was also positive across all 10 repeated category-balanced grouped partitions, with mean macro-F1 increment \(+0.032253\) and range \(+0.020620\) to \(+0.043275\). Thus, the observed gain is not attributable to a single favorable identity partition.

The ablations localize most of the directly observed increment to radial organization. The radial block alone achieved macro-F1 \(0.206831\), compared with \(0.081165\) for the axial block, and adding the radial block to morphology increased macro-F1 by \(+0.026752\). Adding the axial block alone increased it by \(+0.002299\). The complete \(M+R+A\) representation nevertheless produced the largest primary score. These results support the predictive relevance of second-harmonic radial organization while leaving any additional conditional contribution of the axial block beyond \(M+R\) as a question for a separately specified test.

The alignment-permutation control places the strongest boundary on interpretation. Correctly aligned \(M+R+A\) did not outperform a category-preserving identity-level misalignment null unusually strongly: the empirical probabilities were \(p=0.762619\) for macro-F1 and \(p=0.729635\) for balanced accuracy. Consequently, the improvement over morphology cannot be attributed, on the present evidence, to exact garment-specific correspondence between the morphology and axial–radial representations. The supported claim is narrower: the compact axial–radial representation contains reproducible **category-conditioned predictive structure** that is useful alongside morphology, but the experiment does not demonstrate uniquely paired garment-level complementarity, statistical independence, or information-theoretic uniqueness.

The complementary geometric controls explain why such caution is necessary. Rigid-image rotation experiments supported the intended invariant/equivariant transformation structure of the representation over the tested perturbations, while garment-identity-specific analytic rotations caused peak-shell axial reconstruction error to approach the \(45^\circ\) chance expectation. Thus, strong phase regularities in upright CLO-SKET sketches depend substantially on the common image coordinate frame. Sensitivity analyses further showed that broad radial summaries are more stable than localized quantities such as peak radius, onset, termination, and concentration, which remain conditional on radial domain and discretization.

Taken together, the evidence supports an explicit but bounded contribution. CLO-SKET contains radial–angular geometric structure that can be measured compactly, transferred to withheld garment identities, and used to improve category discrimination beyond a morphology baseline. The study also shows that predictive improvement alone is insufficient to establish instance-specific representational complementarity: a category-preserving alignment control is required to test that stronger interpretation, and here that test was negative.

The principal contribution is therefore both representational and methodological: a mathematically explicit axial–radial measurement of sparse garment sketches, coupled to a dependency-aware validation framework that distinguishes **predictive increment** from **garment-specific correspondence**. By retaining that distinction, the study identifies not only what the representation adds, but also where the available evidence stops.


---

## Data Availability

The image data analyzed in this study are from the publicly available CLO-SKET dataset originally released by Fitri Arnia (2020) through Mendeley Data (Version 1; doi:10.17632/jt533nkhsf.1). This study did not collect a new image dataset and does not claim ownership of CLO-SKET. All 2,300 sketches available in the dataset were included in the analysis.

Garment identities used for dependency-aware validation were reconstructed from the category-qualified source identifiers encoded in the original CLO-SKET filenames, as described in the Methods. No additional private, proprietary, or manually annotated image dataset was used in the reported analyses.

Derived analysis code, representation-construction procedures, validation routines, and manuscript-supporting materials are maintained separately from the source image data so that redistribution of the original dataset is not required. The original CLO-SKET images should be obtained from the dataset's official Mendeley Data record.

## Code Availability

The curated computational materials supporting CLO-SKET Paper I are available in this repository under:

```text
papers/CLO-SKET/Codes_paper_I/
```

The public Paper-I package contains five scientific notebooks:

1. `01_Core_Radial_Angular_14D_and_Reconstruction.ipynb` — source-TIFF radial-angular construction, explicit second-harmonic measurements, final 14-dimensional representation, garment-identity-aware validation, and the canonical reconstruction analyses;
2. `02_Parameter_Sensitivity.ipynb` — prespecified parameter, radial-domain, angular-resolution, and radial-resolution sensitivity analyses;
3. `03_Harmonic_Order_Control.ipynb` — low-order harmonic diagnostics supporting the second-harmonic focus;
4. `04_Phase_Conditioning.ipynb` — axial phase/orientation conditioning analyses at the garment-identity level;
5. `05_Rotation_Controls.ipynb` — both analytic/randomized coordinate-frame controls and the distinct rigid-image invariance/equivariance control.

The package also contains `audit_Final_Validation_Shield.ipynb`, retained as an audit/provenance record rather than as the canonical source-to-result execution path.

The primary incremental-representation experiment is additionally frozen as **Experiment 06**. Its permanent evidence bundle contains the master checkpoint `CLO_SKET_EXPERIMENT06_FINAL_CHECKPOINT.pkl` (SHA256 `6e2c600c9cef37c3edcae18300793e37265ba866ee93d83c825aa1b5ad522018`), a final manifest, pooled primary results, ablation contrasts, the category-stratified identity bootstrap, all repeated grouped-CV summaries and fold results, the complete 2,000-permutation alignment null and summary, the evidence ledger, manuscript summary, claim lock, final decision, provenance hashes, and figure metadata. The bundle is the frozen source of record for Experiment 06 numerical claims.

The intended public computational lineage is source-code driven: the official CLO-SKET TIFF images are supplied to Notebook 01, and the downstream validation notebooks operate on the same Paper-I measurement lineage. Large historical runtime-memory pickle snapshots are not treated as the scientific source of record. Where historical checkpoint-loading cells remain for provenance, they should be interpreted as audit/recovery records unless the corresponding checkpoint is explicitly supplied.

Full-harmonic representation-selection, bandwise compression, and latent-geometry analyses belonging to Paper II are intentionally excluded from the Paper-I reproducibility package. The formal ownership boundary is documented in `P1_P2_CLAIM_FIREWALL.md`.

## Software Environment

Two frozen execution lineages support the reported analyses and are distinguished explicitly rather than collapsed into a single retrospective environment.

The earlier Paper-I validation shield recorded:

- Python 3.12.13;
- NumPy 2.0.2;
- pandas 2.2.3;
- scikit-learn 1.6.1;
- Linux x86_64 execution environment.

The permanently frozen Experiment 06 confirmatory run recorded:

- Python 3.13.15;
- NumPy 2.1.3;
- pandas 2.2.3;
- scikit-learn 1.6.1;
- random state 20260820.

The difference reflects separate frozen execution sessions; no claim is made that all analyses were executed under one software image.

The scientific notebooks additionally use SciPy, Matplotlib, Pillow (`PIL`), Joblib, and standard-library modules as declared in their import cells. Pillow is used for TIFF decoding and for the rigid-image rotation control. Because exact SciPy, Matplotlib, Pillow, and Joblib version strings were not written into the frozen validation-shield environment record, no retrospective version number is asserted for those packages here. Their imports and algorithmic roles are explicit in the notebooks, and the manuscript reports the fixed image-rotation operator and interpolation settings used in the rigid-image control.

The canonical source notebook supports a configurable dataset location through `CLO_SKET_DATA_ROOT`; its historical Colab path is only the default used during the reported execution.

## Randomness and Reproducibility Lock

Randomness is restricted to explicitly declared model, resampling, permutation, or rotation-control procedures. Deterministic geometric construction of the radial-angular field and the 14-dimensional descriptor does not depend on random initialization.

The manuscript-facing stochastic controls currently frozen in the public notebooks include:

- `HistGradientBoostingRegressor` reconstruction models with `random_state=42`;
- bootstrap diagnostics in the core notebook with `BOOTSTRAP_SEED=20260820` and `N_BOOT=5000` where those diagnostics are used;
- Experiment 06 paired garment-identity bootstrap and category-stratified robustness bootstrap with 5,000 replicates and random state `20260820`;
- Experiment 06 repeated grouped partitions with seeds `20260820, ..., 20260829`;
- Experiment 06 category-preserving, block-size-matched alignment control with 2,000 permutations and random state `20260820`;
- held-out permutation-importance diagnostics with fold-specific seeds `42 + fold` and `142 + fold`;
- analytic garment-identity-randomized rotation control with 10 independent repeats and seeds `20260830, ..., 20260839`;
- the rigid-image rotation experiment itself is deterministic for a given input image and angle because the tested angles are fixed at `[-20, -10, -5, 0, 5, 10, 20]` degrees and the image operator is fixed.

Some older exploratory/category-discrimination cells retained inside the historical core notebook declare additional random states or permutation seeds. Those cells are not promoted here as independent manuscript claims; the governing numerical and inferential design is the one described in the final Methods and Results.

For reproducibility, users should preserve the exact garment-identity grouping structure, fold assignments where frozen, tested rotation angles, estimator hyperparameters, random states, and declared resampling units. A different random seed may produce numerically different bootstrap or randomized-control realizations even when the qualitative conclusion is unchanged.

## Reproducibility Boundary

The reproducibility package is intended to regenerate and audit the Paper-I measurement and validation chain without requiring Paper-II-only code. Historical `.pkl` checkpoint references that survive inside audit/recovery cells do not redefine the scientific source of record. The canonical evidence remains the explicit source code, the original CLO-SKET images, the final manuscript Methods/Results, and the claim firewall.

---

# Declarations

## Funding

[TO BE COMPLETED TRUTHFULLY BEFORE SUBMISSION]

## Competing interests

[TO BE COMPLETED TRUTHFULLY BEFORE SUBMISSION]

## Author contributions (CRediT)

[TO BE COMPLETED TRUTHFULLY BEFORE SUBMISSION]

## Acknowledgements

[TO BE COMPLETED IF APPLICABLE]

## Ethics statement

[TO BE COMPLETED IF REQUIRED BY THE JOURNAL; DO NOT ADD AN ETHICS APPROVAL CLAIM UNLESS APPLICABLE]

---
