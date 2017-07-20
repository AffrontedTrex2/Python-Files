def recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive(n - 1) + recursive(n - 2)

def iterative(n):
    x = 0
    y = 1
    for num in range(n):
        x, y = y, x + y
    return x

for i in range(1, 10):
    print(iterative(i), end = " ")
