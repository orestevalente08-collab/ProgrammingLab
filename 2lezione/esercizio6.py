def occ(lista):
    dic = {}
    for i in lista:
        c = 0
        for j in lista:
            if(i == j):
                c += 1
        dic [f"{i}"] = c
    return dic

lista = ["DIZIONARIO", "SEPPIA", "SEDIA", "SEPPIA"]
dic = occ(lista)
print(dic)