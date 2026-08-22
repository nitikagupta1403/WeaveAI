# CLO-SKET Paper 2 — Abstract, Title, and Keywords

## Status

**ABSTRACT + TITLE + KEYWORDS: PROVISIONALLY LOCKED**

This document assembles the final high-level manuscript positioning from the frozen Methods, Results, Discussion, literature audit, and novelty claim lock.

No new scientific claim is introduced here.

---

# 1. Preferred working title

## Primary title

**Evidence-Controlled Radial-Spectral Representation of Garment-Sketch Morphology**

### Why this is currently preferred

It emphasizes:

- the methodological principle;
- the representation-selection contribution;
- garment-sketch morphology;
- the radial-spectral nature of the framework.

It does not overemphasize:

- PCA;
- wavelets;
- nonlinear manifolds;
- Fourier novelty.

---

# 2. Alternative title candidates

## Candidate 2

**Harmonic-Dependent Radial Representation in Probabilistic Fourier Garment Morphology**

Strength:

- technically precise;
- foregrounds the main scientific finding.

Risk:

- slightly denser and less accessible.

---

## Candidate 3

**Probabilistic Fourier Morphology with Harmonic-Conditioned Radial Representation**

Strength:

- concise;
- method-focused.

Risk:

- does not emphasize evidence-controlled selection as strongly.

---

## Candidate 4

**Evidence-Guided Harmonic-Dependent Compression of Radial-Angular Garment Morphology**

Strength:

- directly reflects the representation-selection problem.

Risk:

- "compression" may make the paper sound narrower than it is.

---

# 3. Title recommendation

Current recommendation:

\[
\boxed{
\textbf{Evidence-Controlled Radial-Spectral Representation of Garment-Sketch Morphology}
}
\]

Final title should be revisited only after target-journal selection.

---

# 4. Final abstract

## Abstract

Garment sketches contain morphology distributed jointly across radial position and angular scale, yet compact spectral representations typically impose a common encoding rule across the transform domain. We investigate whether radial representation requirements instead vary with angular harmonic scale.

Each sketch is represented as a conditional radial-angular probability field,

\[
P_i(\theta\mid r),
\]

and angular Fourier transformation yields radial harmonic functions

\[
F_{i,k}(r),
\qquad
k=1,\ldots,36.
\]

Using 2,300 sketches from 230 garment identities across 23 categories, candidate radial representations were evaluated separately across four harmonic bands under garment-identity-disjoint validation with family-wise-error-rate-controlled inference. Compact four-coefficient radial representations were supported for \(k=1{:}4\) using a DCT basis and for \(k=25{:}36\) using a db4-wavelet basis, whereas compression was not supported for the intermediate \(k=5{:}24\) harmonics, whose complete 72-shell radial structure was retained.

The resulting heterogeneous DCT/raw/raw/wavelet representation reduced the spectral description from 2,592 to 1,504 complex coefficients per sketch, corresponding to a 41.98% coefficient reduction. Nonlinear latent models did not establish a multiplicity-controlled task advantage over PCA, although geometric audits identified nonlinear structure that was insufficient to justify replacing the validated linear latent representation.

The first 64 principal components retained 44.65% of standardized representation variance. Within this retained subspace, 78.54% of variance-weighted mapped morphology energy occurred at intermediate harmonic orders \(k=5{:}24\), 66.84% occurred in the outer radial zone, and 51.30% occurred jointly in the outer-radial × intermediate-harmonic region.

These results show that radial representation requirements and retained latent morphology vary systematically across angular scale. The study supports an evidence-controlled representation principle in which spectral structure is compressed only where supported and otherwise preserved at full radial resolution.

---

# 5. Abstract claim audit

The Abstract is allowed to state:

- dataset size;
- harmonic range;
- band-specific representation decisions;
- coefficient reduction;
- nonlinear-model negative result;
- PCA retained variance;
- PCA-64 morphology-localization percentages;
- evidence-controlled compression principle.

The Abstract must not imply:

- Fourier novelty;
- wavelet novelty;
- semantic garment interpretation;
- total-morphology percentages;
- universal optimality;
- universal superiority of PCA;
- literature-wide priority.

---

# 6. Short abstract version

For journals with stricter abstract limits:

> Garment sketches contain morphology distributed jointly across radial position and angular harmonic scale, yet compact spectral descriptors often impose uniform representation rules across the transform domain. We represent each sketch as a conditional radial-angular probability field \(P_i(\theta\mid r)\) and derive radial Fourier harmonic functions \(F_{i,k}(r)\), \(k=1,\ldots,36\). Using 2,300 sketches from 230 garment identities across 23 categories, radial representations were evaluated separately across four harmonic bands under garment-identity-disjoint, family-wise-error-rate-controlled inference. Four-coefficient DCT compression was supported for \(k=1{:}4\), four-coefficient db4-wavelet compression for \(k=25{:}36\), while compression was not supported for \(k=5{:}24\), whose full 72-shell radial structure was retained. The resulting DCT/raw/raw/wavelet representation reduced the spectral field from 2,592 to 1,504 complex coefficients, a 41.98% reduction. Nonlinear latent models did not establish a multiplicity-controlled task advantage over PCA. Within the retained PCA-64 subspace, mapped morphology energy was concentrated in intermediate harmonics and outer radial positions. These results support harmonic-conditioned radial representation rather than uniform spectral compression.

---

# 7. One-sentence paper summary

> **Paper 2 shows that radial representation requirements differ across angular harmonic scale and develops an evidence-controlled hybrid Fourier morphology representation that compresses only where supported while preserving full radial structure elsewhere.**

---

# 8. One-sentence methodological contribution

> **Rather than imposing one radial basis across the Fourier field, we evaluate radial encoding separately across angular harmonic bands under garment-identity-disjoint, multiplicity-controlled inference.**

---

# 9. One-sentence empirical contribution

> **Applied to CLO-SKET, the resulting representation reveals strong intermediate-harmonic and outer-radial organization within the retained PCA morphology subspace.**

---

# 10. Keywords

## Preferred keyword set

- garment sketch morphology
- radial-angular representation
- Fourier morphology
- shape analysis
- harmonic-dependent compression
- evidence-controlled representation
- garment-identity-disjoint validation
- principal component analysis
- interpretable spectral morphology

---

# 11. Compact keyword set

If the journal allows only 5–6 keywords:

- garment sketch morphology
- Fourier shape analysis
- radial-angular representation
- spectral compression
- principal component analysis
- interpretable morphology

---

# 12. Keywords to avoid

Do not use:

- semantic garment understanding
- causal morphology
- garment manifold
- denoising
- signal separation
- state-of-the-art
- deep learning

unless those become genuine primary content of the paper.

---

# 13. Running title

Possible short running title:

**Evidence-Controlled Fourier Garment Morphology**

Alternative:

**Radial-Spectral Garment Morphology**

---

# 14. Abstract logic

\[
\boxed{
\text{Problem}
\rightarrow
\text{Representation}
\rightarrow
\text{Inference}
\rightarrow
\text{Hybrid representation}
\rightarrow
\text{Latent validation}
\rightarrow
\text{Morphology localization}
\rightarrow
\text{Principle}
}
\]

---

# 15. Final high-level message

The manuscript should leave the reader with one idea:

\[
\boxed{
\textbf{spectral compression should follow evidence rather than architectural uniformity}
}
\]

For this dataset, that principle produced:

\[
\boxed{
DCT_4
/
RAW_{72}
/
RAW_{72}
/
db4_4
}
\]

rather than one common radial basis across all angular harmonics.

---

# 16. Step 12 lock

\[
\boxed{
\textbf{PAPER 2 ABSTRACT + TITLE + KEYWORDS — ASSEMBLED}
}
\]

Next:

\[
\boxed{
\textbf{STEP 13 — FINAL MANUSCRIPT ASSEMBLY}
}
\]

Step 13 should combine:

- Abstract
- Introduction
- Related Work
- Methods
- Results
- Discussion
- Conclusion
- Figure/table callouts
- bibliography placeholders

into one continuous manuscript draft without changing the frozen scientific claims.