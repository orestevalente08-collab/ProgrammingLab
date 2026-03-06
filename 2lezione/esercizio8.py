def counter(parola):
    c = 0
    with open("file.txt", 'r') as f:
        line = f.split(" ")
        for item in line:
            if (item == parola):
                c += 1
        return c

parola = "ciao"
print(counter(parola))
