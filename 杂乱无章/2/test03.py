import networkx as nx
import numpy as np

if __name__ == '__main__':
    # 用户
    n = 4066
    # 商品
    m = 7649

    with open('ratings_data.txt', "r") as f:
        file = f.read()

    a_train = file.split()
    a_train = np.array(a_train)
    a_train = a_train.reshape(154122, 3)
    a_train = a_train.astype(float)
    G_train = nx.Graph()
    for i in range(1, n + 1):
        G_train.add_node(i,type = 'user')
    for j in range(1, m + 1):
        G_train.add_node(j, type = 'item')
    shape = a_train.shape
    for x in range(0, shape[0]):
        G_train.add_node(int(a_train[x, 0]), type = 'user')
        G_train.add_node(int(a_train[x, 1]), type = 'item')
        G_train.add_weighted_edges_from([(int(a_train[x, 0]), int(a_train[x, 1]), float(a_train[x, 2]))])

    for node in G_train.nodes():
        # print(G_train.degree(node))
        if (G_train.degree(node) == 0):
            print(node)