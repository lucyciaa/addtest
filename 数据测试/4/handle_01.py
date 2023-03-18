import networkx as nx
import numpy as np

if __name__ == '__main__':

    with open('data/ratings_data.txt', "r") as f:
        file = f.read()

    a_train = file.split()
    a_train = np.array(a_train)
    a_train = a_train.reshape(664811, 3)
    a_train = a_train.astype(float)
    G_train = nx.Graph()
    shape = a_train.shape
    for x in range(0, shape[0]):
        G_train.add_node(int(a_train[x, 0]), type = 'user')
        G_train.add_node(str(int(a_train[x, 1])), type = 'item')
        G_train.add_weighted_edges_from([(int(a_train[x, 0]), str(int(a_train[x, 1])), float(a_train[x, 2]))])


    # 用户
    n = 49287

    # 创建用户购买过的商品的字典
    user_goods_dict = {}
    for i in range(1, n + 1) :
        user_goods_dict[i] = []
    with open('data/ratings_data.txt', "r") as f:
        file = f.read()
    user_list = file.split()
    user_list = np.array(user_list)
    user_list = user_list.reshape(664811, 3)
    user_list = user_list.astype(int)
    rows = user_list.shape
    for x in range(0, rows[0]):
        user_goods_dict[user_list[x, 0]].append(user_list[x, 1])

    for key in user_goods_dict:
        if(len(user_goods_dict[key]) == 0) :
            print(key,'孤立点')

    # 构建用户网络
    G_user = nx.Graph()
    for i in range(1, n + 1):
        G_user.add_node(i)
    with open('data/trust_data.txt','r') as f:
        f1 = f.readlines()
    with open('data/trust_data_02.txt', 'w') as f:
        for line in f1:
            if(len(user_goods_dict[int(line.split(' ')[1])]) > 0 and len(user_goods_dict[int(line.split(' ')[2])]) > 0):
                f.write(line)
