def Left():
    amount = int(input("How many? "))
    hashAmount = 1
    for num in range(amount): #Repeats for the number of lines wanted
        for num2 in range(hashAmount): #Repeats for the number of hashes wanted per line-starts at one
            print("#", end = "")
        print("") #Skips to next line
        hashAmount = hashAmount + 1 #Adds a hash for every line
def Right():
    amount = int(input("How many? "))
    hashAmount = amount
    hashAmount2 = 1
    hashAmount3 = hashAmount2
    for num in range(amount): #Repeats for the number of lines wanted
        for num2 in range(hashAmount + 1, 0, -1): #Counts down to see how many spaces are needed
            print(" ", end = "") #Prints spaces
        while hashAmount3 > 0:
            print("#", end = "") #Prints hashes depending on which line
            hashAmount3 = hashAmount3 - 1
        print("")
        hashAmount = hashAmount - 1
        hashAmount2 = hashAmount2 + 1
        hashAmount3 = hashAmount2
def Middle():
    amount = int(input("How many? "))
    lineNum = 1
    largestHashAmount = amount * 2 - 1
    for num in range(amount): #Repeats for the number of lines wanted
        hashAmount = lineNum * 2 - 1 #Sets new number of hashes needed on current line
        for num in range(int(largestHashAmount - hashAmount / 2)): #Spaces before hashes
            print(" ", end = "")
        for num in range(hashAmount): #Hashes
            print("#", end = "")
        for num in range(int(largestHashAmount - hashAmount / 2)): #Spaces after hashes
            print(" ", end = "")
        print("")
        lineNum = lineNum + 1
#Choose which type
answer = input("Left, right, or middle? ")
if answer.lower() == "left":
    Left()
elif answer.lower() == "right":
    Right()
elif answer.lower() == "middle":
    Middle()
