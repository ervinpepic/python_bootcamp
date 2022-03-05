from turtle import Turtle


class Padle(Turtle):
    def __init__(self, goto_x, goto_y):
        super().__init__()
        self.gotox = goto_x
        self.gotoy = goto_y
        self.shape_len = 1
        self.shape_wid = 5
        self.create_padle()

    def create_padle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(self.shape_wid, self.shape_len)
        self.penup()
        self.goto(x=self.gotox, y=self.gotoy)

    def move_up(self):
        y = self.ycor() + 20
        self.goto(x=self.xcor(), y=y)

    def move_down(self):
        y = self.ycor() - 20
        self.goto(x=self.xcor(), y=y)
