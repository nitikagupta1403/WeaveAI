"""
Corpus-level statistics for the WeaveAI Sketch Graph.

Signal
    ↓
CandidateEvent
    ↓
GeometryEvent
    ↓
GeometrySequence
    ↓
EventStatistics

This module aggregates GeometrySequences from
many garments and constructs the statistical
corpus used for

    • descriptive statistics
    • visualization
    • clustering
    • grammar discovery
    • semantic learning
"""

from collections import Counter

import numpy as np
import pandas as pd

from .events import GeometrySequence


# =====================================================
# Event Statistics
# =====================================================

class EventStatistics:
    """
    Build a statistical corpus from many garments.

    Each GeometryEvent becomes one row of the
    event dataframe.
    """

    def __init__(self):

        self.garment_names = []
        self.signatures = []
        self.sequences = []

        self.df = None

    # =================================================
    # Add one garment
    # =================================================

    def add(
        self,
        garment_name,
        signature,
        sequence: GeometrySequence,
    ):

        self.garment_names.append(garment_name)
        self.signatures.append(signature)
        self.sequences.append(sequence)

    # =================================================
    # Build dataframe
    # =================================================

    def build(self):

        records = []

        for garment_name, signature, sequence in zip(

            self.garment_names,
            self.signatures,
            self.sequences,

        ):

            garment_height = len(signature)

            garment_width = float(np.max(np.abs(signature)))

            if garment_width == 0:
                garment_width = 1.0

            for event_index, event in enumerate(sequence):

                records.append({

                    # ---------------------------------
                    # Identity
                    # ---------------------------------

                    "event_id":
                        f"{garment_name}_{event_index}",

                    "garment":
                        garment_name,

                    "event_index":
                        event_index,

                    # ---------------------------------
                    # Symbol
                    # ---------------------------------

                    "kind":
                        event.kind,

                    # ---------------------------------
                    # Position
                    # ---------------------------------

                    "start":
                        event.start,

                    "end":
                        event.end,

                    "center":
                        event.center,

                    "relative_position":
                        event.center / garment_height,

                    # ---------------------------------
                    # Geometry
                    # ---------------------------------

                    "length":
                        event.length,

                    "length_ratio":
                        event.length / garment_height,

                    "amplitude":
                        event.amplitude,

                    "amplitude_ratio":
                        abs(event.amplitude) / garment_width,

                    # ---------------------------------
                    # Differential Geometry
                    # ---------------------------------

                    "mean_gradient":
                        event.mean_gradient,

                    "max_gradient":
                        event.max_gradient,

                    "mean_curvature":
                        event.mean_curvature,

                    "max_curvature":
                        event.max_curvature,

                })

        self.df = pd.DataFrame(records)

        return self.df

    # =================================================
    # Summary
    # =================================================

    def summary(self):

        return self.df.describe()

    # =================================================
    # Event Counts
    # =================================================

    def event_counts(self):

        return Counter(self.df["kind"])

    # =================================================
    # Transition Counts
    # =================================================

    def transition_counts(self):

        transitions = Counter()

        for sequence in self.sequences:

            for a, b in zip(
                sequence.kinds[:-1],
                sequence.kinds[1:]
            ):

                transitions[(a, b)] += 1

        return transitions

    # =================================================
    # Feature Matrix
    # =================================================

    def feature_columns(self):

        return [

            "length_ratio",
            "amplitude_ratio",
            "relative_position",

            "mean_gradient",
            "max_gradient",

            "mean_curvature",
            "max_curvature",

        ]

    def feature_matrix(self):

        return self.df[
            self.feature_columns()
        ].to_numpy()

    # =================================================
    # Export
    # =================================================

    def export_csv(self, filename):

        self.df.to_csv(
            filename,
            index=False,
        )
