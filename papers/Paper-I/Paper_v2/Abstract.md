# Abstract

Fashion sketches provide a compact visual representation of garment design,
but their recurring geometric structure is difficult to represent without
imposing predefined semantic categories. This work investigates whether a
reusable structural vocabulary can instead be learned directly from the
geometry of fashion sketches.

A geometry-first pipeline was applied to 333 garment sketches, extracting
1,934 persistent geometric events and learning a vocabulary of 12 recurring geometry primitives. The learned primitives exhibited strong morphological coherence,
with substantially greater within-primitive than between-primitive similarity
under permutation testing. Primitive sequences also exhibited structured
sequential organization: family-level transitions deviated significantly from
within-garment permutation expectations, and immediate primitive context
substantially improved prediction of subsequent primitives, including on
garments excluded from transition estimation. Primitive identity was
additionally associated with characteristic positional distributions and local
sequential neighborhoods, while complete garments could be represented as
ordered compositions of relatively small subsets of the shared primitive
vocabulary.

The frozen representation was subsequently evaluated on an independent CLO-SK
benchmark comprising 2,299 sketch images from 230 garment identities, 23
categories, and 12 sketchers. Raw geometry substantially outperformed the
symbolic representations for direct garment-identity retrieval, including
under cross-sketcher evaluation, demonstrating that the symbolic vocabulary
does not preserve all image-level geometric information. Nevertheless, the
frozen representation retained measurable structural information: primitive
sets showed greater similarity within garment identities than between
identities, primitive usage contained category-associated information above
the uniform baseline, and primitive usage was systematically associated with
independently measured geometric properties.

Together, these findings provide evidence that recurring geometric structure
in fashion sketches can be learned and represented as a structured system of
reusable components and their relationships. The resulting sequential
regularities support a corpus-derived, grammar-like representation of garment
geometry. The contribution is deliberately limited to computational
structural organization: the learned representation is not treated as a
complete or universal language of fashion design, and its relationship to
independently validated human semantic concepts remains an open question.