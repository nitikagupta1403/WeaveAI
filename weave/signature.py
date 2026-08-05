from scipy.interpolate import interp1d
import numpy as np


def normalize_signature(
    signature,
    n_samples=1024
):
    """
    Parameterize a width signature onto a
    common geometric domain.

    Every garment is represented by the same
    number of samples irrespective of its
    image resolution.
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

    f = interp1d(
        x_old,
        signature,
        kind="cubic"
    )

    return f(x_new)
