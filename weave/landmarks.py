from dataclasses import dataclass
import numpy as np

@dataclass
class Landmark:
    name: str
    x: float
    y: float
    width: float
  


class LandmarkDetector:

    def __init__(self, signature):

        self.signature = np.asarray(signature)

        self.dy = np.gradient(self.signature)

        self.d2y = np.gradient(self.dy)

        self.landmarks = {}

    def shoulder(self):
  
      n = len(self.signature)
  
      search = self.signature[:int(0.25*n)]
  
      y = np.argmax(search)
  
      self.landmarks["shoulder"] = Landmark(
          "shoulder",
          self.signature[y],
          y,
          self.signature[y]
      )

    def waist(self):

        n = len(self.signature)
    
        start = int(0.20*n)
    
        end = int(0.50*n)
    
        y = start + np.argmin(self.signature[start:end])
    
        self.landmarks["waist"] = Landmark(
            "waist",
            self.signature[y],
            y,
            self.signature[y]
        )

    def hem(self):

        y = np.argmax(self.signature)
    
        self.landmarks["hem"] = Landmark(
            "hem",
            self.signature[y],
            y,
            self.signature[y]
        )

    def detect(self):

        self.shoulder()
    
        self.waist()
    
        self.hem()
    
        return self.landmarks
