def dictionary():
    dic = {}
    with open("file.txt", 'r') as f:
        line = f.split(' ')
        for i in line:
            c = 0
            for j in line:
                if (i == j):
                    c += 1
            dic[f"i"] = c
    return dic

dic = dictionary()
print(dic)
