"""
Corpus-level statistics for the
WeaveAI Sketch Graph.

StatisticsAnalyzer aggregates GeometrySequences
from many garments and constructs the statistical
foundation used for

• descriptive statistics
• event visualization
• clustering
• grammar discovery
• semantic learning
"""

from collections import Counter

import numpy as np
import pandas as pd

from .events import (
    GeometrySequence,
    GeometryEvent
)


# =====================================================
# Statistics Analyzer
# =====================================================

class StatisticsAnalyzer:
    """
    Analyze persistent GeometryEvents across
    an entire garment corpus.
    """

    def __init__(self):

        self.records = []

        self.df = None

    # =================================================

    def add(
        self,
        garment_id,
        sequence: GeometrySequence
    ):
        """
        Add one GeometrySequence to the corpus.
        """

        if len(sequence) == 0:
            return

        total_length = sequence[-1].end

        if total_length == 0:
            total_length = 1

        for index, event in enumerate(sequence):

            row = event.as_dict()

            row["garment"] = garment_id

            row["event_index"] = index

            row["center"] = event.center

            row["relative_position"] = (
                event.center / total_length
            )

            self.records.append(row)

    # =================================================

    def build(self):
        """
        Build the event dataframe.
        """

        self.df = pd.DataFrame(
            self.records
        )

        return self.df

    # =================================================

    @property
    def dataframe(self):

        if self.df is None:

            self.build()

        return self.df

    # =================================================

    @property
    def feature_columns(self):

        return [

            "length",

            "amplitude",

            "mean_gradient",

            "max_gradient",

            "mean_curvature",

            "max_curvature",

            "relative_position"

        ]

    # =================================================

    def feature_matrix(self):
        """
        Event feature matrix used by
        PCA and clustering.
        """

        return self.dataframe[
            self.feature_columns
        ].to_numpy()

    # =================================================

    def summary(self):
        """
        Descriptive statistics.
        """

        return self.dataframe.describe()

    # =================================================

    def event_counts(self):
        """
        Frequency of each event type.
        """

        return Counter(
            self.dataframe["kind"]
        )

    # =================================================

    def transition_counts(self):
        """
        Frequency of event transitions.
        """

        counter = Counter()

        for garment in self.dataframe[
            "garment"
        ].unique():

            df = self.dataframe[
                self.dataframe["garment"]
                == garment
            ]

            kinds = df["kind"].tolist()

            for a, b in zip(
                kinds[:-1],
                kinds[1:]
            ):

                counter[(a, b)] += 1

        return counter

    # =================================================

    def histogram(
        self,
        column,
        bins=20
    ):
        """
        Histogram values.
        """

        return np.histogram(

            self.dataframe[column],

            bins=bins

        )

    # =================================================

    def correlation(self):
        """
        Feature correlation matrix.
        """

        return self.dataframe[
            self.feature_columns
        ].corr()

    # =================================================

    def export_csv(
        self,
        filename="events.csv"
    ):
        """
        Save corpus.
        """

        self.dataframe.to_csv(

            filename,

            index=False

        )
