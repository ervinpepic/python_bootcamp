from turtle import Turtle, speed


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape_len = 2
        self.shape_wid = 2
        self.ball_speed = 0.1
        self.create_ball()
    

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
    
    def move_first_start(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x=x, y=y)

    def move_second_start(self):
        self.setposition(0, 0)
        x = self.xcor() - self.x_move
        y = self.ycor() - self.y_move
        self.goto(x=x, y=y)

    def bounce_y(self):
        self.y_move *= -1  
    
    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.setposition(0, 0)
        self.bounce_x()
