# Abstract

Fashion sketches are widely used to communicate garment form, yet the
morphological structure encoded in these sketches remains largely
described through predefined visual categories or manually specified
attributes. This study investigates whether garment sketches contain
an underlying quantitative organization that can be learned directly
from image morphology and that may provide a foundation for a
computational language of fashion sketches.

Using 2,300 sketches from the Clo-Sket dataset, we construct a
canonical 135-dimensional morphology representation comprising
horizontal occupancy, vertical occupancy, and global geometric
descriptors. Source-only standardization and principal component
analysis yield a 73-dimensional representation retaining
approximately 95% of the standardized morphology variance. The
resulting morphology space is characterized through spectral,
neighborhood, graph, transition, and multiscale density analyses.

The morphology representation exhibits concentrated spectral
structure, global connectivity, and relatively smooth local
transitions. Within this connected space, independently derived
density landscapes reveal recurring regions of elevated morphology
density across multiple observational scales. These regions are not
strongly compact clusters: within-region distances remain comparable
to or greater than between-region distances, while local
same-region neighborhood retention is substantial. Nevertheless,
regional morphology profiles are reproducible across observational
scales, and at finer scales their quantitative feature associations
exceed a size-matched permutation null.

Feature-block complementarity and perturbation analyses further show
that the observed morphology geometry is distributed across multiple
quantitative feature families rather than being dominated by a small
number of individual measurements. Importantly, quantitative
properties associated with continuous morphology variation overlap
with those distinguishing recurring density regions, linking
continuous and regional levels of morphology organization.

Taken together, the results support an empirical characterization of
garment sketches as occupying a continuous and connected quantitative
morphology space containing recurring density-organized regions with
reproducible quantitative profiles. The findings do not establish
discrete semantic morphology categories, semantic primitives, or a
compositional morphology grammar. Instead, they establish a
quantitative geometric substrate from which the semantic organization
of garment sketches can be empirically investigated.

**Keywords:** fashion sketches; garment morphology; morphology
representation; intrinsic geometry; density organization; visual
language; computational fashion; semantic morphology