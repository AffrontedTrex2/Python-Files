import random

def Name():
    a = random.randint(0, 5)
    Names = ["Bob", "Robert", "Roberto", "Roberta", "Robin", "Rose"]
    print(Names[a])

def Menu():
    s = random.randint(0, 2)
    m = random.randint(0, 3)
    d = random.randint(0, 1)
    sides = ["salad", "soup", "bread"]
    mainCourse = ["salmon", "pizza", "pasta", "rice"]
    dessert = ["ice cream", "a sorbet"]
    print("Your menu is " + sides[s] + ", " + mainCourse[m] + ", and " + dessert[d] + ".")

def Haiku():
    a = random.randint(0, 1)
    b = random.randint(0, 3)
    c = random.randint(0, 1)
    d = random.randint(0, 2)
    e = random.randint(0, 0)
    fiveArticle = ["The", "A"]
    fiveNoun = ["crow", "horse", "dog", "tree"]
    fiveAdverb = ["sad.", "lonely."]
    print(fiveArticle[a] + " " + fiveNoun[b] + " is " + fiveAdverb[c])
    sevenVerb = ["jumps", "sings", "dies"]
    sevenAdverb = ["quietly, alone."]
    print("It " + sevenVerb[d] + " " + sevenAdverb[e])
    print("It's snowing on Mt. Fuji.")

Haiku()
