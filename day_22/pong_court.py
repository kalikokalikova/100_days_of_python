from turtle import Screen, Turtle

class PongCourt:
    def __init__(self) -> None:
        screen = Screen()
        screen.setup(width=1200, height=800)
        screen.bgcolor("black")

        center_line = Turtle(shape="square")
        center_line.ht()
        center_line.up()
        center_line.goto(0,-400)
        center_line.color("white")
        center_line.down()
        center_line.width(5)
        center_line.setheading(90)
        for _ in range(40):
            center_line.forward(10)
            center_line.up()
            center_line.forward(10)
            center_line.down()

