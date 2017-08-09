def swap(firstElement, secondElement, listName):
    a = listName[firstElement]
    listName[firstElement] = listName[secondElement]
    listName[secondElement] = a

def bubblesort(listName):
    length = len(listName)
    while length > 1:
        for i in range(length-1):
            if listName[i] > listName[i + 1]:
                swap(i, i + 1, listName)
        length -= 1

potato = [1, 8, 9, 24, 82, 33]
bubblesort(potato)
print(potato)
