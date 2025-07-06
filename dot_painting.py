# import colorgram
# colours = colorgram.extract("image.jpg",20)
# rgb_colors = []
# for color in colours:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
#above code only need to run once, then you can comment it like i did.

import random
import turtle
from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()
screen.bgcolor("White")
color_list = [(225, 238, 248), (252, 241, 232), (244, 251, 248), (83, 87, 219), (248, 232, 236), (37, 42, 159), (250, 84, 53), (15, 189, 169), (228, 145, 75), (156, 171, 234), (72, 157, 235), (36, 89, 180), (6, 151, 146), (250, 54, 82), (1, 118, 115), (252, 153, 0), (254, 204, 0), (249, 203, 25), (12, 28, 69), (146, 218, 225)]

turtle.colormode(255)
pen.penup()
pen.hideturtle()
pen.speed(0)

pen.setheading(225)
pen.forward(300)
pen.setheading(0)
for row in range(10):
    for col in range(10):
        pen.dot(20, random.choice(color_list))  # dot size, color
        pen.forward(50)  # Space between dots
    pen.setheading(90)
    pen.forward(50)
    pen.setheading(180)
    pen.forward(500)
    pen.setheading(0)

screen.exitonclick()
