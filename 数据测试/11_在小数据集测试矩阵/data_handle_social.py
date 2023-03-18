import numpy as np
import networkx as nx

if __name__ == '__main__':
    with open('data/train.txt', "r") as f:
        file = f.read()
    a = file.split()
    a = np.array(a)
    a = a.reshape(11,3)
    a = a.astype(float)
    G = nx.Graph()
    shape = a.shape
    for x in range(0, shape[0]):
        G.add_node(int(a[x, 0]))
        G.add_node(str(int(a[x, 1])))
        G.add_weighted_edges_from([(int(a[x, 0]), str(int(a[x, 1])), float(a[x, 2]))])

    # 信任关系网络
    G_user = nx.Graph()
    with open('data/trust_data.txt', 'r') as f:
        f_u = f.readlines()
    for line in f_u:
        G_user.add_edge(int(line.split(' ')[0]), int(line.split(' ')[1]))

    n = 5
    m = 4

    w = np.zeros((m,m))

    p = 0.5
    q = 1 - p

    for i in range(0, m):
        print(i)
        for j in range(0, m):
            sum = 0
            sum2 = 0
            for l in range(1, n + 1):
                if (G.has_node(l)):
                    sum += (int(G.has_edge(l, str(i + 1))) * int(G.has_edge(l, str(j + 1)))) / G.degree(l)
            if (G.has_node(str(j + 1))):
                w[i][j] = p * round(sum / G.degree(str(j + 1)), 8)
            for o in range(1, n + 1):
                for b in range(1, n + 1):
                    if(G.has_node(o) and G_user.has_node(b)):
                        sum2 += (int(G.has_edge(o,str(i + 1)) * int(G.has_edge(b,str(j + 1)) * int(G_user.has_edge(o,b))))) / (G.degree(o) * G_user.degree(b))
            if (G.has_node(str(j + 1))):
                w[i][j] = w[i][j] + q * round(sum2 / G.degree(str(j + 1)), 8)

    np.save("data/small_social.npy", w)