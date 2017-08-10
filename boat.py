class Boat():
    def __init__(self, s, c, n):
        self.speed = s
        self.color = c
        self.name = n

    def __str__(self):
        speedInfo = "Speed: " + str(self.speed)
        colorInfo = "Color: " + self.color
        nameInfo = "Name: " + self.name
        return speedInfo + "\n" + colorInfo + "\n" + nameInfo

    def changeSpeed(self, amount):
        self.speed += amount

    def changeColor(self, newColor):
        self.color = newColor

    def honking(self):
        print("HONK!")

boat = Boat(50, "White", "Hobbes")
boat.changeSpeed(100)
boat.changeColor("Orange")
boat.honking()
print(boat)
