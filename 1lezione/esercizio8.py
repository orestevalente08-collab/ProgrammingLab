def invert(a, b):
    t = a
    a = b
    b = t

def triangolo (num1, num2, num3):
    if(max(num1, num2, num3) == num2):
        invert(num1, num2)
    elif(max(num1, num2, num3) == num3):
        invert(num1, num3)
    else:
        num1 = max(num1, num2, num3)
    if(num1**2 < num2**2 + num3**2 ):
        print("sono i lati di un triangolo")

a = int(input())
b = int(input())
c = int(input())
triangolo(a, b, c)