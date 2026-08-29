## Data Availability

The image data analyzed in this study are from the publicly available CLO-SKET dataset originally released by Fitri Arnia (2020) through Mendeley Data (Version 1; doi:10.17632/jt533nkhsf.1). This study did not collect a new image dataset and does not claim ownership of CLO-SKET. All 2,300 sketches available in the dataset were included in the analysis.

Garment identities used for dependency-aware validation were reconstructed from the category-qualified source identifiers encoded in the original CLO-SKET filenames, as described in the Methods. No additional private or proprietary image dataset is required for the reported analyses. The corrective annotation-controlled image field does use derived manual preprocessing metadata that are deposited with the public evidence, including review status for 928 images, 593 handwriting-box annotations, and adjudication of 22 geometric garment/text overlaps. These derived annotations are preprocessing provenance rather than a separate private image dataset.

Derived analysis code, representation-construction procedures, validation routines, and manuscript-supporting materials are maintained separately from the source image data so that redistribution of the original dataset is not required. The original CLO-SKET images should be obtained from the dataset's official Mendeley Data record.

## Code Availability

The submission-facing computational record for CLO-SKET Paper I is pinned to the versioned Git tag `paper-i-ivc-submission-2026-08-29`:

https://github.com/nitikagupta1403/WeaveAI/tree/paper-i-ivc-submission-2026-08-29/papers/CLO-SKET

The curated computational materials are available under:

```text
papers/CLO-SKET/Codes_paper_I/
```

The public Paper-I package contains five scientific notebooks:

1. `01_Core_Radial_Angular_14D_and_Reconstruction.ipynb` — source-TIFF radial-angular construction, explicit second-harmonic measurements, final 14-dimensional representation, garment-identity-aware validation, and the canonical reconstruction analyses;
2. `02_Parameter_Sensitivity.ipynb` — prespecified parameter, radial-domain, angular-resolution, and radial-resolution sensitivity analyses;
3. `03_Harmonic_Order_Control.ipynb` — low-order harmonic diagnostics supporting the second-harmonic focus;
4. `04_Phase_Conditioning.ipynb` — axial phase/orientation conditioning analyses at the garment-identity level;
5. `05_Rotation_Controls.ipynb` — both analytic/randomized coordinate-frame controls and the distinct rigid-image invariance/equivariance control.

The package also contains `audit_Final_Validation_Shield.ipynb`, retained as a historical audit/provenance record, and `06_Experiment_06_Evidence_Record.md`, which records the frozen historical Experiment-06 design and outputs. That historical package is not presented as a self-contained rerunnable source-to-result pipeline. A distinct executable corrective Experiment-06 workflow is deposited under `Codes_paper_I/Experiment_06_Corrective/`; its governance sequence prospectively froze the corrected identity map, annotation-control artifacts, executable implementation, environment, and pre-outcome checkpoint before the corrective RAW diagnostic and CLEAN confirmatory outcomes were computed. The associated corrective evidence is deposited under `evidence/Experiment_06_Corrective/`.

Fresh executable reproducibility work for Experiment 08 is deposited separately under `Codes_paper_I/Experiment_08/`, with its scientific status and complete evidence chronology recorded in `docs/experiment-08/EXPERIMENT08_EVIDENCE_PROVENANCE_MANIFEST.md`. Experiment 08 failed its frozen mechanical gate and all subsequent predictive results are explicitly classified as post-outcome / exploratory.

In addition to the executable Paper-I notebooks, the repository contains reviewer-facing numerical evidence under `papers/CLO-SKET/evidence/`. The historical Experiment-06 and Experiment-07 records remain preserved for provenance. The current manuscript-facing corrective Experiment-06 evidence is deposited separately under `evidence/Experiment_06_Corrective/`, including the corrected identity/fold artifacts, annotation-control records, frozen corrective outcomes, target-text leakage audit, and the separately frozen post-outcome target-text sensitivity. Experiment-08 evidence remains under `evidence/Experiment_08/`; Experiment 08 is governed by its failed frozen mechanical gate, and all subsequent predictive results are post-outcome / exploratory. Where `evidence/PUBLIC_EVIDENCE_MANIFEST.json` enumerates the older public bundle, it should be interpreted together with the separately deposited corrective Experiment-06 evidence lineage.

The public evidence is intended for numerical audit, provenance verification, and reproduction of the explicitly executable corrective workflows; it is not a replacement for the original CLO-SKET dataset or every historical computational intermediate. In particular, the historical Experiment-06 runtime checkpoint and the 2,300 × 8,100 Experiment-07 HOG feature matrix are intentionally excluded from Git. The absence of the historical Experiment-06 runtime checkpoint does not imply absence of an executable current primary analysis: the later corrective Experiment-06 workflow is separately deposited under `Codes_paper_I/Experiment_06_Corrective/` and is governed by its own frozen chronology. The Experiment-07 HOG feature matrix remains a deterministic intermediate generated by the public Experiment-07 extraction code.

The intended public computational lineage is source-code driven: the official CLO-SKET TIFF images are supplied to Notebook 01, and the downstream validation notebooks operate on the same Paper-I measurement lineage. Large historical runtime-memory pickle snapshots are not treated as the scientific source of record. Where historical checkpoint-loading cells remain for provenance, they should be interpreted as audit/recovery records unless the corresponding checkpoint is explicitly supplied.

Full-harmonic representation-selection, bandwise compression, and latent-geometry analyses belonging to Paper II are intentionally excluded from the Paper-I reproducibility package. The formal ownership boundary is documented in `P1_P2_CLAIM_FIREWALL.md`.

## Software Environment

The project contains several frozen computational lineages and does not retroactively treat them as one homogeneous runtime environment.

| Analysis lineage | Recorded environment |
|---|---|
| Historical Paper-I notebooks / validation shield | Python 3.12.13; NumPy 2.0.2; pandas 2.2.3; scikit-learn 1.6.1; Linux x86_64 |
| Corrective Experiment 06 | Python 3.12.13; NumPy 2.1.3; pandas 2.2.3; Pillow 11.3.0; scikit-learn 1.6.1; SciPy 1.15.1; macOS arm64 |
| Experiment 07 HOG comparator | Python 3.13.15; NumPy 2.1.3; pandas 2.2.3; scikit-learn 1.6.1; scikit-image 0.25.2; Pillow 11.3.0; Linux x86_64 |
| Experiment 08 | Separately pinned executable environment under `Codes_paper_I/Experiment_08/`; the frozen lock includes PyTorch 2.11.0 and torchvision 0.26.0. |

The historical scientific notebooks additionally use SciPy, Matplotlib, Pillow (`PIL`), Joblib, and standard-library modules as declared in their import cells. Where exact package versions were not written into a frozen historical environment record, no retrospective version number is asserted. Corrective Experiment 06, Experiment 07, and Experiment 08 retain their own recorded or pinned environments and must not be inferred from the historical validation-shield environment.

The canonical source notebook supports a configurable dataset location through `CLO_SKET_DATA_ROOT`; its historical Colab path is only the default used during the reported execution.

## Randomness and Reproducibility Lock

Randomness is restricted to explicitly declared model, resampling, permutation, or rotation-control procedures. Deterministic geometric construction of the radial-angular field and the 14-dimensional descriptor does not depend on random initialization.

The manuscript-facing stochastic controls currently frozen in the public notebooks include:

- `HistGradientBoostingRegressor` reconstruction models with `random_state=42`;
- bootstrap diagnostics in the core notebook with `BOOTSTRAP_SEED=20260820` and `N_BOOT=5000` where those diagnostics are used;
- held-out permutation-importance diagnostics with fold-specific seeds `42 + fold` and `142 + fold`;
- analytic garment-identity-randomized rotation control with 10 independent repeats and seeds `20260830, ..., 20260839`;
- the rigid-image rotation experiment itself is deterministic for a given input image and angle because the tested angles are fixed at `[-20, -10, -5, 0, 5, 10, 20]` degrees and the image operator is fixed.

Some older exploratory/category-discrimination cells retained inside the historical core notebook declare additional random states or permutation seeds. Those cells are not promoted here as independent manuscript claims; the governing numerical and inferential design is the one described in the final Methods and Results.

For reproducibility, users should preserve the exact garment-identity grouping structure, fold assignments where frozen, tested rotation angles, estimator hyperparameters, random states, and declared resampling units. A different random seed may produce numerically different bootstrap or randomized-control realizations even when the qualitative conclusion is unchanged.

## Reproducibility Boundary

The reproducibility package is intended to regenerate and audit the Paper-I measurement and validation chain without requiring Paper-II-only code. Historical `.pkl` checkpoint references that survive inside audit/recovery cells do not redefine the current scientific source of record. The historical Experiment-06 evidence remains preserved as provenance, while the manuscript-facing primary predictive claim is governed by the separately frozen corrective Experiment-06 code and evidence under `Codes_paper_I/Experiment_06_Corrective/` and `evidence/Experiment_06_Corrective/`. Experiment 07 remains a frozen secondary comparator under its historical fold provenance, and Experiment 08 remains separately status-bounded by its failed mechanical gate. No statement that the historical Experiment-06 runtime checkpoint is unavailable should be read as a claim that the corrective primary analysis lacks an executable pathway.
