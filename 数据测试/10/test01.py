
if __name__ == '__main__':
    n = 4066
    m = 7649
    ct = 0
    for i in range(0, m):
        print(i)
        for j in range(0, m):
            for l in range(0, n):
                ct += 1
    print(ct)