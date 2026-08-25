# Experiment 08 — Pre-outcome execution gate

This directory implements the fresh-study mathematical design in
`../../PAPER_I_FRESH_STUDY_MATHEMATICAL_DESIGN_LOCK.md`.

The current stage is deliberately limited to preflight validation. It does not load DINOv2, extract dataset embeddings, fit a classifier, or compute a learned-baseline outcome.

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
