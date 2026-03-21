def somma():
    print("Inserisci i numeri da sommare:\n")
    x = float(input("Inserisci x: "))
    y = float(input("inserisci y: "))
    print(f"La somma vale: {x+y}")
    return x+y

def differenza():
    print("Inserisci i numeri da sottrarre:\n")
    x = float(input("Inserisci x: "))
    y = float(input("inserisci y: "))
    print(f"La differenza vale: {x-y}")
    return x-y

print("Menù:\n " \
"1: Calcola la somma tra due numeri\n" \
"2: Calcola ladifferenza tra due numeri\n" \
"3: Exit\n")
n = 0
while(n != 1 and n!=  2 and n != 3):
    n = int(input("Inserisci la tua preferenza:"))

if (n == 1): somma()
if (n == 2): differenza()
print("The End\n")