import numpy as np

from ..events import CandidateEvent


class CandidateDetector:
    """
    Detect candidate geometric events directly
    from a one-dimensional geometric signal.

    Candidate detection intentionally over-segments
    the signal. The resulting CandidateEvents are
    later validated and merged by the
    PersistenceAnalyzer.
    """

    # =====================================================
    # Initialization
    # =====================================================

    def __init__(self, signal):

        self.signal = np.asarray(signal, dtype=float)

        self.gradient = np.gradient(self.signal)

        self.curvature = np.gradient(self.gradient)

    # =====================================================
    # Main API
    # =====================================================

    def detect(self):

        candidates = []

        boundaries = self.find_boundaries()

        for start, end in zip(
            boundaries[:-1],
            boundaries[1:]
        ):

            if end <= start:
                continue

            candidate = self.build_candidate(
                start,
                end
            )

            candidates.append(candidate)

        return candidates

    # =====================================================
    # Candidate Boundary Detection
    # =====================================================

    def find_boundaries(self):
        """
        Detect candidate event boundaries using
        gradient sign changes.

        This deliberately over-segments the signal.
        Later stages merge persistent regions.
        """

        boundaries = [0]

        for i in range(len(self.gradient) - 1):

            if np.sign(self.gradient[i]) != np.sign(self.gradient[i + 1]):

                boundaries.append(i)

        boundaries.append(len(self.signal) - 1)

        return boundaries

    # =====================================================
    # Candidate Construction
    # =====================================================

    def build_candidate(
        self,
        start,
        end
    ):
        """
        Construct one CandidateEvent from a
        signal interval.
        """

        signal = self.signal[start:end + 1]

        gradient = self.gradient[start:end + 1]

        curvature = self.curvature[start:end + 1]

        mean_gradient = float(
            np.mean(gradient)
        )

        eps = 1e-6

        if mean_gradient > eps:

            kind = "rise"

        elif mean_gradient < -eps:

            kind = "fall"

        else:

            kind = "plateau"

        return CandidateEvent(

            kind=kind,

            start=start,
            end=end,

            length=end - start,

            amplitude=float(
                signal[-1] - signal[0]
            ),

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
