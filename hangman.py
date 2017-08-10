possibleWords = {"dogs", "saltine", "ugly", "triangle", "cake",
"salina", "potato", "nesus", "narwhal", "abruptly", "buffalo",
"equip", "ivy", "jiujitsu", "oxygen", "vodka", "waltz", "galaxy",
"czechoslovakia", "jazz", "puzzle", "bagpipes", "cobweb", "dwarves",
"ivory", "haiku", "icebox", "jaywalk", "jigsaw", "juicy", "luxury",
"microwave", "mystify", "pixel", "polka", "quiz", "sphinx", "subway",
"vortex", "wavy", "wizard", "zodiac", "zombie", "avenue", "cycle",
"glyph", "wyvern", "yummy", "fluff", "unzip"}

score = 0

def readFile(fileName):
    f = open(fileName, "r")
    content = f.readline()
    return content

#writes file
def writeFile(fileName, content):
    f = open(fileName, "w")
    f.write(content)
    f.close()

#interprets the file so that the file is put into a dictionary format, and returns a dictionary
def readScoreboard():
    scoreboard = readFile("hangman.txt")
    scoreTable = {}
    word = ""
    isPerson = True
    for letter in scoreboard:
        if letter != " ":
            word = word + letter
        else:
            if isPerson:
                scoreTable[word] = 0
                person = word
                isPerson = False
            else:
                scoreTable[person] = int(word)
                isPerson = True
            word = ""
    return scoreTable

def writeScoreboard(scoreboard):
    content = ""
    for name, number in scoreboard.items():
        content = content + name + " " + str(number) + " "
    writeFile("hangman.txt", content)

scoreboard = readScoreboard()
user = input("Enter your name: ")

wordGuessed = False
gameOver = False

while gameOver == False:
    emptyLetters = ""
    word = possibleWords.pop()
    numOfLetters = 0
    numOfSpaces = 0
    guessedLetters = {}
    guessedLetters = set(guessedLetters)
    correctLetters = 0

    triesLeft = 10

    for i in range(len(word)):
        numOfLetters += 1

    completedWordArray = [" "] * (numOfLetters * 2 - 1)

    for i in range(numOfLetters):
        emptyLetters += "- "

    print(emptyLetters)

    while wordGuessed == False or gameOver == False:
        completedWord = ""
        guess = input("Guess a letter: ")
        if guess in word and guess not in guessedLetters:
            for i in range(len(word)):
                if word[i] == guess:
                    location = i
                    numOfSpaces = location * 2

                    completedWordArray[numOfSpaces] = guess

                    correctLetters += 1
        else:
            if guess in guessedLetters:
                print("You've already guessed this letter.")
            else:
                triesLeft -= 1

        guessedLetters.add(guess)

        for i in completedWordArray:
            completedWord += i

        print(completedWord)
        print(emptyLetters)
        print("Tries left: " + str(triesLeft))

        if triesLeft <= 0:
            gameOver = True
            break

        if correctLetters == len(word):
            wordGuessed = True
            break

    if wordGuessed:
        print("Good job! You won.")
        wordGuessed = False
        score += 1

if user in scoreboard:
    if score > scoreboard[user]:
        scoreboard[user] = score
else:
    scoreboard[user] = score

print("You lost! The word was '" + word + "'")

print("\n~~~~~~~~Highscores~~~~~~~~")
for name, score in scoreboard.items():
    print(name + "\t\tScore: " + str(score))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

writeScoreboard(scoreboard)
