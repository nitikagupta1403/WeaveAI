import numpy as np

from .events import (
    GeometryEvent,
    GeometrySequence,
    RISE,
    FALL,
    PLATEAU
)


class GeometryParser:
    """
    Converts a continuous geometric signal
    into a GeometrySequence.

    Parser v1 partitions the signal using
    gradient sign changes. It serves as a
    baseline implementation for future
    persistence-based parsing.
    """

    def __init__(self, signal):

        self.signal = np.asarray(signal)

        self.gradient = np.gradient(self.signal)

        self.curvature = np.gradient(self.gradient)

    # =====================================================
    # Main API
    # =====================================================

    def parse(self):

        sequence = GeometrySequence()

        boundaries = self.find_boundaries()

        for start, end in zip(
            boundaries[:-1],
            boundaries[1:]
        ):

            if end <= start:
                continue

            event = self.build_event(start, end)

            sequence.append(event)

        return sequence

    # =====================================================
    # Boundary Detection
    # =====================================================

    def find_boundaries(self):
        """
        Detect candidate boundaries by
        observing changes in gradient sign.

        This is a simple baseline method.
        Future versions will replace this
        with persistence-based partitioning.
        """

        boundaries = [0]

        for i in range(len(self.gradient) - 1):

            if np.sign(self.gradient[i]) != np.sign(self.gradient[i + 1]):

                boundaries.append(i)

        boundaries.append(len(self.signal) - 1)

        return boundaries

    # =====================================================
    # Event Construction
    # =====================================================

    def build_event(self, start, end):
        """
        Construct one GeometryEvent from
        a signal interval.
        """

        signal = self.signal[start:end + 1]

        gradient = self.gradient[start:end + 1]

        curvature = self.curvature[start:end + 1]

        mean_gradient = float(np.mean(gradient))

        # ----------------------------------------
        # Event Type
        # ----------------------------------------

        eps = 1e-6

        if mean_gradient > eps:

            kind = RISE

        elif mean_gradient < -eps:

            kind = FALL

        else:

            kind = PLATEAU

        # ----------------------------------------
        # Build Event
        # ----------------------------------------

        return GeometryEvent(

            kind=kind,

            start=start,

            end=end,

            amplitude=float(signal[-1] - signal[0]),

            mean_gradient=mean_gradient,

            max_gradient=float(
                np.max(np.abs(gradient))
            ),

            mean_curvature=float(
                np.mean(curvature)
            ),

            max_curvature=float(
                np.max(np.abs(curvature))
            )
        )
