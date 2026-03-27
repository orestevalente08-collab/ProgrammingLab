def Terna_Pit(x, y):
    return x**2+y**2
l = [[a, b, c] for a in range(1, 21) for b in range(1, 21) for c in range(1, 21) if(Terna_Pit(a, b)== c**2)]
print(l)
