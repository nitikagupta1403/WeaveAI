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
representation (IR) used by all higher-level
reasoning modules.
"""

from collections import Counter
import networkx as nx

from .events import GeometrySequence


class Geometry:

    def __init__(self):

        # ==========================================
        # Signal
        # ==========================================

        self.signature = None

        # ==========================================
        # Geometry
        # ==========================================

        self.sequence = GeometrySequence()

        # ==========================================
        # Learned Representation
        # ==========================================

        self.prototype_curves = None

        # ==========================================
        # Grammar
        # ==========================================

        self.transition_matrix = None
        self.transition_graph = nx.DiGraph()

        # ==========================================
        # Higher-Level Representation
        # ==========================================

        self.sketch_graph = nx.DiGraph()

    # ==================================================
    # Convenience Properties
    # ==================================================

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
    def primitive_counts(self):

        return Counter(self.primitive_sentence)

    @property
    def family_counts(self):

        return Counter(self.family_sentence)

    # ==================================================
    # Graph Construction
    # ==================================================

    def build_transition_graph(self):

        G = nx.DiGraph()

        sentence = self.primitive_sentence

        for a, b in zip(sentence[:-1], sentence[1:]):

            if G.has_edge(a, b):
                G[a][b]["weight"] += 1
            else:
                G.add_edge(a, b, weight=1)

        self.transition_graph = G

        return G

    # ==================================================
    # Sketch Graph
    # ==================================================

    def build_sketch_graph(self):

        G = nx.DiGraph()

        for event in self.events:

            node = event.event_id

            G.add_node(

                node,

                primitive=event.primitive,

                family=event.primitive_family,

                kind=event.kind,

                start=event.start,

                end=event.end,

            )

        for a, b in zip(self.events[:-1], self.events[1:]):

            G.add_edge(a.event_id, b.event_id)

        self.sketch_graph = G

        return G

    # ==================================================
    # Summary
    # ==================================================

    def summary(self):

        print("Geometry")
        print("--------------------")
        print("Events      :", len(self.events))
        print("Primitives  :", self.primitive_sentence)
        print("Families    :", self.family_sentence)

    # ==================================================

    def __len__(self):

        return len(self.sequence)

    def __iter__(self):

        return iter(self.sequence)

    def __getitem__(self, i):

        return self.sequence[i]

    def __repr__(self):

        return f"Geometry({len(self.sequence)} events)"
        
