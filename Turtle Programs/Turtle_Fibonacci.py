
# Python program for plot Fibonacci Spiral Fractal using Turtle
import turtle
import math

def fiboPlotSqure(n):
   prev = 0
   curr = 1
   y.pencolor("blue")
   print(curr)
   # Drawing the first sqr
   y.forward(curr * fac)
   y.left(90)
   y.forward(curr * fac)
   y.left(90)
   y.forward(curr * fac)
   y.left(90)
   y.forward(curr * fac)
   
   # Drawing the rest of the sqrs
   for i in range(1, n):
        next = curr + prev
        prev = curr
        curr = next
        print(curr)

        y.backward(prev * fac)
        y.right(90)
        y.forward(curr * fac)
        y.left(90)
        y.forward(curr * fac)
        y.left(90)
        y.forward(curr * fac)




def fiboPlotSpiral(n):
   prev = 0
   curr = 1

   # Bringing the pen to starting point of the spiral plot
   y.penup()
   y.setposition(fac, 0)
   y.seth(0)
   y.pendown()

   # Set the color of the plotting pen to red
   y.pencolor("red")

   # Fibonacci Spiral Plot
   y.left(90)
   for i in range(n):
       print(curr)
       fwd = math.pi * curr * fac / 2
       fwd /= 90
       for j in range(90):
           y.forward(fwd)
           y.left(1)
       next = curr + prev
       prev = curr
       curr = next



win = turtle.Screen()
win.bgcolor('black')

y = turtle.Turtle()
y.pensize(2)
y.speed(100)

fac = 7
m = 10 # no. of fibonacci series
print("Fibonacci ploting Squre :")
fiboPlotSqure(m)
print("Fibonacci ploting Spiral :")
fiboPlotSpiral(m)

win.exitonclick()
