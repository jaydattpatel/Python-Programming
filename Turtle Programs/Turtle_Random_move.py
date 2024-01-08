'''
we have a working program that draws a random walk of our turtle that has a 90% chance of staying on the screen. We are in a good position, because a large part of our program is working and we can focus on the next bit of work – deciding whether the turtle is inside the screen boundaries or not.

We can find out the width and the height of the screen using the window_width and window_height methods of the screen object. However, remember that the turtle starts at position 0,0 in the middle of the screen. So we never want the turtle to go farther right than width/2 or farther left than negative width/2. We never want the turtle to go further up than height/2 or further down than negative height/2. Once we know what the boundaries are we can use some conditionals to check the turtle position against the boundaries and return False if the turtle is outside or True if the turtle is inside.
'''

import random
import turtle

def isInScreen(win,t):
    leftBound = - win.window_width() / 2
    rightBound = win.window_width() / 2
    topBound = win.window_height() / 2
    bottomBound = -win.window_height() / 2

    turtleX = t.xcor() # get x-cordinate of turtle
    turtleY = t.ycor() # get x-cordinate of turtle

    print("x : {:.2f}, y : {:.2f} ".format(t.xcor(),t.ycor()))
    
    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

t = turtle.Turtle()
win = turtle.Screen()
print("win.wid : {:.2f}, win.hgt : {:.2f}".format(win.window_width(),win.window_height()))

print("leftBound : {:.2f}, rightBound : {:.2f} , topBound : {:.2f}, bottomBound : {:.2f}".format
    ((-win.window_width()/2), (win.window_width()/2),(win.window_height()/2),(-win.window_height()/2)))
t.shape('turtle')
while isInScreen(win,t):
    ran = random.randrange(0, 2)
    if ran == 0:
        t.left(90)
    else:
        t.right(90)
    t.forward(50)


win.exitonclick()

