from tkinter import font
from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        self.score = 0
        self.font = (["Arial", 20, "bold"])

        super().__init__()
        self.color("white")
        self.penup()
        self.setposition(x=0, y=270)
        self.write(arg=f"Score: {self.score}", move=True,
                   align="Right", font=self.font)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.setposition(x=0, y=270)
        self.write(arg=f"Score: {self.score}", move=True,
                   align="Right", font=self.font)
    
    def game_over(self):
        self.setposition(0, 0)
        self.write(arg=f"GAME OVER :( => You ended up with score of: {self.score}", move=False,
                   align="Center", font=self.font)
        
