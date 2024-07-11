from turtle import Turtle, Screen, colormode
import random
import hirst_helpers

color_tuples = [(221, 232, 225), (208, 160, 81), (55, 89, 132), (145, 91, 40), (139, 26, 48)]
SPACE = 50
DOT_SIZE = 20
X_SIZE = 10
Y_SIZE = 10

tim = Turtle()
tim.speed('fastest')
tim.hideturtle()
colormode(255)
tim.penup()

def draw_line():
    tim.dot(DOT_SIZE, random.choice(color_tuples))
    tim.forward(SPACE)

current_y = -250

for _ in range(Y_SIZE):
    tim.teleport(-250, current_y)
    for _ in range(X_SIZE):
        draw_line()
    current_y += SPACE


screen = Screen()
screen.exitonclick()