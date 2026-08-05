import numpy as np

from ..events import CandidateEvent


class CandidateDetector:
    """
    Detects candidate geometric events
    directly from the signal.
    """

    def __init__(self, signal):

        self.signal = np.asarray(signal)

        self.gradient = np.gradient(
            self.signal
        )

        self.curvature = np.gradient(
            self.gradient
        )

    def detect(self):

        candidates = []
    
        boundaries = self.find_boundaries()
    
        for start, end in zip(
            boundaries[:-1],
            boundaries[1:]
        ):
    
            candidates.append(
                self.build_candidate(
                    start,
                    end
                )
            )
    
        return candidates
