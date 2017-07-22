from PIL import Image

#Values for each color
darkerBlue = (1, 7, 17)
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

def changeColor(imageName):
    #Imports picture and converts the pixel data to a list
    im = Image.open(imageName)
    pixelData = im.getdata()
    pixelData = list(pixelData)
    recolored = []

    #pixelSum is the sum of the tuples
    pixelSum = [sum(tup) for tup in pixelData]
    #Changes the color and adds it to the array based on the value of pixelSum
    for i in pixelSum:
        if i <= 120:
            recolored.append(darkerBlue)
        if i < 182 and i > 120:
            recolored.append(darkBlue)
        if i >= 182 and i < 364:
            recolored.append(red)
        if i >= 364 and i < 546:
            recolored.append(lightBlue)
        if i >= 546:
            recolored.append(yellow)

    # Create a new image using the recolored list. Display and save the image.
    new_image = Image.new("RGB", im.size) #Creates a new image that will be the same size as the original image.
    new_image.putdata(recolored) #Adds the data from the recolored list to the image.
    new_image.show() #show the new image on the screen
    new_image.save("Images\\recolored.jpg", "jpeg") #save the new image as "recolored.jpg"

changeColor("Images\\nevada.jpg")
