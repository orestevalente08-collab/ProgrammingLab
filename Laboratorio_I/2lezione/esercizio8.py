def counter(parola):
    c = 0
    with open("file.txt", 'r') as f:
        for line in f:
            divisi = line.split(" ")
            for item in divisi:
                if (item == parola):
                    c += 1
        return c

parola = "carta"
print(counter(parola))
