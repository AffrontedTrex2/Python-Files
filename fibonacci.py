def recursive(n): #.25
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive(n - 1) + recursive(n - 2)

def iterative(n): #.2
    x = 0
    y = 1
    for num in range(n):
        x, y = y, x + y
    return x

def dictRecursive(n): #.22
    values = {0 : 0, 1 : 1}
    if n not in values:
        values[n] = dictRecursive(n - 1) + dictRecursive(n - 2)
    return values[n]

for i in range(1, 20):
    print(iterative(i), end = " ")
