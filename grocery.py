class Food():
    def __init__(self, n, p):
        self.name = n
        self.price = p

class GroceryCart():
    def __init__(self):
        self.foodDict = {}
        self.totalCost = 0

    def __str__(self):
        string = ""
        for food in self.foodDict:
            subtotal = self.foodDict[food] * food.price
            string += "Food: " + food.name + "\tPrice: $" + str(food.price) + "\tQuantity: " + str(self.foodDict[food]) + "\tSubtotal: $" + str(subtotal) + "\n"
        costInfo =  "Total Cost: $" + str(self.totalCost)
        return string + costInfo

    def total(self):
        for food in self.foodDict:
            self.totalCost += food.price * self.foodDict[food]

    def addFood(self, foodName, amount):
        if foodName in self.foodDict:
            self.foodDict[foodName] += amount
        else:
            self.foodDict[foodName] = amount
        self.total()

    def removeItem(self, foodName, amount):
        if foodName in self.foodDict:
            if self.foodDict[foodName] == amount:
                del self.foodDict[foodName]
            elif self.foodDict[foodName] < amount:
                return False
            else:
                self.foodDict[foodName] -= amount
            self.total()
            return True
        else:
            return False

carrot = Food("carrot", 3)
tomato = Food("tomato", 2)

cart = GroceryCart()
cart.addFood(carrot, 1)
cart.addFood(tomato, 15)
print(cart)
cart.removeItem(tomato, 14)
print(cart)
