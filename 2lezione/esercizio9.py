def dictionary(file):
    dic = {}
    for i in file:
        c = 0
        for j in file:
            if (i == j):
                c += 1
        dic[f"i"] = c
    return dic

file = open('file.txt', 'r')
dic = dictionary(file.read())
print(dic)
file.close()