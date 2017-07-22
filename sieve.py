number = ""
while not number.isnumeric():
    number = input("Type in a number: ")
number = int(number)

array = ["", ""]
for i in range(2, number + 1):
    array.append(True)
for i in range(2, number + 1):
    if i ** 2 < number:
        if array[i] == True:
            for j in range(i, number + 1, i):
                if j < number + 1 and j != i:
                    array[j] = False
    else:
        break
for i in range(len(array)):
    if array[i]:
        print(i, end = " ")
