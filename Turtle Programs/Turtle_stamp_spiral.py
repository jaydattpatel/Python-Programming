''' 
author : Jaydatt
turtle program to draw lines.

A turtle's pen can be picked up or put down. This allows us to move a turtle to a different place without drawing a line. The methods are 'up' and 'down'. Note that the methods 'penup' and 'pendown' do the same thing.

Every turtle can have its own shape. The ones available 'out of the box' are arrow, blank, circle, classic, square, triangle, turtle.

You can speed up or slow down the turtle's animation speed. (Animation controls how quickly the turtle turns and moves forward). Speed settings can be set between 1 (slowest) to 10 (fastest).

'''
import turtle
window = turtle.Screen()

obj = turtle.Turtle()
obj.color('blue')
obj.shape('turtle')

obj.penup() # this will not draw line when pen is up 
obj.speed(5)
distance = 2
angle = 24
for i in range(30):
    obj.stamp()
    obj. forward(distance)
    obj.right(angle)
    distance = distance + 2

obj = turtle.Turtle()
obj.color('red')
obj.shape('turtle')

obj.penup() # this will not draw line when pen is up 
obj.speed(1)

for i in range(10):
    obj. forward(50)
    obj.stamp()
    obj. forward(-50)
    obj.right(36)


window.exitonclick()