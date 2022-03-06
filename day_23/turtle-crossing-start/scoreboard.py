from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-230, 260)
        self.write(f"Level: {self.score}", align="center", font=FONT)
        self.score += 1

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
