from .silhouette import ssa
from .signature import width_signature


class Garment:

    def __init__(self,
                 binary):

        self.binary = binary

        self.left = None
        self.right = None

        self.signature = None

    def compute_ssa(self):

        self.left,\
        self.right = ssa(
            self.binary
        )

    def compute_signature(self):

        self.signature = width_signature(
            self.left,
            self.right
        )
