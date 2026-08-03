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

def moving_average(values, window=7):

    kernel = np.ones(window) / window

    return np.convolve(values, kernel, mode="same")

def ssa(binary):

    left_pts, right_pts = detect_boundaries(binary)

    left_x = moving_average(left_pts[:,0])

    right_x = moving_average(right_pts[:,0])

    left_boundary = np.column_stack(
        (left_x, left_pts[:,1])
    )

    right_boundary = np.column_stack(
        (right_x, right_pts[:,1])
    )

    return left_boundary, right_boundary
