import networkx as nx
import numpy as np

if __name__ == '__main__':
    # 训练网络构建
    with open('data/train.txt', "r") as f:
        file = f.read()

    a_train = file.split()
    a_train = np.array(a_train)
    a_train = a_train.reshape(11, 3)
    a_train = a_train.astype(float)
    G_train = nx.Graph()
    shape = a_train.shape
    for x in range(0, shape[0]):
        G_train.add_node(int(a_train[x, 0]), type='user')
        G_train.add_node(str(int(a_train[x, 1])), type='item')
        G_train.add_weighted_edges_from([(int(a_train[x, 0]), str(int(a_train[x, 1])), float(a_train[x, 2]))])

    # 用户
    n = 5
    # 商品
    m = 4

    start = 1
    # end = 944
    end = 2

    w = np.load("data/small_social.npy")
    for user in range(start, end):
        # 第一步 初始资源赋值
        f_goods = np.zeros(m)
        for i in range(1, m + 1):
            if (G_train.has_edge(user, str(i))):
                f_goods[i - 1] = 1
        f_out = np.dot(w, f_goods)
        print(f_out)

