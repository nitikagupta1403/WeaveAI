import cv2
import numpy as np


def detect_boundaries(binary):
    """
    Extract left and right garment boundaries
    from a binary sketch.
    """

    height, width = binary.shape

    left = []
    right = []

    for y in range(height):

        xs = np.where(binary[y] > 0)[0]

        if len(xs) == 0:
            continue

        left.append((xs.min(), y))
        right.append((xs.max(), y))

    return np.array(left), np.array(right)
