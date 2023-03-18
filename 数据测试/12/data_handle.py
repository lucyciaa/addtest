import numpy as np
import networkx as nx

if __name__ == '__main__':
    with open('data/train.txt', "r") as f:
        file = f.read()
    data = file.split()
    data = np.array(data, dtype=float).reshape(138709, 3)

    G = nx.Graph()
    nodes = np.unique(data[:, :2])
    G.add_nodes_from(nodes)
    edges = [(int(e[0]), str(int(e[1])), float(e[2])) for e in data]
    G.add_weighted_edges_from(edges)

    n = 4066
    m = 7649

    w = np.zeros_like(np.zeros((m, m)))

    for i in range(m):
        print(i)
        for j in range(m):
            mask_i = G.has_edge(np.arange(1, n+1), str(i+1)).astype(float)
            mask_j = G.has_edge(np.arange(1, n+1), str(j+1)).astype(float)
            degrees = np.array([G.degree(str(node)) for node in G.nodes()])
            sums = np.sum(mask_i * mask_j / degrees)
            if (G.has_node(str(j + 1))):
                w[i, j] = round(sums / G.degree(str(j + 1)), 8)

    np.save("data/epinions.npy", w)
