from turtle import Screen, Turtle
from score import Score
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("POOOOOOOOONGY")

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

right_score = Score((100, 230))
left_score = Score((-100, 230))
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()


def start_volley():
    volley_on = True

    while volley_on:
        ball.move()

        # Ball hits ceiling or floor
        if ball.distance((ball.xcor(), 300)) < 50 or ball.distance((ball.xcor(), -300)) < 20:
            ball.bounce_y()

        # Ball hits paddle
        if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()
            ball.increase_speed()

        # Ball goes out of bounds
        if ball.xcor() > 400:
            # left player gets point
            left_score.update()
            volley_on = False

        if ball.xcor() < -400:
            # right player gets point
            right_score.update()
            volley_on = False

    ball.reset()
    right_paddle.reset((350, 0))
    left_paddle.reset((-350, 0))


screen.listen()
screen.onkey(right_paddle.move_up, "c")
screen.onkey(right_paddle.move_down, "t")
screen.onkey(left_paddle.move_up, ".")
screen.onkey(left_paddle.move_down, 'e')
screen.onkey(start_volley, "space")
screen.exitonclick()
