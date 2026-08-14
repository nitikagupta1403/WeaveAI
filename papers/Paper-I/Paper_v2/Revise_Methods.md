### V1 Sketch Representation and Dataset Preparation

To establish a standardized visual representation for subsequent geometric analysis, garment images were converted into line-art representations. The V1 dataset comprised 333 garment images with corresponding line-art representations. The image collection was organized as paired image and sketch directories, preserving the original filename stem to maintain correspondence between each garment image and its line-art representation.

Line-art extraction was performed using the `LineartDetector` implementation provided by the `controlnet_aux` package, initialized from the pretrained annotator repository `lllyasviel/Annotators`. Each input image was loaded using the Python Imaging Library (PIL) and converted to RGB before being passed directly to the line-art detector. No additional geometric transformation or morphological processing was applied at the V1 stage.

To verify reproducibility of the representation, 14 samples were selected at approximately uniform intervals across the 333-image collection using evenly spaced indices. Line-art representations were regenerated for these samples and compared with the corresponding reference sketches. The comparison evaluated image dimensions, exact pixel equality, and mean absolute pixel difference.

All 14 regenerated representations had the same dimensions as their corresponding reference sketches. Exact pixel comparison yielded identical images for all 14 samples, with an exact pixel match for every sample and a mean absolute pixel difference of 0.0. This verification established that the V1 line-art representation could be reproduced under the same processing configuration.

The resulting V1 representation was therefore used as the standardized visual input for the subsequent geometric analyses. Later operations involving thresholding, morphological processing, or alternative sketch representations were treated as separate processing stages and were not part of the V1 representation.
# Methodology

## 1. Dataset and V1 Sketch Representation

### 1.1 Garment Image Dataset

The V1 dataset consisted of 333 garment images and their corresponding line-art representations. Image-to-sketch correspondence was maintained through matching filename stems between the image and sketch collections.

The garment images were converted into line-art representations using the `LineartDetector` implementation from the `controlnet_aux` package. The input images were loaded using the Python Imaging Library (PIL) and converted to RGB before being passed to the line-art detector.

The resulting line-art representations were generated and saved as the V1 sketch dataset.

### 1.2 V1 Representation Reproducibility

To verify reproducibility of the V1 line-art representation, 14 samples distributed approximately uniformly across the 333-image dataset were selected. The corresponding line-art representations were regenerated using the same processing configuration and compared with the stored reference sketches.

The comparison evaluated:

- image dimensions;
- exact pixel equality; and
- mean absolute pixel difference.

All 14 regenerated representations had the same dimensions as their corresponding reference sketches. All 14 samples showed exact pixel equality with their stored references, with a mean absolute pixel difference of 0.0.

This verification established reproducibility of the V1 line-art transformation under the same processing configuration.

---

## 2. Geometric Representation

### 2.1 Binary Sketch Representation

The line-art representations were converted into binary representations for subsequent geometric analysis.

Different notebook stages contain different implementations of binary conversion. In the RQ002 exploratory analysis, Otsu thresholding was used. The geometric-event pipeline subsequently used a fixed grayscale threshold of 10, producing a binary representation:

$$
B(x,y) =
\begin{cases}
1, & I(x,y) > 10 \\
0, & I(x,y) \leq 10
\end{cases}
$$

The exact binary preprocessing used for each corpus-level analysis is retained according to the implementation of the corresponding analysis stage.

---

## 3. Silhouette Sweep Algorithm

The binary garment representation was converted into left and right boundary trajectories using a row-wise boundary extraction procedure, referred to as the Silhouette Sweep Algorithm (SSA).

For each image row $y$, all foreground pixel coordinates were identified. The left and right boundary coordinates were defined as:

$$
L(y) = \min\{x : B(x,y) > 0\}
$$

and

$$
R(y) = \max\{x : B(x,y) > 0\}.
$$

Rows containing no foreground pixels were omitted.

The resulting left and right boundary x-coordinate sequences were independently smoothed using a seven-point moving average:

$$
\tilde{L}(y) = MA_7(L(y))
$$

$$
\tilde{R}(y) = MA_7(R(y)).
$$

The original row coordinates were retained, while only the boundary x-coordinates were smoothed.

The SSA therefore represents the garment silhouette as two ordered boundary trajectories:

$$
\tilde{L}(y), \tilde{R}(y).
$$

---

## 4. Width Signature

The left and right boundary trajectories were projected onto their x-coordinates and converted into a one-dimensional width representation.

For each corresponding boundary position:

$$
W(y) = \tilde{R}(y) - \tilde{L}(y).
$$

The resulting function, referred to as the width signature, represents garment width as a function of vertical position.

### 4.1 Signature Parameterization

For analyses requiring comparison between garments with different numbers of sampled rows, the width signature was parameterized onto a common normalized domain.

The original signature samples were assigned to a normalized domain:

$$
t \in [0,1]
$$

and resampled to 1024 points using cubic interpolation.

Thus, a variable-length width signature was transformed into a common representation:

$$
W(t_1), W(t_2), \ldots, W(t_{1024}).
$$

This representation enabled corpus-level comparison of garment width profiles.

---

## 5. Geometric Landmark Detection

RQ003 investigated whether structural garment landmarks could be operationalized directly from the width signature.

Local maxima and minima were detected from the width signature using the `scipy.signal.find_peaks` procedure:

$$
P_{\max} = \operatorname{find\_peaks}(W)
$$

and

$$
P_{\min} = \operatorname{find\_peaks}(-W).
$$

No prominence, minimum-distance, derivative, or amplitude-normalization parameters from the separate generic signal-analysis implementation were used by the `LandmarkDetector` examined here.

### 5.1 Position-Constrained Landmark Rules

Candidate extrema were interpreted as structural garment landmarks using predefined normalized positional intervals.

#### Shoulder

Shoulder detection searched the upper portion of the width signature between 5% and 35% of the signature length.

Among local maxima within this interval, the maximum-width peak was selected:

$$
y_{\mathrm{shoulder}}
=
\arg\max_{y \in P_{\max},\,0.05N \leq y \leq 0.35N}
W(y).
$$

#### Waist

The waist search began at the detected shoulder and extended to 60% of the signature length.

The first local minimum after the detected shoulder was selected:

$$
y_{\mathrm{waist}}
=
\min
\left\{
y \in P_{\min} :
y > y_{\mathrm{shoulder}},
\ y \leq 0.60N
\right\}.
$$

#### Hem

Hem detection searched the lower portion of the width signature between 70% and 100% of the signature length.

The maximum-width local maximum within this interval was selected:

$$
y_{\mathrm{hem}}
=
\arg\max_{y \in P_{\max},\,0.70N \leq y \leq N}
W(y).
$$

The resulting landmarks were therefore defined operationally as position-constrained extrema of the width signature.

These semantic labels represent the operational interpretation assigned by the detector and were not treated as independently validated anatomical ground truth.

---

## 6. Geometric Event Representation

RQ006 extended the width-signature representation beyond a fixed set of semantic landmarks by representing the complete width profile as an ordered sequence of geometric events.

The width signature was differentiated numerically to obtain a first derivative:

$$
G(y) = \nabla W(y)
$$

and a second derivative:

$$
C(y) = \nabla G(y).
$$

The second derivative was retained as a curvature-related descriptor of local geometric change.

---

## 7. Candidate Geometric Events

Candidate geometric events were generated directly from the width signature.

The first derivative was examined for changes in sign. A candidate event boundary was introduced whenever:

$$
\operatorname{sign}(G_i)
\neq
\operatorname{sign}(G_{i+1}).
$$

The beginning and end of the signal were also included as event boundaries.

The resulting boundaries partitioned the width signature into consecutive candidate intervals.

For each candidate interval $[s,e]$, the following geometric descriptors were calculated:

- start position;
- end position;
- interval length;
- signal amplitude;
- mean gradient;
- maximum absolute gradient;
- mean curvature;
- maximum absolute curvature.

The signal amplitude was defined as:

$$
A = W(e) - W(s).
$$

The mean gradient was used to classify each candidate event as:

- `rise`, when the mean gradient was greater than $10^{-6}$;
- `fall`, when the mean gradient was less than $-10^{-6}$; or
- `plateau`, when the absolute mean gradient was at most $10^{-6}$.

Candidate detection was intentionally designed to over-segment the width signal. The resulting candidate events were subsequently filtered and merged to obtain a more compact geometric representation.

---

## 8. Candidate Event Filtering and Persistence

Candidate events were passed to the `PersistenceAnalyzer` for consolidation.

Despite the software component being named `PersistenceAnalyzer`, the implemented procedure does not perform topological persistence analysis. Persistence was operationalized through minimum event length, minimum amplitude, and subsequent merging of adjacent events with the same event type.

An event was retained only when both conditions were satisfied:

$$
\mathrm{length} \geq 8
$$

and

$$
|\mathrm{amplitude}| \geq 3.0.
$$

Candidate events failing either criterion were removed.

### 8.1 Merging of Same-Type Events

After filtering, adjacent events were examined sequentially. If two neighbouring events had the same event type (`rise`, `fall`, or `plateau`), they were merged into a single event.

For a merged interval, the start position was taken from the first event and the end position from the final event.

The merged event length was:

$$
L_{\mathrm{merged}}
=
e_{\mathrm{last}} - s_{\mathrm{first}}.
$$

The amplitudes of merged events were summed, while gradient and curvature descriptors were aggregated according to the implemented averaging and maximum operations.

The resulting events were represented as `GeometryEvent` objects and stored in an ordered `GeometrySequence`.

The complete geometric-event representation was therefore:

$$
W(y)
\rightarrow
\nabla W(y)
\rightarrow
\text{candidate intervals}
\rightarrow
\text{event filtering}
\rightarrow
\text{same-type merging}
\rightarrow
\text{GeometrySequence}.
$$

---

## 9. Corpus-Level Geometric Representation

The complete V1 corpus contained 333 garment sketches.

For corpus-level analyses requiring a common representation, the normalized width signatures were assembled into a matrix:

$$
S \in \mathbb{R}^{333 \times 1024}.
$$

Each row represented one garment and each column represented a normalized vertical position along the garment.

This matrix enabled statistical characterization of garment geometry, including:

- mean width profiles;
- width variability across the normalized garment domain; and
- principal component analysis of width-profile variation.

The mean width profile was calculated as:

$$
\mu(t)
=
\frac{1}{N}
\sum_{i=1}^{N} S_i(t),
$$

where $N=333$.

The corresponding standard deviation profile was calculated across the 333 garment signatures.

---

## 10. Geometry-Event Evaluation

To examine the behaviour of the geometric-event representation across garment types, one representative sketch was selected from each of the 16 observed filename classes.

The resulting evaluation set therefore contained 16 representative garments from the 333-sketch corpus.

For each representative garment, the following quantities were recorded:

- signature length;
- number of candidate geometric events;
- number of persistent geometric events; and
- ordered sequence of persistent event types.

Across the 16 representatives:

- mean candidate events = 135.0;
- mean persistent events = 5.25;
- median persistent events = 3.5;
- minimum persistent events = 2; and
- maximum persistent events = 26.

The number of persistent events therefore varied substantially across garments. This indicates that the resulting symbolic representation is variable in length and reflects differences in geometric complexity rather than imposing a fixed number of geometric units.

This evaluation was treated as a cross-garment geometric evaluation rather than an accuracy validation, because manually annotated ground-truth event locations were not established in the analyses reviewed here.

---

## 11. Methodological Scope of the Current Analysis

The analyses reviewed through RQ006 establish a deterministic geometric pipeline:

$$
\boxed{
\text{Garment Image}
\rightarrow
\text{V1 LineArt}
\rightarrow
\text{Binary Representation}
\rightarrow
\text{SSA}
\rightarrow
\text{Width Signature}
\rightarrow
\text{Geometric Extrema / Events}
\rightarrow
\text{Symbolic Geometry}
}
$$

The landmark branch operationalizes selected extrema as candidate structural landmarks, while the geometric-event branch represents the broader width profile as an ordered sequence of persistent directional events.

At this stage, the evidence supports the construction and exploratory evaluation of a one-dimensional geometric representation and deterministic symbolic event extraction. It does not by itself establish a complete semantic garment grammar, anatomical landmark accuracy, or semantic correctness of the resulting event labels. These claims require additional validation.

## 10.2 Corpus-Level Geometry-Event Statistics

The complete V1 corpus of 333 garment sketches was processed using the deterministic geometric-event pipeline. For each garment, candidate-event count, persistent-event count, candidate-to-persistent compression, event-type counts, mean and maximum event length, and mean event amplitude were recorded.

Across the 333 garments, the mean number of candidate events was 81.31 (median = 57; range = 2–655), whereas the mean number of persistent events was 5.81 (median = 4; range = 2–32).

The candidate-to-persistent compression ratio was defined as:

$$
C =
\frac{N_{\mathrm{candidate}}}
{\max(1,N_{\mathrm{persistent}})}.
$$

The mean compression ratio was 21.77, with a median of 9.25 and a range of 1–327.5. Thus, the event-consolidation procedure substantially reduced the number of candidate events while retaining a variable-length representation across garments.

The persistent event sequences contained, on average, 2.91 rise events and 2.90 fall events per garment. No plateau events were retained in the corpus. The mean persistent-event length was 184.37 samples (median = 151.83; range = 14–592), while the mean of the maximum event length per garment was 474.51 samples (range = 17–1162). The mean event amplitude per garment was 218.47 (median = 199.32; range = 39.03–532.14).

These statistics characterize the scale, variability, and degree of consolidation of the geometric-event representation across the complete garment corpus. They do not establish semantic correctness or identify the events as specific garment components.

## 10.3 Distribution and Recurrence of Geometry-Event Sequences

The persistent-event representation was further examined at the garment level by analysing event-sequence frequencies and the distribution of persistent-event counts.

Across the 333 garments, recurring event-type sequences were observed. The most frequent sequence was:

$$
rise \rightarrow fall \rightarrow rise \rightarrow fall
$$

which occurred in 98 garments, followed by:

$$
rise \rightarrow fall
$$

in 75 garments, and:

$$
rise \rightarrow fall \rightarrow rise \rightarrow fall \rightarrow rise \rightarrow fall
$$

in 53 garments.

The distribution of persistent-event counts was strongly right-skewed. Most garments contained relatively short sequences, with a median of 4 persistent events and a mean of 5.81, while a smaller number of garments contained substantially longer sequences, with a maximum of 32 persistent events.

Candidate-event counts showed greater variability, ranging from 2 to 655 events per garment. Several garments exhibited substantial candidate-to-persistent reduction; for example, ST1 contained 655 candidate events but only 2 persistent events, corresponding to a compression ratio of 327.5. Conversely, garments such as MD4 retained 32 persistent events from 142 candidates.

These observations indicate that the event representation produces variable-length geometric sequences and that the degree of event consolidation varies across garments. The recurring rise/fall sequences were treated as descriptive geometric patterns rather than as validated semantic grammar rules.