def unique(new):
    with open("file.txt", 'r') as f:
        line = f.split(' ')
        for i in line:
            c = True
            for j in line:
                if (i == j):
                    c = False
                    break
            if(c):
                new.write(i)

new = open("unique.txt", 'x')
unique(new)
print(new)
new.close()