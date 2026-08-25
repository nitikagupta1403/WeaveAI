# Paper II — Computational Reproducibility and Provenance

This directory preserves the computational provenance associated with Paper II.

## Current public-release scope

This directory is a hash-verified provenance record, not a clean-environment,
end-to-end reproduction package. The current public release contains the two
notebooks listed below and their checksums. It does **not** contain:

- the CLO-SKET image dataset, which remains available from Mendeley Data at
  <https://doi.org/10.17632/jt533nkhsf.1>;
- the historical `.pkl` intermediate checkpoint files referenced by the
  preserved notebooks;
- a portable package/environment specification; or
- publication-figure export scripts or frozen figure-input objects.

The notebooks therefore support audit of computational origin and embedded
results. They cannot presently be executed end to end from the public contents
of this directory alone.

## Scientific evidence lock

The numerical results reported in the manuscript are frozen.

The authoritative scientific evidence ledger is:

`../P2_02_EVIDENCE_LEDGER.md`

The files in this directory document the computational lineage of those
results. They must not be used for post-hoc retuning, altered model selection,
or replacement of the frozen manuscript evidence by newly obtained results.

## Computational lineage

The audited computational lineage is:

CLO-SKET TIFF images
    ↓
`provenance/CLO_Raw_fft_UPSTREAM_GENERATOR.ipynb`
    ↓
`CLO_SKET_runtime_backup.pkl`
    ↓
continued radial-angular computation
    ↓
`CLO_SKET_runtime_backup_AFTER_CELL25.pkl`
    ↓
`provenance/CLO_SKET_Probabilistic_Fourier_Morphology_FROZEN_EXECUTED.ipynb`
    ↓
Paper-II radial-representation inference,
hybrid representation,
latent-model validation,
and retained-PCA morphology analysis
    ↓
frozen manuscript evidence

The intermediate checkpoint files are computational state snapshots rather
than independent scientific inputs. They are not included in the current public
release. In particular, the downstream notebook expects
`CLO_SKET_runtime_backup_AFTER_CELL25.pkl`; additional historical checkpoints
referenced later in the notebook also retain their original Google Drive paths.

## 1. Upstream radial-angular generator

`provenance/CLO_Raw_fft_UPSTREAM_GENERATOR.ipynb`

SHA-256:

`8ca60402cd64d656381f6a19053dd443fb1e7b12a87efc5b5fe4e91c9d7525e2`

This notebook ingests CLO-SKET TIFF images and performs the upstream
radial-angular morphology computation.

During the preserved workflow it writes:

`CLO_SKET_runtime_backup.pkl`

and subsequently:

`CLO_SKET_runtime_backup_AFTER_CELL25.pkl`

The latter checkpoint initializes the frozen downstream Paper-II analysis.

## 2. Frozen executed Paper-II record

`provenance/CLO_SKET_Probabilistic_Fourier_Morphology_FROZEN_EXECUTED.ipynb`

SHA-256:

`6535735705c23fc3ea25b10583e2baeab816d274263e79b1c9f69cc1f6430367`

This 46-code-cell notebook is the preserved executed downstream Paper-II
computational snapshot. Forty-five of its 46 code cells carry execution
counts.

The notebook was audited against 22 high-specificity numerical and
computational anchors from the frozen Paper-II evidence and matched all 22.

The audited anchors cover:

- harmonic-dependent radial-representation inference;
- bootstrap uncertainty and multiplicity-controlled inference;
- frozen hybrid representation dimensionality;
- latent-model validation;
- retained PCA analysis;
- radial-harmonic morphology localization; and
- frozen random-number seeds.

## Historical extended analysis record

A later 95-code-cell research notebook was also identified during provenance
audit. It matches the same 22 frozen evidence anchors and contains additional
audit, development, manuscript-construction, Colab-environment, and historical
output material.

That extended notebook remains in the private research archive and is not
designated as the public executed record.

A structural audit showed that 45 of the 46 code cells in the frozen executed
record occur exactly in the extended record. The one reserve-only cell is a
finite-value integrity audit over already-computed arrays.

## Historical execution environment

These notebooks preserve historical Google Colab / Google Drive paths and
embedded outputs from the original research workflow. Those paths document
the original execution environment and are not expected to resolve unchanged
on another machine.

The hash-locked provenance notebooks are intentionally preserved rather than
silently rewritten for portability.

Portable execution instructions and submission-facing figure-export code are a
separate reproducibility layer and are not represented as part of this public
provenance release.

## Figures

Publication-only figure export code is not included in the current public
provenance release. When added as a separate reproducibility layer, it should be
stored under `figures/`.

Figure export must consume frozen results or frozen computational objects.
It must not retrain models, repeat model selection, retune hyperparameters,
or alter the inferential evidence reported in the manuscript.

## Integrity

See `SHA256SUMS.txt` for SHA-256 hashes of the public provenance notebooks.
