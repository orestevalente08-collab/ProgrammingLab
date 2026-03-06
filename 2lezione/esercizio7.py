def somma():
    with open("shampoo_sales.csv", 'r') as f:
        somma = 0
        for line in f:
            parola = line.split(',')
            for item in parola:
                try:
                    somma += float(item)
                except ValueError:
                    pass
    return somma

print(somma())