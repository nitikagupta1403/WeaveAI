## 3.1 Study Design and Evidence Architecture

The study was designed to determine whether garment sketches
exhibit reproducible quantitative morphology organization that
can be characterized independently of semantic category labels.

The analysis followed a geometry-first evidence architecture.
Rather than defining morphology states or semantic components
a priori, the study first constructed a fixed quantitative
description of the sketch population and subsequently examined
the organization of that representation through complementary
geometric and statistical analyses.

The analysis proceeded through the following sequence:

    quantitative morphology representation
        ↓
    source-only dimensionality reduction
        ↓
    spectral characterization
        ↓
    local morphology geometry
        ↓
    graph and geodesic organization
        ↓
    multiscale density organization
        ↓
    regional morphology profiles
        ↓
    permutation-based null validation
        ↓
    cross-scale generalization

The same canonical morphology representation was retained
throughout this sequence. Discovery procedures did not use
semantic category labels, replication labels, target sketches,
or learned semantic representations. Subsequent validation
procedures were designed to test the robustness and
non-randomness of structures discovered from morphology alone.

This separation between discovery and validation was maintained
throughout the analysis. The purpose was to determine whether
observed organization could be attributed to quantitative
morphology itself rather than to externally imposed semantic
structure.

The study therefore treats the analyses as complementary
diagnostics of a common morphology representation rather than
as statistically independent experiments. The resulting
evidence is interpreted through convergence across spectral,
local-geometric, graph, density, regional-profile, permutation,
and cross-scale analyses.

## 3.2 Dataset and Canonical Morphology Representation

The analysis was conducted on 2,300 garment sketches from the
Clo-Sket source collection. Each sketch was converted into a
fixed quantitative morphology representation derived solely
from image geometry. No semantic category labels, replication
labels, target sketches, or downstream morphology-state
assignments were used during feature construction.

Each input image was converted to grayscale and represented using
floating-point pixel intensities normalized to the interval
[0,1]. A deterministic foreground estimate was then obtained by
classifying pixels with normalized intensity below 0.8 as
foreground. This threshold was fixed across the complete source
collection and was not estimated from individual sketches or
from the dataset.

The resulting foreground representation was resized to 64 × 64
pixels. Because image resampling may introduce intermediate
intensity values, the resized representation was treated as a
normalized morphology array rather than assumed to remain
strictly binary after resizing.

Two spatial occupancy profiles were subsequently extracted.
Horizontal occupancy was calculated by averaging the morphology
array across columns, producing 64 row-wise measurements.
Vertical occupancy was calculated by averaging across rows,
producing 64 column-wise measurements. Together, these profiles
capture the distribution of foreground morphology along the two
image axes.

Seven global morphology descriptors were appended to the
occupancy representation:

    centroid_x
    centroid_y
    bounding-box width
    bounding-box height
    aspect ratio
    left-right symmetry
    foreground fraction

The centroid was calculated using foreground-weighted image
coordinates and normalized by image size. Bounding-box width
and height were calculated from the spatial extent of the
foreground representation. Aspect ratio was defined as
bounding-box width divided by bounding-box height. Left-right
symmetry was quantified by comparing the morphology array with
its horizontal reflection. Foreground fraction was defined as
the mean value of the resized morphology array.

The resulting feature vector for each sketch therefore contained:

    64 horizontal occupancy features
    +
    64 vertical occupancy features
    +
    7 global morphology descriptors
    =
    135 quantitative features.

The canonical morphology matrix was consequently:

    X_source ∈ R^(2300 × 135)

with rows corresponding to individual sketches and columns
corresponding to fixed quantitative morphology measurements.

The feature ordering was frozen as follows:

    1–64:
        horizontal occupancy

    65–128:
        vertical occupancy

    129–135:
        global morphology descriptors

This ordering and feature definition were retained unchanged
throughout all downstream analyses. The canonical 135-dimensional
representation therefore served as the source feature space for
feature-level analyses, while a separate PCA-derived coordinate
space was subsequently constructed for geometric analyses.

The representation was checked for the expected dimensionality
and finite numerical values before downstream processing.
Failure of either condition was treated as a morphology
construction error.

Importantly, the canonical representation is a quantitative
description of image morphology and is not itself a semantic
representation. Individual measurements, including occupancy
profiles, centroid coordinates, aspect ratio, symmetry, and
foreground fraction, were therefore interpreted only as
morphological quantities unless independently validated in a
subsequent analysis.

## 3.3 Source Standardization and PCA-Derived Morphology Geometry

The canonical 135-dimensional morphology representation was
standardized using a StandardScaler fitted exclusively on the
Clo-Sket source morphology matrix. Let

    X_source ∈ R^(2300 × 135)

denote the canonical morphology matrix defined in Section 3.2.
The fitted source scaler was retained as a frozen transformation:

    X_scaled = source_scaler.transform(X_source)

No target or external dataset was included during estimation of
the centering and scaling parameters. Consequently, the source
morphology representation defines the reference coordinate system
for all subsequent geometry analyses.

Principal component analysis (PCA) was then fitted to the
standardized source morphology representation. PCA was configured
with a variance-retention criterion of 0.95 and full singular-value
decomposition. The resulting transformation retained 73 principal
components, giving:

    Z_source ∈ R^(2300 × 73)

The retained representation explains approximately 95% of the
variance in the standardized morphology representation. The
corresponding variance-retention dimensions were:

    80%   → 32 components
    85%   → 41 components
    90%   → 53 components
    95%   → 73 components
    97.5% → 91 components
    99%   → 108 components

The 73-dimensional representation was used as the operational
PCA-derived morphology geometry space for subsequent analyses of
local neighborhoods, morphology continuity, graph structure,
geodesic relationships, density organization, and cross-scale
regional organization.

The term "intrinsic morphology space" is used operationally to
refer to this PCA-derived analysis space. It does not imply that
73 is the exact dimensionality of an underlying mathematical
manifold. PCA retention dimensionality and intrinsic manifold
dimensionality were therefore treated as distinct quantities.

The source scaler and PCA transformation were frozen after fitting.
All subsequent geometry analyses used these transformations without
refitting them on target or external data. This prevented
target-specific centering, scaling, or dimensionality reduction
from altering the source morphology coordinate system.

The distinction between the canonical feature space and the
PCA-derived geometry space was maintained throughout the study:

    Canonical feature space:
        X_source ∈ R^(2300 × 135)

    PCA-derived geometry space:
        Z_source ∈ R^(2300 × 73)

The canonical 135-dimensional space was retained for feature-level
analyses, including feature contribution, perturbation,
feature-block, regional-profile, and permutation analyses.
The 73-dimensional PCA-derived space was used for analyses in
which distances and geometric relationships among observations
were required.

The resulting source transformation therefore defined a fixed
analysis pipeline:

    135-D canonical morphology
        ↓
    source-only standardization
        ↓
    73-D PCA-derived morphology geometry

The stored source representation was checked for reproducibility
by applying the frozen scaler and PCA transformation to the
canonical morphology matrix and verifying agreement with the
stored 73-dimensional representation within numerical tolerance.

No category labels, replication labels, target sketches,
morphology-state assignments, KMeans assignments, or other
semantic information were used in fitting either the source
standardization or PCA transformation.

## 3.4 Spectral Characterization and Effective Spectral Dimensionality

The spectral structure of the standardized 135-dimensional
morphology representation was characterized before subsequent
geometric analyses. The purpose of this analysis was to quantify
the concentration of morphology variance across principal
directions and to distinguish variance-retention dimensionality
from effective spectral complexity.

Let the ordered PCA eigenvalues be:

    λ₁ ≥ λ₂ ≥ ... ≥ λ₁₃₅ ≥ 0

and let the normalized variance contribution of component k be:

    p_k = λ_k / Σ_j λ_j.

The cumulative variance through component k was calculated as:

    C_k = Σ_{j=1}^{k} p_j.

For a variance threshold τ, the corresponding
variance-retention dimensionality was defined as the smallest
number of components satisfying:

    D_τ = min{k : C_k ≥ τ}.

The complete 135-component spectrum was characterized rather
than restricting the analysis to the 73 components retained by
the operational PCA representation. This allowed variance
retention to be evaluated beyond the 95% threshold.

The observed variance-retention dimensions were:

    80%   → 32 components
    85%   → 41 components
    90%   → 53 components
    95%   → 73 components
    97.5% → 91 components
    99%   → 108 components

Thus, the operational 73-dimensional representation corresponds
to the 95% variance-retention criterion used in the PCA geometry
pipeline.

The eigenvalue spectrum was additionally summarized using the
participation ratio, defined as:

    D_eff =
        (Σ_i λ_i)^2 /
        Σ_i λ_i^2

or equivalently:

    D_eff = 1 / Σ_i p_i^2.

The participation ratio quantifies the effective number of
principal directions contributing to the observed spectral
variance. For the Clo-Sket morphology representation, the
observed effective spectral dimensionality was approximately:

    D_eff ≈ 10.55.

This quantity was interpreted as an effective spectral complexity
measure rather than as an estimate of exact intrinsic manifold
dimensionality. In particular, the following quantities were
treated as conceptually distinct:

    canonical feature dimensionality = 135

    95%-variance PCA dimensionality = 73

    participation-ratio effective dimensionality ≈ 10.55

No equivalence was assumed among these quantities.

The leading principal component accounted for approximately
28.25% of the total standardized morphology variance. This value
was treated descriptively as a property of the morphology
representation and was not assigned a semantic interpretation.

Spectral characterization was performed independently of semantic
or categorical information. No category labels, replication
labels, target sketches, morphology-state assignments, KMeans
assignments, or supervised learning targets were used in the
calculation of the morphology spectrum.

The resulting spectrum therefore serves two purposes in the
study. First, it characterizes how the measured morphology
variance is distributed across principal directions. Second, it
provides the dimensionality basis for the operational 73-dimensional
PCA-derived geometry space used in subsequent local, graph,
geodesic, and density analyses.

Spectral characterization was treated as descriptive evidence
about the morphology representation. It does not by itself
establish an exact manifold dimension, discrete morphology
states, semantic primitives, or a morphology grammar.

## 3.5 Local Morphology Geometry and Continuity

The PCA-derived 73-dimensional morphology space was used to
characterize the local geometry of the Clo-Sket sketch population.
The purpose of this analysis was to determine whether nearby
observations exhibit progressively related quantitative morphology
rather than behaving as an unstructured collection of points.

For each sketch, neighboring observations were identified using
distances in the frozen 73-dimensional morphology geometry space.
The neighborhood structure was evaluated across increasing
neighborhood sizes rather than at a single arbitrarily selected
neighborhood scale.

Local morphology continuity was assessed by examining how
morphology distance changes as progressively larger neighborhoods
are traversed. If the morphology representation contains
continuous local organization, observations close to one another
should exhibit smaller morphology differences, with distances
increasing as increasingly distant neighborhoods are considered.

The analysis therefore evaluates the relationship between:

    neighborhood scale
        and
    morphology distance.

The resulting distance progression provides a quantitative
description of local morphology continuity without requiring
observations to be assigned to discrete morphology states.

Importantly, continuity was evaluated in the frozen PCA-derived
geometry space established in Sections 3.3–3.4. No transformation
was refitted during local-neighborhood analysis, and no semantic
labels or category assignments were used to define neighborhood
membership.

The analysis was subsequently extended from local neighborhoods
to a nearest-neighbor graph. Each observation was represented as a
node, with edges connecting observations according to their local
morphology neighborhood. This graph provides a discrete
representation of the continuous local relationships identified
in the morphology space.

The local-neighborhood analysis and the graph analysis therefore
serve complementary purposes:

    local distance structure
        →
    evaluates quantitative continuity

    nearest-neighbor graph
        →
    represents the connectivity of those local relationships

The continuity analysis does not require the existence of
discrete morphology categories. In particular, gradual variation
between observations is compatible with the observed organization
and is not treated as evidence against structure.

The analysis was also deliberately separated from subsequent
density-region discovery. Local neighborhoods were characterized
from the morphology geometry itself before density-ascent regions
were used to describe recurring density organization.

Accordingly, a positive continuity result is interpreted as
evidence that the quantitative morphology representation possesses
locally organized variation. It does not establish morphology
categories, semantic primitives, or a morphology grammar.

The local-geometry analysis therefore addresses the following
specific question:

> **Do nearby garment sketches occupy locally related positions
> in quantitative morphology space, with morphology differences
> increasing systematically as neighborhood distance increases?**

This provides the geometric foundation for the subsequent graph,
geodesic, and density analyses.

## 3.6 Graph Connectivity and Geodesic Morphology Organization

To extend the local-neighborhood analysis into a global
representation of morphology organization, a nearest-neighbor
graph was constructed from the frozen 73-dimensional
PCA-derived morphology space.

Each sketch was represented as a graph node. Edges connected
observations according to their local morphology neighborhoods,
with edge weights defined by the corresponding morphology
distances in the PCA-derived coordinate space.

The resulting graph provides a discrete representation of the
local geometric relationships identified in Section 3.5 while
retaining the quantitative distances between neighboring
observations.

### Graph Connectivity

Graph connectivity was evaluated to determine whether the
local morphology relationships form a connected organization
rather than a collection of disconnected components.

The analysis distinguishes between:

    local neighborhood relationships
        and
    global graph connectivity.

A connected graph indicates that observations can be linked
through sequences of local morphology relationships, even when
direct pairwise distances between distant observations are
large.

This distinction is important for a morphology space in which
variation may be continuous rather than organized into
well-separated compact groups.

### Geodesic Morphology Distance

For observations that are not direct graph neighbors, morphology
relationships were additionally characterized using shortest-path
distances through the nearest-neighbor graph.

For observations i and j, the graph geodesic distance was defined
as the shortest weighted path:

    d_geo(i,j)
        =
    min over paths P(i,j)
        Σ_{e ∈ P} w_e

where w_e denotes the morphology distance associated with graph
edge e.

Geodesic distance therefore measures morphology separation along
the observed local connectivity structure rather than through a
single direct Euclidean displacement in the 73-dimensional PCA
space.

This distinction allows the analysis to test whether local
morphology relationships provide a coherent route through the
broader morphology representation.

### Morphology Organization Along Graph Paths

The graph was used to examine whether observations separated by
larger geodesic distances exhibit progressively different
quantitative morphology.

The analysis therefore considers two related quantities:

    direct morphology distance
        and
    graph geodesic distance.

Direct distance characterizes displacement in the PCA coordinate
space, whereas geodesic distance characterizes separation along
the locally connected morphology structure.

If the morphology representation contains organized continuous
variation, local relationships should combine to form traversable
paths through morphology space rather than terminating primarily
in disconnected components.

### Relationship to Local Continuity

The graph analysis extends the local continuity analysis rather
than replacing it.

The evidence chain is:

    local neighborhoods
        ↓
    nearest-neighbor graph
        ↓
    graph connectivity
        ↓
    geodesic morphology distances
        ↓
    global organization through local relationships

Local continuity therefore provides the local geometric basis,
while graph connectivity and geodesic analysis examine whether
those local relationships remain globally organized.

### Independence from Semantic Structure

Graph construction uses only the frozen 73-dimensional
quantitative morphology representation.

No category labels, replication labels, target sketches,
semantic annotations, KMeans assignments, or supervised
predictions are used to define graph edges or geodesic paths.

Consequently, graph connectivity represents relationships
arising from quantitative morphology rather than externally
defined semantic neighborhoods.

### Interpretation Boundary

A connected morphology graph does not imply that the sketch
population contains discrete morphology categories. Conversely,
the existence of long geodesic paths does not imply that those
paths correspond to semantic transitions.

The graph analysis is therefore interpreted as evidence about
the organization and traversability of quantitative morphology
space.

Specifically, it addresses the question:

> **Do local quantitative morphology relationships form a
> connected structure through which broader morphology
> differences can be traversed by sequences of neighboring
> observations?**

A positive result supports connected quantitative morphology
organization. It does not establish semantic morphology states,
semantic primitives, or morphology grammar.

## 3.7 Multiscale Density Landscape and Basin Construction

The connected 73-dimensional morphology geometry was examined for
recurring regions of elevated observational density. Density
organization was analyzed independently at multiple observational
scales rather than by selecting a single smoothing parameter or
specifying a predefined number of morphology regions.

The analysis was performed on the frozen PCA-derived morphology
representation:

    Z_source ∈ R^(2300 × 73)

No transformation was refitted during density analysis.

### Empirical Density Scales

A local distance scale was first obtained from the fifth-nearest
neighbor of each observation in the 73-dimensional morphology
space. The empirical distribution of these fifth-nearest-neighbor
distances was then used to define a six-level observational scale
ladder.

The selected scales corresponded to the:

    25th percentile
    40th percentile
    55th percentile
    70th percentile
    85th percentile
    95th percentile

of the empirical fifth-nearest-neighbor distance distribution.

The resulting scales were:

    h₁ = 4.707252
    h₂ = 5.416895
    h₃ = 6.248407
    h₄ = 7.596034
    h₅ = 10.640832
    h₆ = 16.568532

Thus, the density analysis used observational scales derived from
the empirical morphology geometry rather than scales chosen to
produce a desired number of regions.

### Kernel Density Estimation

At each scale h, a Gaussian kernel density estimate was constructed
over the frozen 73-dimensional morphology space. Conceptually, the
density at a location x was estimated as:

    ρ_h(x)
        =
    (1/N) Σ_i K_h(x - x_i)

where K_h denotes the Gaussian kernel associated with the
observational scale h and N = 2300.

A separate density landscape was therefore obtained at each of
the six scales.

### Density Maxima and Basin Construction

Local maxima of each density landscape were identified as
candidate high-density locations. Each observation was then
associated with a terminal density maximum by following local
density ascent through neighboring observations.

The resulting procedure can be represented as:

    observation
        ↓
    local density comparison
        ↓
    movement toward higher density
        ↓
    terminal density maximum
        ↓
    density-ascent basin

Observations terminating at the same density maximum were
assigned to the same basin.

The number of basins was therefore determined by the density
landscape at each observational scale and was not specified
a priori.

The six scales produced the following observed basin counts:

    h₁ = 4.707252     → 7 basins
    h₂ = 5.416895     → 6 basins
    h₃ = 6.248407     → 5 basins
    h₄ = 7.596034     → 7 basins
    h₅ = 10.640832    → 7 basins
    h₆ = 16.568532    → 8 basins

Variation in basin number across scales was retained as part of
the observed morphology organization rather than treated as a
reason to select one preferred scale.

### Cross-Scale Recurrence

Because density organization may depend on observational scale,
basin assignments obtained independently at the six scales were
compared to quantify recurrence.

Pairwise agreement between basin organizations was evaluated
using the adjusted Rand index (ARI). Observation-level
cross-scale consensus and pairwise co-membership were also
examined.

The observed mean pairwise ARI was approximately:

    0.734

with:

    minimum ARI ≈ 0.498
    maximum ARI ≈ 0.926

The mean observation-level cross-scale consensus was approximately:

    0.874

and approximately:

    1917 / 2300 = 83.35%

of observations exhibited consensus of at least 0.90.

These quantities were used to characterize the degree to which
density organization recurred across independently constructed
observational scales.

### Basin Identity Across Scales

Basin identifiers were treated as scale-specific labels.

Thus, a basin assigned a particular numerical identifier at one
scale was not assumed to represent the same region at another
scale. Cross-scale correspondence was evaluated from quantitative
agreement rather than from equality of basin labels.

This distinction prevents numerical basin identifiers from being
interpreted as persistent morphology-state identities.

### Relationship to Subsequent Analyses

The density analysis establishes the candidate regional structure
used by subsequent regional validation analyses.

The evidence sequence is therefore:

    frozen morphology geometry
        ↓
    empirical observational scales
        ↓
    density landscapes
        ↓
    density maxima
        ↓
    density-ascent basins
        ↓
    cross-scale recurrence
        ↓
    regional morphology validation

Subsequent analyses evaluate whether these independently discovered
regions exhibit measurable morphology coherence, quantitative
feature-profile differences, stronger-than-null regional
associations, and cross-scale profile reproducibility.

### Independence from Semantic Structure

Density discovery was performed using the quantitative morphology
geometry alone. No category labels, replication labels, target
sketches, semantic annotations, KMeans assignments, or supervised
predictions were used to construct the density landscapes or
basin assignments.

The resulting basins are therefore treated as geometry-derived
density regions rather than predefined morphology categories.

### Interpretation Boundary

The density analysis establishes recurring organization in the
quantitative morphology space; it does not establish the semantic
meaning of that organization.

In particular:

    density basin
        ≠
    morphology category

and:

    recurring density region
        ≠
    semantic morphology state

The density results are therefore interpreted as evidence for
recurring quantitative organization within the morphology
geometry, with semantic interpretation deliberately deferred.


## 3.8 Regional Morphology Coherence and Feature-Profile Characterization

The density-ascent basins identified independently at each
observational scale were subsequently characterized using both
the PCA-derived morphology geometry and the original canonical
135-dimensional morphology representation.

The purpose of this analysis was twofold. First, we evaluated
whether observations assigned to the same density region exhibit
local quantitative morphology coherence. Second, we characterized
whether independently discovered density regions possess
reproducible differences in their measurable morphology profiles.

### 3.8.1 Within- and Between-Region Morphology Distances

For each density basin, pairwise morphology distances were
calculated in the frozen 73-dimensional PCA-derived geometry
space. Within-region distances quantified the morphological
separation among observations assigned to the same density
region, while between-region distances quantified separation
between observations assigned to different regions.

For each observational scale, the ratio

    R_WB =
        mean within-region distance /
        mean between-region distance

was calculated as a descriptive measure of regional geometric
separation.

Values below one indicate smaller within-region than
between-region distances, whereas values near one indicate
limited contrast between the two distance distributions.

The observed ratios ranged from approximately 1.04 to 1.07
across the six scales. Thus, the density regions did not exhibit
strong global compactness under this distance summary.

This result was retained as negative evidence rather than
interpreted as evidence for discrete morphology clusters.

### 3.8.2 Local Same-Region Neighbor Retention

Because global pairwise distances may obscure local organization,
a complementary neighborhood measure was calculated.

For each observation, the proportion of local morphology neighbors
belonging to the same density basin was determined. This provided
a measure of local same-region neighbor retention.

Mean retention across the six observational scales ranged
approximately from:

    0.755 to 0.845.

The increase in local retention with observational scale indicates
that a substantial proportion of local morphology neighborhoods
remain within the same density-derived region.

This result provides evidence for local regional coherence while
remaining compatible with substantial overlap between regions in
the broader morphology space.

### 3.8.3 Canonical Morphology Feature Profiles

Regional feature profiles were then characterized in the frozen
135-dimensional canonical morphology space rather than in the
73-dimensional PCA coordinate space.

For each density basin b, the subset

    X_b ⊂ X_source

was used to characterize the distributions of the canonical
morphology features.

The resulting regional profile included the complete set of:

    64 horizontal occupancy measurements
    64 vertical occupancy measurements
    7 global morphology descriptors.

Thus, regional characterization remained interpretable in terms
of the original morphology measurements rather than PCA
components.

### 3.8.4 Regional Profile Distances

Regional morphology profiles were compared quantitatively to
characterize differences among independently discovered density
regions.

A silhouette-based statistic was used as a descriptive measure
of profile separation. Positive values indicate stronger
separation under the tested profile-distance representation,
whereas values near zero or below zero indicate substantial
profile overlap or weak correspondence between the regional
profile structure and compact partitioning.

The observed silhouette values were negative at all six
observational scales:

    -0.1916
    -0.1837
    -0.1317
    -0.1873
    -0.2046
    -0.2162

These values do not support an interpretation of the density
regions as cleanly separated compact morphology-profile clusters.

The negative silhouette result is therefore retained as an
important constraint on interpretation.

### 3.8.5 Feature-Level Regional Discrimination

Although regional profiles were not cleanly separated as compact
clusters, individual canonical morphology measurements exhibited
measurable differences among density regions.

Feature-level discrimination was therefore evaluated across the
135 canonical morphology features.

Among the strongest regional discriminators were global
morphology descriptors including:

    bounding-box width
    aspect ratio
    centroid_x
    symmetry
    foreground fraction

along with multiple horizontal and vertical occupancy features.

These measurements were treated as quantitative morphology
properties associated with regional organization. They were not
assigned semantic meanings.

### 3.8.6 Feature-Block Contribution

Feature-level regional discrimination was additionally summarized
by the three predefined morphology blocks:

    global descriptors
    horizontal occupancy
    vertical occupancy.

The observed mean discrimination values were approximately:

    global descriptors       0.518
    horizontal occupancy     0.313
    vertical occupancy       0.264

with corresponding median values of approximately:

    global descriptors       0.442
    horizontal occupancy     0.340
    vertical occupancy       0.291.

These results indicate that the global descriptor block contributes
strongly to measurable differences among density-region profiles,
while both occupancy blocks also contribute to the observed
regional morphology organization.

The analysis does not interpret block contribution as evidence
that any block represents a semantic morphology concept.

### 3.8.7 Regional Heterogeneity

Regional characterization was retained at the basin level rather
than reduced entirely to a global summary.

Density regions varied in population size, and therefore their
profile estimates need not have equal statistical stability.
Small regions were consequently interpreted with greater caution
than large regions.

The analysis therefore treats regional morphology organization
as potentially heterogeneous rather than assuming that every
density region exhibits the same degree of coherence or the same
feature composition.

### 3.8.8 Interpretation

The combined regional analysis supports a specific and limited
description of the observed organization.

Density-derived regions exhibit substantial local same-region
neighbor retention and measurable differences in quantitative
morphology profiles. However, the within/between distance ratios
and negative silhouette values do not support describing these
regions as strongly separated compact clusters.

The appropriate interpretation is therefore:

    recurring density regions
        +
    local quantitative coherence
        +
    reproducible morphology-profile differences

rather than:

    discrete morphology categories.

This distinction is central to the study. The regional analyses
characterize quantitative morphology organization without
assigning semantic meanings to regions or individual features.

## 3.9 Permutation-Based Null Validation

The quantitative regional morphology differences identified in
Section 3.8 were evaluated against a size-preserving permutation
null model. The purpose of this analysis was to determine whether
the observed association between density-region membership and
local morphology organization exceeded that expected from arbitrary
assignment of observations to regions having the same size
distribution.

The analysis used the frozen canonical morphology representation:

    X_source ∈ R^(2300 × 135)

and the density-basin assignments obtained independently from the
multiscale density analysis. Neither the morphology representation
nor the observed basin assignments were modified during null
construction.

### 3.9.1 Size-Preserving Null Design

For each observational scale, the observed basin-size distribution
was preserved exactly. Observation-to-basin membership was then
randomly permuted while maintaining the number of observations
assigned to every basin.

Region identity was represented using the actual unique basin
identifiers. Region counts and region sizes were therefore computed
using unique identifiers and their observed frequencies rather than
assuming that basin identifiers were contiguous integers.

The resulting null preserved:

    • total number of observations
    • number of density regions
    • size of every region
    • complete region-size distribution
    • frozen morphology geometry
    • global feature-value distributions

while destroying:

    • the observed association between morphology
      and density-region membership.

This construction therefore tests whether the observed relationship
between local morphology geometry and density-region membership can
be explained by region-size structure alone.

### 3.9.2 Same-Region Neighbour Retention

The primary statistic in Audit 01 was same-region nearest-neighbour
retention.

For each observation, the ten nearest neighbours were identified
in the frozen 73-dimensional PCA-derived morphology geometry space.
The retention statistic was defined as the fraction of these
neighbours belonging to the same density-defined region as the
observation.

For each density scale, the observed retention was compared with
200 independently generated size-preserving permutation
assignments.

The observed mean same-region retention was:

    scale = 4.707252
        0.755000

    scale = 5.416895
        0.774261

    scale = 6.248407
        0.803522

    scale = 7.596034
        0.803913

    scale = 10.640832
        0.843348

    scale = 16.568532
        0.844652

The corresponding permutation-null means ranged from approximately
0.534 to 0.720.

Across all six scales, observed retention exceeded the
size-preserving null. The empirical upper-tail probability for each
scale was 0.004975, corresponding to the smallest resolvable
upper-tail probability with 200 permutations under the
plus-one empirical-p convention.

The observed-minus-null differences ranged from approximately
0.125 to 0.221, while the observed retention was approximately
1.17–1.41 times the corresponding null mean.

These results indicate that local morphology neighbours are retained
within the same density-defined region more frequently than expected
under arbitrary region assignment with identical region sizes.

### 3.9.3 Interpretation of Audit 01

The same-region retention result supports a limited conclusion:

    density-region membership is associated with local
    morphology geometry beyond the expectation generated
    by size-preserving random assignment.

The result does not imply that the density regions are discrete
semantic categories. The regions remain overlapping quantitative
structures in morphology space, as established by the regional
distance and silhouette analyses in Section 3.8.

The null therefore provides evidence for non-random local
morphology–region association rather than evidence for semantic
classification.

In particular:

    same-region neighbour retention
        ≠
    semantic category coherence

and:

    density region
        ≠
    morphology primitive.

### 3.9.4 Cross-Scale Profile-Correlation Null

A second permutation analysis evaluated whether quantitative
regional morphology profiles were reproducible across density
scales beyond arbitrary size-preserving region assignment.

For each density scale, regional feature discrimination was
calculated in the canonical 135-dimensional morphology space.

For each feature, regional discrimination was defined as:

    max regional feature mean
    -
    min regional feature mean.

This produced one 135-dimensional quantitative regional
discrimination profile for each density scale.

Cross-scale agreement was then quantified using Spearman correlation
between the 135-dimensional profiles of two scales.

Basin identities were not matched across scales. Numerical basin
identifiers were treated as scale-specific labels, and
cross-scale reproducibility was evaluated from the quantitative
feature-discrimination profiles.

For each scale pair, the observation-to-region membership of each
scale was independently permuted while preserving the complete
region-size distribution. Two hundred permutations were generated
for the null distribution.

The observed cross-scale correlations were:

    4.707252 → 5.416895
        ρ = 0.980743

    4.707252 → 6.248407
        ρ = 0.849220

    4.707252 → 7.596034
        ρ = 0.753053

    4.707252 → 10.640832
        ρ = 0.705677

    4.707252 → 16.568532
        ρ = 0.688894

    5.416895 → 6.248407
        ρ = 0.865038

    5.416895 → 7.596034
        ρ = 0.771559

    5.416895 → 10.640832
        ρ = 0.721647

    5.416895 → 16.568532
        ρ = 0.704585

    6.248407 → 7.596034
        ρ = 0.913023

    6.248407 → 10.640832
        ρ = 0.868745

    6.248407 → 16.568532
        ρ = 0.849571

    7.596034 → 10.640832
        ρ = 0.966023

    7.596034 → 16.568532
        ρ = 0.949810

    10.640832 → 16.568532
        ρ = 0.968964

The mean observed pairwise correlation across all fifteen scale
pairs was:

    observed mean ρ = 0.837103

The corresponding size-preserving permutation null was:

    null mean ρ = 0.106945
    null SD     = 0.048700
    null Q05    = 0.031239
    null Q95    = 0.182886

The observed mean exceeded the null mean by:

    observed − null = 0.730159

with:

    empirical upper-tail p = 0.004975
    z-score              = 14.992948.

All fifteen observed scale-pair correlations exceeded their
corresponding permutation-null distributions, with empirical
upper-tail probabilities of 0.004975.

### 3.9.5 Interpretation of the Cross-Scale Null

The cross-scale permutation result supports the reproducibility of
quantitative regional morphology profiles across independently
constructed density landscapes beyond arbitrary region assignment
with preserved region sizes.

This result is stronger than simply observing high correlations
between profiles. The corresponding size-preserving null asks
whether such agreement could arise when observations are randomly
assigned to regions while retaining the same region-size structure.

The observed correlations substantially exceeded this null.

The result is therefore interpreted as evidence for:

    reproducible quantitative regional morphology
    organization across observational scales.

It is not interpreted as evidence for:

    • persistent semantic morphology categories
    • persistent semantic primitives
    • a morphology grammar
    • identical basin identities across scales
    • a preferred density scale
    • exact manifold dimensionality.

### 3.9.6 Relationship Between the Two Null Tests

The two permutation analyses address complementary questions.

Audit 01 asks:

    Do local morphology neighbours remain within the same
    density-defined region more often than expected under
    size-preserving random assignment?

Audit 02 asks:

    Are quantitative regional morphology-discrimination
    profiles reproducible across density scales more strongly
    than expected under independently randomized,
    size-preserving region assignment?

Thus:

    Audit 01
        →
    local morphology–region association

    Audit 02
        →
    cross-scale reproducibility of regional
    morphology profiles

The two analyses use the same frozen morphology representation
and observed density-region assignments but test different
properties of the morphology–region relationship.

They are therefore interpreted as complementary diagnostics rather
than statistically independent experiments.

### 3.9.7 Discovery–Validation Separation

The density regions were discovered independently from the frozen
morphology geometry.

The permutation analyses did not rediscover, optimize, or redefine
the density regions. Instead, they preserved the observed region-size
structure while randomizing observation-to-region membership.

Thus:

    density-region discovery
        =
    morphology-derived density organization

whereas:

    permutation validation
        =
    size-preserving randomized region membership.

The distinction prevents the null procedure from altering the
discovered density landscape.

### 3.9.8 Interpretation Boundary

The combined permutation evidence supports the following limited
claim:

> Quantitative morphology associations with independently derived
> density regions are stronger than expected under size-preserving
> random assignment, and quantitative regional morphology profiles
> remain reproducible across independently constructed density
> scales.

The analysis does not establish:

    • semantic morphology categories
    • semantic morphology primitives
    • morphology states
    • morphology grammar
    • causal morphology structure
    • exact manifold dimensionality.

The appropriate interpretation therefore remains:

    quantitative morphology organization
        +
    non-random regional association
        +
    cross-scale reproducibility

rather than:

    semantic morphology categories
        or
    morphology grammar.

    
## 3.10 Cross-Scale Generalization of Regional Morphology Profiles

The reproducibility of regional morphology organization was
evaluated across independently derived density scales. The purpose
of this analysis was to determine whether quantitative morphology
profiles associated with density-derived regions remain consistent
when the observational scale used to construct the density
landscape changes.

The analysis used the canonical 135-dimensional morphology
representation defined in Section 3.2 and the six independently
constructed density-basin organizations defined in Section 3.7.

Importantly, basin identifiers were not treated as persistent
identities across scales. A numerical basin label at one scale was
not assumed to correspond to the same numerical label at another
scale. Cross-scale comparison was therefore performed using
quantitative morphology profiles rather than basin IDs.

### Cross-Scale Profile Representation

For each density scale, a quantitative morphology profile was
constructed for each density-derived region using the canonical
135-dimensional morphology representation.

The resulting collection of regional profiles at each scale
characterized the quantitative morphology structure associated
with that particular density landscape.

Adjacent observational scales were then compared to determine
whether their regional profile structures were reproducible.

### Profile Correspondence

Cross-scale correspondence was evaluated using quantitative
correlation of the regional morphology-profile structure.

The observed adjacent-scale profile correlations were:

    4.707252 → 5.416895
        ρ = 0.987665

    5.416895 → 6.248407
        ρ = 0.901663

    6.248407 → 7.596034
        ρ = 0.919744

    7.596034 → 10.640832
        ρ = 0.970510

    10.640832 → 16.568532
        ρ = 0.964808

These correlations indicate substantial reproducibility of the
quantitative regional morphology-profile structure across
successive observational scales.

The lower correlation observed for the transition from 5.416895
to 6.248407 nevertheless demonstrates that the regional
organization is not perfectly invariant across scales.

### Interpretation of Cross-Scale Stability

Cross-scale reproducibility was interpreted as evidence that the
quantitative morphology organization identified through density
analysis is not restricted to a single smoothing scale.

The analysis therefore distinguishes between:

    persistent quantitative regional structure

and:

    scale-dependent changes in regional organization.

The goal was not to identify a single optimal density scale.
Instead, the six scales were treated as a family of observational
views of the same underlying morphology representation.

Consistent profile structure across these views provides stronger
evidence for recurring quantitative organization than would be
obtained from a single density landscape.

### Relationship to the Permutation Null

The cross-scale analysis complements the permutation-based null
analysis in Section 3.9.

The permutation analysis asks:

    Are observed regional feature differences stronger
    than expected from arbitrary size-matched regional
    assignment?

The cross-scale analysis asks:

    Do the resulting quantitative regional profiles
    remain reproducible when the density landscape is
    constructed at a different observational scale?

Thus:

    M09
        tests non-random regional association

    M10
        tests cross-scale reproducibility

These analyses address different sources of uncertainty and are
therefore interpreted jointly rather than interchangeably.

### Scale Dependence

Cross-scale reproducibility does not imply that the density
organization is perfectly invariant.

Differences in basin number, basin membership, and regional
profile structure across scales are retained as part of the
observed morphology organization.

The appropriate interpretation is therefore:

    recurring quantitative regional organization
        with
    scale-dependent variation.

No single scale is designated as the canonical or optimal
representation solely on the basis of cross-scale agreement.

### Interpretation Boundary

Cross-scale profile reproducibility supports the stability of
quantitative morphology organization across independently derived
density scales.

It does not establish:

    morphology categories
    semantic morphology states
    semantic primitives
    morphology grammar
    causal morphology structure
    exact manifold dimensionality.

The result is therefore interpreted as evidence that regional
quantitative morphology profiles generalize across observational
scales while remaining compatible with continuous and
scale-dependent morphology organization.

## 3.11 Statistical Analysis, Reproducibility, and Interpretation Controls

All analyses were conducted using the same 2,300 source
observations and the same frozen canonical morphology
representation defined in Sections 3.2–3.3. The analytical
pipeline was designed to separate morphology-derived discovery
from subsequent validation and to prevent external semantic
information from entering the discovery process.

### Source-Only Transformation

The morphology standardization and PCA transformations were
fitted exclusively on the Clo-Sket source dataset and subsequently
frozen. No target or external observations were introduced during
feature scaling or dimensionality reduction.

Consequently, all downstream geometry analyses were performed in
a coordinate system defined independently of target data.

### Discovery–Validation Separation

Morphology organization was discovered using quantitative
morphology alone. Density regions were derived from the frozen
PCA morphology geometry without using category labels, semantic
annotations, replication labels, target sketches, or supervised
prediction.

Validation analyses were subsequently applied to the discovered
structure without redefining or optimizing the density regions.

In particular, the permutation analysis preserved the observed
regional size distribution while randomizing observation-to-region
membership. Cross-scale analysis independently evaluated whether
regional morphology profiles were reproducible across alternative
density scales.

This separation was maintained to prevent validation statistics
from being incorporated into the discovery procedure.

### Multiscale Analysis

Density organization was evaluated at six observational scales
derived empirically from the fifth-nearest-neighbor distance
distribution. The scales were treated as a family of observational
scales rather than as six independent claims of universal
significance.

Agreement across scales was therefore interpreted as evidence of
recurring quantitative organization, while differences across
scales were retained as part of the morphology structure.

No single density scale or basin count was selected solely because
it produced the strongest downstream result.

### Reproducibility

The analysis used fixed feature definitions, feature ordering,
source-only preprocessing, and deterministic transformation
specifications. The canonical morphology matrix and its downstream
transformation objects were retained as frozen analysis artifacts.

The PCA transformation was additionally checked by reproducing
the stored 73-dimensional representation from the canonical
135-dimensional morphology matrix and frozen preprocessing
objects.

Where permutation or resampling procedures were used, the same
statistical procedure was applied to the observed data and the
corresponding null or resampled data.

### Dependence Among Evidence Components

The individual analyses were not treated as statistically
independent experiments. They operate on the same source
observations and inherit the same frozen morphology
representation.

The evidence was therefore interpreted as a sequence of
complementary diagnostics:

    quantitative morphology representation
        ↓
    source-derived geometry
        ↓
    spectral structure
        ↓
    local and graph organization
        ↓
    recurring density organization
        ↓
    regional morphology profiles
        ↓
    permutation-based null validation
        ↓
    cross-scale reproducibility

The scientific strength of the analysis therefore comes from
convergence across complementary measurements of the same
representation rather than from combining the results as
independent hypothesis tests.

### Interpretation Controls

Quantitative morphology features, PCA components, density basins,
and regional profiles were not assigned semantic meanings during
the analysis.

In particular:

    PCA component
        ≠
    semantic morphology dimension

    density basin
        ≠
    morphology category

    morphology feature
        ≠
    semantic primitive

    geodesic path
        ≠
    semantic transition

Similarly, the 73-dimensional PCA representation and the
approximately 10.55-dimensional participation-ratio effective
dimension were not interpreted as exact manifold dimensionality.

These interpretation boundaries were defined before integrating
the evidence into the final scientific claim.

### Overall Claim Control

The final interpretation was restricted to conclusions directly
supported by the convergent evidence.

The analysis was considered capable of supporting claims concerning:

    • reproducible quantitative morphology representation
    • spectral concentration of morphology variation
    • local morphology organization
    • connected quantitative morphology geometry
    • recurring density organization
    • quantitative regional morphology profiles
    • non-random regional feature association under the
      tested permutation null
    • cross-scale quantitative reproducibility

The analysis was not considered sufficient to establish:

    • semantic morphology categories
    • semantic primitives
    • morphology grammar
    • causal morphology structure
    • exact manifold dimensionality

The final scientific interpretation therefore remains at the level
of structured quantitative morphology organization.