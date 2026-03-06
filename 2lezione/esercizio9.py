def dictionary():
    dic = {}
    with open("file.txt", 'r') as f:
        for line in f:
            item = line.split(' ')
            for i in item:
                dic[i] = dic.get(i, 0) + 1
    return dic

dic = dictionary()
print(dic)
