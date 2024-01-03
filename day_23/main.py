import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
car_manager = CarManager()
turtle = Player()

screen.listen()
screen.onkey(turtle.move, "Up")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    # if turtle reaches top of screen
    if turtle.is_safe():
        print("You made it!")
        scoreboard.increase_level()
        turtle.reset_to_bottom()
        car_manager.increase_car_speed()
    # if turtle/car collision
    if car_manager.is_turtle_collision(turtle):
        scoreboard.show_game_over_message()
        game_on = False

screen.exitonclick()
