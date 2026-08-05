"""
Core geometric data structures for WeaveAI.

Signal
    ↓
CandidateEvent
    ↓
GeometryEvent
    ↓
GeometrySequence

GeometrySequence is the symbolic intermediate
representation (IR) used throughout WeaveAI.
"""

from dataclasses import dataclass, field
from typing import Optional


# =====================================================
# Event Types
# =====================================================

RISE = "rise"
FALL = "fall"
PLATEAU = "plateau"


# =====================================================
# Candidate Event
# =====================================================

@dataclass
class CandidateEvent:
    """
    Temporary geometric segment extracted directly
    from the signal.

    CandidateEvents intentionally over-segment the
    signal before persistence filtering.
    """

    # -------------------------------------------------
    # Identity
    # -------------------------------------------------

    kind: str

    # -------------------------------------------------
    # Geometry
    # -------------------------------------------------

    start: int
    end: int

    length: int
    amplitude: float

    # -------------------------------------------------
    # Differential Geometry
    # -------------------------------------------------

    mean_gradient: float
    max_gradient: float

    mean_curvature: float
    max_curvature: float

    # =================================================

    @property
    def center(self):
        return (self.start + self.end) // 2

    @property
    def duration(self):
        return self.length

    @property
    def feature_vector(self):

        return [

            self.length,
            self.amplitude,

            self.mean_gradient,
            self.max_gradient,

            self.mean_curvature,
            self.max_curvature

        ]

    def as_dict(self):

        return {

            "kind": self.kind,

            "start": self.start,
            "end": self.end,

            "center": self.center,

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

@dataclass
class GeometryEvent(CandidateEvent):
    """
    Persistent geometric primitive.

    GeometryEvents survive persistence analysis
    and become nodes of the Sketch Graph.
    """

    # -------------------------------------------------
    # Identity
    # -------------------------------------------------

    event_id: Optional[str] = None
    garment_id: Optional[str] = None

    # -------------------------------------------------
    # Persistence
    # -------------------------------------------------

    persistence: float = 1.0
    strength: float = 1.0
    confidence: float = 1.0

    # -------------------------------------------------
    # Multi-scale
    # -------------------------------------------------

    scale: int = 0

    # -------------------------------------------------
    # Learned Representation
    # -------------------------------------------------

    primitive: Optional[int] = None
    primitive_family: Optional[str] = None
    prototype: Optional[int] = None

    grammar_role: Optional[str] = None

    # =================================================

    @property
    def primitive_name(self):

        if self.primitive is None:
            return None

        return f"P{self.primitive}"

    def as_dict(self):

        data = super().as_dict()

        data.update({

            "event_id": self.event_id,
            "garment_id": self.garment_id,

            "persistence": self.persistence,
            "strength": self.strength,
            "confidence": self.confidence,

            "scale": self.scale,

            "primitive": self.primitive,
            "primitive_family": self.primitive_family,
            "prototype": self.prototype,
            "grammar_role": self.grammar_role

        })

        return data

    def __repr__(self):

        label = self.primitive_name

        if label is None:

            return (
                f"{self.kind}"
                f"[{self.start}:{self.end}]"
            )

        return (
            f"{label} "
            f"{self.kind}"
            f"[{self.start}:{self.end}]"
        )


# =====================================================
# Geometry Sequence
# =====================================================

@dataclass
class GeometrySequence:
    """
    Ordered symbolic representation of
    one garment.
    """

    garment: Optional[str] = None

    events: list[GeometryEvent] = field(
        default_factory=list
    )

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

        return [e.kind for e in self.events]

    @property
    def primitives(self):

        return [e.primitive for e in self.events]

    @property
    def primitive_sentence(self):

        return [

            e.primitive_name

            for e in self.events

            if e.primitive is not None

        ]

    @property
    def family_sentence(self):

        return [

            e.primitive_family

            for e in self.events

            if e.primitive_family is not None

        ]

    @property
    def feature_matrix(self):

        return [

            e.feature_vector

            for e in self.events

        ]

    @property
    def positions(self):

        if not self.events:
            return []

        total = self.events[-1].end

        return [

            e.center / total

            for e in self.events

        ]

    # =================================================

    def summary(self):

        print(
            f"Geometry Sequence ({len(self.events)} events)"
        )

        for event in self.events:

            print(event)

    def __repr__(self):

        return (
            f"GeometrySequence({len(self.events)} events)"
        )
