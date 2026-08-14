# 4. Results

## 4.1 The Clo-Sket morphology representation exhibits concentrated spectral structure

The canonical morphology representation comprised 2,300 Clo-Sket garment sketches described by 135 quantitative morphology features: 64 horizontal occupancy measurements, 64 vertical occupancy measurements, and seven global morphology descriptors.

The standardized morphology spectrum showed substantial variance concentration. The numbers of principal components required to retain 80%, 85%, 90%, 95%, 97.5%, and 99% of the variance were 32, 41, 53, 73, 91, and 108, respectively. Thus, 73 principal components retained approximately 95% of the standardized morphology variance and were used as the principal-coordinate representation for subsequent geometry analyses.

The participation-ratio effective dimensionality was approximately 10.55, indicating substantial concentration of variance within the full 135-dimensional representation.

These quantities describe variance concentration rather than an exact manifold dimension. The 135-dimensional feature representation was therefore retained as the canonical feature space, while the 73-dimensional PCA representation was used as the operational geometry space.

---

## 4.2 Local morphology relationships show continuous neighborhood organization

Local-neighborhood analysis revealed a smooth progression of neighborhood scales in the morphology representation, with relative neighborhood growth decreasing as neighborhood size increased.

The median relative neighborhood growth decreased from 0.0434 at k = 1 to 0.0224 at k = 2, 0.0153 at k = 3, 0.0097 at k = 5, 0.0049 at k = 10, 0.0033 at k = 15, and 0.0027 at k = 19. The corresponding 95th-percentile relative gap decreased from 0.2202 at k = 1 to 0.0129 at k = 19.

Thus, as the neighborhood expanded, successive neighbors were incorporated with progressively smaller relative changes in distance.

A complementary directional-consistency statistic had a mean of 0.4501 and median of 0.4483. However, this statistic did not exceed the corresponding permutation null. Across 200 null realizations, the null mean was 0.4737 (SD = 0.00415), with all 200 null values equal to or greater than the observed statistic (empirical upper-tail p = 1.000).

Therefore, the local geometry provides evidence for smooth neighborhood growth but not for a preferred directional organization through morphology space.

---

## 4.3 The morphology geometry is globally connected

A 10-nearest-neighbor graph constructed from the frozen 73-dimensional morphology representation contained all 2,300 observations within a single connected component.

The graph contained 39,068 edges, and the reachable fraction was 1.000 for the mean, median, and minimum measures. Thus, every observation was reachable from every other observation through the local morphology graph.

Graph-geodesic distances were moderately larger than direct Euclidean distances. The median geodesic-to-Euclidean stretch was approximately 1.902, while the mean was approximately 1.911.

Despite this path stretch, Euclidean and graph-geodesic distances retained strong rank correspondence. The median Spearman correlation was approximately 0.903, with a mean of approximately 0.869.

These results indicate that the local morphology relationships form a connected and traversable geometry rather than a collection of disconnected morphology islands.

---

## 4.4 Recurring density organization emerges across observational scales

Multiscale density analysis identified recurring density-ascent organization within the connected morphology geometry.

Six observational scales were evaluated:

    4.707252
    5.416895
    6.248407
    7.596034
    10.640832
    16.568532

The corresponding density landscapes contained:

    7
    6
    5
    7
    7
    8

density basins, respectively.

Cross-scale basin agreement was substantial. Pairwise adjusted Rand indices ranged from approximately 0.498 to 0.926, with a mean of approximately 0.734.

Observation-level cross-scale consensus was also high. Approximately 1,917 of 2,300 observations (83.35%) had consensus ≥ 0.90, while the median consensus was approximately 0.927.

Agreement decreased as the separation between observational scales increased. Thus, density organization was recurrent across nearby observational scales while remaining scale-dependent.

These results indicate recurring density organization within the morphology geometry rather than a single fixed partition.

---

## 4.5 Density regions are not compact morphology clusters

The density-derived regions were next evaluated for global morphological compactness.

Across all six observational scales, within-region morphology distances were not smaller than between-region distances. The observed within/between distance ratios were:

    1.070
    1.057
    1.043
    1.046
    1.040
    1.075

Thus, the density-derived regions did not exhibit strong global compactness under the tested morphology-distance measure.

A complementary local-neighborhood analysis showed substantial same-region retention. Mean local-neighbor retention increased across the six scales from:

    0.755
    0.774
    0.804
    0.804
    0.843
    0.845

These results distinguish local regional coherence from global compactness. Density regions captured substantial local neighborhood structure while retaining considerable morphology variation internally.

The regions therefore should not be interpreted as conventional discrete morphology clusters. Instead, they represent recurring regions embedded within a broader continuous morphology geometry.

---

## 4.6 Density regions exhibit reproducible quantitative morphology profiles

Although the density-derived regions did not exhibit strong global compactness, they showed reproducible quantitative differences in morphology profiles.

Regional profiles were constructed from the canonical 135-dimensional morphology representation, including horizontal occupancy, vertical occupancy, centroid geometry, bounding-box geometry, aspect ratio, symmetry, and foreground fraction.

The strongest regional discriminators included:

    bbox_width
    aspect_ratio
    centroid_x
    symmetry
    foreground_fraction

together with multiple horizontal and vertical occupancy features.

However, regional profiles were not cleanly separated as compact feature-space clusters. Silhouette values were negative at all six observational scales, ranging from approximately -0.132 to -0.216.

Between/within profile-distance ratios ranged from approximately 0.550 to 0.568.

Thus, regional profiles substantially overlapped despite showing measurable quantitative differences.

The regional feature-block discrimination was:

    global descriptors      ≈ 0.518
    horizontal occupancy   ≈ 0.313
    vertical occupancy     ≈ 0.264

The reproducibility of regional profile structure across scales was high. Adjacent-scale profile correlations were:

    4.707252 → 5.416895       rho = 0.987665
    5.416895 → 6.248407       rho = 0.901663
    6.248407 → 7.596034       rho = 0.919744
    7.596034 → 10.640832      rho = 0.970510
    10.640832 → 16.568532     rho = 0.964808

These results indicate reproducible quantitative regional organization without evidence for cleanly separated discrete morphology profiles.

---

## 4.7 Regional morphology associations exceed a size-matched permutation null

A size-matched permutation analysis was used to determine whether the observed regional morphology associations could arise from arbitrary assignment of observations to regions having the same size distribution as the observed density regions.

At the three finest observational scales, observed regional feature discrimination exceeded the permutation null:

| Scale | Observed discrimination | Null mean | Empirical p | z |
|---:|---:|---:|---:|---:|
| 4.707252 | 0.309747 | 0.164513 | 0.004975 | 6.138 |
| 5.416895 | 0.310943 | 0.158761 | 0.009950 | 4.703 |
| 6.248407 | 0.303514 | 0.116115 | 0.004975 | 8.615 |

At scale 7.596034, the association was weaker and borderline (p = 0.054726). At the two coarsest scales, the observed associations were not clearly separated from the permutation null (p = 0.134328 and 0.169154).

Thus, at finer observational scales, the regional morphology associations were substantially greater than expected from arbitrary size-matched partitioning.

The result provides evidence for a non-random relationship between density-region organization and quantitative morphology properties, with the strength of the relationship depending on observational scale.

---

## 4.8 Regional morphology profiles generalize across observational scales

The persistence of quantitative regional morphology structure was evaluated across the six observational scales without assuming that individual basin identities persisted between scales.

Mean feature-profile correlations between observational scales ranged from approximately:

    rho = 0.9979 – 1.0000

Representative comparisons with the finest scale were:

    4.707252 → 5.416895       rho = 0.999893
    4.707252 → 6.248407       rho = 0.999812
    4.707252 → 7.596034       rho = 0.999867
    4.707252 → 10.640832      rho = 0.999668
    4.707252 → 16.568532      rho = 0.999331

Cross-scale consistency was maintained across all three canonical feature blocks:

    Global descriptors
        mean rho = 1.000000

    Horizontal occupancy
        mean rho = 1.000000

    Vertical occupancy
        mean rho = 0.999074
        minimum rho = 0.985611

Thus, quantitative regional morphology profiles remained highly reproducible when the observational scale used to construct the density landscape was changed.

This persistence concerns quantitative profile structure rather than the identity of individual density basins.

---

## 4.9 The morphology representation contains complementary feature structure

The contribution of the three canonical morphology feature blocks was evaluated by their ability to recover the local structure of the frozen reference morphology geometry.

The observed nearest-neighbor overlap values were:

| Feature representation | NN overlap |
|---|---:|
| Horizontal occupancy only | 0.297783 |
| Vertical occupancy only | 0.227261 |
| Global descriptors only | 0.115217 |
| Horizontal + vertical occupancy | 0.681870 |
| Horizontal + global descriptors | 0.422435 |
| Vertical + global descriptors | 0.326913 |
| All three blocks | 0.863217 |

Combining horizontal and vertical occupancy substantially increased recovery of the reference local geometry compared with either occupancy block alone.

Adding the seven global descriptors further increased nearest-neighbor overlap to 0.863217.

Thus, the observed morphology geometry is distributed across multiple quantitative feature families rather than being recoverable from a single feature block.

---

## 4.10 Whole-block perturbation confirms distributed feature influence

Independent removal of the three canonical feature blocks produced substantial changes in the recovered local morphology geometry.

The complete representation provided:

    NN overlap = 0.863217

Removing horizontal occupancy produced:

    NN overlap = 0.326913
    loss       = 0.536304

Removing vertical occupancy produced:

    NN overlap = 0.422435
    loss       = 0.440783

Removing global morphology descriptors produced:

    NN overlap = 0.681870
    loss       = 0.181348

Thus, all three feature families contributed measurable structure to the morphology geometry, with the two occupancy blocks exerting the largest whole-block influence.

In contrast, individual-feature removal produced substantially smaller changes in nearest-neighbor overlap.

These results indicate that the morphology geometry is not dominated by a small number of isolated measurements. Instead, structural information is distributed across multiple quantitative feature families.

---

## 4.11 Explicit occupancy-feature ordering does not measurably affect the tested geometry

A feature-order perturbation analysis tested whether explicit ordering of the occupancy measurements contributed independently to the observed nearest-neighbor geometry.

The reference nearest-neighbor overlap was:

    0.863217

After independently shuffling the horizontal occupancy order, vertical occupancy order, or both:

    Original:
        0.863217

    H order shuffled:
        0.863217

    V order shuffled:
        0.863217

    H + V order shuffled:
        0.863217

Repeated perturbations produced approximately zero variation in the overlap measure.

Thus, under the tested perturbation, explicit feature ordering did not measurably affect the nearest-neighbor geometry.

This result does not imply that spatial morphology is irrelevant. Rather, it indicates that the tested geometry was sensitive to occupancy values but not detectably sensitive to their explicit ordering within the present representation.

---

## 4.12 Local morphology transitions are smooth but not globally directed

Successive nearest-neighbor transitions were examined to characterize local morphology changes.

The median nearest-neighbor distance was:

    5.225

The median two-step transition distance was:

    5.708

yielding a two-step/one-step distance ratio of:

    median = 1.138
    mean   ≈ 1.14
    Q25    = 1.017
    Q75    = 1.229
    Q95    = 1.363

Local transition scale was also broadly stable, with:

    median scale ratio = 0.872
    mean scale ratio   = 0.869

These results indicate that successive local transitions generally remain close to the characteristic local morphology scale.

However, directional consistency was predominantly negative:

    mean   = -0.338
    median = -0.221
    Q05    = -1.000
    Q75    = -0.077
    Q95    =  0.148

Thus, the morphology geometry supports locally smooth transitions but does not exhibit evidence for a globally directed trajectory.

---

## 4.13 Multiple measurable morphology properties participate in continuous variation

Feature-level analyses identified multiple quantitative morphology properties associated with variation through the continuous morphology geometry.

The strongest local morphology gradients were observed for:

    aspect_ratio      = 0.109777
    centroid_x        = 0.106068
    bbox_width        = 0.103745
    bbox_height       = 0.102680
    centroid_y        = 0.095182

The strongest feature–morphology-distance associations included:

    foreground_fraction       rho = 0.694
    symmetry                  rho = 0.617
    vertical_occupancy_48     rho = 0.499
    vertical_occupancy_49     rho = 0.497
    vertical_occupancy_17     rho = 0.485
    vertical_occupancy_16     rho = 0.483
    horizontal_occupancy_50   rho = 0.483

Mean feature–distance association was distributed across:

    global descriptors      = 0.241
    horizontal occupancy   = 0.284
    vertical occupancy     = 0.296

The corresponding local-gradient means were:

    global descriptors      = 0.086427
    horizontal occupancy   = 0.053728
    vertical occupancy     = 0.051910

Thus, continuous morphology variation was associated with multiple measurable properties spanning global geometry and spatial occupancy measurements.

---

## 4.14 Perturbation confirms distributed morphology structure

The feature-gradient findings were supported by the perturbation analyses.

Whole-block removal substantially altered the local morphology geometry, whereas removal of individual measurements produced comparatively smaller changes.

The largest structural losses followed removal of horizontal and vertical occupancy blocks, while the seven global descriptors produced a smaller but still measurable reduction.

Together with the feature-block complementarity analysis, these results indicate that the observed morphology geometry is distributed across multiple quantitative feature families.

The perturbation result establishes structural influence within the present representation; it does not establish causal importance or semantic meaning.

---

## 4.15 Continuous morphology gradients overlap with regional morphology structure

The quantitative morphology properties associated with continuous variation in the morphology geometry overlapped with those distinguishing independently discovered density regions.

The overlapping properties included:

    global shape descriptors
    centroid measurements
    bounding-box measurements
    aspect ratio
    symmetry
    foreground fraction
    horizontal occupancy
    vertical occupancy

Thus, the continuous-gradient and regional-profile analyses implicated overlapping quantitative morphology properties rather than unrelated feature sets.

The evidence therefore links two levels of organization:

    continuous morphology variation
            ↓
    measurable morphology properties
            ↓
    recurring density organization
            ↓
    regional quantitative morphology profiles

This overlap indicates that the regional organization is related to the same quantitative morphology variation that structures the broader continuous geometry.

No semantic interpretation is assigned to the participating features.

---

## 4.16 Integrated morphology geometry

Taken together, the analyses provide convergent evidence that the 2,300 Clo-Sket garment sketches occupy a continuous and connected quantitative morphology geometry containing recurring density-organized regions.

The morphology representation exhibits concentrated spectral structure, smooth local neighborhood growth, connected graph organization, and relatively gradual local transitions. Within this geometry, independently derived density landscapes reveal recurring regions across observational scales.

These regions do not behave as conventional compact clusters: within-region distances are not substantially smaller than between-region distances. Nevertheless, they exhibit substantial local neighborhood retention, reproducible quantitative morphology profiles, and, at finer observational scales, regional feature associations exceeding a size-matched permutation null.

Feature-block complementarity and perturbation analyses further demonstrate that the observed geometry is distributed across multiple quantitative feature families. The quantitative properties associated with continuous morphology variation also overlap with those distinguishing the recurring density regions.

The resulting empirical characterization is therefore:

> **Clo-Sket garment sketches exhibit a continuous and connected quantitative morphology geometry containing recurring density-organized regions whose quantitative morphology profiles are reproducible across observational scales, while remaining embedded within rather than separable from the broader continuous morphology space.**

These findings do not establish discrete morphology categories, semantic morphology states, semantic morphology primitives, morphology grammar, causal morphology structure, or exact mathematical manifold dimensionality.

The final semantic relationship between measurable morphology properties and putative semantic primitives therefore remains an empirical question beyond the present geometry evidence.