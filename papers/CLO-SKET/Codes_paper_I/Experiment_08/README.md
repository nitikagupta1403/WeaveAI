# Experiment 08 — Pre-outcome execution gate

This directory implements the fresh-study mathematical design in
`../../PAPER_I_FRESH_STUDY_MATHEMATICAL_DESIGN_LOCK.md`.

The current stage is deliberately limited to preflight validation. It does not load DINOv2, extract dataset embeddings, fit a classifier, or compute a learned-baseline outcome.

## Reproducible learned-baseline preflight

The frozen learned baseline uses:

- DINOv2 model variant: `dinov2_vits14`
- upstream repo: `https://github.com/facebookresearch/dinov2.git`
- pinned commit: `7764ea0f912e53c92e82eb78a2a1631e92725fc8`
- pretrained checkpoint: `dinov2_vits14_pretrain.pth`
- canonical weight SHA-256: `b938bf1bc15cd2ec0feacfe3a1bb553fe8ea9ca46a7e1d8d00217f29aef60cd9`
- frozen output contract: 2300 x 384 float32, no additional normalization beyond the final LayerNorm class token (`x_norm_clstoken`)

Environment requirements (see [requirements-lock.txt](requirements-lock.txt)):

- Python 3.12.13
- NumPy 2.1.3
- Pillow 11.3.0
- scikit-learn 1.6.1
- torch 2.11.0
- torchvision 0.26.0
- pandas 2.2.3

The repo does not bundle weights. Download the exact checkpoint from the authoritative DINOv2 release URL and verify the SHA-256 before any extraction step.

Preflight command:

```bash
python papers/CLO-SKET/Codes_paper_I/Experiment_08/preflight.py \
  --data-root /absolute/path/to/Clo-Sket \
  --row-map papers/CLO-SKET/evidence/Experiment_07/experiment07_row_map.csv \
  --fold-map papers/CLO-SKET/evidence/Experiment_07/experiment07_fold_map.csv \
  --identity-overrides papers/CLO-SKET/Codes_paper_I/Experiment_08/experiment08_identity_overrides.json \
  --dinov2-root /absolute/path/to/dinov2 \
  --weights /absolute/path/to/dinov2_vits14_pretrain.pth \
  --output-root /absolute/path/to/experiment08_preflight
```

This read-only gate checks, before any feature extraction:

- TIFF count and canonical order against the frozen Experiment-08 manifest
- DINOv2 repo commit and cleanliness
- pretrained weight bytes and SHA-256
- Python/package version lock
- preprocessing contract from the provenance lock
- model/output contract (ViT-S/14, class-token output, 384 dimensions, float32)
- frozen provenance hashes

If any gate fails, the preflight exits immediately.

Feature-extraction command (portable, no machine-specific defaults):

```bash
python papers/CLO-SKET/Codes_paper_I/Experiment_08/extract_dinov2_features.py \
  --data-root /absolute/path/to/experiment08_materialized \
  --materialized-manifest /absolute/path/to/experiment08_materialized/experiment08_materialized_images.csv \
  --dinov2-root /absolute/path/to/dinov2 \
  --weights /absolute/path/to/dinov2_vits14_pretrain.pth \
  --output-dir /absolute/path/to/experiment08_dinov2_features
```

Expected frozen L characteristics:

- shape: `(2300, 384)`
- dtype: `float32`
- source: label-blind DINOv2 ViT-S/14 class token (`x_norm_clstoken`)
- no classifier fit and no predictive metric computed as part of extraction

`run_primary_comparison.py` expects the frozen DINO feature matrix and row manifest at either the repository-relative default paths:

- `papers/CLO-SKET/Codes_paper_I/Experiment_08/experiment08_dinov2_vits14_embeddings.npy`
- `papers/CLO-SKET/Codes_paper_I/Experiment_08/experiment08_dinov2_embedding_rows.csv`

or via the environment variables:

- `CLO_SKET_DINO_FEATURE_PATH`
- `CLO_SKET_DINO_ROW_PATH`

Example:

```bash
export CLO_SKET_DINO_FEATURE_PATH=/absolute/path/to/experiment08_dinov2_vits14_embeddings.npy
export CLO_SKET_DINO_ROW_PATH=/absolute/path/to/experiment08_dinov2_embedding_rows.csv

python papers/CLO-SKET/Codes_paper_I/Experiment_08/run_primary_comparison.py
```

This path configuration does not alter the frozen feature bytes, model, folds, or estimator.

Run from the repository root:

```bash
python papers/CLO-SKET/Codes_paper_I/Experiment_08/preflight.py \
  --data-root /absolute/path/to/Clo-Sket \
  --output-root /absolute/path/to/experiment08_preflight
```

The preflight:

- validates the public authoritative row and fold maps;
- checks the 2,300-row, 23-category, 230-identity design;
- confirms zero train/test identity overlap;
- enumerates source TIFF files deterministically;
- requires a one-to-one join to the authoritative row map;
- runs analytic axial-angle and rotation-convention tests;
- writes a non-outcome JSON report and source manifest;
- terminates before any learned feature or classifier can be computed.

Feature extraction remains blocked until the exact DINOv2 source commit, downloaded weight hash, and resolved environment lock are recorded.

After preflight, run the preprocessing-only audit:

```bash
python papers/CLO-SKET/Codes_paper_I/Experiment_08/preprocess_audit.py \
  --data-root /absolute/path/to/Clo-Sket \
  --source-manifest /absolute/path/to/experiment08_source_manifest.csv \
  --output-root /absolute/path/to/experiment08_preprocessing_audit
```

This verifies one prespecified image per garment identity and creates a 23-category contact sheet. The script deliberately contains no DINOv2 import or classifier code.

If peripheral writing or other annotation is visible, compare the frozen label-blind masking candidates before feature extraction:

```bash
python papers/CLO-SKET/Codes_paper_I/Experiment_08/annotation_mask_audit.py \
  --data-root /absolute/path/to/Clo-Sket \
  --source-manifest /absolute/path/to/experiment08_source_manifest.csv \
  --output-root /absolute/path/to/experiment08_annotation_mask_audit
```

The audit preserves the rejected single-component 10% candidate and the intermediate multi-component 10% rectangular envelope. It also evaluates a stricter component-only geometry mask: retain the frozen structural garment components and disconnected components wholly enclosed by their unexpanded union, while whitening every exterior component. This avoids retaining nearby writing merely because it falls inside a rectangular context margin. The rule is label-blind and uses no OCR. Selection is based only on preserving garment geometry and removing peripheral annotation; no learned feature or outcome is available at this stage.

Do not approve a mask from retained-ink summaries alone. Inspect the category sheet and the lowest-retention identities. Component-connected handwriting cannot be separated by this rule and must be disclosed and tested through raw-versus-geometry sensitivity analyses.


## Frozen coarse-localization review

Before feature extraction, generate the dataset-wide box proposals, freeze the
review cohort, and complete the dual-box review. The frozen design reviews all
628 proposals with retained ink below 0.98 or an image-boundary contact, plus a
deterministic category-stratified quality-control sample of 300 apparently safe
proposals. A material failure is garment truncation, structural-detail loss, or
interfering annotation; a coordinate-only padding change is not a material
failure. The quality-control sample contained zero material failures and five
non-material padding changes, giving the prespecified rule-of-three approximate
95% upper bound of 1% for material failure in the automatic remainder.

The 928 reviewed records contain 593 handwriting boxes. All 22 geometric
garment/text-box overlaps were flagged and approved by before/after visual
inspection. These annotations are preprocessing metadata, not training targets.

After the review audit passes, freeze the complete 2,300-row localization
manifest:

```bash
python papers/CLO-SKET/Codes_paper_I/Experiment_08/freeze_preprocessing_manifest.py \
  --source-manifest /absolute/path/to/experiment08_source_manifest.csv \
  --proposal-csv /absolute/path/to/experiment08_box_proposals.csv \
  --selection-csv /absolute/path/to/experiment08_box_review_selection.csv \
  --annotations-jsonl /absolute/path/to/review_annotations.jsonl \
  --audit-csv /absolute/path/to/dual_box_pilot_audit.csv \
  --output-root /absolute/path/to/experiment08_preprocessing_freeze
```

The command verifies every frozen evidence hash and terminates before loading
DINOv2 or computing a predictive outcome.


Materialize the frozen images only after the manifest freeze succeeds:

```bash
python papers/CLO-SKET/Codes_paper_I/Experiment_08/materialize_preprocessed_images.py \
  --data-root /absolute/path/to/Clo-Sket \
  --preprocessing-manifest /absolute/path/to/experiment08_preprocessing_manifest.csv \
  --output-root /absolute/path/to/experiment08_materialized
```

The materializer applies orientation, polarity normalization, frozen spatial
localization and handwriting blanking, bicubic longest-side resize, and centered
white padding. It writes deterministic 224x224 grayscale PNGs plus per-file and
ordered pixel-array hashes. It imports neither Torch nor DINOv2.
