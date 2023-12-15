from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.up()
        self.start()

    def start(self):
        while True:
            self.forward(10)