import numpy as np


class EventDetector:

    def __init__(self, signal):

        self.signal = np.asarray(signal)

        self.events = []

    def detect(self):

        return self.events
