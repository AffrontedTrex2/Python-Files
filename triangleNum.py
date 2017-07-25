def triangleNum():
    triangleArray = []
    for i in range(1, 2000000):
        triangleArray.append(recursiveAdd(i))
    return triangleArray
def recursiveAdd(n):
    if n <= 1:
        return 1
    else:
        return recursiveAdd(n - 1) + n
def findFactors():
    triangle = triangleNum()
    numOfFactors = []
    factorSub = 0
    for i in triangle:
        for i2 in range(1, i + 1):
            if i2 ** 2 < i or i < 50:
                if i % i2 == 0:
                    factorSub += 1
            else:
                break
        numOfFactors.append(factorSub)
        factorSub = 0
    return numOfFactors
print(findFactors())
