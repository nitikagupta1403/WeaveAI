## Data Availability

The image data analyzed in this study are from the publicly available CLO-SKET dataset originally released by Fitri Arnia (2020) through Mendeley Data (Version 1; doi:10.17632/jt533nkhsf.1). This study did not collect a new image dataset and does not claim ownership of CLO-SKET. All 2,300 sketches available in the dataset were included in the analysis.

Garment identities used for dependency-aware validation were reconstructed from the category-qualified source identifiers encoded in the original CLO-SKET filenames, as described in the Methods. No additional private, proprietary, or manually annotated image dataset was used in the reported analyses.

Derived analysis code, representation-construction procedures, validation routines, and manuscript-supporting materials are maintained separately from the source image data so that redistribution of the original dataset is not required. The original CLO-SKET images should be obtained from the dataset's official Mendeley Data record.

---

## Code Availability

The curated computational materials supporting CLO-SKET Paper I are available in the public WeaveAI repository under:

`papers/CLO-SKET/Codes_paper_I/`

The package contains five manuscript-facing scientific notebooks:

1. `01_Core_Radial_Angular_14D_and_Reconstruction.ipynb` — canonical source-to-measurement pipeline, 14-dimensional representation construction, garment-identity-aware validation, and reconstruction analyses;
2. `02_Parameter_Sensitivity.ipynb` — support/concentration, radial-domain, angular-resolution, radial-resolution, and common-physical-domain sensitivity analyses;
3. `03_Harmonic_Order_Control.ipynb` — low-order harmonic diagnostics supporting the second-harmonic focus;
4. `04_Phase_Conditioning.ipynb` — axial phase/orientation conditioning and garment-identity-aware association analyses; and
5. `05_Rotation_Controls.ipynb` — both the analytic/garment-identity-randomized reconstruction coordinate-frame controls and the distinct rigid-image invariance/equivariance audit of the final 14-dimensional representation.

An additional notebook, `audit_Final_Validation_Shield.ipynb`, is retained for historical validation and provenance auditing. It is not the primary source-to-result execution path and may reference frozen runtime checkpoints used during development.

The intended public reproducibility workflow is source-code driven: the original CLO-SKET TIFF images are obtained from the official dataset release, the canonical representation is rebuilt from source images, and the targeted validation notebooks are then used to reproduce the manuscript-facing controls and sensitivity analyses. Large private runtime-memory pickle snapshots are not treated as the canonical scientific source and are not required as part of the intended reproducibility package.

The execution order, scientific role of each notebook, rotation-control distinction, and Paper-I/Paper-II scope boundary are documented in `papers/CLO-SKET/Codes_paper_I/README.md`.

---

## Reproducibility Scope

The released code is organized specifically around the scientific claims of CLO-SKET Paper I. Full-harmonic representation selection, bandwise spectral compression, and latent-geometry analyses belong to Paper II and are intentionally excluded from this package.

Where stochastic procedures are used, seeds and resampling/permutation counts are declared in the relevant notebook cells. Garment identity is preserved as the dependency unit for grouped validation and inferential procedures where specified in the manuscript. Historical audit cells that depend on frozen checkpoint files are retained for provenance but should not be interpreted as the canonical execution route.
