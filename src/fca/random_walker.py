import random


class RandomWalker:
    def __init__(self, lattice):
        self.lattice = lattice

    def get_path(self):
        index = 0
        yield self.lattice.C[index].M
        next_nodes = self.get_edges(index)
        while len(next_nodes) != 0:
            index = random.choice(next_nodes)
            yield self.lattice.C[index].M
            next_nodes = self.get_edges(index)

    def get_edges(self, index):
        pairs = list(filter(lambda x: x[1] == index, self.lattice.E))
        return [pair[0] for pair in pairs]
