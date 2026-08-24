# CLO-SKET Paper 2 — Final Conclusion

## Status

**MANUSCRIPT-FACING CONCLUSION: LOCKED FOR INTEGRATION**

---

# 6. Conclusion

This study evaluated whether a common radial encoding should be imposed across angular harmonic bands in garment-sketch Fourier morphology. Under garment-identity-disjoint validation and multiplicity-controlled inference, support for radial compression differed across the four tested harmonic bands. Compact four-coefficient representations were supported for \(k=1{:}4\) using DCT and for \(k=25{:}36\) using db4 wavelets, whereas tested compression was not supported for \(k=5{:}24\), for which the complete 72-shell radial representation was retained. The resulting

\[
\mathrm{DCT}_4/\mathrm{RAW}_{72}/\mathrm{RAW}_{72}/\mathrm{db4}_4
\]

representation reduced the field from 2,592 to 1,504 complex coefficients, a 41.98% reduction, without forcing uniform compression across the representation.

Separately, nonlinear latent models did not establish a multiplicity-controlled held-out task advantage over PCA, although geometric audits identified nonlinear structure. PCA therefore provided the practical validated basis for subsequent interpretation rather than evidence that garment-sketch morphology is globally linear. Within the retained PCA-64 subspace, mapped morphology energy was concentrated predominantly at intermediate harmonic orders and outer radial positions; these quantities remain descriptive properties of the retained representation space rather than semantic garment attributes.

The contribution is therefore an evidence-controlled representation strategy: evaluate radial compression conditionally across angular harmonic bands, retain compact structure where supported, preserve complete radial information where support is absent, and maintain an exact path from latent variation back to radial-harmonic coordinates. Independent datasets and broader candidate representation families are required to determine how far this principle generalizes beyond the present CLO-SKET analysis.
