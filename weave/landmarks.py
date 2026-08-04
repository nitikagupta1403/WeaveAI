from dataclasses import dataclass

import numpy as np

from .signals import SignalAnalyzer

UPPER_REGION = 0.30


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
    Detect garment landmarks from geometric signals.
    """

    def __init__(self, signature):

        self.signature = np.asarray(signature)

        self.signals = SignalAnalyzer(
            self.signature
        ).analyze()

        self.landmarks = {}

    def find_first_major_peak(self):
        """
        Returns the first major peak in the upper
        part of the garment.
        """
    
        peaks = self.signals.local_maxima
    
        if len(peaks) == 0:
            return None
    
        # Search only in upper 30% of garment
        limit = int(UPPER_REGION * len(self.signature))
    
        candidates = peaks[peaks < limit]
    
        if len(candidates) == 0:
            return peaks[0]
    
        return candidates[0]

    def detect_shoulder(self):

        y = self.find_first_major_peak()
    
        if y is None:
            return None
    
        return Landmark(
            name="shoulder",
            x=self.signature[y],
            y=y,
            width=self.signature[y]
        )

    def find_first_major_valley(self):
        """
        Returns the first major valley after
        the shoulder.
        """
    
        shoulder = self.find_first_major_peak()
    
        valleys = self.signals.local_minima
    
        candidates = valleys[valleys > shoulder]
    
        if len(candidates) == 0:
            return np.argmin(self.signature)

        return candidates[0]

    def detect_waist(self):

        y = self.find_first_major_valley()
    
        return Landmark(
            name="waist",
            x=self.signature[y],
            y=y,
            width=self.signature[y]
        )
        
    def find_terminal_peak(self):

        return np.argmax(self.signature)
    def detect_hem(self):

        y = self.find_terminal_peak()
    
        return Landmark(
            name="hem",
            x=self.signature[y],
            y=y,
            width=self.signature[y]
        )
    def detect(self):

        self.landmarks = {
    
            "shoulder": self.detect_shoulder(),
    
            "waist": self.detect_waist(),
    
            "hem": self.detect_hem()
    
        }
    
        return self.landmarks
