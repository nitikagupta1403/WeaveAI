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

A 10-nearest-neighbor graph constructed from the frozen 73-dimensional
morphology representation contained all 2,300 observations within a
single connected component.

The symmetrized graph contained 19,534 undirected edges, and the
reachable fraction was 1.000 for the mean, median, and minimum
measures. Thus, every observation was reachable from every other
observation through the local morphology graph.

Graph-geodesic distances were moderately larger than direct
Euclidean distances. The median geodesic-to-Euclidean stretch was
approximately 1.902, while the mean was approximately 1.911.

Despite this path stretch, Euclidean and graph-geodesic distances
retained strong rank correspondence. Across 250 shortest-path
sources, the median Spearman correlation was approximately 0.903,
with a mean of approximately 0.869.

These results indicate that the local morphology relationships form
a connected and traversable quantitative geometry rather than a
collection of disconnected morphology islands.

The graph analysis does not establish a mathematical manifold,
low-dimensional manifold structure, semantic morphology states, or
directed morphology trajectories. It establishes only that the
observed local morphology relationships are globally connected and
graph-traversable under the tested k = 10 neighborhood graph.---



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
## 4.6 Density regions exhibit reproducible quantitative morphology profiles

Although the density-derived regions did not exhibit strong global
compactness, they showed measurable quantitative differences in
morphology profiles.

Regional profiles were constructed from the canonical 135-dimensional
morphology representation, including horizontal occupancy, vertical
occupancy, centroid geometry, bounding-box geometry, aspect ratio,
symmetry, and foreground fraction.

The strongest regional discriminators included:

    bbox_width
    aspect_ratio
    centroid_x
    symmetry
    foreground_fraction

together with multiple horizontal and vertical occupancy features.

However, regional profiles were not cleanly separated as compact
feature-space clusters. Silhouette values were negative at all six
observational scales, ranging from approximately -0.132 to -0.216.
Between/within profile-distance ratios ranged from approximately
0.550 to 0.568.

Thus, regional profiles substantially overlapped despite showing
measurable quantitative differences.

The regional feature-block discrimination was approximately:

    global descriptors      = 0.518
    horizontal occupancy   = 0.313
    vertical occupancy     = 0.264

These results indicate that the density-derived regions possess
measurable quantitative morphology differences without forming
compact, discretely separated morphology categories.

Importantly, the regional profiles are treated as quantitative
descriptions of density-defined regions. The discriminating
features are not interpreted as semantic morphology primitives, and
the regions are not interpreted as semantic morphology categories.

## 4.7 Regional morphology associations exceed a size-preserving permutation null

A size-preserving permutation analysis was used to determine whether
the observed association between density-region membership and
quantitative morphology could arise from arbitrary assignment of
observations to regions having the same size distribution as the
observed density regions.

For each density scale, the observed region sizes were preserved
exactly while observation-to-region membership was randomly
permuted. Two hundred permutations were generated at each scale.

The first null analysis evaluated same-region nearest-neighbor
retention in the frozen 73-dimensional morphology geometry.

Observed mean retention across the six observational scales was:

    4.707252     0.755000
    5.416895     0.774261
    6.248407     0.803522
    7.596034     0.803913
    10.640832    0.843348
    16.568532    0.844652

The corresponding permutation-null means ranged from approximately
0.534 to 0.720.

Observed retention exceeded the permutation null at every scale.
The empirical upper-tail probability was 0.004975 at each scale,
with observed-minus-null differences ranging from approximately
0.125 to 0.221.

Thus, morphology neighbours were retained within the same
density-defined region substantially more often than expected from
random assignment of observations to regions with identical region
sizes.

A second null analysis tested whether quantitative regional
morphology profiles were reproducible across observational scales
beyond arbitrary region assignment.

For each scale, regional feature discrimination was defined for each
of the 135 morphology features as:

    maximum regional feature mean
    -
    minimum regional feature mean.

This produced one 135-dimensional regional-discrimination profile
for each observational scale. Basin identities were not matched
across scales.

The observed Spearman correlations between the fifteen pairs of
regional-discrimination profiles ranged from:

    rho = 0.688894
    to
    rho = 0.980743.

The mean observed cross-scale correlation was:

    mean rho = 0.837103.

Under the independently permuted, size-preserving null:

    null mean rho = 0.106945
    null SD       = 0.048700
    null Q05      = 0.031239
    null Q95      = 0.182886

The observed mean exceeded the null mean by 0.730159, with:

    empirical p = 0.004975
    z = 14.992948.

All fifteen scale-pair comparisons exceeded their corresponding
permutation-null distributions.

Together, the two null analyses provide complementary evidence:

    local same-region retention
        +
    cross-scale regional-profile reproducibility

both exceed expectations under size-preserving randomized
region membership.

These results support a non-random association between density-defined
regional organization and quantitative morphology, as well as
reproducibility of regional morphology profiles across observational
scales.

The results do not establish semantic morphology categories,
semantic primitives, morphology states, or a morphology grammar.

## 4.8 Regional morphology profiles are reproducible across observational scales

The quantitative regional morphology structure was evaluated across
the six observational scales without assuming that individual basin
identities persisted between scales.

Rather than matching basin identifiers directly, each scale was
represented by a 135-dimensional regional feature-discrimination
profile. For each morphology feature, the profile value was defined
as the difference between the maximum and minimum regional feature
means at that scale.

The observed cross-scale Spearman correlations were:

    4.707252 → 5.416895       rho = 0.980743
    4.707252 → 6.248407       rho = 0.849220
    4.707252 → 7.596034       rho = 0.753053
    4.707252 → 10.640832      rho = 0.705677
    4.707252 → 16.568532      rho = 0.688894

    5.416895 → 6.248407       rho = 0.865038
    5.416895 → 7.596034       rho = 0.771559
    5.416895 → 10.640832      rho = 0.721647
    5.416895 → 16.568532      rho = 0.704585

    6.248407 → 7.596034       rho = 0.913023
    6.248407 → 10.640832      rho = 0.868745
    6.248407 → 16.568532      rho = 0.849571

    7.596034 → 10.640832      rho = 0.966023
    7.596034 → 16.568532      rho = 0.949810

    10.640832 → 16.568532     rho = 0.968964

The overall mean correlation was:

    mean rho = 0.837103.

The corresponding size-preserving permutation null had a mean
correlation of 0.106945.

Thus, the observed regional feature-discrimination profiles were
substantially more reproducible across observational scales than
expected when observation-to-region membership was independently
randomized while preserving region-size distributions.

The strength of profile correspondence was not identical across all
scale pairs. Correlations were generally highest between nearby or
later observational scales and lower for some comparisons involving
the finest and coarsest scales. This variation indicates that the
quantitative regional organization is reproducible but not invariant
to observational scale.

The appropriate interpretation is therefore:

    cross-scale quantitative reproducibility

rather than:

    scale-invariant morphology categories
    or
    persistent semantic states.

This result does not require, and does not establish, correspondence
between individual density basins across scales.


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

## 4.11 Ordered occupancy coordinates exhibit measurable spatial locality

Because the horizontal and vertical occupancy features encode
ordered spatial coordinates, their adjacency structure was examined
separately from the seven global morphology descriptors.

For horizontal occupancy, the observed adjacent-coordinate statistics
were:

    mean adjacent difference     = 0.271227
    median adjacent difference   = 0.078850
    Q90 adjacent difference      = 0.686674
    adjacent correlation         = 0.772648

For vertical occupancy:

    mean adjacent difference     = 0.308013
    median adjacent difference   = 0.085282
    Q90 adjacent difference      = 0.814516
    adjacent correlation         = 0.743219

A spatial-order permutation null was then constructed independently
for every observation. Occupancy values were retained exactly while
their coordinate order was randomly permuted.

Thus, the null preserved:

    • each observation's occupancy-value multiset
    • feature-value distributions
    • number of observations
    • number of spatial coordinates

while destroying:

    • the original spatial ordering
    • local coordinate adjacency.

Under the null, mean adjacent differences increased to:

    horizontal occupancy   = 0.725399
    vertical occupancy     = 0.700187

while adjacent correlations decreased to:

    horizontal occupancy   = 0.205014
    vertical occupancy     = 0.231671.

The observed reductions in adjacent difference relative to the null
were:

    horizontal occupancy   = 0.626100
    vertical occupancy     = 0.560099

and the corresponding gains in adjacent correlation were:

    horizontal occupancy   = 0.567633
    vertical occupancy     = 0.511548.

Both effects were significant under the 200-permutation null
(empirical p = 0.004975 for each block).

These results support reproducible local spatial structure in the
ordered occupancy profiles.

Importantly, this evidence concerns spatial locality of explicitly
ordered quantitative measurements. It does not establish that the
occupancy coordinates are semantic primitives, that their ordering
defines morphology categories, or that the ordering constitutes a
morphology grammar.

The separate nearest-neighbor geometry perturbation showed that
shuffling occupancy-feature order did not change the particular
nearest-neighbor overlap statistic. Therefore, spatial locality
should be interpreted as a property of the ordered occupancy
profiles rather than as evidence that coordinate order is required
for the global nearest-neighbor geometry used in the present study.

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

Taken together, the analyses provide convergent evidence that the
2,300 Clo-Sket garment sketches occupy a structured, connected
quantitative morphology geometry containing recurring
density-associated regions.

The morphology representation exhibits concentrated spectral
structure, smooth quantitative neighborhood growth, connected graph
organization, and relatively gradual local transitions. Within this
geometry, independently derived density landscapes reveal recurring
density organization across multiple observational scales.

These regions do not behave as conventional compact clusters:
within-region distances are not substantially smaller than
between-region distances. Nevertheless, they exhibit substantial
local same-region neighborhood retention, measurable quantitative
regional morphology differences, and cross-scale reproducibility
that exceeds a size-preserving permutation null.

Feature-block complementarity and perturbation analyses further
demonstrate that the observed geometry is distributed across
multiple quantitative feature families. Ordered occupancy profiles
also exhibit reproducible spatial locality, although coordinate
ordering did not measurably alter the tested nearest-neighbor overlap
statistic.

The resulting empirical characterization is therefore:

> **Clo-Sket garment sketches exhibit a structured and connected
> quantitative morphology geometry containing recurring
> density-associated regions whose quantitative morphology profiles
> are reproducible across observational scales, while remaining
> embedded within rather than cleanly separable from the broader
> morphology space.**

Here, "continuous morphology geometry" refers to the continuous-valued
quantitative representation and its observed local variation. It does
not imply a mathematical manifold, a globally directed trajectory,
or formally continuous semantic dimensions.

The findings do not establish discrete morphology categories,
semantic morphology states, semantic morphology primitives,
morphology grammar, causal morphology structure, or exact
mathematical manifold dimensionality.

The relationship between these measurable quantitative structures
and higher-level semantic organization therefore remains an
independent empirical question.

