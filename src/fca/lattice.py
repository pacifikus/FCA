import json

import matplotlib.pyplot as plt
import networkx as nx


class Lattice:
    def __init__(self, C, E):
        self.C = C
        self.E = self.get_cleared_edges(E)

    def get_cleared_edges(self, edges):
        res = set()
        levels = list(set(sorted([c.level for c in self.C])))
        for concept in self.C:
            concept.level = levels.index(concept.level)
        for edge in edges:
            if abs(self.C[edge[0]].level - self.C[edge[1]].level) == 1:
                res.add(edge)
        return res

    def draw_hasse(self):
        plt.figure(figsize=(30, 10))
        G = nx.Graph()
        G.add_edges_from(self.E)
        plt.subplot(111)

        pos = {}
        labels = {}
        i = 1
        prev_level = 0
        lev_mult = 1
        level_num = 1
        for n in range(len(self.C)):
            labels[n] = self.C[n].__str__()
            level = self.C[n].level
            count = sum(1 for i in self.C if i.level == level)
            if prev_level != level:
                level_num += 1
                lev_mult = 1
                prev_level = level
            else:
                lev_mult += 1
            pos[n] = (i / (count + 1) * lev_mult, 1 - i * level_num)

        nx.draw_networkx_labels(G, pos, labels, font_size=12)
        nx.draw_networkx_nodes(G, pos, range(len(self.C)), node_color="r")
        nx.draw_networkx_edges(G, pos)
        plt.show()

    def to_json(self, path):
        with open(path, "w") as outfile:
            json.dump(self.__dict__, outfile)

    def __repr__(self):
        return "({0}) ({1})".format(", ".join(self.C), ", ".join(self.E))
