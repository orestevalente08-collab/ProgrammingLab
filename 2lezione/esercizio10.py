def unique(file, new):
    for i in file:
        c = True
        for j in file:
            if (i == j):
                c = False
                break
        if(c == True):
            new = i

file = open('file.txt', 'r')
new = open("unique.txt", 'x')
unique(file.read(), new.write())
print(new)
file.close()
new.close()