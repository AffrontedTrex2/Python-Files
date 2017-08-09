possibleWords = {"dogs", "saltine", "ugly", "triangle", "cake", "salina", "potato", "nesus", "narwhal",
"abruptly", "buffalo", "equip", "ivy", "jiujitsu", "oxygen", "vodka", "waltz", "czechoslovakia", "jazz", "puzzle"}
possibleWords = set(possibleWords)
emptyLetters = ""
word = possibleWords.pop()
numOfLetters = 0
numOfSpaces = 0
guessedLetters = {}
guessedLetters = set(guessedLetters)
wordGuessed = False
gameOver = False
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

if gameOver:
    print("You lost! The word was '" + word + "'")
if wordGuessed:
    print("Good job! You won.")
