from dataclasses import dataclass

import numpy as np

from .signals import SignalAnalyzer


@dataclass
class Landmark:

    name: str

    x: float
    y: int

    width: float


class LandmarkDetector:
    """
    Detect semantic garment landmarks from
    geometric signals.
    """

    def __init__(self, signature):

        self.signature = np.asarray(signature)

        self.signals = SignalAnalyzer(
            self.signature
        ).analyze()

        self.landmarks = {}

    def detect(self):

        width = self.signals.signal

        shoulder = self.detect_shoulder(width)

        waist = self.detect_waist(width)

        hem = self.detect_hem(width)

        self.landmarks = {

            "shoulder": shoulder,

            "waist": waist,

            "hem": hem

        }

        return self.landmarks

    def detect_shoulder(self, width):

        search = width[: len(width)//3]

        y = np.argmax(search)

        return Landmark(

            name="shoulder",

            x=width[y],

            y=y,

            width=width[y]

        )

    def detect_waist(self, width):

        shoulder = self.detect_shoulder(width)

        search = width[shoulder.y:]

        y = shoulder.y + np.argmin(search)

        return Landmark(

            name="waist",

            x=width[y],

            y=y,

            width=width[y]

        )

    def detect_hem(self, width):

        search = width[len(width)//2:]

        y = len(width)//2 + np.argmax(search)

        return Landmark(

            name="hem",

            x=width[y],

            y=y,

            width=width[y]

        )
