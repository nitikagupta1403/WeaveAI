# Figure 1 caption — manuscript-ready v1.0

**Figure 1. Probabilistic radial–angular Fourier morphology representation.**  
**(A)** A garment sketch is expressed relative to radial coordinate \(r\) and angular coordinate \(\theta\); the outline shown here is schematic and is not a dataset exemplar.  
**(B)** Spatial morphology is reorganized into the implemented \(72\times72\) radial-shell × angular-bin grid.  
**(C)** For each occupied radial shell, angular morphology is normalized as the conditional distribution \(P_i(\theta\mid r)\), satisfying \(\sum_\theta P_i(\theta\mid r)=1\); empty shells are retained as all-zero angular vectors.  
**(D)** Applying a one-sided real Fourier transform along the angular axis yields the complex radial-harmonic field \(F_{i,k}(r)\), retaining radial position explicitly for each positive angular harmonic \(k=1,\ldots,36\). The displayed Fourier magnitude field is schematic and serves only to explain the coordinate organization.  
**(E)** Positive harmonics are partitioned prospectively into four prespecified bands, \(k=1{:}4\), \(5{:}12\), \(13{:}24\), and \(25{:}36\). Subsequent radial-representation decisions are evaluated separately within these bands. Figure 1 defines the measurement construction only and does not imply semantic garment parts, relative frequency importance, or compression superiority.
