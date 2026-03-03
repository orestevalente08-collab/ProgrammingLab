def somma_list (lista):
    somma = 0
    for i in lista:
        somma = somma + i
    return somma

lista = [2, 3, 6, 8]
print(somma_list (lista))