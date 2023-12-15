from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")

center_line = Turtle(shape="turtle")
center_line.speed("fastest")
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
center_line.ht()

left_paddle = Paddle("left")
right_paddle = Paddle("right")
ball = Ball()

screen.listen()
screen.onkey(right_paddle.move_up, "c")
screen.onkey(right_paddle.move_down, "t")
screen.onkey(left_paddle.move_up, ".")
screen.onkey(left_paddle.move_down, 'e')


screen.exitonclick()