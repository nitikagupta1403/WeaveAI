from .silhouette import ssa
from .signature import width_signature
from .visualization import plot_width_signature


class Garment:

    def __init__(self, binary):

        self.binary = binary

        self.left_boundary = None
        self.right_boundary = None

        self.signature = None

    def compute_ssa(self):

        self.left_boundary, self.right_boundary = ssa(
            self.binary
        )

        return self

    def compute_signature(self):

        if self.left_boundary is None:
            self.compute_ssa()

        self.signature = width_signature(
            self.left_boundary,
            self.right_boundary
        )

        return self

    def plot_signature(self):

        if self.signature is None:
            self.compute_signature()

        plot_width_signature(self.signature)

        return self
