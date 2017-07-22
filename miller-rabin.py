'''write n − 1 as 2r·d with d odd by factoring powers of 2 from n − 1
WitnessLoop: repeat k times:
   pick a random integer a in the range [2, n − 2]
   x ← ad mod n
   if x = 1 or x = n − 1 then
      continue WitnessLoop
   repeat r − 1 times:
      x ← x2 mod n
      if x = 1 then
         return composite
      if x = n − 1 then
         continue WitnessLoop
   return composite
return probably prime'''
import math
import random

def squaring(n):
    for i in range(n, 0, -1):
        if 2 ** int(math.log(i, 2)) == i:
            if n % i == 0:
                return int(math.log(i, 2)), int(n / i)

def primality(k, n):
    r, d = squaring((n - 1))
    for i in range(k):
        a = random.randint(2, n - 2)
        x = (a ** d) % n
        if x != 1 and x != n - 1:
            if r < 2:
                return 'Composite'
            else:
                for i in range(r - 1):
                    x = (x ** 2) % n
                    if x == 1:
                        return "Composite"
                    if x == n - 1:
                        break
    return "Probably Prime"
num1 = ""
num2 = ""
while not num1.isnumeric() or not num2.isnumeric():
    if not num1.isnumeric():
        num1 = input("Type in how accurate you want your calculation to be: ")
    if not num2.isnumeric():
        num2 = input("Type in the number you want to identify: ")

print(primality(int(num1), int(num2)))
