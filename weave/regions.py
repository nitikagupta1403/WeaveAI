from dataclasses import dataclass


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

  def detect_bodice(self):

    shoulder = self.landmarks["shoulder"].y

    waist = self.landmarks["waist"].y

    return Region(
        name="bodice",
        start=shoulder,
        end=waist,
        length=waist - shoulder,
        mean_width=np.mean(
            self.signature[shoulder:waist]
        ),
        min_width=np.min(
            self.signature[shoulder:waist]
        ),
        max_width=np.max(
            self.signature[shoulder:waist]
        )
    )
