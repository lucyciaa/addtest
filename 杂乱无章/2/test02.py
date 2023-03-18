
if __name__ == '__main__':
    with open('train.txt','r') as f:
        file = f.readlines()

    for line in file:
        if(len(line.split(' ')) > 3):
            print(line)

