import numpy as np


class EventDetector:
    """
    Detect primitive geometric events
    from a 1D geometric signal.
    """

    def __init__(self, signal):

        self.signal = np.asarray(signal)

        self.gradient = np.gradient(self.signal)

        self.curvature = np.gradient(self.gradient)

        self.events = []

    def detect(self):

        self.events = []

        return self.events
