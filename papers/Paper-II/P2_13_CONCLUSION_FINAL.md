# CLO-SKET Paper 2 — Final Conclusion

## Status

**MANUSCRIPT-FACING CONCLUSION: LOCKED FOR INTEGRATION**

---

# 6. Conclusion

This study formulates compression of a structured garment-sketch radial-angular Fourier field as a **band-conditional inferential representation decision**. Candidate compact radial encodings are selected using training identities and retained only when their held-out garment-identity effect is supported under simultaneous inference; where support is absent, the complete radial field is preserved. The central methodological principle is therefore

\[
\boxed{\text{compress where supported; preserve otherwise.}}
\]

Applied to CLO-SKET, support for radial compression differed across the four tested harmonic bands. Four-coefficient representations were supported for \(k=1{:}4\) using DCT and for \(k=25{:}36\) using db4 wavelets, whereas tested compression was not supported for \(k=5{:}24\), for which the complete 72-shell radial representation was retained. The resulting

\[
\mathrm{DCT}_4/\mathrm{RAW}_{72}/\mathrm{RAW}_{72}/\mathrm{db4}_4
\]

representation reduced the field from 2,592 to 1,504 complex coefficients, a 41.98% reduction, without imposing a uniform basis or global coefficient budget.

Separately, nonlinear latent models did not establish a multiplicity-controlled held-out task advantage over PCA, although geometric audits identified nonlinear structure. PCA therefore provided the practical validated basis for subsequent interpretation rather than evidence that garment-sketch morphology is globally linear. The exact inverse lineage from PCA perturbations to \(\Delta F_j(r,k)\) retained mathematical traceability to the original radial-harmonic coordinates; localization within PCA-64 remains descriptive of that retained subspace rather than semantic garment structure.

The contribution is not a new Fourier, DCT, wavelet, or PCA transform. It is an evidence-controlled framework for deciding **where a structured spectral representation may be compressed, where its original radial resolution should be preserved, and how the selected latent variation can be traced back to explicit radial-harmonic coordinates**. Independent datasets and broader candidate representation families are required to determine how far this principle generalizes beyond the present CLO-SKET analysis.
