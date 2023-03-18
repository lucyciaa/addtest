import networkx as nx

if __name__ == '__main__':
    G_user = nx.Graph()
    with open('social_data.txt', 'r') as f:
        f_u = f.readlines()
    for line in f_u:
        G_user.add_edge(int(line.split(' ')[0]), int(line.split(' ')[1]))
    print(len(G_user.nodes))
    print(len(G_user.edges))

    G_test = nx.Graph()
    G_test.add_edge(1,2)
    G_test.add_edge(2,1)
    G_test.add_edge(1,2)
    print(G_test.degree(1))