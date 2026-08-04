from .silhouette import ssa
from .signature import width_signature
from .visualization import plot_width_signature
from .landmarks import LandmarkDetector


class Garment:
    """
    Represents one garment sketch and all geometric
    information derived from it.
    """

    def __init__(self, binary):

        # Original binary sketch
        self.binary = binary

        # -----------------------------
        # Global Geometry
        # -----------------------------
        self.geometry = Geometry()

        # -----------------------------
        # Silhouette
        # -----------------------------
        self.left_boundary = None
        self.right_boundary = None

        # -----------------------------
        # Width Signature
        # -----------------------------
        self.signature = None

        # -----------------------------
        # Landmarks
        # -----------------------------
        self.landmarks = None

    # ===================================================
    # Geometry
    # ===================================================

    def compute_geometry(self):
        self.geometry.compute(self.binary)

    # ===================================================
    # Silhouette
    # ===================================================

    def compute_ssa(self):

        self.left_boundary, self.right_boundary = ssa(
            self.binary
        )

    # ===================================================
    # Width Signature
    # ===================================================

    def compute_signature(self):

        if self.left_boundary is None:
            self.compute_ssa()

        self.signature = width_signature(
            self.left_boundary,
            self.right_boundary
        )

    # ===================================================
    # Landmarks
    # ===================================================

    def compute_landmarks(self):

        if self.signature is None:
            self.compute_signature()

        detector = LandmarkDetector(self.signature)

        self.landmarks = detector.detect()

    # ===================================================
    # Visualization
    # ===================================================

    def plot_signature(self):

        if self.signature is None:
            self.compute_signature()

        plot_width_signature(self.signature)
