def fattoriale (num):
    prod = 1
    for i in range(num):
        prod = prod* (num-i)
    return prod

x = int(input())
print(fattoriale(x))
