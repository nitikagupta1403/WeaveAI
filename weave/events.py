import numpy as np

@dataclass
class GeometryEvent:

    kind: str

    start: int
    end: int

    length: int

    amplitude: float

    mean_gradient: float

    max_gradient: float

    curvature: float

    scale: int

    confidence: float = 1.0

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
