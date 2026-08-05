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
