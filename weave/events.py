"""
Core symbolic data structures for WeaveAI.

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

from collections import Counter
from dataclasses import dataclass, field
from typing import Optional

import numpy as np


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

        return np.array(

            [

                self.length,
                self.amplitude,

                self.mean_gradient,
                self.max_gradient,

                self.mean_curvature,
                self.max_curvature,

            ],

            dtype=float,

        )

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
            "max_curvature": self.max_curvature,

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

    GeometryEvents survive persistence analysis
    and become the symbolic atoms of WeaveAI.
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

    @property
    def family_name(self):

        return self.primitive_family

    @property
    def grammar_symbol(self):

        return self.grammar_role

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

            "grammar_role": self.grammar_role,

        })

        return data

    def __repr__(self):

        label = self.primitive_name

        if label is None:

            return (
                f"{self.kind}"
                f"[{self.start}:{self.end}]"
            )

        if self.family_name is None:

            return (
                f"{label} "
                f"{self.kind}"
                f"[{self.start}:{self.end}]"
            )

        return (

            f"{label}"
            f"({self.family_name}) "

            f"{self.kind}"

            f"[{self.start}:{self.end}]"

        )


# =====================================================
# Geometry Sequence
# =====================================================

@dataclass
class GeometrySequence:
    """
    Ordered symbolic representation of one garment.
    """

    garment: Optional[str] = None

    events: list[GeometryEvent] = field(
        default_factory=list
    )

    # =================================================

    def append(self, event: GeometryEvent):

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
    # Event Properties
    # =================================================

    @property
    def kinds(self):

        return [

            e.kind

            for e in self.events

        ]

    @property
    def primitives(self):

        return [

            e.primitive

            for e in self.events

            if e.primitive is not None

        ]

    @property
    def primitive_sentence(self):

        return [

            e.primitive_name

            for e in self.events

            if e.primitive_name is not None

        ]

    @property
    def family_sentence(self):

        return [

            e.family_name

            for e in self.events

            if e.family_name is not None

        ]

    @property
    def grammar_sentence(self):

        return [

            e.grammar_symbol

            for e in self.events

            if e.grammar_symbol is not None

        ]

    @property
    def event_ids(self):

        return [

            e.event_id

            for e in self.events

        ]

    # =================================================
    # Geometry
    # =================================================

    @property
    def positions(self):

        if len(self.events) == 0:
            return []

        total = self.events[-1].end

        if total == 0:
            return [0.0] * len(self.events)

        return [

            e.center / total

            for e in self.events

        ]

    @property
    def feature_matrix(self):

        if len(self.events) == 0:

            return np.empty((0, 6))

        return np.stack(

            [

                e.feature_vector

                for e in self.events

            ]

        )

    # =================================================
    # Grammar
    # =================================================

    @property
    def transitions(self):

        return list(

            zip(

                self.primitive_sentence[:-1],

                self.primitive_sentence[1:]

            )

        )

    @property
    def primitive_counts(self):

        return Counter(

            self.primitive_sentence

        )

    @property
    def family_counts(self):

        return Counter(

            self.family_sentence

        )

    # =================================================

    def summary(self):

        print(
            f"Geometry Sequence ({len(self.events)} events)"
        )

        for event in self.events:

            print(event)

    # =================================================

    def __repr__(self):

        return (
            f"GeometrySequence({len(self.events)} events)"
        )
