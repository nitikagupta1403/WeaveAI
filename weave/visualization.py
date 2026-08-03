import matplotlib.pyplot as plt
import numpy as np


def plot_width_signature(signature):

    plt.figure(figsize=(5,10))

    plt.plot(signature,
             np.arange(len(signature)))

    plt.gca().invert_yaxis()

    plt.xlabel("Width (pixels)")
    plt.ylabel("Height")

    plt.title("Garment Width Signature")

    plt.show()
