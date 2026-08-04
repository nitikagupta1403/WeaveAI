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

    def detect_rises(self, threshold=0.5):
    
        gradient = self.gradient
    
        inside = False
    
        start = 0
    
        for i, g in enumerate(gradient):
    
            if g > threshold and not inside:
    
                start = i
                inside = True
    
            elif g <= threshold and inside:
    
                self.events.append(
    
                    GeometryEvent(
    
                        kind="rise",
    
                        start=start,
    
                        end=i,
    
                        strength=self.signal[i] - self.signal[start]
                    )
                )
    
                inside = False
