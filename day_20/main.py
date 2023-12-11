from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sneeeek")
screen.tracer(0)

snek = Snake()
screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")

screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(.1)
    snek.move()


screen.exitonclick()
