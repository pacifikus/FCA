from src.fca.context import Context
from src.fca.json_reader import read_json
from src.fca.random_walker import RandomWalker

if __name__ == "__main__":

    G = ["girl", "woman", "boy", "man"]
    M = ["female", "juvenile", "adult", "male"]
    I = [[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 1]]

    # G, M, I = read_json(r'C:/Users/Krutizna/PycharmProjects/fca/src/xml_data/source.json')

    G = [
        "canal",
        "channel",
        "lagoon",
        "lake",
        "maar",
        "puddle",
        "pond",
        "pool",
        "reservoir",
        "river",
        "rivulet",
        "runnel",
        "sea",
        "stream",
        "tarn",
        "torrent",
        "trickle",
    ]
    M = ["temporary", "running", "natural", "stagnant", "constant", "maritime"]
    I = [
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 1],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 0],
    ]

    context = Context(G, M, I)
    res = context.build_lattice()
    rw = RandomWalker(res)
    for node in rw.get_path():
        print(node)
    res.draw_hasse()
