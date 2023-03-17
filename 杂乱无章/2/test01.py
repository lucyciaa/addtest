
if __name__ == '__main__':
    with open('ratings_data.txt','r') as f:
        file = f.readlines()
    count = 0
    for line in file:
        if(int(line.split(' ')[2]) > 4):
            count += 1
    print(count)
