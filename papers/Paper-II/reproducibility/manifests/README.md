# Sample and fold manifests

No exact manifest CSV is committed because the public provenance notebooks do
not contain the complete row-level frozen identity and fold vectors.

When the trusted `CLO_SKET_FINAL_IDENTITY_FIGURES.pkl` archive is available, run:

```bash
python scripts/export_manifests.py \
  --trusted-pickle /path/to/CLO_SKET_FINAL_IDENTITY_FIGURES.pkl \
  --output-dir manifests/generated \
  --i-understand-pickle-risk
```

The exporter requires aligned `garment_identity_ids` and
`cell30m_fold_assignment` arrays, checks the expected 2,300 rows, 230 garment
identities and five folds, verifies that every garment identity occurs in only
one fold, and writes:

- `sample_fold_manifest.csv`; and
- `manifest_summary.json`.

Category and filename columns are included only when aligned arrays with known
keys are present in the trusted package. Missing values are never inferred.
