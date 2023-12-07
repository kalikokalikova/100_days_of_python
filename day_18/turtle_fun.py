from turtle import Turtle, Screen, colormode
import random
import colorgram

timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
timmy.color("teal")

# colors = ['teal', 'medium aquamarine', 'purple', 'goldenrod', 'maroon', 'pale turquoise', 'thistle', 'chartreuse', 'yellow green', 'rosy brown', 'olive']

def dotted_line():
    # dotted line
    for _ in range(10):
        timmy.down()
        timmy.forward(10)
        timmy.up()
        timmy.forward(10)

def ten_shapes():
    for i in range(3,11):
        angle = 360/i
        # do this i times
        timmy.pencolor(random.choice(colors))
        # timmy.pencolor(colors[i-3])
        for _ in range(i):
            timmy.right(angle)
            timmy.forward(100)

directions = [0,90,180,270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

def random_walk(paces):
    colormode(255)
    timmy.width(10)
    timmy.speed("fast")
    # do i walks
    for _ in range(paces):
        # choose a color
        # timmy.color(random.choice(colors))
        timmy.color(random_color())
        # # choose a direction (up, down, right, left)
        timmy.setheading(random.choice(directions))
        timmy.forward(30)

def spirograph():
    colormode(255)
    timmy.speed("fastest")
    for _ in range(72):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.right(5)

colors = colorgram.extract('dots.jpeg', 20)
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
timmy.speed("fastest")
colormode(255)

def make_row(dots_in_row):
    for _ in range(dots_in_row):
        timmy.down()
        color = random.choice(colors)
        timmy.dot(20, color.rgb)
        timmy.up()
        timmy.forward(50)

def reset_and_move_down():
    timmy.up()
    timmy.setx(0)
    timmy.sety(timmy.position()[1]+50)

def create_dot_masterpiece(grid_size):
    for _ in range(grid_size):
        make_row(grid_size)
        reset_and_move_down()

create_dot_masterpiece(10)


screen.exitonclick()