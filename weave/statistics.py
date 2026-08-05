"""
Corpus-level statistics for persistent
geometric events.

This module aggregates GeometrySequences
from many garments and computes the
statistical foundation used for

• event analysis
• clustering
• grammar discovery
• semantic learning
"""

from collections import Counter

import numpy as np
import pandas as pd

from .events import (
    GeometryEvent,
    GeometrySequence,
)


class StatisticsAnalyzer:
    """
    Analyze persistent geometric events
    across an entire garment corpus.
    """

    def __init__(self):

        self.records = []
        self.df = None

    # ==================================================
    # Add one garment
    # ==================================================

    def add(
        self,
        garment_id,
        sequence
    ):
        """
        Add one GeometrySequence to the corpus.
        """

        if len(sequence) == 0:
            return

        total_length = sequence[-1].end

        for i, event in enumerate(sequence):

            self.records.append({

                "garment": garment_id,

                "event_index": i,

                "kind": event.kind,

                "start": event.start,

                "end": event.end,

                "center": event.center,

                "relative_position":
                    event.center / total_length,

                "length": event.length,

                "amplitude":
                    event.amplitude,

                "mean_gradient":
                    event.mean_gradient,

                "max_gradient":
                    event.max_gradient,

                "mean_curvature":
                    event.mean_curvature,

                "max_curvature":
                    event.max_curvature

            })

    # ==================================================
    # Build DataFrame
    # ==================================================

    def build(self):

        self.df = pd.DataFrame(self.records)

        return self.df

    # ==================================================
    # Summary Statistics
    # ==================================================

    def summary(self):

        if self.df is None:
            self.build()

        return self.df.describe()

    # ==================================================
    # Event Counts
    # ==================================================

    def event_counts(self):

        if self.df is None:
            self.build()

        return Counter(
            self.df["kind"]
        )

    # ==================================================
    # Grammar Sentence Counts
    # ==================================================

    def sentence_counts(
        self,
        sequences
    ):

        counter = Counter()

        for seq in sequences:

            sentence = tuple(
                event.kind
                for event in seq
            )

            counter[sentence] += 1

        return counter

    # ==================================================
    # Transition Statistics
    # ==================================================

    def transition_counts(self):

        if self.df is None:
            self.build()

        counter = Counter()

        for garment in self.df["garment"].unique():

            df = self.df[
                self.df["garment"] == garment
            ]

            kinds = df["kind"].tolist()

            for a, b in zip(
                kinds[:-1],
                kinds[1:]
            ):

                counter[(a, b)] += 1

        return counter

    # ==================================================
    # Feature Matrix
    # ==================================================

    def feature_matrix(self):

        if self.df is None:
            self.build()

        columns = [

            "length",

            "amplitude",

            "mean_gradient",

            "max_gradient",

            "mean_curvature",

            "max_curvature",

            "relative_position"

        ]

        return self.df[
            columns
        ].to_numpy() 
