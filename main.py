from turtle import *
import turtle
import random

hirst_colors = [
    "red", "firebrick", "tomato",
    "skyblue", "blue", "navy",
    "yellow", "gold", "khaki",
    "green", "lime", "olive",
    "violet", "purple", "plum",
    "orange", "coral", "darkorange",
    "magenta", "hotpink", "deep pink",
     "white", "gray", "beige"
]

step = 50
start_x = -(10 // 2) * step
start_y = -(10 // 2) * step

win = turtle.Screen()
win.setup(width=600,height=600)
win.bgcolor("black")
win.title("Hirst's Spot Painting")

hirst = Turtle()
hirst.turtlesize(2)
hirst.shape("circle")
hirst.isvisible()
hirst.penup()

hirst.setx(start_x)
hirst.sety(start_y)

for y in range(10):
    for x in range(10):
        xpos = start_x + x * step
        ypos = start_y + y * step
        hirst.goto(xpos, ypos)
        hirst.color(random.choice(hirst_colors))
        hirst.stamp()

win.mainloop()
