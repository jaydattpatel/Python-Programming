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
win = turtle.Screen()
t1 = turtle.Turtle()
t1.pensize(3)

t1.right(36)
t1.forward(50)

t1.right(36*2)
t1.forward(50)

t1.right(36*2)
t1.forward(50)

t1.right(36*2)
t1.forward(50)

t1.right(36*2)
t1.forward(50)

t2 = turtle.Turtle()
t2.pensize(3)
t2.color('red')

t2.right(30)
t2.forward(50)

t2.right(30*2)
t2.forward(50)

t2.right(30*2)
t2.forward(50)

t2.right(30*2)
t2.forward(50)

t2.right(30*2)
t2.forward(50)

t2.right(30*2)
t2.forward(50)

win.exitonclick()