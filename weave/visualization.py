import matplotlib.pyplot as plt
import numpy as np


def plot_width_signature(signature):
    """
    Plot garment width signature.
    """

    plt.figure(figsize=(5, 10))

    plt.plot(
        signature,
        np.arange(len(signature)),
        linewidth=2
    )

    plt.gca().invert_yaxis()

    plt.xlabel("Width (pixels)")
    plt.ylabel("Height")
    plt.title("Garment Width Signature")

    plt.grid(alpha=0.3)

    plt.show()


def plot_landmarks(
    signal,
    landmarks,
    analyzer=None
):
    """
    Visualize detected garment landmarks.

    Parameters
    ----------
    signal : ndarray
        Width signature.

    landmarks : dict
        Dictionary returned by LandmarkDetector.

    analyzer : SignalAnalyzer, optional
        If provided, local maxima and minima
        are also displayed.
    """

    y = np.arange(len(signal))

    plt.figure(figsize=(6, 10))

    # -------------------------------------------------
    # Width signal
    # -------------------------------------------------

    plt.plot(
        signal,
        y,
        color="black",
        linewidth=2,
        label="Width Signature"
    )

    # -------------------------------------------------
    # Signal extrema
    # -------------------------------------------------

    if analyzer is not None:

        plt.scatter(
            signal[analyzer.local_maxima],
            analyzer.local_maxima,
            color="red",
            s=40,
            label="Peaks"
        )

        plt.scatter(
            signal[analyzer.local_minima],
            analyzer.local_minima,
            color="blue",
            s=40,
            label="Valleys"
        )

    # -------------------------------------------------
    # Landmarks
    # -------------------------------------------------

    colors = {
        "shoulder": "red",
        "waist": "blue",
        "hem": "green"
    }

    for name, landmark in landmarks.items():

        plt.scatter(
            landmark.width,
            landmark.y,
            color=colors.get(name, "black"),
            s=120,
            edgecolors="white",
            linewidth=1.5,
            zorder=10
        )

        plt.text(
            landmark.width + 8,
            landmark.y,
            name.capitalize(),
            fontsize=10,
            weight="bold",
            va="center"
        )

    plt.gca().invert_yaxis()

    plt.xlabel("Width (pixels)")
    plt.ylabel("Height")
    plt.title("Detected Garment Landmarks")

    plt.grid(alpha=0.3)
    plt.legend()

    plt.show()
