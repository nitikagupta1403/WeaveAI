"""
Geometry Grammar.

Grammar operates on GeometrySequences and
discovers higher-level geometric motifs.

Grammar remains garment-independent.
Semantic interpretation belongs to a later stage.
"""

from dataclasses import dataclass
from typing import List

from .events import GeometryEvent, GeometrySequence

@dataclass
class GeometryMotif:
    """
    A GeometryMotif is a meaningful arrangement
    of GeometryEvents.
    """

    kind: str

    events: List[GeometryEvent]

    confidence: float = 1.0

    @property
    def start(self):

        return self.events[0].start

    @property
    def end(self):

        return self.events[-1].end

    @property
    def length(self):

        return self.end - self.start

    def __repr__(self):

        return (
            f"GeometryMotif("
            f"{self.kind}, "
            f"{len(self.events)} events)"
        )

  class GeometryGrammar:
    """
    Converts GeometryEvents into
    higher-level geometric motifs.
    """

    def __init__(self, sequence):

        self.sequence = sequence

        self.motifs = []

    def parse(self):

        return self.motifs
