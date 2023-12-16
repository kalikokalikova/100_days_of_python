from turtle import Turtle
STEP_SIZE = 30

class Paddle(Turtle):
    def __init__(self, starting_position) -> None:
        super().__init__()
        self.shape("square")
        self.up()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(starting_position)
        self.speed("fastest")

    def move_up(self):
        new_y = self.ycor() + STEP_SIZE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - STEP_SIZE
        self.goto(self.xcor(), new_y)

    def reset(self, starting_position):
        self.goto(starting_position)
