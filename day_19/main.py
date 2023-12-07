from turtle import Turtle, Screen
import random

screen = Screen()
screen_left_boundary = -screen.window_width()/2
screen_right_boundary = screen.window_width()/2

turtle_data = [
    {"name": "Myrtle", "color": "lavender"},
    {"name": "Turtella", "color": "green"},
    {"name": "Shelly", "color": "blue"},
    {"name": "Oceana", "color": "turquoise"},
    {"name": "Franklin", "color": "goldenrod"},
    {"name": "Spike", "color": "pink"},
]

turtles = {
    # "myrtle": <Turtle Object>
}

def create_turtles(turtle_data):
    for turtle in turtle_data:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(turtle["color"])
        new_turtle.up()
        new_turtle.goto(x=screen_left_boundary + 20, y=250 -
                        (turtle_data.index(turtle) * 40))
        turtles[turtle["name"]] = new_turtle


def move_random_distance(turtle):
    turtle.forward(random.randint(0, 10))


def start_race():
    # pop up to get bet, save the bet
    bet = screen.textinput(title="WHICH TURTLE WILL WIN???", prompt="Choose your fighter: (Myrtle, Turtella, Shelly, Oceana, Franklin, or Spike)")
    winner = False
    create_turtles(turtle_data)

    while not winner:
        turtle_name, turtle = random.choice(list(turtles.items()))
        move_random_distance(turtle)
        # detect when a turtle has reached the right side of the screen
        if turtle.pos()[0] > screen_right_boundary-20:
            print(f"{turtle_name} has won!")
            winner = True

    # let the user know if they've won or lost
    if bet.lower() == turtle_name.lower():
        print("Lucky bet!!!")
    else:
        print("Sorry, you lose your moneys  :(")

start_race()

screen.listen()
screen.exitonclick()
