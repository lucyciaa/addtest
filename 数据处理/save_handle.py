
if __name__ == '__main__':
    with open('../../data/ml-100k/movies_100k_index.txt', "w") as f:
        for i in range(0,1683):
            f.write(str(i) + '\n')