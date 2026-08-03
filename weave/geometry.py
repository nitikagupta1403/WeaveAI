import numpy as np


class Geometry:

    """
    Stores global geometric properties of a garment.
    """

    def __init__(self):

        self.xmin = None
        self.xmax = None

        self.ymin = None
        self.ymax = None

        self.width = None
        self.height = None

        self.area = None

        self.aspect_ratio = None

        self.centroid = None

        self.edge_pixels = None

    def compute(self, binary):

        ys, xs = np.where(binary > 0)

        self.xmin = int(xs.min())
        self.xmax = int(xs.max())

        self.ymin = int(ys.min())
        self.ymax = int(ys.max())

        self.width = self.xmax - self.xmin
        self.height = self.ymax - self.ymin

        self.area = self.width * self.height

        self.aspect_ratio = self.width / self.height

        self.centroid = (
            float(xs.mean()),
            float(ys.mean())
        )

        self.edge_pixels = len(xs)
