import sys

def readFile(fileName):
    f = open(fileName, "r")
    content = f.readline()
    content = content.lower()
    return content

def writeFile(fileName, content):
    f = open(fileName, "w")
    f.write(content)
    f.close()

def encodeLetter(key, letter):
    asciiLetter = ord(letter)
    key = key % 26
    asciiLetter += key
    if asciiLetter > 122:
        asciiLetter -= 26
    return asciiLetter

def decodeLetter(key, letter):
    asciiLetter = ord(letter)
    key = key % 26
    asciiLetter -= key
    if asciiLetter < 97:
        asciiLetter += 26
    return asciiLetter

def encodeWord(key, word):
    encoded = ""
    for i in range(len(word)):
        encodedLetter = encodeLetter(key, word[i])
        encodedLetter = chr(encodedLetter)
        encodedLetter = punctuation(encodedLetter)
        encoded += encodedLetter
    return encoded

def decodeWord(key, word):
    decoded = ""
    for i in range(len(word)):
        decodedLetter = decodeLetter(key, word[i])
        decodedLetter = chr(decodedLetter)
        decodedLetter = punctuation(decodedLetter)
        decoded += decodedLetter
    return decoded

def caesar(key, action, inputFile, outputFile):
    readThis = readFile(inputFile)
    if action == "-e":
        result = encodeWord(key, readThis)
    elif action == "-d":
        result = decodeWord(key, readThis)
    writeFile(outputFile, result)

def punctuation(letter):
    asciiLetter = ord(letter)
    if asciiLetter < 97 or asciiLetter > 122:
        asciiLetter = 32
    return chr(asciiLetter)

key = int(sys.argv[1])
inputFile = sys.argv[3]
outputFile = sys.argv[4]
action = sys.argv[2]

caesar(key, action, inputFile, outputFile)
