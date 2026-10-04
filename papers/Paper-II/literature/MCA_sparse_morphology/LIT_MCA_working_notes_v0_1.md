# WeaveAI — MCA / Sparse Morphological Decomposition
## Working Literature Checkpoint v0.1

### Scope
This checkpoint freezes the current cross-domain MCA literature branch before further reading.

It is **not**:
- a final novelty synthesis,
- a claim that MCA belongs in Paper II,
- a frozen garment experiment,
- a frozen dictionary pair.

## Core mathematical idea

Classical MCA:

    x = Phi_1 alpha_1 + Phi_2 alpha_2 + ... + Phi_K alpha_K

The dictionaries/transforms are usually chosen in advance.
The sparse coefficients are recovered so that different structures are explained economically by different representations.

The core principle is:

> Different structures may be simple in different mathematical languages.

This is stronger than low-vs-high frequency. Morphology may depend on:
- scale,
- orientation,
- locality,
- elongation,
- curvature,
- continuity / coherence,
- oscillatory structure.

## MCA vs RPCA

MCA:
    x = sum_k Phi_k alpha_k

driven by different sparse morphologies.

RPCA:
    D = L + S

driven by low-rank shared structure plus sparse deviations.

For garments:
- L is not automatically silhouette.
- S is not automatically intricacy.
- an MCA component is not automatically semantic either.

## Cross-domain conclusions

1. Astronomy / GMCA:
   sparse morphological diversity can support blind latent-source separation.

2. OCT:
   structures with similar intensity can separate because one is point-like and another curve-like.

3. Seismic:
   dictionary choice follows actual signal morphology; there is no universal pair.

4. Hyperspectral:
   separated components can be retained as downstream feature channels.

5. Audio:
   components can overlap in the same domain and still separate without hard exclusive ownership.

6. Graphical documents:
   text and graphics may be separable despite identical black foreground and physical touching.

7. Actin microscopy:
   frequency alone is insufficient; thin coherent filaments and noise may both be high-frequency.

8. Retinal vessels:
   two legitimate meaningful structures can be factored; MCA is not restricted to signal-vs-noise.

9. Technical line drawings:
   morphology may be insufficient for semantics; relationships and context can be decisive.

## Future WeaveAI roles

### Role 1 — nuisance separation
garment structure vs annotation text / scan clutter

### Role 2 — structural factorization
global geometry vs internal construction / detail

### Role 3 — multi-branch representation
retain both or all useful components and process them differently downstream

## Experimental discipline for future garment MCA

1. Start with fixed generic dictionaries.
2. Use as few dictionaries as possible.
3. Measure structure-specific sparsity before full MCA.
4. Do not assign semantic names merely from component appearance.
5. Inspect residuals.
6. Add a dictionary only if residuals contain coherent unexplained morphology.
7. Learn garment-specific dictionaries only if fixed transforms are inadequate.
8. Separate morphology evaluation from semantic interpretation.
9. Add graph/topological/contextual reasoning only if morphology cannot resolve ambiguity.

## Open research question

> Do garment sketch structures exhibit sufficiently distinct sparse morphologies that a small fixed-dictionary MCA can factor useful global and local structure without deep representation learning?

Status: OPEN. Not yet tested.
