class Concept:
    def __init__(self, G, M):
        self.G = G
        self.M = M
        self.level = len(G)

    def __hash__(self):
        return hash(frozenset(self.G)) + hash(frozenset(self.M))

    def __eq__(self, other):
        return self.G == other.G and self.M == other.M

    def __repr__(self):
        return "({0})\n({1})".format(", ".join(self.G), ", ".join(self.M))
