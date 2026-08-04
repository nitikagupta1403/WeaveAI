from dataclasses import dataclass
import numpy as np

from .signals import SignalAnalyzer


@dataclass
class Landmark:
    """
    Represents one semantic garment landmark.
    """
    name: str
    x: float
    y: int
    width: float


class LandmarkDetector:
    """
    Detect semantic garment landmarks from
    one-dimensional geometric signals.
    """

    def __init__(self, signature):

        self.signature = np.asarray(signature)

        self.signals = SignalAnalyzer(
            self.signature
        ).analyze()

        self.landmarks = {}

    # =====================================================
    # Generic geometric queries
    # =====================================================

    def find_peak(
        self,
        start=0.0,
        end=1.0,
        strategy="largest"
    ):

        peaks = self.signals.local_maxima

        n = len(self.signature)

        start = int(start * n)
        end = int(end * n)

        peaks = peaks[
            (peaks >= start) &
            (peaks <= end)
        ]

        if len(peaks) == 0:
            return None

        if strategy == "first":
            return peaks[0]

        if strategy == "last":
            return peaks[-1]

        if strategy == "largest":
            return peaks[np.argmax(self.signature[peaks])]

        raise ValueError(f"Unknown strategy: {strategy}")

    def find_valley(
        self,
        start=0.0,
        end=1.0,
        strategy="first"
    ):

        valleys = self.signals.local_minima

        n = len(self.signature)

        start = int(start * n)
        end = int(end * n)

        valleys = valleys[
            (valleys >= start) &
            (valleys <= end)
        ]

        if len(valleys) == 0:
            return None

        if strategy == "first":
            return valleys[0]

        if strategy == "last":
            return valleys[-1]

        if strategy == "deepest":
            return valleys[np.argmin(self.signature[valleys])]

        raise ValueError(f"Unknown strategy: {strategy}")

    # =====================================================
    # Semantic landmarks
    # =====================================================

    def detect_shoulder(self):

        y = self.find_peak(
            start=0.05,
            end=0.35,
            strategy="largest"
        )

        return Landmark(
            "shoulder",
            self.signature[y],
            y,
            self.signature[y]
        )

    def detect_waist(self):

        shoulder = self.detect_shoulder().y

        y = self.find_valley(
            start=shoulder / len(self.signature),
            end=0.60,
            strategy="first"
        )

        return Landmark(
            "waist",
            self.signature[y],
            y,
            self.signature[y]
        )

    def detect_hem(self):

        y = self.find_peak(
            start=0.70,
            end=1.00,
            strategy="largest"
        )

        return Landmark(
            "hem",
            self.signature[y],
            y,
            self.signature[y]
        )

    # =====================================================
    # Main API
    # =====================================================

    def detect(self):

        self.landmarks = {
            "shoulder": self.detect_shoulder(),
            "waist": self.detect_waist(),
            "hem": self.detect_hem(),
        }

        return self.landmarks
