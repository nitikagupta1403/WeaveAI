# WeaveAI — Intrinsic Geometry & Structural Spectral Learning v0.2

Status: conceptual checkpoint; literature-guided; architecture not frozen.

## Core progression

raster coordinates
→ object-relative coordinates
→ graph topology
→ geodesic geometry
→ graph spectrum
→ diffusion geometry
→ intrinsic coordinates

Core principle:

> Represent variation relative to the structure itself, not merely relative to the image canvas.

For WeaveAI, this extends the Paper-II question from:

- Where does information lie in raster/angular frequency?

toward:

- Where does information lie across intrinsic structural scales?

## Mathematical bridge

For a graph:

L = D - A

and:

L phi_k = lambda_k phi_k

The Laplacian eigenvectors form a graph analogue of Fourier modes.

Small eigenvalues correspond to slow variation across connected structure.
Large eigenvalues correspond to rapid variation across connected structure.

Spectral graph wavelets add localization:

> what structural scale changes + where on the graph it changes

## Geodesic insight

Euclidean distance asks how close two things are in ambient coordinates.
Geodesic distance asks how close they are along the structure they belong to.

For future WeaveAI:

d_image(i,j) != d_structural(i,j)

may be important.

Two strokes can be visually close but structurally unrelated.
Two primitives can be farther apart in the image but tightly related through garment construction.

Boundary:

> Geodesics are meaningful only after the graph/topology is meaningful.

Working order:

earn nodes → earn edges → earn topology → then use geodesics

## Diffusion Maps insight

Geodesic distance and diffusion distance are not the same.

Geodesic:
- shortest structural route

Diffusion:
- connectivity through many possible routes

This suggests a robust structural embedding for noisy sketches where one erroneous edge need not completely determine relational distance.

Potential future uses:
- coherent-part discovery
- graph clustering
- intrinsic embedding
- motif discovery
- structure-aware dimensionality reduction

## Laplacian Eigenmaps insight

Central principle:

> If neighborhood relations are meaningful, coordinates can emerge from structure.

Potential WeaveAI progression:

relations → graph → intrinsic coordinates

rather than imposing a global coordinate system first.

## Relationship to Paper II

Paper II established a narrower empirical result:

Under the tested raster-relative representation, spectral allocation depends on raster support; an object-relative construction removes that specific same-pixel support dependency.

This literature does not retroactively change that result.

It suggests a broader future direction:

canvas-relative representation
→ object-relative representation
→ structure-relative representation

This is an intellectual progression, not yet an experimental result.

## Emerging WeaveAI hierarchy

signal
→ geometry
→ relations
→ graph/topology
→ intrinsic geometry
→ grammar/program
→ semantics

Probability may operate at multiple levels.

One conceptual form is:

P(S, G, R, T, H | x)

where:
- S = signal / morphological evidence
- G = geometric primitives
- R = relations
- T = topology / structural organization
- H = higher-level garment explanation / program

No factorization or model is frozen.

## Strongest principles

Geometry supplies evidence.
Topology supplies structure.
Intrinsic geometry supplies meaningful distance and scale.
Probability manages uncertainty.

Top-line principle:

> Learn variation relative to the object's structure, not the coordinates in which it happened to be observed.
