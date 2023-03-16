import networkx as nx
import numpy as np

if __name__ == '__main__':
    # 训练网络构建
    with open('../data/ml-100k/ub.base', "r") as f:
        file = f.read()
    a_train = file.split()
    a_train = np.array(a_train)
    a_train = a_train.reshape(90570, 4)
    a_train = a_train.astype(float)
    G_train = nx.Graph()
    shape = a_train.shape
    for x in range(0, shape[0]):
        if a_train[x, 2] > 2:
            G_train.add_node(int(a_train[x, 0]))
            G_train.add_node(str(int(a_train[x, 1])))
            G_train.add_weighted_edges_from([(int(a_train[x, 0]), str(int(a_train[x, 1])), float(a_train[x, 2]))])

    # 测试网络构建
    with open('../data/ml-100k/ub.test', "r") as f:
        file_test = f.read()
    a_test = file_test.split()
    a_test = np.array(a_test)
    a_test = a_test.reshape(9430, 4)
    a_test = a_test.astype(float)
    G_test = nx.Graph()
    shape_2 = a_test.shape
    for x in range(0, shape_2[0]):
        if a_test[x, 2] > 2:
            G_test.add_node(int(a_test[x, 0]))
            G_test.add_node(str(int(a_test[x, 1])))
            G_test.add_weighted_edges_from([(int(a_test[x, 0]), str(int(a_test[x, 1])), float(a_test[x, 2]))])

    # 电影序列号构建
    with open('../data/ml-100k/movies_100k_index.txt', "r") as f:
        file = f.read()
    movies_index = file.split()

    # 用户
    n = 943
    # 商品
    m = 1682

    start = 1
    # end = 944
    end = 10

    sum_1 = 0
    count = 0

    # 创建用户购买过的商品的字典
    user_goods_dict = {}
    for i in range(1, n + 1) :
        user_goods_dict[i] = []
    with open('../data/ml-100k/ub.base', "r") as f:
        file = f.read()
    user_list = file.split()
    user_list = np.array(user_list)
    user_list = user_list.reshape(90570, 4)
    user_list = user_list.astype(int)
    rows = user_list.shape
    for x in range(0, rows[0]):
        user_goods_dict[user_list[x, 0]].append(user_list[x, 1])
    # print(user_goods_dict)

    p = 0.9
    q = 0.5
    for user in range(start, end):
        # 第一步 初始资源赋值
        f_goods = np.zeros(m)
        for i in range(1, m + 1):
            if (G_train.has_edge(user, str(movies_index[i]))):
                f_goods[i - 1] = 1
        # 第二步 商品向用户传播资源
        f_user = np.zeros(n)
        for i in range(1, n + 1):
            # 商品向用户扩散的资源总值
            goodsToUser = 0
            for j in range(1, m + 1):
                if (G_train.has_edge(i, str(movies_index[j]))):
                    goodsToUser += (f_goods[j - 1] * int(G_train.has_edge(i, str(movies_index[j])))) / G_train.degree(
                        str(movies_index[j]))
            f_user[i - 1] = goodsToUser

        # 定义关系
        # 用户A和用户B购买过的交集 / 用户A和用户B购买过的并集

        # 构建用户网络
        ctt = 0
        ctt2 = 0
        G_user = nx.Graph()
        for i in range(1, n + 1):
            G_user.add_node(i)
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                ctt2 += 1
                # 交集
                inter = len(set(user_goods_dict[i]).intersection(set(user_goods_dict[j])))
                # 并集
                union = len(set(user_goods_dict[i] + user_goods_dict[j]))
                if(inter / union > 0.2):
                    G_user.add_edge(i,j)
                    ctt += 1
                    # print(inter, union, inter / union)
        print(ctt,ctt2, ctt / ctt2)

        # 第三步 用户向商品和用户传播资源，设 p = 0.5
        # 首先向商品传播资源
        f_final = np.zeros(m)
        for i in range(1, m + 1):
            userToGoods = 0
            for j in range(1, n + 1):
                if (G_train.has_edge(j, str(movies_index[i]))):
                    userToGoods += p * f_user[j - 1] * int(G_train.has_edge(j, str(movies_index[i]))) / G_train.degree(j)
            f_final[i - 1] = userToGoods

        # print(f_final)
        # 用户向用户传递资源
        f_user_to_user = np.zeros(n)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if(i == j):
                    continue
                if(G_user.has_edge(i, j)):
                    f_user_to_user[j - 1] = f_user_to_user[j - 1] + q * f_user[i - 1] / G_user.degree(i)
        # print(f_user_to_user)

        # 第四步 用户再次向商品传播资源
        for i in range(1, m + 1):
            userToGoods = 0
            for j in range(1, n + 1):
                if (G_train.has_edge(j, str(movies_index[i]))):
                    userToGoods += f_user_to_user[j - 1] * int(G_train.has_edge(j, str(movies_index[i]))) / G_train.degree(j)
            f_final[i - 1] = f_final[i - 1] + userToGoods
        # print(f_user)
        # print(f_final)

        # 对结果进行排序
        f_out_sort = abs(np.sort(-f_final))

        if (G_test.has_node(user) and G_train.has_node(user) and G_test.degree(user) > 0):

            for item in G_test[user]:
                ct = 0
                for i in f_out_sort:
                    ct += 1
                    if (f_final[movies_index.index(str(item)) - 1] == i):
                        count += 1
                        break
                print('用户:' + str(user), '节点:' + item, '第' + str(ct) + '名', 'y/x:' + str((ct) / m))

                sum_1 += (ct) / m
                print('现在已有评价:', count, '现在平均值为:', sum_1 / count)
        print('')
    print(sum_1 / count)