def isPrime(n):
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return False
    return True

def theThing():
    primeSum = 2
    for i in range(3, 2000000, 2):
        if isPrime(i) == True:
            primeSum += i
    return primeSum

print(theThing())
