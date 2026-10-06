# CLO-SKET Paper II — P2_13  
## 05K Support Dependence, Literature Positioning, and Claim Reconciliation

**Status:** DRAFT FOR FREEZE  
**Purpose:** reconcile the completed 05F–05K support-dependence audit with the previously locked Paper-II evidence, literature audit, novelty positioning, and manuscript architecture **without altering frozen numerical evidence or historical computational artifacts**.

---

# 0. Governing principle

This amendment is required because the original Paper-II literature audit and novelty lock were written before the preprocessing-localization and support-dependence sequence was completed.

The earlier claim hierarchy remains valid for the representation-selection contribution:

\[
\boxed{
\text{harmonic-conditioned, evidence-controlled radial representation selection}
}
\]

The 05F–05K sequence adds a separate and more fundamental question:

> **Before interpreting or optimizing the radial-angular spectral representation, is the representation itself sensitive to the raster frame in which an unchanged garment is observed?**

The amendment therefore changes the **hierarchy of manuscript emphasis**, not the frozen numerical evidence.

The new scientific order is:

\[
\boxed{
\text{representation validity}
\rightarrow
\text{representation selection}
\rightarrow
\text{latent interpretation}
}
\]

or, more simply:

\[
\boxed{
\text{measure correctly}
\rightarrow
\text{compress carefully}
\rightarrow
\text{interpret cautiously}
}
\]

---

# 1. Relationship to existing Paper-II governance documents

This document is an **amendment and reconciliation layer**.

It does **not** replace:

- `P2_02_EVIDENCE_LEDGER.md`;
- `P2_03_LITERATURE_NOVELTY_AUDIT.md`;
- `P2_04_NOVELTY_CLAIM_LOCK.md`;
- the frozen reproducibility and provenance artifacts.

The earlier documents established that Paper II must **not** claim novelty for:

- Fourier shape descriptors;
- radial-angular or polar representations;
- Fourier-wavelet combinations;
- DCT/cosine radial bases;
- PCA on Fourier descriptors;
- reconstruction of morphology along PCA axes;
- generic scale, translation, or rotation normalization.

Those boundaries remain in force.

This amendment addresses only the additional question introduced by the 05F–05K audit:

> **whether raster support itself is a demonstrated dependency of the historical raster-relative radial-angular representation under a controlled same-pixel intervention.**

---

# 2. Evidence hierarchy used in this amendment

The Paper-II evidence hierarchy remains unchanged:

- **M — Mathematical / construction evidence**
- **I — Inferential evidence**
- **D — Descriptive evidence**
- **Q — Qualified scientific interpretation**

For the support-dependence sequence, one further distinction is essential:

- **A — Associational evidence**  
  observed covariation without controlled manipulation;

- **C — Controlled intervention evidence**  
  evidence from a prespecified intervention in which the target factor is manipulated while designated controls are held fixed.

This distinction is local to the reasoning in P2_13 and does not revise the frozen evidence-ledger taxonomy.

The critical boundary is:

\[
\boxed{
05J = A
}
\]

whereas

\[
\boxed{
05K = C
}
\]

05J identifies an association between raster-relative support change and spectral redistribution.

05K manipulates raster support while holding the garment pixel patch fixed.

---

# 3. Why the support-dependence audit was necessary

The historical Paper-II representation uses a radial-angular coordinate system defined relative to the raster on which the garment is observed.

The central concern was therefore not simply whether cropping or resizing changes an image.

That is already well established.

The specific concern was:

> **Can the same garment content be assigned different angular spectral allocation solely because the surrounding raster support changes?**

This question is narrower than generic scale invariance, image cropping, image resizing, zero-padding, or Fourier-window theory.

It concerns the **measurement coordinate system** itself.

The conceptual distinction is:

\[
\text{object change}
\neq
\text{observation-frame change}
\]

and the 05K intervention was designed to isolate the latter.

---

# 4. The 05F–05K evidence chain

## 4.1 05F — localization of the historical preprocessing effect

The 05F audit decomposed the historical RAW→CLEAN transformation into more specific interventions.

The key conclusion was:

- text removal did **not** explain the population-level high-band collapse;
- the major change entered with **crop-only** processing;
- the later resize/pad stage contributed little additional high-band change;
- the earlier working suspicion that bicubic resampling was the dominant cause was therefore falsified.

For the high band:

\[
\Delta_{\text{TEXT\_ONLY}-\text{RAW}}
= +0.0054165112
\]

\[
\Delta_{\text{CROP\_ONLY}-\text{RAW}}
= -0.0391425304
\]

\[
\Delta_{\text{LOCALIZE\_ONLY}-\text{CROP\_ONLY}}
= -0.0001572699
\]

\[
\Delta_{\text{CLEAN}-\text{LOCALIZE\_ONLY}}
= -0.0001045733
\]

The scientifically permitted conclusion is:

> **Most of the historical high-band change enters with cropping/new raster support rather than with the subsequent resize/pad step.**

The scientifically prohibited conclusion is:

> “Bicubic interpolation caused the historical high-band collapse.”

That hypothesis was not supported.

### Evidence status

\[
\boxed{
\text{05F = localization evidence}
}
\]

It identifies where the effect enters the preprocessing chain.

It does not yet establish why.

---

## 4.2 05G — candidate descriptor audit

05G tested candidate explanations for the RAW→CROP change.

Verified facts included:

- exact equality of the raw garment rectangle and crop array;
- zero centroid map-back error;
- unchanged retained pixel intensities.

Descriptive changes included:

- median crop area fraction: approximately \(0.2559\);
- median raw foreground fraction: approximately \(0.02293\);
- median crop foreground fraction: approximately \(0.09448\);
- median radius/grid ratio: approximately \(0.92886 \rightarrow 0.92238\);
- mean gradient concentration increased;
- border-gradient fraction increased substantially.

The strongest surviving category-centered FDR associations were linked to change in foreground radius relative to raster support.

For example:

\[
\rho(
\Delta \text{foreground-radius/grid-radius},
\Delta \text{high fraction}
)
\approx 0.269
\]

and

\[
\rho(
\Delta \text{foreground-radius/grid-radius},
\Delta \log \text{high energy}
)
\approx 0.290.
\]

The correct interpretation is:

> **The instability was associated more strongly with radial scale relative to raster support than with centroid displacement, interpolation, or border-gradient concentration alone.**

The incorrect interpretation is:

> “Foreground-radius change was proven to be the mechanism.”

05G remained associational.

---

## 4.3 05J — population support–spectral audit

05J expanded the support analysis to the full population and used category-preserving permutation inference with BH-FDR correction.

The strongest descriptor was:

\[
\Delta q_{99}\text{ radius-to-grid ratio}.
\]

Representative associations were:

\[
\Delta\text{low}: \rho=-0.332738
\]

\[
\Delta\text{mid}: \rho=-0.155208
\]

\[
\Delta\text{high-mid}: \rho=+0.345008
\]

\[
\Delta\text{high}: \rho=+0.257411
\]

with FDR-surviving results.

The broad pattern was:

\[
\boxed{
\text{crop-induced raster-relative tightening}
\Rightarrow
\text{low/mid decrease and high-mid/high increase}
}
\]

All 23 category medians showed positive high-band change descriptively.

However, the largest absolute association was only moderate.

Therefore:

\[
\boxed{
\text{support geometry is associated with the spectral shift}
}
\]

but:

\[
\boxed{
\text{support geometry is not a complete deterministic explanation}
}
\]

### Evidence status

\[
\boxed{
05J = \text{population-level association}
}
\]

The manuscript must preserve:

\[
\boxed{
\text{association} \neq \text{causation}
}
\]

for 05J.

---

# 5. 05K — controlled same-pixel support intervention

## 5.1 Primary causal question

05K asked:

> **If garment pixels are kept fixed while only the surrounding raster support is enlarged, does the historical raster-relative representation systematically redistribute angular spectral allocation?**

This is the central controlled question.

---

## 5.2 Intervention definition

Support enlargement levels were:

\[
s \in
\{1.00,1.10,1.25,1.50,2.00,2.50,3.00\}.
\]

For an original raster of size \(H\times W\), the enlarged dimensions were frozen as:

\[
H_s
=
H
+
2\left\lceil
\frac{(s-1)H}{2}
\right\rceil
\]

\[
W_s
=
W
+
2\left\lceil
\frac{(s-1)W}{2}
\right\rceil.
\]

The original rectangle was embedded using symmetric integer padding.

The intervention explicitly prohibited:

- resizing the garment;
- interpolation;
- antialiasing;
- contour retracing;
- crop recomputation;
- rethresholding;
- square forcing;
- post-padding resize.

The entire frozen crop rectangle, including existing border marks or stray pixels, was copied unchanged.

Thus the treatment was:

\[
\boxed{
\text{raster support}
}
\]

not garment geometry.

---

## 5.3 Prespecified directional predictions

Before the primary full-population analysis, the endpoint predictions were frozen:

as support enlargement increases,

\[
\Delta\text{low}>0
\]

\[
\Delta\text{high-mid}<0
\]

\[
\Delta\text{high}<0
\]

with no directional primary claim for the mid band.

A graded increase in bandwise \(L_1\) redistribution was also predicted.

These predictions are important because they prevent interpreting the endpoint pattern only after observing it.

---

## 5.4 Hierarchical execution

The 05K execution hierarchy was:

\[
\text{10 sentinels}
\rightarrow
\text{230 calibration sketches}
\rightarrow
\text{2300-sketch primary population}.
\]

The sentinel set was used for QA/visualization rather than inference.

The calibration set was deterministic: one canonical sketch per identity.

The full primary population contained:

\[
2300 \times 7 = 16100
\]

support conditions.

---

## 5.5 Pixel-preservation and intrinsic-control checks

The full support materialization passed the same-pixel construction checks.

For the object-relative comparator:

\[
\boxed{
16100/16100
}
\]

conditions were exactly invariant within numerical precision.

The \(s=1\) replay reproduced the baseline for:

\[
\boxed{
2300/2300
}
\]

sketches with maximum discrepancy approximately

\[
2.22\times10^{-16}.
\]

This establishes that the intervention machinery itself did not introduce an unintended baseline perturbation.

---

# 6. 05K primary population results

## 6.1 Population median trajectories

Population median band-fraction changes relative to \(s=1\) were:

| support level \(s\) | low | mid | high-mid | high | bandwise \(L_1\) |
|---:|---:|---:|---:|---:|---:|
| 1.00 | 0 | 0 | 0 | 0 | 0 |
| 1.10 | +0.014163 | +0.004217 | -0.008783 | -0.011837 | 0.045464 |
| 1.25 | +0.024044 | +0.004795 | -0.013892 | -0.020213 | 0.072890 |
| 1.50 | +0.031578 | +0.006666 | -0.017996 | -0.027958 | 0.099140 |
| 2.00 | +0.041836 | +0.011776 | -0.023574 | -0.038519 | 0.132808 |
| 2.50 | +0.051059 | +0.014783 | -0.029119 | -0.046172 | 0.157245 |
| 3.00 | +0.060047 | +0.016530 | -0.034858 | -0.052944 | 0.179920 |

The broad endpoint pattern is therefore:

\[
\boxed{
\text{support enlargement}
\Rightarrow
\text{low increase}
}
\]

\[
\boxed{
\text{support enlargement}
\Rightarrow
\text{high-mid decrease}
}
\]

\[
\boxed{
\text{support enlargement}
\Rightarrow
\text{high decrease}
}
\]

This is directionally opposite to the natural RAW→CROP tightening pattern observed in 05J.

---

## 6.2 Image-level endpoint concordance

At \(s=3\) versus \(s=1\):

- low direction concordance:

\[
2104/2300
=
91.5\%
\]

- high-mid direction concordance:

\[
2059/2300
=
89.5\%
\]

- high direction concordance:

\[
2008/2300
=
87.3\%.
\]

This demonstrates a broad response but not a universal one.

---

## 6.3 Category-level breadth

All:

\[
\boxed{
23/23
}
\]

category medians followed the predicted endpoint direction for:

- low;
- high-mid;
- high.

This supports broad category-level consistency.

It does not establish that every image is monotonic or that every garment responds identically.

---

## 6.4 Full-trajectory monotonicity

Across all seven support levels, full monotonicity was not universal:

- low monotonic:

\[
1171/2300
=
50.9\%
\]

- high-mid monotonic:

\[
1015/2300
=
44.1\%
\]

- high monotonic:

\[
869/2300
=
37.8\%
\]

- \(L_1\) monotonic:

\[
1296/2300
=
56.3\%.
\]

Therefore the manuscript must distinguish:

\[
\boxed{
\text{broad endpoint direction}
}
\]

from:

\[
\boxed{
\text{universal per-image monotonic law}
}
\]

The latter is not supported.

---

## 6.5 Exact category-level inference

Primary endpoint inference used:

- 23 category effects;
- \(s=3\) versus \(s=1\);
- exact joint sign-flip enumeration over all

\[
2^{23}
\]

sign configurations;
- common sign flips across the three directional bands;
- studentized max-\(T\) FWER control.

Results:

### Low band

Median category effect:

\[
+0.052497
\]

Mean category effect:

\[
+0.070816
\]

\[
T=8.876063
\]

Raw exact probability:

\[
1.192093\times10^{-7}
\]

Max-\(T\) FWER:

\[
1.430511\times10^{-6}.
\]

### High-mid band

Median category effect:

\[
-0.035074
\]

Mean category effect:

\[
-0.037901
\]

\[
T=11.942573
\]

Raw and max-\(T\) FWER probabilities reached the exact enumeration floor:

\[
1.192093\times10^{-7}.
\]

### High band

Median category effect:

\[
-0.046223
\]

Mean category effect:

\[
-0.053174
\]

\[
T=15.210773
\]

Raw and max-\(T\) FWER probabilities reached:

\[
1.192093\times10^{-7}.
\]

The controlled population inference therefore supports the prespecified endpoint directions.

---

# 7. What 05K establishes

The strongest manuscript-safe statement is:

> **Under the frozen historical raster-relative coordinate normalization, raster support is a demonstrated dependency of angular spectral allocation in the tested garment-sketch population.**

The matched object-relative construction provides the corresponding control:

> **Under the same support intervention and identical garment pixels, the matched object-relative representation remained numerically invariant.**

Together:

\[
\boxed{
\text{historical raster-relative allocation}
\text{ is support-dependent}
}
\]

whereas

\[
\boxed{
\text{matched object-relative allocation}
\text{ removes this tested support dependency}
}
\]

under the controlled same-pixel intervention.

---

# 8. What 05K does not establish

05K does not establish that:

1. raster support explains every historical RAW→CROP difference;
2. every image changes monotonically with support;
3. the object-relative representation is universally superior for every downstream task;
4. the historical raster-relative representation is invalid for all uses;
5. all Fourier descriptors are support-dependent in the same way;
6. all crop effects are caused by coordinate normalization;
7. high-frequency allocation is always artifact;
8. low-frequency allocation is always intrinsic garment structure;
9. the object-relative construction is a novel normalization method;
10. same-pixel support sensitivity is absent from all prior literature.

The allowed conclusion is narrower:

\[
\boxed{
\text{05K demonstrates one controlled representation dependency}
}
\]

not a complete causal theory of preprocessing.

---

# 9. Relationship between 05J and 05K

The strength of the Paper-II support story is not 05K in isolation.

It is the convergence of:

\[
\boxed{
05J + 05K
}
\]

05J observed that natural crop-induced changes in raster-relative extent were associated with a shift:

\[
\text{low/mid}\downarrow
\quad
\text{and}
\quad
\text{high-mid/high}\uparrow.
\]

05K then imposed the inverse support manipulation while keeping garment pixels fixed:

\[
\text{support enlargement}
\]

and observed the inverse endpoint pattern:

\[
\text{low}\uparrow
\]

\[
\text{high-mid/high}\downarrow.
\]

This directional opposition strengthens the interpretation that raster support is not merely correlated with the historical effect by accident.

However, it still does not justify:

> “support accounts for the full RAW→CROP phenomenon.”

The appropriate synthesis is:

> **The observational population audit and controlled support intervention converge on raster-relative support as a genuine dependency of the historical representation, while leaving additional contributors to the natural RAW→CROP effect unresolved.**

---

# 10. Literature precedent framework

The literature is classified using four levels.

## DIRECT PRECEDENT

A study qualifies only if it substantially matches the 05K intervention:

- foreground/object pixels held fixed;
- surrounding 2-D raster support changed independently;
- no resizing/interpolation required for the intervention;
- spectral/descriptor allocation recomputed;
- support dependence quantified;
- preferably contrasted against an intrinsic/object-relative control.

## PARTIAL / CLOSE PRECEDENT

The work addresses closely related shape normalization, polar spectral representation, digital invariance, or support sensitivity, but does not isolate the same 05K intervention.

## GENERAL THEORY

The work establishes broader mathematics of Fourier analysis, finite windows, scaling, or invariant shape representation without reproducing the specific experiment.

## DIFFERENT / TERMINOLOGICAL NEAR-MISS

The work uses similar terminology such as “padding,” “cropping,” or “scale,” but changes a mathematically different object.

---

# 11. 05K precedent matrix

| Source / family | Representation | Object geometry fixed? | Object pixels fixed? | 2-D raster support independently manipulated? | Resize / resampling involved? | Spectral effect measured? | Classification | Implication for Paper II |
|---|---|---:|---:|---:|---:|---:|---|---|
| Classical Fourier descriptors (Zahn & Roskies; Persoon & Fu; Kuhl & Giardina) | contour / boundary Fourier coefficients | not the 05K question | generally not | no isolated 2-D support intervention | varies | yes, descriptor behavior | GENERAL THEORY | Fourier shape analysis and normalization are prior art |
| MPEG-7 contour / region shape, including ART | contour and region descriptors; angular-radial basis | geometric invariance tested | no same-pixel support-only design located | no | digital scaling/rotation tests involve rerasterization | descriptor robustness measured | PARTIAL / CLOSE | scale/rotation robustness and angular-radial shape description are established |
| Zhang & Lu (2002), Generic Fourier Descriptor | 2-D Fourier transform of polar-raster sampled shape | shape is normalized for descriptor construction | not as 05K | no isolated support-only manipulation | polar sampling / normalization | yes | CLOSE PARTIAL | polar-raster Fourier shape representation is not novel |
| Region-based shape normalization / invariant moments | region pixels in normalized coordinate systems | intended after normalization | not as 05K | no | often normalization/resampling | yes | PARTIAL | object-centred/scale-normalized region description is established |
| Yang & Fang (2010), Zernike normalization accuracy | Zernike moment normalization | transformed object compared | no | no | digital discretization and noise affect normalization | yes | PARTIAL / DIGITAL-INVARIANCE CAVEAT | mathematically intended invariance can be imperfect in digital implementation |
| Wu et al. (2026), complete EFD normalization | elliptic Fourier descriptors of contours | canonicalized under basic contour transformations | no | no | contour normalization | yes | MODERN PARTIAL | normalization under translation, scale, rotation, reversal, starting point and symmetry is active prior art; not 05K |
| Harris (1978), DFT windowing | finite-window signal spectral analysis | not a shape-object intervention | not applicable | finite observation support is central | no garment/image intervention | yes | GENERAL THEORY | finite support/window effects in Fourier analysis are old; Paper II must not claim generic support sensitivity as new |
| Kunttu et al. (2005), Fourier descriptor zero-padding | 1-D boundary function padded to increase spectral sampling resolution | boundary signal unchanged in samples but sequence length altered | not equivalent to 2-D raster patch identity | no 2-D support manipulation | zero-padding of 1-D boundary signal | yes | DIFFERENT / TERMINOLOGICAL NEAR-MISS | must not conflate ordinary Fourier zero-padding with 05K raster-support intervention |
| Dzanic, Shah & Witherden (2020) | Fourier properties of images under preprocessing / corruption | no | no | not isolated as same-pixel support intervention | cropping/resolution/compression modify image data | yes | PARTIAL / DIFFERENT | image preprocessing can alter spectra; not the same intervention |
| Van Hoorick & Vondrick (2021), *Dissecting Image Crops* | image-distribution effects of cropping | no | no | cropping changes observed content/context | yes, crop operation | not a radial-angular band audit | PARTIAL / DIFFERENT | cropping leaves detectable effects, but does not isolate fixed-object support dependence |
| Fashion-sketch Fourier/wavelet descriptor work already documented in P2_03 | predetermined fashion shape descriptors | not the 05K question | no | no | varies | descriptor/classification effects | DIFFERENT | fashion-domain use of Fourier/wavelet descriptors is prior art; 05K novelty cannot rest on domain transfer |
| 05K | historical raster-relative radial-angular field + matched object-relative field | **yes** | **yes** | **yes** | **no** | **yes, predefined angular bands** | CURRENT STUDY | controlled support-dependence audit |

---

# 12. Literature conclusion

The literature strongly establishes that the following are prior art:

- Fourier shape analysis;
- contour and region Fourier descriptors;
- polar-raster Fourier description;
- radial-angular shape bases;
- object centering;
- scale normalization;
- translation normalization;
- rotation normalization;
- digital invariance testing;
- Fourier window/support theory;
- zero-padding in ordinary spectral analysis;
- cropping and preprocessing effects on image spectra.

Therefore Paper II must **not** claim novelty for any of these individually.

The literature review did **not** identify, among the reviewed sources, a direct precedent that combines all of the following:

\[
\boxed{
\begin{array}{c}
\text{bit-identical garment pixels}\\
+\\
\text{independent 2-D raster-support manipulation}\\
+\\
\text{no resize/interpolation}\\
+\\
\text{prespecified support dose}\\
+\\
\text{bandwise spectral redistribution}\\
+\\
\text{population-level inference}\\
+\\
\text{matched object-relative invariance control}
\end{array}
}
\]

This is a literature-search conclusion, not proof of absolute priority.

Therefore manuscript wording must use:

> **“We did not identify a direct precedent in the reviewed literature…”**

rather than:

> “No previous work has done this.”

---

# 13. The zero-padding boundary

The phrase “padding” is potentially misleading and should be controlled carefully.

Ordinary Fourier zero-padding generally means appending zeros to a 1-D or 2-D signal before evaluating its DFT, commonly to sample the underlying spectral response more densely.

05K is not presented as a generic zero-padding discovery.

In 05K, the central issue is that the historical radial-angular representation defines object coordinates **relative to raster support**.

Changing raster dimensions therefore changes the mapping:

\[
\frac{r_{\text{object}}}{r_{\text{grid}}}
\]

even though the embedded garment patch itself is unchanged.

The safe description is:

> **support enlargement changes the raster-relative coordinate mapping on which the historical radial-angular field is constructed.**

Avoid:

> “Padding creates low-frequency information.”

Avoid:

> “Zero-padding changes the true Fourier content of the garment.”

Those formulations are too broad and invite an incorrect DSP interpretation.

---

# 14. Reconciled Paper-II contribution hierarchy

## 14.1 Primary scientific / measurement-validity contribution

> **A controlled representation audit demonstrating that raster support alone can systematically redistribute angular spectral allocation in a raster-relative garment-morphology representation even when garment pixels are unchanged.**

This is now the strongest **measurement-validity** contribution.

---

## 14.2 Matched control / counterfactual result

> **Under the same support intervention, a matched object-relative construction remains numerically invariant.**

This is not claimed as a new normalization method.

Its role is to show that the tested dependency is not inevitable once the coordinate system is defined relative to the object rather than the raster frame.

---

## 14.3 Primary representation-selection contribution

The previously locked representation-selection contribution remains:

> **An evidence-controlled radial-spectral strategy in which radial encoding is selected separately across angular harmonic bands using identity-disjoint, multiplicity-controlled validation, compressing supported bands while preserving full radial structure where compression is not supported.**

This remains the strongest **representation-design / inferential-selection** contribution.

---

## 14.4 Secondary latent-interpretation contribution

The secondary methodological contribution remains:

\[
\Delta x_j
\rightarrow
\Delta F_j(r,k)
\rightarrow
|\Delta F_j(r,k)|^2.
\]

Safe wording:

> **Retained PCA perturbations are mapped through the exact frozen inverse hybrid representation to localize latent variation in radial-harmonic coordinates.**

---

# 15. Revised central research questions

The manuscript should now be understood as answering two ordered questions.

## RQ-A — Representation validity

> **When garment morphology is encoded in raster-relative radial-angular spectral coordinates, does changing only the surrounding raster support alter angular spectral allocation even when garment pixels are unchanged?**

Answer:

\[
\boxed{
\text{yes, under the tested historical representation}
}
\]

with matched object-relative invariance under the same intervention.

## RQ-B — Representation allocation

> **Given the radial-angular Fourier field, should radial representation be imposed uniformly across angular harmonic orders, or selected conditionally on harmonic scale using held-out inferential evidence?**

Answer:

\[
\boxed{
\text{uniform radial compression was not supported}
}
\]

and the frozen heterogeneous representation remains:

\[
\mathrm{DCT}_4
/
\mathrm{RAW}_{72}
/
\mathrm{RAW}_{72}
/
\mathrm{db4}_4.
\]

The ordering is important:

\[
\boxed{
RQ\text{-A before }RQ\text{-B}
}
\]

because a representation should be audited before its internal evidence is interpreted or compressed.

---

# 16. Exact manuscript-safe claim amendments

## 16.1 Abstract

### Add

> **A controlled same-pixel audit showed that the historical raster-relative coordinate system was sensitive to surrounding raster support: enlarging blank support alone shifted allocation toward lower angular bands and away from high-middle/high bands, whereas a matched object-relative construction remained invariant.**

### Keep

The evidence-controlled heterogeneous radial representation contribution.

### Avoid

- “new invariant descriptor”;
- “first support-invariant Fourier representation”;
- “support explains all preprocessing instability.”

---

## 16.2 Introduction

### New framing sentence

> **Explicit spectral representations are interpretable only to the extent that their coordinates reflect object structure rather than incidental observation-frame geometry.**

### New gap

> **Prior shape-analysis literature provides extensive Fourier, polar, radial-angular, and normalized descriptors, but the reviewed literature did not identify a direct same-pixel audit that isolates surrounding 2-D raster support as an independent intervention and measures the resulting redistribution across predefined angular spectral bands.**

### Research order

1. audit representation sensitivity to raster support;
2. determine whether radial representation requirements differ across angular harmonic scale;
3. map retained latent variation back to radial-harmonic coordinates.

---

## 16.3 Related Work

Create a dedicated subsection:

### Raster support, digital invariance, and shape normalization

This subsection should distinguish four literatures:

1. classical Fourier / EFD normalization;
2. polar-raster and angular-radial shape descriptors;
3. digital invariance limitations and discretization;
4. finite-window, crop, and padding effects.

End with:

> **These literatures establish that normalization and finite support matter, but they do not by themselves answer the present controlled question: whether changing only blank raster support around a bit-identical garment patch systematically reassigns evidence across the frozen radial-angular spectral bands.**

---

## 16.4 Methods

Add a separate subsection before representation-selection inference:

### Controlled raster-support audit

It must state:

- support levels;
- exact integer-padding rule;
- same-pixel requirement;
- prohibition of resize/interpolation;
- prespecified directional predictions;
- sentinel → calibration → primary hierarchy;
- exact intrinsic-invariance check;
- category-level exact sign-flip max-\(T\) inference.

Avoid describing the support audit as an exploratory afterthought.

---

## 16.5 Results

Use a distinct sequence:

1. preprocessing localization (05F);
2. candidate support descriptors (05G);
3. population association (05J);
4. controlled intervention (05K);
5. representation-selection results;
6. latent interpretation.

The controlled result should appear before any broad interpretation of the spectral bands.

---

## 16.6 Discussion

Use the sentence:

> **The principal implication of 05K is not that Fourier analysis is intrinsically unstable to padding, but that the historical coordinate normalization couples the garment’s apparent radial scale to the raster frame, allowing an observation-frame change to alter angular spectral allocation even when garment pixels are unchanged.**

Then explicitly qualify:

> **This establishes raster support as a genuine dependency of the historical representation, not as a complete explanation of every natural RAW→CROP difference.**

---

## 16.7 Limitations

Add:

- one dataset / one historical representation family;
- support-only intervention does not reproduce every effect of real cropping;
- per-image trajectories are not universally monotonic;
- object-relative invariance is exact for the tested construction but does not establish universal downstream superiority;
- literature review did not establish absolute priority;
- generalization to other Fourier/polar descriptors remains untested.

---

## 16.8 Conclusion

Preferred ending:

> **The study therefore separates two questions that are often conflated: whether a spectral representation is stable to the coordinate frame in which the object is observed, and how representation complexity should be allocated once that measurement system is understood.**

---

# 17. Prohibited manuscript claims

The following wording is prohibited unless new evidence is obtained.

1. “We introduce scale normalization.”
2. “We introduce object-centred Fourier representation.”
3. “We introduce the first radial-angular Fourier garment descriptor.”
4. “No prior study has investigated support dependence.”
5. “Padding creates low-frequency garment information.”
6. “Cropping caused the high-frequency collapse because of interpolation.”
7. “Raster support is the complete mechanism of RAW→CROP instability.”
8. “The historical representation is invalid.”
9. “The object-relative representation is universally superior.”
10. “All images respond monotonically to support.”
11. “High-frequency evidence is artifact.”
12. “Low-frequency evidence is intrinsic garment structure.”
13. “05K proves all Fourier descriptors are support-dependent.”
14. “The support audit establishes semantic meaning for individual harmonic bands.”
15. “The same-pixel intervention proves all crop effects are coordinate effects.”

---

# 18. Preferred manuscript language

Use:

- “demonstrated dependency”;
- “controlled same-pixel intervention”;
- “raster-relative support”;
- “matched object-relative control”;
- “broad category-consistent endpoint response”;
- “not universally monotonic at the individual-image level”;
- “association in 05J; controlled intervention in 05K”;
- “did not identify a direct precedent in the reviewed literature”;
- “does not establish complete causal explanation”;
- “representation validity precedes representation optimization.”

Avoid:

- “mechanism” without qualification;
- “causal explanation of cropping”;
- “invariance breakthrough”;
- “novel Fourier mathematics”;
- “support-invariant descriptor invention.”

---

# 19. Manuscript architecture amendment

The recommended final scientific order is:

## 1. Representation definition

\[
P(\theta\mid r)
\rightarrow
F_k(r)
\]

## 2. Representation validity audit

\[
05F
\rightarrow
05G
\rightarrow
05J
\rightarrow
05K
\]

## 3. Harmonic-conditioned radial representation selection

\[
\mathrm{DCT}_4
/
\mathrm{RAW}_{72}
/
\mathrm{RAW}_{72}
/
\mathrm{db4}_4
\]

## 4. Frozen hybrid representation

## 5. Latent-model validation

## 6. Exact latent-to-radial-harmonic interpretation

## 7. Scientific synthesis and limitations

This order should replace any architecture in which 05K is treated merely as a late robustness appendix.

---

# 20. Figure and table consequences

The support-dependence result deserves a primary figure, not only supplementary placement.

A strong main-paper figure would contain:

### Panel A — same-pixel support intervention

Show one garment patch embedded at:

\[
s=1,\ 1.5,\ 2,\ 3.
\]

The object pixels must be visually and numerically identical.

### Panel B — population median trajectories

Show:

- low;
- mid;
- high-mid;
- high

band-fraction changes over support level.

### Panel C — category endpoint effects

Show the 23 category effects for:

\[
s=3 - s=1
\]

for low/high-mid/high.

### Panel D — matched object-relative control

Show zero or numerical-noise-level trajectory under the same support intervention.

The visual message should be:

\[
\boxed{
\text{same garment}
+
\text{different frame}
\Rightarrow
\text{different raster-relative spectral allocation}
}
\]

but:

\[
\boxed{
\text{same garment}
+
\text{different frame}
\Rightarrow
\text{same object-relative allocation}
}
\]

---

# 21. Reproducibility and provenance boundary

The historical provenance notebooks and frozen artifacts must remain untouched.

P2_13 is a manuscript-governance amendment.

It may:

- reorder manuscript emphasis;
- refine claim wording;
- add literature positioning;
- connect already-frozen audits.

It must not:

- rerun historical model selection;
- change selected representations;
- alter frozen inferential outcomes;
- reconstruct or silently rewrite provenance notebooks;
- replace frozen evidence with newly generated results.

Any submission-facing figure-export or portable code should consume frozen results or frozen computational objects.

---

# 22. Reviewer-defense matrix

| Reviewer challenge | Manuscript response |
|---|---|
| “Is this just zero-padding?” | No. The issue is recomputation of a raster-relative radial-angular coordinate field after support enlargement. Ordinary Fourier zero-padding is a different operation. |
| “Scale invariance is old.” | Correct. The paper does not claim new scale normalization. The contribution is the controlled audit of a historical raster-relative representation under same-pixel support manipulation. |
| “Cropping obviously changes images.” | Correct, but 05K removes content removal, resize, interpolation, and rerasterization, isolating support/frame change. |
| “Why not just use GFD/ART/Zernike?” | Those are established normalized shape descriptors and are acknowledged as prior art. Paper II is not claiming descriptor superiority; the matched object-relative construction serves as the direct counterfactual needed for the support question. |
| “Does 05K explain all preprocessing effects?” | No. It demonstrates one genuine dependency and does not exclude other contributors to RAW→CROP differences. |
| “Is the effect universal?” | No. Endpoint direction is broad and category-consistent; individual trajectories are not universally monotonic. |
| “Was the direction selected after looking?” | No. Low↑, high-mid↓, high↓ under support enlargement were frozen before the full primary population analysis. |
| “Is the object-relative method novel?” | No claim of that kind is made. Its role is a matched invariant control. |
| “Why is this relevant to the earlier representation-selection result?” | Because band-specific evidence should be interpreted only after understanding whether band allocation depends on the observation coordinate frame. |
| “Is support dependence a general law of Fourier descriptors?” | No. It is demonstrated for the tested historical representation. |

---

# 23. Final reconciled claim lock

## Claim A — representation validity

**Allowed**

> **Under the tested historical raster-relative radial-angular representation, surrounding raster support is a demonstrated dependency of angular spectral allocation.**

**Not allowed**

> “Raster support determines garment morphology.”

---

## Claim B — controlled intervention

**Allowed**

> **With garment pixels held fixed, parametric support enlargement produced broad, category-consistent redistribution toward lower angular bands and away from high-middle/high bands.**

**Not allowed**

> “Every garment follows a monotonic support law.”

---

## Claim C — matched intrinsic control

**Allowed**

> **The matched object-relative construction remained numerically invariant under the same same-pixel support intervention.**

**Not allowed**

> “The object-relative construction is universally optimal.”

---

## Claim D — relation to natural cropping

**Allowed**

> **The direction of the controlled support response is consistent with the inverse of the natural crop-tightening association observed in 05J, supporting raster support as a genuine dependency of the historical representation.**

**Not allowed**

> “05K fully explains RAW→CROP preprocessing effects.”

---

## Claim E — representation selection

**Allowed**

> **Radial representation requirements differed across angular harmonic scale under identity-disjoint, multiplicity-controlled inference.**

**Not allowed**

> “Radial complexity follows a universal monotonic law with harmonic order.”

---

## Claim F — novelty positioning

**Allowed**

> **The contribution is not a new Fourier transform or normalization scheme. It is a controlled representation audit combined with evidence-controlled allocation of radial representation complexity.**

**Not allowed**

> “First-ever support-invariant Fourier garment descriptor.”

---

# 24. Final scientific identity of Paper II after 05K

Paper II should now be described as a study of:

\[
\boxed{
\textbf{representation validity and evidence-controlled representation allocation}
}
\]

within explicit radial-angular garment morphology.

A manuscript-ready formulation is:

> **Paper II first audits whether angular spectral allocation reflects garment structure or incidental raster framing, using a controlled same-pixel support intervention and a matched object-relative control. It then asks whether radial representation requirements are uniform across angular harmonic scale and uses identity-disjoint, multiplicity-controlled evidence to construct a heterogeneous hybrid representation that compresses only where support is established. Finally, retained latent variation is mapped exactly back into radial-harmonic coordinates for interpretation.**

This formulation preserves all earlier frozen contributions while placing them in the stronger scientific order revealed by the 05F–05K audit.

---

# 25. Closure decision

## Support-dependence question

\[
\boxed{
\texttt{CLOSED\_FOR\_CURRENT\_SUPPORT\_DEPENDENCE\_QUESTION}
}
\]

No additional support-only experiment is required for the present claim.

## Literature boundary

\[
\boxed{
\texttt{NO\_DIRECT\_PRECEDENT\_LOCATED\_IN\_REVIEWED\_LITERATURE}
}
\]

This is not an absolute-priority claim.

## Manuscript implication

\[
\boxed{
\texttt{REPRESENTATION\_VALIDITY\_PRECEDES\_REPRESENTATION\_SELECTION}
}
\]

## Historical artifact policy

\[
\boxed{
\texttt{FROZEN\_ARTIFACTS\_UNTOUCHED}
}
\]

---

# 26. References to integrate in the final manuscript

The support-dependence subsection should include, at minimum, literature from the following categories:

1. classical Fourier shape descriptors and EFD normalization;
2. Generic Fourier Descriptor / polar-raster Fourier shape description;
3. MPEG-7 region-shape / Angular Radial Transform;
4. digital normalization limitations, including Zernike normalization accuracy;
5. finite-window Fourier theory;
6. zero-padding distinction;
7. image-crop distribution / spectral effects;
8. modern EFD normalization, including Wu et al. (2026).

Key references for this amendment include:

- Harris, F. J. (1978). *On the use of windows for harmonic analysis with the discrete Fourier transform*. Proceedings of the IEEE, 66(1), 51–83.
- Zhang, D., & Lu, G. (2002). *Shape-based image retrieval using generic Fourier descriptor*. Signal Processing: Image Communication, 17(10), 825–848.
- Kunttu, I., Kunttu, L., & Visa, A. (2005). *Enhanced Fourier Shape Descriptor Using Zero-Padding*. Scandinavian Conference on Image Analysis.
- Yang, [author as cited in final bibliography] & Fang, [author as cited in final bibliography] (2010). *On the accuracy of image normalization by Zernike moments*. Image and Vision Computing, 28(3), 403–413.
- Van Hoorick, B., & Vondrick, C. (2021). *Dissecting Image Crops*. ICCV, 9741–9750.
- Wu, H., Yang, J.-J., Wu, P., Li, C.-Q., Ran, J.-H., Peng, R.-H., & Wang, X.-Q. (2026). *Complete elliptic Fourier descriptor normalization and its application in quantitative morphological analysis*. Methods in Ecology and Evolution, 17, 2123–2134.

Exact bibliography formatting and any additional citations should be resolved during the `P2_11` related-work revision.

---

# 27. Freeze note

When this document is accepted:

1. preserve this file as the explicit 05K amendment;
2. do not silently rewrite historical `P2_03` or `P2_04`;
3. use this amendment to reconcile the manuscript-facing files;
4. update `P2_08`–`P2_12` only after this claim hierarchy is accepted;
5. keep all historical support-audit, evidence, and provenance artifacts immutable.

---

## FINAL LOCK CANDIDATE

\[
\boxed{
\textbf{
Paper II is not a claim of new Fourier mathematics.
It is a measurement-validity and evidence-allocation study:
first determine whether the representation depends on the observation frame,
then allocate representation complexity only where held-out evidence supports it.
}
}
\]