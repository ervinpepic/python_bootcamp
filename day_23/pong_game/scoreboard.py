from turtle import Turtle

class Scoreborad(Turtle):
    def __init__(self):
        super().__init__()
        

        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        
        
    def update_score(self):
        self.goto(-150, 200)
        self.write(self.l_score, align="center", font=("Arial", 70, "bold"))
        self.goto(150, 200)
        self.write(self.r_score, align="center", font=("Arial", 70, "bold"))

    def update_score_r(self):
        self.clear()
        self.r_score += 1
        self.update_score()

    def update_score_l(self):
        self.clear()
        self.l_score += 1
        self.update_score()