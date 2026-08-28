# CLO-SKET Paper I
## Experiment 06 Corrective Reanalysis
## Historical M135 Definition Lock

### Status

PRE-OUTCOME IMPLEMENTATION LOCK.

This document freezes the exact historical 135-dimensional morphology comparator used in the CLO-SKET morphology / Experiment-06 lineage.

No predictive outcome is computed by this lock.

## Authoritative implementation

The authoritative executable reconstruction is:

`papers/CLO-SKET/Codes_paper_I/Experiment_08/materialize_morphology.py`

That implementation explicitly identifies its extractor as the exact frozen morphology definition copied from the historical Validation Shield / morphology-discovery lineage.

The historical raw morphology array SHA-256 is:

`66ae04156ee3fbf3f2605f382a16fc41cf19af34b50e59dd43f6c9427d96b2ee`

## Input preprocessing

For each source sketch:

1. open source TIFF;
2. convert to grayscale (`L`);
3. convert to `float32`;
4. divide intensities by `255.0`;
5. define foreground as `array < 0.8`;
6. convert foreground mask to `uint8 * 255`;
7. resize to `64 x 64` using the historical Pillow `.resize((64,64))` call with no newly specified resampling mode;
8. divide resized mask by `255.0`.

No alternative threshold, resampling rule, crop, or morphology definition may be selected after outcome inspection.

## Feature ordering

The 135-dimensional vector is ordered as:

### Dimensions 0–63: horizontal occupancy

For the 64x64 foreground mask:

`horizontal = mask.mean(axis=1)`

### Dimensions 64–127: vertical occupancy

`vertical = mask.mean(axis=0)`

### Dimensions 128–134: seven global descriptors

In exact order:

1. `centroid_x`
2. `centroid_y`
3. `bbox_width`
4. `bbox_height`
5. `aspect_ratio`
6. `symmetry`
7. `foreground_fraction`

Definitions follow.

### centroid_x

Intensity/foreground-weighted x centroid:

`sum(xx * mask) / (sum(mask) + 1e-8)`

then normalized by `64`.

### centroid_y

Intensity/foreground-weighted y centroid:

`sum(yy * mask) / (sum(mask) + 1e-8)`

then normalized by `64`.

### bbox_width

For positive mask pixels:

`(x_max - x_min + 1) / 64`

If no foreground exists: `0.0`.

### bbox_height

For positive mask pixels:

`(y_max - y_min + 1) / 64`

If no foreground exists: `0.0`.

### aspect_ratio

`bbox_width / (bbox_height + 1e-8)`

If no foreground exists: `0.0`.

### symmetry

Horizontal reflection similarity:

`1.0 - mean(abs(mask - fliplr(mask)))`

### foreground_fraction

`mask.mean()`

## Scientific terminology

This representation shall be described as the:

**lower-performing frozen morphology baseline**

when relative performance wording is required.

The comparator consists of:

- 64 horizontal occupancy-profile coordinates;
- 64 vertical occupancy-profile coordinates;
- 7 global morphology descriptors.

It must not be described simply as an “outline morphology” representation.

## Corrective RAW/CLEAN rule

The feature definition above is immutable.

For the corrective Experiment 06:

- RAW applies the exact frozen M135 extractor to the native source-canvas field.
- CLEAN applies the same exact M135 extractor to the already-frozen annotation-controlled clean image field.

The extractor itself must not differ between RAW and CLEAN.

## Governance

This lock was created before any corrected Experiment-06 predictive outcome was computed.

No classifier fitting, prediction, macro-F1, balanced accuracy, bootstrap, permutation, or annotation-sensitivity outcome is introduced by this document.
