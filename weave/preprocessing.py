import cv2
import numpy as np


def load_binary(path, threshold=10):
    """
    Load a garment sketch and convert it to binary.
    """

    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        raise FileNotFoundError(path)

    binary = (image > threshold).astype(np.uint8)

    return binary
