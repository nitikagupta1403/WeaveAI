import numpy as np
from scipy.signal import find_peaks


class SignalAnalyzer:
    """
    Generic analyzer for one-dimensional geometric signals.

    Examples
    --------
    - Width signal
    - Curvature signal
    - Boundary angle signal
    """

    def __init__(self, signal):

        # Original signal
        self.signal = np.asarray(signal, dtype=float)

        # Processed signal
        self.smoothed = None

        # Derivatives
        self.gradient = None
        self.curvature = None

        # Features
        self.local_maxima = None
        self.local_minima = None
        self.zero_crossings = None

    # =====================================================
    # Smoothing
    # =====================================================

    def smooth(self, window=7):

        kernel = np.ones(window) / window

        self.smoothed = np.convolve(
            self.signal,
            kernel,
            mode="same"
        )

        return self.smoothed

    # =====================================================
    # First Derivative
    # =====================================================

    def compute_gradient(self):

        if self.smoothed is None:
            self.smooth()

        self.gradient = np.gradient(self.smoothed)

        return self.gradient

    # =====================================================
    # Second Derivative (Curvature)
    # =====================================================

    def compute_curvature(self):

        if self.gradient is None:
            self.compute_gradient()

        self.curvature = np.gradient(self.gradient)

        return self.curvature

    # =====================================================
    # Peak Detection
    # =====================================================

    def detect_local_maxima(
        self,
        prominence=10,
        distance=40
    ):

        if self.smoothed is None:
            self.smooth()

        peaks, _ = find_peaks(
            self.smoothed,
            prominence=prominence,
            distance=distance
        )

        self.local_maxima = peaks

        return peaks

    def detect_local_minima(
        self,
        prominence=10,
        distance=40
    ):

        if self.smoothed is None:
            self.smooth()

        valleys, _ = find_peaks(
            -self.smoothed,
            prominence=prominence,
            distance=distance
        )

        self.local_minima = valleys

        return valleys

    # =====================================================
    # Zero Crossings
    # =====================================================

    def detect_zero_crossings(self):

        if self.gradient is None:
            self.compute_gradient()

        self.zero_crossings = np.where(
            np.diff(np.sign(self.gradient))
        )[0]

        return self.zero_crossings

    # =====================================================
    # Normalize
    # =====================================================

    def normalize(self):

        s = self.signal

        self.signal = (
            s - s.min()
        ) / (
            s.max() - s.min()
        )

        return self.signal

    # =====================================================
    # Complete Analysis
    # =====================================================

    def analyze(
        self,
        window=7,
        prominence=10,
        distance=40
    ):

        self.smooth(window)

        self.compute_gradient()

        self.compute_curvature()

        self.detect_local_maxima(
            prominence,
            distance
        )

        self.detect_local_minima(
            prominence,
            distance
        )

        self.detect_zero_crossings()

        return self
