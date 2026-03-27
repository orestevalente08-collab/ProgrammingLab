def scambia(lista, i, j):
    t = lista[i]
    lista[i] = lista[j]
    lista[j] = t

lista = [1, 2, 3]
i = int(input("Inserisci il primo indice: "))
j = int(input("Inserisci il secondo indice: "))
scambia(lista, i, j)
print(lista)