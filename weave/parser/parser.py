from .candidate import CandidateDetector

from ..events import (
    GeometrySequence
)


class GeometryParser:
    """
    High-level geometry parsing pipeline.
    """

    def __init__(self, signal):

        self.signal = signal

    def parse(self):

        candidates = CandidateDetector(
            self.signal
        ).detect()

        sequence = GeometrySequence()

        sequence.extend(
            candidates
        )

        return sequence
