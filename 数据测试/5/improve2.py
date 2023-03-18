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




    # 构建用户网络
    G_user = nx.Graph()
    for i in range(1, n + 1):
        G_user.add_node(i)


    # 信任关系网络
    with open('data/trust_data.txt','r') as f:
        f_u = f.readlines()
    for line in f_u:
        G_user.add_edge(int(line.split(' ')[0]),int(line.split(' ')[1]))

    p = 0.5
    q = 1 - p
    for user in range(start, end):
        # 第一步 初始资源赋值
        f_goods = np.zeros(m)
        for i in range(1, m + 1):
            if (G_train.has_edge(user, str(i))):
                f_goods[i - 1] = 1
        # print(f_goods)
        # 第二步 商品向用户传播资源
        # 商品向用户扩散的资源总值
        f_user = np.zeros(n)
        for i in G_train.nodes():
            goodsToUser = 0
            if(G_train.nodes[i]['type'] == 'user'):
                for j in G_train.neighbors(i):
                    goodsToUser += f_goods[int(j) - 1] / G_train.degree(j)
                f_user[i - 1] = goodsToUser
        print('f_user', f_user)

        # 第三步 用户向商品和用户传播资源
        # 首先向商品传播资源
        f_final = np.zeros(m)
        for i in G_train.nodes():
            userToGoods = 0
            if (G_train.nodes[i]['type'] == 'item'):
                for j in G_train.neighbors(i):
                    userToGoods += p * f_user[int(j) - 1] / G_train.degree(int(j))
                f_final[int(i) - 1] = userToGoods
        print('f_final',f_final)

        # 用户向用户传递资源
        f_user_to_user = np.zeros(n)
        for i in G_user.nodes():
            for j in G_user.neighbors(i):
                f_user_to_user[int(j) - 1] = f_user_to_user[int(j) - 1] + q * f_user[int(i) - 1] / G_user.degree(int(i))
        print('f_user_to_user', f_user_to_user)
        # 第四步 用户再次向商品传播资源
        for i in G_train.nodes():
            userToGoods = 0
            if (G_train.nodes[i]['type'] == 'item'):
                for j in G_train.neighbors(i):
                    userToGoods += f_user_to_user[int(j) - 1] / G_train.degree(int(j))
                f_final[int(i) - 1] = f_final[int(i) - 1] + userToGoods
        print('f_final', f_final)

