import turtle
from turtle import Turtle, Screen
import random

pen = Turtle()
turtle.colormode(255)
pen.shape("classic")
pen.speed("fastest")

def colors():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r,g,b)
    return random_colour

def draw(size_of_gap):
    for angle in range(0,360,size_of_gap):
        pen.color(colors())
        pen.circle(100) #radius
        pen.setheading(angle) #tilt


screen = Screen()
screen.bgcolor("Black")
draw(3)

screen.exitonclick()
