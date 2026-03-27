def is_prime (x):
    for i in range(2, int(x/2)):
        if (x%i == 0):
            return False
    return True

x = int(input())
print(is_prime(x))