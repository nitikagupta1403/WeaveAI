# P2_11 Introduction + Related Work Claim/Literature Audit v1.0

**Audited file:** `P2_11_INTRODUCTION_RELATED_WORK_RECONCILED_v1_0.md`

**Against:**
1. `P2_03_LITERATURE_NOVELTY_AUDIT.md`
2. `P2_04_NOVELTY_CLAIM_LOCK.md`
3. `P2_13_05K_SUPPORT_DEPENDENCE_AND_CLAIM_RECONCILIATION_v1_0.md`

## Overall decision

\[
\boxed{\text{PASS WITH TWO REQUIRED REVISIONS}}
\]

The manuscript spine is correctly updated to representation validity → representation selection → latent interpretation, and the novelty boundary is appropriately conservative. Two revisions are required before freeze.

---

## Required revision 1 — restore citation integration

The reconciled draft preserved the literature structure but dropped most inline citations that were present in the current citation-integrated P2_11.

This is not acceptable for a manuscript-facing Introduction/Related Work file.

### Required action

Restore inline citations for the specific prior-art claims already supported by the frozen P2_11 and P2_13 literature layer, including:

- Zahn & Roskies (1972);
- Kuhl & Giardina (1982);
- Zhang & Lu (2002);
- Ricard et al. (2005);
- Yap et al. (2010);
- Kunttu et al. (2006) for multiscale Fourier descriptors, as in the current P2_11;
- An & Li (2014);
- Jolliffe & Cadima (2016);
- Hinton & Salakhutdinov (2006);
- Kingma & Welling (2014);
- Hastie & Stuetzle (1989);
- Tenenbaum et al. (2000);
- Coifman & Lafon (2006);
- Lei et al. (2021);
- Li et al. (2022);
- Bhunia et al. (2022);
- Chaudhuri et al. (2023);
- Koley et al. (2024);
- Lee et al. (2024);
- Islam et al. (2024);
- Yang & Fang (2010);
- Harris (1978);
- Kunttu, Kunttu & Visa (2005) for the 1-D zero-padding near-miss;
- Van Hoorick & Vondrick (2021);
- Wu et al. (2026).

Do not invent additional literature claims beyond the frozen review.

---

## Required revision 2 — do not elevate latent-complexity selection to a novelty contribution

Current Introduction says:

> “The study makes four contributions”

and lists **evidence-controlled latent-complexity selection** as a standalone contribution.

P2_04 and P2_13 treat the PCA/AE/VAE distinction as important scientific discipline, but not as a primary algorithmic novelty claim.

### Required action

Use **three main methodological contributions**:

1. controlled representation-validity audit;
2. harmonic-conditioned, evidence-controlled radial representation selection;
3. exact latent-to-morphology traceability.

Then state separately that the same evidential discipline is applied to latent-model complexity, where nonlinear-model utility is tested independently of nonlinear predictive structure.

This preserves the claim hierarchy without diminishing the latent validation result.

---

# Cross-checks that passed

## Representation-validity question

PASS.

The Introduction now asks whether unchanged garment content can receive different angular spectral allocation solely because surrounding raster support changes.

This matches P2_13.

## Prior-art concessions

PASS.

The draft explicitly concedes prior art for:

- Fourier descriptors;
- polar/radial-angular representations;
- GFD;
- ART;
- PHT;
- object centering;
- scale normalization;
- DCT/wavelet compression;
- PCA;
- AE/VAE;
- manifold methods.

## Same-pixel novelty boundary

PASS.

The strongest literature-facing claim remains:

> “We did not identify a direct precedent in the reviewed literature for this specific same-pixel support-dependence audit.”

This is appropriately qualified and does not claim absolute priority.

## Zero-padding boundary

PASS.

The draft correctly distinguishes 05K from ordinary Fourier zero-padding and does not claim that padding creates new garment information.

## GFD / ART differentiation

PASS.

The draft does not claim that Paper II is the first radial-angular shape descriptor.

## Representation-selection contribution

PASS.

The previously locked contribution remains intact:

\[
\text{harmonic-conditioned, evidence-controlled radial representation selection}.
\]

## Object-relative control

PASS.

The object-relative construction is framed as a matched control/counterfactual rather than as a novel normalization scheme.

## Historical chronology

PASS.

The support audit changes manuscript emphasis but does not retroactively alter the frozen hybrid.

## Prohibited novelty language

PASS.

No “first-ever,” “unprecedented,” “state-of-the-art,” “optimal,” or universal-superiority language appears.

## Contemporary CV positioning

PASS.

The manuscript does not turn Paper II into a retrieval benchmark against modern neural methods. It correctly distinguishes an audit-and-selection question from learned representation performance.

---

# Freeze decision

After restoring citation integration and reducing the formal contribution list from four to three main methodological contributions:

\[
\boxed{\text{P2\_11 INTRODUCTION + RELATED WORK = FREEZE-READY}}
\]
