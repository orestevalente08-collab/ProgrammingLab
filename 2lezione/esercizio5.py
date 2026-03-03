def alfa(lista):
    parole = ["zero", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove"]
    for i, item in enumerate(lista):
        lista[i] = parole[item]

lista = [1, 3, 6, 8, 0]
alfa(lista)
print(lista)