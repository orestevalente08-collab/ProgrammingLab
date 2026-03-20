list_a = [0, 1, 3, 4]
list_b = ['a', 'b', 'c']
l = [(n, l) for n in list_a if n%2==0 for i, l in enumerate(list_b) if i%2 != 0]
print(l)