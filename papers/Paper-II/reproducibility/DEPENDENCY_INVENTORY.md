# Paper II dependency inventory

## Public inputs

| Input | Status | Role |
|---|---|---|
| CLO-SKET v1, DOI `10.17632/jt533nkhsf.1` | Public at Mendeley Data | Original 2,300 TIFF sketches |
| `CLO_Raw_fft_UPSTREAM_GENERATOR.ipynb` | Public, hash locked | Image-to-radial-angular lineage |
| `CLO_SKET_Probabilistic_Fourier_Morphology_FROZEN_EXECUTED.ipynb` | Public, hash locked | Executed Paper-II evidence record |

The images are not redistributed by WeaveAI.

## Historical checkpoint dependencies

These pickle files are referenced by the preserved workflow but are not in the
public release. Pickle files must only be opened when they come from a trusted
archive.

| Checkpoint | Produced/used role | Public? |
|---|---|---|
| `CLO_SKET_runtime_backup.pkl` | Upstream runtime snapshot | No |
| `CLO_SKET_runtime_backup_AFTER_CELL25.pkl` | Initializes the downstream notebook | No |
| `CLO_SKET_MORPHOLOGY_INFERENCE_AFTER_CELL07_VERIFIED.pkl` | Frozen identity/category alignment | No |
| `CLO_SKET_PROBABILISTIC_FOURIER_AFTER_CELL07.pkl` | Fourier-state checkpoint | No |
| `CLO_SKET_PROBABILISTIC_FOURIER_AFTER_CELL08_VERIFIED.pkl` | Verified Fourier-state checkpoint | No |
| `CLO_SKET_FINAL_IDENTITY_FIGURES.pkl` | Exact identity vector and five-fold assignment | No |

Because these objects are absent, the public release cannot regenerate the exact
sample/fold CSVs or all publication figures. `scripts/export_manifests.py`
provides a validated export path when the trusted frozen identity package is
available.

## Observed Python dependency families

Static inspection of the notebooks identifies NumPy, pandas, Pillow,
Matplotlib, SciPy, scikit-learn, PyWavelets, tifffile and PyTorch, together with
Google Colab/Drive helpers. Notebook output identifies Python 3.12 and a
scikit-learn 1.5-era runtime, but the complete historical package lock was not
recorded. `environment.yml` is therefore an inspection/helper environment, not
a claim of exact historical bitwise reproducibility.

## Frozen random seeds reported in the record

| Purpose | Seed |
|---|---:|
| Confirmatory stratified bootstrap | `20260913` |
| Confirmatory category-cluster permutation | `20260914` |
| Latent-model base seed | `20260821` |

Additional seed use is inventoried by `scripts/audit_release.py` directly from
the preserved notebook source.
