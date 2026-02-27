def numero_l (parola, lettera):
    c = 0
    for l in parola:
        if (l == lettera):
            c = c +1
    return c

print(numero_l("programmazione", "r"))