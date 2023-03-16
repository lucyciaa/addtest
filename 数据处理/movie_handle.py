
if __name__ == '__main__':
    with open('../../data/ml-100k/u.item','r',encoding='ISO-8859-1') as f:
        file = f.read()

    a = file.split('\n')

    with open('../../data/ml-100k/u.genre','r') as f:
        file = f.read()
    movies_clf = file.split()

    movie_clf = {}
    for item in movies_clf:
        movie_clf[item.split('|')[1]] = item.split('|')[0]
    with open('../../data/ml-100k/movies.dat','w',encoding='utf-8') as f:
        for item in a:
            index_dict = {}
            clf_list = []
            ct = 0
            for index in item.split('||')[1].split('|'):
                index_dict[ct] = index
                ct += 1
            for v in index_dict:
                if(index_dict[v] == '1'):
                    clf_list.append(movie_clf[str(v - 1)])

            f.write(item.split('||')[0].split('|')[0] + '::' + item.split('||')[0].split('|')[1] + '::')
            ctt = 0
            for listt in clf_list:
                if(ctt == 0):
                    f.write(listt)
                else:
                    f.write('|' + listt)
                ctt += 1
            f.write('\n')