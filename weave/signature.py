import numpy as np


def width_signature(left_boundary,
                    right_boundary):

    signature = []

    for left, right in zip(left_boundary,
                           right_boundary):

        signature.append(
            right[0]-left[0]
        )

    return np.array(signature)
