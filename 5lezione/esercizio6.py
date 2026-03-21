b = False
while(b == False):
    try:
        x = int(input())
        b = True
    except ValueError:
        print("il valore inserito non è valido. Riprova\n")