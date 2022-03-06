import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
game_itration = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    game_itration += 1
    if game_itration == 5:
        cars.create_cars()
        game_itration = 0
    cars.move()

    for car in cars.cars_array:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

        elif player.is_reached_finish():
            player.reset_position()
            cars.increase_spped()
            scoreboard.update_score()

screen.exitonclick()
