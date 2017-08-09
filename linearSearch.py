def linearSearch(listName, number):
    #goes through list and tries to match target with list objects
    for i in range(len(listName)):
        if listName[i] == number:
            return i
    #if there's no match, return a diff output
    return -1

#the list
potato = [1, 2, 3, 4, 5]
#the exemacution
print(linearSearch(potato, 3))
