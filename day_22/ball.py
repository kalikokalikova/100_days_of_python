from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.up()
        self.x_move = 3
        self.y_move = 3

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def increase_speed(self):
        self.x_move *= 1.1
        self.y_move *= 1.1

    def reset(self):
        self.x_move = 3
        self.y_move = 3
        self.ht()
        self.goto(0,0)
        self.st()