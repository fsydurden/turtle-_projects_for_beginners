from turtle import Turtle, Screen
import random

pen = Turtle()
turtle.colormode(255)
pen.shape("arrow")
pen.speed("fastest")

def colors():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r,g,b)
    return random_colour



directions = [0, 90, 180, 270]

screen = Screen()
screen.bgcolor("Black")

for _ in range(200):
    colours = colors()
    pen.color(colours)
    pen.pensize(5)
    pen.forward(20)
    pen.setheading(random.choice(directions))


screen.exitonclick()
