from dataclasses import dataclass
import numpy as np


@dataclass
class Region:
    """
    One semantic garment region.
    """

    name: str

    start: int
    end: int

    length: int

    mean_width: float
    min_width: float
    max_width: float


class RegionDetector:

    def __init__(
        self,
        signature,
        landmarks
    ):

        self.signature = np.asarray(signature)

        self.landmarks = landmarks

        self.regions = {}
    
    def detect_bodice(self):
    
        shoulder = self.landmarks["shoulder"].y
    
        waist = self.landmarks["waist"].y
    
        region = self.signature[shoulder:waist]
    
        return Region(
            name="bodice",
        
            start=shoulder,
            end=waist,
        
            length=waist - shoulder,
        
            mean_width=float(np.mean(region)),
            min_width=float(np.min(region)),
            max_width=float(np.max(region))
        )

    def detect(self):

        self.regions = {
            "bodice": self.detect_bodice()
        }
    
        return self.regions
