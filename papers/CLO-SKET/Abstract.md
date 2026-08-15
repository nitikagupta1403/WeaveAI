# Abstract

Fashion sketches are widely used to communicate garment form, yet the
quantitative morphology encoded in these sketches has received less
attention as an object of analysis independent of predefined semantic
categories. This study investigates whether garment sketches exhibit
reproducible quantitative morphology organization that can be
characterized directly from explicit image-derived morphology
measurements without semantic supervision.

Using 2,300 sketches from the Clo-Sket dataset, we construct a
canonical 135-dimensional morphology representation comprising
horizontal occupancy, vertical occupancy, and global geometric
descriptors. Source-only standardization followed by principal
component analysis yields a 73-dimensional intrinsic representation
retaining approximately 95% of the standardized morphology variance.
The resulting morphology space is evaluated using spectral,
neighborhood, graph-geodesic, transition, and multiscale density
analyses.

The morphology representation exhibits structured spectral and local
geometric organization, a connected morphology graph, and substantial
agreement between Euclidean and graph-based neighborhood ordering.
Multiscale density analysis identifies density-defined regions whose
quantitative morphology profiles differ from one another. Same-region
nearest-neighbor retention is substantially greater than expected
under a region-size-preserving permutation null, demonstrating that
density-region membership is non-randomly associated with local
morphology geometry. Cross-scale permutation analysis further shows
that the feature-level regional discrimination profiles are
substantially more correlated across density scales than expected
under independently permuted, size-preserving region assignments.

The regional profiles are not interpreted as compact morphology
categories. Within-region morphology dispersion remains substantial,
and the analysis therefore does not treat density-defined regions as
discrete states. Feature-order permutation analysis additionally
shows reproducible local structure in the ordered occupancy
coordinates, while preserving each observation's occupancy values
under the null.

Taken together, the results support an empirical characterization of
garment sketches as occupying a structured quantitative morphology
space containing connected local organization and reproducible
density-associated regional structure. The evidence supports
quantitative morphology organization rather than discrete semantic
categories. It does not establish semantic morphology primitives,
named morphology categories, a compositional morphology grammar, or a
mathematical manifold. Instead, the study establishes a measurable
geometric layer from which the relationship between quantitative
morphology and higher-level semantic organization can be investigated
in subsequent work.

**Keywords:** fashion sketches; garment morphology; morphology
representation; intrinsic geometry; density organization; spatial
locality; computational fashion; semantic morphology

