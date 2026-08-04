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
