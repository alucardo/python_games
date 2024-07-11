from turtle import Turtle, Screen
import random

r = lambda: random.randint(0,255)

tim = Turtle()
FULL = 360
angles = 3

while angles < 10:
    rotation = FULL / angles
    color = '#%02X%02X%02X' % (r(),r(),r())
    tim.color(color)
    for _ in range(angles):
        tim.forward(100)
        tim.right(rotation)
    angles += 1

screen = Screen()
screen.exitonclick()