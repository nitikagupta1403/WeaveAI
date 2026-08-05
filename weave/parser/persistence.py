import numpy as np

from ..events import (
    CandidateEvent,
    GeometrySequence,
)


class PersistenceAnalyzer:
    """
    Removes unstable candidate events and
    constructs a persistent GeometrySequence.
    """

    def __init__(
        self,
        candidates,
        min_length=8,
        min_amplitude=3.0,
    ):

        self.candidates = candidates
        self.min_length = min_length
        self.min_amplitude = min_amplitude

    # =====================================================
    # Main API
    # =====================================================

    def analyze(self):

        events = self.filter_small(
            self.candidates
        )

        events = self.merge_same_kind(
            events
        )

        return GeometrySequence(events)

    # =====================================================
    # Stage 1
    # Remove insignificant events
    # =====================================================

    def filter_small(
        self,
        events
    ):

        persistent = []

        for event in events:

            if (
                event.length >= self.min_length
                and
                abs(event.amplitude) >= self.min_amplitude
            ):
                persistent.append(event)

        return persistent

    # =====================================================
    # Stage 2
    # Merge neighbouring events
    # =====================================================

    def merge_same_kind(
        self,
        events
    ):

        if len(events) == 0:
            return []

        merged = [events[0]]

        for event in events[1:]:

            last = merged[-1]

            if event.kind == last.kind:

                merged[-1] = CandidateEvent(

                    kind=last.kind,

                    start=last.start,
                    end=event.end,

                    length=event.end - last.start,

                    amplitude=last.amplitude + event.amplitude,

                    mean_gradient=np.mean(
                        [
                            last.mean_gradient,
                            event.mean_gradient,
                        ]
                    ),

                    max_gradient=max(
                        last.max_gradient,
                        event.max_gradient,
                    ),

                    mean_curvature=np.mean(
                        [
                            last.mean_curvature,
                            event.mean_curvature,
                        ]
                    ),

                    max_curvature=max(
                        last.max_curvature,
                        event.max_curvature,
                    ),
                )

            else:

                merged.append(event)

        return merged
