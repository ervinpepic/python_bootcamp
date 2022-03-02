from turtle import Turtle, Screen, back, left
import turtle


screen = Screen()
screen.setup(500, 500)

turtle_1 = Turtle()


def move_turtle():
    turtle_1.fd(10)


def backward_turtle():
    turtle_1.forward(10)


def right_turtle():
    turtle_1.right(10)


def left_turtle():
    turtle_1.left(10)

def clear():
    screen.clear()
    turtle_1.penup()
    turtle_1.home()
    turtle_1.pendown()
    turtle_1.shape("turtle")

screen.onkeypress(fun=backward_turtle, key='s')
screen.onkeypress(fun=left_turtle, key='a')
screen.onkeypress(fun=right_turtle, key='d')

screen.listen()
screen.onkey(fun=move_turtle, key="w")
screen.onkey(fun=backward_turtle, key="s")
screen.onkey(fun=left_turtle, key="a")
screen.onkey(fun=right_turtle, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
