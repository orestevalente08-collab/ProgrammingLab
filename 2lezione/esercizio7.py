def somma():
    with open("file.txt", 'r') as f:
        somma = 0
        contenuto = f.read()
        for line in contenuto:
            parola = line.split(',')
            somma += float(parola)
    return somma

print(somma())