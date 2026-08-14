# 3. Methods

## 3.1 Study Design

This study uses a geometry-first computational pipeline to investigate whether recurring structural units can be learned directly from fashion-sketch geometry.

The analysis proceeds in five stages:

1. extraction of persistent geometric events from garment sketches;
2. normalization and representation of individual event geometries;
3. unsupervised learning of a reusable primitive vocabulary;
4. analysis of primitive morphology, position, sequential organization, and composition;
5. evaluation of the frozen representation on an independent sketch benchmark.

The primary corpus is used to discover the geometry-derived vocabulary and characterize its internal organization. The learned vocabulary is subsequently frozen and transferred to the independent CLO-SK benchmark for external evaluation.

The overall representation can be summarized as:

$$
\text{Sketch}
\rightarrow
\text{Geometric Signature}
\rightarrow
\text{Persistent Events}
\rightarrow
\text{Normalized Event Curves}
\rightarrow
\text{Geometry Primitives}
\rightarrow
\text{Primitive Sequences}.
$$


## 3.2 Primary Sketch Corpus

The primary corpus comprised **333 fashion garment images** and their
corresponding line-art sketch representations. The source images were
organized as PNG files and processed to obtain line-art representations for
subsequent geometric analysis.

The data-preparation pipeline used the `LineartDetector` implementation from
the `controlnet_aux` package, with the pretrained annotator model
`lllyasviel/Annotators`. Each input garment image was loaded as an RGB image
and passed through the LineArt detector to obtain a corresponding line-art
representation.

The generated line-art representations were inspected visually against the
original garment images and, where corresponding reference sketches were
available, compared with the existing dataset sketch representations. This
comparison was used to assess the visual consistency of the generated
line-art representation with the available sketch data.

The resulting sketch corpus was subsequently used as the input to the
geometry-analysis pipeline described below.

Across the 333-sketch primary corpus, the geometry-analysis pipeline
ultimately yielded **1,934 persistent geometric events**. These persistent
events constitute the observations from which the geometry-primitive
vocabulary was learned.

## 3.3 Geometric Event Extraction

The garment width signature was parsed into a sequence of local geometric events using a two-stage procedure consisting of candidate-event detection followed by persistence filtering.

### 3.3.1 Candidate Event Detection

Candidate events were detected directly from the one-dimensional width signature. For each garment, the first derivative of the signature was computed numerically, and candidate boundaries were identified at changes in the sign of the gradient. Consecutive boundaries defined candidate intervals along the vertical extent of the garment.

For each candidate interval, the corresponding segment of the width signature was characterized by its mean gradient, maximum absolute gradient, mean curvature, maximum absolute curvature, interval length, and amplitude. The mean gradient was used to assign a provisional geometric type:

- `rise` for positive mean gradient,
- `fall` for negative mean gradient, and
- `plateau` when the mean gradient was approximately zero.

Candidate detection was intentionally permissive and therefore allowed short or weak events to be generated. These candidates were subsequently evaluated by the persistence stage rather than being treated as final geometric units.

### 3.3.2 Persistence Filtering

Candidate events were converted into persistent geometric events using fixed geometric thresholds. An event was retained when its interval length was at least 8 samples and its absolute amplitude was at least 3 pixels.

\[
L \geq 8
\]

and

\[
|A| \geq 3.
\]

Events that did not satisfy either criterion were discarded.

After filtering, neighboring events with the same provisional geometric type were merged into a single event. For merged events, the interval was extended from the beginning of the first event to the end of the last event, while amplitude, mean gradient, mean curvature, and related quantities were recomputed from the constituent events.

The resulting representation therefore consists of ordered persistent geometric events rather than manually defined garment components.

### 3.3.3 Event-Sequence Validation

The event-extraction procedure was evaluated on a validation sample of 16 sketches drawn from the 333-sketch corpus. For each validation sketch, the analysis recorded the width-signature length, number of candidate events, number of persistent events, and the resulting ordered sequence of geometric event types.

Across the validation cases, the number of candidate events varied substantially between sketches, reflecting differences in the complexity of the width signatures. Persistence filtering consistently reduced the candidate representation to a smaller set of retained events. For example, the validation cases included sketches with 70, 16, 203, and 8 candidate events, which were reduced to 4, 2, 7, and 2 persistent events, respectively.

The resulting event sequences preserved the vertical ordering of geometric changes. Examples included sequences such as

```text
rise → fall

## 3.4 Corpus-Wide Event Characterization

Following persistence filtering, the event-extraction pipeline was applied to the complete primary sketch corpus. For each garment, the resulting persistent events were retained in their original vertical order and summarized by event count, event type, interval length, and absolute amplitude.

For each garment, the number of candidate events and persistent events was recorded. The ratio

$$
C_g =
\frac{N_{\mathrm{candidate},g}}
{\max(1,N_{\mathrm{persistent},g})}
$$

was used as a descriptive measure of event compression produced by persistence filtering.

The distribution of the immediate geometric event types was quantified by counting occurrences of `rise`, `fall`, and `plateau` across the corpus. For each garment, the ordered sequence of persistent event types was also retained as a discrete event sequence.

To characterize corpus-level organization at this stage, complete event sequences were counted across garments and adjacent event transitions were recorded. For every ordered pair of consecutive event types $(a,b)$, the transition count

$$
T(a,b)
=
\sum_g
\sum_t
\mathbf{1}
\left[
e_{g,t}=a
\land
e_{g,t+1}=b
\right]
$$

was computed.

These analyses were descriptive and were used to characterize the structure produced by the event-extraction stage. The event types `rise`, `fall`, and `plateau` describe local behavior of the width signature and were not interpreted as semantic garment components. Subsequent primitive discovery operated on the geometric representation of persistent events rather than directly treating these three event types as the final primitive vocabulary.