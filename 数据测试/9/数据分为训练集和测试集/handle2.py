import random


if __name__ == '__main__':
    # 读取原始数据文件
    with open('../data/ratings_data.txt', 'r') as f:
        data = f.readlines()

    # 随机打乱数据
    random.shuffle(data)

    # 分割数据
    split_idx = int(len(data) * 0.9)
    train_data = data[:split_idx]
    test_data = data[split_idx:]

    # 将训练数据写入文件
    with open('../data/train.txt', 'w') as f:
        f.writelines(train_data)

    # 将测试数据写入文件
    with open('../data/test.txt', 'w') as f:
        f.writelines(test_data)
