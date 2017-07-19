def methodOne():
    counter = 6
    for num in range(5):
        counter = counter - 1
        print(counter)
    print("Blastoff!")
def methodTwo():
    counter = 6
    while counter > 1:
        counter = counter - 1
        print(counter)
    print("Blastoff!")
def methodThree():
    counter = 5
    for num in range(5):
        print(counter)
        counter = counter - 1
    print("Blastoff!")
def methodFour():
    for num in range(5, 0, -1):
        print(num)
    print("Blastoff!")
def methodFive():
    for num in range(5):
        print(5 - num)
    print("Blastoff!")
def recursion(n):
    if n == 1:
        return 1
    else:
        return recursion(n - 1) + 1
def methodSix():
    for num in range(5, 0, -1):
        print(recursion(num))
    print("Blastoff!")
methodSix()
