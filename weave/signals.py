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
