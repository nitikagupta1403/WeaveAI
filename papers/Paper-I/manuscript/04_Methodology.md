## 4. Methods

### 4.1 Color Image to V1 Line-Art Sketch

Color fashion images are converted into V1 line-art sketches using the LineartDetector. The resulting V1 sketches provide the computational representation used for subsequent geometric analysis.


### 4.2 Silhouette Boundary Extraction and Width Signature

Each V1 line-art sketch is converted into a binary representation. The binary sketch is processed row-wise to identify the leftmost and rightmost foreground coordinates at each retained vertical position. These boundary trajectories are smoothed using a seven-sample moving-average filter.

The garment width at each vertical position is then computed from the separation between the smoothed left and right boundaries, producing a one-dimensional width signature.

The resulting width signature represents garment width as a function of vertical position and provides the geometric signal used for subsequent analysis.


### 4.3 Candidate Geometric Event Detection

The width signature is analyzed as a one-dimensional geometric signal. Its first and second numerical derivatives are computed, and candidate event boundaries are identified from sign changes in the first derivative.

The resulting boundaries partition the width signature into consecutive intervals. Each interval is represented as a candidate geometric event characterized by its direction of change, length, amplitude, gradient, and curvature statistics.

Candidate detection intentionally over-segments the geometric signal. The resulting candidate events are therefore treated as provisional geometric intervals for subsequent persistence analysis.


### 4.4 Persistent Geometry Event Extraction

Candidate geometric events are filtered to remove geometrically insignificant intervals. A candidate event is retained when its length is at least 8 samples and its absolute amplitude is at least 3 pixels.

Adjacent retained events having the same geometric direction are subsequently merged. Each resulting event retains its geometric attributes, including event type, start and end positions, length, amplitude, mean and maximum gradient, and mean and maximum curvature.

The resulting ordered set of events forms the GeometrySequence for an individual garment and provides the persistent geometric representation used for subsequent corpus-level analysis.


### 4.5 Geometry Primitive Discovery

Persistent geometry events extracted across the garment sketch corpus are grouped according to their geometric similarity to identify recurring structural representations.

Let

\[
\mathcal{E}=\{E_1,E_2,\ldots,E_m\}
\]

denote the collection of persistent geometry events extracted from the corpus. A geometry primitive \(P_k\) is obtained from a subset of geometrically similar events,

\[
\mathcal{E}_k\subseteq\mathcal{E},
\]

according to

\[
P_k=\Psi(\mathcal{E}_k),
\]

where \(\Psi(\cdot)\) denotes the primitive-learning operator.

The resulting geometry primitives represent recurring geometric structures rather than individual event observations. The complete set of learned primitives is represented as

\[
\mathcal{P}=\{P_1,P_2,\ldots,P_K\},
\]

where \(K\) denotes the number of learned geometry primitives.

These primitives provide the reusable structural units from which the subsequent symbolic representation of individual garment sketches is constructed.