"""
GeometryEvent is the atomic unit of the
WeaveAI Sketch Graph.

Every higher-level concept
(landmarks, regions, descriptors, grammar,
garment semantics) must be expressible as
combinations of GeometryEvents.
"""

# =====================================================
# Candidate Event
# =====================================================
from dataclasses import dataclass
@dataclass
class CandidateEvent:
    """
    Raw geometric segment extracted directly
    from the signal.

    CandidateEvents intentionally
    over-segment the geometry and
    are later validated by the
    PersistenceAnalyzer.
    """

    kind: str

    start: int
    end: int

    length: int

    amplitude: float

    mean_gradient: float
    max_gradient: float

    mean_curvature: float
    max_curvature: float

    @property
    def center(self):

        return (self.start + self.end) // 2

    def __repr__(self):

        return (
            f"{self.kind}"
            f"[{self.start}:{self.end}]"
        )
