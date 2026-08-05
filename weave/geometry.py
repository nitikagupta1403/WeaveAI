"""
Symbolic geometry representation for WeaveAI.

Signal
    ↓
Width Signature
    ↓
Candidate Events
    ↓
Persistent Geometry Events
    ↓
Geometry Sequence
    ↓
Primitive Sentence
    ↓
Primitive Families
    ↓
Transition Graph
    ↓
Sketch Graph

Geometry is the symbolic intermediate
representation (IR) used throughout WeaveAI.
"""

from collections import Counter

import networkx as nx

from .events import GeometrySequence


class Geometry:
    """
    Symbolic representation of one garment.

    Geometry owns the GeometrySequence and all
    higher-level symbolic structures derived from it.
    """

    def __init__(self):

        # =================================================
        # Signal
        # =================================================

        self.signature = None

        # =================================================
        # Symbolic Geometry
        # =================================================

        self.sequence = GeometrySequence()

        # =================================================
        # Learned Representation
        # =================================================

        self.prototype_curves = None

        # =================================================
        # Grammar
        # =================================================

        self.transition_graph = nx.DiGraph()

        # =================================================
        # Sketch Graph
        # =================================================

        self.sketch_graph = nx.DiGraph()

    # =================================================
    # Convenience Properties
    # =================================================

    @property
    def events(self):

        return self.sequence.events

    @property
    def primitive_sentence(self):

        return self.sequence.primitive_sentence

    @property
    def family_sentence(self):

        return self.sequence.family_sentence

    @property
    def grammar_sentence(self):

        return self.sequence.grammar_sentence

    @property
    def primitive_counts(self):

        return Counter(self.primitive_sentence)

    @property
    def family_counts(self):

        return Counter(self.family_sentence)

    @property
    def feature_matrix(self):

        return self.sequence.feature_matrix

    # =================================================
    # Graph Construction
    # =================================================

    def build_transition_graph(self):
        """
        Build a primitive transition graph.
        """

        G = nx.DiGraph()

        for a, b in self.sequence.transitions:

            if G.has_edge(a, b):

                G[a][b]["weight"] += 1

            else:

                G.add_edge(a, b, weight=1)

        self.transition_graph = G

        return G

    # =================================================

    def build_sketch_graph(self):
        """
        Build an event-level sketch graph.
        """

        G = nx.DiGraph()

        for i, event in enumerate(self.events):

            node = event.event_id or f"E{i}"

            G.add_node(

                node,

                kind=event.kind,
                primitive=event.primitive,
                family=event.primitive_family,
                grammar_role=event.grammar_role,

                start=event.start,
                end=event.end,
                center=event.center,

                length=event.length,
                amplitude=event.amplitude,

            )

        for a, b in zip(self.events[:-1], self.events[1:]):

            G.add_edge(a.event_id, b.event_id)

        self.sketch_graph = G

        return G

    # =================================================
    # Summary
    # =================================================

    def summary(self):

        print("Geometry")
        print("--------------------")
        print(f"Events      : {len(self.events)}")
        print(f"Primitives  : {len(self.primitive_counts)}")
        print(f"Families    : {len(self.family_counts)}")

    # =================================================

    def __len__(self):

        return len(self.sequence)

    def __iter__(self):

        return iter(self.sequence)

    def __getitem__(self, index):

        return self.sequence[index]

    # =================================================

    def __repr__(self):

        return f"Geometry({len(self.sequence)} events)"
