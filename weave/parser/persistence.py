from ..events import (
    CandidateEvent,
    GeometryEvent,
    GeometrySequence,
)


class PersistenceAnalyzer:
    """
    Converts CandidateEvents into
    persistent GeometryEvents.

    CandidateEvents intentionally
    over-segment the signal.

    PersistenceAnalyzer removes
    insignificant events and merges
    neighboring events that belong
    to the same geometric structure.
    """

    def __init__(self, candidates):

        self.candidates = list(candidates)

    # =================================================

    def analyze(self):

        events = self.candidates

        events = self.filter_short(events)

        events = self.filter_small(events)

        events = self.merge_same_kind(events)

        return GeometrySequence(events)

    def filter_short(
        self,
        events,
        min_length=5
    ):
        """
        Remove tiny geometric fragments.
    
        They usually arise from numerical
        differentiation rather than
        meaningful geometry.
        """
    
        filtered = []
    
        for e in events:
    
            if e.length >= min_length:
    
                filtered.append(e)
    
        return filtered

    def filter_small(
        self,
        events,
        min_amplitude=3
    ):
    
        filtered = []
    
        for e in events:
    
            if abs(e.amplitude) >= min_amplitude:
    
                filtered.append(e)
    
        return filtered

    def merge_same_kind(
        self,
        events
    ):
    
        if not events:
            return []
    
        merged = [events[0]]
    
        for event in events[1:]:
    
            last = merged[-1]
    
            if event.kind == last.kind:
    
                last.end = event.end
    
                last.length = last.end - last.start
    
                last.amplitude += event.amplitude
    
            else:
    
                merged.append(event)
    
        return merged
