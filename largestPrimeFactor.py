def primeFactor(n):
    largestFactor = n
    for i in range(2, n + 1):
        if i * i < (n + 1):
            if n % i == 0:
                n = int(n / i)
                largestFactor = n
                i = 2
    return largestFactor

print(primeFactor(600851475143))
#600851475143
