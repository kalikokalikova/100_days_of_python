from turtle import Turtle, Screen, colormode
import random
import colorgram

timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
timmy.up()

colors = colorgram.extract('dots.jpeg', 20)
timmy.speed("fastest")
colormode(255)
timmy.setposition(-200, -200)

def make_row(dots_in_row):
    for _ in range(dots_in_row):
        color = random.choice(colors)
        timmy.dot(20, color.rgb)
        timmy.forward(50)

def reset_and_move_up():
    timmy.setx(-200)
    timmy.sety(timmy.position()[1]+50)

def create_dot_masterpiece(grid_size):
    for _ in range(grid_size):
        make_row(grid_size)
        reset_and_move_up()

create_dot_masterpiece(10)

screen.exitonclick()