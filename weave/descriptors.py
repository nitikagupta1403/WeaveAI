from dataclasses import dataclass

import numpy as np


@dataclass
class Descriptor:
    """
    Numerical description of one garment region.
    """

    name: str

    length: int

    mean_width: float
    min_width: float
    max_width: float

    width_std: float

    area: float

    expansion: float

    average_slope: float
    maximum_slope: float


class RegionDescriptor:
    """
    Computes geometric descriptors
    for one garment region.
    """

    def __init__(self, signature, region):

        self.signature = np.asarray(signature)

        self.region = region

    # =====================================================
    # Helpers
    # =====================================================

    def signal(self):

        return self.signature[
            self.region.start:self.region.end
        ]

    # =====================================================
    # Measurements
    # =====================================================

    def compute(self):

        s = self.signal()

        gradient = np.gradient(s)

        return Descriptor(

            name=self.region.name,

            length=len(s),

            mean_width=float(np.mean(s)),
            min_width=float(np.min(s)),
            max_width=float(np.max(s)),

            width_std=float(np.std(s)),

            area=float(np.sum(s)),

            expansion=float(
                s[-1] / s[0]
            ),

            average_slope=float(
                np.mean(gradient)
            ),

            maximum_slope=float(
                np.max(np.abs(gradient))
            )
        )
