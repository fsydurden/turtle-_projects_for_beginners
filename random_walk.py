from turtle import Turtle, Screen
import random

pen = Turtle()
pen.shape("arrow")
colors = ["red", "blue", "green", "yellow", "orange", "purple", "cyan"]
directions = [0, 90, 180, 270]

screen = Screen()
screen.bgcolor("Black")

for _ in range(200):
    pen.color(random.choice(colors))
    pen.pensize(5)
    pen.forward(20)
    pen.setheading(random.choice(directions))


screen.exitonclick()
