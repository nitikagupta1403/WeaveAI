import numpy as np
from scipy.signal import find_peaks
DEFAULT_WINDOW = 7
DEFAULT_PROMINENCE = 10
DEFAULT_DISTANCE = 40

class SignalAnalyzer:
    """
    Generic analyzer for one-dimensional geometric signals.

    Examples
    --------
    - Width signal
    - second_derivative signal
    - Boundary angle signal
    """

    def __init__(self, signal):

        # Original signal
        self.signal = np.asarray(signal, dtype=float)

        # Processed signal
        self.smoothed = None

        # Derivatives
        self.gradient = None
        self.second_derivative = None

        # Features
        self.local_maxima = None
        self.local_minima = None
        self.zero_crossings = None

        self.normalized = None

    # =====================================================
    # Smoothing
    # =====================================================

    def smooth(self, window=DEFAULT_WINDOW):

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
    # Second Derivative (second_derivative)
    # =====================================================

    def compute_second_derivative(self):

        if self.gradient is None:
            self.compute_gradient()

        self.second_derivative = np.gradient(self.gradient)

        return self.second_derivative

    # =====================================================
    # Peak Detection
    # =====================================================

    def detect_local_maxima(
        self,
        prominence=DEFAULT_PROMINENCE,
        distance=DEFAULT_DISTANCE
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
        prominence=DEFAULT_PROMINENCE,
        distance=DEFAULT_DISTANCE
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
    
        self.normalized = (
            s - s.min()
        ) / (
            s.max() - s.min()
        )
    
        return self.normalized

    # =====================================================
    # Complete Analysis
    # =====================================================

    def analyze(
        self,
        window=DEFAULT_WINDOW,
        prominence=DEFAULT_PROMINENCE,
        distance=DEFAULT_DISTANCE
    ):

        self.smooth(window)

        self.compute_gradient()
        
        self.compute_second_derivative()
        
        self.detect_local_maxima(
            prominence=prominence,
            distance=distance
        )
        
        self.detect_local_minima(
            prominence=prominence,
            distance=distance
        )
        
        self.detect_zero_crossings()
        
        return self

    def summary(self):

        print("Signal Length :", len(self.signal))
    
        print("Local Maxima  :", len(self.local_maxima))
    
        print("Local Minima  :", len(self.local_minima))
    
        print("Zero Crossings:", len(self.zero_crossings))
