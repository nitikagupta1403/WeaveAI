# 2. Related Work

## 2.1 From garment sketches to explicit geometry

Garment sketches already serve as computational representations in a wide range of fashion tasks. Sparse drawings have been mapped to garment meshes, sewing-pattern parameters, and simulation variables [2,3], while stylized fashion sketches have also been used to transfer garment shape and fold structure to virtual characters [4]. Sketch-conditioned systems now span clothing-image generation and synthesis [5–9], sewing-pattern reconstruction [10], and sketch-based retrieval and benchmarking [11,12]. Together, these studies show that a sketch contains information that can support sophisticated downstream inference.

Our interest begins one step earlier: **what geometric organization is present in the sketch itself?**

Explicit shape descriptions provide a natural language for this question. Fourier descriptors and geometric morphometrics have long represented periodic outlines, curves, and shape variation numerically [13–15], including applications to fashion-flat classification [16]. Related fashion work has also treated silhouette geometry as an object of explicit classification [17] and used geometric relationships for garment-pattern construction [18]. These approaches motivate representing shape through quantities whose geometric meaning remains visible rather than only through downstream prediction.

The axial–radial representation developed here follows this tradition but changes the object being summarized. Rather than applying a harmonic descriptor only to an external contour, we condition foreground sketch evidence on radial distance from the centroid and examine its angular organization within each shell. The resulting description therefore asks not only **what direction is present**, but also **where in the sketch that directional organization occurs**.

### 2.1.1 Relation to established polar and harmonic shape descriptors

Polar and harmonic shape representations substantially predate the present work. The MPEG-7 region-shape family includes the Angular Radial Transform (ART), which represents normalized region shape through complex orthogonal basis functions on a disk [22]. Generic Fourier Descriptor (GFD) maps a polar-rasterized shape image into radial and angular frequency components using a two-dimensional Fourier transform [23]. Shape contexts instead summarize the relative distribution of boundary points in log-polar bins for correspondence and matching [24]. Angular Radial Edge Histogram (AREH) descriptors pool edge density over angular and radial coordinates and use Fourier processing to handle rotation [25]. ART has also been generalized beyond its original formulation [26], and later phase-aware variants combine coefficient magnitude with aligned phase rather than discarding phase information [27].

The contribution here is therefore not the invention of polar coordinates, radial-angular shape representation, harmonic shape analysis, or a general Fourier descriptor class. The present construction differs in the specific quantity and inferential use that are frozen for CLO-SKET: the foreground angular distribution is normalized separately within each centroid-relative radial shell; the second circular harmonic is selected from the axial-symmetry condition \(\theta\equiv\theta+\pi\); selected axial orientations are represented using doubled-angle Cartesian coordinates; and the resulting shell field is compressed into a fixed 14-dimensional summary. The accompanying evaluation framework then treats recovered source garments as dependency units and separately tests incremental predictive utility and exact garment-level correspondence.

## 2.2 Axial organization as a circular-geometry problem

Directional structure in a garment sketch is naturally axial. An undirected orientation at angle \(\theta\) is equivalent to one at \(\theta+\pi\), so the geometry is periodic over \(180^\circ\) rather than \(360^\circ\). This doubled-angle treatment is standard for axial data in circular statistics [19]. The second circular harmonic is the lowest non-zero Fourier order that respects this equivalence.

Within a radial shell, its magnitude \(R_2(r)\) describes the strength of second-harmonic directional organization, while its half-phase \(\alpha_2(r)\) describes the corresponding undirected axis. Doubled-angle coordinates \((\cos 2\alpha,\sin 2\alpha)\) then provide a continuous Euclidean representation of axial orientation without treating opposite directions as distinct.

This explicit construction also makes the expected behavior of the representation inspectable. Under rigid image rotation, harmonic magnitude and axial phase have different transformation roles; localized radial summaries can depend on discretization; and phase becomes unstable when directional organization is weak. Rotation, reconstruction, discretization, harmonic-order, and phase-conditioning analyses therefore serve as geometric diagnostics of the representation itself. They answer a different question from classification performance: whether the measured quantities behave in ways consistent with their intended interpretation.

## 2.3 From predictive increment to garment-level correspondence

A second issue arises from the structure of the observations rather than from the descriptor. CLO-SKET contains repeated sketches associated with recovered source-garment identities. Different drawings of the same garment are related observations, so an image-level train/test split can place evidence from one garment on both sides of the validation boundary.

Grouped evaluation addresses this dependency by treating the complete garment identity as the indivisible unit of train/test separation. The same principle extends naturally to uncertainty estimation and repeated validation: if the scientific unit is the garment, resampling and repartitioning should operate at the garment level rather than at the individual image level.

There is also a subtler issue when two representations are combined. If axial–radial features improve prediction when appended to morphology, the result shows that the added representation carries useful information under the tested protocol. It does not yet tell us whether that information must come from the **exact same garment**.

We therefore distinguish predictive increment from garment-level correspondence. Complete axial–radial identity blocks can be reassigned within garment category while preserving category membership and repeated-observation structure. This retains category-conditioned information while deliberately breaking exact morphology–axial–radial pairing. The comparison asks whether correct garment-level alignment contributes information beyond what remains after this controlled misalignment.

Together, these strands motivate the evaluation framework used in the remainder of the paper: explicit axial–radial measurement, garment-identity-aware prediction, and a separate test of exact garment-level correspondence.
