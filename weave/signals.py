import numpy as np


class SignalAnalyzer:
    """
    Generic analyzer for one-dimensional geometric signals.

    Examples
    --------
    Width signal
    Curvature signal
    Boundary angle signal
    """

    def __init__(self, signal):

        self.signal = np.asarray(signal, dtype=float)

        self.gradient = None
        self.second_derivative = None

    def smooth(self, window=7):

      kernel = np.ones(window) / window

      self.signal = np.convolve(
          self.signal,
          kernel,
          mode="same"
      )

      return self.signal

    def compute_gradient(self):

        self.gradient = np.gradient(self.signal)
    
        return self.gradient

        def compute_second_derivative(self):

        if self.gradient is None:
            self.compute_gradient()

        self.second_derivative = np.gradient(
            self.gradient
        )

        return self.second_derivative

    def local_maxima(self):

        maxima = []
    
        for i in range(1, len(self.signal)-1):
    
            if (
                self.signal[i] >= self.signal[i-1]
                and
                self.signal[i] >= self.signal[i+1]
            ):
    
                maxima.append(i)

        return maxima

    def local_minima(self):

        minima = []
    
        for i in range(1, len(self.signal)-1):
    
            if (
                self.signal[i] <= self.signal[i-1]
                and
                self.signal[i] <= self.signal[i+1]
            ):
    
                minima.append(i)
    
        return minima

    def zero_crossings(self):

        if self.gradient is None:
            self.compute_gradient()

        zeros = []

        for i in range(len(self.gradient)-1):

            if self.gradient[i] * self.gradient[i+1] < 0:

                zeros.append(i)

        return zeros

    def normalize(self):

        s = self.signal
    
        self.signal = (
            s - s.min()
        ) / (
            s.max() - s.min()
        )
    
        return self.signal

    def analyze(self):
        """
        Complete analysis pipeline.
        """

        self.smooth()
        self.compute_gradient()
        self.compute_second_derivative()

        return self

    
