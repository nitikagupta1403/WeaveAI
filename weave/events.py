"""
GeometryEvent is the atomic unit of the
WeaveAI geometric representation.

Every higher-level concept
(landmarks, regions, descriptors, grammar,
garment semantics) must be expressible as
combinations of GeometryEvents.
"""


from dataclasses import dataclass, field


# =====================================================
# Geometry Event
# =====================================================

@dataclass
class GeometryEvent:
    """
    Atomic unit of geometric information.

    A GeometryEvent represents one continuous region
    of homogeneous geometric behaviour in a 1D signal.

    Higher-level concepts such as landmarks,
    garment regions and semantics should be derived
    from GeometryEvents rather than detected directly.
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

    length: int

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

    @property
    def center(self):
        """
        Center of the event.
        """
        return (self.start + self.end) // 2

    def __repr__(self):

        return (
            f"{self.kind}"
            f"(start={self.start}, "
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

    GeometrySequence is analogous to a token stream
    in NLP. It forms the intermediate representation
    of garment geometry.
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
        """
        Returns only the event names.
        """

        return [e.kind for e in self.events]

    @property
    def centers(self):
        """
        Centers of all events.
        """

        return [e.center for e in self.events]

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
