#looking for the object
def binarySearch(listName, item):
#setting the left and right boundaries
    left = 0
    right = len(listName) - 1
#in case of overlap, break glass
    while left <= right:
        average = int((right + left) / 2)
#if found, return the placement
        if listName[average] == item:
            return average
#if too high, lower the upperbound
        if listName[average] > item:
            right = average - 1
#if too low, raise the lowerbound
        else:
            left = average + 1
    return -1

#exemacution
potato = [1, 2, 3, 4, 5]
print(binarySearch(potato, 6))
