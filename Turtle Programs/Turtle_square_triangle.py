''' 
author : Jaydatt
turtle program to draw lines.

methods: 
obj.forward(length)
obj.back(length)
obj.left(degree)
obj.right(degree)

attribute:
obj.color()
obj.pensize()
obj.heading()
obj.position()
obj.width()

'''

import turtle   # allows us to use the turtles library
window = turtle.Screen()    # creates a graphics window
window.bgcolor('lightgreen')

# draw squre 
obj = turtle.Turtle()    # create a turtle named obj
obj.color('blue')
obj.pensize(3)

obj.forward(150)    # tell obj to move forward by 150 units
obj.left(90)    # turn by 90 degrees
obj.forward(75)    # complete the second side of a rectangle
obj.left(90)
obj.forward (150)
obj.left(90)
obj.forward(75)


# draw triangle
obj2 = turtle.Turtle()
obj2.color("red")  # make obj2 blue
obj2.pensize(3)    # set the width of her pen

obj2.back(150)
obj2.left(60)
obj2.forward(150)
obj2.right(120)
obj2.forward(150)

window.exitonclick() # wait for input to exit window screen



