"""
GeometryEvent is the atomic unit of the
WeaveAI Sketch Graph.

Every higher-level concept
(landmarks, regions, descriptors, grammar,
garment semantics) must be expressible as
combinations of GeometryEvents.
"""

from dataclasses import dataclass, field
from typing import List


# =====================================================
# Event Types
# =====================================================

RISE = "rise"
FALL = "fall"
PLATEAU = "plateau"
PEAK = "peak"
VALLEY = "valley"
CORNER = "corner"
INFLECTION = "inflection"
TERMINATION = "termination"


# =====================================================
# Geometry Event
# =====================================================

@dataclass
class GeometryEvent:
    """
    Atomic unit of geometric information.

    A GeometryEvent represents one continuous region
    of homogeneous geometric behaviour in a one-
    dimensional signal.

    Higher-level concepts such as landmarks,
    garment regions and semantics should emerge
    from combinations of GeometryEvents rather
    than being detected directly.
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
    # Basic Geometry
    # -----------------------------------------

    amplitude: float

    # -----------------------------------------
    # Differential Geometry
    # -----------------------------------------

    mean_gradient: float
    max_gradient: float

    mean_curvature: float
    max_curvature: float

    # -----------------------------------------
    # Multi-scale Geometry
    # -----------------------------------------

    scale: int = 0

    # -----------------------------------------
    # Confidence
    # -----------------------------------------

    confidence: float = 1.0

    # =================================================
    # Derived Properties
    # =================================================

    @property
    def length(self):
        """
        Length of the event.
        """
        return self.end - self.start

    @property
    def duration(self):
        """
        Alias for length.
        """
        return self.length

    @property
    def center(self):
        """
        Center location of the event.
        """
        return (self.start + self.end) // 2

    # =================================================

    def __str__(self):

        return (
            f"{self.kind}"
            f"[{self.start}:{self.end}]"
        )

    def __repr__(self):

        return (
            "GeometryEvent("
            f"kind='{self.kind}', "
            f"start={self.start}, "
            f"end={self.end}, "
            f"length={self.length})"
        )


# =====================================================
# Geometry Sequence
# =====================================================

@dataclass
class GeometrySequence:
    """
    Ordered collection of GeometryEvents.

    GeometrySequence is analogous to a token
    stream in NLP. It forms the intermediate
    representation of the Sketch Graph.
    """

    events: List[GeometryEvent] = field(default_factory=list)

    # =================================================
    # Container Interface
    # =================================================

    def append(self, event: GeometryEvent):

        self.events.append(event)

    def extend(self, events: List[GeometryEvent]):

        self.events.extend(events)

    def clear(self):

        self.events.clear()

    # =================================================

    def __len__(self):

        return len(self.events)

    @property
    def size(self):

        return len(self.events)

    def __iter__(self):

        return iter(self.events)

    def __getitem__(self, index):

        return self.events[index]

    # =================================================
    # Queries
    # =================================================

    @property
    def kinds(self):

        return [event.kind for event in self.events]

    @property
    def centers(self):

        return [event.center for event in self.events]

    def filter(self, kind):

        """
        Return all events of a given type.
        """

        return [
            event
            for event in self.events
            if event.kind == kind
        ]

    # =================================================
    # Visualization
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
            f"{self.size} events)"
        )
