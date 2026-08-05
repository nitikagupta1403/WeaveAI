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
Geometry
    ↓
EventStatistics

This module aggregates symbolic Geometry objects
from many garments and constructs the statistical
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

from .geometry import Geometry


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
        self.geometries = []

        self.df = None

    # =================================================
    # Add one garment
    # =================================================

    def add(
        self,
        garment_name: str,
        geometry: Geometry,
    ):

        self.garment_names.append(garment_name)
        self.geometries.append(geometry)

    # =================================================
    # Build dataframe
    # =================================================

    def build(self):

        records = []

        for garment_name, geometry in zip(

            self.garment_names,
            self.geometries,

        ):

            signature = geometry.signature
            sequence = geometry.sequence

            garment_height = len(signature)

            garment_width = float(
                np.max(np.abs(signature))
            )

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
                    # Symbolic
                    # ---------------------------------

                    "kind":
                        event.kind,

                    "primitive":
                        event.primitive,

                    "primitive_family":
                        event.primitive_family,

                    "grammar_role":
                        event.grammar_role,

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

                    # ---------------------------------
                    # Persistence
                    # ---------------------------------

                    "persistence":
                        event.persistence,

                    "strength":
                        event.strength,

                    "confidence":
                        event.confidence,

                    "scale":
                        event.scale,

                })

        self.df = pd.DataFrame(records)

        return self.df

    # =================================================
    # Summary
    # =================================================

    def summary(self):

        return self.df.describe()

    # =================================================
    # Counts
    # =================================================

    def event_counts(self):

        return Counter(
            self.df["kind"]
        )

    def primitive_counts(self):

        return Counter(
            self.df["primitive"]
        )

    def family_counts(self):

        return Counter(
            self.df["primitive_family"]
        )

    # =================================================
    # Grammar Statistics
    # =================================================

    def transition_counts(self):

        transitions = Counter()

        for geometry in self.geometries:

            for transition in geometry.sequence.transitions:

                transitions[transition] += 1

        return transitions

    # =================================================
    # Feature Matrix
    # =================================================

    @staticmethod
    def feature_columns():

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
    # Convenience
    # =================================================

    def primitives(self):

        return self.df["primitive"].to_numpy()

    def families(self):

        return self.df["primitive_family"].to_numpy()

    # =================================================
    # Export
    # =================================================

    def export_csv(
        self,
        filename,
    ):

        self.df.to_csv(
            filename,
            index=False,
        )
