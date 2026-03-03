def counter(file, parola):
    c = 0
    for item in file:
        if (item == parola):
            c += 1
    return c

file = open('file.txt', 'r')
parola = "ciao"
print(counter(file.read(), parola))
file.close()