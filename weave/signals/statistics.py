from dataclasses import dataclass

import numpy as np
from scipy.signal import find_peaks


@dataclass
class SignalStatistics:

    local_maxima: np.ndarray
    local_minima: np.ndarray


def analyze(signal):
    """
    Compute simple statistics of a 1D signal.
    """

    signal = np.asarray(signal)

    maxima, _ = find_peaks(signal)

    minima, _ = find_peaks(-signal)

    return SignalStatistics(
        local_maxima=maxima,
        local_minima=minima
    )
