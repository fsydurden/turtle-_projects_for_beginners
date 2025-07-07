from turtle import Turtle,Screen

pen = Turtle()
screen = Screen()

def move_forward():
    pen.forward(10)
    #function to move forward

def move_backwards():
    pen.backward(10)
    #function to move backward


def clock_wise():
    pen.right(10)
    #function to turn clockwise

def anti_clockwise():
    pen.left(10)
    #function to turn anti clockwise

def clear_screen():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()
    #function that clears the screen, penup is used because it will draw a line backwardif not used.


screen.listen()
screen.onkey(key="space", fun=clear_screen)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=clock_wise)
screen.onkey(key="d", fun=anti_clockwise)

screen.exitonclick()

