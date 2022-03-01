from turtle import Turtle, Screen
import turtle


turtle_1 = Turtle()
turtle_1.shape("circle")
turtle_1.color("red")

# # for _ in range(4):
# #     turtle_1.left(90)
# #     turtle_1.forward(100)
import random
turtle.colormode(255)



def random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple

turtle_1.speed(0)
# directions = [0, 90, 180, 270]
# for i in range(1, 37):
#     turtle_1.circle(100)
#     turtle_1.left(10)
#     turtle_1.pencolor(random_rgb())

def draw_spyrograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle_1.pencolor(random_rgb())
        turtle_1.circle(100)
        turtle_1.setheading(turtle_1.heading() + size_of_gap)

draw_spyrograph(size_of_gap=5)

# for _ in range(200):
#     turtle_1.forward(40)
#     turtle_1.pencolor(random_rgb())
#     turtle_1.setheading(random.choice(directions))


# def shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         turtle_1.forward(100)
#         turtle_1.right(angle)
# import random

# for shape_sizes in range(3, 11):
#     turtle_1.color(random.choice(colors))
#     shape(shape_sizes)


scr = Screen()
scr.exitonclick()