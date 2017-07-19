userInput = "wwwbbrwrbrbrrbrbrwrwwrbwrwrrb"
necklace = userInput + userInput
necklaceArray = [] #I don't think we need two arrays but lul too late
necklaceArray2 = necklaceArray #necklaceArray2 doesn't have any w's
mostBeads = 0
beadNum = 1

for num in necklace: #Creates the necklaceArray
    necklaceArray.append(num)
for num in range(len(necklaceArray)): #Sets necklaceArray2 as a copy with no w's
    if necklaceArray[num] == "w":
        if num != 0:
            necklaceArray2[num] = necklaceArray2[num - 1]
for num in range(len(necklaceArray2)): #Cycle through every single letter
    beads = 0
    changedColor = 0
    for num in range(beadNum, len(necklaceArray2)): #Start at the next letter every cycle
        if changedColor != 2: #If we haven't changed color yet
            if necklaceArray[num] == "w": #If it's a w, add a bead
                beads = beads + 1
            elif necklaceArray[num] == necklaceArray[num - 1]: #If the color is same as the previous one, add a bead
                beads = beads + 1
            else:
                changedColor = changedColor + 1 #If not, then we've changed color and still added a bead
                beads = beads + 1
        else:
            if beads > mostBeads: #If we've already changed color, update the new mostBeads
                mostBeads = beads
            break #Stop counting
    beadNum = beadNum + 1
if necklaceArray2[1] == necklaceArray2[0] or necklaceArray2[0] == "w" or necklaceArray2[1] == "w":
    mostBeads = mostBeads + 1
if mostBeads > len(necklaceArray):
    mostBeads = len(necklaceArray)
print(mostBeads)
