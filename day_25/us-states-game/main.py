from itertools import count
from re import S
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()
countries = []

while len(countries) < 50:
    answer_state = screen.textinput(
        title=f"{len(countries)}/50 States correct", prompt="Enter country name? ").title()
    country = data[data.state == answer_state]
    if answer_state == "Exit":
        left_countries = []
        for state in states:
            if state not in countries:
                left_countries.append(state)
        new_data = pandas.DataFrame(left_countries)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(country.x), int(country.y))
        t.write(answer_state)
        countries.append(answer_state)


