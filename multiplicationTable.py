def multiply(n, factor): #Returns numbers that are multiples of that factor
    if n == 1:
        return factor
    else:
        return multiply(n - 1, factor) + factor
def cycle(numOfCycles, factor): #Prints the line of numbers
    for i in range(1, numOfCycles + 1):
        print(multiply(i, factor), end = "\t")
    print("")
    print("")
def table(rows, columns): #Prints the table
    for i in range(rows):
        cycle(columns, i + 1)


table(6, 5)
