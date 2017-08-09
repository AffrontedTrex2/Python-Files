cupcake = {
"sugar" : 2,
"butter" : 1,
"flour" : 2,
"eggs" : 1
}

jam = {
"sugar" : 5,
"fruit" : 1
}

cookies = {
"sugar" : 2,
"butter" : 2,
"flour" : 2
}

pavlova = {
"sugar" : 3,
"eggs" : 2
}

fruitTart = {
"sugar" : 2,
"butter" : 1,
"flour" : 3,
"fruit" : 2,
"eggs" : 1
}

recipeBook = {
"cupcakes" : cupcake,
"fruit tart" : fruitTart,
"jam" : jam,
"cookies" : cookies,
"pavlova" : pavlova
}

shop = {
"sugar" : 5,
"butter" : 10,
"flour" : 5,
"fruit" : 15,
"eggs" : 20
}

sellCost = {
"sugar": 1,
"butter" : 2,
"flour" : 1,
"fruit" : 3,
"cupcakes" : 100,
"fruit tart" : 150,
"jam" : 75,
"cookies" : 90,
"pavlova" : 80
}

def readFile(fileName):
    f = open(fileName, "r")
    content = f.read()
    return content

def writeFile(fileName, content):
    f = open(fileName, "w")
    f.write(content)
    f.close()

def readSaveFileMoney():
    saveFile = readFile("dictionaryproject.txt")
    word = ""
    money = 100
    for letter in saveFile:
        if letter != " ":
            word = word + letter
        else:
            money = int(word)
            break
    return money

def readSaveFile():
    saveFile = readFile("dictionaryproject.txt")
    pantry = {}
    word = ""
    isFood = False
    isMoneySkippedYet = False
    for letter in saveFile:
        if letter != " ":
            word = word + letter
        else:
            if isFood:
                pantry[word] = 0
                food = word
                isFood = False
            else:
                if isMoneySkippedYet:
                    pantry[food] = int(word)
                else:
                    isMoneySkippedYet = True
                isFood = True
            word = ""
    return pantry

money = readSaveFileMoney()
pantry = readSaveFile()

def writeSaveFile(pantry, money):
    content = ""
    content = content + str(money) + " "
    for food, amount in pantry.items():
        content = content + food + " " + str(amount) + " "
    writeFile("dictionaryproject.txt", content)

def view(money):
    print("")
    print("Money: " + str(money))
    print("Press 'p' to view pantry.")
    print("Press 'r' to view recipes.")
    print("Press 'b' to buy.")
    print("Press 's' to sell.")
    print("Press 'q' to quit.")

def printDictionary(dictionary, place):
    print("~~~~~~~~~~" + place + "~~~~~~~~~~")
    for item, amount in dictionary.items():
        print(item + "\t\tAmount: " + str(amount))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

def selling(money):
    printDictionary(pantry, "Pantry")
    print("\nWhat do you want to sell?")
    answer = input("")
    print("How many do you want to sell?")
    amount = int(input(""))
    if answer in pantry:
        if pantry[answer] > amount - 1:
            money += (sellCost[answer] * amount)
            changeInventory("subtract", answer, amount)
            print("You sold " + answer + "!")
        else:
            print("You don't have that item!")
    else:
        print("You don't have that item!")
    return money

def actions(money):
    while True:
        view(money)
        answer = input("")
        print("")
        if answer == "p":
            printDictionary(pantry, "Pantry")
        if answer == "r":
            print("~~~~~Recipes~~~~~")
            for key in recipeBook:
                print(key)
            print("~~~~~~~~~~~~~~~~~")
            make()
        if answer == "b":
            print("Money: " + str(money))
            print("")
            printDictionary(shop, "Shop")
            money = shopping(money)
        if answer == "q":
            print("Goodbye.")
            writeSaveFile(pantry, money)
            break
        if answer == "s":
            money = selling(money)

def shopping(money):
    print("\nWhat would you like to buy?")
    item = input("")
    print("How many do you want to buy?")
    amount = int(input(""))
    if item in shop:
        if money >= (shop[item] * amount):
            money -= (shop[item] * amount)
            changeInventory("add", item, amount)
            print("You bought " + item + "!")
        else:
            print("You don't have enough money!")
    else:
        print("That's not in the store.")
    return money

def youHaveTheStuff(pantry, recipe, amount):
    for key in recipe:
        if pantry[key] < recipe[key] * amount:
            return False
    return True

def changeInventory(typeOfChange, item, amount):
    if typeOfChange == "add":
        if item in pantry:
            pantry[item] += amount
        else:
            pantry[item] = amount
    if typeOfChange == "subtract":
        pantry[item] -= amount

def make():
    print("\nWhat would you like to make?")
    item = input("")
    if item in recipeBook:
        printDictionary(recipeBook[item], "Recipe")
        print("\nMake this item?")
        answer = input("")
        if answer.lower() == "yes":
            print("How many of this item do you want to make?")
            amount = int(input(""))
            recipe = recipeBook[item]
            if youHaveTheStuff(pantry, recipe, amount):
                for key in recipe:
                    pantry[key] -= (recipe[key] * amount)
                print("You made " + item + "!")
                changeInventory("add", item, amount)
            else:
                print("You don't have enough ingredients.")

actions(money)
