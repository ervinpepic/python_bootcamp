from hashlib import blake2b
import time
from turtle import Screen
from ball import Ball
from padle import Padle
from scoreboard import Scoreborad

ball_speed = 6

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

padle1 = Padle(goto_x=350, goto_y=0)
padle2 = Padle(goto_x=-350, goto_y=0)
ball = Ball()
score = Scoreborad()

screen.listen()

screen.onkey(padle1.move_up, "Up")
screen.onkey(padle1.move_down, "Down")
screen.onkey(padle2.move_up, "w")
screen.onkey(padle2.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_first_start()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()


    if ball.distance(padle1) < 50 and ball.xcor() > 320 or ball.distance(padle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_position()
        score.update_score_l()


    if ball.xcor() < -380:
        ball.reset_position()
        score.update_score_r()


screen.exitonclick()
