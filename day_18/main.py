import random
from turtle import Screen, Turtle
import turtle
colors = [ (245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102) ]


turtle.colormode(255)

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")
screen = Screen()
screen.setup(500, 500)
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
def draw_dots(spaces_btw_dots, number_of_dots):
    for _ in range(number_of_dots):
        for _ in range(number_of_dots):
            my_turtle.dot(20, random.choice(colors))
            my_turtle.forward(spaces_btw_dots)

        my_turtle.backward(spaces_btw_dots * number_of_dots)
        my_turtle.right(-90)
        my_turtle.forward(spaces_btw_dots)
        my_turtle.left(-90)

my_turtle.penup()
draw_dots(50, 10)




screen.exitonclick()