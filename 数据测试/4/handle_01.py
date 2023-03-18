import networkx as nx
import numpy as np

if __name__ == '__main__':

    with open('data/ratings_data.txt', "r") as f:
        file = f.read()

    # 用户
    n = 49289

    a_train = file.split()
    a_train = np.array(a_train)
    a_train = a_train.reshape(664824, 3)
    a_train = a_train.astype(float)
    G_train = nx.Graph()
    for i in range(1,n + 1):
        G_train.add_node(i,type='user')
    shape = a_train.shape
    for x in range(0, shape[0]):
        if a_train[x, 2] > 2:
            G_train.add_node(str(int(a_train[x, 1])), type = 'item')
            G_train.add_weighted_edges_from([(int(a_train[x, 0]), str(int(a_train[x, 1])), float(a_train[x, 2]))])




    # 构建用户网络
    G_user = nx.Graph()
    for i in range(1,n + 1):
        G_user.add_node(i)
    with open('data/trust_data.txt', 'r') as f:
        f_u = f.readlines()
    for line in f_u:
        G_user.add_edge(int(line.split(' ')[1]), int(line.split(' ')[2]))

    lone_node = []
    for node in G_train.nodes():
        if (G_train.nodes[node]['type'] == 'user'):
            if (G_train.degree(node) == 0):
                lone_node.append(node)
    print('商品二部图网络中孤立的用户节点：', len(lone_node))

    print('第一次删除前用户网络中连边的个数：', len(G_user.edges))
    nodes_delete = []
    for node in G_user.nodes():
        if(node in lone_node) :
            nodes_delete.append(node)

    for node in nodes_delete:
        edges_to_remove = list(G_user.edges(node))
        G_user.remove_edges_from(edges_to_remove)
    print('第一次删除后用户网络中连边的个数', len(G_user.edges))

    lone_node = []
    for node in G_user.nodes():
        if(G_user.degree(node) == 0):
            lone_node.append(node)
    print('社交网络中孤立的点：', len(lone_node))


    print('第一次删除前商品二部图网络中连边数', len(G_train.edges))
    nodes_delete = []
    for node in G_train.nodes:
        if(G_train.nodes[node]['type'] == 'user'):
            if(node in lone_node):
                nodes_delete.append(node)
    for node in nodes_delete:
        edges_to_remove = list(G_train.edges(node))
        G_train.remove_edges_from(edges_to_remove)

    print('第一次删除后商品二部图网络中连边数', len(G_train.edges))


    lone_node = []
    for node in G_train.nodes():
        if (G_train.nodes[node]['type'] == 'user'):
            if(G_train.degree(node) == 0):
                lone_node.append(node)
    print('商品二部图网络中孤立的点：', len(lone_node))


    print('第二次删除前用户网络中连边的个数：', len(G_user.edges))
    nodes_delete = []
    for node in G_user.nodes():
        if (node in lone_node):
            nodes_delete.append(node)
    print('node_delete', len(nodes_delete))
    for node in nodes_delete:
        edges_to_remove = list(G_user.edges(node))
        G_user.remove_edges_from(edges_to_remove)

    print('第二次删除后用户网络中连边的个数', len(G_user.edges))
    print('')
    lone_node = []
    for node in G_user.nodes():
        if (G_user.degree(node) == 0):
            lone_node.append(node)
    print('社交网络中孤立的用户节点：', len(lone_node))


    print('第三次删除前商品二部图网络中连边数', len(G_train.edges))
    nodes_delete = []
    for node in G_train.nodes():
        if (G_train.nodes[node]['type'] == 'user'):
            if (node in lone_node):
                nodes_delete.append(node)
    for node in nodes_delete:
        edges_to_remove = list(G_train.edges(node))
        G_train.remove_edges_from(edges_to_remove)

    print('第三次删除后商品二部图网络中连边数', len(G_train.edges))


    lone_node = []
    for node in G_train.nodes():
        if (G_train.nodes[node]['type'] == 'user'):
            if (G_train.degree(node) == 0):
                lone_node.append(node)
    print('商品二部图网络中孤立的用户节点：', len(lone_node))


    print('第四次删除前用户网络中连边的个数：', len(G_user.edges))
    nodes_delete = []
    for node in G_user.nodes():
        if (node in lone_node):
            nodes_delete.append(node)
    for node in nodes_delete:
        edges_to_remove = list(G_user.edges(node))
        G_user.remove_edges_from(edges_to_remove)

    print('第四次删除后用户网络中连边的个数', len(G_user.edges))
