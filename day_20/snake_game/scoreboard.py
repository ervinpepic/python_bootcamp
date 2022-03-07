
from turtle import Turtle
from datetime import datetime
FONT = (["Arial", 20, "bold"])
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0

        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}",
                   align="Right", font=FONT)
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()
        date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        with open("snake_score.txt", 'a') as score_save:
            score_save.write(f"\nHigh score: {self.highscore} on the {date_time}")
    
    def score_increase(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write(arg=f"GAME OVER :( => You ended up with score of: {self.score}", move=False,
    #                align="Center", font=self.font)

        
