from turtle import *

# Name your Turtle.
Steve = Turtle()

# Set Up your screen and starting position.
setup(900,500)
x_pos = -250
y_pos = -150
Steve.penup()
Steve.setposition(x_pos, y_pos)
Steve.pendown()


### Write your code below:
length = 50
#Draw any shape
def Level3():
    #Sets pen color and side number
    sides = input('How many sides?')
    sides = int(sides)
    color = input('Which color?')
    Steve.pencolor(color)
    #Draws shape
    for number in range(sides):
        Steve.forward(length)
        Steve.right(360/sides)
#Draws square and triangle
def Level1():
    #Draws square
    for number in range(4):
        Steve.forward(length)
        Steve.right(90)
    #Resets position
    Steve.penup()
    Steve.setposition(0,0)
    Steve.pendown()
    #Draws triangle
    for number in range(3):
        Steve.forward(length)
        Steve.left(120)

        
Level1()

# Close window on click.
exitonclick()
