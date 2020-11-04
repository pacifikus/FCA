from src.fca.concept import Concept
from src.fca.lattice import Lattice


class Context:
    def __init__(self, G, M, I):
        self.G = G
        self.M = M
        self.I = I
        self.objects_of = {}
        self.attributes_of = {}

        for id_g, g in enumerate(G):
            obj = G[id_g]
            self.attributes_of[obj] = set()
            for id_m, m in enumerate(M):
                if I[id_g][id_m] == 1:
                    attribute = M[id_m]
                    self.attributes_of[obj].add(attribute)
                    if attribute not in self.objects_of:
                        self.objects_of[attribute] = set()
                    self.objects_of[attribute].add(obj)

    def __getitem__(self, item):
        if item in self.attributes_of:
            return self.attributes_of[item]
        else:
            return self.objects_of[item]

    def get_object_closure(self, *args):
        """Return the extent closure"""
        attrs = self.get_attributes(*args)
        objects = self.get_objects(*attrs)
        return objects

    def get_attribute_closure(self, *args):
        """Return the intent closure"""
        objects = self.get_objects(*args)
        attrs = self.get_attributes(*objects)
        return attrs

    def get_attributes(self, *args):
        """Return all attributes that share obj"""
        res = set()
        if len(args) > 0:
            res |= self.attributes_of[args[0]]
            for obj in args[1:]:
                res &= self.attributes_of[obj]
        return res

    def get_objects(self, *args):
        """Return all objects that share attribute"""
        res = set()
        if len(args) > 0:
            res |= self.objects_of[args[0]]
            for attribute in args[1:]:
                res &= self.objects_of[attribute]
        return res

    def build_lattice(self):
        start_concept = Concept(self.G, self.get_attributes(*self.G))
        C = [start_concept]
        E = set()
        current_level = {start_concept}
        while len(current_level) != 0:
            next_level = set()
            for concept in current_level:
                lower_neighbours = self.find_lower_neighbours(concept)
                for lower_concept in lower_neighbours:
                    if lower_concept not in C:
                        C.append(lower_concept)
                        next_level.add(lower_concept)
                    E.add((C.index(lower_concept), C.index(concept)))
            current_level = next_level
        return Lattice(C, E)

    def find_lower_neighbours(self, concept):
        neighbours = set()
        for m in self.M:
            if m not in concept.M:
                x = concept.M.copy()
                x.add(m)
                x = self.get_objects(*x)
                y = self.get_attributes(*x)
                if Concept(x, y) not in neighbours:
                    neighbours.add(Concept(x, y))
        return self.get_max_general(neighbours)

    def get_max_general(self, neighbours):
        res = set()
        for c in neighbours:
            general = True
            for cc in neighbours:
                if c != cc and len(cc.G & c.G) == len(c.G):
                    general = False
                    break
            if general:
                res.add(c)
        return res
