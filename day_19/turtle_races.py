from turtle import Turtle, Screen
import random
import turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=500)
user_color_picker = screen.textinput(
    title="Color picker", prompt="Type a color for your turtle racer: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

current_position = -100
for c in colors:
    race_turtles = Turtle("turtle")
    race_turtles.color(c)
    race_turtles.penup()
    current_position += 30
    race_turtles.goto(x=-235, y=current_position)
    all_turtles.append(race_turtles)

if user_color_picker:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_color_picker:
                print(f"You won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lost! {winner_color} has win this race!")
        random_movement = random.randint(0, 10)
        turtle.forward(random_movement)

screen.exitonclick()
