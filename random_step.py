from turtle import Turtle, Screen
import random

r = lambda: random.randint(0,255)

tim = Turtle()

max_moves = 100
start_move = 0
angles = [0, 90, 180, 270]
tim.pensize(10)
tim.speed('fast')

while start_move < max_moves:
    color = '#%02X%02X%02X' % (r(),r(),r())
    tim.color(color)
    angle = random.choice(angles)
    tim.setheading(angle)
    tim.forward(50)
    start_move += 1

screen = Screen()
screen.exitonclick()