"""
Garment abstraction for WeaveAI.

Garment orchestrates the complete symbolic
geometry pipeline.

Binary
    ↓
Silhouette
    ↓
Width Signature
    ↓
Candidate Events
    ↓
Persistence Analysis
    ↓
GeometrySequence
    ↓
Geometry
"""

from dataclasses import replace

from .geometry import Geometry

from .silhouette import ssa
from .signature import width_signature

from .parser.candidate import CandidateDetector
from .parser.persistence import PersistenceAnalyzer

from .landmarks import LandmarkDetector
from .segmentation import RegionDetector

from .visualization import (
    plot_width_signature,
    plot_landmarks,
)


class Garment:
    """
    Represents one garment sketch.

    All derived symbolic representations are
    computed lazily and cached.
    """

    def __init__(self, binary, name=None):

        self.binary = binary
        self.name = name

        # ==========================================
        # Silhouette
        # ==========================================

        self.left_boundary = None
        self.right_boundary = None

        # ==========================================
        # Cached representations
        # ==========================================

        self._signature = None
        self._geometry = None

        self._landmarks = None
        self._regions = None

    # =================================================
    # Silhouette
    # =================================================

    def compute_ssa(self):

        if self.left_boundary is None:

            self.left_boundary, self.right_boundary = ssa(
                self.binary
            )

    # =================================================
    # Width Signature
    # =================================================

    def compute_signature(self):

        if self._signature is None:

            self.compute_ssa()

            self._signature = width_signature(
                self.left_boundary,
                self.right_boundary,
            )

        return self._signature

    @property
    def signature(self):

        return self.compute_signature()

    # =================================================
    # Symbolic Geometry
    # =================================================

    def compute_geometry(self):

        if self._geometry is not None:
            return self._geometry

        geometry = Geometry()

        geometry.signature = self.signature

        # ------------------------------------------
        # Candidate Detection
        # ------------------------------------------

        candidates = CandidateDetector(
            self.signature
        ).detect()

        # ------------------------------------------
        # Persistence Analysis
        # ------------------------------------------

        sequence = PersistenceAnalyzer(
            candidates
        ).analyze()

        # ------------------------------------------
        # Assign garment + event ids
        # ------------------------------------------

        sequence.garment = self.name

        sequence.events = [

            replace(

                event,

                garment_id=self.name,

                event_id=f"{self.name}_{i}"

            )

            for i, event in enumerate(sequence)

        ]

        geometry.sequence = sequence

        self._geometry = geometry

        return geometry

    @property
    def geometry(self):

        return self.compute_geometry()

    # =================================================
    # Landmarks
    # =================================================

    def compute_landmarks(self):

        if self._landmarks is None:

            detector = LandmarkDetector(
                self.signature
            )

            self._landmarks = detector.detect()

        return self._landmarks

    @property
    def landmarks(self):

        return self.compute_landmarks()

    # =================================================
    # Regions
    # =================================================

    def compute_regions(self):

        if self._regions is None:

            detector = RegionDetector(
                self.signature,
                self.landmarks,
            )

            self._regions = detector.detect()

        return self._regions

    @property
    def regions(self):

        return self.compute_regions()

    # =================================================
    # Visualization
    # =================================================

    def plot_signature(self):

        plot_width_signature(
            self.signature
        )

    def plot_landmarks(self):

        plot_landmarks(
            self.signature,
            self.landmarks,
            regions=self.regions,
        )

    # =================================================
    # Summary
    # =================================================

    def summary(self):

        print("Garment")
        print("----------------------")
        print(f"Name             : {self.name}")
        print(f"Signature Length : {len(self.signature)}")
        print(f"Events           : {len(self.geometry)}")
        print(f"Landmarks        : {len(self.landmarks)}")
        print(f"Regions          : {len(self.regions)}")
