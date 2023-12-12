from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sneeeek")
screen.tracer(0)

snek = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")

screen.update()

game_on = True

def game_over():
    global game_on
    game_on = False
    scoreboard.display_game_over()

while game_on:
    screen.update()
    time.sleep(.1)
    snek.move()

    # Detect collision with food
    if snek.head.distance(food) < 20:
        print("nom nom nom")
        food.go_to_random_location()
        snek.grow()
        scoreboard.increase_score()

    # Detect collision with wall
    if snek.head.xcor() > 280 or snek.head.xcor() < -300 or snek.head.ycor() > 300 or snek.head.ycor() < -280:
        game_over()

    # Detect collision with own tail
    for segment in snek.segments[1:-1]:
        if snek.head.distance(segment) < 10:
            game_over()


screen.exitonclick()
