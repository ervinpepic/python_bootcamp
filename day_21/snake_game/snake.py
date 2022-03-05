from turtle import Turtle

x_y_positions = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.segments = []
        self.move_distance = 20
        self.create_snake()

    def create_snake(self):
        for x_y in x_y_positions:
            self.add_segment(x_y)
    
    def add_segment(self, x_y_positions):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(x_y_positions)
        self.segments.append(new_snake)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(self.move_distance)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
