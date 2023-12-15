from turtle import Turtle
STEP_SIZE = 20

class Paddle(Turtle):
    def __init__(self, side) -> None:
        super().__init__()
        self.shape("square")
        self.up()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=4)
        if side == "left":
            self.goto(-550, 0)
        else:
            self.goto(550, 0)
        self.setheading(90)
        self.speed("fastest")

    def move_up(self):
        self.forward(STEP_SIZE)

    def move_down(self):
        self.backward(STEP_SIZE)
