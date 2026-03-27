def vocali (parola):
    c = 0
    for l in parola:
        if(l == "a" or l == "e" or l == "i" or l == "o" or l == "u"):
            c +=1
    return c

print(vocali("programmazione"))