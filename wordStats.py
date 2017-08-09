def wordStats(word):
    wordDictionary = {}
    for letter in word:
        if letter in wordDictionary:
            wordDictionary[letter] += 1
        else:
            wordDictionary[letter] = 1
    return wordDictionary

word = input("Type a word: ")
wordDictionary = wordStats(word)
for letter, number in wordDictionary.items():
    print("Letter: " + letter + "\tAppeared: " + str(number) + " times")
