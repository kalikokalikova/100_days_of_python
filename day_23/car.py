from turtle import Turtle


class Car(Turtle):
    def __init__(self, color, starting_position):
        super().__init__()
        # set itself to appropriate car shape and color
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(color)
        self.up()
        self.goto(starting_position)
