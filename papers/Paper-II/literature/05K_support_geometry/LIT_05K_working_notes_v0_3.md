# WeaveAI Paper II — 05K Support Geometry Literature
## Working Notes v0_3

### Status
This checkpoint consolidates the literature discussion through **LIT-05K-012**.
It is a **working research ledger**, not a final novelty determination.

Important provenance note: these files were generated from the consolidated WeaveAI master-chat literature state. The local bytes of the user's earlier `v0_2` files were not available in this execution environment, so v0_3 should be compared against the user's local `v0_2` before freezing/committing.

---

## 1. Current Paper II empirical boundary

The strongest current result is **not** a new descriptor claim.

The support-dependence result is:

> Under the frozen historical raster-relative coordinate normalization, raster support is a demonstrated dependency of angular spectral allocation in the tested dataset and controlled same-pixel canvas intervention.

The matched object-relative implementation was exactly invariant under the tested same-pixel, no-resampling support-only intervention.

This does **not** establish:
- universal digital invariance,
- a complete causal explanation of all representation instability,
- novelty of object-centred normalization,
- novelty of polar / radial-angular coordinates,
- novelty of Fourier shape representation,
- superiority over established shape descriptors.

---

## 2. Representation-family map

### A. Raster / spectral
Historical WeaveAI, 05H, GFD, ART, Zernike.

Key distinction:
- **Historical WeaveAI**: raster/grid-relative normalization.
- **05H**: foreground-centred, foreground-radius normalization.
- **GFD**: object-centred polar raster and 2-D Fourier coefficients retaining joint radial × angular frequency structure.
- **ART**: fixed angular-radial basis on normalized region.
- **Zernike**: fixed orthogonal radial-polynomial × angular-harmonic basis on unit disk.

### B. Contour / spectral
Zahn & Roskies, Persoon & Fu, Kuhl & Giardina, Kunttu et al.

These operate primarily on boundary-derived signals rather than the full raster region.

### C. Contour geometry / multiscale
CSS and Turning Function.

These encode geometry directly:
- CSS: persistence of contour inflections / curvature structure across smoothing scale.
- Turning Function: tangent direction as a function of normalized boundary arc length.

### D. Relational point geometry
Shape Context.

Dense sampled points are represented by relative log-polar distributions around each reference point. This is object-relative geometry, but not semantic garment-landmark correspondence.

### E. Semantic / population geometry
Landmarks → GPA → PCA / SSM / ASM.

This is a learned population model over homologous structural points. It is conceptually distinct from a fixed Fourier basis.

### F. Fourier registration
Reddy & Chatterji.

This uses Fourier properties to estimate translation, rotation and scale between images. It is not a support-only descriptor-sensitivity experiment.

---

## 3. Fixed basis vs learned basis

Keep these three layers separate:

1. **Coordinate system**
   - Cartesian `(x,y)`
   - polar `(r, θ)`
   - boundary arc length `s`

2. **Fixed mathematical basis / representation**
   - Fourier
   - ART
   - Zernike
   - CSS / turning functions / shape-context histograms

3. **Learned population basis**
   - PCA
   - SSM / ASM

Polar coordinates are not themselves a descriptor.
Fourier / ART / Zernike are fixed mathematical expansions.
PCA / SSM learn basis directions from data.

---

## 4. GFD ↔ 05H ↔ Historical WeaveAI

### GFD
Conceptually:
`shape → object centroid → object-derived radius → polar raster → 2-D Fourier transform → selected normalized radial × angular coefficients`

### 05H intrinsic
Conceptually:
`foreground → foreground centroid → max foreground radius → radial-angular conditional field → angular Fourier analysis / band summaries`

05H belongs to the same broad object-centred polar/spectral family as GFD but is **not identical**:
- GFD retains a 2-D coefficient grid indexed by radial and angular frequency.
- 05H ultimately studies angular-frequency allocation with radial information aggregated differently.

### Historical WeaveAI
The key distinction is not “Fourier vs non-Fourier”; it is the **reference frame**:
- historical = raster/grid-relative scale normalization,
- 05H = object-relative normalization.

This distinction is the centre of the 05K support audit.

---

## 5. High-priority literature lessons

### Yang & Fang
Core lesson:
**ideal mathematical invariance and digital implementation invariance are not the same thing.**

Digital errors can arise from discretization, centroid estimation, noise, interpolation, and resampling.

Paper II implication:
Do not say 05H is universally invariant. Say it was exactly invariant **under the tested no-resampling, same-pixel support-only intervention**.

Future resize implication:
Canonical resizing is a different experiment because it reintroduces resampling and boundary/centroid effects.

### Kunttu et al.
Important terminology:
**1-D signal-domain zero padding is not 2-D blank-canvas enlargement.**

Kunttu:
`boundary signal → append zeros → FFT → denser frequency sampling / improved descriptor behaviour`

05K:
`same exact 2-D patch → larger blank image canvas → no resampling → recompute representation`

### Reddy & Chatterji
Classical Fourier nuisance-transform handling:
translation, rotation, scale.

This is background theory, not direct 05K precedent.

### CSS
A different shape language:
**which contour bends persist across smoothing scale?**

### Turning Function
A geometrically literal representation:
**as I walk around the boundary, how does tangent direction change?**

---

## 6. Benchmark decision

Do **not** automatically implement every literature method.

Current Paper II claim:
- support dependence of a historical raster-relative formulation,
- matched object-relative contrast.

Therefore:
- a broad benchmark zoo is not required,
- literature can establish prior art without being implemented,
- GFD remains the closest strategic comparator if one is later needed,
- Shape Context / SSM / CSS / turning-function baselines should only be added if a specific reviewer-relevant question requires them.

No benchmark suite is frozen at v0_3.

---

## 7. Current novelty boundary

Established prior art:
- Fourier shape descriptors,
- polar / radial-angular coordinates,
- object-centred normalization,
- object-radius normalization,
- angular-radial region descriptors,
- dense relational point geometry,
- landmark PCA / SSM.

Current empirical contribution:
- controlled evidence that the **historical raster-relative formulation** changes with blank raster support under a same-pixel intervention,
- exact matched object-relative invariance under that tested intervention.

Potential novelty of the **specific experimental audit design** remains **OPEN** pending broader literature review.

---

## 8. Next literature direction

Natural next branch:
- Generalized Procrustes Analysis / landmark alignment foundations,
- then additional sketch / line-drawing / contour / silhouette literature,
- then decide whether one strategic comparator is needed.

Do not freeze a novelty verdict yet.
