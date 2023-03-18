import networkx as nx
import numpy as np

if __name__ == '__main__':
    n = 4066
    G_user = nx.Graph()
    for i in range(1, n + 1):
        G_user.add_node(i)

    # 信任关系网络
    with open('data/social_data.txt', 'r') as f:
        f_u = f.readlines()
    for line in f_u:
        G_user.add_edge(int(line.split(' ')[0]), int(line.split(' ')[1]))
    print(len(G_user.nodes))
    print(len(G_user.edges))

    with open('data/ratings_data.txt', "r") as f:
        file = f.read()

    a_train = file.split()
    a_train = np.array(a_train)
    a_train = a_train.reshape(154122, 3)
    a_train = a_train.astype(float)
    G_train = nx.Graph()
    for i in range(1, n + 1):
        G_train.add_node(i)
    shape = a_train.shape
    for x in range(0, shape[0]):
        if a_train[x, 2] > 3:
            G_train.add_node(int(a_train[x, 0]), type = 'user')
            G_train.add_node(str(int(a_train[x, 1])), type = 'item')
            G_train.add_weighted_edges_from([(int(a_train[x, 0]), str(int(a_train[x, 1])), float(a_train[x, 2]))])

    print(len(G_train.edges))

    delet_node = []
    for node in G_train.nodes():
        if(G_train.degree(node) == 0):
            print(node)
            delet_node.append(node)

    G_user.remove_nodes_from(delet_node)
    print(len(G_user.nodes))
    print(len(G_user.edges))