import numpy as np
import networkx as nx

if __name__ == '__main__':
    with open('../../data/ml-100k/ub.base', "r") as f:
        file = f.read()
    a = file.split()
    a = np.array(a)
    a = a.reshape(90570,4)
    a = a.astype(float)
    G = nx.Graph()
    shape = a.shape
    for x in range(0, shape[0]):
        if a[x, 2] > 2:
            G.add_node(int(a[x, 0]))
            G.add_node(str(int(a[x, 1])))
            G.add_weighted_edges_from([(int(a[x, 0]), str(int(a[x, 1])), float(a[x, 2]))])

    with open('../../data/ml-100k/movies_100k_index.txt', "r") as f:
        file = f.read()
    movies_index = file.split()

    n = 943
    m = 1682

    w = np.zeros((m,m))

    for i in range(0, m):
        print(i)
        for j in range(0, m):
            sum = 0
            for l in range(1, n + 1):
                if (G.has_node(l)):
                    sum += (int(G.has_edge(l, str(movies_index[i + 1]))) * int(G.has_edge(l, str(movies_index[j + 1])))) / G.degree(l)
            if (G.has_node(str(movies_index[i + 1]))):
                w[i][j] = round(sum / G.degree(str(movies_index[i + 1])), 8)

    np.save("../../data/ml-100k/movies_100k_UC_02.npy", w)