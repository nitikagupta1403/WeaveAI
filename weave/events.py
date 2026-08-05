"""
Core geometric data structures for WeaveAI.

The Sketch Graph is constructed progressively
through three levels of abstraction.

Signal
    ↓
CandidateEvent
    ↓
GeometryEvent
    ↓
GeometrySequence

CandidateEvents are temporary geometric
segments extracted directly from a signal.

GeometryEvents are persistent geometric
primitives that survive persistence analysis.

GeometrySequence is the symbolic intermediate
representation (IR) used by all higher-level
modules such as statistics, grammar,
semantics and garment reasoning.
"""

from dataclasses import dataclass, field


# =====================================================
# Event Types
# =====================================================

RISE = "rise"
FALL = "fall"
PLATEAU = "plateau"


# =====================================================
# Candidate Event
# =====================================================

@dataclass(frozen=True)
class CandidateEvent:
    """
    Raw geometric segment extracted directly
    from a one-dimensional signal.

    CandidateEvents intentionally over-segment
    the geometry. They are temporary objects
    that are later validated, merged or removed
    by the PersistenceAnalyzer.
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
        """Center of the event."""
        return (self.start + self.end) // 2

    @property
    def duration(self):
        """Alias for event length."""
        return self.length

    @property
    def feature_vector(self):
        """
        Numerical representation of the event.
        """

        return [

            self.length,

            self.amplitude,

            self.mean_gradient,

            self.max_gradient,

            self.mean_curvature,

            self.max_curvature

        ]

    def as_dict(self):
        """
        Dictionary representation.
        """

        return {

            "kind": self.kind,

            "start": self.start,
            "end": self.end,

            "length": self.length,

            "amplitude": self.amplitude,

            "mean_gradient": self.mean_gradient,
            "max_gradient": self.max_gradient,

            "mean_curvature": self.mean_curvature,
            "max_curvature": self.max_curvature

        }

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

    persistence: float = 1.0

    strength: float = 1.0

    confidence: float = 1.0

    # -----------------------------------------
    # Multi-scale Geometry
    # -----------------------------------------

    scale: int = 0

    # =================================================

    def as_dict(self):

        data = super().as_dict()

        data.update({

            "persistence": self.persistence,

            "strength": self.strength,

            "confidence": self.confidence,

            "scale": self.scale

        })

        return data

    def __repr__(self):

        return (

            f"{self.kind}"

            f"[{self.start}:{self.end}]"

            f""

            f"(p={self.persistence:.2f})"

        )


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

    Every higher-level module operates
    on GeometrySequence rather than
    directly on signals.
    """

    events: list[GeometryEvent] = field(
        default_factory=list
    )

    # =================================================

    def append(
        self,
        event: GeometryEvent
    ):

        self.events.append(event)

    def extend(
        self,
        events
    ):

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

        return [

            event.kind

            for event in self.events

        ]

    @property
    def centers(self):

        return [

            event.center

            for event in self.events

        ]

    @property
    def feature_matrix(self):

        return [

            event.feature_vector

            for event in self.events

        ]

    @property
    def positions(self):

        if len(self.events) == 0:
            return []

        total = self.events[-1].end

        return [

            event.center / total

            for event in self.events

        ]

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
