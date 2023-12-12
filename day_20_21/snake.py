from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.up()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # loop backwards thru snake segments
        for index in range(len(self.segments)-1, 0, -1):
            # get position of segment ahead of current segment
            new_position = self.segments[index-1].pos()
            # move seg to position of previous segment
            self.segments[index].setpos(new_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        print("snek up")
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
