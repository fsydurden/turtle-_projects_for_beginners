from turtle import Turtle,Screen

pen = Turtle()
screen = Screen()

def move_forward():
    pen.forward(10)

def move_backwards():
    pen.backward(10)


def clock_wise():
    pen.right(10)

def anti_clockwise():
    pen.left(10)

def clear_screen():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()


screen.listen()
screen.onkey(key="space", fun=clear_screen)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=clock_wise)
screen.onkey(key="d", fun=anti_clockwise)

screen.exitonclick()

