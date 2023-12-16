from turtle import Screen, Turtle

class Court(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.setup(width=1200, height=800)
        self.bgcolor("black")

        center_line = Turtle(shape="turtle")
        center_line.speed("fastest")
        center_line.up()
        center_line.goto(0, -400)
        center_line.color("white")
        center_line.down()
        center_line.width(5)
        center_line.setheading(90)
        for _ in range(40):
            center_line.forward(10)
            center_line.up()
            center_line.forward(10)
            center_line.down()
        center_line.ht()
