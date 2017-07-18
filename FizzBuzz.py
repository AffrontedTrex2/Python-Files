def factor(num1, num2):
    if num2 % num1 == 0:
        return True
    else:
        return False
def FizzBuzz(num):
    if num == 0:
        print("Bad number")
    elif factor(15, num):
        print("FizzBuzz")
    elif factor(5, num):
        print("Buzz")
    elif factor(3, num):
        print("Fizz")
    else:
        print("Bad number")
repeat = True
while repeat:
    number = input("Input a number: ")
    if number == "exit":
        repeat = False
    else:
        if number.isnumeric():
            num = int(number)
            FizzBuzz(num)
        else:
            print("Not a number")
