# 1. Introduction

Garment sketches are sparse visual objects whose few strokes encode silhouette, proportion, bilateral organization, and directional structure before a garment is physically realized. They are increasingly used as inputs to fashion retrieval, generation, editing, and reconstruction systems, yet most computational work evaluates sketches through downstream task performance. A complementary question is therefore whether garment-sketch geometry can be represented explicitly, with its construction and transformation properties visible, and whether that representation contributes predictive information beyond conventional morphology.

This distinction matters because an improved downstream score does not by itself explain what geometric information has been added. Explicit numerical shape representations provide a way to expose that information directly. In this study, foreground evidence is described relative to the sketch centroid using radial shells and their conditional angular distributions. For shell \(r\), let \(p(\theta\mid r)\) denote the normalized angular distribution. Undirected directional organization is summarized by the second circular harmonic

\[
F_2(r)=\sum_k p(\theta_k\mid r)e^{-2\mathrm{i}\theta_k},
\]

with magnitude \(R_2(r)=|F_2(r)|\) and axial orientation

\[
\alpha_2(r)=-\tfrac12\arg F_2(r)\pmod{\pi}
=\tfrac12\operatorname{atan2}\!\left(S_2(r),C_2(r)\right)\pmod{\pi},
\]

under the adopted negative-exponential convention \(F_2=C_2-\mathrm{i}S_2\). The choice \(m=2\) follows from axial symmetry rather than retrospective classification performance: an undirected axis satisfies \(\theta\equiv\theta+\pi\), making the second harmonic the lowest non-zero order compatible with axial reversal.

The shell-level field is summarized by a compact 14-dimensional representation comprising eight radial descriptors of second-harmonic magnitude and six axial descriptors encoded in doubled-angle form. Algebraically redundant quantities are excluded, and axial directions are represented through Cartesian doubled-angle coordinates rather than raw Euclidean angles. The representation is therefore explicit, low-dimensional, and mechanically interpretable rather than learned as a latent embedding.

CLO-SKET provides a particularly important validation setting because its 2,300 images are not 2,300 independent garment instances. They correspond to 230 recoverable source-garment identities distributed across 23 categories, with repeated sketches associated with each identity. We therefore treat complete garment identity as the indivisible unit of train/test separation, uncertainty resampling, and permutation. This evaluates transfer to unseen recovered garments rather than merely unseen image files and prevents repeated drawings of the same source garment from crossing validation boundaries.

The primary predictive question is whether the axial–radial representation adds category-discriminative information beyond a frozen 135-dimensional morphology vector. For evaluation score \(\mathcal S\), the prespecified increment is

\[
\Delta_{RA}=\mathcal S(\mathbf z_M\oplus\mathbf z_{RA})-\mathcal S(\mathbf z_M).
\tag{1}
\]

A positive \(\Delta_{RA}\) establishes incremental predictive utility under the tested protocol, but it does not establish statistical independence, information-theoretic uniqueness, or garment-specific complementarity. In particular, concatenation can improve prediction even if the added representation carries category-conditioned structure that does not depend on being paired with the exact same garment identity.

We therefore test a stronger correspondence requirement by reassigning complete axial–radial identity blocks within garment category while preserving category membership and block-size structure. If correct garment-level pairing contributes specifically to the observed gain, the aligned combination should outperform category-preserving misalignment:

\[
\mathcal S(\mathbf z_{M,i},\mathbf z_{RA,i})
>
\mathcal S(\mathbf z_{M,i},\mathbf z_{RA,\pi(i)}).
\tag{2}
\]

This restricted permutation separates two claims that are often conflated in multi-representation studies: **predictive increment** and **instance-specific correspondence**.

The study therefore addresses three research questions. **RQ1:** Does the second-harmonic axial–radial representation have explicit geometric meaning and the intended transformation behavior? **RQ2:** Does it improve garment-category discrimination beyond morphology under garment-identity-disjoint validation, and is that increment robust to identity-aware uncertainty and repeated grouped partitions? **RQ3:** Is the increment concentrated in radial or axial organization, and does it depend on exact garment-level morphology–axial–radial correspondence?

The contribution is both representational and methodological. We provide a compact axial–radial measurement of garment-sketch geometry; evaluate it under dependency-aware grouped validation; quantify uncertainty using category-stratified garment-identity bootstrap and repeated grouped partitions; and use a category-preserving identity-block permutation to test whether predictive improvement requires exact garment pairing. Rotation, reconstruction, discretization, harmonic, and phase-conditioning controls further define the representation's transformation behavior and numerical limits, with extended diagnostics reported in the Supplementary Material. The resulting framework is intentionally claim-bounded: it supports an explicit geometric representation and tests its predictive contribution without equating predictive gain with semantic meaning, causal structure, or uniquely paired garment-level complementarity.
