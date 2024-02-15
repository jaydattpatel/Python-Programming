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
import turtle
window = turtle.Screen()

# line spiral draw
obj = turtle.Turtle()
obj.pensize(3)
distance = 50
angle = 90
for i in range(16):
    obj. forward(distance)
    obj.right(angle)
    distance = distance + 10
    angle = angle - 3

# Squre spiral draw
obj = turtle.Turtle()
obj.color('red')
obj.pensize(3)

distance = 50
angle = 90
for i in range(16):
    obj. forward(distance)
    obj.right(angle)
    distance = distance + 10

# spiral circle draw
obj = turtle.Turtle()
obj.color('blue')
obj.pensize(3)

for i in range(300):
    obj.forward(0.1 + (i*0.1))
    obj.right(10)


window.exitonclick()