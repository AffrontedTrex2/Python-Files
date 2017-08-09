goodbye = {
"french" : "au revoir",
"spanish" : "adios"
}

hello = {
"french" : "bonjour",
"spanish" : "hola"
}

dictionary = {
"hello" : hello,
"goodbye" : goodbye
}

for key in dictionary:
    print(key)

word = input("\nWhat phrase would you like to translate? ")

language = input("\nWould you like to translate it into french or spanish? ")

location = dictionary[word]
print(location[language])
