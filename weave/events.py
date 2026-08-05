"""
Core geometric data structures for WeaveAI.

The Sketch Graph is built progressively through
three levels of abstraction:

Signal
    ↓
CandidateEvent
    ↓
GeometryEvent
    ↓
GeometrySequence

CandidateEvents are raw geometric segments extracted
directly from the signal.

GeometryEvents are persistent geometric primitives
obtained after persistence analysis.

GeometrySequence is the symbolic intermediate
representation (IR) of garment geometry.
"""

from dataclasses import dataclass, field


# =====================================================
# Candidate Event
# =====================================================

@dataclass(frozen=True)
class CandidateEvent:
    """
    Raw geometric segment extracted directly
    from a 1D geometric signal.

    CandidateEvents intentionally over-segment
    the signal. They are temporary objects that
    are later validated, merged or discarded by
    the PersistenceAnalyzer.
    """

    # -----------------------------------------
    # Identity
    # -----------------------------------------

    kind: str

    # -----------------------------------------
    # Location
    # -----------------------------------------

    start: int
    end: int

    # -----------------------------------------
    # Geometry
    # -----------------------------------------

    length: int
    amplitude: float

    # -----------------------------------------
    # Differential Geometry
    # -----------------------------------------

    mean_gradient: float
    max_gradient: float

    mean_curvature: float
    max_curvature: float

    # =================================================

    @property
    def center(self):
        """Center location of the event."""
        return (self.start + self.end) // 2

    @property
    def duration(self):
        """Alias for event length."""
        return self.length

    # =================================================

    def __repr__(self):

        return (
            f"{self.kind}"
            f"[{self.start}:{self.end}]"
        )


# =====================================================
# Geometry Event
# =====================================================

@dataclass(frozen=True)
class GeometryEvent(CandidateEvent):
    """
    Persistent geometric primitive.

    GeometryEvents are CandidateEvents that
    survive persistence analysis and become
    part of the Sketch Graph.
    """

    # -----------------------------------------
    # Persistence
    # -----------------------------------------

    persistence: float = 0.0

    strength: float = 0.0

    confidence: float = 1.0

    # -----------------------------------------
    # Multi-scale Geometry
    # -----------------------------------------

    scale: int = 0


# =====================================================
# Geometry Sequence
# =====================================================

@dataclass
class GeometrySequence:
    """
    Ordered collection of GeometryEvents.

    GeometrySequence forms the symbolic
    intermediate representation (IR)
    of garment geometry.

    Higher-level reasoning modules
    (statistics, grammar, semantics)
    operate on GeometrySequence rather
    than directly on signals.
    """

    events: list = field(default_factory=list)

    # =================================================

    def append(self, event):

        self.events.append(event)

    def extend(self, events):

        self.events.extend(events)

    def clear(self):

        self.events.clear()

    # =================================================

    def __len__(self):

        return len(self.events)

    def __iter__(self):

        return iter(self.events)

    def __getitem__(self, index):

        return self.events[index]

    # =================================================

    @property
    def kinds(self):

        return [event.kind for event in self.events]

    @property
    def centers(self):

        return [event.center for event in self.events]

    # =================================================

    def summary(self):

        print("Geometry Sequence")
        print("-----------------")

        for event in self.events:

            print(event)

    # =================================================

    def __repr__(self):

        return (
            f"GeometrySequence("
            f"{len(self.events)} events)"
        )
