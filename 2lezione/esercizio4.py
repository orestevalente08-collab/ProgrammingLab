def simili(l1, l2):
    for i1, o1 in enumerate(l1):
        for i2, o2 in enumerate(l2):
            if(o1 == o2):
                return True
    return False

l1 = [1, 4, 5, 9, 12]
l2 = [3, 6, 8, 7]
print(simili(l1, l2))