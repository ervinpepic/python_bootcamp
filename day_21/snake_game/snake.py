from turtle import Turtle


class Snake:

    def __init__(self):
        self.segments = []
        self.x_position = 0
        self.move_distance = 20
        self.create_snake()

    def create_snake(self):
        for _ in range(0, 3):
            new_snake = Turtle("square")
            new_snake.color("white")
            new_snake.penup()
            self.x_position -= 20
            new_snake.goto(x=self.x_position, y=0)
            self.segments.append(new_snake)

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
