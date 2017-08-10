class Char():
    def __init__(self, n, h):
        self.name = n
        self.health = h

    def __str__(self):
        nameInfo = "Name: " + self.name
        healthInfo = "Health: " + str(self.health)
        return nameInfo + "\n" + healthInfo

    def eat(self, amount):
        self.health += amount

    def changeName(self, n):
        self.name = n

    def attack(self, otherplayer):
        otherplayer.health -= 10

player1 = Char("Almond", 100)
player2 = Char("Walnut", 200)

player1.attack(player2)
player1.changeName("Cashew")
player1.eat(1)

print(player1)
print("")
print(player2)
