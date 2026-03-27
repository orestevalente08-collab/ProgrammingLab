def unique(new):
    with open("file.txt", 'r') as f:
        counts = {}
        for line in f:
            item = line.split(' ')
            for i in item:
                counts[i] = counts.get(i, 0) +1
        for parola, c in counts.items():
            if c==1:
                new.write(parola + '\n')

new = open("unique.txt", 'w')
unique(new)
new.close()