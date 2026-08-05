"""
Width signature utilities.

This module provides functions for

1. Computing the width signature from
   left and right garment boundaries.

2. Parameterizing (normalizing) the
   signature onto a common geometric domain.
"""

import numpy as np

from scipy.interpolate import interp1d


# =====================================================
# Width Signature
# =====================================================

def width_signature(
    left_boundary,
    right_boundary
):
    """
    Compute garment width at every row.
    """

    left_boundary = np.asarray(left_boundary)
    right_boundary = np.asarray(right_boundary)

    return right_boundary - left_boundary


# =====================================================
# Signature Normalization
# =====================================================

def normalize_signature(
    signature,
    n_samples=1024
):
    """
    Parameterize a width signature onto a
    common geometric domain.

    Every garment is represented by the same
    number of samples irrespective of image
    resolution.
    """

    signature = np.asarray(signature)

    x_old = np.linspace(
        0,
        1,
        len(signature)
    )

    x_new = np.linspace(
        0,
        1,
        n_samples
    )

    interpolator = interp1d(
        x_old,
        signature,
        kind="cubic"
    )

    return interpolator(x_new)
