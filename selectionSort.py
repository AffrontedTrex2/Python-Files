#find min value
def minimum(listName):
    smallestLocation = 0
    #goes through list and compares values
    for i in range(len(listName)):
        if listName[i] < listName[smallestLocation]:
            smallestLocation = i
    return smallestLocation

#execute the sorting
def selectionSort(listName):
    #placeholder list
    newList = []
    #popping into new list and return to old lis
    for i in range(len(listName)):
        minLocation = minimum(listName)
        minValue = listName.pop(minLocation)
        newList.append(minValue)
    listName.extend(newList)

#exemacution
potato = [4, 12, 7, 5, 60, 10000]
selectionSort(potato)
print(potato)
