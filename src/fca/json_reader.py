import json


def read_json(path):
    with open(path) as json_file:
        data = json.load(json_file)
        G = data['dims']
        M = data['measures']
        I = data['matrix']
    return G, M, I
