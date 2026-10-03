# P2-R0-05K4-D3 — Manuscript-Safe Synthesis

## Status

**Support-dependence audit: CLOSED for the current internal question.**

No additional support-only experiment is required to establish the tested
dependency of the frozen historical raster-relative representation.

This closure does **not** establish external generalization or methodological
novelty.

---

## Core manuscript-safe synthesis

Preprocessing ablation localized the historical high-frequency change primarily to the crop-only transition rather than to text removal or subsequent resize/pad processing. The retained garment pixels and source-coordinate centroid were unchanged by this crop, while garment occupancy relative to the raster changed substantially. Population-level analyses subsequently showed that the magnitude of raster-relative support change was associated with systematic spectral redistribution. To test this dependency directly, raster support was then manipulated while the embedded garment pixels were held fixed. Across the complete 2,300-image dataset, increasing blank support produced the preregistered directional response: low-band allocation increased whereas highmid and high allocation decreased. All 23 category medians agreed with these directions, and exact category-level sign-flip inference remained supported after joint max-T familywise correction. Under the same intervention, the matched object-relative representation was exactly invariant across all 16,100 support conditions. Together, these results demonstrate that raster support is a dependency of the frozen historical raster-relative representation under the tested same-pixel intervention, while also showing that the endpoint response is broad rather than universally monotonic at the individual-image level.

---

## Results-style version

The support audit localized the high-band change to the crop-only transition and identified raster-relative garment extent as the strongest population-level correlate of spectral redistribution. A controlled same-pixel intervention then increased blank raster support without resizing, resampling, or altering the embedded garment pixels. At s=3, 91.5% of images increased in low-band allocation, 89.5% decreased in highmid allocation, and 87.3% decreased in high allocation. All 23 category medians changed in the preregistered direction. Exact category-level sign-flip inference with joint max-T familywise correction supported the low, highmid, and high endpoint effects. In contrast, the matched object-relative representation remained exactly invariant across all 16,100 intervention conditions.

---

## Discussion-style version

These findings indicate that the historical angular spectral allocation is not solely a property of the embedded garment geometry: it also depends on how that geometry is normalized relative to the raster support. The controlled intervention is important because the garment pixels themselves were unchanged; only surrounding blank support was altered. The matched object-relative control removes this specific support dependence under the tested intervention. However, the result should not be interpreted as a universal claim about Fourier descriptors or as evidence that support is the only source of spectral variation. Individual trajectories also remained heterogeneous and frequently non-monotonic.

---

## Supported core conclusion

Under the frozen historical raster-relative coordinate normalization, raster support is a demonstrated dependency of angular spectral allocation in the tested dataset and same-pixel support intervention.

---

## Matched control conclusion

The tested object-relative normalization eliminates this support dependence exactly under the same intervention.

---

## Heterogeneity boundary

The endpoint effect is broad and category-consistent, but individual trajectories are not universally monotonic.

---

## Closure decision

**CLOSED_FOR_CURRENT_SUPPORT_DEPENDENCE_QUESTION**

No additional support-only experiment required:

**True**

---

## Unresolved but non-blocking questions

- Why individual-image trajectories are frequently non-monotonic.
- Which garment-level geometric properties explain intervention response heterogeneity.
- Whether analogous support dependence appears in other datasets or other raster-relative descriptors.
- How the present finding relates to prior methodological literature and whether it contributes novelty.


---

## Literature / novelty status

NOT_ASSESSED_IN_D3. Literature integration and novelty assessment must be performed separately before manuscript novelty claims are written.
