import numpy as np

from .events import (
    GeometryEvent,
    GeometrySequence
)


class GeometryParser:
    """
    Converts a continuous geometric signal
    into a sequence of GeometryEvents.
    """

    def __init__(self, signal):

        self.signal = np.asarray(signal)

        self.gradient = np.gradient(self.signal)

        self.curvature = np.gradient(self.gradient)

    def parse(self):

        sequence = GeometrySequence()

        boundaries = self.find_boundaries()

        for start, end in zip(
            boundaries[:-1],
            boundaries[1:]
        ):

            sequence.append(
                self.build_event(start, end)
            )

        return sequence
      def find_boundaries(self):

        gradient = self.gradient
    
        boundaries = [0]
    
        for i in range(len(gradient)-1):
    
            if np.sign(
                gradient[i]
            ) != np.sign(
                gradient[i+1]
            ):
    
                boundaries.append(i)
    
        boundaries.append(
            len(self.signal)-1
        )
    
        return boundaries

      def build_event(
          self,
          start,
          end
      ):
      
          g = self.gradient[start:end+1]
      
          c = self.curvature[start:end+1]
      
          s = self.signal[start:end+1]
      
          mean_gradient = np.mean(g)
      
          if mean_gradient > 0:
      
              kind = "rise"
      
          elif mean_gradient < 0:
      
              kind = "fall"
      
          else:
      
              kind = "plateau"
      
          return GeometryEvent(
      
              kind=kind,
      
              start=start,
      
              end=end,
      
              length=end-start,
      
              amplitude=float(
                  s[-1]-s[0]
              ),
      
              mean_gradient=float(
                  np.mean(g)
              ),
      
              max_gradient=float(
                  np.max(np.abs(g))
              ),
      
              mean_curvature=float(
                  np.mean(c)
              ),
      
              max_curvature=float(
                  np.max(np.abs(c))
              )
          )
