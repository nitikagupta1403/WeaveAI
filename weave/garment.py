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
    Represents one garment sketch and all geometric
    information derived from it.
    """

    def __init__(self, binary):

        # ==================================================
        # Original Sketch
        # ==================================================

        self.binary = binary

        # ==================================================
        # Global Geometry
        # ==================================================

        self.geometry = Geometry()

        # ==================================================
        # Silhouette
        # ==================================================

        self.left_boundary = None
        self.right_boundary = None

        # ==================================================
        # Width Signature
        # ==================================================

        self.signature = None

        # ==================================================
        # Landmarks
        # ==================================================

        self.landmark_detector = None
        self.landmarks = None

        # ==================================================
        # Regions
        # ==================================================

        self.region_detector = None
        self.regions = None

    # ==================================================
    # Geometry
    # ==================================================

    def compute_geometry(self):

        self.geometry.compute(self.binary)

    # ==================================================
    # Silhouette
    # ==================================================

    def compute_ssa(self):

        self.left_boundary, self.right_boundary = ssa(
            self.binary
        )

    # ==================================================
    # Width Signature
    # ==================================================

    def compute_signature(self):

        if self.left_boundary is None:
            self.compute_ssa()

        self.signature = width_signature(
            self.left_boundary,
            self.right_boundary
        )

    # ==================================================
    # Landmarks
    # ==================================================

    def compute_landmarks(self):

        if self.signature is None:
            self.compute_signature()

        self.landmark_detector = LandmarkDetector(
            self.signature
        )

        self.landmarks = self.landmark_detector.detect()

    # ==================================================
    # Regions
    # ==================================================

    def compute_regions(self):

        if self.landmarks is None:
            self.compute_landmarks()

        self.region_detector = RegionDetector(
            self.signature,
            self.landmarks
        )

        self.regions = self.region_detector.detect()

    # ==================================================
    # Visualization
    # ==================================================

    def plot_signature(self):

        if self.signature is None:
            self.compute_signature()

        if self.landmarks is None:

            plot_width_signature(
                self.signature
            )

            return

    def plot_landmarks(
        signal,
        landmarks,
        analyzer=None,
        regions=None
        ):
