from turtle import Turtle, Screen

pen = Turtle()  #created an object of Turtle class


def draw(sides):
    """Takes n0.of sides as input and draw the shape"""
    angle = 360 / sides
    for _ in range(sides):
        pen.forward(100)
        pen.right(angle)


draw(3) #triangle
draw(5) #pentagon
draw(6) #hexagon
draw(7) #heptagon
draw(8) #octagon

#the screen exit when clicked
screen = Screen()
screen.exitonclick()
