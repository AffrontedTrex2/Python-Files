class Dog():
    def __init__(self, name):
        self.name = name
        self.tricks = []
    def teachTricks(self, trick):
        self.tricks.append(trick)
    def printTricks(self):
        roundNum = 0;
        print(dog.name, "knows how to", end = " ")
        for num in range(len(self.tricks)):
            print(self.tricks[num], end = "")
            roundNum = roundNum + 1
            if len(self.tricks) <= 2:
                if roundNum <= len(self.tricks) - 1:
                    print(" and", end = " ")
                else:
                    print(".")
            else:
                if roundNum <= len(self.tricks) - 2:
                    print(",", end = " ")
                else:
                    print(", and ", self.tricks[num + 1], end = ".")
                    break
answer = "yes"
dogName = input('Name? ')
dog = Dog(dogName)
while answer == "yes" and answer != "no":
    trickName = input('Trick to teach: ')
    dog.teachTricks(trickName)
    answer = "a"
    while answer != "yes" and answer != "no":
        answer = input('Teach more tricks? ')
dog.printTricks()
