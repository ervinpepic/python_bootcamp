import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_array = []
        self.cars_speed = 5

    def create_cars(self):
        car = Turtle("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(300, random.randint(-250, 250))
        self.cars_array.append(car)

    def move(self):
        for car in self.cars_array:
            car.setheading(180)
            car.forward(self.cars_speed)

    def increase_spped(self):
        self.cars_speed += MOVE_INCREMENT
