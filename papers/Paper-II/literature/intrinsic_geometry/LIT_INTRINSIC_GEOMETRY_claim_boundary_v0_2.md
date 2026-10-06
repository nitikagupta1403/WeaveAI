# WeaveAI v0.2 — Claim Boundary

## Supported conceptual statements

1. Graph Laplacian eigenvectors provide a spectral basis over connectivity and can be interpreted as graph-frequency modes.
2. Spectral graph wavelets combine graph-frequency selectivity with localization over the graph.
3. Geodesic distance measures distance along a structure/manifold rather than purely through ambient coordinates.
4. Diffusion geometry summarizes multistep connectivity and can define intrinsic coordinates and distances.
5. Laplacian Eigenmaps derive low-dimensional coordinates from local neighborhood relationships.
6. These ideas provide precedents for moving from raster-relative toward more intrinsic representations.

## Not established for WeaveAI

1. We have not shown that a graph representation outperforms the current raster/object-relative representation.
2. We have not established the correct node definition.
3. We have not established the correct edge or relation types.
4. We have not established that geodesic or diffusion distance is superior for garment reasoning.
5. We have not established that graph wavelets are the correct spectral representation.
6. We have not selected a GNN, MeshCNN, diffusion model, or any other architecture.
7. We have not shown a causal link between Paper-II raster-support findings and future graph/manifold representations.

## Research rule

Representation precedents are not architecture decisions.

Before using geodesics, diffusion, graph spectra, or graph learning, WeaveAI must first earn:
nodes → edges → topology.
