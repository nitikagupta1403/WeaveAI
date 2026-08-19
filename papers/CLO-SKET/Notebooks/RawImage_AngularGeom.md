# 🧪 CLO-SKET — RAW IMAGE RADIAL / ANGULAR GEOMETRY
## Stage 2 — Independent Analysis from Raw Sketch Images

**Status:** RAW-DATA EXPERIMENT INITIALIZED

---

# 1. Purpose

The preceding directional experiment derived centroid-referenced angular
morphology from the already-defined 135-D canonical morphology
representation.

The present experiment asks a stronger and more independent question:

\[
\boxed{
\text{Can comparable geometric structure be recovered directly from
the original sketch images?}
}
\]

The analysis therefore begins from the original TIFF images and retains
their grayscale intensity information.

---

# 2. Raw Dataset

The original CLO-SKET source directory contains:

\[
\boxed{2300}
\]

TIFF sketches distributed across:

\[
\boxed{23}
\]

source categories.

The complete source inventory was verified.

No images were added or removed.

---

# 3. Starting Representation

Each sketch begins as its original grayscale intensity field.

Example source image:

\[
224\times224
\]

After grayscale conversion:

\[
I_i(x,y)
\]

where \(I_i(x,y)\) represents the original grayscale intensity at
pixel location \((x,y)\).

The raw experiment therefore begins with:

\[
\boxed{
\text{original TIFF}
\rightarrow
\text{grayscale intensity field}
}
\]

rather than:

\[
\text{image}
\rightarrow
\text{threshold}
\rightarrow
\text{64}\times\text{64 mask}
\rightarrow
\text{occupancy}.
\]

---

# 4. Raw Image Integrity

Test image:

\[
\texttt{A-Line/1-1.tif}
\]

Original spatial resolution:

\[
224\times224
\]

Grayscale representation:

\[
224\times224
\]

Data type:

\[
\text{float32}
\]

Intensity range:

\[
105\le I(x,y)\le255
\]

Mean intensity:

\[
251.10097
\]

All values were finite.

A SHA-256 fingerprint was recorded for the raw test image:

\[
\boxed{
\texttt{cb827e09389c9ae936b1dc2b1e198ab1bcb057ea721d2fbc5509a582b4631906}
}
\]

This provides an integrity reference for the original input.

---

# 5. Explicit Independence from Paper-I

The raw-image experiment does **not** inherit the following objects from
the canonical morphology analysis:

- 135-D morphology coordinates;
- horizontal occupancy;
- vertical occupancy;
- canonical global descriptors;
- PCA coordinates;
- clustering;
- KDE;
- previously derived angular morphology;
- previously derived Fourier coordinates.

Therefore the starting point is:

\[
\boxed{
\text{raw grayscale image}
}
\]

rather than:

\[
\boxed{
\text{predefined morphology representation}.
}
\]

---

# 6. Processing State at Initialization

At initialization, none of the following operations has been performed:

- spatial normalization;
- thresholding;
- binarization;
- 64 × 64 morphology reconstruction;
- occupancy calculation;
- centroid calculation;
- radial sampling;
- angular sampling;
- circular statistics;
- Fourier transformation.

This is important because it establishes a clean experimental boundary
between the predefined-morphology experiment and the raw-image
experiment.

---

# 7. Scientific Logic

The previous experiment established:

\[
\text{canonical morphology}
\rightarrow
\text{angular geometry}
\rightarrow
\text{Fourier structure}
\rightarrow
\text{reproducible correspondence}.
\]

The present experiment tests:

\[
\boxed{
\text{raw image intensity}
\rightarrow
\text{independent geometric representation}
}
\]

If comparable structure subsequently emerges, it would provide evidence
that the observed geometry is not merely an artifact of first defining
the 135-D morphology coordinates.

---

# 8. Critical Design Principle

The raw experiment should preserve as much information from the original
image as possible until the geometric coordinate system has been
defined.

Therefore:

\[
\boxed{
\text{spatial normalization}
\neq
\text{morphology feature extraction}
}
\]

and:

\[
\boxed{
\text{coordinate normalization}
\neq
\text{thresholding}
}
\]

The first operation should establish a common spatial coordinate system
while preserving grayscale intensity.

Only subsequently should intensity-weighted geometric quantities be
computed.

---

# 9. Next Operation

The immediate next step is therefore:

\[
\boxed{
\text{raw grayscale image}
\rightarrow
\text{common spatial coordinate system}
}
\]

followed by calculation of the intensity-weighted centroid:

\[
c_x=
\frac{\sum_{x,y}x\,I(x,y)}
{\sum_{x,y}I(x,y)}
\]

\[
c_y=
\frac{\sum_{x,y}y\,I(x,y)}
{\sum_{x,y}I(x,y)}.
\]

The centroid will then provide the origin for the subsequent
radial–angular analysis.

---

# 10. Experimental Boundary

The raw-image experiment is therefore a separate analytical branch:

\[
\boxed{
\textbf{RAW IMAGE BRANCH}
}
\]

\[
\text{TIFF}
\rightarrow
\text{grayscale intensity}
\rightarrow
\text{spatial normalization}
\rightarrow
\text{centroid}
\rightarrow
\text{radial/angular geometry}
\rightarrow
\text{population analysis}
\]

while the original Paper-I representation remains:

\[
\boxed{
\textbf{FROZEN}
}
\]

No result from this experiment will modify the canonical 135-D
morphology representation.

---

# 11. Current Status

\[
\boxed{
\textbf{RAW IMAGE INVENTORY = VERIFIED}
}
\]

Population:

\[
\boxed{2300}
\]

Categories:

\[
\boxed{23}
\]

Starting representation:

\[
\boxed{\text{original grayscale intensity field}}
\]

Canonical 135-D morphology:

\[
\boxed{\text{NOT USED}}
\]

Thresholding:

\[
\boxed{\text{NOT PERFORMED}}
\]

Centroid:

\[
\boxed{\text{NOT YET CALCULATED}}
\]

Angular geometry:

\[
\boxed{\text{NOT YET CALCULATED}}
\]

Fourier analysis:

\[
\boxed{\text{NOT YET PERFORMED}}
\]

---

# 12. Interpretation Boundary

At this stage there is **no scientific result yet** regarding radial or
angular morphology.

The only established result is that the raw CLO-SKET population has
been correctly inventoried and that the experiment begins from the
original grayscale image representation.

The next cell will determine how the raw intensity field behaves under
a common spatial coordinate system.

\[
\boxed{
\text{RAW IMAGE ANALYSIS — CELL 1 LOCKED}
}
\]

# 🧪 CLO-SKET — RAW IMAGE RADIAL / ANGULAR GEOMETRY
## Stage 2 — Canvas and Source-Geometry Audit

**Status:** FROZEN BEFORE SPATIAL NORMALIZATION

---

# 1. Purpose

Before calculating any intensity-weighted centroid or radial/angular
geometry from the original sketch images, the source-image coordinate
system must be audited.

The raw CLO-SKET images are not all stored at the same spatial
resolution or canvas aspect ratio.

Because radial and angular measurements depend directly on spatial
coordinates, performing geometric analysis in the original pixel
coordinates could introduce artificial directional structure caused by
the image canvas rather than by garment morphology.

The purpose of this audit is therefore:

\[
\boxed{
\text{source-image geometry}
\rightarrow
\text{coordinate-system validation}
}
\]

before any centroid, radial, or angular representation is constructed.

---

# 2. Source Image Dimensions

All 2,300 source TIFF files were scanned exactly once.

Three unique image dimensions were found:

| Width | Height | Number of images |
|---:|---:|---:|
| 224 | 224 | 400 |
| 862 | 1228 | 1898 |
| 1724 | 2457 | 2 |

Therefore:

\[
400+1898+2=2300.
\]

The complete source population is accounted for.

No images were excluded.

---

# 3. Dimension–Category Structure

The image dimensions are strongly associated with source categories.

### Square group

The following categories contain 100 images each at:

\[
224\times224:
\]

- A-Line
- Bermuda
- Blouse
- Wide-Leg

Thus:

\[
4\times100=400.
\]

### Portrait group

The following categories contain 100 images each at:

\[
862\times1228:
\]

- Cardigan
- Circle
- Dress
- Flare
- Harem
- Hoodie
- Jacket
- Jumpsuit
- Mermaid
- Mini
- Sarong
- Shirt
- Skinny
- Straight
- Suit
- Tunic
- Vest

and the remaining 99 images in:

- Pencil
- T-shirt

for a total of:

\[
1898.
\]

### Large portrait images

Two images use:

\[
1724\times2457:
\]

one Pencil image and one T-shirt image.

---

# 4. Representative Source Dimensions

Representative files were inspected for each image-size group.

### Square

\[
224\times224
\]

Example:

```text
A-Line/1-1.tif

# Representative Source-Canvas Geometry

The source-dimension audit is illustrated by representative sketches from
each of the three observed canvas-size groups.

![Representative CLO-SKET source images by canvas size](representative_source_canvas_geometry.png)

The examples demonstrate that the heterogeneous image dimensions are not
merely differences in numerical resolution. The square and portrait
source groups also differ in their spatial canvas geometry.

The representative images show:

\[
224\times224
\]

for the square source group, compared with

\[
862\times1228
\]

and

\[
1724\times2457
\]

for the portrait source groups.

The portrait groups share approximately the same aspect ratio, whereas
the square group has an aspect ratio of 1.0.

Because radial and angular coordinates depend on the underlying spatial
metric, these source canvases cannot be treated as a single isotropic
pixel coordinate system without normalization.

The figure therefore provides a visual complement to the quantitative
canvas audit:

\[
\boxed{
\text{heterogeneous source canvas}
\rightarrow
\text{potential coordinate distortion}
}
\]

No geometric measurements are derived from this figure itself. It is
used only to document the source-image geometry before defining the
common coordinate system.

# 🧪 CLO-SKET — RAW IMAGE RADIAL / ANGULAR GEOMETRY
## CELL 3 — ISOTROPIC PHYSICAL COORDINATE SYSTEM

---

## 1. Objective

Before calculating any centroid, radial coordinate, or angular
measurement from the raw source images, a common spatial coordinate
system must be established.

The objective is to ensure that:

\[
\boxed{
\text{x and y coordinates retain the same physical scale}
}
\]

without:

- independently normalizing the two axes;
- stretching portrait images into square images;
- changing garment aspect ratio;
- rotating sketches;
- straightening sketches.

---

## 2. Coordinate Normalization

For an image with width \(W\) and height \(H\), define

\[
S = \max(W,H).
\]

Image coordinates are centered on the canvas and normalized as

\[
\boxed{
x' = \frac{x-x_c}{S}
}
\]

and

\[
\boxed{
y' = \frac{y-y_c}{S}
}
\]

where

\[
x_c = \frac{W}{2},
\qquad
y_c = \frac{H}{2}.
\]

Because the same scale \(S\) is used for both axes,

\[
\boxed{
\Delta x' \text{ and } \Delta y'
\text{ have the same spatial scale}
}
\]

and radial/angular calculations are therefore performed in an
isotropic coordinate system.

---

## 3. Normalized Canvas Geometry

### 224 × 224

\[
S=224
\]

Normalized x extent:

\[
(-0.49776787,\;0.49776787)
\]

Normalized y extent:

\[
(-0.49776787,\;0.49776787)
\]

Aspect ratio:

\[
1.000000
\]

Therefore the square source format retains its original square geometry.

---

### 862 × 1228

\[
S=1228
\]

Normalized x extent:

\[
(-0.35057002,\;0.35057002)
\]

Normalized y extent:

\[
(-0.49959284,\;0.49959284)
\]

Aspect ratio:

\[
0.7019544
\]

The portrait geometry is therefore preserved.

---

### 1724 × 2457

\[
S=2457
\]

Normalized x extent:

\[
(-0.35063085,\;0.35063085)
\]

Normalized y extent:

\[
(-0.49979650,\;0.49979650)
\]

Aspect ratio:

\[
0.7016687
\]

This format preserves essentially the same portrait geometry as the
862 × 1228 group.

---

## 4. Scale-Equivalence Test

The two portrait source formats have aspect ratios:

\[
r_1 = 0.7019543974
\]

and

\[
r_2 = 0.7016687017.
\]

Their absolute difference is

\[
|r_1-r_2|
=
0.0002856957.
\]

The relative difference is

\[
0.0004070004
\]

or approximately

\[
\boxed{0.0407\%}.
\]

Therefore:

\[
\boxed{
\text{862×1228 and 1724×2457 are accepted as
scale-equivalent portrait formats}
}
\]

The square format is independently verified as:

\[
\boxed{
224\times224 \rightarrow \text{aspect ratio }1.0
}
\]

---

## 5. Important Methodological Decision

The normalization deliberately uses **one common scale factor**

\[
S=\max(W,H)
\]

rather than separate x- and y-axis normalization.

Thus we do NOT perform:

\[
x'=\frac{x-x_c}{W},
\qquad
y'=\frac{y-y_c}{H}
\]

because independent normalization would transform the relative geometry
of portrait sketches.

Instead:

\[
\boxed{
(x,y)
\rightarrow
(x',y')
\quad\text{using one isotropic scale}
}
\]

This preserves the original aspect ratio of each source canvas.

---

## 6. Operations Explicitly NOT Performed

At this stage:

- no image stretching;
- no aspect-ratio correction;
- no rotation;
- no straightening;
- no centroid calculation;
- no radial coordinates;
- no angular profile;
- no circular statistics;
- no Fourier transform.

The source grayscale intensity field remains unchanged apart from its
coordinate interpretation.

---

## 7. Why This Step Is Necessary

Radial and angular morphology depend directly on spatial geometry.

If the source image were independently normalized along its two axes,
the transformation would alter distances and angles:

\[
\boxed{
\text{anisotropic normalization}
\rightarrow
\text{distorted geometry}
\rightarrow
\text{potentially artificial angular structure}
}
\]

The present coordinate system instead provides:

\[
\boxed{
\text{raw source image}
\rightarrow
\text{centered isotropic coordinates}
}
\]

while preserving the original spatial relationships.

---

## 8. Current Experimental State

The raw-image experiment now has:

\[
\boxed{
2300
\text{ original Clo-SKET source images}
}
\]

with:

\[
\boxed{
\text{raw grayscale intensity fields}
}
\]

and a verified common isotropic coordinate system.

No Paper-I representation has been used.

In particular, the experiment has NOT inherited:

- the 64 × 64 morphology masks;
- the 135-D morphology representation;
- occupancy measurements;
- PCA;
- clustering;
- KDE;
- semantic labels.

---

## 9. Scientific Status

### 🟢 ISOTROPIC COORDINATE SYSTEM DEFINED

Verified:

\[
224\times224
\rightarrow
\text{square geometry}
\]

\[
862\times1228
\rightarrow
\text{portrait geometry}
\]

\[
1724\times2457
\rightarrow
\text{scale-equivalent portrait geometry}
\]

The coordinate transformation preserves the source aspect ratio and
uses identical spatial scaling along both axes.

---

## 10. Next Step

The next measurement is the **intensity-weighted centroid** of the raw
grayscale ink field.

For pixel intensity \(I_i\) at coordinate \((x_i',y_i')\),

\[
\boxed{
x_c^{(I)}
=
\frac{\sum_i I_i x_i'}
{\sum_i I_i}
}
\]

and

\[
\boxed{
y_c^{(I)}
=
\frac{\sum_i I_i y_i'}
{\sum_i I_i}.
}
\]

This provides the first geometric measurement derived directly from the
raw source image.

The resulting centroid will then serve as the candidate origin for:

\[
\boxed{
\text{raw intensity field}
\rightarrow
\text{centroid}
\rightarrow
(r,\theta)
\rightarrow
\text{radial/angular morphology}
}
\]

No angular representation will be created until the centroid behaviour
has been empirically inspected.

# 🧪 CLO-SKET — RAW IMAGE RADIAL / ANGULAR GEOMETRY
## CELL 4 — RAW INTENSITY-WEIGHTED CENTROID

---

## 1. Objective

The objective of this cell is to establish a geometric reference point
directly from the **raw grayscale source image**, without introducing
the previously defined 135-D morphology representation.

The centroid is calculated from the continuous grayscale intensity field
after transformation into the previously verified isotropic coordinate
system.

Thus:

\[
\boxed{
\text{raw TIFF}
\rightarrow
\text{grayscale intensity}
\rightarrow
\text{isotropic coordinates}
\rightarrow
\text{intensity-weighted centroid}
}
\]

The centroid is used only as a geometric reference point at this stage.

---

## 2. Intensity-Weighted Centroid

Let

\[
I_i
\]

denote the grayscale intensity associated with pixel \(i\), and let

\[
(x_i',y_i')
\]

denote its isotropic coordinates.

The intensity-weighted centroid is calculated as

\[
\boxed{
C_x =
\frac{\sum_i I_i x_i'}
{\sum_i I_i}
}
\]

and

\[
\boxed{
C_y =
\frac{\sum_i I_i y_i'}
{\sum_i I_i}.
}
\]

The resulting centroid therefore represents the spatial centre of the
continuous image-intensity field.

---

## 3. Test Sketch

For the test sketch:

**Image:**

```text
A-Line/1-1.tif

# 🧪 CLO-SKET — RAW IMAGE RADIAL / ANGULAR GEOMETRY
## CELL 5R — RAW POLAR MORPHOLOGY — NUMERICALLY VERIFIED

---

## 1. Objective

This cell converts the original grayscale sketch into a
centroid-referenced polar representation.

The transformation is performed directly on the raw source image:

\[
\boxed{
\text{Original TIFF}
\rightarrow
\text{grayscale intensity}
\rightarrow
\text{intensity-weighted centroid}
\rightarrow
(r,\theta)
\rightarrow
\text{angular and radial morphology}
}
\]

No 64 × 64 canonical representation is used.

---

## 2. Polar Coordinate Transformation

For each pixel with isotropic coordinates

\[
(x_i',y_i')
\]

and intensity weight

\[
w_i,
\]

the centroid-referenced coordinates are

\[
\Delta x_i = x_i' - C_x
\]

and

\[
\Delta y_i = y_i' - C_y.
\]

The radial coordinate is

\[
\boxed{
r_i =
\sqrt{
\Delta x_i^2+\Delta y_i^2
}
}
\]

and the angular coordinate is

\[
\boxed{
\theta_i =
\operatorname{atan2}
(\Delta y_i,\Delta x_i)
}
\]

with

\[
\theta_i \in [-\pi,\pi).
\]

The grayscale intensity remains the weighting quantity.

Thus the experiment does not threshold the sketch into a binary
foreground mask.

---

## 3. Angular Morphology

The angular domain is divided into

\[
72
\]

equal angular sectors.

Therefore:

\[
\boxed{
360^\circ / 72 = 5^\circ
}
\]

per angular bin.

For each angular sector, the accumulated intensity is normalized
by total image intensity.

The resulting representation is:

\[
\boxed{
\mathbf{A}_i \in \mathbb{R}^{72}
}
\]

for sketch \(i\).

---

## 4. Radial Morphology

The radial coordinate is similarly divided into 72 radial bins.

The accumulated intensity in each radial interval is normalized by
the total image intensity.

The resulting representation is:

\[
\boxed{
\mathbf{P}_i \in \mathbb{R}^{72}
}
\]

for sketch \(i\).

The radial and angular profiles therefore describe two different
marginal organizations of the same raw intensity field.

---

## 5. Test Sketch

### Category

```text
A-Line

# 🧪 CLO-SKET — RAW IMAGE RADIAL / ANGULAR GEOMETRY
## CELL 6 — RAW ANGULAR / RADIAL MORPHOLOGY INSPECTION

---

## 1. Objective

This cell examines the population-level structure of the raw-image
polar representations obtained in Cell 5R.

The analysis evaluates:

1. population angular morphology;
2. population radial morphology;
3. individual angular profiles;
4. distribution of circular resultant length;
5. category-level variation in angular concentration;
6. population-level angular uniformity.

No Fourier transformation or learned representation is introduced
at this stage.

---

# 2. Input Verification

The analysis operates on the raw-image polar representations derived
directly from the original grayscale sketches.

Angular profiles:

\[
\boxed{
2300\times72
}
\]

Radial profiles:

\[
\boxed{
2300\times72
}
\]

Population:

\[
\boxed{
N=2300
}
\]

Number of source categories:

\[
\boxed{
23
}
\]

---

# 3. Population Angular Morphology

The population mean angular profile was calculated across the
2300 sketches.

The mean profile preserves normalized angular mass:

\[
\sum_j \bar A_j
=
0.9999999999997484.
\]

The mean angular maximum is

\[
\boxed{
0.0266230
}
\]

and the mean angular minimum is

\[
\boxed{
0.0070135
}
\]

Thus the population mean is not angularly uniform.

For comparison, a perfectly uniform 72-bin angular distribution
would have

\[
\frac{1}{72}
=
0.0138889
\]

mass per angular bin.

The observed mean profile therefore contains clear departures from
uniformity.

---

# 4. Population Angular Uniformity

The expected uniform angular mass is

\[
\mu_{\mathrm{uniform}}
=
\frac{1}{72}
=
0.0138889.
\]

The observed population angular mass has:

\[
\text{Mean}
=
0.0138889
\]

as required by normalization.

The across-bin standard deviation is

\[
\boxed{
SD=0.0055593
}
\]

giving a coefficient of variation of

\[
\boxed{
CV=0.40027
}
\]

Therefore, although the mean mass is necessarily \(1/72\), the
distribution around that mean is substantially non-uniform.

This provides direct evidence that the population-level angular
representation contains organized directional variation.

---

# 5. Population Angular Profile

The population mean and median profiles show a broad,
non-uniform angular organization.

Two broad regions of elevated angular mass are visible, with the
population profile showing substantial concentration in specific
angular sectors rather than approximately equal mass around the
circle.

The median follows a similar broad pattern, although with lower
magnitude and somewhat different local structure.

The agreement between mean and median is important because the
population pattern is not produced solely by a small number of
extreme sketches.

---

# 6. Population Radial Morphology

The radial representation is also examined independently.

The population mean radial profile satisfies

\[
\sum_j \bar P_j
=
0.9999999999997014.
\]

The mean radial maximum is

\[
\boxed{
0.0281585
}
\]

and the mean radial minimum is

\[
\boxed{
0.0001052
}
\]

The radial profile exhibits a broad concentration at intermediate
radial distances followed by a gradual decrease toward larger
radii.

Thus the radial mass distribution is also strongly non-uniform.

Importantly, the radial profile provides a different description
from the angular profile:

\[
\boxed{
\text{angular morphology}
\neq
\text{radial morphology}
}
\]

even though both are derived from the same raw intensity field.

---

# 7. Individual Angular Morphology

The population average should not be interpreted as representing
every individual sketch.

Representative sketches show markedly different angular profiles.

Five examples were inspected:

| Index | Category | \(R\) | Mean direction |
|---:|---|---:|---:|
| 243 | Blouse | 0.000393 | \(145.00^\circ\) |
| 1877 | Suit | 0.033523 | \(95.57^\circ\) |
| 1725 | Straight | 0.057175 | \(221.03^\circ\) |
| 1864 | Suit | 0.088774 | \(273.54^\circ\) |
| 575 | Dress | 0.245550 | \(92.75^\circ\) |

These examples demonstrate that individual angular profiles can range
from nearly cancelling directional distributions to strongly
concentrated profiles.

---

# 8. Circular Resultant Distribution

For each sketch, the angular morphology was summarized by the
circular resultant length

\[
R=
\sqrt{C^2+S^2}.
\]

The population distribution is concentrated toward relatively small
values of \(R\), but extends to substantially larger values.

The observed range is:

\[
0.000393
\leq R
\leq
0.245550.
\]

The representative examples illustrate this range:

\[
R\approx0
\]

for the Blouse example, indicating strong directional cancellation,

while

\[
R=0.24555
\]

for the Dress example indicates substantially stronger directional
concentration.

---

# 9. Category-Level Circular Resultant

Mean circular resultant varies across the 23 source categories.

The category means range from:

\[
\boxed{
0.033895
}
\]

for Wide-Leg to

\[
\boxed{
0.093935
}
\]

for Sarong.

Selected category-level values include:

| Category | Mean \(R\) |
|---|---:|
| Wide-Leg | 0.033895 |
| Jacket | 0.042972 |
| Harem | 0.049640 |
| Cardigan | 0.049705 |
| Skinny | 0.049878 |
| Straight | 0.051879 |
| Circle | 0.054808 |
| Bermuda | 0.057393 |
| Tunic | 0.059698 |
| Hoodie | 0.060464 |
| Vest | 0.061606 |
| Blouse | 0.061801 |
| Flare | 0.065006 |
| Suit | 0.065922 |
| T-shirt | 0.070729 |
| A-Line | 0.073166 |
| Pencil | 0.074081 |
| Dress | 0.076822 |
| Mermaid | 0.077014 |
| Shirt | 0.079946 |
| Jumpsuit | 0.086986 |
| Mini | 0.088479 |
| Sarong | 0.093935 |

These values demonstrate variation in directional concentration
across the source categories.

However, this analysis is descriptive only.

It does **not** establish that the categories are defined by
directional morphology, nor does it establish statistically
significant category separation.

---

# 10. Population vs Individual Structure

An important observation emerges from comparing the population
profile with the individual profiles.

Individual sketches can contain strong directional peaks, while the
population mean can remain comparatively smooth.

This occurs because directional concentration can occur at different
angles across sketches.

Consequently:

\[
\boxed{
\text{individual directional structure}
\not\Rightarrow
\text{same-direction population concentration}
}
\]

and conversely:

\[
\boxed{
\text{population angular structure}
\neq
\text{simply the angular profile of a typical sketch}
}
\]

Population averaging therefore needs to be interpreted separately
from individual-sketch organization.

---

# 11. Important Finding From the Resultant Distribution

The circular-resultant distribution provides an important complement
to the population angular profile.

The mean resultant is relatively small, but the individual profiles
show substantial variation in angular concentration.

Therefore:

\[
\boxed{
\text{low average }R
\neq
\text{absence of angular morphology}
}
\]

Instead, the result indicates that strong directional components are
not consistently aligned to a single direction across the entire
population.

This is consistent with a population containing differently
oriented or differently structured garment geometries.

---

# 12. What This Cell Establishes

The raw-image analysis provides evidence that:

### 1. Angular morphology is non-uniform

\[
CV=0.40027
\]

across the 72 angular bins.

### 2. Radial morphology is non-uniform

The population radial profile contains a pronounced distribution
across radial distance rather than uniform radial mass.

### 3. Individual angular profiles vary substantially

Circular resultant values range from approximately

\[
0.0004
\]

to

\[
0.2456.
\]

### 4. Directional concentration varies across categories

Category-level mean \(R\) values range from approximately

\[
0.034
\]

to

\[
0.094.
\]

These findings support further investigation of the angular
representation.

---

# 13. What This Cell Does NOT Establish

This analysis does not establish:

- semantic meaning of angular sectors;
- semantic meaning of radial bins;
- category separability;
- statistical significance of category differences;
- superiority of polar morphology;
- independence from the 135-D morphology representation;
- predictive utility;
- a learned morphology space;
- a morphology manifold;
- causal relationships.

In particular:

\[
\boxed{
\text{non-uniform angular morphology}
\neq
\text{semantic structure}
}
\]

The observed geometry remains a quantitative geometric observation.

---

# 14. No Fourier Representation Yet

No frequency-domain transformation has been applied.

The current representation remains:

\[
\boxed{
A_i(\theta)
}
\]

with 72 angular bins.

The next question is therefore:

> Can the observed angular organization be represented compactly
> through its angular frequency components?

This motivates the next experiment:

\[
\boxed{
\text{RAW ANGULAR MORPHOLOGY}
\rightarrow
\text{ANGULAR FOURIER DECOMPOSITION}
}
\]

---

# 15. Scientific Status

### 🟢 RAW ANGULAR / RADIAL MORPHOLOGY INSPECTION COMPLETE

Verified:

- 2300 angular profiles;
- 2300 radial profiles;
- normalized profile integrity;
- non-uniform population angular morphology;
- non-uniform radial morphology;
- substantial individual angular variation;
- distribution of circular resultant;
- category-level descriptive variation.

The results justify proceeding to Fourier analysis as a
representation-analysis step.

They do **not** justify semantic interpretation at this stage.

---

# 16. Locked Interpretation

The strongest defensible statement from this cell is:

\[
\boxed{
\textbf{
Raw garment sketches exhibit measurable,
non-uniform angular and radial intensity organization
when represented in a centroid-referenced polar coordinate system.
}
}
\]

The next experiment asks whether this angular organization possesses
a compact and reproducible frequency-domain representation.

# 🧪 CLO-SKET — RAW IMAGE RADIAL / ANGULAR GEOMETRY
## CELL 7R — RAW ANGULAR FOURIER MORPHOLOGY

### Numerically Corrected Parseval Accounting

---

# 1. Objective

This experiment asks whether the non-uniform angular morphology observed
directly in the raw grayscale sketches can be represented in the
frequency domain.

The analysis starts from the raw-image angular morphology

\[
A_i(\theta)
\]

and applies a circular Fourier transform.

The purpose is to determine:

1. whether angular morphology contains dominant low-order harmonics;
2. whether the first and second angular harmonics differ systematically;
3. how much angular morphology can be reconstructed using a limited
   number of harmonics;
4. whether the observed angular structure is quantitatively
   represented by a compact frequency-domain description.

No semantic interpretation is assigned to individual harmonics.

---

# 2. Input

The input consists of the raw-image angular morphology profiles
derived in Cell 5R.

Number of sketches:

\[
\boxed{N=2300}
\]

Angular resolution:

\[
\boxed{72\text{ bins}}
\]

Input matrix:

\[
\boxed{
\mathbf{A}\in\mathbb{R}^{2300\times72}
}
\]

Each angular profile is normalized to unit total mass.

Maximum normalization error:

\[
\boxed{
4.57\times10^{-13}
}
\]

Thus all 2300 profiles satisfy the normalization requirement to
numerical precision.

---

# 3. Fourier Transformation

For each sketch \(i\), the angular profile

\[
A_i(\theta)
\]

is transformed using the real discrete Fourier transform.

The resulting representation is

\[
\boxed{
\mathbf{F}\in\mathbb{C}^{2300\times37}
}
\]

because a 72-point real-valued signal produces

\[
\frac{72}{2}+1=37
\]

non-negative-frequency Fourier components.

The harmonics are indexed by

\[
k=0,\ldots,36.
\]

---

# 4. Parseval Energy Verification

Because Fourier power is subsequently used to quantify the contribution
of different angular frequencies, energy accounting was explicitly
verified.

The maximum absolute Parseval error was

\[
\boxed{
1.73\times10^{-17}
}
\]

with mean absolute error

\[
\boxed{
3.97\times10^{-18}
}
\]

and maximum relative error

\[
\boxed{
9.94\times10^{-16}
}
\]

Therefore:

\[
\boxed{
\text{Parseval energy conservation verified}
}
\]

The reported Fourier power fractions therefore account for the
angular-profile energy without numerical loss.

---

# 5. Harmonic Spectrum

The population-level Fourier spectrum is strongly dominated by
low-order components.

The mean Fourier magnitudes are:

| Harmonic | Mean magnitude | Corrected power | Fraction of total power |
|---:|---:|---:|---:|
| \(k=0\) | 0.013889 | 0.013889 | 0.741504 |
| \(k=1\) | 0.000897 | 0.000162 | 0.008659 |
| \(k=2\) | 0.003843 | 0.002514 | 0.134203 |
| \(k=3\) | 0.001147 | 0.000249 | 0.013307 |
| \(k=4\) | 0.001143 | 0.000271 | 0.014442 |
| \(k=5\) | 0.001002 | 0.000201 | 0.010743 |
| \(k=6\) | 0.000836 | 0.000138 | 0.007359 |
| \(k=7\) | 0.000826 | 0.000138 | 0.007368 |
| \(k=8\) | 0.000750 | 0.000114 | 0.006074 |
| \(k=9\) | 0.000691 | 0.000097 | 0.005173 |
| \(k=10\) | 0.000673 | 0.000090 | 0.004785 |
| \(k=11\) | 0.000606 | 0.000074 | 0.003937 |
| \(k=12\) | 0.000576 | 0.000065 | 0.003495 |
| \(k=13\) | 0.000543 | 0.000059 | 0.003156 |
| \(k=14\) | 0.000516 | 0.000054 | 0.002889 |
| \(k=15\) | 0.000488 | 0.000049 | 0.002598 |
| \(k=16\) | 0.000485 | 0.000048 | 0.002541 |

The DC component

\[
k=0
\]

accounts for approximately

\[
\boxed{74.15\%}
\]

of the total Fourier power.

Among the non-DC components, the second harmonic is the dominant
component.

---

# 6. First vs Second Harmonic

The first harmonic has:

\[
\boxed{
\text{Mean }|F_1|=0.0008969
}
\]

whereas the second harmonic has:

\[
\boxed{
\text{Mean }|F_2|=0.0038425
}
\]

The ratio is therefore:

\[
\boxed{
\frac{|F_2|}{|F_1|}
=
4.284
}
\]

using the population means.

The corresponding median ratio is:

\[
\boxed{
4.770
}
\]

because

\[
\text{Median }|F_1|
=
0.0007933
\]

and

\[
\text{Median }|F_2|
=
0.0037841.
\]

Thus the second harmonic is consistently much stronger than the
first harmonic across the population.

---

# 7. Interpretation of the First Harmonic

The first harmonic represents the first-order directional component
of the angular morphology.

Its relatively small magnitude is consistent with the earlier
circular-resultant analysis.

In particular:

\[
R_i
=
|F_{i,1}|
\]

up to the normalization convention used for the Fourier transform.

Therefore, weak first-order directional concentration is not
evidence that the angular morphology itself is weak.

Instead, directional contributions can cancel at the first harmonic
while remaining strongly organized at higher harmonics.

---

# 8. Dominance of the Second Harmonic

The second harmonic accounts for:

\[
\boxed{
13.42\%
}
\]

of the total corrected Fourier power.

This is substantially larger than the first harmonic contribution:

\[
\boxed{
0.866\%
}
\]

and is also larger than any of the individual higher harmonics
reported in the table.

Therefore:

\[
\boxed{
|F_2| \gg |F_1|
}
\]

is a reproducible population-level property of the raw angular
representation.

The result is consistent with a strong two-fold angular component
in the observed morphology.

This should be interpreted strictly as a statement about the
geometry of the angular signal.

It is **not** interpreted as evidence that garments are universally
bilaterally symmetric.

---

# 9. Fourier Reconstruction

The angular profiles were reconstructed using progressively larger
numbers of harmonics.

The results are:

| \(K\) | Mean RMSE | Median RMSE | 90th percentile RMSE | Mean explained variance | Median explained variance |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.007718 | 0.007327 | 0.010955 | 0.040739 | 0.022355 |
| 2 | 0.005237 | 0.004979 | 0.007379 | 0.521178 | 0.558421 |
| 4 | 0.004534 | 0.004276 | 0.006486 | 0.642422 | 0.667276 |
| 8 | 0.003589 | 0.003304 | 0.005339 | 0.775753 | 0.794779 |
| 16 | 0.002470 | 0.002245 | 0.003825 | 0.891474 | 0.906959 |
| 32 | 0.000857 | 0.000738 | 0.001513 | 0.985277 | 0.989917 |

---

# 10. Importance of the \(K=2\) Reconstruction

Using only the first harmonic gives relatively poor reconstruction:

\[
\boxed{
EV_{K=1}=0.0407
}
\]

When the second harmonic is added:

\[
\boxed{
EV_{K=2}=0.5212
}
\]

This is a large increase.

The median explained variance similarly increases from

\[
0.0224
\]

to

\[
0.5584.
\]

Therefore the second harmonic captures a substantial component of
the angular morphology that is not represented by the first
directional harmonic alone.

This is consistent with the spectral result:

\[
\boxed{
\text{strong second-harmonic structure}
}
\]

---

# 11. Higher Harmonics

Additional harmonics progressively improve reconstruction:

\[
K=4
\rightarrow
64.24\%
\]

mean explained variance,

\[
K=8
\rightarrow
77.58\%
\]

\[
K=16
\rightarrow
89.15\%
\]

and

\[
K=32
\rightarrow
98.53\%.
\]

Thus the angular morphology contains both:

1. a strong low-order component; and
2. progressively finer angular structure.

The Fourier representation therefore provides a natural multiscale
description of the raw angular morphology.

---

# 12. Representative Reconstruction

For a representative high-resultant sketch

\[
R=0.246,
\]

the observed angular morphology contains several sharp local
features.

The reconstructions show the expected progression:

\[
K=2
\rightarrow
\text{broad low-frequency structure}
\]

\[
K=4
\rightarrow
\text{additional angular variation}
\]

\[
K=8
\rightarrow
\text{more localized structure}
\]

\[
K=16
\rightarrow
\text{close approximation of the observed profile}.
\]

This demonstrates that the Fourier representation is not merely
describing a population average; it can also reconstruct
individual angular morphology profiles at increasing levels of
frequency resolution.

---

# 13. What This Experiment Establishes

The raw-image Fourier analysis provides evidence for the following:

### 1. Angular morphology has measurable frequency structure

The Fourier spectrum is strongly non-uniform across harmonics.

### 2. The second harmonic is particularly prominent

\[
\boxed{
\frac{\text{Mean }|F_2|}
{\text{Mean }|F_1|}
=
4.284
}
\]

### 3. The second harmonic contributes substantial angular-profile
energy

\[
\boxed{
13.42\%
}
\]

of total corrected Fourier power.

### 4. Low-order harmonics provide meaningful reconstruction

Using only \(K=2\) harmonics explains approximately

\[
\boxed{
52.1\%
}
\]

of the mean variance.

### 5. Increasing frequency resolution progressively recovers finer
morphological structure

\[
\boxed{
K=32
\Rightarrow
98.53\%
}
\]

mean explained variance.

### 6. Fourier energy accounting is numerically exact

Parseval's identity was satisfied to approximately machine precision.

---

# 14. What This Experiment Does NOT Establish

This analysis does not establish:

- that \(k=2\) corresponds to a semantic garment property;
- that garments are universally symmetric;
- that Fourier coefficients are independent;
- that Fourier representation is superior to the 135-D morphology
  representation;
- that Fourier coordinates form a semantic morphology space;
- category separability;
- predictive superiority;
- causal interpretation;
- human perceptual correspondence.

In particular:

\[
\boxed{
\text{strong }k=2
\neq
\text{semantic bilateral symmetry}
}
\]

and

\[
\boxed{
\text{Fourier compactness}
\neq
\text{semantic understanding}
}
\]

---

# 15. Relationship to the Earlier Raw Polar Analysis

The previous cell established that raw angular morphology is
non-uniform and that individual sketches can exhibit different
degrees of directional concentration.

The present analysis adds a frequency-domain interpretation:

\[
\boxed{
A(\theta)
\rightarrow
F_k
}
\]

and shows that the dominant low-order non-DC structure is concentrated
particularly strongly at

\[
\boxed{
k=2.
}
\]

Thus the two analyses are complementary:

\[
\text{Circular statistics}
\rightarrow
\text{first-order directional concentration}
\]

whereas

\[
\text{Fourier analysis}
\rightarrow
\text{multi-order angular structure}.
\]

The low \(k=1\) magnitude and strong \(k=2\) magnitude are therefore
not contradictory.

They describe different aspects of the same angular morphology.

---

# 16. Scientific Status

### 🟢 RAW ANGULAR FOURIER MORPHOLOGY COMPLETE

Verified:

- 2300 normalized angular profiles;
- 37 Fourier components per sketch;
- Parseval energy conservation;
- first-harmonic magnitude;
- second-harmonic magnitude;
- corrected Fourier power;
- harmonic spectrum;
- low-order reconstruction;
- individual-profile reconstruction.

The principal quantitative observation is:

\[
\boxed{
\textbf{
The raw angular morphology exhibits substantially stronger
second-harmonic structure than first-order directional structure.
}
}
\]

---

# 17. Locked Interpretation

The strongest defensible conclusion at this stage is:

\[
\boxed{
\textbf{
Raw garment-sketch intensity fields exhibit structured angular
variation that is strongly represented by low-order Fourier
components, with the second angular harmonic substantially
exceeding the first.
}
}
\]

This supports treating angular Fourier coefficients as a candidate
compact geometric representation.

It does **not** yet establish what those coefficients mean
semantically.

The next scientific question is therefore not:

> "What does \(k=2\) mean?"

but:

> **Does the raw-image Fourier representation contain reproducible
> information that corresponds to, overlaps with, or complements the
> independently defined morphology representation?**

That is the point at which cross-representation analysis becomes
scientifically justified.

# 🧪 CLO-SKET — RAW IMAGE RADIAL / ANGULAR GEOMETRY
## CELL 8 — SECOND-HARMONIC ROBUSTNESS AUDIT

---

# 1. Objective

Cell 7R established that the second angular Fourier harmonic
substantially exceeds the first harmonic at the population level.

The purpose of this cell is to determine whether that observation
is:

- driven by a small number of sketches;
- restricted to particular garment categories;
- sensitive to population averaging;

or instead represents a broad property of the Clo-SKET collection.

The primary comparison is:

\[
|F_2| \quad \text{vs.} \quad |F_1|
\]

for every individual sketch.

---

# 2. Input Verification

Fourier magnitude matrix:

\[
\boxed{
2300\times37
}
\]

Number of source sketches:

\[
\boxed{
2300
}
\]

The Fourier representation used here is exactly the representation
verified in Cell 7R.

No new image representation is introduced.

---

# 3. Population-Level Second-Harmonic Dominance

The previously observed population means are:

\[
\text{Mean }|F_1|
=
0.000896911
\]

\[
\text{Mean }|F_2|
=
0.003842511
\]

Therefore:

\[
\boxed{
\frac{\text{Mean }|F_2|}
{\text{Mean }|F_1|}
=
4.284
}
\]

The median values show the same pattern:

\[
\text{Median }|F_1|
=
0.0007933087
\]

\[
\text{Median }|F_2|
=
0.003784139
\]

giving

\[
\boxed{
\frac{\text{Median }|F_2|}
{\text{Median }|F_1|}
=
4.770
}
\]

Thus second-harmonic dominance is present under both
mean and median summaries.

---

# 4. Individual-Sketch Comparison

The most important robustness test compares the two harmonics
for every sketch independently.

Number of sketches satisfying

\[
|F_2|>|F_1|
\]

was:

\[
\boxed{
2226/2300
}
\]

or

\[
\boxed{
96.78\%
}
\]

of the complete dataset.

Therefore only

\[
74/2300
\]

sketches have

\[
|F_1|\geq |F_2|.
\]

This demonstrates that the population-level result is not produced
by a small subset of highly structured sketches.

Instead, second-harmonic dominance occurs in the overwhelming
majority of individual sketches.

---

# 5. Distribution of the \(F_2/F_1\) Ratio

The distribution of

\[
\frac{|F_2|}{|F_1|}
\]

is strongly shifted above unity.

The empirical quantiles are:

| Percentile | \(|F_2|/|F_1|\) |
|---:|---:|
| 10th | 1.720 |
| 25th | 2.685 |
| 50th | 4.602 |
| 75th | 8.311 |
| 90th | 14.582 |
| 95th | 22.061 |

The median ratio is therefore:

\[
\boxed{
4.60
}
\]

meaning that at least half of the sketches have a second harmonic
more than four times the magnitude of the first harmonic.

Even the 10th percentile remains above unity:

\[
\boxed{
Q_{0.10}=1.72
}
\]

Thus second-harmonic dominance is not confined to the extreme tail
of the population.

---

# 6. \(F_1\) vs \(F_2\) Geometry

The scatter plot of

\[
|F_1|
\]

against

\[
|F_2|
\]

provides an individual-level view of the result.

The diagonal

\[
|F_2|=|F_1|
\]

marks equal first- and second-harmonic magnitude.

The large majority of observations lie above this diagonal.

This is consistent with the direct count:

\[
\boxed{
96.78\%
\text{ of sketches have } |F_2|>|F_1|.
}
\]

The result therefore persists at the individual-sketch level rather
than arising solely from averaging Fourier coefficients across the
population.

---

# 7. Category-Level Verification

The dataset contains:

\[
\boxed{
23
}
\]

Clo-SKET categories, with 100 sketches per category.

The second-harmonic dominance was evaluated independently within
each category.

| Category | Mean \(|F_1|\) | Mean \(|F_2|\) | Mean \(F_2/F_1\) | Fraction \(F_2>F_1\) |
|---|---:|---:|---:|---:|
| Skinny | 0.000693 | 0.005715 | 8.252 | 1.00 |
| Straight | 0.000720 | 0.005597 | 7.769 | 1.00 |
| Harem | 0.000689 | 0.004584 | 6.652 | 1.00 |
| Flare | 0.000902 | 0.005680 | 6.294 | 1.00 |
| Wide-Leg | 0.000470 | 0.002724 | 5.797 | 1.00 |
| Dress | 0.001067 | 0.005413 | 5.074 | 1.00 |
| Vest | 0.000855 | 0.004247 | 4.967 | 1.00 |
| Pencil | 0.001028 | 0.004932 | 4.797 | 1.00 |
| Jacket | 0.000597 | 0.002851 | 4.778 | 1.00 |
| Jumpsuit | 0.001208 | 0.005692 | 4.713 | 1.00 |
| Circle | 0.000761 | 0.003519 | 4.626 | 1.00 |
| Mermaid | 0.001069 | 0.004747 | 4.439 | 1.00 |
| Tunic | 0.000829 | 0.003640 | 4.389 | 0.99 |
| Cardigan | 0.000690 | 0.002893 | 4.192 | 0.99 |
| Sarong | 0.001304 | 0.005187 | 3.977 | 1.00 |
| Hoodie | 0.000839 | 0.003236 | 3.856 | 1.00 |
| Suit | 0.000916 | 0.003088 | 3.373 | 0.96 |
| Shirt | 0.001110 | 0.003205 | 2.888 | 0.99 |
| Mini | 0.001228 | 0.003285 | 2.674 | 0.98 |
| A-Line | 0.001015 | 0.002611 | 2.571 | 0.90 |
| T-shirt | 0.000982 | 0.002331 | 2.374 | 0.93 |
| Bermuda | 0.000797 | 0.001808 | 2.268 | 0.81 |
| Blouse | 0.000859 | 0.001394 | 1.623 | 0.71 |

---

# 8. Category Consistency

The category-level result is particularly important.

All 23 categories satisfy:

\[
\boxed{
\text{fraction}(F_2>F_1)>0.50
}
\]

Therefore:

\[
\boxed{
23/23
}
\]

categories show second-harmonic dominance in more than half of their
individual sketches.

The minimum category-level fraction is:

\[
\boxed{
0.71
}
\]

while the median is:

\[
\boxed{
1.00
}
\]

and the maximum is:

\[
\boxed{
1.00.
}
\]

Thus the phenomenon is not confined to a particular garment class.

---

# 9. Category-Level Variation

Although second-harmonic dominance is highly consistent across
categories, its magnitude varies.

The largest mean ratios occur for:

- Skinny: \(8.25\)
- Straight: \(7.77\)
- Harem: \(6.65\)
- Flare: \(6.29\)
- Wide-Leg: \(5.80\)

The smallest mean ratios occur for:

- Blouse: \(1.62\)
- Bermuda: \(2.27\)
- T-shirt: \(2.37\)
- A-Line: \(2.57\)
- Mini: \(2.67\)

This indicates that the **existence of second-harmonic dominance**
is highly consistent, while its strength varies across categories.

This category variation is descriptive only.

It is not yet interpreted as semantic category structure.

---

# 10. Bootstrap Robustness

To test the stability of the population difference, the statistic

\[
D=\overline{|F_2|-|F_1|}
\]

was evaluated through bootstrap resampling.

Observed difference:

\[
\boxed{
D=0.00294560
}
\]

The 95% bootstrap confidence interval is:

\[
\boxed{
[0.00287830,\;0.00301289]
}
\]

The entire interval lies above zero.

Therefore:

\[
\boxed{
|F_2|>|F_1|
}
\]

is supported at the population level under bootstrap resampling.

Importantly, this conclusion does not depend on a single estimate
of the sample mean.

---

# 11. What the Bootstrap Result Means

The bootstrap analysis supports the stability of the observed
population difference:

\[
\overline{|F_2|}
-
\overline{|F_1|}
>0.
\]

The confidence interval remains positive under resampling of the
2300 sketches.

This provides an additional robustness check alongside the
individual-sketch comparison.

The evidence therefore converges across three levels:

### Population level

\[
\overline{|F_2|}
>
\overline{|F_1|}
\]

### Individual level

\[
96.78\%
\]

of sketches satisfy

\[
|F_2|>|F_1|.
\]

### Category level

\[
23/23
\]

categories have more than 50% of sketches satisfying

\[
|F_2|>|F_1|.
\]

---

# 12. Convergent Evidence

The second-harmonic observation is therefore supported by
multiple independent summaries:

\[
\boxed{
\text{Mean ratio}=4.284
}
\]

\[
\boxed{
\text{Median ratio}=4.602
}
\]

\[
\boxed{
96.78\%\text{ of sketches: }F_2>F_1
}
\]

\[
\boxed{
23/23\text{ categories: }F_2>F_1\text{ in }>50\%
}
\]

\[
\boxed{
95\%\text{ bootstrap CI for }F_2-F_1
=
[0.002878,\;0.003013]
}
\]

These results all point in the same direction.

---

# 13. Scientific Interpretation

The strongest defensible interpretation is:

\[
\boxed{
\textbf{
Second-harmonic angular structure is a broad geometric property
of the raw Clo-SKET sketch collection rather than an artifact
of population averaging or a small number of sketches.
}
}
\]

The evidence is particularly strong because the effect is observed:

- across individual sketches;
- across all 23 categories;
- in both mean and median summaries;
- across the distribution of \(F_2/F_1\);
- and under bootstrap resampling.

---

# 14. What This Does NOT Establish

This robustness audit does **not** establish:

- semantic meaning of \(k=2\);
- that \(k=2\) represents garment symmetry in a semantic sense;
- that the 23 categories are defined by their Fourier structure;
- perceptual equivalence between Fourier components and human design
  concepts;
- predictive usefulness;
- superiority over the canonical morphology representation;
- causal explanations for the second-harmonic dominance.

In particular:

\[
\boxed{
\text{robust geometric structure}
\neq
\text{semantic structure}
}
\]

and

\[
\boxed{
F_2>F_1
\neq
\text{proof of garment symmetry}.
}
\]

The result should remain a statement about the geometry of the
raw angular intensity field.

---

# 15. Relationship to Cell 7R

Cell 7R established:

\[
|F_2| \gg |F_1|
\]

at the population level and showed that low-order Fourier components
can reconstruct substantial angular morphology.

Cell 8 strengthens that observation by demonstrating that the
second-harmonic dominance is:

\[
\boxed{
\text{individual-level}
+
\text{category-consistent}
+
\text{bootstrap-stable}.
}
\]

Therefore Cell 8 does not introduce a new representation.

It provides a robustness audit of the Fourier structure already
identified in Cell 7R.

---

# 16. Locked Result

The principal result from Cells 7R–8 is:

\[
\boxed{
\textbf{
Raw Clo-SKET angular morphology exhibits strong and robust
second-harmonic structure.
}
}
\]

Quantitatively:

\[
\boxed{
\text{Mean }|F_2|/
\text{Mean }|F_1|
=
4.284
}
\]

and

\[
\boxed{
2226/2300
=
96.78\%
}
\]

of sketches have

\[
|F_2|>|F_1|.
\]

Furthermore:

\[
\boxed{
23/23
}
\]

categories show the same direction of dominance in more than half
of their sketches.

The bootstrap confidence interval for the mean difference is also
strictly positive:

\[
\boxed{
0.002878
<
\overline{|F_2|-|F_1|}
<
0.003013
}
\]

at the 95% bootstrap level.

---

# 17. Scientific Status

### 🟢 CELL 8 — SECOND-HARMONIC ROBUSTNESS AUDIT COMPLETE

Verified:

- individual \(F_1\) vs \(F_2\);
- \(F_2/F_1\) distribution;
- individual-sketch dominance;
- category-level dominance;
- 23-category consistency;
- bootstrap confidence interval;
- population-level robustness.

The raw TIFF representation remains untouched.

The Paper-I canonical morphology representation remains untouched.

No semantic interpretation has been introduced.

---

# 18. Next Scientific Question

The second-harmonic result is now sufficiently robust to justify
the next question:

> **Does this raw-image angular structure correspond to, complement,
> or remain independent of the morphology structure already captured
> by the predefined canonical morphology representation?**

This is the appropriate point to move from:

\[
\boxed{
\text{discovery of raw geometric structure}
}
\]

to

\[
\boxed{
\text{cross-representation validation}.
}
\]

Any semantic interpretation should be deferred until that comparison
is performed.

# 🧪 CLO-SKET — RAW IMAGE RADIAL / ANGULAR GEOMETRY
## CELL 9 — SECOND-HARMONIC PHASE + TWO-FOLD ORIENTATION

---

# 1. Objective

Cell 8 established that the second angular Fourier harmonic
systematically dominates the first harmonic across individual
sketches and across all 23 Clo-SKET categories.

Cell 9 asks a different question:

> If the second harmonic is strong, is its **phase** also
> geometrically organized?

The magnitude of \(F_2\) measures the strength of the two-fold
angular component.

The phase of \(F_2\) determines its orientation.

Therefore this cell separates:

\[
\boxed{
\text{strength}
}
\]

from

\[
\boxed{
\text{orientation}.
}
\]

---

# 2. Input Verification

Angular morphology representation:

\[
\boxed{
2300\times72
}
\]

Number of angular bins:

\[
\boxed{
72
}
\]

Maximum profile normalization error:

\[
2.22\times10^{-16}
\]

Thus the angular profiles remain numerically normalized before
Fourier analysis.

---

# 3. Complex Angular Fourier Representation

The normalized angular morphology profile

\[
A_i(\theta)
\]

is transformed using the complex discrete Fourier transform.

For each sketch:

\[
A_i(\theta)
\rightarrow
F_{i,k}.
\]

The complex rFFT contains:

\[
\boxed{
37
}
\]

available harmonics.

For the present analysis, the principal quantity is:

\[
F_2.
\]

Because \(F_2\) is complex, it contains two independent pieces
of information:

\[
F_2
=
|F_2|e^{i\phi_2}.
\]

Therefore:

- \(|F_2|\) describes the strength of the two-fold component;
- \(\phi_2=\arg(F_2)\) describes its phase.

---

# 4. Second-Harmonic Magnitude

The mean and median magnitudes are:

\[
\text{Mean }|F_1|
=
0.064578
\]

\[
\text{Mean }|F_2|
=
0.276661
\]

and

\[
\text{Median }|F_1|
=
0.057118
\]

\[
\text{Median }|F_2|
=
0.272458.
\]

Thus the second harmonic remains substantially stronger than the
first under the complex Fourier representation.

This is consistent with the magnitude-based robustness analysis
from Cell 8.

---

# 5. Definition of the Two-Fold Axis

Because a second harmonic repeats every \(180^\circ\), its orientation
is axial rather than directional.

The two-fold axis is defined as:

\[
\boxed{
\alpha_2
=
-\frac{\arg(F_2)}{2}
\pmod{180^\circ}
}
\]

Therefore:

\[
\alpha_2
\equiv
\alpha_2+180^\circ.
\]

This distinction is important.

A two-fold axis does not have an intrinsic arrow.

For example:

\[
90^\circ
\]

and

\[
270^\circ
\]

represent the same axis.

---

# 6. Population Two-Fold Orientation

Across all 2300 sketches:

\[
\text{Mean axis angle}
=
87.698^\circ
\]

\[
\text{Median axis angle}
=
87.385^\circ.
\]

The observed range is:

\[
1.521^\circ
\leq
\alpha_2
\leq
179.286^\circ.
\]

The population distribution is therefore strongly concentrated
around approximately:

\[
\boxed{
87^\circ-88^\circ
}
\]

rather than being uniformly distributed over the full
\(0^\circ-180^\circ\) axial domain.

---

# 7. Axial Circular Statistics

Because \(\alpha_2\) is an axial quantity, ordinary directional
circular statistics are inappropriate.

The doubled-angle representation is used:

\[
2\alpha_2.
\]

The corresponding axial components are:

\[
C_2
=
\operatorname{mean}
\left[
\cos(2\alpha_2)
\right]
\]

and

\[
S_2
=
\operatorname{mean}
\left[
\sin(2\alpha_2)
\right].
\]

The axial resultant is:

\[
R_2
=
\sqrt{C_2^2+S_2^2}.
\]

Observed values:

\[
C_2=-0.936751
\]

\[
S_2=0.083469
\]

and

\[
\boxed{
R_2=0.940462
}
\]

with population mean axis:

\[
\boxed{
87.454^\circ.
}
\]

A resultant this close to one indicates strong concentration of the
estimated two-fold axes around a common orientation.

---

# 8. Interpretation of the Axial Resultant

The axial resultant

\[
R_2=0.940462
\]

indicates that the estimated second-harmonic axes are highly
concentrated.

This is qualitatively different from the low first-order resultant
observed earlier.

The two quantities describe different structures:

### First harmonic

\[
F_1
\]

describes first-order directional concentration.

### Second harmonic

\[
F_2
\]

describes a two-fold angular component.

Therefore:

\[
\boxed{
\text{low }F_1
\not\Rightarrow
\text{absence of directional organization}
}
\]

because a strong two-fold component can cancel the first-order
directional resultant while maintaining a highly stable axial
orientation.

---

# 9. Phase Stability as a Function of \(F_2\) Strength

Weak Fourier components can have unstable phase estimates.

Therefore phase concentration was additionally examined after
restricting the analysis to sketches with relatively strong
second-harmonic magnitude.

The 25th percentile of \(|F_2|\) is:

\[
\boxed{
0.1908758
}
\]

and sketches above this threshold form the strong-\(F_2\) subset:

\[
\boxed{
1725/2300
}
\]

sketches.

For this subset:

\[
\boxed{
R_2=0.987345
}
\]

and

\[
\boxed{
\text{mean axis}=87.254^\circ.
}
\]

Thus the orientation becomes even more concentrated when only
stronger second-harmonic components are considered.

This supports the interpretation that the phase concentration is not
simply generated by unstable low-amplitude Fourier coefficients.

---

# 10. Population vs Strong-\(F_2\) Orientation

The comparison is:

| Population | Strong-\(F_2\) subset |
|---|---:|
| \(n=2300\) | \(n=1725\) |
| Mean axis | \(87.698^\circ\) |
| Axial resultant | \(0.940462\) |
| Mean axis, strong subset | \(87.254^\circ\) |
| Axial resultant, strong subset | \(0.987345\) |

The estimated axis therefore remains essentially unchanged while
concentration increases substantially.

This provides evidence that the dominant orientation is not
dependent on weak \(F_2\) estimates.

---

# 11. Category-Level Two-Fold Orientation

The axial orientation was also evaluated independently within each
of the 23 Clo-SKET categories.

| Category | Mean \(|F_2|\) | Axial resultant \(R_2\) | Mean axis (°) |
|---|---:|---:|---:|
| Jumpsuit | 0.409800 | 0.996500 | 87.108 |
| Mermaid | 0.341765 | 0.994830 | 87.794 |
| Pencil | 0.355090 | 0.994660 | 87.280 |
| Skinny | 0.411515 | 0.994622 | 86.675 |
| Vest | 0.305812 | 0.994529 | 86.879 |
| Straight | 0.403002 | 0.994410 | 87.730 |
| Dress | 0.389744 | 0.994024 | 87.426 |
| Flare | 0.408948 | 0.993841 | 86.749 |
| Hoodie | 0.232983 | 0.993634 | 87.235 |
| Harem | 0.330042 | 0.993591 | 86.612 |
| Jacket | 0.205249 | 0.991566 | 87.810 |
| Circle | 0.253397 | 0.988656 | 87.842 |
| Shirt | 0.230758 | 0.986443 | 87.929 |
| Sarong | 0.373433 | 0.984520 | 87.409 |
| Cardigan | 0.208292 | 0.983142 | 86.419 |
| Suit | 0.222339 | 0.980793 | 87.008 |
| Mini | 0.236491 | 0.980133 | 88.432 |
| Tunic | 0.262047 | 0.973144 | 88.411 |
| T-shirt | 0.167847 | 0.967699 | 87.357 |
| Wide-Leg | 0.196105 | 0.960882 | 88.567 |
| A-Line | 0.187992 | 0.955108 | 89.932 |
| Bermuda | 0.130204 | 0.754181 | 86.024 |
| Blouse | 0.100343 | 0.190832 | 83.139 |

---

# 12. Category-Level Stability

The category results reveal an important distinction.

For most categories, the estimated two-fold axis is extremely
concentrated:

\[
R_2\approx0.96-0.997.
\]

The corresponding mean axes are generally clustered around:

\[
\boxed{
87^\circ-89^\circ
}
\]

despite substantial differences in mean \(F_2\) magnitude.

Thus:

\[
\boxed{
\text{strength of two-fold structure}
}
\]

and

\[
\boxed{
\text{orientation of two-fold structure}
}
\]

are not the same quantity.

Some categories exhibit weaker \(F_2\) magnitude but can still show
a strongly concentrated axis.

---

# 13. Important Category Exceptions

The strongest concentration is not universal.

In particular:

### Bermuda

\[
R_2=0.754181
\]

### Blouse

\[
R_2=0.190832
\]

These categories show substantially weaker axial concentration than
the majority of categories.

Therefore the appropriate claim is not that every category possesses
the same perfectly stable two-fold axis.

Instead, the evidence supports a strong population-level axial
organization with category-dependent variation in concentration.

---

# 14. What the Phase Analysis Adds to Cell 8

Cell 8 established:

\[
|F_2|>|F_1|
\]

for the overwhelming majority of sketches.

Cell 9 adds:

\[
\boxed{
\arg(F_2)
\rightarrow
\text{stable two-fold orientation}.
}
\]

Therefore the evidence now separates into two dimensions:

\[
\boxed{
F_2
=
\underbrace{|F_2|}_{\text{strength}}
+
\underbrace{\arg(F_2)}_{\text{orientation}}
}
\]

The magnitude result says that a two-fold component is strong.

The phase result says that this component is also geometrically
oriented in a highly consistent manner.

---

# 15. Geometric Interpretation

The observed population axis is approximately:

\[
\boxed{
87.5^\circ
}
\]

in the original image coordinate system.

The concentration around this orientation indicates that the dominant
two-fold angular component is not randomly rotated across the
dataset.

Importantly, this is an observation about the coordinate system
used by the source sketches.

It should not yet be interpreted as a semantic "vertical garment
axis" or as a learned notion of garment orientation.

The current evidence establishes:

\[
\boxed{
\text{stable image-coordinate axial orientation}
}
\]

not:

\[
\boxed{
\text{semantic garment axis}.
}
\]

---

# 16. Critical Distinction: Magnitude vs Phase

The experiment demonstrates why magnitude and phase must be analyzed
separately.

Two sketches may have:

\[
|F_2|_{\!A}
\approx
|F_2|_{\!B}
\]

but different phases.

Conversely, two sketches may have very different \(F_2\) magnitudes
while sharing nearly the same axis.

Therefore a complete description of the two-fold component requires
both:

\[
\boxed{
(|F_2|,\alpha_2)
}
\]

rather than magnitude alone.

This motivates retaining the two quantities as separate geometric
descriptors in subsequent representation analysis.

---

# 17. What This Result Does NOT Establish

The phase concentration does **not** by itself establish:

- bilateral symmetry;
- semantic garment symmetry;
- a garment-part axis;
- category semantics;
- human perceptual organization;
- a universal fashion-design coordinate system;
- causal reasons for the observed orientation.

In particular:

\[
\boxed{
\text{axial concentration}
\neq
\text{semantic symmetry}.
}
\]

The present result remains a geometric statement about the raw
image-derived angular intensity field.

---

# 18. Scientific Result

The strongest defensible statement from Cell 9 is:

> The dominant second angular Fourier component of the raw Clo-SKET
> grayscale morphology exhibits a strongly concentrated two-fold
> axial orientation, centered near \(87.5^\circ\) in the original
> image coordinate system. This concentration becomes stronger when
> analysis is restricted to sketches with larger second-harmonic
> magnitude and is observed across most Clo-SKET categories, although
> the strength of axial concentration varies substantially by category.

Quantitatively:

\[
\boxed{
R_2=0.940462
}
\]

for all sketches, increasing to

\[
\boxed{
R_2=0.987345
}
\]

for the strong-\(F_2\) subset.

---

# 19. Current Raw-Image Evidence Chain

The raw-image branch now forms the following sequence:

\[
\boxed{
\text{Original TIFF}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{Intensity-weighted centroid}
}
\]

\[
\downarrow
\]

\[
\boxed{
A(\theta)
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{Angular Fourier transform}
}
\]

\[
\downarrow
\]

\[
\boxed{
|F_2|>|F_1|
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{Second-harmonic robustness}
}
\]

\[
\downarrow
\]

\[
\boxed{
\arg(F_2)
\rightarrow
\alpha_2
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{stable two-fold axial orientation}
}
\]

This is now a coherent empirical geometric result derived directly
from the original grayscale images.

---

# 20. Scientific Status

### 🟢 CELL 9 — SECOND-HARMONIC PHASE AUDIT COMPLETE

Established:

- complex Fourier representation;
- second-harmonic magnitude;
- two-fold axial orientation;
- axial circular statistics;
- population-level phase concentration;
- strong-\(F_2\) phase stability;
- category-level orientation statistics.

The raw TIFF representation remains untouched.

The canonical Paper-I morphology representation remains untouched.

No semantic labels were used to construct the raw angular
representation.

No semantic interpretation is made from the observed axis.

---

# 21. Next Scientific Question

The next question is now more precise.

We have established that raw-image angular morphology contains:

\[
\boxed{
\text{strong two-fold magnitude}
}
\]

and

\[
\boxed{
\text{stable two-fold orientation}.
}
\]

The next step is therefore to ask:

> **How does this radial–angular structure relate to the morphology
> representation already defined from canonical occupancy measurements?**

Specifically, we can test whether:

\[
\mathbf{X}_{135D}
\]

contains information associated with:

\[
|F_2|,
\qquad
\alpha_2,
\]

and the broader radial–angular representation.

This moves the study from **discovering raw geometric structure** to
**testing cross-representation correspondence**.

No semantic interpretation is required for this step.

# 🧪 CLO-SKET — RAW IMAGE RADIAL / ANGULAR GEOMETRY
## CELL 10 — F₂ AXIS ALIGNMENT + BOOTSTRAP ROBUSTNESS

---

# 1. Objective

Cell 9 established that the second angular Fourier component has a
strong and highly concentrated axial orientation.

The population mean two-fold axis was approximately:

\[
87.7^\circ.
\]

Cell 10 asks the next geometric question:

> **Is this two-fold axis aligned with the original image coordinate
> system, specifically the vertical axis, without imposing any
> rotation or alignment during preprocessing?**

The reference vertical axis is:

\[
\boxed{90^\circ}
\]

in the original image coordinate system.

The analysis therefore tests whether the observed \(F_2\) orientation
is merely concentrated in an arbitrary direction or is specifically
aligned with the source-image vertical axis.

---

# 2. Input Verification

Angular morphology:

\[
\boxed{2300\times72}
\]

Population:

\[
\boxed{2300}
\]

Angular bins:

\[
\boxed{72}
\]

No transformation of the angular representation was introduced for
this analysis.

In particular:

- no image rotation;
- no image straightening;
- no PCA-based orientation;
- no semantic labels used to define the reference axis.

The original image coordinate system remains unchanged.

---

# 3. F₂ Axis Orientation

The two-fold orientation is defined from the complex second Fourier
coefficient as:

\[
\alpha_2
=
-\frac{\arg(F_2)}{2}
\pmod{180^\circ}.
\]

Observed population statistics:

\[
\text{Mean axis}
=
87.6983^\circ
\]

\[
\text{Median axis}
=
87.3854^\circ.
\]

Thus the estimated population axis lies very close to the original
image vertical axis:

\[
90^\circ.
\]

The difference between the mean axis and vertical is:

\[
87.6983^\circ-90^\circ
=
-2.3017^\circ.
\]

Therefore:

\[
\boxed{
\text{mean signed deviation}
=
-2.302^\circ
}
\]

---

# 4. Deviation from the Image Vertical Axis

For each sketch, the axial deviation from the image vertical was
calculated.

Because the axis is axial,

\[
\alpha_2\equiv\alpha_2+180^\circ,
\]

the deviation is evaluated on the appropriate axial domain.

Observed:

\[
\boxed{
\text{Mean absolute deviation}
=
5.927^\circ
}
\]

\[
\boxed{
\text{Median absolute deviation}
=
3.358^\circ
}
\]

\[
\boxed{
Q_{90}
=
9.000^\circ
}
\]

The maximum deviation is:

\[
89.286^\circ.
\]

The large maximum is attributable to a small number of sketches
whose estimated \(F_2\) axis is poorly aligned with the dominant
population orientation.

The central distribution, however, is strongly concentrated near
the vertical axis.

---

# 5. Orientation Tolerance

The proportion of sketches lying within progressively larger
angular tolerances of the image vertical axis is:

| Tolerance | Fraction | Percentage |
|---|---:|---:|
| ±2° | 0.2970 | 29.70% |
| ±5° | 0.6809 | 68.09% |
| ±10° | 0.9122 | 91.22% |
| ±15° | 0.9543 | 95.43% |
| ±20° | 0.9670 | 96.70% |
| ±30° | 0.9730 | 97.30% |

The most informative result is:

\[
\boxed{
91.22\%
}
\]

of all 2300 sketches have their \(F_2\) axis within \(10^\circ\) of
the original image vertical axis.

Thus the alignment is not restricted to the population mean alone.

It is present across the overwhelming majority of individual
sketches.

---

# 6. Axial Alignment Statistic

Alignment with the vertical axis can also be expressed using axial
circular statistics.

The observed quantities are:

\[
C_{\text{vertical}}
=
0.936751
\]

\[
S_{\text{vertical}}
=
-0.083469
\]

with axial concentration:

\[
\boxed{
R_{\text{vertical}}
=
0.940462
}
\]

This is the same concentration magnitude established in Cell 9,
now expressed relative to the image vertical reference.

The result therefore confirms that the concentrated \(F_2\) axis is
specifically centered close to the image vertical direction.

---

# 7. F₂ Magnitude vs Axis Alignment

A potential concern is that strong \(F_2\) components might simply be
better estimated and therefore appear more aligned.

To investigate this, \(F_2\) magnitude was compared with absolute
axis deviation.

Pearson correlation:

\[
\boxed{
r=-0.320836
}
\]

Spearman correlation:

\[
\boxed{
\rho=-0.222597
}
\]

The relationship is therefore negative but not strong.

This suggests that stronger second-harmonic components tend to be
somewhat better aligned with the image vertical axis, but the
orientation concentration cannot be reduced to a simple deterministic
relationship between \(F_2\) magnitude and orientation.

---

# 8. Strong-\(F_2\) Subset

Cell 9 identified the 25th percentile of \(F_2\) magnitude as:

\[
\boxed{
|F_2|=0.190876
}
\]

Using this threshold gives:

\[
\boxed{
n=1725
}
\]

strong-\(F_2\) sketches.

For this subset:

\[
\text{Mean absolute deviation}
=
3.816^\circ
\]

\[
\text{Median absolute deviation}
=
3.067^\circ
\]

and:

\[
\boxed{
73.80\%
}
\]

are within \(5^\circ\) of the vertical axis.

More importantly:

\[
\boxed{
96.52\%
}
\]

are within \(10^\circ\).

Thus the stronger \(F_2\) components exhibit even tighter alignment
with the original image vertical axis.

---

# 9. Bootstrap Robustness

The population-level orientation was evaluated using bootstrap
resampling.

The bootstrap estimate of the mean-axis deviation was:

\[
\boxed{
-2.546^\circ
}
\]

with a 95% bootstrap interval:

\[
\boxed{
[-2.794^\circ,\,-2.301^\circ]
}
\]

The entire interval lies below zero.

Thus the observed small offset from \(90^\circ\) is stable under
resampling rather than being produced by a small number of sketches.

The population axis is consistently estimated slightly to the left
of the nominal vertical reference:

\[
\sim87.5^\circ-87.7^\circ.
\]

---

# 10. Category-Level Alignment

The same analysis was repeated separately within each Clo-SKET
category.

| Category | Mean \(|F_2|\) | Mean abs. deviation | Median abs. deviation | Within ±5° | Within ±10° |
|---|---:|---:|---:|---:|---:|
| Mermaid | 0.3418 | 2.95° | 2.52° | 87% | 100% |
| Straight | 0.4030 | 3.04° | 2.45° | 80% | 99% |
| Jumpsuit | 0.4098 | 3.13° | 2.86° | 82% | 100% |
| Dress | 0.3897 | 3.26° | 2.89° | 80% | 98% |
| Pencil | 0.3551 | 3.47° | 3.47° | 75% | 100% |
| Skinny | 0.4115 | 3.53° | 2.80° | 77% | 97% |
| Jacket | 0.2052 | 3.55° | 3.14° | 74% | 98% |
| Hoodie | 0.2330 | 3.56° | 3.14° | 78% | 99% |
| Circle | 0.2534 | 3.61° | 2.76° | 72% | 96% |
| Flare | 0.4089 | 3.67° | 3.06° | 71% | 97% |
| Vest | 0.3058 | 3.68° | 3.52° | 72% | 99% |
| Harem | 0.3300 | 3.84° | 3.49° | 71% | 96% |
| Shirt | 0.2308 | 3.89° | 3.21° | 72% | 95% |
| Sarong | 0.3734 | 4.43° | 3.10° | 60% | 91% |
| Tunic | 0.2620 | 4.52° | 3.26° | 65% | 96% |
| Mini | 0.2365 | 4.57° | 3.60° | 61% | 89% |
| T-shirt | 0.1678 | 4.85° | 3.52° | 70% | 90% |
| Cardigan | 0.2083 | 4.87° | 4.30° | 60% | 92% |
| Suit | 0.2223 | 5.03° | 3.96° | 58% | 89% |
| A-Line | 0.1880 | 5.54° | 3.46° | 67% | 84% |
| Wide-Leg | 0.1961 | 5.86° | 4.51° | 55% | 82% |
| Bermuda | 0.1302 | 14.54° | 4.46° | 51% | 70% |
| Blouse | 0.1003 | 36.96° | 20.97° | 28% | 41% |

---

# 11. Category-Level Pattern

Most categories show strong alignment with the image vertical axis.

For the majority:

\[
\text{mean absolute deviation}
\approx
3^\circ-6^\circ.
\]

Many categories also have:

\[
\text{within }10^\circ
\geq
90\%.
\]

The strongest alignment is observed for categories such as:

- Mermaid;
- Straight;
- Jumpsuit;
- Dress;
- Pencil;
- Skinny;
- Jacket;
- Hoodie.

However, the concentration is not equally strong for every category.

The most notable exceptions are:

### Bermuda

\[
\text{mean absolute deviation}=14.54^\circ
\]

\[
\text{within }10^\circ=70\%.
\]

### Blouse

\[
\text{mean absolute deviation}=36.96^\circ
\]

\[
\text{within }10^\circ=41\%.
\]

These categories also have comparatively weak mean \(F_2\)
magnitudes.

Therefore category-level orientation stability varies with the
strength and organization of the underlying second harmonic.

---

# 12. What Cell 10 Establishes

Cell 9 established:

\[
\boxed{
\text{strong and concentrated }F_2\text{ phase}
}
\]

Cell 10 establishes that this concentration is not merely around an
arbitrary population direction.

Instead:

\[
\boxed{
\alpha_2
\approx
90^\circ
}
\]

where \(90^\circ\) corresponds to the original image vertical axis.

The key quantitative findings are:

\[
\boxed{
\text{Mean axis}=87.70^\circ
}
\]

\[
\boxed{
\text{Mean absolute deviation}=5.93^\circ
}
\]

\[
\boxed{
91.22\%\text{ within }10^\circ
}
\]

\[
\boxed{
R_{\text{vertical}}=0.94046
}
\]

and, for strong-\(F_2\) sketches:

\[
\boxed{
96.52\%\text{ within }10^\circ.
}
\]

---

# 13. Important Scientific Interpretation

The raw angular morphology therefore contains a reproducible
two-fold component whose principal axis is strongly aligned with the
original image vertical direction.

This is notable because the alignment was **not imposed by the
analysis**.

The pipeline did not:

- rotate the images;
- straighten the garments;
- perform PCA orientation normalization;
- align images to a learned template;
- define the axis using category labels.

The orientation emerged from the Fourier phase of the raw
intensity-derived angular morphology.

Thus the current result is:

\[
\boxed{
\text{emergent image-coordinate axial organization}
}
\]

rather than an imposed normalization.

---

# 14. Important Limitation

The result should still be described carefully.

The analysis establishes alignment with the **source image vertical
axis**.

It does not yet establish why this alignment exists.

Possible explanations cannot be distinguished from Cell 10 alone.

For example, the result could reflect properties of:

- how the garments are represented in the source images;
- the drawing/canvas convention;
- garment orientation;
- dataset construction;
- or the morphology of the sketches themselves.

Therefore we should **not yet convert**

\[
\text{image vertical axis}
\]

into

\[
\text{semantic garment axis}.
\]

That interpretation requires additional evidence.

---

# 15. Scientific Status

### 🟢 CELL 10 — F₂ AXIS ALIGNMENT + ROBUSTNESS COMPLETE

Established:

- strong alignment of \(F_2\) with image vertical;
- individual-sketch orientation distribution;
- tolerance-based alignment;
- axial concentration;
- magnitude–orientation relationship;
- strong-\(F_2\) stability;
- bootstrap robustness;
- category-level consistency and exceptions.

The original raw TIFF coordinate system remains unchanged.

No rotation or orientation normalization has been applied.

No semantic interpretation has been introduced.

---

# 16. Updated Raw-Image Evidence Chain

The raw-image analysis now forms a progressively stronger chain:

\[
\boxed{
\text{Original grayscale TIFF}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{Intensity-weighted centroid}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{Angular morphology }A(\theta)
}
\]

\[
\downarrow
\]

\[
\boxed{
|F_2|>|F_1|
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{Population-wide second-harmonic dominance}
}
\]

\[
\downarrow
\]

\[
\boxed{
\arg(F_2)
\rightarrow
\alpha_2
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{Stable two-fold axis}
}
\]

\[
\downarrow
\]

\[
\boxed{
\alpha_2\approx90^\circ
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{alignment with original image vertical axis}
}
\]

This gives us a much stronger geometric characterization of the raw
Clo-SKET images than magnitude-only analysis.

---

# 17. Next Question

The next step is now naturally:

> **Does the strength of this two-fold angular structure depend on
> radial distance from the intensity-weighted centroid?**

In other words, instead of treating the angular profile as a single
72-bin vector, we can examine the joint structure:

\[
\boxed{
A(r,\theta)
}
\]

and ask whether:

\[
F_2(r)
\]

changes systematically across radius.

This is the beginning of the:

\[
\boxed{
\text{RADIAL × ANGULAR COUPLING}
}
\]

analysis.

The question is no longer merely:

> "Is there a two-fold angular structure?"

but:

> **"Where, radially, does that two-fold structure live?"**

That is the next genuinely informative geometric question.

# Cell 11 — Radial × Angular Coupling

## Objective

The previous analysis established that the raw CLO-SKET sketches exhibit a strong second angular harmonic, with the second harmonic exceeding the first harmonic in the vast majority of sketches. Its phase also showed a highly concentrated two-fold axis that was strongly aligned with the original image vertical axis.

The next question is whether this angular organization is distributed uniformly throughout the sketch or whether its strength and orientation vary systematically with radial distance from the intensity-weighted centroid.

To test this, the analysis moves from the marginal angular representation

\[
A(\theta)
\]

to the joint radial-angular mass field

\[
A(r,\theta).
\]

This preserves the spatial relationship between radial position and angular structure rather than treating the radial and angular profiles independently.

---

## Representation

The source remains the original grayscale TIFF image.

For each sketch, grayscale darkness is used as a continuous intensity weight. No thresholding, binarization, resizing, or PCA-based alignment is applied.

The intensity-weighted centroid provides the geometric reference point:

\[
C=(C_x,C_y).
\]

Each pixel is then represented in polar coordinates relative to this centroid:

\[
r=\sqrt{(x-C_x)^2+(y-C_y)^2},
\]

\[
\theta=\operatorname{atan2}(y-C_y,x-C_x).
\]

The resulting joint polar mass field is

\[
A(r,\theta),
\]

with 72 radial bins and 72 angular bins.

The joint polar representation is normalized so that the total mass of every sketch is conserved:

\[
\sum_{r,\theta} A(r,\theta)=1.
\]

Across all 2,300 sketches, the maximum deviation from unit mass was approximately

\[
2.22\times10^{-16},
\]

confirming numerical mass conservation.

---

## Radial Fourier Decomposition

Rather than multiplying the marginal radial and angular profiles, the Fourier transform is applied directly to the angular dimension of the joint field:

\[
A(r,\theta)
\rightarrow
F_k(r).
\]

For each radial position, the angular field is decomposed into Fourier harmonics:

\[
F_k(r)=
\sum_{\theta}
A(r,\theta)e^{-ik\theta}.
\]

The primary quantities examined are

\[
|F_1(r)|
\]

and

\[
|F_2(r)|.
\]

The first harmonic represents first-order directional organization, while the second harmonic represents two-fold angular organization.

The analysis therefore asks whether the previously observed second-harmonic structure persists equally across radial distance.

---

## Radial Distribution of Harmonic Strength

The magnitude of the second harmonic is not spatially uniform.

The population-level second harmonic reaches its maximum at approximately

\[
r=0.299.
\]

At this radial position,

\[
|F_2|=0.01807,
\]

while

\[
|F_1|=0.01230.
\]

Thus,

\[
\frac{|F_2|}{|F_1|}
\approx 2.70.
\]

The strongest second-harmonic organization therefore occurs in an intermediate radial region rather than directly at the centroid or at the outermost image extent.

This indicates that the observed two-fold angular structure has a radial organization rather than being uniformly distributed throughout the sketch.

---

## Radial Prevalence of Second-Harmonic Dominance

The fraction of sketches satisfying

\[
|F_2(r)|>|F_1(r)|
\]

provides a more stable measure of radial second-harmonic dominance than the raw ratio alone.

The prevalence of second-harmonic dominance increases from the centroid toward the intermediate radial region.

It exceeds 50% at approximately

\[
r\approx0.05
\]

and reaches approximately 0.64–0.65 around

\[
r\approx0.25-0.30.
\]

Beyond the intermediate region, the prevalence gradually decreases and becomes substantially lower toward the outer radial boundary.

Thus, the second harmonic is most consistently dominant at intermediate radial distances.

---

## Radial F₂ Phase and Axis Orientation

The phase of the second harmonic provides an estimate of its two-fold axis orientation:

\[
\alpha_2(r)
=
-\frac{\arg(F_2(r))}{2}
\pmod{180^\circ}.
\]

The corresponding axial concentration is measured using

\[
R_2(r)
=
\sqrt{
\left[\operatorname{mean}\cos(2\alpha_2)\right]^2+
\left[\operatorname{mean}\sin(2\alpha_2)\right]^2
}.
\]

The radial analysis shows that the two-fold axis becomes strongly concentrated through the central and intermediate radial region.

Axial concentration reaches approximately

\[
R_2\approx0.90
\]

over a broad interval around

\[
r\approx0.30-0.40.
\]

Within this region, the estimated two-fold axis remains close to the original image vertical axis.

This indicates that the second-harmonic structure is not only stronger at particular radial distances but also maintains a relatively coherent orientation across those distances.

---

## Interpretation

The radial-angular analysis therefore provides evidence for three related geometric properties:

1. **Second-harmonic dominance**

   \[
   |F_2|>|F_1|
   \]

   is prevalent across a substantial radial region.

2. **Radial localization**

   The magnitude of \(F_2(r)\) reaches its population maximum near

   \[
   r\approx0.30.
   \]

3. **Directional coherence**

   The phase-derived two-fold axis becomes highly concentrated in the same intermediate radial region.

Together, these observations indicate that the two-fold angular organization detected in the raw CLO-SKET images is not spatially uniform. It has a measurable radial profile and a relatively stable orientation through the central-to-intermediate radial extent.

---

## Category-Level Radial Variation

The radial location of maximum second-harmonic magnitude also varies across CLO-SKET categories.

The mean peak radial positions range from approximately

\[
r\approx0.23
\]

for Mini and T-shirt sketches to approximately

\[
r\approx0.47
\]

for Wide-Leg sketches.

Examples include:

| Category | Mean peak \(F_2\) radius |
|---|---:|
| Mini | 0.227 |
| T-shirt | 0.232 |
| Sarong | 0.272 |
| Shirt | 0.281 |
| Vest | 0.297 |
| Hoodie | 0.300 |
| Pencil | 0.318 |
| Tunic | 0.344 |
| Skinny | 0.366 |
| Straight | 0.371 |
| Mermaid | 0.378 |
| Flare | 0.399 |
| Dress | 0.401 |
| Blouse | 0.411 |
| A-Line | 0.429 |
| Jumpsuit | 0.434 |
| Wide-Leg | 0.474 |

These differences are descriptive geometric observations. They do not, by themselves, establish that the radial harmonic structure is semantic, perceptual, or category-defining.

---

## Numerical Stability Consideration

The ratio

\[
\frac{|F_2(r)|}{|F_1(r)|}
\]

becomes numerically unstable at large radial distances because the first-harmonic magnitude approaches zero.

Consequently, extremely large ratio values observed in the outer radial bins should not be interpreted as evidence of extreme second-harmonic dominance.

The more stable quantities for interpretation are therefore:

- absolute harmonic magnitude,
- median harmonic ratios,
- the fraction of sketches satisfying \(F_2>F_1\),
- and axial concentration.

The outer radial region also contains progressively weaker harmonic signal, making phase-derived orientations increasingly unstable.

---

## Conclusion

The radial-angular analysis extends the previous global Fourier result by showing that the observed second-harmonic organization has a spatial structure.

The raw CLO-SKET representation therefore exhibits:

\[
\boxed{
A(r,\theta)
\rightarrow
F_2(r)
}
\]

with the strongest and most directionally coherent second-harmonic organization occurring at intermediate radial distances from the intensity-weighted centroid.

The result remains strictly geometric.

No claim is made at this stage regarding:

- semantic structure,
- garment grammar,
- garment-category meaning,
- anatomical correspondence,
- or perceptual interpretation.

The analysis establishes only that the raw grayscale sketch field contains a **radially organized and directionally coherent two-fold angular component**.

---

### Key Result

\[
\boxed{
\text{Raw CLO-SKET sketches exhibit radially localized,
directionally coherent second-harmonic angular organization.}
}
\]

### Representation Status

- Original grayscale TIFF: **preserved**
- Continuous intensity weighting: **preserved**
- Intensity-weighted centroid: **used**
- Polar representation \(A(r,\theta)\): **used**
- Radial-angular Fourier decomposition: **performed**
- Mass conservation: **verified**
- Thresholding: **not used**
- Binarization: **not used**
- Resizing: **not used**
- PCA alignment: **not used**
- Semantic labels for coordinate definition: **not used**

### Next Question

The next analysis should determine whether the radial-angular structure contains reproducible relationships between radial morphology and angular organization beyond the population-level harmonic pattern.

# Cell 11R — Conditional Radial × Angular Fourier Structure

## Objective

The previous analysis established that the raw CLO-SKET sketches contain a strong second angular harmonic and that its phase is highly aligned with the original image vertical axis.

The next question is more specific:

> **At what radial distances from the intensity-weighted centroid does the two-fold angular organization emerge, strengthen, and remain directionally coherent?**

To answer this, the analysis preserves the joint radial-angular structure rather than averaging over radius.

For each sketch, the raw grayscale intensity field is represented as a radial × angular mass distribution:

\[
W(r,\theta).
\]

The angular distribution is then conditioned on radial distance:

\[
P(\theta\mid r).
\]

A circular Fourier transform is applied independently within each radial shell, producing radial functions

\[
F_1(r),\quad F_2(r),\quad \ldots
\]

This allows angular organization to be examined as a function of distance from the centroid.

---

## Representation

The analysis starts directly from the original grayscale TIFF images.

\[
\text{Original grayscale TIFF}
\]

\[
\downarrow
\]

\[
\text{continuous darkness / ink weight}
\]

\[
\downarrow
\]

\[
\text{intensity-weighted centroid}
\]

\[
\downarrow
\]

\[
\text{isotropic coordinates}
\]

\[
\downarrow
\]

\[
W(r,\theta)
\]

\[
\downarrow
\]

\[
P(\theta\mid r)
\]

\[
\downarrow
\]

\[
\text{circular Fourier transform}
\]

\[
\downarrow
\]

\[
F_1(r),F_2(r),\text{ higher harmonics}
\]

The dataset contains:

- 2,300 sketches
- 72 radial bins
- 72 angular bins

The radial × angular mass was recovered for all 2,300 sketches.

---

## Numerical Validation

### Radial × Angular Mass Conservation

The complete radial × angular representation satisfies exact mass conservation.

- Maximum absolute mass error: **0.0**
- Mean absolute mass error: **0.0**
- Maximum relative mass error: **0.0**

Thus,

\[
\sum_{r,\theta}W(r,\theta)=1
\]

was preserved numerically for every sketch.

### Radial Normalization

The maximum radial normalization error was

\[
2.22\times10^{-16}.
\]

### Conditional Angular Normalization

Of the

\[
2300\times72=165600
\]

radial shells, 165,363 contained non-zero mass.

For all non-empty shells:

\[
0.9999999999999996
\leq
\sum_\theta P(\theta\mid r)
\leq
1.0000000000000004.
\]

The maximum conditional normalization error was

\[
4.44\times10^{-16}.
\]

Thus each non-empty radial shell defines a properly normalized angular distribution.

### Fourier Validation

The conditional Fourier transform has shape

\[
(2300,72,37),
\]

corresponding to 37 real Fourier harmonics.

Parseval energy conservation was also verified:

- Maximum absolute energy error:
  \[
  7.77\times10^{-16}
  \]

- Mean absolute energy error:
  \[
  1.72\times10^{-17}
  \]

Therefore the conditional Fourier decomposition is numerically consistent with the underlying angular distributions.

---

# Conditional Radial Fourier Structure

The principal quantities measured at each radial position are:

1. radial shell mass,
2. mean first-harmonic magnitude \(|F_1(r)|\),
3. mean second-harmonic magnitude \(|F_2(r)|\),
4. fraction of sketches satisfying
   \[
   |F_2(r)|>|F_1(r)|,
   \]
5. axial resultant \(R_2(r)\),
6. mean two-fold axis orientation.

---

## Emergence of Second-Harmonic Dominance

The conditional analysis shows that second-harmonic dominance is not uniform across radial distance.

Near the centroid, the second harmonic is initially weaker than the first.

For example:

\[
r=0.0069:
\qquad
|F_1|=0.291,\quad |F_2|=0.220
\]

with only

\[
P(|F_2|>|F_1|)=0.328.
\]

As radial distance increases, the second harmonic becomes progressively more prevalent.

At

\[
r=0.0486,
\]

the fraction of sketches with second-harmonic dominance reaches

\[
0.513.
\]

It continues to increase through the early-to-intermediate radial region.

At

\[
r=0.0764,
\]

\[
P(|F_2|>|F_1|)=0.557.
\]

At

\[
r=0.1042,
\]

the fraction reaches

\[
0.564.
\]

The dominance then temporarily weakens around

\[
r\approx0.15-0.20,
\]

before increasing again.

---

## Intermediate-Radius Second-Harmonic Structure

A second and substantially stronger region of second-harmonic organization appears in the intermediate-to-outer radial range.

At

\[
r=0.2569,
\]

the dominance fraction is

\[
0.626.
\]

At

\[
r=0.2986,
\]

it increases to

\[
0.646.
\]

The maximum in this central/intermediate region occurs around

\[
r=0.3125,
\]

where

\[
P(|F_2|>|F_1|)
=
0.650.
\]

The corresponding Fourier magnitudes are

\[
|F_1|=0.271,
\]

\[
|F_2|=0.382.
\]

Thus the conditional second harmonic is substantially stronger than the first.

---

## Strongest Conditional F₂ Dominance

The strongest second-harmonic dominance occurs further outward.

Beginning around

\[
r\approx0.56,
\]

the conditional second-harmonic dominance rises sharply.

At

\[
r=0.5625:
\]

\[
P(|F_2|>|F_1|)=0.643.
\]

At

\[
r=0.5764:
\]

\[
P(|F_2|>|F_1|)=0.766.
\]

At

\[
r=0.5903:
\]

\[
P(|F_2|>|F_1|)=0.829.
\]

At

\[
r=0.6042:
\]

\[
P(|F_2|>|F_1|)=0.862.
\]

The maximum occurs around

\[
r=0.6319,
\]

where

\[
P(|F_2|>|F_1|)
=
0.878.
\]

At this radius,

\[
|F_1|=0.110,
\]

while

\[
|F_2|=0.377.
\]

Thus the conditional angular structure is strongly dominated by the second harmonic in this radial region.

---

## Outer-Radius Behaviour

Beyond approximately

\[
r\approx0.70,
\]

the second harmonic remains larger than the first in most sketches, but the interpretation changes because the radial shell mass becomes progressively smaller.

For example:

\[
r=0.7014:
\qquad
P(F_2>F_1)=0.808
\]

and

\[
r=0.7569:
\qquad
P(F_2>F_1)=0.752.
\]

At still larger radii, the dominance fraction decreases:

\[
r=0.8264:
\qquad
0.547
\]

\[
r=0.8542:
\qquad
0.445
\]

\[
r=0.9097:
\qquad
0.250
\]

and eventually approaches zero toward the outermost shell.

The decrease therefore occurs alongside rapidly declining radial mass.

---

# Radial F₂ Axial Concentration

The magnitude of \(F_2(r)\) tells us how strong the two-fold component is.

Its phase tells us how that two-fold structure is oriented.

To measure the stability of that orientation across sketches, the axial resultant is calculated as

\[
R_2(r)
=
\sqrt{
\left[
\operatorname{mean}\cos(2\alpha_2)
\right]^2
+
\left[
\operatorname{mean}\sin(2\alpha_2)
\right]^2
}.
\]

where

\[
\alpha_2
=
-\frac{\arg(F_2)}{2}
\pmod{180^\circ}.
\]

---

## Increasing Orientation Coherence

Near the centroid, the F₂ axis is poorly concentrated.

At

\[
r=0.0069,
\]

\[
R_2=0.110.
\]

As radial distance increases, axial concentration strengthens.

At

\[
r=0.2431,
\]

\[
R_2=0.520.
\]

At

\[
r=0.3264,
\]

\[
R_2=0.711.
\]

At

\[
r=0.3542,
\]

\[
R_2=0.726.
\]

At

\[
r=0.3819,
\]

\[
R_2=0.736.
\]

Thus, through the intermediate radial region, the second-harmonic axis becomes increasingly coherent across sketches.

---

## Strongest Axial Concentration

A second major increase occurs in the outer-intermediate region.

At

\[
r=0.5625,
\]

\[
R_2=0.835.
\]

At

\[
r=0.5903,
\]

\[
R_2=0.849.
\]

At

\[
r=0.6319,
\]

\[
R_2=0.804.
\]

The axial concentration subsequently becomes even stronger around

\[
r\approx0.70-0.80.
\]

For example:

\[
r=0.7153:
\qquad
R_2=0.914
\]

and

\[
r=0.7292:
\qquad
R_2=0.912.
\]

The concentration remains approximately

\[
R_2\approx0.90
\]

through much of this region.

This indicates that where the second-harmonic component is strong, its orientation is also highly coherent across the population.

---

# Conditional F₂ Axis Orientation

The mean conditional F₂ axis remains remarkably stable.

Across the well-populated radial region, the mean axis is generally close to

\[
87^\circ-88^\circ.
\]

Examples include:

\[
r=0.2847:
\qquad
86.88^\circ
\]

\[
r=0.3125:
\qquad
86.89^\circ
\]

\[
r=0.3542:
\qquad
87.51^\circ
\]

\[
r=0.6042:
\qquad
87.13^\circ
\]

\[
r=0.7153:
\qquad
87.20^\circ
\]

\[
r=0.7986:
\qquad
87.73^\circ.
\]

The orientation therefore remains close to the original image vertical axis

\[
90^\circ
\]

over a broad radial range.

The unstable orientations very close to the centroid should not be overinterpreted because the corresponding angular Fourier signal is weak and the axial concentration is low.

---

# What the Conditional Analysis Adds

The previous marginal analysis established that the raw sketches contain a strong second harmonic.

The present conditional analysis adds a spatial dimension.

Instead of asking only

\[
|F_2|>|F_1|?
\]

we can now ask

\[
|F_2(r)|>|F_1(r)|?
\]

and

\[
R_2(r)=?
\]

for each radial shell.

The result is a structured radial pattern:

\[
\boxed{
\text{weak / unstable near centroid}
\rightarrow
\text{emerging F}_2
\rightarrow
\text{strong intermediate F}_2
\rightarrow
\text{highly coherent outer-intermediate F}_2
\rightarrow
\text{weakening toward boundary}
}
\]

The two-fold axis, meanwhile, remains close to the image vertical direction through the region where the signal is strong.

---

# Important Statistical Choice

A direct radial mean of

\[
\frac{|F_2|}{|F_1|}
\]

is **not used** as the primary measure.

The reason is that \(|F_1|\) can approach zero, producing arbitrarily large and numerically unstable ratios.

Instead, conditional dominance is defined as

\[
\boxed{
P(|F_2|>|F_1|\mid r)
}
\]

which remains bounded between 0 and 1.

This makes the radial dominance curve interpretable even when the first harmonic becomes very small.

---

# Boundary Condition

The normalized radial coordinate explicitly assigns

\[
r_{\mathrm{norm}}=1
\]

to the final radial shell.

Therefore the outermost radial point represents the maximum radial extent of the normalized coordinate system rather than an extrapolation beyond the observed image support.

---

# Interpretation

The conditional radial × angular Fourier analysis provides evidence that the second-harmonic organization of raw CLO-SKET sketches is **spatially structured**.

Three observations are particularly important:

### 1. F₂ dominance varies systematically with radius

Second-harmonic dominance is weak near the centroid, becomes prevalent through intermediate regions, reaches a strong maximum around

\[
r\approx0.63,
\]

and decreases again toward the outermost shell.

### 2. F₂ orientation becomes highly coherent

The axial resultant increases from weak concentration near the centroid to values around

\[
R_2\approx0.9
\]

through much of the outer-intermediate radial region.

### 3. The dominant axis remains approximately vertical

The conditional mean F₂ axis remains close to

\[
87^\circ-88^\circ,
\]

despite no rotation or PCA alignment being applied.

Thus the radial structure is expressed relative to the **original image coordinate system**.

---

# What This Does NOT Establish

This analysis remains geometric.

It does **not** establish:

- bilateral symmetry as a semantic property,
- garment-category meaning,
- garment grammar,
- perceptual salience,
- anatomical correspondence,
- design intent,
- or a learned semantic representation.

The observed two-fold structure could arise from the geometry and orientation of the sketch population itself.

Those interpretations require separate tests.

---

# Representation Integrity

The following were preserved:

- Original grayscale TIFF
- Continuous darkness / ink weighting
- Intensity-weighted centroid
- Isotropic coordinate system
- Radial × angular mass
- Conditional angular distributions
- Circular Fourier representation

The following were **not** used:

- Thresholding
- Binarization
- Morphology resizing
- Rotation
- PCA alignment
- Clustering
- Semantic labels

---

# Conclusion

The conditional radial × angular Fourier analysis demonstrates that the second-harmonic organization observed in raw CLO-SKET sketches is not merely a population-level angular effect.

It has a measurable **radial organization**.

The strongest and most reproducible two-fold organization occurs away from the centroid, particularly in the intermediate-to-outer radial region, where:

\[
P(|F_2|>|F_1|\mid r)
\]

becomes very high and

\[
R_2(r)
\]

approaches strong axial concentration.

At the same time, the estimated two-fold axis remains close to the original image vertical axis.

Therefore:

\[
\boxed{
W(r,\theta)
\rightarrow
P(\theta\mid r)
\rightarrow
F_2(r)
}
\]

reveals a **radially structured, directionally coherent second-harmonic component in the raw grayscale CLO-SKET sketches**.

This remains a geometric finding, with no semantic interpretation assigned.

---

## Key Result

\[
\boxed{
\text{Two-fold angular organization is strongest and most coherent
at specific radial distances rather than being uniformly distributed.}
}
\]

The next question is whether this radial-angular organization represents a reproducible relationship between **radial morphology and angular morphology**, rather than simply two correlated marginal descriptions of the same image field.

# Cell 12 — Statistical Audit of Radial × Angular Coupling

## Objective

Cell 11R established that the conditional angular Fourier structure varies across radial distance.

The next question is:

> **Does angular organization vary systematically with radial distance from the intensity-weighted centroid, beyond what would be expected if radial organization were absent?**

This cell performs a statistical audit of the radial × angular relationship.

The analysis evaluates the radial behaviour of:

\[
|F_1(r)|
\]

\[
|F_2(r)|
\]

\[
|F_2(r)|-|F_1(r)|
\]

\[
P(|F_2|>|F_1|\mid r)
\]

and

\[
R_2(r).
\]

Two complementary approaches are used:

1. **descriptive radial trend statistics**
2. **within-sketch radial permutation testing**

Bootstrap confidence intervals are additionally used to assess robustness of the observed radial heterogeneity.

---

# Input Verification

The conditional representation contains:

- Conditional angular distributions:
  \[
  (2300,72,72)
  \]

- Conditional Fourier coefficients:
  \[
  (2300,72,37)
  \]

- Radial \(F_1\) magnitudes:
  \[
  (2300,72)
  \]

- Radial \(F_2\) magnitudes:
  \[
  (2300,72)
  \]

- Non-empty radial-shell mask:
  \[
  (2300,72)
  \]

- Radial centers:
  \[
  (72,)
  \]

All inputs were verified.

---

# Conditional Angular Normalization

There are

\[
165363
\]

valid radial shells across the dataset.

The conditional angular distributions satisfy:

\[
\sum_\theta P(\theta\mid r)=1
\]

to numerical precision.

Maximum normalization error:

\[
4.44\times10^{-16}.
\]

Mean normalization error:

\[
1.72\times10^{-17}.
\]

Therefore the conditional angular profiles are properly normalized before statistical analysis.

---

# Fourier Magnitude Verification

Across the radial × angular representation:

\[
\text{mean }|F_1|=0.005192
\]

\[
\text{mean }|F_2|=0.006393
\]

while the corresponding medians are:

\[
\text{median }|F_1|=0.001000
\]

\[
\text{median }|F_2|=0.000926.
\]

The means are larger than the medians because Fourier magnitude varies substantially across radial shells.

The Fourier magnitudes were verified before proceeding to the radial statistical analysis.

---

# Descriptive Radial Trend Audit

Spearman rank correlations were calculated between radial position and each radial statistic.

### First harmonic

\[
\rho_{\mathrm{Spearman}}(|F_1|,r)
=
-0.827191
\]

### Second harmonic

\[
\rho_{\mathrm{Spearman}}(|F_2|,r)
=
-0.793009
\]

### Difference between harmonics

\[
\rho_{\mathrm{Spearman}}
(|F_2|-|F_1|,r)
=
-0.424047
\]

### F₂ dominance

\[
\rho_{\mathrm{Spearman}}
\left(
P(|F_2|>|F_1|\mid r),r
\right)
=
-0.848858
\]

### Axial concentration

\[
\rho_{\mathrm{Spearman}}(R_2,r)
=
0.772236.
\]

These statistics describe broad radial trends.

However, they are **not treated as the primary inferential evidence**.

---

# Why Correlation Is Not the Primary Test

The radial curves are visibly non-monotonic.

For example, \(F_2\) rises through the inner region, reaches a strong region, decreases substantially, and later exhibits different behaviour toward the outer boundary.

Therefore, a simple correlation with radius cannot adequately characterize the structure.

A strong radial relationship does not need to be monotonic.

The appropriate question is instead:

> **Is the observed radial heterogeneity larger than would be expected if radial positions were exchangeable within each sketch?**

For this reason, the within-sketch radial permutation test is the primary inferential test.

---

# Observed Radial Heterogeneity

The observed variance across radial positions was calculated for four quantities.

### Mean F₂ radial profile

\[
\operatorname{Var}(\overline{F_2(r)})
=
3.76199727\times10^{-5}
\]

### Mean F₂ − F₁ profile

\[
\operatorname{Var}
\left(
\overline{F_2(r)-F_1(r)}
\right)
=
3.34149021\times10^{-6}
\]

### F₂ dominance profile

\[
\operatorname{Var}
\left(
P(|F_2|>|F_1|\mid r)
\right)
=
0.035437
\]

### Axial concentration profile

\[
\operatorname{Var}(R_2(r))
=
0.0534736.
\]

These quantify how strongly the angular Fourier structure changes across radial position.

---

# Within-Sketch Radial Permutation Null

A radial permutation null was constructed by disrupting the correspondence between radial position and the observed conditional Fourier structure **within each sketch**.

The purpose is to preserve the sketch-level data while removing the specific radial ordering.

The observed radial heterogeneity is then compared against the distribution obtained under these permutations.

A total of:

\[
500
\]

permutations were performed.

---

# Permutation Result — F₂ Radial Variance

Observed:

\[
3.76199727\times10^{-5}
\]

Null mean:

\[
4.81113089\times10^{-8}
\]

Null 95th percentile:

\[
6.23087391\times10^{-8}
\]

Empirical permutation p-value:

\[
p=0.001996.
\]

The observed radial variance is therefore vastly larger than the permutation null distribution.

---

# Permutation Result — F₂ − F₁

Observed:

\[
3.34149021\times10^{-6}
\]

Null mean:

\[
1.87332703\times10^{-8}
\]

Null 95th percentile:

\[
2.36929229\times10^{-8}
\]

Empirical:

\[
p=0.001996.
\]

Thus the radial variation in the relative strength of the second and first harmonics is also substantially larger than expected under the radial permutation null.

---

# Permutation Result — F₂ Dominance

Observed radial variance:

\[
0.035437.
\]

Null mean:

\[
9.46\times10^{-5}.
\]

Null 95th percentile:

\[
1.22\times10^{-4}.
\]

Empirical:

\[
p=0.001996.
\]

Therefore:

\[
P(|F_2|>|F_1|\mid r)
\]

shows strong radial heterogeneity that is not explained by the permutation null.

---

# Permutation Result — Axial Concentration

Observed:

\[
\operatorname{Var}(R_2(r))
=
0.0534736.
\]

Null mean:

\[
1.816\times10^{-4}.
\]

Null 95th percentile:

\[
2.309\times10^{-4}.
\]

Empirical:

\[
p=0.001996.
\]

Thus the radial variation in two-fold axial concentration is also substantially greater than expected under the null.

---

# Bootstrap Robustness

Bootstrap confidence intervals were calculated for the observed radial heterogeneity statistics.

### F₂ radial variance

\[
95\%\ CI
=
[3.61449\times10^{-5},
3.90876\times10^{-5}]
\]

### F₂ − F₁ radial variance

\[
95\%\ CI
=
[2.99688\times10^{-6},
3.74399\times10^{-6}]
\]

### F₂ dominance variance

\[
95\%\ CI
=
[0.0341411,
0.0369738].
\]

The bootstrap intervals are narrow relative to the observed effects, indicating that the radial heterogeneity is stable under resampling.

---

# Radial Structure

The detailed radial profile reveals several distinct regimes.

## Inner region

Very close to the centroid, F₂ is initially weaker than F₁.

For example:

\[
r=0.5:
\quad
|F_1|=0.001084,
\quad
|F_2|=0.000833
\]

with

\[
P(|F_2|>|F_1|)=0.194.
\]

The axial concentration is also weak:

\[
R_2=0.128.
\]

Thus the innermost region does not show a strongly coherent two-fold component.

---

## Emergence of F₂ dominance

Moving outward, F₂ becomes progressively stronger relative to F₁.

At:

\[
r=3.5,
\]

\[
P(|F_2|>|F_1|)=0.504.
\]

At:

\[
r=6.5,
\]

\[
P(|F_2|>|F_1|)=0.587.
\]

At:

\[
r=17.5,
\]

\[
P(|F_2|>|F_1|)=0.636.
\]

At:

\[
r=19.5,
\]

the dominance reaches:

\[
P(|F_2|>|F_1|)
=
0.648.
\]

The associated axial concentration is:

\[
R_2=0.600.
\]

---

# Peak Intermediate F₂ Dominance

The strongest dominance occurs around the intermediate radial region.

At:

\[
r=20.5,
\]

\[
|F_1|=0.012726
\]

and

\[
|F_2|=0.017887.
\]

The difference is:

\[
|F_2|-|F_1|
=
0.005161.
\]

The F₂ dominance fraction is:

\[
0.640.
\]

The axial concentration is:

\[
R_2=0.639.
\]

The F₂ dominance remains elevated through approximately

\[
r\approx17-27.
\]

---

# Transition Region

After the intermediate maximum, F₂ dominance decreases.

For example:

\[
r=27.5:
\quad
P(F_2>F_1)=0.513
\]

and

\[
r=30.5:
\quad
P(F_2>F_1)=0.456.
\]

By:

\[
r=34.5,
\]

the dominance has fallen to

\[
0.402.
\]

Thus the radial relationship is clearly **not monotonic**.

---

# Outer Region

Beyond approximately

\[
r\approx40,
\]

both Fourier magnitudes become small.

For example:

\[
r=40.5:
\]

\[
|F_1|=0.003190,
\qquad
|F_2|=0.003446.
\]

The F₂ dominance fraction is only:

\[
0.323.
\]

At:

\[
r=50.5,
\]

it falls to:

\[
0.279.
\]

At:

\[
r=60.5,
\]

it is:

\[
0.157.
\]

By the outermost region:

\[
r=71.5,
\]

the dominance fraction is only:

\[
0.017.
\]

The Fourier magnitudes themselves have also approached zero.

---

# Radial Evolution of Axial Concentration

The behaviour of \(R_2(r)\) is particularly interesting.

It begins very low near the centroid:

\[
R_2(0.5)=0.128.
\]

It increases through the intermediate region:

\[
R_2(20.5)=0.639
\]

and

\[
R_2(25.5)=0.727.
\]

It later decreases temporarily before increasing strongly again.

At:

\[
r=40.5,
\]

\[
R_2=0.831.
\]

At:

\[
r=41.5,
\]

\[
R_2=0.844.
\]

The strongest axial concentration occurs around the outer-intermediate region.

At:

\[
r=51.5,
\]

\[
R_2=0.906.
\]

It remains close to

\[
R_2\approx0.9
\]

through much of the following region.

For example:

\[
R_2(53.5)=0.902
\]

\[
R_2(57.5)=0.887
\]

\[
R_2(60.5)=0.874.
\]

Only toward the extreme outer boundary does the concentration fall substantially.

---

# Axis Orientation

The conditional F₂ axis remains close to the image vertical direction through most of the meaningful radial range.

Examples include:

\[
r=20.5:
\quad
86.85^\circ
\]

\[
r=25.5:
\quad
87.51^\circ
\]

\[
r=40.5:
\quad
86.99^\circ
\]

\[
r=51.5:
\quad
87.23^\circ
\]

\[
r=60.5:
\quad
89.01^\circ.
\]

The extreme outer and inner shells should be interpreted cautiously because the corresponding Fourier magnitudes and/or concentration are weak.

---

# What the Permutation Test Establishes

The most important result of Cell 12 is not simply that some radial curves correlate with radius.

The stronger result is:

\[
\boxed{
\text{Observed radial heterogeneity}
\gg
\text{radial permutation null}
}
\]

for all four audited measures:

\[
|F_2(r)|
\]

\[
|F_2(r)|-|F_1(r)|
\]

\[
P(|F_2|>|F_1|\mid r)
\]

and

\[
R_2(r).
\]

All four permutation tests produced:

\[
p=0.001996.
\]

The observed values also lie far beyond the null 95th percentiles.

Therefore, the radial variation cannot be adequately described as random radial ordering under the tested permutation null.

---

# Why This Is Stronger Than the Previous Cell

Cell 11R demonstrated:

> the angular Fourier structure changes with radial position.

Cell 12 adds:

> **the observed radial heterogeneity is statistically distinguishable from a within-sketch radial permutation null.**

This is an important methodological progression.

The evidence chain is now:

\[
\text{raw grayscale TIFF}
\]

\[
\downarrow
\]

\[
\text{intensity-weighted centroid}
\]

\[
\downarrow
\]

\[
W(r,\theta)
\]

\[
\downarrow
\]

\[
P(\theta\mid r)
\]

\[
\downarrow
\]

\[
F_1(r),F_2(r)
\]

\[
\downarrow
\]

\[
\text{radial heterogeneity}
\]

\[
\downarrow
\]

\[
\text{permutation test}
\]

\[
\boxed{
\text{statistically supported radial × angular coupling}
}
\]

within the tested null framework.

---

# Important Statistical Interpretation

The permutation result should be described carefully.

It establishes evidence for **radial heterogeneity of the conditional angular Fourier structure relative to the specified within-sketch permutation null**.

It does **not** by itself establish:

- semantic structure,
- garment grammar,
- category meaning,
- perceptual organization,
- anatomical correspondence,
- design intent,
- or bilateral symmetry.

The result remains geometric.

---

# Important Methodological Choices

The analysis deliberately avoids the unstable ratio

\[
\frac{|F_2|}{|F_1|}
\]

as a primary radial statistic because \(F_1\) can approach zero.

Instead, F₂ dominance is represented as:

\[
\boxed{
P(|F_2|>|F_1|\mid r)
}
\]

which is bounded:

\[
0\leq P\leq1.
\]

The radial curves are also **not assumed to be monotonic**.

Consequently, the permutation-based radial heterogeneity statistic is more appropriate than relying solely on a simple correlation with radius.

---

# Representation Integrity

The analysis remains entirely within the raw-image geometric representation.

Used:

- Original grayscale TIFF
- Continuous ink/darkness weighting
- Intensity-weighted centroid
- Isotropic coordinates
- Radial × angular mass
- Conditional angular distributions
- Circular Fourier transform
- Radial Fourier statistics
- Permutation testing
- Bootstrap resampling

Not used:

- F₂/F₁ ratio
- Thresholding
- Binarization
- Resizing
- Rotation
- PCA
- Clustering
- Semantic labels

---

# Conclusion

Cell 12 provides the statistical audit for the radial × angular relationship.

The observed conditional Fourier structure varies substantially across radial distance, and this radial heterogeneity is highly inconsistent with the within-sketch radial permutation null.

The strongest evidence is obtained for:

\[
|F_2(r)|
\]

\[
|F_2(r)|-|F_1(r)|
\]

\[
P(|F_2|>|F_1|\mid r)
\]

and

\[
R_2(r),
\]

all of which show permutation-test evidence of radial heterogeneity with

\[
p=0.001996.
\]

The important geometric finding is therefore:

\[
\boxed{
\text{Angular organization is not radially uniform.}
}
\]

More specifically:

\[
\boxed{
\text{the strength and coherence of the two-fold angular component
change systematically across radial distance.}
}
\]

The result is supported by both permutation inference and bootstrap robustness.

No semantic interpretation is made at this stage.

---

## Final Evidence Chain

\[
\boxed{
\text{Raw TIFF}
\rightarrow
\text{isotropic physical coordinates}
\rightarrow
\text{intensity centroid}
\rightarrow
W(r,\theta)
\rightarrow
P(\theta|r)
\rightarrow
F_1(r),F_2(r)
\rightarrow
\text{radial heterogeneity}
\rightarrow
\text{permutation audit}
}
\]

### Established so far

1. **A strong second angular harmonic exists in the raw sketches.**
2. **Its axis is strongly aligned with the original image vertical direction.**
3. **Its strength and axial concentration vary with radial distance.**
4. **That radial heterogeneity is statistically stronger than the tested permutation null.**
5. **The result survives bootstrap resampling.**

### Still NOT established

\[
\boxed{
\text{No semantic meaning has yet been assigned to this geometry.}
}
\]

The next stage should therefore ask whether this statistically established radial × angular organization is **related to reproducible morphological structure across sketches**, without jumping prematurely to semantic/category claims.

# 🧪 CLO-SKET — RAW IMAGE RADIAL / ANGULAR GEOMETRY
## CELL 13 — RADIAL COUPLING EFFECT LOCALIZATION AUDIT

---

## Objective

Cell 12 established statistical evidence that the conditional angular Fourier structure varies across radial distance.

Cell 13 addresses the next question:

> **Where in the radial geometry is the F₂-dominated angular organization strongest?**

The purpose is therefore **localization**, not significance testing.

The analysis identifies the radial locations of:

1. maximum mean \(|F_2|\)
2. maximum mean \(|F_2|-|F_1|\)
3. maximum F₂-dominance
4. maximum axial concentration \(R_2\)
5. the longest contiguous F₂-dominant radial zone
6. the stronger F₂-dominant subregion
7. axial concentration within the primary zone

No semantic interpretation is introduced.

---

# Input Verification

The following representations were verified:

- Conditional Fourier coefficients:
  \[
  (2300,72,37)
  \]

- Conditional angular distributions:
  \[
  (2300,72,72)
  \]

- Radial centers:
  \[
  (72,)
  \]

- Radial first-harmonic magnitudes:
  \[
  (2300,72)
  \]

- Radial second-harmonic magnitudes:
  \[
  (2300,72)
  \]

- Radial second-harmonic phase:
  \[
  (2300,72)
  \]

- Radial two-fold axis:
  \[
  (2300,72)
  \]

All inputs were verified.

---

# Valid Radial Shells

There are:

\[
165363
\]

valid sketch × radial-shell observations out of:

\[
165600.
\]

Therefore:

\[
\frac{165363}{165600}
=
0.998569
\]

or approximately:

\[
99.857\%
\]

of all possible sketch × radial-shell observations are valid.

A valid-shell mask is therefore used throughout the localization analysis.

---

# Global Harmonic Summary

Across valid radial shells:

\[
\operatorname{mean}|F_1|
=
0.005199288
\]

\[
\operatorname{mean}|F_2|
=
0.006402373
\]

and therefore:

\[
\operatorname{mean}(|F_2|-|F_1|)
=
0.001203085.
\]

Thus, across the radial representation as a whole, the second harmonic has a larger mean magnitude than the first.

This global result is descriptive.

The important question in this cell is **where that advantage is concentrated**.

---

# Localization of the F₂ Structure

## Maximum Mean \(|F_2|\)

The largest mean second-harmonic magnitude occurs at:

\[
\boxed{r=21.5}
\]

with:

\[
\boxed{
\operatorname{mean}|F_2|
=
0.01807305
}
\]

This identifies the radial location where the second-harmonic component is strongest in absolute magnitude.

---

## Maximum F₂ Advantage Over F₁

The maximum difference:

\[
|F_2|-|F_1|
\]

occurs at:

\[
\boxed{r=21.5}
\]

with:

\[
\boxed{
|F_2|-|F_1|
=
0.00577309
}
\]

Therefore the radial location of maximum absolute F₂ strength and maximum F₂-over-F₁ advantage coincide.

This is an important localization result.

---

## Maximum F₂ Dominance

The largest fraction of sketches for which:

\[
|F_2|>|F_1|
\]

occurs at:

\[
\boxed{r=19.5}
\]

with:

\[
\boxed{
P(|F_2|>|F_1|)
=
0.648261
}
\]

Thus approximately:

\[
64.8\%
\]

of sketches are F₂-dominant at this radial shell.

The maximum dominance location is slightly inward from the maximum absolute F₂ magnitude.

---

## Maximum Axial Concentration

The strongest radial concentration of the two-fold axis occurs at:

\[
\boxed{r=25.5}
\]

with:

\[
\boxed{
R_2=0.686844
}
\]

Therefore the three localization measures peak at slightly different but closely related radial positions:

| Measure | Peak radius |
|---|---:|
| Maximum mean \(|F_2|\) | 21.5 |
| Maximum \(|F_2|-|F_1|\) | 21.5 |
| Maximum F₂ dominance | 19.5 |
| Maximum \(R_2\) | 25.5 |

This indicates that **strength, relative dominance, and angular concentration are related but not identical properties**.

---

# Primary F₂-Dominant Radial Zone

The longest contiguous region in which:

\[
P(|F_2|>|F_1|)>0.5
\]

extends from:

\[
\boxed{r=3.5\rightarrow27.5}
\]

covering:

\[
\boxed{25\text{ radial shells}}
\]

with a peak dominance of:

\[
\boxed{0.648261}.
\]

This defines the **primary F₂-dominant radial zone**.

Importantly, the zone is not defined by an arbitrary Fourier-magnitude threshold.

It is defined by the population prevalence criterion:

\[
P(|F_2|>|F_1|)>50\%.
\]

---

# Strong F₂-Dominance Region

A more stringent region was also identified using:

\[
P(|F_2|>|F_1|)\geq0.60.
\]

There are:

\[
\boxed{8/72}
\]

radial shells satisfying this criterion.

They occupy:

\[
\boxed{r=16.5\rightarrow23.5}.
\]

This is the region where F₂ dominance is most concentrated.

The peak occurs near:

\[
r\approx19.5-21.5.
\]

---

# Axial Concentration Within the Primary Zone

Within the primary F₂-dominant zone:

\[
r=3.5\rightarrow27.5,
\]

the axial concentration \(R_2\) has:

\[
\text{mean }R_2=0.489651
\]

\[
\min R_2=0.201966
\]

\[
\max R_2=0.686844.
\]

Thus F₂ dominance does not imply uniformly strong axial concentration throughout the entire zone.

Instead, the two properties strengthen progressively toward the central portion of the zone.

---

# Radial Evolution

The localization table shows a clear sequence.

### Near the centroid

At:

\[
r=0.5
\]

\[
|F_2|-|F_1|=-0.000251
\]

and:

\[
P(F_2>F_1)=0.194.
\]

Thus F₂ is not dominant near the centroid.

---

### Emergence of F₂ dominance

By:

\[
r=3.5,
\]

the dominance fraction reaches:

\[
0.504.
\]

It then increases:

\[
r=5.5:
\quad0.577
\]

\[
r=6.5:
\quad0.587
\]

and later:

\[
r=16.5:
\quad0.621.
\]

---

### Strongest F₂-dominant region

The strongest region occurs around:

\[
r=16.5-23.5.
\]

For example:

\[
r=17.5:
\quad P(F_2>F_1)=0.636
\]

\[
r=18.5:
\quad0.641
\]

\[
r=19.5:
\quad0.648
\]

\[
r=20.5:
\quad0.640
\]

\[
r=21.5:
\quad0.640
\]

\[
r=22.5:
\quad0.631
\]

\[
r=23.5:
\quad0.609.
\]

This is the strongest radial localization of F₂ dominance.

---

# Peak F₂ Strength

At the maximum-F₂ radius:

\[
r=21.5,
\]

the radial Fourier magnitudes are approximately:

\[
|F_1|=0.012300
\]

and

\[
|F_2|=0.018073.
\]

Therefore:

\[
|F_2|-|F_1|
=
0.005773.
\]

This is the largest observed mean separation between the first and second angular harmonics across radial position.

---

# Peak Axial Concentration

The maximum \(R_2\) occurs slightly farther outward:

\[
r=25.5
\]

where:

\[
R_2=0.686844.
\]

At this radius:

\[
P(F_2>F_1)=0.567.
\]

This distinction is useful:

> **The radial location of strongest F₂ amplitude is not exactly the radial location of strongest phase/axis concentration.**

The amplitude and phase organization therefore contain partially distinct information.

---

# Decline Beyond the Primary Zone

After the primary F₂-dominant zone, F₂ dominance decreases.

At:

\[
r=30.5:
\quad
P(F_2>F_1)=0.456.
\]

At:

\[
r=40.5:
\quad
P(F_2>F_1)=0.324.
\]

At:

\[
r=50.5:
\quad
P(F_2>F_1)=0.279.
\]

At:

\[
r=60.5:
\quad
P(F_2>F_1)=0.157.
\]

By:

\[
r=70.5:
\quad
P(F_2>F_1)=0.017.
\]

Thus the F₂-dominant organization is strongly localized rather than extending uniformly throughout the radial extent.

---

# Important Distinction: F₂ Strength vs F₂ Dominance

The three curves should not be conflated.

### Absolute F₂ strength

\[
|F_2(r)|
\]

answers:

> **Where is the second harmonic strongest?**

Peak:

\[
r=21.5.
\]

### Relative harmonic advantage

\[
|F_2(r)|-|F_1(r)|
\]

answers:

> **Where does F₂ most strongly exceed F₁ in absolute magnitude?**

Peak:

\[
r=21.5.
\]

### Population dominance

\[
P(|F_2|>|F_1|\mid r)
\]

answers:

> **At what radius is F₂ dominant in the largest fraction of sketches?**

Peak:

\[
r=19.5.
\]

### Axial concentration

\[
R_2(r)
\]

answers:

> **Where is the two-fold orientation most coherently concentrated?**

Peak:

\[
r=25.5.
\]

These are complementary measurements rather than interchangeable definitions.

---

# Relationship to Cell 12

Cell 12 established:

\[
\boxed{
\text{radial heterogeneity is statistically supported}
}
\]

using a within-sketch radial permutation null.

Cell 13 now establishes:

\[
\boxed{
\text{where that heterogeneity is concentrated}
}
\]

The progression is therefore:

\[
\text{Cell 12}
\rightarrow
\text{Is radial heterogeneity real?}
\]

followed by:

\[
\text{Cell 13}
\rightarrow
\text{Where is the effect located?}
\]

This is a cleaner scientific separation than repeatedly performing significance tests at individual radial positions.

---

# Representation Integrity

The analysis remains entirely in the raw-image geometric representation.

Used:

- Original grayscale TIFF
- Intensity-weighted centroid
- Radial × angular representation
- Conditional angular distributions
- Circular Fourier transform
- Radial F₁/F₂ magnitude
- F₂ phase
- Two-fold axial orientation
- Radial dominance localization

Not used:

- F₂/F₁ ratio
- Image thresholding
- Binarization
- Resizing
- Rotation
- PCA
- Clustering
- Semantic labels

---

# Interpretation Boundary

The present result supports a geometric statement:

> **The second-harmonic angular organization is spatially localized in radial coordinates, with its strongest absolute magnitude and greatest F₂-over-F₁ advantage occurring around the intermediate radial region, approximately \(r=19.5-25.5\), and with a broader F₂-dominant zone extending from approximately \(r=3.5\) to \(27.5\).**

This is a statement about the measured geometry of the raw images.

It does **not** establish that this radial region corresponds to:

- a particular garment component,
- a semantic primitive,
- a garment category,
- a body region,
- a perceptual feature,
- or a design concept.

Those interpretations require separate evidence.

---

# Conclusion

Cell 13 localizes the radial × angular coupling established in Cell 12.

The principal localization results are:

\[
\boxed{
r_{\max |F_2|}=21.5
}
\]

\[
\boxed{
r_{\max(|F_2|-|F_1|)}=21.5
}
\]

\[
\boxed{
r_{\max P(F_2>F_1)}=19.5
}
\]

\[
\boxed{
r_{\max R_2}=25.5
}
\]

The longest contiguous F₂-dominant zone is:

\[
\boxed{
r=3.5\rightarrow27.5
}
\]

and the strongest F₂-dominance region is:

\[
\boxed{
r=16.5\rightarrow23.5
}
\]

where:

\[
P(F_2>F_1)\geq0.60.
\]

The result therefore indicates that the radial × angular organization is **not spatially uniform**. It is concentrated in an intermediate radial region, with distinct peaks for harmonic amplitude, harmonic dominance, and axial concentration.

---

## Evidence Chain So Far

\[
\boxed{
\text{Raw TIFF}
\rightarrow
\text{centroid}
\rightarrow
W(r,\theta)
\rightarrow
P(\theta|r)
\rightarrow
F_1,F_2
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{F₂ dominance}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{radial heterogeneity}
\quad
\text{(Cell 12)}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{radial localization}
\quad
\text{(Cell 13)}
}
\]

### Current geometric finding

> **A coherent two-fold angular organization is strongest within a localized intermediate radial region of the raw CLO-SKET images.**

### Still deliberately unclaimed

\[
\boxed{
\text{No semantic interpretation.}
}
\]

The next scientific question should therefore be whether this localized radial organization is **reproducible at the individual-sketch level and structurally related to other geometric descriptors**, before introducing any semantic or category-level interpretation.

# 🧪 CLO-SKET — RAW IMAGE RADIAL / ANGULAR GEOMETRY
## CELL 14 — VISUAL INTERPRETATION OF RADIAL F₂ ANGULAR STRUCTURE

---

## Objective

Cell 13 localized the radial region in which the second harmonic is strongest and most frequently dominant.

Cell 14 provides a **visual inspection of the radial F₂ structure at the individual-sketch level**.

The purpose is to connect the numerical radial measurements to their corresponding image-space representation without introducing semantic interpretation.

The visualization follows:

\[
\text{raw sketch}
\rightarrow
\text{intensity-weighted centroid}
\rightarrow
|F_2(r)|
\rightarrow
\text{reliable phase}
\rightarrow
k=2\text{ reconstruction}
\rightarrow
\text{image overlay}
\]

This is an interpretive visualization rather than a new statistical test.

---

# Input Verification

Verified inputs:

- Radial F₂ magnitude:
  \[
  (2300,72)
  \]

- Radial F₂ phase:
  \[
  (2300,72)
  \]

- Number of radial bins:
  \[
  72
  \]

- Population:
  \[
  2300
  \]

All Fourier inputs were verified.

---

# Radial Coordinate Verification

The radial coordinate is represented using 72 shells.

The first shell center is:

\[
r=0.50
\]

corresponding to normalized radius:

\[
r_{\mathrm{norm}}
=
\frac{0.50}{72}
=
0.006944.
\]

The final shell center is:

\[
r=71.50
\]

corresponding to:

\[
r_{\mathrm{norm}}
=
0.993056.
\]

Thus the visualization covers essentially the complete normalized radial extent:

\[
0<r_{\mathrm{norm}}<1.
\]

---

# Representative-Sketch Selection

Three sketches were selected according to their population position in mean radial F₂ magnitude:

| Population position | Index | Mean \(|F_2|\) |
|---|---:|---:|
| 25th percentile | 30 | 0.004701 |
| 50th percentile | 443 | 0.006412 |
| 75th percentile | 1130 | 0.008175 |

These examples therefore represent increasing levels of overall radial F₂ magnitude.

The selection is intended to provide **visual coverage across the population**, rather than to identify representative garment categories.

---

# 25th-Percentile F₂ Example

### Sketch index

\[
\boxed{30}
\]

Mean radial F₂ magnitude:

\[
\boxed{0.004701}
\]

Peak radial F₂ shell:

\[
24.5
\]

Normalized peak radius:

\[
\boxed{r=0.340}
\]

F₂ axis at the peak:

\[
\boxed{87.29^\circ}
\]

The radial F₂ magnitude shows a clear localized maximum around:

\[
r_{\mathrm{norm}}\approx0.34.
\]

The corresponding F₂ axis is close to the image vertical axis:

\[
90^\circ.
\]

The reconstructed \(k=2\) field produces an explicitly two-fold angular pattern centered on the intensity-weighted centroid.

The overlay allows the geometric field to be compared directly with the original sketch.

---

# 50th-Percentile F₂ Example

### Sketch index

\[
\boxed{443}
\]

Mean radial F₂ magnitude:

\[
\boxed{0.006412}
\]

Peak radial F₂ shell:

\[
20.5
\]

Normalized peak radius:

\[
\boxed{r=0.285}
\]

F₂ axis at the peak:

\[
\boxed{163.97^\circ}
\]

Because the F₂ orientation is axial:

\[
\alpha_2\equiv\alpha_2+180^\circ,
\]

the value

\[
163.97^\circ
\]

represents the same axis as:

\[
-16.03^\circ.
\]

This example therefore differs substantially from the population-level tendency toward the vertical axis.

This is an important visualization result:

> **Population-level F₂ axis concentration does not imply that every individual sketch has an F₂ axis aligned with the image vertical.**

The individual-sketch visualization therefore provides an important complement to the population statistics from Cells 9–10.

---

# 75th-Percentile F₂ Example

### Sketch index

\[
\boxed{1130}
\]

Mean radial F₂ magnitude:

\[
\boxed{0.008175}
\]

Peak radial F₂ shell:

\[
19.5
\]

Normalized peak radius:

\[
\boxed{r=0.271}
\]

F₂ axis:

\[
\boxed{91.53^\circ}
\]

The F₂ magnitude is stronger than in the 25th- and 50th-percentile examples.

The peak occurs in the same broad intermediate radial region identified in the population-level localization analysis.

The F₂ axis is again close to the image vertical axis.

---

# Cross-Example Comparison

The three examples show:

| Example | Mean \(|F_2|\) | Peak radius | F₂ axis |
|---|---:|---:|---:|
| 25th percentile | 0.004701 | 0.340 | 87.29° |
| 50th percentile | 0.006412 | 0.285 | 163.97° |
| 75th percentile | 0.008175 | 0.271 | 91.53° |

Two observations are particularly important.

### 1. Radial localization is broadly consistent

All three examples have their strongest radial F₂ response in an intermediate radial region:

\[
r_{\mathrm{norm}}\approx0.27-0.34.
\]

This is consistent with the population-level localization found in Cell 13.

### 2. Individual F₂ orientation can differ

Two examples have axes close to:

\[
90^\circ,
\]

while the median-strength example has:

\[
163.97^\circ.
\]

Therefore the population-level concentration around the image vertical axis describes a **distributional tendency**, not a universal individual property.

---

# Reconstructed \(k=2\) Field

For each sketch, the radial second-harmonic field is represented as:

\[
F_2(r)
=
|F_2(r)|e^{i\phi_2(r)}.
\]

The corresponding real-valued two-fold angular contribution is:

\[
A_2(r,\theta)
=
|F_2(r)|
\cos\left(2\theta+\phi_2(r)\right).
\]

The reconstruction therefore preserves two independent pieces of information:

### Magnitude

\[
|F_2(r)|
\]

determines the strength of the two-fold component at each radius.

### Phase

\[
\phi_2(r)
\]

determines its angular orientation.

The reconstructed field is therefore not an arbitrary visual filter.

It is generated directly from the measured radial second-harmonic magnitude and phase.

---

# Phase Reliability

Phase is interpreted only in radial regions where the corresponding F₂ magnitude is sufficiently strong.

This restriction is necessary because phase becomes unstable when:

\[
|F_2(r)|\rightarrow0.
\]

The phase plots therefore intentionally show only the reliable radial region.

Outside regions of sufficient F₂ magnitude, phase values are not treated as meaningful geometric evidence.

---

# Overlay Interpretation

The final overlay combines:

1. the original raw sketch,
2. the intensity-weighted centroid,
3. the reconstructed \(k=2\) field.

The overlay is used only to visually inspect how the measured harmonic structure is distributed relative to the original image geometry.

It does **not** imply that the reconstructed field corresponds to a specific garment component.

---

# Relationship to Population Results

The individual visualizations are consistent with the population-level findings:

### Population-level F₂ localization

Cell 13 identified:

\[
r_{\max |F_2|}
=
21.5
\]

corresponding approximately to:

\[
r_{\mathrm{norm}}\approx0.30.
\]

The representative sketches show peak locations around:

\[
0.271,\quad0.285,\quad0.340.
\]

Thus the individual examples occupy the same broad intermediate radial region.

---

# Important Individual-vs-Population Distinction

The visualization demonstrates why the population-level statistics should not be interpreted as deterministic rules.

At the population level:

\[
R_2\approx0.94
\]

for the global F₂ axis distribution, indicating strong concentration around the vertical axis.

However, individual sketches can still exhibit substantially different orientations.

For example:

\[
\alpha_2=163.97^\circ
\]

is far from:

\[
90^\circ,
\]

while remaining a valid axial orientation.

Therefore:

\[
\boxed{
\text{population concentration}
\neq
\text{individual invariance}
}
\]

This distinction should be retained in the interpretation of the F₂ geometry.

---

# What the Visualization Supports

The visualization supports the following geometric observations:

1. Individual sketches contain measurable radial F₂ structure.
2. The strongest F₂ response can occur in an intermediate radial region.
3. The radial location of peak F₂ varies between sketches but remains broadly localized.
4. F₂ phase provides an individual two-fold axis orientation.
5. Individual F₂ axes need not all align with the image vertical axis.
6. The reconstructed \(k=2\) field provides a direct visual representation of the measured harmonic component.
7. The visual examples are consistent with the population-level radial localization identified previously.

---

# What the Visualization Does NOT Establish

This cell does **not** establish:

- semantic meaning of the F₂ field,
- garment-part identity,
- garment grammar,
- bilateral symmetry,
- perceptual importance,
- category semantics,
- correspondence to body anatomy,
- designer intention,
- or causal interpretation.

In particular:

> A visually apparent two-fold field should not be described as a semantic garment structure solely on the basis of this visualization.

Such claims require independent evidence.

---

# Representation Integrity

The canonical representation remains unchanged.

The analysis uses:

- original grayscale TIFF
- intensity-weighted centroid
- radial/angular representation
- conditional angular distributions
- complex Fourier coefficients
- radial F₂ magnitude
- radial F₂ phase
- \(k=2\) reconstruction

No:

- thresholding
- binarization
- resizing
- rotation
- PCA
- clustering
- semantic relabeling

is introduced.

---

# Interpretation Boundary

Cell 14 is intentionally a **visual interpretation layer** over the quantitative results established in Cells 9–13.

The evidence chain is:

\[
\text{Raw TIFF}
\]

\[
\downarrow
\]

\[
\text{Intensity-weighted centroid}
\]

\[
\downarrow
\]

\[
\text{Angular mass distribution}
\]

\[
\downarrow
\]

\[
F_2\text{ magnitude + phase}
\]

\[
\downarrow
\]

\[
\text{Two-fold axis}
\]

\[
\downarrow
\]

\[
\text{Radial localization}
\]

\[
\downarrow
\]

\[
\boxed{
\text{Individual-sketch visualization}
}
\]

---

# Conclusion

Cell 14 provides individual-sketch visual evidence for the radial F₂ structure identified quantitatively in the preceding cells.

Across the three population-percentile examples, the peak radial F₂ response occurs at:

\[
r_{\mathrm{norm}}
=
0.271-0.340.
\]

This is consistent with the intermediate radial localization observed at the population level.

At the same time, the examples demonstrate meaningful individual variation in F₂ orientation.

The most important methodological conclusion is therefore:

\[
\boxed{
\text{Radial F₂ localization is population-level,
while F₂ orientation remains an individual geometric variable.}
}
\]

The visualization provides qualitative geometric grounding for the quantitative findings without introducing semantic interpretation.

---

## 🟢 CELL 14 — VISUAL F₂ INTERPRETATION COMPLETE

### Established

\[
\boxed{
\text{Radial F₂ structure can be visualized directly
from the raw-image Fourier representation.}
}
\]

### Consistent with previous cells

\[
\boxed{
\text{Peak F₂ structure occurs in an intermediate radial region.}
}
\]

### Important individual variation

\[
\boxed{
\text{F₂ axis orientation is not invariant across sketches.}
}
\]

### Still deliberately unclaimed

\[
\boxed{
\text{No semantic interpretation.}
}
\]

\[
\boxed{
\text{No garment-part interpretation.}
}
\]

\[
\boxed{
\text{No perceptual interpretation.}
}
\]

# 🧪 CLO-SKET — RAW IMAGE RADIAL / ANGULAR GEOMETRY
## CELL 15R — PARSEVAL-CORRECTED FOURIER ENERGY + CONTROLLED RECONSTRUCTION

---

## Objective

Cell 15R quantifies how the angular signal is distributed across
the lowest Fourier harmonics as a function of radial distance.

The analysis addresses two related but distinct questions:

1. **How much Fourier energy is carried by \(k=0\), \(k=1\), and \(k=2\)?**
2. **How well can the measured angular profile at a radial shell be
   reconstructed using only low-order harmonics?**

The analysis therefore combines:

\[
\text{Fourier energy accounting}
\]

with

\[
\text{controlled low-order reconstruction}.
\]

No semantic interpretation is introduced.

---

# Input Verification

Verified inputs:

- Conditional angular profiles:
  \[
  (2300,72,72)
  \]

- Conditional Fourier coefficients:
  \[
  (2300,72,37)
  \]

- Radial centers:
  \[
  (72,)
  \]

- Angular bins:
  \[
  72
  \]

- Fourier bins:
  \[
  37
  \]

All required inputs were verified.

---

# Fourier Convention

For each sketch and radial shell, the conditional angular profile is:

\[
A(r,\theta).
\]

It is decomposed using the discrete angular Fourier transform:

\[
F_k(r)
=
\sum_{\theta}
A(r,\theta)
\exp
\left(
-\frac{2\pi i k\theta}{N_\theta}
\right).
\]

The conditional Fourier representation contains the one-sided
real FFT coefficients.

Because:

\[
N_\theta=72
\]

is even, the one-sided rFFT contains only one member of each
positive/negative frequency pair.

Therefore the corresponding Parseval energy is:

\[
E_{\mathrm{total}}
=
|F_0|^2
+
2\sum_{k=1}^{N_\theta/2-1}|F_k|^2
+
|F_{N_\theta/2}|^2.
\]

The factor of two is therefore essential for the non-zero,
non-Nyquist harmonics.

---

# Parseval-Corrected Fourier Energy

Population-averaged energy fractions are:

| Component | Mean energy fraction |
|---|---:|
| \(k=0\) | 0.375880 |
| \(k=1\) | 0.051892 |
| \(k=2\) | 0.095396 |
| \(k\leq2\) | 0.523168 |

Thus the combined low-order contribution is:

\[
\boxed{
E_{k\leq2}=0.523168
}
\]

or approximately:

\[
\boxed{52.3\%}
\]

of the total Parseval-corrected angular Fourier energy.

The individual contributions are:

\[
E_{k=0}\approx37.6\%
\]

\[
E_{k=1}\approx5.2\%
\]

\[
E_{k=2}\approx9.5\%.
\]

Importantly, these are **energy fractions**, not Fourier magnitudes.

---

# Parseval Consistency Check

The numerical reconstruction of Fourier energy satisfies:

\[
\max |\Delta E|
=
6.661338\times10^{-16}
\]

and:

\[
\mathrm{mean}|\Delta E|
=
1.653345\times10^{-17}.
\]

Therefore:

\[
\boxed{
\text{Parseval energy accounting passes to numerical precision.}
}
\]

This establishes that the reported Fourier energy fractions are
consistent with the full angular signal under the specified
one-sided rFFT convention.

---

# Radial Energy Localization

The Fourier energy fractions are evaluated independently at each
radial shell.

The primary F₂-dominant zone previously established in Cell 13 is:

\[
\boxed{
r=3.5\rightarrow27.5
}
\]

containing:

\[
25
\]

radial shells.

This independently established radial region is retained as the
control region for the representative reconstruction analysis.

---

# Low-Order Energy Localization

The maximum population mean \(k=2\) energy fraction occurs at:

\[
\boxed{
r=24.5
}
\]

with:

\[
\boxed{
E_{k=2}=0.089208.
}
\]

The maximum population mean \(k\leq2\) energy fraction occurs at:

\[
\boxed{
r=27.5
}
\]

with:

\[
\boxed{
E_{k\leq2}=0.487111.
}
\]

Thus low-order angular energy is not radially uniform.

It varies systematically with distance from the
intensity-weighted centroid.

---

# Controlled Representative Sketches

Representative sketches were selected from the Cell 13
primary F₂-dominant radial zone.

Selection is based on the mean F₂ magnitude within that previously
defined zone.

| Population position | Sketch index | Mean \(|F_2|\) in primary zone |
|---|---:|---:|
| 25th percentile | 2079 | 0.270755 |
| 50th percentile | 471 | 0.330401 |
| 75th percentile | 142 | 0.398674 |

These examples therefore represent increasing levels of radial
F₂ strength.

They are **not** selected as semantic or category representatives.

---

# Controlled Radial-Shell Reconstruction

For each representative sketch, reconstruction is performed at
its own F₂ peak shell within the primary radial zone.

This avoids selecting an arbitrary common radial shell.

The procedure is:

\[
\text{select sketch}
\rightarrow
\text{identify F₂ peak within primary zone}
\rightarrow
\text{extract }A(r,\theta)
\rightarrow
\text{reconstruct using low-order harmonics}.
\]

Three reconstruction levels are compared:

### \(k=0\)

Only the angular mean is retained:

\[
A_0(\theta)=F_0.
\]

### \(k\leq1\)

The mean and first harmonic are retained.

### \(k\leq2\)

The mean, first harmonic, and second harmonic are retained.

The full Fourier reconstruction is also evaluated as a numerical
reference.

---

# 25th-Percentile Reconstruction

### Sketch

\[
\boxed{2079}
\]

Radial shell:

\[
\boxed{r=7.5}
\]

F₂ magnitude:

\[
\boxed{|F_2|=0.61028958}
\]

F₂ axis:

\[
\boxed{112.89^\circ}
\]

Reconstruction errors:

| Reconstruction | NRMSE |
|---|---:|
| \(k=0\) | 0.888638 |
| \(k\leq1\) | 0.773949 |
| \(k\leq2\) | 0.665076 |
| Full Fourier | \(3.28\times10^{-16}\) |

The addition of the second harmonic substantially improves the
reconstruction relative to the \(k=0\) and \(k\leq1\) representations.

However, the remaining \(k\leq2\) error is substantial.

Therefore:

> The second harmonic captures an important component of the
> angular structure, but it does not by itself reproduce the full
> measured angular profile.

---

# 50th-Percentile Reconstruction

### Sketch

\[
\boxed{471}
\]

Radial shell:

\[
\boxed{r=3.5}
\]

F₂ magnitude:

\[
\boxed{|F_2|=0.61090707}
\]

F₂ axis:

\[
\boxed{94.70^\circ}
\]

Reconstruction errors:

| Reconstruction | NRMSE |
|---|---:|
| \(k=0\) | 0.938395 |
| \(k\leq1\) | 0.936907 |
| \(k\leq2\) | 0.888066 |
| Full Fourier | \(2.89\times10^{-16}\) |

Here the low-order reconstruction remains relatively poor despite
the strong local F₂ magnitude.

This demonstrates an important distinction:

\[
\boxed{
\text{strong }|F_2|
\neq
\text{complete low-order representation}.
}
\]

The second harmonic can be strong while substantial angular
structure remains in higher harmonics.

---

# 75th-Percentile Reconstruction

### Sketch

\[
\boxed{142}
\]

Radial shell:

\[
\boxed{r=25.5}
\]

F₂ magnitude:

\[
\boxed{|F_2|=0.61516144}
\]

F₂ axis:

\[
\boxed{90.94^\circ}
\]

Reconstruction errors:

| Reconstruction | NRMSE |
|---|---:|
| \(k=0\) | 0.867039 |
| \(k\leq1\) | 0.832235 |
| \(k\leq2\) | 0.710445 |
| Full Fourier | \(3.56\times10^{-16}\) |

Again, adding \(k=2\) improves the reconstruction relative to
lower-order representations, while substantial higher-order
structure remains.

---

# Reconstruction Comparison

Across all three examples:

\[
\mathrm{NRMSE}_{k\leq2}
<
\mathrm{NRMSE}_{k\leq1}
\]

and:

\[
\mathrm{NRMSE}_{k\leq1}
<
\mathrm{NRMSE}_{k=0}
\]

for the controlled examples.

The full Fourier reconstruction reaches numerical zero error:

\[
\mathrm{NRMSE}_{\mathrm{full}}
\approx10^{-16}.
\]

This is expected because the full set of Fourier coefficients
contains the complete measured angular profile.

The important observation is therefore not that the full Fourier
reconstruction works — that is mathematically expected — but that
including the second harmonic systematically improves the
low-order representation.

---

# What the Radial Energy Plot Shows

The radial energy visualization separates:

\[
k=0,
\]

\[
k=1,
\]

\[
k=2,
\]

and:

\[
k\leq2.
\]

The resulting curves show that the relative contribution of these
components changes with radial distance.

In particular, the region highlighted from Cell 13 corresponds to
a radial interval in which the second harmonic is repeatedly
important.

The analysis therefore supports a **radially heterogeneous angular
Fourier structure** rather than a single global angular pattern.

---

# Important Distinction: Magnitude vs Energy vs Reconstruction

Three quantities are intentionally kept separate.

### 1. F₂ magnitude

\[
|F_2|
\]

measures the strength of the second angular harmonic.

---

### 2. F₂ energy fraction

\[
\frac{|F_2|^2}{E_{\mathrm{total}}}
\]

under the appropriate Parseval weighting measures its contribution
to the total angular signal energy.

---

### 3. \(k\leq2\) reconstruction error

\[
\mathrm{NRMSE}(A,A_{k\leq2})
\]

measures how accurately the measured angular profile can be
represented using harmonics up to second order.

These quantities answer different questions.

They must not be interpreted interchangeably.

---

# Critical Control Design

The representative reconstruction does **not** select arbitrary
radial shells.

Instead:

1. Cell 13 first identifies the primary F₂-dominant radial zone.
2. Representative sketches are selected by their mean F₂ strength
   within that zone.
3. Each selected sketch is then evaluated at its own F₂ peak
   within that same zone.

Therefore the reconstruction audit is anchored to an independently
identified radial region.

This avoids using outer sparse radial shells merely because they
happen to contain numerical fluctuations.

---

# What This Cell Establishes

The analysis establishes:

### 1. Correct Fourier energy accounting

The one-sided rFFT representation satisfies Parseval's identity
to numerical precision.

### 2. Measurable low-order angular energy

The mean energy fractions are:

\[
k=0:\;37.6\%
\]

\[
k=1:\;5.2\%
\]

\[
k=2:\;9.5\%
\]

with:

\[
k\leq2:\;52.3\%.
\]

### 3. Radial heterogeneity

The relative contribution of low-order harmonics changes with
radial distance.

### 4. Radial localization

The strongest population-level F₂ energy occurs near:

\[
r=24.5.
\]

The strongest \(k\leq2\) energy occurs near:

\[
r=27.5.
\]

### 5. Second-harmonic contribution to reconstruction

Adding \(k=2\) improves reconstruction of the measured angular
profile in all three controlled examples.

### 6. Higher-order structure remains

The \(k\leq2\) reconstruction does not reproduce the full angular
signal.

Therefore the observed geometry cannot be reduced to only the
first two harmonics.

---

# What This Cell Does NOT Establish

This analysis does **not** establish:

- semantic structure,
- garment grammar,
- garment-part identity,
- category meaning,
- perceptual importance,
- bilateral symmetry,
- designer intention,
- correspondence to anatomy,
- or classification capability.

In particular:

\[
\boxed{
52.3\%\text{ low-order Fourier energy}
}
\]

must **not** be interpreted as:

> “52.3% of garment meaning is encoded in the first three
> harmonics.”

It is strictly a statement about the measured angular signal
under the specified Fourier and Parseval representation.

---

# Representation Integrity

The canonical raw-image representation remains unchanged.

The analysis uses:

- original grayscale TIFF images,
- intensity-weighted centroids,
- conditional angular profiles,
- radial shells,
- complex angular Fourier coefficients,
- Parseval-corrected energy,
- and Fourier reconstruction.

No:

- thresholding,
- binarization,
- resizing,
- rotation,
- PCA,
- clustering,
- semantic relabeling,
- or Paper-I representation modification

is introduced.

---

# Evidence Chain

The analysis now forms a coherent sequence:

\[
\boxed{\text{Raw TIFF}}
\]

\[
\downarrow
\]

\[
\boxed{\text{Intensity-weighted centroid}}
\]

\[
\downarrow
\]

\[
\boxed{A(r,\theta)}
\]

\[
\downarrow
\]

\[
\boxed{F_k(r)}
\]

\[
\downarrow
\]

\[
\boxed{\text{F₂ magnitude + phase}}
\]

\[
\downarrow
\]

\[
\boxed{\text{Two-fold orientation}}
\]

\[
\downarrow
\]

\[
\boxed{\text{Radial localization}}
\]

\[
\downarrow
\]

\[
\boxed{\text{Parseval-corrected energy}}
\]

\[
\downarrow
\]

\[
\boxed{\text{Controlled low-order reconstruction}}
\]

This provides a quantitative-to-visual bridge between the raw image
geometry and its low-order angular Fourier representation.

---

# Interpretation Boundary

The result should currently be described as:

> **A radially heterogeneous angular Fourier organization in which
> the second harmonic contributes a measurable and spatially
> localized component of the raw-image angular signal.**

It should **not yet** be described as:

> garment grammar,

> semantic structure,

> garment-part structure,

> or a learned fashion primitive.

Those interpretations require subsequent independent analysis.

---

# Conclusion

Cell 15R establishes that the angular organization observed in the
raw CLO-SKET images has a measurable low-order Fourier structure.

The Parseval-corrected analysis shows:

\[
\boxed{
E_{k\leq2}=0.523168
}
\]

of the total angular Fourier energy on average, with the second
harmonic contributing:

\[
\boxed{
E_{k=2}=0.095396.
}
\]

The low-order energy is radially heterogeneous, with the strongest
population-level F₂ energy near:

\[
\boxed{
r=24.5.
}
\]

Controlled individual reconstructions further show that adding the
second harmonic improves the representation of the measured angular
profile, although substantial higher-order structure remains.

Thus:

\[
\boxed{
\text{F₂ is a measurable component of the radial-angular geometry,
but not a complete description of it.}
}
\]

---

## 🟢 CELL 15R — PARSEVAL-CORRECTED FOURIER AUDIT COMPLETE

### Established

- Parseval energy accounting is numerically verified.
- \(k=0\), \(k=1\), and \(k=2\) energy contributions are quantified.
- \(k\leq2\) accounts for approximately 52.3% of mean angular Fourier energy.
- Low-order Fourier energy varies systematically with radial distance.
- The strongest F₂ energy is localized within the intermediate radial region.
- Controlled \(k\leq2\) reconstructions improve over lower-order reconstructions.
- Full Fourier reconstruction reproduces the measured profile to numerical precision.

### Critical methodological distinction

\[
\boxed{
\text{F₂ magnitude}
\neq
\text{F₂ energy fraction}
\neq
\text{low-order reconstruction accuracy}
}
\]

### Still deliberately unclaimed

\[
\boxed{
\text{No semantic interpretation.}
}
\]

\[
\boxed{
\text{No garment-part interpretation.}
}
\]

\[
\boxed{
\text{No category semantics.}
}
\]

\[
\boxed{
\text{No perceptual interpretation.}
}

# 🧪 CLO-SKET — RAW IMAGE RADIAL / ANGULAR GEOMETRY
## CELL 16R — CORRECTED F₂ RADIAL + AXIAL STABILITY AUDIT

---

## Objective

Cell 16R evaluates whether the radial F₂ structure identified in
the previous cells is stable across the sketch population.

Two distinct forms of stability are evaluated:

### Radial stability

Where, relative to the intensity-weighted centroid, does the
strongest F₂ component tend to occur?

### Axial stability

Do the strongest F₂ components tend to share a common axial
orientation?

These questions are deliberately treated separately.

\[
\boxed{
\text{Radial concentration}
\neq
\text{Axial concentration}
}
\]

---

# Input Verification

Verified inputs:

- \(F_1\) magnitude:
  \[
  (2300,72)
  \]

- \(F_2\) magnitude:
  \[
  (2300,72)
  \]

- \(F_2\) phase:
  \[
  (2300,72)
  \]

- Radial bins:
  \[
  72
  \]

- Population:
  \[
  2300
  \]

All required Fourier inputs were verified.

---

# Fourier Axis Convention

For each sketch and radial shell:

\[
F_2(r)
=
|F_2(r)|e^{i\phi_2(r)}.
\]

The corresponding two-fold angular field is:

\[
A_2(r,\theta)
=
|F_2(r)|
\cos(2\theta+\phi_2(r)).
\]

The positive F₂ axis is therefore:

\[
\boxed{
\alpha_2(r)
=
-\frac{\phi_2(r)}{2}
\pmod{180^\circ}
}
\]

with:

\[
\alpha_2\in[0^\circ,180^\circ).
\]

This is an **axial** orientation.

Therefore:

\[
\alpha
\equiv
\alpha+180^\circ.
\]

Angles separated by \(180^\circ\) represent the same axis.

The stored F₂ phase was detected in radians and converted to
degrees before axis calculation.

---

# Primary F₂-Dominant Radial Zone

The radial zone independently established in Cell 13 is recovered:

\[
\boxed{
r=3.5\rightarrow27.5
}
\]

containing:

\[
\boxed{25\text{ radial shells}}.
\]

This same zone is retained here rather than redefining the radial
region from the stability analysis.

This preserves the analysis sequence:

\[
\text{localization}
\rightarrow
\text{stability audit}.
\]

---

# Sketch-Level F₂ Peak

For every sketch, the strongest F₂ radial location is determined
within the previously established primary zone.

Valid sketches:

\[
\boxed{2300/2300}
\]

Thus every sketch contributes a valid radial F₂ peak to the
population-level stability analysis.

---

# Radial Peak Distribution

The distribution of sketch-level peak locations is:

| Statistic | Value |
|---|---:|
| Median peak radius | 21.5000 |
| Mean peak radius | 20.8609 |
| SD | 5.1665 |
| 25th percentile | 17.5000 |
| 75th percentile | 25.5000 |

The median peak occurs at:

\[
\boxed{r=21.5}.
\]

The interquartile range is:

\[
17.5\rightarrow25.5.
\]

Therefore the strongest F₂ component is not uniformly distributed
throughout the radial domain.

Instead, sketch-level F₂ peaks are concentrated toward the
intermediate radial region.

---

# Peak F₂ Strength

At the sketch-level F₂ peak:

\[
\text{Median peak }|F_2|
=
0.039141
\]

and:

\[
\text{Mean peak }|F_2|
=
0.040096.
\]

These values describe the **maximum F₂ magnitude within the
primary zone for each sketch**.

They should not be confused with the population mean
\(|F_2(r)|\) at a fixed radial shell.

Thus:

\[
\boxed{
\text{mean sketch-level peak }|F_2|
=
0.040096
}
\]

and:

\[
\boxed{
\text{population mean }|F_2|\text{ at }r=21.5
=
0.01807305
}
\]

are different quantities and are not expected to be equal.

---

# Radial Peak Concentration

The population concentration around the median peak radius is:

| Tolerance around median | Fraction of sketches |
|---|---:|
| ±2 radial units | 0.3191 |
| ±4 radial units | 0.5878 |
| ±6 radial units | 0.8635 |
| ±8 radial units | 0.9148 |

Therefore:

\[
\boxed{
86.35\%
}
\]

of sketches have their strongest F₂ component within ±6 radial
units of the population median:

\[
r=21.5.
\]

And:

\[
\boxed{
91.48\%
}
\]

fall within ±8 radial units.

This provides direct population-level evidence that the radial
location of strongest F₂ is concentrated rather than uniformly
distributed.

---

# F₂ Axial Orientation Stability

The sketch-level strongest F₂ component is also associated with its
corresponding axial orientation.

The population statistics are:

\[
\boxed{
\text{Mean axial orientation}=87.8177^\circ
}
\]

and:

\[
\boxed{
R=0.672479
}
\]

where \(R\) is the axial circular resultant.

For axial data:

\[
R
=
\sqrt{
C_2^2+S_2^2
}
\]

with:

\[
C_2
=
\frac{1}{N}
\sum_i\cos(2\alpha_i)
\]

and:

\[
S_2
=
\frac{1}{N}
\sum_i\sin(2\alpha_i).
\]

The interpretation is:

\[
R\rightarrow1
\]

for strong concentration around a common axis, while:

\[
R\rightarrow0
\]

indicates broad axial dispersion.

The observed:

\[
\boxed{R=0.6725}
\]

therefore indicates substantial population-level axial
concentration, while clearly not representing perfect alignment.

---

# Axial Deviation

Deviation is measured from the population vertical reference axis
near \(90^\circ\), using axial geometry.

| Statistic | Value |
|---|---:|
| Median deviation | 3.9130° |
| Mean deviation | 16.7879° |
| SD | 28.1149° |
| ≤15° | 0.7900 |
| ≤30° | 0.8330 |
| ≤45° | 0.8426 |
| ≤60° | 0.8548 |
| ≤90° | 1.0000 |

The median deviation is only:

\[
\boxed{3.91^\circ}
\]

while:

\[
\boxed{79.0\%}
\]

of sketches fall within \(15^\circ\) of the reference axis.

The mean is substantially larger because the population contains
a minority of strongly deviating orientations.

This distinction is important:

\[
\boxed{
\text{median deviation}
\neq
\text{mean deviation}
}
\]

and the mean should not be used alone to characterize the
population.

---

# Radial–Angular Coupling

A descriptive comparison was performed between:

- radial location of the strongest F₂ component, and
- strength of that strongest F₂ component.

The rank correlation is:

\[
\boxed{
\rho=-0.136949
}
\]

This is a weak negative association.

In practical terms, sketches whose strongest F₂ component occurs
farther from the centroid do not show a strong tendency toward
larger peak F₂ magnitude.

This analysis is descriptive only.

It does not establish:

- causality,
- semantic organization,
- garment-part identity,
- category identity,
- or any mechanistic relationship.

---

# Population Radial F₂ Profile

The population-averaged radial F₂ profile reaches its maximum at:

\[
\boxed{
r=21.5
}
\]

with:

\[
\boxed{
\mathrm{mean}|F_2(r)|=0.01807305.
}
\]

This agrees with the median sketch-level peak location:

\[
\boxed{
\mathrm{median}(r_{\mathrm{peak}})=21.5.
}
\]

This agreement is important because two different population
summaries identify the same radial neighborhood:

1. the population mean radial F₂ profile, and
2. the distribution of sketch-level F₂ peak locations.

They should nevertheless remain conceptually distinct measurements.

---

# Axis Convention Sanity Check

Three representative sketches were independently checked.

| Sketch | Peak radius | Peak \(|F_2|\) | Phase | Axis |
|---|---:|---:|---:|---:|
| 30 | 24.5 | 0.030976 | −174.59° | 87.29° |
| 443 | 20.5 | 0.053518 | 32.06° | 163.97° |
| 1130 | 19.5 | 0.040539 | 176.95° | 91.53° |

Using:

\[
\alpha_2
=
-\frac{\phi_2}{2}
\pmod{180^\circ}
\]

gives the reported orientations.

This confirms that the radial F₂ axis is being derived directly
from the Fourier phase rather than from a previously stored
orientation variable.

---

# Critical Correction Relative to Previous Analysis

A previous Cell 16 analysis treated the stored:

\[
\texttt{alpha2\_radial}
\]

variable as authoritative.

Cell 16R does **not** rely on that variable.

Instead, the axis is recalculated directly from:

\[
F_2(r)
=
|F_2(r)|e^{i\phi_2(r)}
\]

using:

\[
\boxed{
\alpha_2=-\phi_2/2\pmod{180^\circ}.
}
\]

This is the same mathematical convention used in Cell 14.

Therefore the radial axial-stability result is internally tied to
the Fourier phase itself.

---

# Two Independent Forms of Population Stability

The results can now be separated cleanly.

## 1. Radial stability

Question:

> Where does the strongest F₂ component tend to occur?

Evidence:

\[
\mathrm{median}(r_{\mathrm{peak}})=21.5
\]

and:

\[
86.35\%
\]

of sketches lie within ±6 radial units of that median.

---

## 2. Axial stability

Question:

> Do those strongest F₂ components tend to share an orientation?

Evidence:

\[
\mathrm{mean\ axis}=87.82^\circ
\]

and:

\[
R=0.6725.
\]

Additionally:

\[
79.0\%
\]

of sketches fall within \(15^\circ\) of the reference axis.

These are complementary but independent properties.

---

# What Cell 16R Establishes

The analysis establishes:

### 1. Population-level radial concentration

Strongest F₂ components tend to occur in an intermediate radial
region.

\[
\boxed{
\mathrm{median}\;r_{\mathrm{peak}}=21.5
}
\]

---

### 2. Agreement with the population radial profile

The population mean radial F₂ profile also peaks at:

\[
\boxed{
r=21.5.
}
\]

---

### 3. Population-level axial concentration

The strongest F₂ components show a common preferred axial
orientation near:

\[
\boxed{
88^\circ.
}
\]

---

### 4. The axial concentration is substantial but not perfect

\[
\boxed{
R=0.6725
}
\]

indicates meaningful concentration with non-negligible
population dispersion.

---

### 5. Radial and angular organization are separable

The radial peak location and peak F₂ strength show only a weak
rank association:

\[
\boxed{
\rho=-0.136949.
}
\]

Therefore radial position and F₂ strength should not be treated
as interchangeable measurements.

---

# What Cell 16R Does NOT Establish

This cell does **not** establish:

- bilateral symmetry,
- garment-part identity,
- semantic primitives,
- garment grammar,
- category semantics,
- perceptual importance,
- designer intention,
- anatomical correspondence,
- or classification capability.

In particular:

\[
R=0.6725
\]

does not mean:

> “67.25% of sketches are aligned.”

It is a circular concentration statistic, not a percentage.

Likewise:

\[
86.35\%
\]

within ±6 radial units does not mean that 86.35% of the image
energy occurs at that radius.

It refers specifically to the **location of the sketch-level
strongest F₂ peak**.

---

# Representation Integrity

The canonical representation remains unchanged.

The analysis uses:

- original grayscale TIFF images,
- intensity-weighted centroids,
- radial shells,
- angular Fourier coefficients,
- F₂ magnitude,
- F₂ phase,
- axial circular statistics,
- and sketch-level peak localization.

No:

- thresholding,
- binarization,
- resizing,
- rotation,
- PCA,
- clustering,
- semantic relabeling,
- or learned transformation

is introduced.

---

# Evidence Chain

The current evidence chain is:

\[
\boxed{\text{Raw TIFF}}
\]

\[
\downarrow
\]

\[
\boxed{\text{Intensity-weighted centroid}}
\]

\[
\downarrow
\]

\[
\boxed{A(r,\theta)}
\]

\[
\downarrow
\]

\[
\boxed{F_2(r)}
\]

\[
\downarrow
\]

\[
\boxed{\text{F₂ magnitude + phase}}
\]

\[
\downarrow
\]

\[
\boxed{\text{Radial localization}}
\]

\[
\downarrow
\]

\[
\boxed{\text{Population radial stability}}
\]

and independently:

\[
\boxed{\text{F₂ phase}}
\]

\[
\downarrow
\]

\[
\boxed{\text{Axial orientation}}
\]

\[
\downarrow
\]

\[
\boxed{\text{Population axial stability}}
\]

This gives two independent population-level tests of the same
radial-angular representation.

---

# Interpretation Boundary

The strongest defensible statement at this stage is:

> **The raw CLO-SKET population exhibits a radially concentrated
> second-harmonic component whose strongest radial expression
> tends to occur around an intermediate distance from the
> intensity-weighted centroid, while the corresponding F₂ axes
> show substantial concentration around the image vertical axis.**

This is a statement about **geometric organization**.

It should not yet be converted into a claim about semantic garment
structure.

---

# Transition Toward Semantic Analysis

The preceding cells have now established:

\[
\text{F₂ exists}
\]

\[
\downarrow
\]

\[
\text{F₂ has a measurable phase}
\]

\[
\downarrow
\]

\[
\text{F₂ defines an axial orientation}
\]

\[
\downarrow
\]

\[
\text{orientation is population-concentrated}
\]

\[
\downarrow
\]

\[
\text{F₂ strength is radially localized}
\]

\[
\downarrow
\]

\[
\text{radial peak locations are population-concentrated}
\]

The next question is therefore no longer:

> "Is there a geometric effect?"

The geometric evidence is now substantial enough to move forward.

The next scientifically meaningful question is:

> **Does this radial-angular organization vary systematically
> across garment categories?**

That transition must be tested rather than assumed.

---

# 🟢 CELL 16R — CORRECTED F₂ STABILITY AUDIT COMPLETE

## Established

- The primary F₂-dominant radial zone is independently recovered.
- Every sketch has a valid F₂ peak within that zone.
- The median sketch-level F₂ peak occurs at:
  \[
  r=21.5.
  \]
- 86.35% of sketches have their F₂ peak within ±6 radial units
  of the median.
- The population mean radial F₂ profile also peaks at \(r=21.5\).
- F₂ axes are recalculated directly from Fourier phase.
- Mean axial orientation is:
  \[
  87.82^\circ.
  \]
- Axial resultant concentration is:
  \[
  R=0.6725.
  \]
- 79.0% of sketches lie within \(15^\circ\) of the reference axis.
- Peak radius and peak F₂ strength show only a weak rank association:
  \[
  \rho=-0.136949.
  \]

## Critical distinction

\[
\boxed{
\text{Radial stability}
\neq
\text{Axial stability}
}
\]

Radial stability asks **where** the F₂ component occurs.

Axial stability asks **which direction** it prefers.

## Still deliberately unclaimed

\[
\boxed{
\text{No semantic interpretation.}
}
\]

\[
\boxed{
\text{No garment-part identity.}
}
\]

\[
\boxed{
\text{No category semantics.}
}
\]

\[
\boxed{
\text{No perceptual interpretation.}
}


# 🧪 CLO-SKET — RAW IMAGE RADIAL / ANGULAR GEOMETRY
## CELL 17 — CATEGORY-STRATIFIED F₂ GEOMETRIC ORGANIZATION AUDIT

---

## Objective

Cell 17 asks whether the radial-angular organization established
in Cells 11R–16R varies systematically across the 23 CLO-SKET
garment categories.

The analysis remains fully derived from the raw-image Fourier
representation.

The category labels are introduced **only at this stage** for
stratification and statistical description.

---

# Input Verification

Verified inputs:

- F₂ magnitude:
  \[
  (2300,72)
  \]

- F₂ phase:
  \[
  (2300,72)
  \]

- Radial bins:
  \[
  72
  \]

- Population:
  \[
  2300
  \]

\[
\boxed{\text{INPUTS VERIFIED}}
\]

---

# Category Label Recovery

Category source:

```text
categories

# 🧪 CLO-SKET — RAW IMAGE RADIAL / ANGULAR GEOMETRY
## CELL 18 — CATEGORY EFFECT ROBUSTNESS / PERMUTATION AUDIT

---

## Objective

Cell 18 tests whether the category-associated geometric effects
identified in Cell 17 are stronger than would be expected under
arbitrary category assignment.

The two pre-specified geometric features are:

1. peak radial location of F₂
2. peak magnitude of F₂

The test preserves every sketch's measured geometric properties
while randomly permuting only the category labels.

Therefore, the null hypothesis is:

> The observed association between category membership and the
> geometric feature is no stronger than would arise from arbitrary
> assignment of category labels.

This is a robustness test of the Cell 17 category effects.

---

# Input Verification

Verified inputs:

- F₂ magnitude:
  \[
  (2300,72)
  \]

- F₂ phase:
  \[
  (2300,72)
  \]

- radial bins:
  \[
  72
  \]

- population:
  \[
  2300
  \]

\[
\boxed{\text{INPUTS VERIFIED}}
\]

---

# Primary Radial Zone Recovery

The independently established primary F₂-dominant radial zone was
recovered:

\[
\boxed{
r=3.5\rightarrow27.5
}
\]

Number of radial shells:

\[
\boxed{25}
\]

The same radial coordinate system established in the preceding
cells is therefore retained.

---

# Sketch-Level Category Features

Valid sketches:

\[
\boxed{2300/2300}
\]

Number of categories:

\[
\boxed{23}
\]

Each category contains:

\[
\boxed{100\text{ sketches}}
\]

Thus the category design is balanced.

---

# Observed Category Effects

The observed category-associated variance was:

### Peak radial location

\[
\boxed{
\eta^2_{\mathrm{peak}\,r}=0.136880
}
\]

### Peak F₂ magnitude

\[
\boxed{
\eta^2_{\mathrm{peak}|F_2|}=0.412920
}
\]

These are the observed effect sizes against which the permutation
null distributions are evaluated.

---

# Permutation Null Design

Category labels were randomly permuted while keeping all
sketch-level geometric measurements unchanged.

For each permutation:

\[
\text{geometry}_i
\quad\text{remains fixed}
\]

while:

\[
\text{category}_i
\quad\text{is randomly reassigned}.
\]

The category-wise \(\eta^2\) statistic is then recalculated.

This generates the distribution of category effects expected under
the null hypothesis of arbitrary category assignment.

---

# Number of Permutations

Total permutations:

\[
\boxed{2000}
\]

Progress:

```text
500/2000
1000/2000
1500/2000
2000/2000


import pypandoc

markdown = r"""# CLO-SKET — Cell 19R Scientific Review

## Verdict

Cell 19R is the first genuinely important learning result.

It moves the analysis from:

> Categories differ geometrically.

to:

> The measured F₂ geometry contains information that can discriminate categories on unseen sketches.

The label-permutation control makes this substantially stronger.

---

## 1. What Cell 19R establishes

The experiment uses:

- 2,300 sketches
- 23 balanced categories
- 100 sketches per category
- Frozen primary F₂-dominant zone: **r = 3.5 → 27.5**
- Interpretable F₂-derived features
- Multinomial logistic regression
- Stratified 5-fold cross-validation

### R1 — Scalar F₂ Geometry

- Peak |F₂|
- Peak radius
- F₂ axial orientation

### R2 — Radial F₂ Geometry

- Complete radial |F₂(r)| profile

### R3 — Combined F₂ Geometry

- Radial |F₂(r)| profile
- Peak radius
- Peak |F₂|
- Axial orientation

---

## 2. Main result

| Representation | Accuracy | Macro-F1 |
|---|---:|---:|
| Chance | 0.0435 | ~0.0435 |
| R1 — Scalar F₂ | 0.1448 | 0.1200 |
| R2 — Radial F₂ | 0.1883 | 0.1784 |
| **R3 — Combined F₂** | **0.2235** | **0.2126** |

R3 achieves approximately:

\[
\frac{0.2235}{0.0435}\approx5.14
\]

times chance accuracy.

The important point is that this is **cross-validated, out-of-sample performance**, rather than training performance.

---

## 3. The permutation control is critical

Observed R3 macro-F1:

\[
\boxed{0.212596}
\]

Label-permutation null:

\[
\mu_{\mathrm{null}}=0.042080
\]

\[
\sigma_{\mathrm{null}}=0.004327
\]

\[
P_{95}=0.049833
\]

\[
\boxed{p_{\mathrm{perm}}=0.004975}
\]

Therefore, the observed category discrimination is far outside the distribution obtained when category labels are randomly reassigned.

### Supported conclusion

> **The F₂-derived representation contains reproducible category-discriminative information that generalizes to unseen sketches.**

This is substantially stronger than simply observing differences between category means.

---

## 4. R1 → R2 → R3 is scientifically interesting

The progression is:

\[
\boxed{R1 < R2 < R3}
\]

### R1

\[
\mathrm{MacroF1}=0.120
\]

Only three scalar descriptors are used.

### R2

\[
\mathrm{MacroF1}=0.178
\]

The complete radial F₂ profile produces a substantial improvement.

### R3

\[
\mathrm{MacroF1}=0.213
\]

Adding peak radius, peak magnitude, and axial orientation provides further improvement.

This suggests that the category-discriminative information is **not reducible to a single F₂ peak statistic**.

The radial organization of F₂ itself appears informative.

---

## 5. The confusion matrix is heterogeneous

The representation does not discriminate all 23 categories equally well.

### Higher-performing categories

| Category | F1 |
|---|---:|
| Blouse | 0.515 |
| Wide-Leg | 0.423 |
| Bermuda | 0.361 |
| Mini | 0.291 |
| Sarong | 0.289 |

### Lower-performing categories

| Category | F1 |
|---|---:|
| Harem | 0.058 |
| Tunic | 0.062 |
| Mermaid | 0.081 |
| Cardigan | 0.096 |
| Hoodie | 0.108 |

This is not a weakness to hide.

It tells us that the F₂ representation contains different amounts of category-discriminative information for different categories.

The representation is therefore **not a complete category representation**.

---

## 6. What we can claim

The paper can now reasonably state:

> **F₂-derived radial-angular geometry contains reproducible, out-of-sample category-discriminative information in fashion sketches.**

This is supported by:

1. Category-associated geometric effects
2. Permutation robustness
3. Cross-validated category discrimination
4. Label-permutation control

---

## 7. What we still cannot claim

We should **not yet** say:

> “F₂ learns the semantic language of fashion.”

That would go beyond the evidence.

We also cannot claim:

- F₂ corresponds to a particular garment part
- F₂ represents sleeves
- F₂ represents waist
- F₂ represents hem
- F₂ represents skirts
- F₂ has a human-defined semantic meaning
- The representation has learned garment morphology

The current result establishes **category-discriminative information**, not semantic interpretation.

---

## 8. The F₂ axis needs an ablation

Earlier analysis showed a strong population axial concentration around:

\[
87.8^\circ
\]

The axial variable is correctly represented using the doubled-angle formulation:

\[
(\cos 2\alpha,\sin 2\alpha)
\]

because the orientation is axial:

\[
\alpha\equiv\alpha+180^\circ
\]

However, the dataset is predominantly composed of upright sketches.

Therefore, an important question remains:

> **How much of the category discrimination actually comes from axial orientation?**

This does not invalidate Cell 19R.

It tells us that the contribution of each feature needs to be separated.

---

## 9. Cell 20 — Feature Ablation

Run the identical cross-validation procedure for:

### A. Radial profile only

\[
|F_2(r)|
\]

### B. Radial profile + peak radius

\[
|F_2(r)|+r_{\max}
\]

### C. Radial profile + peak magnitude

\[
|F_2(r)|+|F_2|_{\max}
\]

### D. Radial profile + axis

\[
|F_2(r)|+\alpha
\]

### E. Full R3

\[
|F_2(r)|+
r_{\max}+
|F_2|_{\max}+
\alpha
\]

Compare:

- Accuracy
- Macro-F1
- Per-category F1
- Permutation p-value

This will tell us **where the discriminative information actually resides**.

---

## 10. The more important control: Fourier-order ablation

We should also compare Fourier orders:

\[
F_0,\quad F_1,\quad F_2,\quad F_3,\ldots
\]

All should use the same:

- Cross-validation
- Classifier
- Feature dimensionality strategy
- Evaluation metrics
- Permutation control

The key question is:

> **Is F₂ unusually informative compared with other angular Fourier orders?**

If the answer is yes, the result becomes much stronger.

---

## 11. Current evidence ladder

### Stage 1 — Fourier representation

\[
A(r,\theta)\rightarrow F_k(r)
\]

Parseval consistency was verified.

### Stage 2 — F₂ population organization

F₂ shows:

- Localized radial magnitude
- Concentrated axial orientation
- Reproducible radial structure

### Stage 3 — Category-associated variation

\[
\eta^2_{\mathrm{peak\ radius}}=0.137
\]

\[
\eta^2_{\mathrm{peak}\ |F_2|}=0.413
\]

### Stage 4 — Category effects survive permutation

\[
p=0.0005
\]

for both primary geometric effects.

### Stage 5 — Geometry predicts unseen categories

\[
\boxed{\mathrm{R3\ MacroF1}=0.213}
\]

versus approximately:

\[
\boxed{\mathrm{chance}=0.043}
\]

with:

\[
\boxed{p_{\mathrm{label\ permutation}}=0.004975}
\]

---

# Final Verdict

## **Cell 19R absolutely stays.**

It is the first experiment demonstrating:

> **The F₂-derived geometric representation contains reproducible category-discriminative information that generalizes to unseen sketches.**

But the scientifically defensible claim remains:

\[
\boxed{\text{category-discriminative geometric information}}
\]

rather than:

\[
\boxed{\text{semantic understanding}}
\]

The next step is:

\[
\boxed{\textbf{CELL 20 — FEATURE + FOURIER-ORDER ABLATION}}
\]

That is the right experiment before moving further toward semantic learning.
"""

# Convert through pypandoc as required for Markdown generation.
out = "/mnt/data/CLO_SKET_Cell_19R_Review.md"
pypandoc.convert_text(markdown, "md", format="md", outputfile=out, extra_args=["--standalone"])
print(out)

# CLO-SKET — Cell 20 Review

## 1. Critical Problem Resolved

The initial Cell 20 revealed a representation/provenance mismatch.

The reconstructed Fourier magnitude from `conditional_angular` produced:

\[
\mathrm{mean\ peak}\ |F_2| \approx 0.644
\]

while the validated Cells 16–18 reported:

\[
\mathrm{mean\ peak}\ |F_2| = 0.040096
\]

This was not treated as a normalization problem to be solved by choosing
a convenient scaling factor.

Instead, the historical feature was traced back to its source.

### Provenance result

The forensic reconstruction established:

\[
\boxed{
\mathrm{peak\_F2}
=
\max(F2\_primary)
}
\]

with:

- Correlation = `1.000000`
- RMSE = `0`

Therefore the historical F₂ peak was reproduced exactly.

---

## 2. Canonical F₂ Representation

The authoritative magnitude representation for the descriptor chain is:

\[
m_i(r)=|F_{2,i}(r)|
\]

using the historically validated `F2_mag` object.

The descriptor domain is restricted to the independently established
primary F₂-dominant radial zone:

\[
r \in [3.5,27.5]
\]

with 25 radial shells.

### Important

The canonical representation is **not** reconstructed from the current
`conditional_fourier` object.

The historical `F2_mag` representation is retained to preserve
continuity with Cells 16–18.

---

## 3. Canonical Radial Descriptors

For each sketch, the canonical F₂ magnitude profile is:

\[
m(r)=|F_2(r)|
\]

within the primary radial zone.

The following descriptors are computed.

### 3.1 F₂ Integral

\[
I_{F_2}=\int m(r)\,dr
\]

Measures the total radial F₂ magnitude.

### 3.2 F₂ Radial Centroid

\[
\bar r=
\frac{\int r\,m(r)\,dr}
{\int m(r)\,dr}
\]

Measures the radial location around which F₂ magnitude is concentrated.

### 3.3 F₂ Radial Spread

\[
\sigma_r=
\sqrt{
\frac{
\int (r-\bar r)^2m(r)\,dr
}{
\int m(r)\,dr
}
}
\]

Measures radial dispersion of the F₂ magnitude.

### 3.4 F₂ Radial Concentration

The concentration descriptor measures the fraction of integrated F₂
magnitude contained within ±4 radial units of the sketch-specific peak:

\[
C_{F_2}=
\frac{
\int_{|r-r_{\max}|\le4}m(r)\,dr
}{
\int_{Z_{\mathrm{primary}}}m(r)\,dr
}
\]

where:

\[
r_{\max}=\arg\max_r m(r)
\]

The concentration window is evaluated within the primary F₂ zone.

### 3.5 F₂ Onset Radius

The onset is the first sampled radial shell satisfying:

\[
m(r)\ge0.10\,m_{\max}
\]

where:

\[
m_{\max}=\max_r m(r)
\]

Thus:

\[
r_{\mathrm{onset}}
=
\min
\left\{
r:m(r)\ge0.1m_{\max}
\right\}
\]

### 3.6 F₂ Termination Radius

The termination is the last sampled radial shell satisfying:

\[
m(r)\ge0.10\,m_{\max}
\]

Thus:

\[
r_{\mathrm{termination}}
=
\max
\left\{
r:m(r)\ge0.1m_{\max}
\right\}
\]

These are discrete shell-based measurements rather than continuous
crossing estimates.

### 3.7 F₂ Radial Extent

\[
E_{F_2}
=
r_{\mathrm{termination}}
-
r_{\mathrm{onset}}
\]

### 3.8 F₂ Peak Radius

\[
r_{\max}
=
\arg\max_r m(r)
\]

### 3.9 F₂ Peak Magnitude

\[
m_{\max}
=
\max_r m(r)
\]

---

## 4. Population Summary

The canonical descriptors produce:

| Descriptor | Mean | Median | SD | Min | Max |
|---|---:|---:|---:|---:|---:|
| F2_integral | 0.328129 | 0.332189 | 0.138104 | 0.031583 | 0.727492 |
| F2_radial_centroid | 17.450124 | 17.772461 | 2.265861 | 7.233670 | 25.979608 |
| F2_radial_spread | 6.092015 | 6.179478 | 0.946107 | 1.889004 | 8.402041 |
| F2_radial_concentration | 0.511414 | 0.510851 | 0.119824 | 0.200591 | 0.950632 |
| F2_onset_radius | 4.805652 | 3.500000 | 2.348695 | 3.500000 | 22.500000 |
| F2_termination_radius | 26.446087 | 27.500000 | 2.323108 | 11.500000 | 27.500000 |
| F2_radial_extent | 21.640435 | 23.000000 | 3.258851 | 5.000000 | 24.000000 |
| F2_peak_radius | 20.860870 | 21.500000 | 5.166496 | 3.500000 | 27.500000 |
| F2_peak_magnitude | 0.040096 | 0.039141 | 0.020387 | 0.003810 | 0.144782 |

---

## 5. Important Distinction: Population Profile vs Sketch-Level Peak

The population radial profile is:

\[
\bar m(r)=\frac{1}{N}\sum_i m_i(r)
\]

while the mean sketch-level peak is:

\[
\frac{1}{N}
\sum_i
\max_r m_i(r)
\]

Therefore:

\[
\boxed{
\max_r E[m_i(r)]
\neq
E[\max_r m_i(r)]
}
\]

The population profile peaks at approximately:

\[
|F_2|\approx0.018
\]

whereas the mean sketch-level peak magnitude is:

\[
0.040096.
\]

These quantities are different by definition and should not be treated
as contradictory.

---

## 6. Why the Radial Centroid Matters

Peak radius depends on a single radial shell:

\[
r_{\max}=\arg\max m(r)
\]

whereas the radial centroid uses the entire F₂ magnitude distribution:

\[
\bar r=
\frac{\int r\,m(r)\,dr}
{\int m(r)\,dr}
\]

Therefore two sketches can have similar peak radii while having
different radial distributions.

The descriptor family provides complementary information:

\[
\boxed{
\text{peak}
\rightarrow
\text{centroid}
\rightarrow
\text{spread}
\rightarrow
\text{support}
}
\]

---

## 7. Methodological Items to Lock Before Freezing Cell 20

### 7.1 Numerical integration

The notebook should explicitly document the numerical approximation used
for:

\[
\int m(r)\,dr
\]

For example:

\[
\int m(r)\,dr
\approx
\operatorname{trapz}(m(r),r)
\]

or the exact method actually implemented.

This affects:

- `F2_integral`
- `F2_radial_centroid`
- `F2_radial_spread`
- `F2_radial_concentration`

### 7.2 Concentration window

The ±4 radial-unit concentration window should explicitly state that
it is evaluated within the primary F₂ zone.

### 7.3 ComplexWarning

The following warning should be removed:

```text
ComplexWarning: Casting complex values to real discards the imaginary part
```

The canonical descriptor path should explicitly use:

\[
F_2(r)
\rightarrow
|F_2(r)|
\rightarrow
m(r)
\rightarrow
\text{descriptors}
\]

rather than relying on implicit complex-to-real casting.

---

## 8. What Should NOT Be Changed

Do **not** replace the validated `F2_mag` representation with the raw
magnitude reconstructed directly from `conditional_fourier`.

The forensic audit demonstrated that these are not numerically identical
representations.

The historically validated chain should therefore remain:

```text
historical F2_mag
        ↓
primary F₂ zone
        ↓
F2_primary
        ↓
peak_F2
        ↓
Cells 16–18
        ↓
Cell 20 descriptors
```

---

## 9. Scientific Status

### CELL 20 — ACCEPTED

The initial representation-scale discrepancy was real, but it has now
been resolved through provenance tracing rather than arbitrary
renormalization.

The critical identity is:

\[
\boxed{
\mathrm{peak\_F2}
=
\max(F2\_primary)
}
\]

with:

\[
\boxed{
\mathrm{correlation}=1.0,\qquad
\mathrm{RMSE}=0
}
\]

The resulting descriptor family is:

\[
\boxed{
|F_2(r)|
\rightarrow
\{
\text{amount},
\text{location},
\text{spread},
\text{concentration},
\text{support},
\text{peak}
\}
}
\]

No category information is used.

No semantic label is assigned.

No classifier is trained.

No clustering is performed.

No image thresholding is performed.

No image resizing is performed.

No rotation is performed.

---

## 10. Next Step

The next cell should introduce the angular component separately:

# CELL 21 — α₂ RADIAL / AXIAL DESCRIPTORS

with:

\[
\alpha_2(r)
=
-\frac{\phi_2(r)}{2}
\pmod{180^\circ}
\]

The radial magnitude and angular orientation should remain separate
descriptor families initially.

They can then be combined in **Cell 22** to construct radial–angular
relational features.

```text
CELL 20
    ↓
|F₂(r)| radial descriptors
    ↓
CELL 21
    ↓
α₂(r) axial descriptors
    ↓
CELL 22
    ↓
radial–angular relational features
    ↓
CELL 23
    ↓
feature-family correlation / redundancy audit
    ↓
CELL 24
    ↓
controlled category discrimination
```

**CELL 20 IS READY TO FREEZE AFTER THE THREE SMALL METHOD FIXES ABOVE.**


# CLO-SKET — CELL 21
## α₂ RADIAL / AXIAL DESCRIPTOR CONSTRUCTION

---

## 1. Input Verification

| Input | Shape / Value |
|---|---|
| F₂ magnitude source | `F2_mag` |
| F₂ magnitude shape | `(2300, 72)` |
| Complex F₂ source | `F2_radial` |
| Complex F₂ shape | `(2300, 72)` |
| Radial centers | `(72,)` |
| Population | `2300` |

**Status:** 🟢 Input objects verified.

---

## 2. Complex F₂ / Magnitude Consistency

The preserved complex F₂ field is checked against the canonical
magnitude representation.

\[
|F_2(r)| = F2\_mag
\]

### Result

- Maximum absolute difference: `0.000000000000e+00`
- Mean absolute difference: `0.000000000000e+00`

**Status:** 🟢 Complex F₂ magnitude exactly matches `F2_mag`.

This confirms that the complex field used to recover phase is consistent
with the canonical magnitude representation established in Cell 20.

---

## 3. Primary F₂ Radial Zone

The independently established primary F₂-dominant radial zone is:

\[
r \in [3.5,27.5]
\]

with:

- Radial shells: `25`
- Lower bound: `3.5`
- Upper bound: `27.5`

**Status:** 🟢 Established zone recovered.

---

# 4. Canonical F₂ Phase Recovery

The previously available object `f2_phase` has shape:

```text
(72,)
```

and therefore represents a radial-level quantity rather than the required
sketch × radial phase field.

It is **not used** in Cell 21.

The sketch-level phase is recovered directly from the preserved complex
F₂ field:

\[
\phi_2(i,r)=\arg(F_2(i,r))
\]

### Recovered phase

```text
shape = (2300, 25)
```

Phase range:

\[
-\pi \leq \phi_2 \leq \pi
\]

Numerically:

```text
-3.141593 → 3.141593 radians
```

**Status:** 🟢 Sketch-level F₂ phase recovered.

---

# 5. Axial Orientation

For the second Fourier harmonic:

\[
F_2(r)
=
|F_2(r)|
\exp(i\phi_2(r))
\]

the corresponding two-fold positive axis is:

\[
\boxed{
\alpha_2(r)
=
-\frac{\phi_2(r)}{2}
}
\]

Because this is an **axial orientation**, orientations separated by
\(180^\circ\) are equivalent:

\[
\alpha_2
\equiv
\alpha_2+180^\circ
\]

Therefore:

\[
\boxed{
\alpha_2\in[0^\circ,180^\circ)
}
\]

The resulting axial orientation field has shape:

```text
(2300, 25)
```

**Status:** 🟢 Axial orientation field constructed.

---

# 6. Axial Field Validity

| Quantity | Result |
|---|---:|
| Valid sketches | `2300 / 2300` |
| Mean valid radial fraction | `1.000000` |

**Status:** 🟢 All sketches valid.

---

# 7. Sketch-Level F₂ Peak

The strongest F₂ radial location and corresponding orientation are
summarized below.

| Quantity | Value |
|---|---:|
| Median peak radius | `21.5000` |
| Mean peak radius | `20.8609` |
| Mean peak \(|F_2|\) | `0.040096` |
| Mean α₂ at peak | `92.0024°` |

The peak orientation is evaluated at each sketch's individual strongest
F₂ radial shell.

---

# 8. Axial Circular Coherence

Because \(\alpha_2\) is an axial quantity, ordinary circular statistics
cannot be applied directly.

The orientation is therefore doubled:

\[
\beta = 2\alpha_2
\]

The F₂ magnitude is used as the radial weight.

The axial concentration statistic is:

\[
R_2
=
\frac{
\left|
\sum_r
m(r)
\exp(i2\alpha_2(r))
\right|
}{
\sum_r m(r)
}
\]

where:

\[
m(r)=|F_2(r)|
\]

### Interpretation

\[
R_2\rightarrow1
\]

indicates strong axial coherence.

\[
R_2\rightarrow0
\]

indicates dispersed axial orientation.

### Population results

| Statistic | Value |
|---|---:|
| Mean axial coherence \(R_2\) | `0.666147` |
| Median axial coherence \(R_2\) | `0.727217` |

The population therefore shows substantial but non-uniform axial
organization.

---

# 9. Axial Circular Dispersion

The resulting axial circular dispersion is:

| Statistic | Value |
|---|---:|
| Mean axial dispersion | `25.8294°` |
| Median axial dispersion | `22.8656°` |

Lower dispersion corresponds to stronger concentration around a common
axial direction.

---

# 10. Radial Axial Deviation

The F₂-weighted RMS deviation from the preferred axial orientation is:

| Statistic | Value |
|---|---:|
| Mean weighted RMS deviation | `28.5916°` |
| Median weighted RMS deviation | `27.8103°` |

This measures how strongly the axial orientation varies around the
sketch-specific preferred direction across the radial F₂ support.

---

# 11. Axial Orientation Persistence

Persistence measures the F₂-weighted fraction of radial support remaining
within a specified angular deviation from the preferred axis.

Three thresholds are evaluated:

\[
15^\circ,\quad30^\circ,\quad45^\circ
\]

### Population results

| Threshold | Mean persistence |
|---|---:|
| ≤ 15° | `0.715155` |
| ≤ 30° | `0.808190` |
| ≤ 45° | `0.848003` |

Thus, on average:

- approximately `71.5%` of weighted radial support lies within `15°`;
- approximately `80.8%` lies within `30°`;
- approximately `84.8%` lies within `45°`.

These are geometric persistence measures and are not semantic labels.

---

# 12. Radial Orientation Drift

Orientation drift measures the change in axial orientation across the
radial F₂ support.

| Statistic | Value |
|---|---:|
| Mean orientation drift | `37.7145°` |
| Median orientation drift | `30.2122°` |

This quantity captures radial variation in the preferred F₂ axis rather
than the absolute orientation of the sketch.

---

# 13. Descriptor Validity

| Descriptor | Valid |
|---|---:|
| `alpha2_peak_deg` | `2300 / 2300` |
| `alpha2_weighted_mean_deg` | `2300 / 2300` |
| `alpha2_axial_coherence` | `2300 / 2300` |
| `alpha2_axial_dispersion_deg` | `2300 / 2300` |
| `alpha2_persistence_15deg` | `2300 / 2300` |
| `alpha2_persistence_30deg` | `2300 / 2300` |
| `alpha2_persistence_45deg` | `2300 / 2300` |
| `alpha2_orientation_drift_deg` | `2300 / 2300` |
| `alpha2_weighted_rms_deviation_deg` | `2300 / 2300` |
| `alpha2_peak_radius` | `2300 / 2300` |
| `F2_peak_magnitude` | `2300 / 2300` |

**Status:** 🟢 All descriptors valid for all 2300 sketches.

---

# 14. Population α₂ Descriptor Summary

| Descriptor | Mean | Median | SD | Min | Max |
|---|---:|---:|---:|---:|---:|
| `alpha2_peak_deg` | 92.002429 | 87.695673 | 32.533860 | 0.015857 | 179.941513 |
| `alpha2_weighted_mean_deg` | 88.565165 | 87.368314 | 23.296564 | 0.492103 | 179.528943 |
| `alpha2_axial_coherence` | 0.666147 | 0.727217 | 0.237000 | 0.006798 | 0.999770 |
| `alpha2_axial_dispersion_deg` | 25.829384 | 22.865619 | 13.644809 | 0.615113 | 90.512305 |
| `alpha2_persistence_15deg` | 0.715155 | 0.780641 | 0.226119 | 0.000000 | 1.000000 |
| `alpha2_persistence_30deg` | 0.808190 | 0.849981 | 0.158289 | 0.015120 | 1.000000 |
| `alpha2_persistence_45deg` | 0.848003 | 0.880710 | 0.122308 | 0.398889 | 1.000000 |
| `alpha2_orientation_drift_deg` | 37.714504 | 30.212188 | 30.480099 | 0.000000 | 90.000000 |
| `alpha2_weighted_rms_deviation_deg` | 28.591560 | 27.810276 | 11.610182 | 0.615118 | 59.459557 |
| `alpha2_peak_radius` | 20.860870 | 21.500000 | 5.166496 | 3.500000 | 27.500000 |
| `F2_peak_magnitude` | 0.040096 | 0.039141 | 0.020387 | 0.003810 | 0.144782 |

---

# 15. Output Objects

## `alpha2_radial`

Sketch-level axial orientation field:

```text
shape = (2300, 25)
```

---

## `phase_radial`

Canonical sketch-level F₂ phase restricted to the primary F₂ zone.

---

## `alpha2_descriptors`

One descriptor row per sketch.

---

## `alpha2_summary`

Population-level descriptor statistics.

---

## `alpha2_peak_deg`

Axial orientation at the strongest F₂ radial location.

---

## `alpha2_weighted_deg`

F₂-weighted preferred axial orientation.

---

## `axial_coherence`

F₂-weighted axial concentration:

\[
R_2
=
\frac{
|\sum m(r)e^{i2\alpha_2(r)}|
}{
\sum m(r)
}
\]

---

## `axial_dispersion_deg`

Axial circular dispersion.

---

## `alpha2_persistence_15deg`

F₂-weighted persistence within \(15^\circ\) of the preferred axis.

---

## `alpha2_persistence_30deg`

F₂-weighted persistence within \(30^\circ\) of the preferred axis.

---

## `alpha2_persistence_45deg`

F₂-weighted persistence within \(45^\circ\) of the preferred axis.

---

## `orientation_drift_deg`

Axial orientation change across radial support.

---

## `population_alpha2_deg`

Population radial orientation profile.

---

## `population_R2`

Population radial axial coherence profile.

---

# 16. Canonical Provenance

The Cell 21 provenance chain is:

```text
Complex F₂ field
      ↓
F2_radial
      ↓
arg(F2_radial)
      ↓
φ₂(r)
      ↓
-φ₂(r) / 2
      ↓
α₂(r) mod 180°
```

The magnitude chain remains:

```text
Complex F₂ field
      ↓
|F2_radial|
      ↓
F2_mag
      ↓
Cell 20 canonical F₂ magnitude
```

The two representations are explicitly checked for consistency.

---

# 17. Cell 20 → Cell 21

Cell 20 described the **radial magnitude organization** of F₂:

- total F₂ magnitude
- radial location
- radial spread
- radial concentration
- radial support
- radial peak
- peak magnitude

Cell 21 describes the **axial orientation organization** of F₂:

- axial orientation
- axial coherence
- axial dispersion
- orientation persistence
- radial orientation drift
- weighted angular deviation

Thus:

\[
\boxed{
\text{Cell 20}
=
\text{radial magnitude geometry}
}
\]

and

\[
\boxed{
\text{Cell 21}
=
\text{radial axial geometry}
}
\]

These remain separate descriptor families at this stage.

---

# 18. Important Representation Decision

The previously available object:

```text
f2_phase
shape = (72,)
```

is **not** used.

It does not contain sketch-specific phase information.

Instead, Cell 21 derives the required phase directly from:

```text
F2_radial
shape = (2300, 72)
```

through:

\[
\phi_2(i,r)=\arg(F2\_radial(i,r))
\]

This preserves sketch-level phase information and prevents accidental
use of a population-level radial quantity as if it were an individual
sketch field.

---

# 19. No Category Information

Cell 21 is entirely category-independent.

No category labels are used.

No classifier is trained.

No semantic label is assigned to α₂.

No clustering is performed.

No category-specific optimization is performed.

The analysis remains purely geometric.

---

# 20. Scientific Interpretation

The current results establish that the F₂ representation contains two
distinct measurable forms of organization:

### Radial organization

Where the F₂ magnitude is concentrated:

\[
|F_2(r)|
\]

### Axial organization

How the corresponding two-fold axis is oriented:

\[
\alpha_2(r)
=
-\frac{\phi_2(r)}{2}
\pmod{180^\circ}
\]

The population-level results indicate:

\[
R_2 \approx 0.666
\]

with a median of:

\[
R_2 \approx 0.727
\]

This indicates non-random but heterogeneous axial organization across
the sketch population.

The orientation is not perfectly constant with radius, as reflected by:

\[
\text{mean drift}\approx37.7^\circ
\]

and:

\[
\text{mean weighted RMS deviation}\approx28.6^\circ.
\]

Therefore the F₂ axis is better characterized as a **dominant but
radially variable axial organization**, rather than a perfectly fixed
global axis.

This remains a geometric statement.

It does not establish:

- garment-part identity
- semantic meaning
- category identity
- perceptual interpretation
- causality

---

# 21. Generating Visualizations

The following visualizations are produced by Cell 21:

1. **α₂ at individual F₂ peaks**
2. **Population axial dispersion**
3. **Population α₂ radial profile**

These provide complementary views of:

\[
\text{peak orientation}
\]

\[
\text{sketch-level angular variability}
\]

and

\[
\text{population radial orientation stability}.
\]

---

# 22. Cell 21 Scientific Status

## 🟢 CELL 21 — α₂ RADIAL / AXIAL DESCRIPTOR AUDIT COMPLETE

The canonical phase provenance is:

\[
\boxed{
F2\_radial
\rightarrow
\arg(F2\_radial)
\rightarrow
\phi_2
\rightarrow
-\phi_2/2
\rightarrow
\alpha_2
}
\]

The canonical magnitude remains:

\[
\boxed{
F2\_mag
}
\]

and the two representations are numerically consistent.

The resulting descriptor family captures:

\[
\boxed{
\text{orientation}
+
\text{coherence}
+
\text{dispersion}
+
\text{persistence}
+
\text{radial drift}
}
\]

No category information is used.

No semantic labels are assigned.

No classifier is trained.

No clustering is performed.

---

# 23. Next Scientific Step

## CELL 22 — RADIAL–ANGULAR RELATIONAL FEATURES

Cell 22 will explicitly couple the two independently validated
descriptor families:

```text
CELL 20
    ↓
F₂ radial magnitude descriptors
    +
CELL 21
    ↓
α₂ axial orientation descriptors
    ↓
CELL 22
    ↓
radial–angular relational features
```

Candidate relational quantities include:

- magnitude-weighted orientation persistence
- orientation change per radial distance
- F₂ concentration × axial coherence
- radial location × axial stability
- magnitude–orientation coupling

These relational quantities are deliberately **not** constructed in
Cell 21.

The purpose of Cell 21 is to establish the angular descriptor family
independently before coupling it to radial magnitude structure.

---

# 24. Final Cell 21 Chain

```text
RAW SKETCH
    ↓
INTENSITY CENTROID
    ↓
RADIAL SHELLS
    ↓
CONDITIONAL ANGULAR MASS
    ↓
FOURIER DECOMPOSITION
    ↓
COMPLEX F₂
    ├──→ |F₂| → F2_mag → CELL 20
    │
    └──→ arg(F₂) → φ₂ → α₂ → CELL 21
                              ↓
                       axial descriptors
                              ↓
                           CELL 22
                              ↓
                  radial–angular relations
```

**CELL 21 IS COMPLETE AND READY FOR CELL 22.**


# CLO-SKET — CELL 22A
## SINGLE vs TWO-COMPONENT AXIAL CIRCULAR MODEL AUDIT

---

## 1. Input Verification

| Input | Shape / Value |
|---|---|
| `conditional_angular` | `(2300, 72, 72)` |
| `F2_mag` | `(2300, 72)` |
| `radial_centers` | `(72,)` |
| Population | `2300` |
| Angular bins | `72` |

**Status:** 🟢 Input objects verified.

---

## 2. Primary F₂ Radial Zone

The established primary F₂-dominant radial zone is:

\[
r \in [3.5,27.5]
\]

with:

- Radial shells: `25`
- Lower bound: `3.5`
- Upper bound: `27.5`

**Status:** 🟢 Established zone recovered.

---

## 3. Observed Angular Probability Distribution

For each sketch and radial shell, the conditional angular distribution
is normalized as:

\[
p(\theta\mid r)
\]

### Validation

| Quantity | Result |
|---|---:|
| Valid sketch × radial shells | `57500 / 57500` |
| Mean angular normalization | `1.000000` |

**Status:** 🟢 \(p(\theta\mid r)\) constructed.

---

# 4. Axial Circular Models

Two competing models are evaluated.

## Model K = 1

A single axial von Mises distribution:

\[
p(\theta)
=
VM_{\mathrm{axial}}(\mu,\kappa)
\]

---

## Model K = 2

A two-component axial von Mises mixture:

\[
p(\theta)
=
\pi VM_{\mathrm{axial}}(\mu_1,\kappa_1)
+
(1-\pi)VM_{\mathrm{axial}}(\mu_2,\kappa_2)
\]

The mixture introduces additional parameters and is therefore evaluated
using complexity-adjusted model selection.

---

# 5. Model Fitting

The two models were fitted at each sketch's F₂ peak shell.

| Quantity | Result |
|---|---:|
| Sketch-level peak-shell fits | `2300 / 2300` |

**Status:** 🟢 Model fitting complete.

---

# 6. Model Comparison at Sketch-Specific F₂ Peak

The models are compared using:

- log likelihood
- KL divergence
- angular MAE
- BIC

The primary complexity-adjusted criterion is BIC.

\[
BIC = -2\log L + k\log n
\]

where \(k\) is the number of fitted parameters.

Lower BIC indicates the preferred model after accounting for model
complexity.

### Results

| Metric | Result |
|---|---:|
| Mean ΔBIC `(K1 − K2)` | `-12.680165` |
| Median ΔBIC | `-12.718293` |
| Mixture BIC wins | `0.0000` |
| Mean KL improvement | `0.074917` |
| Mean MAE improvement | `0.001063` |

Because:

\[
\Delta BIC = BIC_{K1}-BIC_{K2}
\]

negative values indicate that the single-component model has the lower
BIC.

Therefore:

\[
\boxed{\text{K = 1 is preferred}}
\]

at the sketch-specific F₂ peak shells.

---

# 7. Mixture Degeneracy Audit

Although the two-component model is not preferred by BIC, its fitted
components were examined for numerical degeneracy.

| Quantity | Result |
|---|---:|
| Median smaller component weight | `0.224042` |
| Fraction weight < 0.05 | `0.089565` |
| Median component separation | `52.274363°` |
| Fraction separation < 10° | `0.099130` |
| Median \(\kappa_1\) | `1.232475` |
| Median \(\kappa_2\) | `9.198372` |

The mixture therefore does not simply collapse universally into one
component. However, its additional flexibility is not supported by the
complexity-adjusted BIC comparison.

---

# 8. Population Radial Model Audit

The same model comparison was performed independently at every radial
shell within the primary zone.

| Quantity | Result |
|---|---:|
| Population radial shells fitted | `25` |
| Mean ΔBIC `(K1 − K2)` | `-12.826105` |
| Mixture BIC wins across shells | `0 / 25` |

Thus, the population radial audit provides the same model-selection
result:

\[
\boxed{\text{K = 1 is preferred}}
\]

across the established radial zone.

---

# 9. Scientific Interpretation

The question is:

> Is the observed angular probability distribution adequately described
> by a single axial mode, or does it require multiple axial modes?

The results strongly favor the simpler representation.

If K = 1 is preferred:

\[
p(\theta\mid r)
\approx
VM_{\mathrm{axial}}(\mu(r),\kappa(r))
\]

This means that the first axial circular mode provides an adequate
complexity-adjusted description of the observed angular organization.

The data do **not** provide BIC support for retaining a two-component
axial mixture.

---

# 10. Important Distinction

A second statistical angular mode, even if present, would **not**
automatically correspond to:

- a sleeve
- a waist
- a skirt
- a hem
- a collar
- a garment part
- any other semantic component

It would only represent:

\[
\boxed{
\text{a latent angular mode of }p(\theta\mid r)
}
\]

Therefore no semantic interpretation is assigned to the mixture
components.

---

# 11. Model Selection Decision

The Cell 22A decision is:

```text
K = 1 axial model
        ↓
preferred by BIC
        ↓
K = 2 mixture rejected
        ↓
single-axial representation retained

# CLO-SKET — CELL 23
## FEATURE-FAMILY CORRELATION / REDUNDANCY AUDIT

---

## 1. Scientific Purpose

Cell 23 asks:

> Do the geometric descriptor families developed in Cells 20–22
> contain overlapping information, or do they provide complementary
> measurements of the sketch representation?

This is an **audit**, not a classification experiment.

The analysis is performed before category discrimination so that the
feature representation can be understood and frozen independently of
category performance.

---

# 2. Feature-Family Architecture

The current representation consists of five feature families.

| Family | Scientific role |
|---|---|
| **F₂ radial** | Magnitude and radial organization |
| **α₂ axial** | Axial orientation and orientation stability |
| **Observed circular** | Directly observed angular organization |
| **Learned circular** | Population-level predicted angular organization |
| **Relational** | Coupling between radial F₂ magnitude and angular organization |

The complete canonical representation contains:

\[
\boxed{28\text{ scalar features}}
\]

for:

\[
2300
\]

sketches.

---

# 3. Important Development History

The first Cell 23 audit recovered only the F₂ radial family:

```text
F2_radial
    9 features

alpha2_axial
    0 features

observed_circular
    0 features

learned_circular
    0 features

relational
    0 features

# CLO-SKET — CELL 24
## CONTROLLED CATEGORY DISCRIMINATION

---

## 1. Scientific Purpose

Cell 24 introduces category labels for the first time.

The scientific question is:

> How much category-discriminative information is contained in the
> different geometric feature families?

Cells 20–23C constructed and audited the representation without using
category labels.

Cell 24 therefore provides the first controlled test of whether the
learned radial–angular representation contains information that
distinguishes garment categories.

---

# 2. Input Verification

Canonical descriptor matrix:

\[
X_{\mathrm{canonical}}
\in
\mathbb{R}^{2300\times28}
\]

Therefore:

```text
Population        : 2300
Canonical descriptors : 28

# 🧪 CELL 25 — LEAN PERMUTATION + CROSS-VALIDATION ROBUSTNESS

## Scientific Question

Does each additional feature family provide category-discriminative information beyond the canonical **F₂ radial baseline**?

---

## Primary Baseline

**F₂ radial only**

---

## Experimental Design

We use a paired permutation test.

For each permutation:

- Category labels are shuffled.
- Features remain unchanged.
- The classifier remains unchanged.
- The cross-validation folds remain unchanged.

The incremental quantity is:

\[
\Delta BA =
BA(\text{augmented representation})
-
BA(F_2)
\]

The null hypothesis is:

> The additional feature family provides no systematic category-discriminative information beyond F₂.

---

## Tested Feature Additions

1. **F₂ + α₂**
2. **F₂ + observed circular**
3. **F₂ + learned circular**
4. **F₂ + relational**
5. **All canonical families**

---

## Cross-Validation

- 5-fold stratified cross-validation
- Fixed random state: **42**
- CV folds locked
- Number of permutations: **100** for the fast robustness audit

---

## Observed Performance

| Representation | Balanced Accuracy | Incremental ΔBA |
|---|---:|---:|
| F₂ radial only | 0.253913 | — |
| F₂ + α₂ | 0.281739 | +0.027826 |
| F₂ + observed circular | 0.292174 | +0.038261 |
| F₂ + learned circular | 0.279130 | +0.025217 |
| F₂ + relational | 0.288261 | +0.034348 |
| **All canonical families** | **0.333043** | **+0.079130** |

---

## Permutation Results

| Comparison | Observed ΔBA | Null Mean | Null SD | Null 2.5% | Null 97.5% | Permutation p |
|---|---:|---:|---:|---:|---:|---:|
| F₂ + α₂ | +0.027826 | −0.000580 | 0.005566 | −0.011279 | 0.010480 | 0.0099 |
| F₂ + observed circular | +0.038261 | +0.000437 | 0.004670 | −0.008335 | 0.008799 | 0.0099 |
| F₂ + learned circular | +0.025217 | −0.000174 | 0.004520 | −0.008705 | 0.008226 | 0.0099 |
| F₂ + relational | +0.034348 | +0.000221 | 0.004941 | −0.008669 | 0.008799 | 0.0099 |
| **All canonical families** | **+0.079130** | **+0.000261** | **0.006232** | **−0.011196** | **0.012157** | **0.0099** |

---

## Interpretation

All tested feature-family additions produced positive incremental balanced-accuracy gains over the F₂ radial baseline.

The observed gains were substantially larger than the corresponding label-permutation null distributions.

In particular, the complete canonical representation improved balanced accuracy by:

\[
\Delta BA = +0.079130
\]

relative to F₂ radial geometry alone.

The permutation null for this comparison was centered near zero:

\[
\mu_{\mathrm{null}} = 0.000261
\]

with a 95% permutation interval of:

\[
[-0.011196,\;0.012157]
\]

The observed improvement therefore lies well outside the permutation null range.

---

## Statistical Caution

Because only **100 permutations** were used, the minimum attainable corrected permutation p-value is:

\[
p_{\min} = \frac{1}{101} \approx 0.0099
\]

Therefore, this experiment should be treated as a **fast robustness audit**, rather than the final high-resolution permutation analysis.

For the final paper-level analysis, repeat the same locked experiment with:

\[
\boxed{1000\text{ permutations}}
\]

without changing the representation, classifier, CV folds, or analysis procedure.

---

## Scientific Conclusion

The permutation audit provides evidence that the additional geometric feature families contain **systematic category-discriminative information beyond the canonical F₂ radial representation**.

The result supports the interpretation that category information is not captured entirely by radial geometry and that additional angular, circular, and relational descriptors contribute measurable discriminative information.

This result does **not** by itself establish a complete semantic grammar of fashion sketches.

---

## Next Cell

### CELL 26 — CATEGORY-WISE ANALYSIS

Investigate:

- Confusion matrix
- Precision
- Recall
- F1
- Category-wise performance
- Which categories benefit most from angular geometry

# 🧪 CELL 27 — CONTROLLED FEATURE-FAMILY ABLATION

## Scientific Question

How much does each feature family contribute to the complete geometric representation?

The experiment asks whether removing an entire feature family causes a measurable loss in category discrimination.

---

## Complete Representation

The canonical representation contains five feature families:

\[
X_{\mathrm{ALL}}
=
X_{F_2}
+
X_{\alpha_2}
+
X_{\mathrm{obs}}
+
X_{\mathrm{learned}}
+
X_{\mathrm{relational}}
\]

with:

| Feature family | Features |
|---|---:|
| F₂ radial | 9 |
| α₂ axial | 7 |
| Observed circular | 3 |
| Learned circular | 4 |
| Relational | 5 |
| **Total** | **28** |

The canonical representation was frozen before category discrimination.

---

## Ablation Design

Each feature family is removed independently:

\[
\mathrm{ALL} - F_2
\]

\[
\mathrm{ALL} - \alpha_2
\]

\[
\mathrm{ALL} - \mathrm{observed\ circular}
\]

\[
\mathrm{ALL} - \mathrm{learned\ circular}
\]

\[
\mathrm{ALL} - \mathrm{relational}
\]

The complete representation is retained as the reference condition.

---

## Classifier

The same fixed classifier is used for every representation:

```text
StandardScaler
      ↓
Multinomial Logistic Regression


### 🔴 One thing I want us to fix before Cell 28

Bro, **don't blindly move on yet**. There is a reproducibility issue worth fixing now:

- Cell 24: `ALL canonical families = 0.3330`, **30 classifier inputs**
- Cell 27: `ALL canonical families = 0.3374`, **28 features**

That's explainable by the axial encoding, **but only if the code actually evaluates different matrices**. We should document that distinction explicitly in the notebook and make Cell 28 use the **same representation/evaluation convention throughout**.

That will make the eventual paper much harder for a reviewer to poke holes in.

# 🧪 CELL 25 — PERMUTATION + CROSS-VALIDATION ROBUSTNESS

## Scientific Question

Are the category-discriminative gains observed in Cell 24 larger than expected when category labels are unrelated to the geometric representation?

---

## Input Verification

```text
🟢 X_cell24_feature_sets
🟢 cell24_results
🟢 cell24_incremental
🟢 category_labels

Population : 2300
Feature sets : 11

# 🧪 CLO-SKET — CELL 26
# CATEGORY-WISE DISCRIMINATION DIAGNOSTICS

---

## Input Verification

```text
🟢 X_cell24_feature_sets
🟢 cell24_results
🟢 category_labels
🟢 cv_splits

Categories : 23
Samples    : 2300

ALL matrix : (2300, 30)
F₂ matrix  : (2300, 9)

🟢 DIAGNOSTIC INPUTS VERIFIED

CELL 20
    canonical F₂ radial geometry
        ↓
CELL 21
    α₂ axial geometry
        ↓
CELL 22A
    single vs two-component axial model audit
        ↓
CELL 22B
    learned single-axial relationship
        ↓
CELL 23B / 23C
    feature-family redundancy audit
    canonical feature-set lock
        ↓
CELL 24
    controlled category discrimination
        ↓
CELL 25
    permutation robustness
        ↓
CELL 26
    category-wise diagnostics
        ↓
CELL 27
    feature-family ablation
        ↓
CELL 28
    final statistical synthesis

# 🧪 CLO-SKET — CELL 28
# FINAL STATISTICAL / SCIENTIFIC SYNTHESIS

---

## Result Object Verification

```text
🟢 cell24_results
🟢 cell24_incremental
🟢 cell24_primary
🟢 cell25_permutation_summary
🟢 cell26_global_metrics
🟢 cell26_category_metrics
🟢 cell26_category_delta
🟢 cell26_top_confusion_pairs
🟢 cell26_confusion_reduction
🟢 cell27b_results
🟢 cell27b_family_impact
```

---

# CELL 24 — PRIMARY DISCRIMINATION

| Quantity | Value |
|---|---:|
| F₂ radial baseline BA | 0.253913 |
| ALL representation BA | 0.333043 |
| Observed ΔBA | **+0.079130** |

---

# CELL 24 ↔ CELL 25 CONSISTENCY

```text
Cell 24 ΔBA : +0.079130
Cell 25 ΔBA : +0.079130
Difference   : +0.0000000000

🟢 OBSERVED GAIN REPRODUCED
```

---

# CELL 25 — PERMUTATION ROBUSTNESS

| Quantity | Value |
|---|---:|
| Permutations | 1000 |
| Observed ΔBA | +0.079130 |
| Null mean | +0.000008 |
| Null SD | 0.005845 |
| Null 95% CI | [-0.011407, +0.011239] |
| Permutation p | **0.000999** |

```text
🟢 OBSERVED GAIN SEPARATES FROM NULL
```

---

# CELL 26 — CATEGORY-WISE DIAGNOSTICS

| Quantity | Value |
|---|---:|
| Categories | 23 |
| Categories improved | **22/23** |
| Categories unchanged | 0/23 |
| Categories declined | 1/23 |
| Mean ΔF1 | +0.089610 |
| Median ΔF1 | +0.067019 |
| Best ALL category | Bermuda (F1=0.5767) |
| Lowest ALL category | Harem (F1=0.0854) |

---

# CELL 26 — STRONGEST REMAINING CONFUSIONS

| Category A | Category B | A→B | B→A | Combined Confusion |
|---|---|---:|---:|---:|
| Blouse | Wide-Leg | 16 | 21 | 37 |
| Flare | Skinny | 18 | 18 | 36 |
| A-Line | Wide-Leg | 24 | 11 | 35 |
| A-Line | Bermuda | 22 | 12 | 34 |
| Skinny | Straight | 22 | 12 | 34 |
| Jacket | Shirt | 17 | 11 | 28 |
| Bermuda | Wide-Leg | 15 | 12 | 27 |
| A-Line | Blouse | 11 | 16 | 27 |
| Cardigan | Suit | 18 | 9 | 27 |
| Flare | Straight | 14 | 11 | 25 |

---

# CELL 26 — LARGEST CONFUSION REDUCTIONS

| Category Pair | F₂ Confusion | ALL Confusion | Reduction |
|---|---:|---:|---:|
| Mini ↔ T-shirt | 31 | 14 | **17** |
| Sarong ↔ Skinny | 29 | 14 | **15** |
| Shirt ↔ Suit | 33 | 21 | **12** |
| T-shirt ↔ Vest | 16 | 4 | **12** |
| Cardigan ↔ Jumpsuit | 13 | 3 | **10** |
| Bermuda ↔ Wide-Leg | 37 | 27 | **10** |
| Skinny ↔ Vest | 13 | 3 | **10** |
| Jacket ↔ Suit | 20 | 11 | **9** |
| Jumpsuit ↔ Shirt | 10 | 2 | **8** |
| Jumpsuit ↔ Suit | 14 | 6 | **8** |

---

# CELL 24 ↔ CELL 27B CONSISTENCY

```text
Cell 24 ALL BA  : 0.333043
Cell 27B ALL BA : 0.333043
Difference      : +0.0000000000

🟢 REPRESENTATION CONSISTENCY PASSED
```

---

# CELL 27B — FAMILY CONTRIBUTION RANKING

| Removed Family | ALL BA | BA Without Family | Performance Loss | CV SD |
|---|---:|---:|---:|---:|
| **F₂ radial** | 0.3330 | 0.2813 | **0.0517** | 0.0194 |
| α₂ axial | 0.3330 | 0.3157 | 0.0174 | 0.0194 |
| relational | 0.3330 | 0.3174 | 0.0157 | 0.0117 |
| learned circular | 0.3330 | 0.3213 | 0.0117 | 0.0086 |
| observed circular | 0.3330 | 0.3235 | 0.0096 | 0.0082 |

### Largest Ablation Loss

```text
Largest ablation loss : F₂ radial
Performance loss      : 0.051739
```

---

# PAPER-READY PRIMARY SUMMARY

| Quantity | Value |
|---|---:|
| Population | 2300 |
| Number of categories | 23 |
| F₂ radial baseline BA | 0.253913 |
| ALL representation BA | 0.333043 |
| Observed ΔBA | **+0.079130** |
| Permutation null mean ΔBA | +0.000008 |
| Permutation null SD | 0.005845 |
| Permutation null 95% lower | -0.011407 |
| Permutation null 95% upper | +0.011239 |
| Permutation p | **0.000999** |
| Number of permutations | 1000 |
| Categories improved in F1 | **22/23** |
| Categories declined in F1 | 1/23 |
| Mean category ΔF1 | +0.089610 |
| Median category ΔF1 | +0.067019 |
| Largest family ablation loss — F₂ radial | **0.051739** |

---

# SCIENTIFIC CLAIM BOUNDARY

## Supported by the Current Evidence

The current experiments support the following claims:

1. The evaluated radial-angular geometric representation contains **category-discriminative information**.

2. The complete representation improves balanced accuracy over the F₂ radial baseline.

3. The observed improvement is substantially larger than the shuffled-label permutation null.

4. The improvement is broadly distributed, with:

   ```text
   22 / 23 categories
   showing positive F1 change relative to F₂.
   ```

5. Different geometric feature families contribute incremental information to the complete representation.

6. F₂ radial geometry produces the largest leave-one-family-out performance loss.

---

## Not Established

The current experiments do **not** establish:

- semantic understanding
- garment-part recognition
- causal garment structure
- human-like interpretation
- that a statistical angular mode corresponds to a physical garment component

---

# IMPORTANT DISTINCTION

Category discrimination demonstrates:

```text
statistical information about category identity
```

It does **not** by itself demonstrate:

```text
semantic meaning of individual features
```

---

# 135-D MORPHOLOGY RESULT

The earlier 135-D morphology analysis remains an independent morphology-level result.

It is **not numerically merged** into the present radial-angular classification experiment.

The two analyses should instead be connected later as complementary representations:

```text
135-D morphology
        ↕
interpretable radial-angular geometry
```

This preserves the independence of the original morphology discovery while allowing a later cross-representation comparison.

---

# NO CATEGORY-BASED FEATURE SELECTION

The canonical representation was frozen before category labels entered the analysis.

Therefore Cells 24–27B evaluate a predefined representation rather than selecting features according to category performance.

---

# FINAL CONSISTENCY CHECKS

```text
🟢 Cell 24 F₂ reproduced
🟢 Cell 24 ALL reproduced
🟢 Cell 24 ΔBA = Cell 25 ΔBA
🟢 Cell 24 ALL = Cell 27B ALL
🟢 Observed gain > null 97.5%
🟢 Permutation p < 0.05
🟢 All canonical features finite
🟢 22+ categories improved
```

---

# 🟢 CELL 28 — FINAL STATISTICAL / SCIENTIFIC SYNTHESIS

## Central Result

The complete radial-angular geometric representation achieves:

\[
\boxed{BA = 0.3330}
\]

compared with:

\[
BA_{F_2}=0.2539
\]

giving:

\[
\boxed{\Delta BA = +0.0791}
\]

---

## Permutation Robustness

The observed gain was:

\[
+0.0791
\]

while the shuffled-label null had:

\[
\text{mean }\Delta BA = 0.000008
\]

\[
SD = 0.005845
\]

with a 95% permutation interval:

\[
[-0.011407,\,+0.011239]
\]

Permutation test:

\[
\boxed{p=0.000999}
\]

The observed gain therefore lies outside the central 95% permutation-null interval.

---

## Category-Wise Behavior

```text
22 / 23 categories
improved in F1 relative to F₂.
```

Mean category ΔF1:

\[
+0.0896
\]

Median category ΔF1:

\[
+0.0670
\]

Thus the improvement is not confined to a single category.

---

## Family Ablation

The largest leave-one-family-out loss was produced by removing:

```text
F₂ radial
```

with:

\[
\boxed{\text{loss}=0.0517}
\]

This indicates that F₂ radial geometry provides the largest incremental contribution within the complete representation under the evaluated classifier.

This is an **incremental contribution measure**, not causal feature importance.

---

# FINAL SCIENTIFIC INTERPRETATION

The evidence supports the narrower claim that:

```text
radial magnitude geometry,
axial orientation geometry,
circular angular organization,
and radial-angular relational structure
```

contain category-discriminative information in the evaluated CLO-SKET dataset.

The evidence does **not** establish that these features constitute semantic garment-part representations.

---

# EXPERIMENTAL STATUS

```text
Cell 22A       ✓
Cell 22B       ✓
Cell 23B       ✓
Cell 23C       ✓
Cell 24        ✓
Cell 25        ✓
Cell 26        ✓
Cell 27B       ✓
Cell 28        ✓
```

---

# RESULT STATUS

The current radial-angular classification analysis has passed its internal consistency checks.

```text
No additional category-driven feature selection
was performed.

No hyperparameter search was introduced.

The 135-D morphology analysis remains an
independent earlier result and has not been
conflated with the present experiment.
```

---

# NEXT — CELL 29

## FINAL REPRODUCIBILITY / RESULT LOCK

Cell 29 should perform only:

- final bookkeeping
- provenance checks
- reproducibility checks
- result locking

It should **not** introduce:

- another classifier
- feature-selection procedure
- new scientific hypothesis

---

# 🟢 CELL 28 — FINAL SYNTHESIS COMPLETE

# 🧪 CLO-SKET — CELL 29
# FINAL REPRODUCIBILITY / RESULT LOCK

---

## NOTE

The current notebook kernel does not contain the intermediate
objects from Cells 20–27B.

Therefore this cell does **not** attempt to reconstruct or invent
those arrays.

The numerical results below are locked from the completed
Cell 28 synthesis.

Raw/intermediate objects will be required again for Cell 30
sketch-level visualization.

---

# LOCKED EXPERIMENTAL CONFIGURATION

| Configuration | Value |
|---|---|
| Population | 2300 |
| Categories | 23 |
| Samples per category | 100 |
| Canonical descriptors | 28 |
| Classifier coordinates | 30 |
| CV folds | 5 |
| CV random state | 42 |
| Permutations | 1000 |
| Permutation seed | 20260817 |
| Classifier | StandardScaler + Multinomial Logistic Regression |
| Axial encoding | cos(2α), sin(2α) |
| Hyperparameter search | False |
| Category-based feature selection | False |
| Canonical feature selection after labels | False |
| Primary baseline | F₂ radial only |
| Primary representation | ALL canonical families |

---

# LOCKED PRIMARY RESULTS

| Result | Value |
|---|---:|
| F₂ baseline BA | **0.253913** |
| ALL BA | **0.330435** |
| Observed ΔBA | **+0.076522** |
| Permutation null mean | 0.000053 |
| Permutation null SD | 0.005875 |
| Permutation null 95% lower | -0.011314 |
| Permutation null 95% upper | +0.011757 |
| Permutation p | **0.000999** |
| Number of permutations | 1000 |
| Categories improved | **22** |
| Categories declined | 1 |
| Mean category ΔF1 | +0.088106 |
| Median category ΔF1 | +0.083777 |

---

# LOCKED FAMILY ABLATION

| Feature family removed | Performance loss |
|---|---:|
| **F₂ radial** | **0.0487** |
| α₂ axial | 0.0165 |
| learned circular | 0.0091 |
| relational | 0.0087 |
| observed circular | 0.0017 |

### Largest contribution

```text
F₂ radial
loss = 0.0487
```

---

# CANONICAL FEATURE ORDER

```text
00  F2_integral
01  F2_radial_centroid
02  F2_radial_spread
03  F2_radial_concentration
04  F2_onset_radius
05  F2_termination_radius
06  F2_radial_extent
07  F2_peak_radius
08  F2_peak_magnitude
09  alpha2_peak_deg
10  alpha2_weighted_mean_deg
11  alpha2_axial_coherence
12  alpha2_persistence_15deg
13  alpha2_persistence_30deg
14  alpha2_persistence_45deg
15  alpha2_orientation_drift_deg
16  obs_R2_mean
17  obs_R2_sd
18  obs_R2_peak
19  hat_R2_mean
20  hat_R2_sd
21  hat_R2_peak
22  hat_R2_F2_weighted
23  F2_weighted_R2
24  R2_at_F2_peak
25  F2_concentration_x_R2
26  peak_vs_weighted_R2_difference
27  F2_R2_spearman
```

---

# CORE MATHEMATICAL CONSISTENCY

The locked balanced-accuracy difference is:

\[
\Delta BA
=
BA_{\mathrm{ALL}}
-
BA_{F_2}
\]

Therefore:

\[
0.330435 - 0.253913
=
0.076522
\]

```text
ALL BA − F₂ BA : +0.076522
Locked ΔBA     : +0.076522

🟢 ΔBA consistency
```

---

# PERMUTATION CONSISTENCY

```text
Observed ΔBA : +0.076522
Null 97.5%   : +0.011757

🟢 Observed gain exceeds null 97.5% bound
```

The observed gain is therefore separated from the
upper 97.5th percentile of the shuffled-label null
distribution.

---

# SCIENTIFIC CLAIM STATUS

```text
🟢 category_discriminative_information       : True
🟢 permutation_robust                        : True
🟢 broad_category_improvement                : True
🟢 F2_largest_ablation_contribution         : True

⚪ semantic_garment_part_recognition         : False
⚪ causal_garment_structure                  : False
⚪ physical_part_interpretation_of_angular_modes : False
```

---

# 🔒 CELL 29 — RADIAL-ANGULAR RESULTS LOCKED

## Locked Primary Result

```text
F₂ baseline BA      = 0.2539

ALL representation  = 0.3304

ΔBA                 = +0.0765

permutation p       = 0.000999
```

---

## Category Result

```text
improved            = 22 / 23

mean ΔF1            = +0.0881

median ΔF1          = +0.0838
```

---

## Ablation

```text
largest contribution = F₂ radial

loss                  = 0.0487
```

---

# REPRODUCIBILITY HASH

```text
a25667e65ea028bfb2ff225059b5de2dd89acb230900a8431ff37ac17aa92255
```

---

# IMPORTANT

Cell 29 introduced **NO new scientific result**.

The numerical results are locked from the completed
Cell 28 synthesis.

Intermediate arrays are **NOT** assumed to exist in the
current kernel.

---

# NEXT

## CELL 30 — SKETCH-LEVEL GEOMETRY VISUALIZATION

Cell 30 will require recovery of the original sketch
and geometry arrays before visualization.

---

# 🟢 CELL 29 — RADIAL-ANGULAR RESULTS LOCKED

# 🧪 CLO-SKET — CELL 30 REVIEW / FINAL VISUALIZATION LOCK

## Overall Status

**🟢 Cell 30C is the final scientifically defensible visualization.**

Cell 30C corrects the radial-domain mismatch present in the initial Cell 30B visualization.

The established circular-analysis domain is:

\[
r \in [3.5,\;27.5]
\]

Therefore, sketch-level angular quantities must be evaluated at radial locations within this established domain.

---

## 1. Cell 30B → Cell 30C Correction

### Cell 30B

The initial visualization used the **global F₂ peak radius**.

Examples:

| Sketch | Global F₂ peak radius |
|---|---:|
| 383 | 29.50 |
| 1129 | 37.50 |
| 1397 | 33.50 |
| 491 | 23.50 |
| 2210 | 34.50 |

Several global F₂ peaks lie outside the established circular-analysis domain:

\[
3.5 \leq r \leq 27.5
\]

Therefore, the global F₂ peak cannot always be directly paired with the circular descriptors established within that domain.

### Cell 30C

Cell 30C instead determines the **domain-restricted F₂ peak**:

\[
r_{\mathrm{peak}}^{\mathrm{domain}}
=
\arg\max_{r\in[3.5,27.5]} |F_2(r)|
\]

The corresponding circular radial shell is then selected.

This ensures that the radial and angular quantities being visualized correspond to a common, domain-valid radial location.

---

## 2. Terminology Correction

The restricted peak should **not** simply be called:

> F₂ peak radius

because the global F₂ peak may occur outside the circular-analysis domain.

Use:

> **Domain-restricted F₂ peak radius**

Recommended reporting:

| Quantity | Definition |
|---|---|
| Global F₂ peak radius | Maximum of \(|F_2(r)|\) over the full radial domain |
| Domain-restricted F₂ peak radius | Maximum of \(|F_2(r)|\) within \(3.5 \leq r \leq 27.5\) |
| Matched circular radius | Circular shell corresponding to the domain-restricted F₂ peak |

For example:

```text
Global F₂ peak radius           : 29.50
Domain-restricted F₂ peak radius: 15.50
Matched circular radius         : 15.50

# 🧪 CLO-SKET — CELL 30D
# Population-Level Radial–Angular Recovery

## 1. Purpose

Cell 30D evaluates whether the learned radial–angular representation
recovers the measured circular organization across the complete
population of 2300 sketches.

The analysis is performed within the established shared radial domain:

\[
r \in [3.5,\;27.5]
\]

The analysis separates two distinct aspects of recovery:

1. **circular concentration strength**
   \[
   R_2
   \]

2. **preferred axial orientation**
   \[
   \mu_2
   \]

These quantities are evaluated independently.

---

# 2. Input Verification

| Object | Shape | Status |
|---|---:|---|
| `image_paths` | (2300,) | 🟢 |
| `F2_mag` | (2300, 72) | 🟢 |
| `radial_centers` | (72,) | 🟢 |
| `R2_obs` | (2300, 25) | 🟢 |
| `mu2_obs_deg` | (2300, 25) | 🟢 |
| `R2_hat_field` | (2300, 25) | 🟢 |
| `mu2_hat_field_deg` | (2300, 25) | 🟢 |

Population:

\[
N=2300
\]

All required sketch-level arrays are finite and dimensionally
consistent.

---

# 3. Shared Radial Domain

The radial domain established by the circular analysis is:

\[
3.50 \leq r \leq 27.50
\]

There are:

- 72 radial bins in the original \(F_2\) representation
- 25 circular-analysis shells
- 25 \(F_2\) bins within the shared domain

The domain-restricted \(F_2\) peak is therefore defined as:

\[
r_{\mathrm{peak}}
=
\arg\max_{r\in[3.5,27.5]} |F_2(r)|
\]

All 2300 sketches have valid domain-restricted peaks.

Maximum mismatch between the selected \(F_2\) peak radius and the
corresponding circular shell:

\[
0.0000
\]

Thus the radial and angular quantities are evaluated at exactly
matched radial locations.

---

# 4. Population Summary

| Quantity | Median | IQR |
|---|---:|---:|
| Domain-restricted \(F_2\) peak radius | 21.500 | [17.500, 25.500] |
| Observed \(R_2\) | 0.4364 | [0.3000, 0.5697] |
| Learned \(R_2\) | 0.4032 | [0.2845, 0.4858] |
| \(\Delta R_2\) | -0.0688 | [-0.1872, +0.0590] |
| Axial angular error | 6.13° | [2.24°, 23.11°] |
| \(\cos(2\Delta\alpha)\) | 0.9772 | — |

where:

\[
\Delta R_2
=
R_{2,\mathrm{learned}}
-
R_{2,\mathrm{observed}}
\]

---

# 5. Circular-Strength Recovery

The learned circular concentration is generally weaker than the
observed concentration.

### Median values

\[
\mathrm{median}(R_{2,\mathrm{obs}})=0.4364
\]

\[
\mathrm{median}(R_{2,\mathrm{learned}})=0.4032
\]

Therefore:

\[
\mathrm{median}(\Delta R_2)=-0.0688
\]

The negative median indicates that the learned representation
typically underestimates the strength of the observed circular
organization.

This does **not** imply failure to recover the angular organization.
Concentration strength and preferred orientation are separate
properties.

---

# 6. Direction of \(R_2\) Difference

The population contains:

- Learned \(R_2 >\) observed \(R_2\): **814 / 2300 (35.39%)**
- Learned \(R_2 <\) observed \(R_2\): **1486 / 2300 (64.61%)**

Thus the learned representation produces weaker circular concentration
than the observed representation for the majority of sketches.

The distribution of:

\[
\Delta R_2
=
R_{2,\mathrm{learned}}
-
R_{2,\mathrm{observed}}
\]

is centered below zero, with median:

\[
-0.0688
\]

---

# 7. Observed vs Learned Circular Strength

The population-level relationship between observed and learned
circular concentration is:

### Pearson correlation

\[
r=0.3270
\]

\[
p=1.80843\times10^{-58}
\]

### Spearman correlation

\[
\rho=0.3640
\]

\[
p=5.16105\times10^{-73}
\]

The learned and observed \(R_2\) values therefore show a statistically
detectable positive association.

However, the magnitude of the correlation is moderate rather than
near-perfect.

Therefore the learned representation should be described as showing
**partial population-level recovery of circular concentration**, rather
than exact reconstruction of observed concentration.

---

# 8. Axial Orientation Recovery

Axial orientations satisfy:

\[
\alpha \equiv \alpha+180^\circ
\]

Therefore angular disagreement is evaluated using the axial circular
difference:

\[
\Delta\alpha =
\min
\left(
|\alpha_1-\alpha_2|\bmod180^\circ,\;
180^\circ-
\left(|\alpha_1-\alpha_2|\bmod180^\circ\right)
\right)
\]

The resulting error lies in:

\[
0^\circ\leq\Delta\alpha\leq90^\circ
\]

Population median:

\[
\mathrm{median}(\Delta\alpha)=6.13^\circ
\]

IQR:

\[
[2.24^\circ,\;23.11^\circ]
\]

The corresponding doubled-angle agreement is:

\[
\mathrm{median}\left[\cos(2\Delta\alpha)\right]
=
0.9772
\]

---

# 9. Axial Recovery Bands

| Axial error | Sketches | Percentage |
|---|---:|---:|
| \(\leq15^\circ\) | 1600 | 69.57% |
| \(15^\circ-45^\circ\) | 231 | 10.04% |
| \(>45^\circ\) | 469 | 20.39% |

Thus approximately **70% of sketches show low axial angular error
(≤15°)** under the defined recovery criterion.

Approximately **20% show high angular disagreement (>45°)**.

This demonstrates heterogeneous sketch-level recovery rather than
uniform recovery across the population.

---

# 10. Observed Circular Strength vs Angular Recovery Error

The relationship between observed circular strength and axial error is:

### Pearson

\[
r=-0.3686
\]

\[
p=5.95666\times10^{-75}
\]

### Spearman

\[
\rho=-0.4794
\]

\[
p=1.6234\times10^{-132}
\]

The negative association indicates that sketches with stronger observed
axial concentration tend to exhibit smaller observed–learned angular
disagreement.

This is an important result because it suggests that the reliability
of orientation recovery is related to the strength of the underlying
observed circular organization.

However, this association is empirical and does not establish a causal
mechanism.

---

# 11. Interpretation of the Population Plots

## A. Population \(F_2\) Peak Radius

The distribution of domain-restricted \(F_2\) peak radius spans the
established circular-analysis domain.

The median peak radius is:

\[
21.5
\]

The distribution is not uniform and contains substantial mass toward
the upper part of the permitted radial domain.

---

## B. Observed vs Learned \(R_2\)

The scatter plot shows a positive but imperfect relationship between
observed and learned circular strength.

The learned values are concentrated in a narrower band than the
observed values.

This is consistent with:

\[
\rho=0.3640
\]

and the negative median difference:

\[
\Delta R_2=-0.0688
\]

Therefore the learned representation captures some population-level
variation in circular organization but does not reproduce the full
observed range of concentration strengths.

---

## C. Learned − Observed \(R_2\)

The difference distribution is centered below zero.

\[
\mathrm{median}(\Delta R_2)=-0.0688
\]

Therefore systematic underestimation of circular concentration is
present at the population level.

---

## D. Observed \(R_2\) vs Axial Error

The scatter plot shows that large angular errors are more common when
observed circular concentration is weak.

The negative Spearman association:

\[
\rho=-0.4794
\]

supports this population-level relationship.

This provides an important qualification for sketch-level angular
recovery: orientation estimates are not equally informative when
circular concentration is weak.

---

# 12. What Cell 30D Demonstrates

Cell 30D provides evidence for three distinct observations:

### 1. Radial localization

The \(F_2\) representation provides a measurable radial organization
with a population distribution of domain-restricted peak locations.

### 2. Partial circular-strength recovery

Observed and learned \(R_2\) values are positively associated:

\[
\rho=0.3640
\]

but the learned representation generally has lower concentration:

\[
\mathrm{median}(\Delta R_2)=-0.0688
\]

### 3. Axial orientation recovery

The learned preferred axial orientation is close to the observed
orientation for a substantial fraction of sketches:

\[
69.57\%
\]

have axial error:

\[
\leq15^\circ
\]

---

# 13. Important Scientific Distinction

Circular strength and angular orientation should not be conflated.

A sketch may have:

- close observed–learned orientation but different \(R_2\), or
- similar \(R_2\) but substantial orientation disagreement.

Therefore recovery should be reported as a multidimensional property:

\[
\text{radial localization}
+
\text{circular concentration}
+
\text{axial orientation}
\]

rather than as a single scalar measure.

---

# 14. What This Does NOT Establish

Cell 30D does **not** establish:

- semantic garment-part recognition
- causal garment structure
- physical interpretation of angular modes
- human-like garment understanding
- direct correspondence between angular modes and garment components

The angular modes remain descriptive properties of the learned
geometric representation.

---

# 15. Relationship to Earlier Cells

```text
CELL 20
Canonical F₂ radial geometry
        ↓
CELL 21
α₂ axial geometry
        ↓
CELL 22A
Single vs two-component axial model audit
        ↓
CELL 22B
Learned single-axial conditional relationship
        ↓
CELL 23B
Feature-family redundancy audit
        ↓
CELL 23C
Canonical feature-set lock
        ↓
CELL 24
Controlled category discrimination
        ↓
CELL 25
Permutation robustness
        ↓
CELL 26
Category-wise diagnostics
        ↓
CELL 27
Feature-family ablation
        ↓
CELL 29
Final radial–angular result lock
        ↓
CELL 30A
Geometry recovery audit
        ↓
CELL 30B
Sketch-level visualization
        ↓
CELL 30C
Domain-consistent sketch visualization
        ↓
CELL 30D
Population-level radial–angular recovery

# 🧪 CLO-SKET — CELL 30E
# Stratified Angular Recovery by Observed \(R_2\)

## 1. Purpose

Cell 30E evaluates whether the reliability of angular recovery depends
on the strength of the observed circular organization.

The population is divided into four strata according to the observed
\(R_2\) distribution:

- Q1 — weakest observed \(R_2\)
- Q2
- Q3
- Q4 — strongest observed \(R_2\)

The strata are defined exclusively from the observed \(R_2\) values.

No category labels are used.

No classifier is retrained.

No feature selection is performed.

No representation is modified.

---

# 2. Input Verification

| Object | Shape | Status |
|---|---:|---|
| `F2_mag` | (2300, 72) | 🟢 |
| `radial_centers` | (72,) | 🟢 |
| `R2_obs` | (2300, 25) | 🟢 |
| `mu2_obs_deg` | (2300, 25) | 🟢 |
| `R2_hat_field` | (2300, 25) | 🟢 |
| `mu2_hat_field_deg` | (2300, 25) | 🟢 |

Population:

\[
N=2300
\]

All 2300 sketches contain finite values.

---

# 3. Shared Radial Domain

The analysis uses the established circular-analysis domain:

\[
3.50 \leq r \leq 27.50
\]

with 25 circular shells.

The domain-consistent \(F_2\) peak is restricted to this same
radial domain.

All 2300 sketches have valid domain-consistent \(F_2\) peaks.

---

# 4. Observed \(R_2\) Quartiles

The observed circular-strength distribution has:

\[
Q_{25}=0.3000
\]

\[
Q_{50}=0.4364
\]

\[
Q_{75}=0.5697
\]

The population is divided into four approximately equal strata:

\[
N_{\mathrm{Q1}}
=
N_{\mathrm{Q2}}
=
N_{\mathrm{Q3}}
=
N_{\mathrm{Q4}}
=
575
\]

---

# 5. Stratified Angular Recovery

| Stratum | \(N\) | Median observed \(R_2\) | Median learned \(R_2\) | Median \(\Delta R_2\) | Median angular error | Error \(\leq15^\circ\) | Error \(>45^\circ\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q1 — weakest \(R_2\) | 575 | 0.2010 | 0.3145 | +0.1217 | 23.58° | 39.30% | 37.74% |
| Q2 | 575 | 0.3672 | 0.3556 | -0.0108 | 8.57° | 63.13% | 27.65% |
| Q3 | 575 | 0.5019 | 0.4333 | -0.0774 | 4.53° | 82.61% | 11.30% |
| Q4 — strongest \(R_2\) | 575 | 0.6517 | 0.4729 | -0.2061 | 2.56° | 93.22% | 4.87% |

where:

\[
\Delta R_2
=
R_{2,\mathrm{learned}}
-
R_{2,\mathrm{observed}}
\]

---

# 6. Main Angular-Recovery Result

A strong monotonic pattern is visible across the four observed-\(R_2\)
strata.

Median axial error decreases from:

\[
23.58^\circ
\]

in Q1 to:

\[
2.56^\circ
\]

in Q4.

Therefore:

\[
23.58^\circ
\rightarrow
8.57^\circ
\rightarrow
4.53^\circ
\rightarrow
2.56^\circ
\]

as observed circular strength increases.

The fraction of sketches with low angular error also increases:

\[
39.30\%
\rightarrow
63.13\%
\rightarrow
82.61\%
\rightarrow
93.22\%
\]

for the criterion:

\[
\Delta\alpha\leq15^\circ
\]

At the same time, the proportion with high angular error decreases:

\[
37.74\%
\rightarrow
27.65\%
\rightarrow
11.30\%
\rightarrow
4.87\%
\]

for:

\[
\Delta\alpha>45^\circ
\]

---

# 7. Stratified \(R_2\) Recovery

The behavior of circular-strength recovery differs from angular
orientation recovery.

The median learned-minus-observed \(R_2\) difference is:

| Stratum | Median \(\Delta R_2\) |
|---|---:|
| Q1 | +0.1217 |
| Q2 | -0.0108 |
| Q3 | -0.0774 |
| Q4 | -0.2061 |

Thus the learned representation behaves differently across the
strength regime.

### Weak observed circular organization

In Q1:

\[
\Delta R_2=+0.1217
\]

The learned representation is, on average, more concentrated than the
observed representation.

### Strong observed circular organization

In Q4:

\[
\Delta R_2=-0.2061
\]

The learned representation substantially underestimates the observed
circular concentration.

This produces an important distinction:

> **Angular orientation becomes more accurately recovered as observed
> circular strength increases, while the magnitude of circular strength
> itself becomes increasingly attenuated relative to the observed
> representation.**

Therefore orientation recovery and concentration-strength recovery
should not be treated as the same phenomenon.

---

# 8. Within-Stratum Associations

Pearson correlation between observed \(R_2\) and axial error was also
calculated separately within each stratum.

| Stratum | Pearson \(r\) |
|---|---:|
| Q1 | -0.0081 |
| Q2 | -0.0253 |
| Q3 | -0.1164 |
| Q4 | -0.0677 |

These within-stratum correlations are weak.

This is expected to differ from the strong population-level trend because
the stratification itself removes much of the between-stratum variation
in observed \(R_2\).

Therefore the primary evidence for the relationship comes from the
**systematic change in angular-error distributions across the four
strata**, rather than from the within-stratum Pearson correlations.

---

# 9. Stratum-Level Trend

The correlation between the four stratum median observed \(R_2\) values
and the corresponding median angular errors is:

\[
r=-0.9232
\]

This indicates a strong monotonic stratum-level trend:

\[
R_2\uparrow
\quad\Rightarrow\quad
\text{angular error}\downarrow
\]

However, this correlation is based on only four stratum-level points.

It should therefore be treated as a **descriptive summary of the
stratified trend**, not as an independent inferential test.

The stronger evidence is the large and consistent shift in the complete
error distributions shown by the boxplots.

---

# 10. Interpretation of the Boxplot

The boxplot shows a pronounced change in angular-error distribution
across observed-\(R_2\) strata.

### Q1 — weakest \(R_2\)

The error distribution is broad:

- median = 23.58°
- upper quartile approaches very high angular error
- 37.74% exceed 45°

Angular orientation is therefore poorly constrained for a substantial
fraction of weakly organized sketches.

### Q2

Angular recovery improves substantially:

\[
\mathrm{median\ error}=8.57^\circ
\]

### Q3

Recovery becomes substantially tighter:

\[
\mathrm{median\ error}=4.53^\circ
\]

### Q4 — strongest \(R_2\)

The error distribution is concentrated near zero:

\[
\mathrm{median\ error}=2.56^\circ
\]

and:

\[
93.22\%
\]

of sketches have error:

\[
\leq15^\circ
\]

Only:

\[
4.87\%
\]

have error:

\[
>45^\circ
\]

---

# 11. Scientific Interpretation

The results support an empirical relationship between the strength of
observed circular organization and the reliability of axial orientation
recovery.

Specifically:

\[
R_{2,\mathrm{obs}}\uparrow
\quad\Longrightarrow\quad
\Delta\alpha\downarrow
\]

at the population-stratum level.

The interpretation is that stronger observed circular organization
provides a more stable measurable preferred axial orientation, whereas
weak circular organization is associated with substantially greater
orientation disagreement.

This is consistent with the population-level result from Cell 30D:

\[
\rho(R_{2,\mathrm{obs}},\Delta\alpha)
=
-0.4794
\]

Cell 30E strengthens this observation by showing that the relationship
persists as a clear distributional shift across independently defined
observed-\(R_2\) strata.

---

# 12. Important Distinction: Orientation vs Strength

Cell 30E provides an important qualification to the interpretation of
Cell 30D.

Two different recovery properties behave differently:

### Axial orientation

Recovery improves strongly with observed \(R_2\):

\[
23.58^\circ
\rightarrow
2.56^\circ
\]

from Q1 to Q4.

### Circular concentration strength

The learned representation increasingly underestimates observed
concentration at high \(R_2\):

\[
+0.1217
\rightarrow
-0.2061
\]

from Q1 to Q4.

Therefore the learned representation does not simply reproduce the
observed circular field by uniformly scaling it.

Instead, the results indicate:

\[
\boxed{
\text{orientation recovery}
\neq
\text{concentration-strength recovery}
}
\]

---

# 13. What Cell 30E Supports

Cell 30E supports the following empirical observations:

1. **Angular recovery is strongly stratified by observed circular
   strength.**

2. **Stronger observed \(R_2\) is associated with lower angular
   recovery error.**

3. **Low-error recovery becomes increasingly common as observed
   \(R_2\) increases.**

4. **High-error recovery becomes uncommon in the strongest observed
   \(R_2\) stratum.**

5. **Learned circular concentration does not reproduce observed
   concentration uniformly across the \(R_2\) range.**

6. **Weak circular organization is associated with substantially
   greater uncertainty/disagreement in recovered orientation.**

---

# 14. What Cell 30E Does NOT Establish

This analysis does **not** establish:

- causality between \(R_2\) strength and angular recovery
- semantic garment-part recognition
- physical meaning of the angular modes
- human-like interpretation of the sketch
- causal garment structure
- that strong \(R_2\) is itself the mechanism producing better recovery

The results describe an empirical association within the evaluated
representation.

---

# 15. Relationship to Cell 30D

Cell 30D established:

\[
\rho(R_{2,\mathrm{obs}},\Delta\alpha)
=
-0.4794
\]

across the full population.

Cell 30E now shows how this relationship manifests across the
distribution.

The population can be summarized as:

```text
Weak observed circular organization
        ↓
Broad angular-error distribution
        ↓
Greater orientation disagreement

Moderate observed circular organization
        ↓
Improved angular recovery

Strong observed circular organization
        ↓
Tight angular-error distribution
        ↓
Highly reliable axial orientation recovery

# 🧪 CLO-SKET — CELL 30E
# Observed vs Learned Circular Strength Across \(R_2\) Strata

## Figure Interpretation

The grouped bar plot compares the median observed and learned circular
strength:

\[
R_2
\]

across the four strata defined from the observed \(R_2\) distribution.

The strata progress from:

- Q1 — weakest observed circular organization
- Q2
- Q3
- Q4 — strongest observed circular organization

---

## Median Circular Strength by Stratum

| Stratum | Median observed \(R_2\) | Median learned \(R_2\) | Learned − observed |
|---|---:|---:|---:|
| Q1 | 0.2010 | 0.3145 | +0.1217 |
| Q2 | 0.3672 | 0.3556 | -0.0108 |
| Q3 | 0.5019 | 0.4333 | -0.0774 |
| Q4 | 0.6517 | 0.4729 | -0.2061 |

where:

\[
\Delta R_2
=
R_{2,\mathrm{learned}}
-
R_{2,\mathrm{observed}}
\]

---

# 1. Observed Circular Strength Increases Across Strata

Because the strata are defined using the observed \(R_2\) distribution,
the median observed strength increases systematically:

\[
0.2010
\rightarrow
0.3672
\rightarrow
0.5019
\rightarrow
0.6517
\]

from Q1 to Q4.

This progression represents increasingly strong measured axial
organization.

---

# 2. Learned Circular Strength Has a Compressed Dynamic Range

The learned representation also increases across strata:

\[
0.3145
\rightarrow
0.3556
\rightarrow
0.4333
\rightarrow
0.4729
\]

but the increase is substantially smaller than that of the observed
representation.

Thus the learned \(R_2\) values occupy a narrower effective range.

The learned representation therefore captures the broad ordering of
circular-strength regimes but compresses the magnitude of the observed
variation.

---

# 3. Regime-Dependent Bias

The direction of the learned–observed difference changes across the
observed-strength distribution.

### Q1 — weakest observed organization

\[
\Delta R_2 = +0.1217
\]

The learned representation **overestimates** circular strength.

### Q2

\[
\Delta R_2 = -0.0108
\]

Observed and learned medians are approximately aligned.

### Q3

\[
\Delta R_2 = -0.0774
\]

The learned representation begins to **underestimate** observed
circular strength.

### Q4 — strongest observed organization

\[
\Delta R_2 = -0.2061
\]

The underestimation is strongest in the most highly organized stratum.

---

# 4. Scientific Pattern

The figure therefore suggests a form of strength compression:

\[
\text{weak observed } R_2
\quad\rightarrow\quad
\text{learned } R_2 \text{ biased upward}
\]

while:

\[
\text{strong observed } R_2
\quad\rightarrow\quad
\text{learned } R_2 \text{ biased downward}
\]

Equivalently, the learned representation tends to pull extreme
observed circular-strength values toward an intermediate range.

This behavior is consistent with the population-level result from
Cell 30D, where:

\[
\mathrm{median}(\Delta R_2)=-0.0688
\]

and the learned \(R_2\) distribution showed a visibly narrower range
than the observed distribution.

---

# 5. Relation to Angular Recovery

Importantly, this strength-compression pattern occurs simultaneously
with improving axial orientation recovery.

Across the same strata:

\[
\mathrm{median\ axial\ error}
=
23.58^\circ
\rightarrow
8.57^\circ
\rightarrow
4.53^\circ
\rightarrow
2.56^\circ
\]

Thus two different properties behave differently:

### Orientation

\[
R_{2,\mathrm{obs}}\uparrow
\quad\Rightarrow\quad
\text{angular error}\downarrow
\]

### Circular-strength magnitude

\[
R_{2,\mathrm{obs}}\uparrow
\quad\Rightarrow\quad
\text{increasing learned underestimation}
\]

Therefore:

\[
\boxed{
\text{orientation recovery}
\neq
\text{strength recovery}
}
\]

The learned representation can recover the preferred axis accurately
while still underestimating the strength of the observed circular
organization.

---

# 6. Interpretation Boundary

This figure supports the statement that the learned circular-strength
representation exhibits **regime-dependent calibration error**.

It does **not** establish why that compression occurs.

Possible mechanisms should not be asserted without an additional
experiment.

In particular, the figure does not establish:

- causal shrinkage
- model regularization as the mechanism
- noise suppression as the mechanism
- semantic abstraction
- garment-part interpretation

The appropriate interpretation remains descriptive.

---

# 7. Recommended Manuscript Language

> **Observed and learned circular concentration increased across progressively stronger observed-\(R_2\) strata, but the learned representation occupied a narrower dynamic range. It overestimated circular concentration in the weakest stratum and increasingly underestimated it in the stronger strata, indicating regime-dependent attenuation of circular-strength magnitude. This contrasted with axial orientation recovery, which improved substantially as observed circular strength increased.**

---

# 8. Figure-Level Scientific Conclusion

The plot provides direct visual evidence that:

1. learned \(R_2\) preserves the broad ordering of observed-strength strata;
2. learned \(R_2\) does not reproduce the full observed dynamic range;
3. weak observed circular organization is overestimated;
4. strong observed circular organization is underestimated;
5. orientation recovery and concentration-strength recovery behave differently.

---

## 🔒 CELL 30E — STRENGTH-RECOVERY INTERPRETATION

\[
\boxed{
R_{2,\mathrm{learned}}
\text{ shows compressed recovery across the observed }R_2\text{ range}
}
\]

while:

\[
\boxed{
\text{axial orientation recovery improves strongly as observed }R_2\text{ increases}
}
\]

This distinction should be preserved explicitly in the final manuscript.

# 🧪 CLO-SKET — CELLS 30F–30H
# Recovery Reliability, Failure Regimes, and Final Radial–Angular Synthesis

## Objective

Cells 30F–30H examine the reliability of the learned radial–angular representation after the population-level recovery analysis.

The analysis asks three related questions:

1. **When is the learned axial orientation reliable?**
2. **What distinguishes successful recovery from failure?**
3. **Are circular-strength recovery and angular-orientation recovery the same phenomenon?**

The analysis remains entirely diagnostic.

No classifier is retrained, no category labels are used, and no representation is altered.

---

# Cell 30F — Recovery Reliability / Failure-Regime Analysis

## Recovery-Regime Definition

Each sketch is assigned to a recovery regime using only the axial angular error:

\[
\Delta \alpha
=
\min
\left(
|\alpha_{\mathrm{obs}}-\alpha_{\mathrm{learned}}|\bmod 180^\circ,
180^\circ-
|\alpha_{\mathrm{obs}}-\alpha_{\mathrm{learned}}|\bmod 180^\circ
\right)
\]

with:

- **Reliable recovery:** \(\Delta\alpha \leq 15^\circ\)
- **Moderate recovery:** \(15^\circ < \Delta\alpha \leq 45^\circ\)
- **Failure:** \(\Delta\alpha > 45^\circ\)

Because the orientation is axial,

\[
\alpha \equiv \alpha + 180^\circ
\]

and the maximum possible axial disagreement is therefore \(90^\circ\).

---

## Population Recovery Regimes

| Recovery regime | N | Population fraction | Median observed \(R_2\) | Median learned \(R_2\) | Median \(\Delta R_2\) | Median peak \(|F_2|\) | Median angular error |
|---|---:|---:|---:|---:|---:|---:|---:|
| Reliable \(\leq15^\circ\) | 1600 | 69.57% | 0.4973 | 0.4446 | -0.0830 | 0.04147 | 3.37° |
| Moderate 15–45° | 231 | 10.04% | 0.2598 | 0.3365 | +0.0582 | 0.04153 | 22.46° |
| Failure \(>45^\circ\) | 469 | 20.39% | 0.3172 | 0.2579 | -0.0656 | 0.02521 | 80.56° |

where:

\[
\Delta R_2
=
R_{2,\mathrm{learned}}
-
R_{2,\mathrm{observed}}
\]

---

# 1. Most Sketches Show Reliable Axial Recovery

The largest population group is the reliable regime:

\[
\frac{1600}{2300}
=
69.57\%
\]

Thus approximately seven out of ten sketches have an observed-versus-learned axial disagreement of no more than \(15^\circ\).

A further:

\[
10.04\%
\]

fall within the moderate-error regime.

The high-error failure regime contains:

\[
20.39\%
\]

of the population.

Therefore the learned representation does not recover orientation uniformly, but successful low-error recovery is the dominant population regime.

---

# 2. Observed Circular Strength Is Associated with Recovery Reliability

Reliable sketches exhibit substantially stronger observed circular organization:

\[
\mathrm{median}\ R_{2,\mathrm{obs}}
=
0.4973
\]

compared with:

\[
0.3172
\]

for the failure group.

Earlier population analysis also showed:

\[
\rho_{\mathrm{Spearman}}
\left(
R_{2,\mathrm{obs}},
\Delta\alpha
\right)
=
-0.4794
\]

indicating that stronger observed circular organization is associated with smaller axial error.

The stratified analysis in Cell 30E further showed a strong monotonic population trend:

\[
23.58^\circ
\rightarrow
8.57^\circ
\rightarrow
4.53^\circ
\rightarrow
2.56^\circ
\]

in median error from the weakest to the strongest observed-\(R_2\) quartile.

---

# 3. Failure Is Enriched in the Weak-\(R_2\) Regime

The lower quartile of observed circular strength is defined by:

\[
R_{2,\mathrm{obs}}
\leq
0.3000
\]

Among the 469 high-error failures:

\[
217
\]

occur in this lowest-\(R_2\) quartile.

Therefore:

\[
\frac{217}{469}
=
46.27\%
\]

of all high-error failures are concentrated in the weakest quarter of the observed circular-strength distribution.

This is considerably greater than the 25% expected from an evenly distributed failure pattern.

The result supports the interpretation that weak circular organization is associated with reduced angular recoverability.

However, it does **not** imply that weak \(R_2\) is sufficient to explain all failures.

---

# 4. \(F_2\) Magnitude Is Also Lower in the Failure Regime

Median peak \(F_2\) magnitude is:

\[
0.04147
\]

for reliably recovered sketches but only:

\[
0.02521
\]

for failures.

Thus failure sketches tend to exhibit weaker second-harmonic structure.

This is consistent with the interpretation that the learned axial direction becomes less recoverable when the underlying two-fold signal itself is weak.

However, this association is not deterministic.

Strong-\(F_2\) failures are also observed.

---

# 5. Strength Recovery and Orientation Recovery Are Distinct

The sign of:

\[
\Delta R_2
=
R_{2,\mathrm{learned}}
-
R_{2,\mathrm{observed}}
\]

varies across recovery regimes.

### Reliable regime

\[
\mathrm{median}\ \Delta R_2
=
-0.0830
\]

Despite excellent angular recovery, the learned circular strength is usually lower than observed.

### Moderate regime

\[
\mathrm{median}\ \Delta R_2
=
+0.0582
\]

Here learned circular strength tends to exceed observed strength.

### Failure regime

\[
\mathrm{median}\ \Delta R_2
=
-0.0656
\]

High angular error can coexist with underestimation of circular strength.

Therefore angular error and circular-strength error do not describe the same property.

\[
\boxed{
\text{orientation recovery}
\neq
\text{circular-strength recovery}
}
\]

---

# Cell 30G — Representative Success and Failure Cases

Four representative sketches were selected directly from the empirical recovery regimes.

No garment category was used in their selection.

---

## Case 1 — Strong Successful Recovery

**Sketch 1652**

- Peak radius: \(r=23.50\)
- Peak \(|F_2|=0.07669\)
- Observed \(R_2=0.844\)
- Learned \(R_2=0.503\)
- \(\Delta R_2=-0.340\)
- Axial error: \(0.26^\circ\)

This sketch provides a particularly clear example of the distinction between angular and strength recovery.

The preferred axial orientation is recovered almost perfectly:

\[
\Delta\alpha
=
0.26^\circ
\]

yet the learned circular concentration is substantially attenuated:

\[
0.503
<
0.844
\]

Thus excellent orientation recovery does not require accurate recovery of concentration magnitude.

---

## Case 2 — Weak-Signal Failure

**Sketch 1978**

- Peak radius: \(r=5.50\)
- Peak \(|F_2|=0.03951\)
- Observed \(R_2=0.001\)
- Learned \(R_2=0.244\)
- \(\Delta R_2=+0.242\)
- Axial error: \(83.99^\circ\)

The observed circular organization is essentially absent:

\[
R_{2,\mathrm{obs}}
\approx 0
\]

In such a regime, the observed preferred axis is intrinsically weakly defined.

The learned model nevertheless produces a nonzero concentration and an orientation far from the measured one.

This case illustrates a plausible **weak-signal failure regime**.

The appropriate interpretation is not that the model chose a physically incorrect garment axis, but that axial recovery becomes unreliable when the measured circular signal provides very little directional support.

---

## Case 3 — Strong-Signal Failure

**Sketch 1994**

- Peak radius: \(r=8.50\)
- Peak \(|F_2|=0.03405\)
- Observed \(R_2=0.811\)
- Learned \(R_2=0.124\)
- \(\Delta R_2=-0.687\)
- Axial error: \(88.23^\circ\)

This is diagnostically important.

The sketch has strong observed circular organization:

\[
R_{2,\mathrm{obs}}
=
0.811
\]

yet the learned orientation is almost maximally misaligned:

\[
\Delta\alpha
=
88.23^\circ
\]

Therefore weak observed \(R_2\) cannot explain every failure.

This prevents an overly simple interpretation such as:

> low circular strength causes all angular failures.

The population trend is real, but exceptions remain substantial and scientifically important.

---

## Case 4 — Moderate Recovery

**Sketch 1242**

- Peak radius: \(r=9.50\)
- Peak \(|F_2|=0.04831\)
- Observed \(R_2=0.123\)
- Learned \(R_2=0.084\)
- \(\Delta R_2=-0.039\)
- Axial error: \(29.90^\circ\)

This case represents the intermediate recovery regime.

Neither orientation agreement nor circular-strength disagreement is extreme.

It demonstrates that recovery behavior is continuous rather than cleanly divided into only success and failure.

---

# Representative-Case Interpretation

Together, these cases establish that at least three different recovery behaviors occur:

\[
\text{strong signal + good orientation recovery}
\]

\[
\text{weak signal + poor orientation recovery}
\]

and:

\[
\text{strong signal + poor orientation recovery}
\]

The third case is particularly important because it demonstrates that recovery failure is not reducible to signal weakness alone.

---

# Cell 30H — Final Population Synthesis

## Population Summary

| Quantity | Result |
|---|---:|
| Population | 2300 |
| Shared radial domain | 3.50–27.50 |
| Reliable \(\leq15^\circ\) | 1600 (69.57%) |
| Moderate 15–45° | 231 (10.04%) |
| Failure \(>45^\circ\) | 469 (20.39%) |
| Median observed \(R_2\) | 0.4364 |
| Median learned \(R_2\) | 0.4032 |
| Median \(\Delta R_2\) | -0.0688 |
| Median axial error | 6.13° |
| Median axial agreement \(\cos(2\Delta\alpha)\) | 0.9772 |
| Median \(F_2\) peak radius | 21.50 |
| Median \(F_2\) peak magnitude | 0.03914 |

---

# 6. The Population Shows Strong but Incomplete Orientation Recovery

The median axial error is:

\[
6.13^\circ
\]

and:

\[
69.57\%
\]

of sketches fall within \(15^\circ\).

The corresponding median doubled-angle axial agreement is:

\[
\cos(2\Delta\alpha)
=
0.9772
\]

indicating strong population-level angular agreement.

The representation therefore learns a substantial component of the measured axial organization.

However:

\[
20.39\%
\]

of the population remains in the high-error regime.

Thus the learned relationship is systematic but not universally accurate.

---

# 7. Learned Circular Strength Is Systematically Compressed

Across the full population:

\[
\mathrm{median}\ R_{2,\mathrm{obs}}
=
0.4364
\]

while:

\[
\mathrm{median}\ R_{2,\mathrm{learned}}
=
0.4032
\]

and:

\[
\mathrm{median}\ \Delta R_2
=
-0.0688
\]

The learned representation therefore tends, on average, to underestimate observed circular strength.

The stratified analysis shows that this bias is not constant.

At weak observed \(R_2\), the model tends to overestimate concentration.

At strong observed \(R_2\), it increasingly underestimates concentration.

This produces a compressed learned dynamic range.

---

# 8. Circular Strength Predicts Reliability Better Than It Determines It

Population-level association:

\[
\rho
\left(
R_{2,\mathrm{obs}},
\Delta\alpha
\right)
=
-0.4794
\]

shows a substantial relationship between signal strength and angular recovery.

But the strong-signal failure case demonstrates that:

\[
R_{2,\mathrm{obs}}\text{ high}
\not\Rightarrow
\Delta\alpha\text{ small}
\]

for every sketch.

Thus observed circular strength is a **reliability-associated variable**, not a deterministic guarantee of recovery.

---

# 9. \(F_2\) Strength Also Relates to Recovery Regime

Reliable sketches exhibit stronger median peak second-harmonic magnitude than failure sketches:

\[
0.04147
\quad\text{vs}\quad
0.02521
\]

respectively.

This supports a second empirical relationship:

\[
|F_2|
\uparrow
\quad\Longrightarrow\quad
\text{greater probability of reliable orientation recovery}
\]

at the population level.

Again, the presence of strong-signal failures prevents a deterministic interpretation.

---

# 10. Radial Location Also Differs Across Recovery Regimes

Median \(F_2\) peak radii are:

\[
22.50
\]

for the reliable regime,

\[
18.50
\]

for moderate recovery, and:

\[
17.50
\]

for the failure regime.

Therefore high-quality angular recovery is associated not only with stronger circular organization but also with a tendency for the dominant \(F_2\) structure to occur farther from the centroid.

This radial association is descriptive and should not yet be assigned garment-part meaning.

---

# 11. Main Scientific Result of Cells 30D–30H

The learned model captures a reproducible radial–angular population relationship, but its recovery behavior is multidimensional.

Two distinct quantities must be separated:

## Axial orientation

\[
\alpha_2
\]

describes **where** the two-fold organization is directed.

## Circular concentration

\[
R_2
\]

describes **how strongly** angular mass is organized around that axis.

The results show that these quantities can behave independently.

For example:

\[
\Delta\alpha \approx 0^\circ
\]

can coexist with substantial:

\[
\Delta R_2 < 0
\]

and conversely strong observed \(R_2\) can coexist with large angular disagreement.

Therefore:

\[
\boxed{
\text{directional recovery and concentration recovery are empirically separable}
}
\]

---

# 12. What Has Been Established

The raw-image analysis now supports the following evidence chain:

\[
\text{raw grayscale sketch}
\]

\[
\downarrow
\]

\[
\text{intensity-weighted centroid}
\]

\[
\downarrow
\]

\[
p(\theta\mid r)
\]

\[
\downarrow
\]

\[
F_2(r),\;\alpha_2(r)
\]

\[
\downarrow
\]

\[
R_2(r)
\]

\[
\downarrow
\]

\[
(r,|F_2|)
\rightarrow
(\hat C_2,\hat S_2)
\]

\[
\downarrow
\]

\[
(\hat R_2,\hat\alpha_2)
\]

\[
\downarrow
\]

\[
\text{population-level radial–angular recovery}
\]

The learned model shows meaningful recovery of the observed axial organization across the population.

Recovery reliability is strongly associated with the strength of measured angular organization but is not determined by signal strength alone.

---

# 13. Important Negative Result

The failure analysis prevents the claim:

\[
\text{all failures are caused by weak angular signal}
\]

because strong-signal failures exist.

Likewise, the analysis prevents the claim:

\[
\text{accurate axis recovery implies accurate }R_2\text{ recovery}
\]

because successful orientation cases can exhibit substantial concentration attenuation.

These negative results materially strengthen the analysis because they define the limits of the learned representation.

---

# 14. Manuscript-Safe Interpretation

> **The learned radial–angular model recovered the measured axial orientation within 15° for 69.6% of the 2,300 sketches, with a population median axial error of 6.13°. Recovery reliability increased with observed circular concentration, and nearly half of high-error failures occurred within the weakest observed-\(R_2\) quartile. Nevertheless, strong-signal failures were also observed, indicating that signal strength alone does not determine recovery success. Circular-strength recovery exhibited a distinct pattern: the learned representation showed a compressed dynamic range, tending to overestimate weak organization and underestimate strong organization. These results demonstrate that axial orientation recovery and circular-strength recovery are empirically separable properties of the learned radial–angular representation.**

---

# 15. Claims We Can Make

The current evidence supports:

- reproducible two-fold angular organization in raw Clo-SKET sketches;
- stable radial localization of this organization;
- category-associated variation in radial–angular geometry;
- significant category-discriminative information;
- a learned relationship between radial position, \(F_2\) magnitude, and axial organization;
- substantial population-level recovery of axial orientation;
- systematic dependence of recovery reliability on observed circular strength;
- distinct recovery behavior for orientation and concentration magnitude.

---

# 16. Claims We Still Cannot Make

The current evidence does **not** establish:

- garment-part recognition;
- physical identity of a Fourier harmonic;
- human-like semantic understanding;
- causal garment structure;
- that \(F_2\) corresponds to a particular garment component;
- that recovery failures arise from one unique mechanism;
- that the learned representation captures the complete angular distribution.

---

# 🔒 Final Cell 30 Scientific Statement

\[
\boxed{
\text{Raw garment sketches exhibit reproducible radial–angular organization}
}
\]

\[
\boxed{
\text{that organization contains category-discriminative information}
}
\]

\[
\boxed{
\text{and a substantial component of its axial structure is learnable}
}
\]

but:

\[
\boxed{
\text{orientation recovery and circular-strength recovery remain distinct}
}
\]

and:

\[
\boxed{
\text{the geometry has not yet been assigned garment-part semantics}
}
\]

This provides a defensible transition from:

**geometric organization**

to:

**learnable category-associated structure**

without overstating the result as semantic garment understanding.

# 🧪 CLO-SKET — CELLS 30F–30H
# Recovery Reliability, Failure Regimes, and Final Radial–Angular Synthesis

## Objective

Cells 30F–30H examine the reliability of the learned radial–angular representation after the population-level recovery analysis.

The analysis asks three related questions:

1. **When is the learned axial orientation reliable?**
2. **What distinguishes successful recovery from failure?**
3. **Are circular-strength recovery and angular-orientation recovery the same phenomenon?**

The analysis remains entirely diagnostic.

No classifier is retrained, no category labels are used, and no representation is altered.

---

# Cell 30F — Recovery Reliability / Failure-Regime Analysis

## Recovery-Regime Definition

Each sketch is assigned to a recovery regime using only the axial angular error:

\[
\Delta \alpha
=
\min
\left(
|\alpha_{\mathrm{obs}}-\alpha_{\mathrm{learned}}|\bmod 180^\circ,
180^\circ-
|\alpha_{\mathrm{obs}}-\alpha_{\mathrm{learned}}|\bmod 180^\circ
\right)
\]

with:

- **Reliable recovery:** \(\Delta\alpha \leq 15^\circ\)
- **Moderate recovery:** \(15^\circ < \Delta\alpha \leq 45^\circ\)
- **Failure:** \(\Delta\alpha > 45^\circ\)

Because the orientation is axial,

\[
\alpha \equiv \alpha + 180^\circ
\]

and the maximum possible axial disagreement is therefore \(90^\circ\).

---

## Population Recovery Regimes

| Recovery regime | N | Population fraction | Median observed \(R_2\) | Median learned \(R_2\) | Median \(\Delta R_2\) | Median peak \(|F_2|\) | Median angular error |
|---|---:|---:|---:|---:|---:|---:|---:|
| Reliable \(\leq15^\circ\) | 1600 | 69.57% | 0.4973 | 0.4446 | -0.0830 | 0.04147 | 3.37° |
| Moderate 15–45° | 231 | 10.04% | 0.2598 | 0.3365 | +0.0582 | 0.04153 | 22.46° |
| Failure \(>45^\circ\) | 469 | 20.39% | 0.3172 | 0.2579 | -0.0656 | 0.02521 | 80.56° |

where:

\[
\Delta R_2
=
R_{2,\mathrm{learned}}
-
R_{2,\mathrm{observed}}
\]

---

# 1. Most Sketches Show Reliable Axial Recovery

The largest population group is the reliable regime:

\[
\frac{1600}{2300}
=
69.57\%
\]

Thus approximately seven out of ten sketches have an observed-versus-learned axial disagreement of no more than \(15^\circ\).

A further:

\[
10.04\%
\]

fall within the moderate-error regime.

The high-error failure regime contains:

\[
20.39\%
\]

of the population.

Therefore the learned representation does not recover orientation uniformly, but successful low-error recovery is the dominant population regime.

---

# 2. Observed Circular Strength Is Associated with Recovery Reliability

Reliable sketches exhibit substantially stronger observed circular organization:

\[
\mathrm{median}\ R_{2,\mathrm{obs}}
=
0.4973
\]

compared with:

\[
0.3172
\]

for the failure group.

Earlier population analysis also showed:

\[
\rho_{\mathrm{Spearman}}
\left(
R_{2,\mathrm{obs}},
\Delta\alpha
\right)
=
-0.4794
\]

indicating that stronger observed circular organization is associated with smaller axial error.

The stratified analysis in Cell 30E further showed a strong monotonic population trend:

\[
23.58^\circ
\rightarrow
8.57^\circ
\rightarrow
4.53^\circ
\rightarrow
2.56^\circ
\]

in median error from the weakest to the strongest observed-\(R_2\) quartile.

---

# 3. Failure Is Enriched in the Weak-\(R_2\) Regime

The lower quartile of observed circular strength is defined by:

\[
R_{2,\mathrm{obs}}
\leq
0.3000
\]

Among the 469 high-error failures:

\[
217
\]

occur in this lowest-\(R_2\) quartile.

Therefore:

\[
\frac{217}{469}
=
46.27\%
\]

of all high-error failures are concentrated in the weakest quarter of the observed circular-strength distribution.

This is considerably greater than the 25% expected from an evenly distributed failure pattern.

The result supports the interpretation that weak circular organization is associated with reduced angular recoverability.

However, it does **not** imply that weak \(R_2\) is sufficient to explain all failures.

---

# 4. \(F_2\) Magnitude Is Also Lower in the Failure Regime

Median peak \(F_2\) magnitude is:

\[
0.04147
\]

for reliably recovered sketches but only:

\[
0.02521
\]

for failures.

Thus failure sketches tend to exhibit weaker second-harmonic structure.

This is consistent with the interpretation that the learned axial direction becomes less recoverable when the underlying two-fold signal itself is weak.

However, this association is not deterministic.

Strong-\(F_2\) failures are also observed.

---

# 5. Strength Recovery and Orientation Recovery Are Distinct

The sign of:

\[
\Delta R_2
=
R_{2,\mathrm{learned}}
-
R_{2,\mathrm{observed}}
\]

varies across recovery regimes.

### Reliable regime

\[
\mathrm{median}\ \Delta R_2
=
-0.0830
\]

Despite excellent angular recovery, the learned circular strength is usually lower than observed.

### Moderate regime

\[
\mathrm{median}\ \Delta R_2
=
+0.0582
\]

Here learned circular strength tends to exceed observed strength.

### Failure regime

\[
\mathrm{median}\ \Delta R_2
=
-0.0656
\]

High angular error can coexist with underestimation of circular strength.

Therefore angular error and circular-strength error do not describe the same property.

\[
\boxed{
\text{orientation recovery}
\neq
\text{circular-strength recovery}
}
\]

---

# Cell 30G — Representative Success and Failure Cases

Four representative sketches were selected directly from the empirical recovery regimes.

No garment category was used in their selection.

---

## Case 1 — Strong Successful Recovery

**Sketch 1652**

- Peak radius: \(r=23.50\)
- Peak \(|F_2|=0.07669\)
- Observed \(R_2=0.844\)
- Learned \(R_2=0.503\)
- \(\Delta R_2=-0.340\)
- Axial error: \(0.26^\circ\)

This sketch provides a particularly clear example of the distinction between angular and strength recovery.

The preferred axial orientation is recovered almost perfectly:

\[
\Delta\alpha
=
0.26^\circ
\]

yet the learned circular concentration is substantially attenuated:

\[
0.503
<
0.844
\]

Thus excellent orientation recovery does not require accurate recovery of concentration magnitude.

---

## Case 2 — Weak-Signal Failure

**Sketch 1978**

- Peak radius: \(r=5.50\)
- Peak \(|F_2|=0.03951\)
- Observed \(R_2=0.001\)
- Learned \(R_2=0.244\)
- \(\Delta R_2=+0.242\)
- Axial error: \(83.99^\circ\)

The observed circular organization is essentially absent:

\[
R_{2,\mathrm{obs}}
\approx 0
\]

In such a regime, the observed preferred axis is intrinsically weakly defined.

The learned model nevertheless produces a nonzero concentration and an orientation far from the measured one.

This case illustrates a plausible **weak-signal failure regime**.

The appropriate interpretation is not that the model chose a physically incorrect garment axis, but that axial recovery becomes unreliable when the measured circular signal provides very little directional support.

---

## Case 3 — Strong-Signal Failure

**Sketch 1994**

- Peak radius: \(r=8.50\)
- Peak \(|F_2|=0.03405\)
- Observed \(R_2=0.811\)
- Learned \(R_2=0.124\)
- \(\Delta R_2=-0.687\)
- Axial error: \(88.23^\circ\)

This is diagnostically important.

The sketch has strong observed circular organization:

\[
R_{2,\mathrm{obs}}
=
0.811
\]

yet the learned orientation is almost maximally misaligned:

\[
\Delta\alpha
=
88.23^\circ
\]

Therefore weak observed \(R_2\) cannot explain every failure.

This prevents an overly simple interpretation such as:

> low circular strength causes all angular failures.

The population trend is real, but exceptions remain substantial and scientifically important.

---

## Case 4 — Moderate Recovery

**Sketch 1242**

- Peak radius: \(r=9.50\)
- Peak \(|F_2|=0.04831\)
- Observed \(R_2=0.123\)
- Learned \(R_2=0.084\)
- \(\Delta R_2=-0.039\)
- Axial error: \(29.90^\circ\)

This case represents the intermediate recovery regime.

Neither orientation agreement nor circular-strength disagreement is extreme.

It demonstrates that recovery behavior is continuous rather than cleanly divided into only success and failure.

---

# Representative-Case Interpretation

Together, these cases establish that at least three different recovery behaviors occur:

\[
\text{strong signal + good orientation recovery}
\]

\[
\text{weak signal + poor orientation recovery}
\]

and:

\[
\text{strong signal + poor orientation recovery}
\]

The third case is particularly important because it demonstrates that recovery failure is not reducible to signal weakness alone.

---

# Cell 30H — Final Population Synthesis

## Population Summary

| Quantity | Result |
|---|---:|
| Population | 2300 |
| Shared radial domain | 3.50–27.50 |
| Reliable \(\leq15^\circ\) | 1600 (69.57%) |
| Moderate 15–45° | 231 (10.04%) |
| Failure \(>45^\circ\) | 469 (20.39%) |
| Median observed \(R_2\) | 0.4364 |
| Median learned \(R_2\) | 0.4032 |
| Median \(\Delta R_2\) | -0.0688 |
| Median axial error | 6.13° |
| Median axial agreement \(\cos(2\Delta\alpha)\) | 0.9772 |
| Median \(F_2\) peak radius | 21.50 |
| Median \(F_2\) peak magnitude | 0.03914 |

---

# 6. The Population Shows Strong but Incomplete Orientation Recovery

The median axial error is:

\[
6.13^\circ
\]

and:

\[
69.57\%
\]

of sketches fall within \(15^\circ\).

The corresponding median doubled-angle axial agreement is:

\[
\cos(2\Delta\alpha)
=
0.9772
\]

indicating strong population-level angular agreement.

The representation therefore learns a substantial component of the measured axial organization.

However:

\[
20.39\%
\]

of the population remains in the high-error regime.

Thus the learned relationship is systematic but not universally accurate.

---

# 7. Learned Circular Strength Is Systematically Compressed

Across the full population:

\[
\mathrm{median}\ R_{2,\mathrm{obs}}
=
0.4364
\]

while:

\[
\mathrm{median}\ R_{2,\mathrm{learned}}
=
0.4032
\]

and:

\[
\mathrm{median}\ \Delta R_2
=
-0.0688
\]

The learned representation therefore tends, on average, to underestimate observed circular strength.

The stratified analysis shows that this bias is not constant.

At weak observed \(R_2\), the model tends to overestimate concentration.

At strong observed \(R_2\), it increasingly underestimates concentration.

This produces a compressed learned dynamic range.

---

# 8. Circular Strength Predicts Reliability Better Than It Determines It

Population-level association:

\[
\rho
\left(
R_{2,\mathrm{obs}},
\Delta\alpha
\right)
=
-0.4794
\]

shows a substantial relationship between signal strength and angular recovery.

But the strong-signal failure case demonstrates that:

\[
R_{2,\mathrm{obs}}\text{ high}
\not\Rightarrow
\Delta\alpha\text{ small}
\]

for every sketch.

Thus observed circular strength is a **reliability-associated variable**, not a deterministic guarantee of recovery.

---

# 9. \(F_2\) Strength Also Relates to Recovery Regime

Reliable sketches exhibit stronger median peak second-harmonic magnitude than failure sketches:

\[
0.04147
\quad\text{vs}\quad
0.02521
\]

respectively.

This supports a second empirical relationship:

\[
|F_2|
\uparrow
\quad\Longrightarrow\quad
\text{greater probability of reliable orientation recovery}
\]

at the population level.

Again, the presence of strong-signal failures prevents a deterministic interpretation.

---

# 10. Radial Location Also Differs Across Recovery Regimes

Median \(F_2\) peak radii are:

\[
22.50
\]

for the reliable regime,

\[
18.50
\]

for moderate recovery, and:

\[
17.50
\]

for the failure regime.

Therefore high-quality angular recovery is associated not only with stronger circular organization but also with a tendency for the dominant \(F_2\) structure to occur farther from the centroid.

This radial association is descriptive and should not yet be assigned garment-part meaning.

---

# 11. Main Scientific Result of Cells 30D–30H

The learned model captures a reproducible radial–angular population relationship, but its recovery behavior is multidimensional.

Two distinct quantities must be separated:

## Axial orientation

\[
\alpha_2
\]

describes **where** the two-fold organization is directed.

## Circular concentration

\[
R_2
\]

describes **how strongly** angular mass is organized around that axis.

The results show that these quantities can behave independently.

For example:

\[
\Delta\alpha \approx 0^\circ
\]

can coexist with substantial:

\[
\Delta R_2 < 0
\]

and conversely strong observed \(R_2\) can coexist with large angular disagreement.

Therefore:

\[
\boxed{
\text{directional recovery and concentration recovery are empirically separable}
}
\]

---

# 12. What Has Been Established

The raw-image analysis now supports the following evidence chain:

\[
\text{raw grayscale sketch}
\]

\[
\downarrow
\]

\[
\text{intensity-weighted centroid}
\]

\[
\downarrow
\]

\[
p(\theta\mid r)
\]

\[
\downarrow
\]

\[
F_2(r),\;\alpha_2(r)
\]

\[
\downarrow
\]

\[
R_2(r)
\]

\[
\downarrow
\]

\[
(r,|F_2|)
\rightarrow
(\hat C_2,\hat S_2)
\]

\[
\downarrow
\]

\[
(\hat R_2,\hat\alpha_2)
\]

\[
\downarrow
\]

\[
\text{population-level radial–angular recovery}
\]

The learned model shows meaningful recovery of the observed axial organization across the population.

Recovery reliability is strongly associated with the strength of measured angular organization but is not determined by signal strength alone.

---

# 13. Important Negative Result

The failure analysis prevents the claim:

\[
\text{all failures are caused by weak angular signal}
\]

because strong-signal failures exist.

Likewise, the analysis prevents the claim:

\[
\text{accurate axis recovery implies accurate }R_2\text{ recovery}
\]

because successful orientation cases can exhibit substantial concentration attenuation.

These negative results materially strengthen the analysis because they define the limits of the learned representation.

---

# 14. Manuscript-Safe Interpretation

> **The learned radial–angular model recovered the measured axial orientation within 15° for 69.6% of the 2,300 sketches, with a population median axial error of 6.13°. Recovery reliability increased with observed circular concentration, and nearly half of high-error failures occurred within the weakest observed-\(R_2\) quartile. Nevertheless, strong-signal failures were also observed, indicating that signal strength alone does not determine recovery success. Circular-strength recovery exhibited a distinct pattern: the learned representation showed a compressed dynamic range, tending to overestimate weak organization and underestimate strong organization. These results demonstrate that axial orientation recovery and circular-strength recovery are empirically separable properties of the learned radial–angular representation.**

---

# 15. Claims We Can Make

The current evidence supports:

- reproducible two-fold angular organization in raw Clo-SKET sketches;
- stable radial localization of this organization;
- category-associated variation in radial–angular geometry;
- significant category-discriminative information;
- a learned relationship between radial position, \(F_2\) magnitude, and axial organization;
- substantial population-level recovery of axial orientation;
- systematic dependence of recovery reliability on observed circular strength;
- distinct recovery behavior for orientation and concentration magnitude.

---

# 16. Claims We Still Cannot Make

The current evidence does **not** establish:

- garment-part recognition;
- physical identity of a Fourier harmonic;
- human-like semantic understanding;
- causal garment structure;
- that \(F_2\) corresponds to a particular garment component;
- that recovery failures arise from one unique mechanism;
- that the learned representation captures the complete angular distribution.

---

# 🔒 Final Cell 30 Scientific Statement

\[
\boxed{
\text{Raw garment sketches exhibit reproducible radial–angular organization}
}
\]

\[
\boxed{
\text{that organization contains category-discriminative information}
}
\]

\[
\boxed{
\text{and a substantial component of its axial structure is learnable}
}
\]

but:

\[
\boxed{
\text{orientation recovery and circular-strength recovery remain distinct}
}
\]

and:

\[
\boxed{
\text{the geometry has not yet been assigned garment-part semantics}
}
\]

This provides a defensible transition from:

**geometric organization**

to:

**learnable category-associated structure**

without overstating the result as semantic garment understanding.

# 🧪 CLO-SKET — CELLS 30I–30J
# Statistical Robustness and Confidence Analysis of Radial–Angular Recovery

## Objective

Cells 30I–30J formally test and visualize whether the radial–angular quantities identified in Cells 30D–30H are statistically associated with axial recovery reliability.

The analysis is performed under the previously locked radial domain:

\[
r = 3.50 \rightarrow 27.50
\]

using exactly:

\[
25
\]

shared radial/circular shells.

No new representation is introduced.

No classifier is retrained.

No category labels are used.

---

# Cell 30I — Statistical Robustness / Association Tests

## Domain Consistency

All quantities are measured within the same established radial domain:

\[
3.50 \leq r \leq 27.50
\]

The \(F_2\) peak is identified only inside this region and then matched exactly to the corresponding circular shell.

Maximum radial mismatch:

\[
0.0000
\]

Therefore the statistical analysis does not mix geometric measurements from different radial domains.

---

# Primary Recovery Outcome

The principal recovery variable is the axial angular error:

\[
\Delta \alpha
=
\min
\left(
|\alpha_{\mathrm{obs}}-\alpha_{\mathrm{learned}}|\bmod180^\circ,
180^\circ-
|\alpha_{\mathrm{obs}}-\alpha_{\mathrm{learned}}|\bmod180^\circ
\right)
\]

Because the orientation is axial:

\[
\alpha \equiv \alpha + 180^\circ
\]

and therefore:

\[
0^\circ \leq \Delta\alpha \leq 90^\circ
\]

Smaller values correspond to better orientation recovery.

---

# 1. Observed Circular Strength Is the Strongest Tested Associate of Axial Recovery

For observed circular concentration:

\[
R_{2,\mathrm{obs}}
\]

versus axial error:

### Pearson correlation

\[
r=-0.3686
\]

\[
p=5.96\times10^{-75}
\]

### Spearman correlation

\[
\rho=-0.4794
\]

\[
p=1.62\times10^{-132}
\]

Bootstrapped 95% confidence interval:

\[
\rho
=
-0.4794
\quad
[95\%\,CI:
-0.5103,\,-0.4476]
\]

The interval remains clearly below zero.

Thus stronger observed circular organization is robustly associated with lower angular recovery error.

Among the three tested radial–angular quantities, observed \(R_2\) shows the strongest monotonic association with recovery error.

---

# 2. \(F_2\) Peak Magnitude Is Also Associated with Recovery Reliability

For peak second-harmonic magnitude:

\[
|F_2|_{\mathrm{peak}}
\]

versus axial error:

### Pearson correlation

\[
r=-0.2505
\]

\[
p=2.97\times10^{-34}
\]

### Spearman correlation

\[
\rho=-0.1784
\]

\[
p=6.74\times10^{-18}
\]

Bootstrapped 95% confidence interval:

\[
\rho
=
-0.1784
\quad
[95\%\,CI:
-0.2196,\,-0.1349]
\]

The association is statistically robust but weaker than that observed for \(R_2\).

Therefore stronger \(F_2\) structure is associated with improved angular recovery, but the effect is modest.

---

# 3. Radial Location of the \(F_2\) Peak Is Substantially Associated with Recovery

For \(F_2\) peak radius:

\[
r_{F_2,\mathrm{peak}}
\]

versus axial error:

### Pearson correlation

\[
r=-0.3262
\]

\[
p=3.77\times10^{-58}
\]

### Spearman correlation

\[
\rho=-0.3646
\]

\[
p=3.08\times10^{-73}
\]

Bootstrapped 95% confidence interval:

\[
\rho
=
-0.3646
\quad
[95\%\,CI:
-0.3992,\,-0.3287]
\]

Thus sketches whose dominant \(F_2\) structure occurs farther from the centroid tend to exhibit lower axial recovery error.

This association is stronger than the association with \(F_2\) magnitude but weaker than the association with observed \(R_2\).

The ordering of the tested monotonic associations is therefore:

\[
|\,\rho(R_2,\Delta\alpha)\,|
>
|\,\rho(r_{F_2},\Delta\alpha)\,|
>
|\,\rho(|F_2|,\Delta\alpha)\,|
\]

or numerically:

\[
0.4794
>
0.3646
>
0.1784
\]

---

# 4. Circular-Strength Error Is Strongly Related to Observed Circular Strength

Define:

\[
\Delta R_2
=
R_{2,\mathrm{learned}}
-
R_{2,\mathrm{observed}}
\]

Observed \(R_2\) is strongly negatively associated with \(\Delta R_2\):

### Pearson

\[
r=-0.7149
\]

### Spearman

\[
\rho=-0.7138
\]

This relationship is substantially stronger than the associations involving axial error.

The interpretation is consistent with the population patterns observed earlier:

- when observed \(R_2\) is weak, the learned representation often overestimates circular strength;
- when observed \(R_2\) is strong, the learned representation increasingly underestimates circular strength.

This supports the previously observed compression of the learned \(R_2\) dynamic range.

---

# 5. \(F_2\) Magnitude Has Little Association with Circular-Strength Bias

For peak \(F_2\) magnitude versus:

\[
\Delta R_2
\]

the results are:

### Pearson

\[
r=0.0495,
\qquad
p=0.0176
\]

### Spearman

\[
\rho=0.0402,
\qquad
p=0.0537
\]

These associations are extremely small.

Thus \(F_2\) peak magnitude is associated with orientation reliability, but it does not meaningfully explain the magnitude bias:

\[
\Delta R_2
\]

This further supports the distinction between:

**orientation recovery**

and:

**circular-strength recovery**.

---

# Recovery-Group Statistical Comparison

The recovery groups remain defined exclusively by axial angular error:

- Reliable: \(\Delta\alpha \leq15^\circ\)
- Moderate: \(15^\circ < \Delta\alpha \leq45^\circ\)
- Failure: \(\Delta\alpha >45^\circ\)

Population sizes:

| Group | N |
|---|---:|
| Reliable | 1600 |
| Moderate | 231 |
| Failure | 469 |

The formal group comparison focuses on:

\[
\text{Reliable}
\quad\text{vs}\quad
\text{Failure}
\]

using the Mann–Whitney \(U\) test and Cliff's delta.

---

# 6. Reliable and Failure Sketches Differ Strongly in Observed \(R_2\)

Median observed circular strength:

\[
\text{Reliable}
=
0.4973
\]

\[
\text{Failure}
=
0.3172
\]

Mann–Whitney result:

\[
p
=
1.08\times10^{-70}
\]

Effect size:

\[
\delta_{\mathrm{Cliff}}
=
+0.5390
\]

This is the largest of the three tested reliable-versus-failure effect sizes.

Therefore observed circular strength differs substantially between successful and failed angular-recovery regimes.

---

# 7. Reliable and Failure Sketches Also Differ in \(F_2\) Magnitude

Median peak \(F_2\):

\[
\text{Reliable}
=
0.04147
\]

\[
\text{Failure}
=
0.02521
\]

Mann–Whitney result:

\[
p
=
4.94\times10^{-37}
\]

Cliff's delta:

\[
\delta
=
+0.3855
\]

Thus reliable sketches tend to contain stronger peak second-harmonic structure.

The effect is clear, but smaller than the observed-\(R_2\) effect.

---

# 8. Reliable and Failure Sketches Differ in Radial Localization

Median \(F_2\) peak radius:

\[
\text{Reliable}
=
22.5
\]

\[
\text{Failure}
=
17.5
\]

Mann–Whitney result:

\[
p
=
7.44\times10^{-48}
\]

Cliff's delta:

\[
\delta
=
+0.4395
\]

Thus reliable recovery is associated with a more outward radial localization of the dominant two-fold structure.

Among the three reliable-versus-failure comparisons:

\[
\delta(R_2)
=
0.5390
\]

\[
\delta(r_{F_2})
=
0.4395
\]

\[
\delta(|F_2|)
=
0.3855
\]

Therefore observed circular strength provides the strongest group separation, followed by radial location and then \(F_2\) peak magnitude.

---

# Cell 30J — Robustness / Confidence Visualization

Cell 30J visualizes the precomputed statistical results from Cell 30I.

No new test is performed.

---

# Figure 1 — Spearman Associations with Axial Error

The bootstrap-confidence visualization shows:

\[
R_{2,\mathrm{obs}}
:
\rho=-0.4794
\]

\[
r_{F_2,\mathrm{peak}}
:
\rho=-0.3646
\]

\[
|F_2|_{\mathrm{peak}}
:
\rho=-0.1784
\]

with all 95% confidence intervals remaining entirely below zero.

This confirms that all three associations are directionally stable under bootstrap resampling.

The strongest empirical predictor among these measured quantities is observed circular organization.

---

# Figure 2 — Reliable vs Failure Effect Sizes

Cliff's delta confirms meaningful reliable-versus-failure separation for all three quantities:

| Variable | Cliff's \(\delta\) |
|---|---:|
| Observed \(R_2\) | 0.5390 |
| \(F_2\) peak radius | 0.4395 |
| \(F_2\) peak magnitude | 0.3855 |

The ordering mirrors the correlation analysis.

Thus the same qualitative conclusion appears under two different statistical views:

1. continuous association with angular error;
2. direct comparison of reliable versus failed recovery.

---

# Figure 3 — Observed \(R_2\) Across Recovery Regimes

The observed-\(R_2\) distribution differs visibly across recovery regimes.

Median values are approximately:

\[
0.4973
\]

for reliable recovery,

\[
0.2598
\]

for moderate recovery, and:

\[
0.3172
\]

for failure.

The ordering of the moderate and failure medians is not strictly monotonic.

This is important.

The recovery regimes are defined from angular error, and the observed-\(R_2\) relationship is probabilistic rather than deterministic.

Therefore:

\[
R_2
\]

is associated with recovery reliability but does not uniquely determine the recovery regime.

---

# Combined Scientific Interpretation

Cells 30I–30J provide formal statistical support for patterns previously identified descriptively.

Three measured geometric quantities are associated with axial orientation recovery:

\[
R_{2,\mathrm{obs}}
\]

\[
r_{F_2,\mathrm{peak}}
\]

and:

\[
|F_2|_{\mathrm{peak}}
\]

The strongest relationship is observed for circular organization itself:

\[
\rho=-0.4794
\]

followed by radial location:

\[
\rho=-0.3646
\]

and peak \(F_2\) magnitude:

\[
\rho=-0.1784
\]

All three bootstrap confidence intervals exclude zero.

Reliable-versus-failure comparisons independently support the same ordering.

---

# Main Robustness Result

The statistical evidence supports:

\[
\boxed{
\text{stronger observed circular organization is associated with more reliable axial recovery}
}
\]

and:

\[
\boxed{
\text{more outward localization of dominant }F_2
\text{ is also associated with better recovery}
}
\]

while:

\[
\boxed{
\text{peak }F_2\text{ magnitude contributes a weaker but reproducible association}
}
\]

These relationships are statistically robust across the full population of:

\[
N=2300
\]

sketches.

---

# Important Distinction

The strongest relationship involving circular-strength error is:

\[
R_{2,\mathrm{obs}}
\leftrightarrow
\Delta R_2
\]

with:

\[
\rho=-0.7138
\]

whereas the relationship involving angular recovery is weaker:

\[
R_{2,\mathrm{obs}}
\leftrightarrow
\Delta\alpha
\]

with:

\[
\rho=-0.4794
\]

Therefore the learned representation exhibits at least two separable behaviors:

### 1. Orientation reliability

How accurately the learned model recovers:

\[
\alpha_2
\]

### 2. Circular-strength calibration

How accurately the model recovers:

\[
R_2
\]

These should not be collapsed into a single notion of representation quality.

---

# Manuscript-Safe Result

> **Axial recovery reliability was significantly associated with the strength and radial organization of the measured two-fold geometry. Observed circular concentration showed the strongest monotonic association with axial error (Spearman \(\rho=-0.479\), bootstrap 95% CI \([-0.510,-0.448]\)), followed by the radial position of peak \(F_2\) (\(\rho=-0.365\), 95% CI \([-0.399,-0.329]\)) and peak \(F_2\) magnitude (\(\rho=-0.178\), 95% CI \([-0.220,-0.135]\)). Reliable and failed recovery regimes were also separated by moderate-to-large Cliff's delta effect sizes for observed \(R_2\) (\(\delta=0.539\)), peak radius (\(\delta=0.440\)), and peak \(F_2\) magnitude (\(\delta=0.386\)). These results establish robust empirical associations between measured radial–angular organization and recovery reliability, while not implying causality or semantic garment-part interpretation.**

---

# What Cell 30I Adds Beyond Cells 30D–30H

Cells 30D–30H established the descriptive pattern:

\[
\text{stronger geometric organization}
\rightarrow
\text{better angular recovery}
\]

Cell 30I formally tests that pattern using:

- Pearson correlation;
- Spearman rank correlation;
- bootstrap confidence intervals;
- Mann–Whitney \(U\);
- Cliff's delta.

Thus the interpretation progresses from:

**visual observation**

to:

**population description**

to:

**formal statistical support**.

---

# What Has Not Been Established

These results do **not** show that:

- \(R_2\) causes successful recovery;
- radial position causes successful recovery;
- \(F_2\) magnitude causes successful recovery;
- the \(F_2\) mode corresponds to a particular garment part;
- the learned system performs human-like semantic interpretation;
- recovery failures have a single underlying mechanism.

The results establish associations only.

---

# 🔒 Cell 30I–30J Result Lock

## Domain

\[
3.50 \rightarrow 27.50
\]

\[
25\text{ matched circular shells}
\]

## Associations with axial error

\[
R_{2,\mathrm{obs}}:
\quad
\rho=-0.4794
\quad
[95\%\,CI=-0.5103,-0.4476]
\]

\[
r_{F_2,\mathrm{peak}}:
\quad
\rho=-0.3646
\quad
[95\%\,CI=-0.3992,-0.3287]
\]

\[
|F_2|_{\mathrm{peak}}:
\quad
\rho=-0.1784
\quad
[95\%\,CI=-0.2196,-0.1349]
\]

## Reliable-vs-failure effect sizes

\[
\delta(R_2)
=
0.5390
\]

\[
\delta(r_{F_2})
=
0.4395
\]

\[
\delta(|F_2|)
=
0.3855
\]

## Circular-strength calibration

\[
\rho
\left(
R_{2,\mathrm{obs}},
\Delta R_2
\right)
=
-0.7138
\]

---

# Final Scientific Statement

The recovery analysis now supports a statistically robust relationship between the measured radial–angular organization of raw fashion sketches and the reliability with which that organization can be learned.

The evidence specifically supports:

\[
\boxed{
R_2\text{ strength}
}
\]

\[
\boxed{
F_2\text{ radial localization}
}
\]

and, more weakly,

\[
\boxed{
F_2\text{ magnitude}
}
\]

as population-level correlates of axial recovery reliability.

At the same time:

\[
\boxed{
\text{orientation recovery}
\neq
\text{circular-strength calibration}
}
\]

and none of these associations yet imply garment-part semantics or causal structure.

# 🧪 CLO-SKET — CELLS 30I–30J
# Statistical Robustness and Confidence Analysis of Radial–Angular Recovery

## Objective

Cells 30I–30J formally test and visualize whether the radial–angular quantities identified in Cells 30D–30H are statistically associated with axial recovery reliability.

The analysis is performed under the previously locked radial domain:

\[
r = 3.50 \rightarrow 27.50
\]

using exactly:

\[
25
\]

shared radial/circular shells.

No new representation is introduced.

No classifier is retrained.

No category labels are used.

---

# Cell 30I — Statistical Robustness / Association Tests

## Domain Consistency

All quantities are measured within the same established radial domain:

\[
3.50 \leq r \leq 27.50
\]

The \(F_2\) peak is identified only inside this region and then matched exactly to the corresponding circular shell.

Maximum radial mismatch:

\[
0.0000
\]

Therefore the statistical analysis does not mix geometric measurements from different radial domains.

---

# Primary Recovery Outcome

The principal recovery variable is the axial angular error:

\[
\Delta \alpha
=
\min
\left(
|\alpha_{\mathrm{obs}}-\alpha_{\mathrm{learned}}|\bmod180^\circ,
180^\circ-
|\alpha_{\mathrm{obs}}-\alpha_{\mathrm{learned}}|\bmod180^\circ
\right)
\]

Because the orientation is axial:

\[
\alpha \equiv \alpha + 180^\circ
\]

and therefore:

\[
0^\circ \leq \Delta\alpha \leq 90^\circ
\]

Smaller values correspond to better orientation recovery.

---

# 1. Observed Circular Strength Is the Strongest Tested Associate of Axial Recovery

For observed circular concentration:

\[
R_{2,\mathrm{obs}}
\]

versus axial error:

### Pearson correlation

\[
r=-0.3686
\]

\[
p=5.96\times10^{-75}
\]

### Spearman correlation

\[
\rho=-0.4794
\]

\[
p=1.62\times10^{-132}
\]

Bootstrapped 95% confidence interval:

\[
\rho
=
-0.4794
\quad
[95\%\,CI:
-0.5103,\,-0.4476]
\]

The interval remains clearly below zero.

Thus stronger observed circular organization is robustly associated with lower angular recovery error.

Among the three tested radial–angular quantities, observed \(R_2\) shows the strongest monotonic association with recovery error.

---

# 2. \(F_2\) Peak Magnitude Is Also Associated with Recovery Reliability

For peak second-harmonic magnitude:

\[
|F_2|_{\mathrm{peak}}
\]

versus axial error:

### Pearson correlation

\[
r=-0.2505
\]

\[
p=2.97\times10^{-34}
\]

### Spearman correlation

\[
\rho=-0.1784
\]

\[
p=6.74\times10^{-18}
\]

Bootstrapped 95% confidence interval:

\[
\rho
=
-0.1784
\quad
[95\%\,CI:
-0.2196,\,-0.1349]
\]

The association is statistically robust but weaker than that observed for \(R_2\).

Therefore stronger \(F_2\) structure is associated with improved angular recovery, but the effect is modest.

---

# 3. Radial Location of the \(F_2\) Peak Is Substantially Associated with Recovery

For \(F_2\) peak radius:

\[
r_{F_2,\mathrm{peak}}
\]

versus axial error:

### Pearson correlation

\[
r=-0.3262
\]

\[
p=3.77\times10^{-58}
\]

### Spearman correlation

\[
\rho=-0.3646
\]

\[
p=3.08\times10^{-73}
\]

Bootstrapped 95% confidence interval:

\[
\rho
=
-0.3646
\quad
[95\%\,CI:
-0.3992,\,-0.3287]
\]

Thus sketches whose dominant \(F_2\) structure occurs farther from the centroid tend to exhibit lower axial recovery error.

This association is stronger than the association with \(F_2\) magnitude but weaker than the association with observed \(R_2\).

The ordering of the tested monotonic associations is therefore:

\[
|\,\rho(R_2,\Delta\alpha)\,|
>
|\,\rho(r_{F_2},\Delta\alpha)\,|
>
|\,\rho(|F_2|,\Delta\alpha)\,|
\]

or numerically:

\[
0.4794
>
0.3646
>
0.1784
\]

---

# 4. Circular-Strength Error Is Strongly Related to Observed Circular Strength

Define:

\[
\Delta R_2
=
R_{2,\mathrm{learned}}
-
R_{2,\mathrm{observed}}
\]

Observed \(R_2\) is strongly negatively associated with \(\Delta R_2\):

### Pearson

\[
r=-0.7149
\]

### Spearman

\[
\rho=-0.7138
\]

This relationship is substantially stronger than the associations involving axial error.

The interpretation is consistent with the population patterns observed earlier:

- when observed \(R_2\) is weak, the learned representation often overestimates circular strength;
- when observed \(R_2\) is strong, the learned representation increasingly underestimates circular strength.

This supports the previously observed compression of the learned \(R_2\) dynamic range.

---

# 5. \(F_2\) Magnitude Has Little Association with Circular-Strength Bias

For peak \(F_2\) magnitude versus:

\[
\Delta R_2
\]

the results are:

### Pearson

\[
r=0.0495,
\qquad
p=0.0176
\]

### Spearman

\[
\rho=0.0402,
\qquad
p=0.0537
\]

These associations are extremely small.

Thus \(F_2\) peak magnitude is associated with orientation reliability, but it does not meaningfully explain the magnitude bias:

\[
\Delta R_2
\]

This further supports the distinction between:

**orientation recovery**

and:

**circular-strength recovery**.

---

# Recovery-Group Statistical Comparison

The recovery groups remain defined exclusively by axial angular error:

- Reliable: \(\Delta\alpha \leq15^\circ\)
- Moderate: \(15^\circ < \Delta\alpha \leq45^\circ\)
- Failure: \(\Delta\alpha >45^\circ\)

Population sizes:

| Group | N |
|---|---:|
| Reliable | 1600 |
| Moderate | 231 |
| Failure | 469 |

The formal group comparison focuses on:

\[
\text{Reliable}
\quad\text{vs}\quad
\text{Failure}
\]

using the Mann–Whitney \(U\) test and Cliff's delta.

---

# 6. Reliable and Failure Sketches Differ Strongly in Observed \(R_2\)

Median observed circular strength:

\[
\text{Reliable}
=
0.4973
\]

\[
\text{Failure}
=
0.3172
\]

Mann–Whitney result:

\[
p
=
1.08\times10^{-70}
\]

Effect size:

\[
\delta_{\mathrm{Cliff}}
=
+0.5390
\]

This is the largest of the three tested reliable-versus-failure effect sizes.

Therefore observed circular strength differs substantially between successful and failed angular-recovery regimes.

---

# 7. Reliable and Failure Sketches Also Differ in \(F_2\) Magnitude

Median peak \(F_2\):

\[
\text{Reliable}
=
0.04147
\]

\[
\text{Failure}
=
0.02521
\]

Mann–Whitney result:

\[
p
=
4.94\times10^{-37}
\]

Cliff's delta:

\[
\delta
=
+0.3855
\]

Thus reliable sketches tend to contain stronger peak second-harmonic structure.

The effect is clear, but smaller than the observed-\(R_2\) effect.

---

# 8. Reliable and Failure Sketches Differ in Radial Localization

Median \(F_2\) peak radius:

\[
\text{Reliable}
=
22.5
\]

\[
\text{Failure}
=
17.5
\]

Mann–Whitney result:

\[
p
=
7.44\times10^{-48}
\]

Cliff's delta:

\[
\delta
=
+0.4395
\]

Thus reliable recovery is associated with a more outward radial localization of the dominant two-fold structure.

Among the three reliable-versus-failure comparisons:

\[
\delta(R_2)
=
0.5390
\]

\[
\delta(r_{F_2})
=
0.4395
\]

\[
\delta(|F_2|)
=
0.3855
\]

Therefore observed circular strength provides the strongest group separation, followed by radial location and then \(F_2\) peak magnitude.

---

# Cell 30J — Robustness / Confidence Visualization

Cell 30J visualizes the precomputed statistical results from Cell 30I.

No new test is performed.

---

# Figure 1 — Spearman Associations with Axial Error

The bootstrap-confidence visualization shows:

\[
R_{2,\mathrm{obs}}
:
\rho=-0.4794
\]

\[
r_{F_2,\mathrm{peak}}
:
\rho=-0.3646
\]

\[
|F_2|_{\mathrm{peak}}
:
\rho=-0.1784
\]

with all 95% confidence intervals remaining entirely below zero.

This confirms that all three associations are directionally stable under bootstrap resampling.

The strongest empirical predictor among these measured quantities is observed circular organization.

---

# Figure 2 — Reliable vs Failure Effect Sizes

Cliff's delta confirms meaningful reliable-versus-failure separation for all three quantities:

| Variable | Cliff's \(\delta\) |
|---|---:|
| Observed \(R_2\) | 0.5390 |
| \(F_2\) peak radius | 0.4395 |
| \(F_2\) peak magnitude | 0.3855 |

The ordering mirrors the correlation analysis.

Thus the same qualitative conclusion appears under two different statistical views:

1. continuous association with angular error;
2. direct comparison of reliable versus failed recovery.

---

# Figure 3 — Observed \(R_2\) Across Recovery Regimes

The observed-\(R_2\) distribution differs visibly across recovery regimes.

Median values are approximately:

\[
0.4973
\]

for reliable recovery,

\[
0.2598
\]

for moderate recovery, and:

\[
0.3172
\]

for failure.

The ordering of the moderate and failure medians is not strictly monotonic.

This is important.

The recovery regimes are defined from angular error, and the observed-\(R_2\) relationship is probabilistic rather than deterministic.

Therefore:

\[
R_2
\]

is associated with recovery reliability but does not uniquely determine the recovery regime.

---

# Combined Scientific Interpretation

Cells 30I–30J provide formal statistical support for patterns previously identified descriptively.

Three measured geometric quantities are associated with axial orientation recovery:

\[
R_{2,\mathrm{obs}}
\]

\[
r_{F_2,\mathrm{peak}}
\]

and:

\[
|F_2|_{\mathrm{peak}}
\]

The strongest relationship is observed for circular organization itself:

\[
\rho=-0.4794
\]

followed by radial location:

\[
\rho=-0.3646
\]

and peak \(F_2\) magnitude:

\[
\rho=-0.1784
\]

All three bootstrap confidence intervals exclude zero.

Reliable-versus-failure comparisons independently support the same ordering.

---

# Main Robustness Result

The statistical evidence supports:

\[
\boxed{
\text{stronger observed circular organization is associated with more reliable axial recovery}
}
\]

and:

\[
\boxed{
\text{more outward localization of dominant }F_2
\text{ is also associated with better recovery}
}
\]

while:

\[
\boxed{
\text{peak }F_2\text{ magnitude contributes a weaker but reproducible association}
}
\]

These relationships are statistically robust across the full population of:

\[
N=2300
\]

sketches.

---

# Important Distinction

The strongest relationship involving circular-strength error is:

\[
R_{2,\mathrm{obs}}
\leftrightarrow
\Delta R_2
\]

with:

\[
\rho=-0.7138
\]

whereas the relationship involving angular recovery is weaker:

\[
R_{2,\mathrm{obs}}
\leftrightarrow
\Delta\alpha
\]

with:

\[
\rho=-0.4794
\]

Therefore the learned representation exhibits at least two separable behaviors:

### 1. Orientation reliability

How accurately the learned model recovers:

\[
\alpha_2
\]

### 2. Circular-strength calibration

How accurately the model recovers:

\[
R_2
\]

These should not be collapsed into a single notion of representation quality.

---

# Manuscript-Safe Result

> **Axial recovery reliability was significantly associated with the strength and radial organization of the measured two-fold geometry. Observed circular concentration showed the strongest monotonic association with axial error (Spearman \(\rho=-0.479\), bootstrap 95% CI \([-0.510,-0.448]\)), followed by the radial position of peak \(F_2\) (\(\rho=-0.365\), 95% CI \([-0.399,-0.329]\)) and peak \(F_2\) magnitude (\(\rho=-0.178\), 95% CI \([-0.220,-0.135]\)). Reliable and failed recovery regimes were also separated by moderate-to-large Cliff's delta effect sizes for observed \(R_2\) (\(\delta=0.539\)), peak radius (\(\delta=0.440\)), and peak \(F_2\) magnitude (\(\delta=0.386\)). These results establish robust empirical associations between measured radial–angular organization and recovery reliability, while not implying causality or semantic garment-part interpretation.**

---

# What Cell 30I Adds Beyond Cells 30D–30H

Cells 30D–30H established the descriptive pattern:

\[
\text{stronger geometric organization}
\rightarrow
\text{better angular recovery}
\]

Cell 30I formally tests that pattern using:

- Pearson correlation;
- Spearman rank correlation;
- bootstrap confidence intervals;
- Mann–Whitney \(U\);
- Cliff's delta.

Thus the interpretation progresses from:

**visual observation**

to:

**population description**

to:

**formal statistical support**.

---

# What Has Not Been Established

These results do **not** show that:

- \(R_2\) causes successful recovery;
- radial position causes successful recovery;
- \(F_2\) magnitude causes successful recovery;
- the \(F_2\) mode corresponds to a particular garment part;
- the learned system performs human-like semantic interpretation;
- recovery failures have a single underlying mechanism.

The results establish associations only.

---

# 🔒 Cell 30I–30J Result Lock

## Domain

\[
3.50 \rightarrow 27.50
\]

\[
25\text{ matched circular shells}
\]

## Associations with axial error

\[
R_{2,\mathrm{obs}}:
\quad
\rho=-0.4794
\quad
[95\%\,CI=-0.5103,-0.4476]
\]

\[
r_{F_2,\mathrm{peak}}:
\quad
\rho=-0.3646
\quad
[95\%\,CI=-0.3992,-0.3287]
\]

\[
|F_2|_{\mathrm{peak}}:
\quad
\rho=-0.1784
\quad
[95\%\,CI=-0.2196,-0.1349]
\]

## Reliable-vs-failure effect sizes

\[
\delta(R_2)
=
0.5390
\]

\[
\delta(r_{F_2})
=
0.4395
\]

\[
\delta(|F_2|)
=
0.3855
\]

## Circular-strength calibration

\[
\rho
\left(
R_{2,\mathrm{obs}},
\Delta R_2
\right)
=
-0.7138
\]

---

# Final Scientific Statement

The recovery analysis now supports a statistically robust relationship between the measured radial–angular organization of raw fashion sketches and the reliability with which that organization can be learned.

The evidence specifically supports:

\[
\boxed{
R_2\text{ strength}
}
\]

\[
\boxed{
F_2\text{ radial localization}
}
\]

and, more weakly,

\[
\boxed{
F_2\text{ magnitude}
}
\]

as population-level correlates of axial recovery reliability.

At the same time:

\[
\boxed{
\text{orientation recovery}
\neq
\text{circular-strength calibration}
}
\]

and none of these associations yet imply garment-part semantics or causal structure.

# CLO-SKET — Final Radial–Angular Evidence, Robustness, and Contribution Lock

## Cells 30K–30Q

---

# Cell 30K — Threshold Sensitivity / Recovery-Regime Robustness

## Scientific Question

Does the observed separation between reliable and failed angular recovery depend strongly on the particular angular-error thresholds used to define recovery regimes?

The primary analysis used:

- Reliable: axial error ≤ 15°
- Moderate: 15° < axial error ≤ 45°
- Failure: axial error > 45°

To test whether the result depends on this specific choice, four reasonable threshold configurations were evaluated:

1. 10° / 30°
2. 15° / 45°
3. 20° / 45°
4. 20° / 60°

No threshold was optimized against the data.

---

## Locked Radial Domain

All threshold analyses retain the established radial domain:

\[
r = 3.50 \rightarrow 27.50
\]

with:

\[
25
\]

shared circular-analysis shells.

Maximum radial-shell mismatch:

\[
0.0000
\]

---

## Threshold Sensitivity Results

| Thresholds | Reliable | Moderate | Failure | Reliable median \(R_2\) | Failure median \(R_2\) | Median difference | Cliff's \(\delta\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| 10° / 30° | 62.30% | 14.74% | 22.96% | 0.5163 | 0.3040 | +0.2124 | +0.6034 |
| 15° / 45° | 69.57% | 10.04% | 20.39% | 0.4973 | 0.3172 | +0.1801 | +0.5390 |
| 20° / 45° | 73.48% | 6.13% | 20.39% | 0.4893 | 0.3172 | +0.1721 | +0.5100 |
| 20° / 60° | 73.48% | 8.39% | 18.13% | 0.4893 | 0.3284 | +0.1609 | +0.4843 |

For every tested threshold configuration:

\[
\text{Median }R_{2,\mathrm{reliable}}
>
\text{Median }R_{2,\mathrm{failure}}
\]

and:

\[
\delta_{\mathrm{Cliff}} > 0
\]

All Mann–Whitney comparisons remained statistically significant.

---

## Robustness Interpretation

The reliable-versus-failure separation in observed circular strength is therefore **not dependent on a single arbitrary threshold definition**.

The effect size varies quantitatively:

\[
0.4843
\leq
\delta
\leq
0.6034
\]

but its direction remains stable.

This analysis supports robustness of the recovery-strength relationship.

It does not establish causality.

---

# Cell 30L — Final Evidence Audit / Claim Boundary

## Representation-Domain Verification

The radial representations have different native dimensionalities:

\[
F_2(r):
72 \text{ radial bins}
\]

and:

\[
R_2(r),\mu_2(r):
25 \text{ circular-analysis shells}
\]

Therefore the valid processing sequence is:

\[
F_2
\rightarrow
\text{locked-domain masking}
\rightarrow
F_2\text{ peak}
\rightarrow
\text{matching circular shell}
\rightarrow
R_2,\mu_2
\]

The 72-bin \(F_2\) mask is **not** directly applied to the 25-column circular arrays.

Exact radial matching was verified:

\[
\text{maximum mismatch}=0.0000
\]

for all:

\[
N=2300
\]

sketches.

---

## Population Recovery

Population:

\[
N=2300
\]

Recovery regimes under the primary 15° / 45° definition:

| Regime | N | Fraction |
|---|---:|---:|
| Reliable ≤15° | 1600 | 69.57% |
| Moderate 15–45° | 231 | 10.04% |
| Failure >45° | 469 | 20.39% |

Median axial error:

\[
6.13^\circ
\]

Median observed circular strength:

\[
R_{2,\mathrm{obs}}=0.4364
\]

Median learned circular strength:

\[
R_{2,\mathrm{learned}}=0.4032
\]

Median strength difference:

\[
\Delta R_2
=
R_{2,\mathrm{learned}}
-
R_{2,\mathrm{observed}}
=
-0.0688
\]

---

# Primary Recovery Associations

## Observed \(R_2\) vs Axial Error

\[
\rho=-0.4794
\]

Bootstrap 95% CI:

\[
[-0.5103,-0.4476]
\]

This is the strongest of the tested recovery associations.

---

## \(F_2\) Peak Radius vs Axial Error

\[
\rho=-0.3646
\]

Bootstrap 95% CI:

\[
[-0.3992,-0.3287]
\]

Dominant \(F_2\) structure occurring farther from the centroid is associated with lower angular recovery error.

---

## \(F_2\) Peak Magnitude vs Axial Error

\[
\rho=-0.1784
\]

Bootstrap 95% CI:

\[
[-0.2196,-0.1349]
\]

The association is weaker but remains reproducible.

---

## Relative Association Strength

The absolute Spearman associations satisfy:

\[
|\,\rho(R_2,\Delta\alpha)\,|
>
|\,\rho(r_{F_2},\Delta\alpha)\,|
>
|\,\rho(|F_2|,\Delta\alpha)\,|
\]

numerically:

\[
0.4794
>
0.3646
>
0.1784
\]

---

# Reliable vs Failure Effect Sizes

Observed circular strength:

\[
\delta=+0.5390
\]

\(F_2\) peak radius:

\[
\delta=+0.4395
\]

\(F_2\) peak magnitude:

\[
\delta=+0.3855
\]

The largest reliable-versus-failure separation occurs for observed circular organization.

---

# Circular-Strength Recovery

Observed \(R_2\) is strongly associated with:

\[
\Delta R_2
=
R_{2,\mathrm{learned}}
-
R_{2,\mathrm{observed}}
\]

with:

\[
\rho=-0.7138
\]

This indicates a systematic difference between observed and learned circular strength.

Higher observed \(R_2\) tends to accompany stronger negative:

\[
\Delta R_2
\]

meaning that stronger observed circular organization tends to be attenuated by the learned model.

By contrast:

\[
\rho(|F_2|_{\mathrm{peak}},\Delta R_2)
=
0.0402
\]

which is negligible.

---

# Key Scientific Separation

The experiments therefore support a distinction between:

## Angular orientation recovery

\[
\alpha_{2,\mathrm{obs}}
\rightarrow
\alpha_{2,\mathrm{learned}}
\]

and:

## Circular-strength recovery

\[
R_{2,\mathrm{obs}}
\rightarrow
R_{2,\mathrm{learned}}
\]

Good angular agreement does not necessarily imply accurate circular-strength magnitude.

Likewise, poor angular recovery is not always explained by weak observed circular organization.

---

# Supported Claims

The evidence supports the following statements:

1. Observed circular strength \(R_2\) is negatively associated with axial angular recovery error.

2. \(F_2\) peak magnitude is negatively associated with angular recovery error.

3. \(F_2\) peak radius is negatively associated with angular recovery error.

4. Reliable angular recovery cases exhibit stronger observed \(R_2\) than failure cases.

5. The reliable-versus-failure \(R_2\) separation persists across multiple reasonable threshold definitions.

6. Learned circular strength is not identical to observed circular strength.

7. Angular orientation recovery and circular-strength recovery exhibit empirically distinct behavior.

---

# Supported With Qualification

The following statements are supported as observational findings:

> Stronger observed circular organization is generally associated with more reliable axial orientation recovery.

and:

> Radial localization of the dominant \(F_2\) response is associated with angular recovery reliability.

These are associations.

They are **not causal claims**.

---

# Not Supported / Not Tested

The current evidence does not establish:

- semantic garment-part recognition;
- physical garment-part identity of the Fourier modes;
- human-like visual understanding;
- causal garment structure;
- causal mechanisms underlying recovery failure;
- direct correspondence between radial-angular modes and expert semantic judgments.

---

# Cell 30M — Manuscript-Level Evidence Matrix

## Population-Level Results

| Quantity | Result |
|---|---:|
| Population | 2300 |
| Median observed \(R_2\) | 0.4364 |
| Median learned \(R_2\) | 0.4032 |
| Median \(\Delta R_2\) | -0.0688 |
| Median axial error | 6.13° |
| Reliable ≤15° | 69.57% |
| Moderate 15–45° | 10.04% |
| Failure >45° | 20.39% |
| Median \(F_2\) peak radius | 21.50 |
| Median \(F_2\) peak magnitude | 0.03914 |

---

## Evidence Units

### E1 — Observed Circular Strength → Axial Error

\[
\rho=-0.4794
\]

\[
95\%\,CI=[-0.5103,-0.4476]
\]

Interpretation:

> Stronger observed circular organization is associated with lower angular recovery error.

---

### E2 — \(F_2\) Peak Magnitude → Axial Error

\[
\rho=-0.1784
\]

\[
95\%\,CI=[-0.2196,-0.1349]
\]

Interpretation:

> Stronger dominant second-harmonic response is associated with lower axial angular error.

---

### E3 — \(F_2\) Peak Radius → Axial Error

\[
\rho=-0.3646
\]

\[
95\%\,CI=[-0.3992,-0.3287]
\]

Interpretation:

> Radial localization of dominant \(F_2\) structure is associated with angular recovery reliability.

---

### E4 — Reliable vs Failure: Observed \(R_2\)

\[
\delta=+0.5390
\]

Interpretation:

> Reliable recovery cases exhibit substantially stronger observed circular organization than failure cases.

---

### E5 — Reliable vs Failure: \(F_2\) Magnitude

\[
\delta=+0.3855
\]

Interpretation:

> Reliable recovery cases tend to exhibit stronger dominant \(F_2\) responses.

---

### E6 — Reliable vs Failure: \(F_2\) Radius

\[
\delta=+0.4395
\]

Interpretation:

> Reliable recovery cases tend to exhibit more outward localization of dominant \(F_2\) organization.

---

# Cell 30N — Evidence → Literature Comparison

## Literature Position

The relevant prior literature establishes that:

- radial-angular shape representations already exist;
- Fourier shape descriptors already exist;
- polar Fourier descriptors already exist;
- doubled-angle treatment of axial orientation is established;
- garment classification is established;
- fashion-sketch recognition and retrieval are established.

Therefore CLO-SKET must **not** claim novelty for these mathematical foundations.

---

## High-Risk Novelty Claims

Do **not** claim:

> CLO-SKET invents radial-angular shape representation.

Do **not** claim:

> CLO-SKET invents Fourier shape descriptors.

Do **not** claim:

> CLO-SKET invents axial circular statistics.

Do **not** claim:

> CLO-SKET is the first computational analysis of garment sketches.

Do **not** claim:

> Category discrimination demonstrates semantic garment understanding.

---

## More Defensible Contribution Space

The stronger candidate contribution lies in:

1. the exact interpretable organization of:

\[
F_2
+
\alpha_2
+
R_2
\]

into a canonical radial-angular measurement system;

2. controlled category-discrimination evidence using a frozen geometric representation;

3. population-level analysis of radial-angular recovery;

4. characterization of recovery reliability;

5. identification of heterogeneous recovery/failure behavior.

---

# Cell 30O — Novelty Gap / Contribution Stress Test

## Established Components

The following are methodological foundations rather than novelty claims:

- radial-angular geometry;
- Fourier descriptors;
- \(F_2\) harmonic decomposition;
- axial doubled-angle encoding;
- circular statistics;
- logistic-regression classification;
- permutation testing;
- threshold sensitivity analysis.

---

## Method-Specific Candidate Contribution

Potentially distinctive, but not yet safe to call novel:

\[
F_2
+
\alpha_2
+
R_2
\]

as a joint canonical representation for garment-sketch geometry.

This requires exhaustive prior-art verification.

---

## Strongest Candidate Scientific Contribution

The strongest present contribution candidate is not:

> a new Fourier descriptor.

It is:

> **an interpretable framework for measuring how reliably radial-angular organization is recovered in garment sketches, together with empirical evidence that recovery reliability varies systematically with the strength and radial localization of the observed organization.**

Supporting evidence includes:

\[
N=2300
\]

\[
69.57\%
\text{ of sketches with axial error }\leq15^\circ
\]

\[
\rho(R_2,\Delta\alpha)
=
-0.4794
\]

\[
\rho(|F_2|,\Delta\alpha)
=
-0.1784
\]

\[
\rho(r_{F_2},\Delta\alpha)
=
-0.3646
\]

and:

\[
\delta_{\mathrm{reliable/failure},R_2}
=
+0.5390
\]

---

# Novelty Kill Conditions

The central novelty would be substantially weakened if prior work is found that already:

1. explicitly measures observed-versus-learned radial-angular recovery in garment sketches;

2. reports that circular-strength magnitude predicts angular recovery reliability in a closely equivalent representation;

3. uses essentially the same:

\[
F_2+\alpha_2+R_2
\]

canonical representation for garment sketches;

4. reports equivalent angular-versus-strength failure-regime decomposition.

By contrast, prior use of generic Fourier or polar descriptors alone does **not** invalidate the empirical recovery contribution.

---

# Cell 30P — Contribution Triangulation

## Contribution Chain

The frozen evidence forms the following hierarchy:

\[
\text{Representation}
\]

\[
\downarrow
\]

\[
\text{Controlled discrimination}
\]

\[
\downarrow
\]

\[
\text{Population recovery}
\]

\[
\downarrow
\]

\[
\text{Recovery reliability}
\]

\[
\downarrow
\]

\[
\text{Failure regimes}
\]

\[
\downarrow
\]

\[
\text{Scientific contribution}
\]

---

# 1. Representation

CLO-SKET constructs an interpretable radial-angular system containing:

- \(F_2\) radial descriptors;
- \(\alpha_2\) axial descriptors;
- observed circular descriptors;
- learned circular descriptors;
- radial-angular relational features.

Canonical descriptor count:

\[
28
\]

Role:

**Methodological foundation**

Novelty status:

**Potentially distinctive combination, not yet established as novel**

---

# 2. Controlled Category Discrimination

The \(F_2\)-radial baseline achieves:

\[
BA=0.2539
\]

The complete canonical representation achieves:

\[
BA=0.3304
\]

Therefore:

\[
\Delta BA
=
+0.0765
\]

Permutation test:

\[
p=0.000999
\]

Categories improved:

\[
22/23
\]

Mean category-wise:

\[
\Delta F1=+0.0881
\]

Median:

\[
\Delta F1=+0.0838
\]

Interpretation:

> The measured radial-angular feature families contain category-discriminative information beyond the \(F_2\)-radial baseline.

This is an empirical result.

It is not evidence of semantic garment-part recognition.

---

# 3. Population-Level Recovery

Across:

\[
2300
\]

sketches:

\[
\text{median axial error}=6.13^\circ
\]

and:

\[
69.57\%
\]

fall within:

\[
15^\circ
\]

axial error.

Interpretation:

> Radial-angular organization can be empirically recovered, but recovery reliability is non-uniform across sketches.

This constitutes central scientific evidence.

---

# 4. Recovery Reliability

Observed circular strength is associated with axial recovery error:

\[
\rho=-0.4794
\]

with:

\[
95\%\,CI=[-0.5103,-0.4476]
\]

Interpretation:

> Stronger observed circular organization is associated with lower angular recovery error.

This is currently one of the strongest candidate scientific findings.

---

# 5. Failure Regimes

Recovery failure is heterogeneous.

Two qualitatively different situations occur:

### Weak-signal failure

Observed circular organization is weak and angular recovery is poor.

### Strong-signal failure

Observed circular organization can remain strong while angular recovery fails severely.

Therefore weak signal alone cannot explain all recovery failures.

Likewise:

\[
\Delta R_2
\]

and angular error need not move together.

Interpretation:

> Orientation recovery and circular-strength recovery exhibit partially distinct behavior.

---

# 6. Robustness

The observed reliable-versus-failure \(R_2\) separation persists across threshold choices:

\[
\delta=0.4843\rightarrow0.6034
\]

Bootstrap confidence intervals for the major associations remain separated from zero.

Thus the main recovery-reliability result is not confined to a single threshold definition.

---

# Final Contribution Hierarchy

## Core Contribution

1. Empirical characterization of radial-angular organization and its recovery in garment sketches.

2. Demonstration that recovery reliability varies systematically with observed circular organization.

---

## Primary Supporting Contribution

The complete frozen radial-angular representation contains category-discriminative information beyond an \(F_2\)-radial baseline.

\[
BA:
0.2539
\rightarrow
0.3304
\]

\[
\Delta BA=+0.0765
\]

\[
p_{\mathrm{perm}}=0.000999
\]

---

## Secondary Scientific Findings

- Angular orientation recovery and circular-strength magnitude recovery are empirically distinct.

- Recovery failures are heterogeneous.

- Strong-signal angular failures exist.

- \(F_2\) peak magnitude is associated with angular recovery reliability.

- \(F_2\) peak radial position is associated with angular recovery reliability.

---

## Robustness Evidence

- Reliable/failure \(R_2\) separation survives multiple threshold definitions.

- Bootstrap confidence intervals remain separated from zero.

- All analyses retain the same locked radial domain.

- Exact \(F_2\)-to-circular-shell matching is maintained.

---

## Methodological Foundation

- radial-angular representation;
- Fourier decomposition;
- \(F_2\) magnitude;
- \(\alpha_2\) axial orientation;
- doubled-angle statistics;
- circular concentration \(R_2\).

These foundations are established methods and are **not claimed as novel**.

---

# Proposed Paper Story

CLO-SKET investigates whether garment sketches contain measurable radial-angular organization that can be captured using an interpretable geometric representation.

The representation is first tested under controlled category discrimination.

The \(F_2\)-radial baseline achieves:

\[
BA=0.2539
\]

whereas the complete canonical representation achieves:

\[
BA=0.3304
\]

corresponding to:

\[
\Delta BA=+0.0765
\]

with:

\[
p_{\mathrm{perm}}=0.000999
\]

and improvement across:

\[
22/23
\]

categories.

The analysis then moves beyond classification to ask whether the measured radial-angular organization itself can be recovered.

Across:

\[
2300
\]

sketches, median axial error is:

\[
6.13^\circ
\]

with:

\[
69.57\%
\]

of sketches falling within:

\[
15^\circ
\]

of the observed axial orientation.

Recovery reliability is non-uniform.

Observed circular strength is negatively associated with angular recovery error:

\[
\rho=-0.4794
\]

\[
95\%\,CI=[-0.5103,-0.4476]
\]

while \(F_2\) peak radius and magnitude exhibit weaker but reproducible associations.

The analysis further shows that angular orientation recovery and circular-strength magnitude recovery are not interchangeable.

Some sketches exhibit strong angular agreement despite attenuated \(R_2\), whereas others exhibit strong observed circular organization together with poor angular recovery.

Threshold sensitivity confirms that reliable-versus-failure separation remains directionally stable under multiple reasonable angular-error definitions.

Together, these results provide an empirical characterization of radial-angular organization in garment sketches and identify measurable conditions under which that organization is more or less reliably recovered.

The evidence does not establish semantic garment-part recognition, causal garment structure, or human-like visual understanding.

---

# Cell 30Q — Final Result Table / Manuscript Export

## Frozen Experimental Configuration

| Parameter | Value |
|---|---|
| Population | 2300 |
| Categories | 23 |
| Samples/category | 100 |
| Canonical descriptors | 28 |
| Classifier coordinates | 30 |
| CV folds | 5 |
| CV random state | 42 |
| Permutations | 1000 |
| Permutation seed | 20260817 |
| Classifier | StandardScaler + Multinomial Logistic Regression |
| Axial encoding | \(\cos(2\alpha),\sin(2\alpha)\) |
| Baseline | \(F_2\) radial |
| Primary representation | All canonical families |
| Category-based feature selection | None |
| Locked radial domain | 3.50 → 27.50 |
| Circular shells | 25 |

---

# Master Results

| ID | Analysis | Primary Result | Statistical Support |
|---|---|---|---|
| R1 | Category discrimination | \(BA:0.2539\rightarrow0.3304\), \(\Delta BA=+0.0765\) | permutation \(p=0.000999\) |
| R2 | Category-wide improvement | 22/23 categories improved | mean \(\Delta F1=+0.0881\) |
| R3 | Angular recovery | median error \(6.13^\circ\) | 69.57% ≤15° |
| R4 | Circular-strength recovery | \(R_2:0.4364\rightarrow0.4032\) | median \(\Delta R_2=-0.0688\) |
| R5 | \(R_2\) vs angular error | \(\rho=-0.4794\) | 95% CI [-0.5103,-0.4476] |
| R6 | \(F_2\) magnitude vs error | \(\rho=-0.1784\) | 95% CI [-0.2196,-0.1349] |
| R7 | \(F_2\) radius vs error | \(\rho=-0.3646\) | 95% CI [-0.3992,-0.3287] |
| R8 | Reliable vs failure | \(\delta=+0.5390\) for observed \(R_2\) | MW \(p=1.08\times10^{-70}\) |
| R9 | Threshold robustness | \(\delta=+0.4843\rightarrow+0.6034\) | direction stable across four definitions |

---

# Final Manuscript Claim Set

## CORE — Supported

> **CLO-SKET empirically characterizes radial-angular organization in garment sketches and its recovery reliability.**

---

## CORE — Supported

> **Observed circular organization is associated with angular recovery reliability.**

---

## PRIMARY SUPPORT — Supported

> **The complete radial-angular representation contains category-discriminative information beyond the \(F_2\)-radial baseline.**

---

## SECONDARY — Supported With Caution

> **Angular orientation recovery and circular-strength magnitude recovery exhibit partially distinct empirical behavior.**

---

## ROBUSTNESS — Supported

> **Reliable-versus-failure \(R_2\) separation persists across multiple reasonable angular-error threshold definitions.**

---

# Claims We Must Not Make

## Not Supported

> The Fourier/polar/axial mathematics underlying CLO-SKET is novel.

## Not Tested

> CLO-SKET performs semantic garment-part recognition.

## Not Supported

> The observed radial-angular associations are causal.

## Not Tested

> CLO-SKET demonstrates human-like garment understanding.

---

# Final Scientific Claim Boundary

The strongest defensible interpretation is:

> **CLO-SKET provides an interpretable framework for quantifying radial-angular organization in garment sketches, demonstrates that the resulting geometric feature families contain category-discriminative information, and shows that the learned radial-angular organization is recovered with non-uniform reliability that varies systematically with observed circular strength and radial localization.**

The evidence supports an empirical **representation-and-recovery** contribution.

It does not yet support a claim of semantic garment understanding.

---

# Frozen Analysis Status

- [x] Raw radial-angular geometry validated
- [x] Parseval accounting verified
- [x] \(F_2\) radial structure quantified
- [x] \(\alpha_2\) axial orientation quantified
- [x] Category association verified
- [x] Canonical feature representation frozen
- [x] Controlled discrimination completed
- [x] Permutation robustness completed
- [x] Feature-family ablation completed
- [x] Population recovery characterized
- [x] Recovery reliability characterized
- [x] Failure regimes analyzed
- [x] Statistical robustness completed
- [x] Threshold sensitivity completed
- [x] Literature overlap audited
- [x] Novelty stress test completed
- [x] Contribution hierarchy locked
- [x] Claim boundaries locked

---

# Analysis Phase

## 🟢 FROZEN

No additional descriptor construction should be introduced into the current result chain unless it is explicitly treated as a new experiment.

---

# Next Phase

1. Exhaustive literature verification
2. Reviewer-style novelty audit
3. Final figure selection
4. Results section drafting
5. Discussion drafting
6. Limitations section
7. Final manuscript claim audit

---

# CLO-SKET Scientific Chain

\[
\text{Raw garment sketch}
\]

\[
\downarrow
\]

\[
\text{Radial-angular measurement}
\]

\[
\downarrow
\]

\[
F_2(r)
+
\alpha_2(r)
+
R_2(r)
\]

\[
\downarrow
\]

\[
\text{Frozen interpretable representation}
\]

\[
\downarrow
\]

\[
\text{Category-discriminative information}
\]

\[
\downarrow
\]

\[
\text{Population-level recovery}
\]

\[
\downarrow
\]

\[
\text{Recovery reliability}
\]

\[
\downarrow
\]

\[
\text{Failure-regime characterization}
\]

\[
\downarrow
\]

\[
\boxed{
\text{Empirical characterization of radial-angular organization in garment sketches}
}
\]