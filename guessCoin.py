import random

#reads file
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
    scoreboard = readFile("scoreboard.txt")
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

#writes the scoreboard so that it can be read by the readScoreboard function
def writeScoreboard(scoreboard):
    content = ""
    for name, number in scoreboard.items():
        content = content + name + " " + str(number) + " "
    writeFile("scoreboard.txt", content)

#prints the scoreboard ingame after the user loses
def printScoreboard(scoreboard):
    for name, number in scoreboard.items():
        print("User: " + name + "\tScore: " + str(number))

#reads the scoreboard, asks the user for their name, and sets their score to zero
scoreboard = readScoreboard()
missed = False
user = input("Enter a name: ")
score = 0

while not missed:
    #user guesses heads or tails
    guess = input("\nHeads or tails? ")
    #computer generates heads or tails
    randomNum = random.randrange(1, 3)
    if randomNum == 1:
        randomNum = "heads"
    else:
        randomNum = "tails"

    #if the user guesses correctly, their score increases; else, the game ends
    if guess.lower() == randomNum:
        score += 1
        print("Good job")
    else:
        print("Game over")
        missed = True

#replace the scoreboard's score if the user's score is higher
if user in scoreboard:
    if score > scoreboard[user]:
        scoreboard[user] = score
else:
    scoreboard[user] = score
#prints the highscore table
print("\nHighscores")
printScoreboard(scoreboard)
#writes the table to the file
writeScoreboard(scoreboard)
