"""
Garment abstraction for WeaveAI.

Garment is responsible for orchestrating the
complete geometric pipeline while exposing
a simple API to notebooks.

Nothing is computed until it is first needed.
"""

from .geometry import Geometry
from .silhouette import ssa
from .signature import width_signature

from .landmarks import LandmarkDetector
from .segmentation import RegionDetector

from .visualization import (
    plot_width_signature,
    plot_landmarks,
)


class Garment:
    """
    Represents one garment sketch.

    The garment owns the binary image and lazily
    computes all derived geometric information.

    Binary
        ↓
    Silhouette
        ↓
    Width Signature
        ↓
    Geometry
        ↓
    Landmarks
        ↓
    Regions
    """

    def __init__(self, binary):

        # ============================================
        # Original sketch
        # ============================================

        self.binary = binary

        # ============================================
        # Cached geometry
        # ============================================

        self._geometry = None

        self.left_boundary = None
        self.right_boundary = None

        self._signature = None

        self._landmarks = None
        self._regions = None

    # ==================================================
    # Silhouette
    # ==================================================

    def compute_ssa(self):

        if self.left_boundary is None:

            self.left_boundary, self.right_boundary = ssa(
                self.binary
            )

    # ==================================================
    # Signature
    # ==================================================

    def compute_signature(self):

        if self._signature is None:

            self.compute_ssa()

            self._signature = width_signature(
                self.left_boundary,
                self.right_boundary
            )

        return self._signature

    @property
    def signature(self):

        return self.compute_signature()

    # ==================================================
    # Geometry
    # ==================================================

    def compute_geometry(self):

        if self._geometry is None:

            geometry = Geometry()

            geometry.compute(self.binary)

            self._geometry = geometry

        return self._geometry

    @property
    def geometry(self):

        return self.compute_geometry()

    # ==================================================
    # Landmarks
    # ==================================================

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

    # ==================================================
    # Regions
    # ==================================================

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

    # ==================================================
    # Visualization
    # ==================================================

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

    # ==================================================
    # Summary
    # ==================================================

    def summary(self):

        print("Garment")
        print("-------")
        print(f"Signature Length : {len(self.signature)}")
        print(f"Events           : {len(self.geometry.sequence)}")
        print(f"Landmarks        : {len(self.landmarks)}")
        print(f"Regions          : {len(self.regions)}")
