def somma(file):
    somma = 0
    for item in file:
        somma += item
    return somma

file = open('shampoo_sales.txt', 'r')
print(somma(file.read()))
file.close()