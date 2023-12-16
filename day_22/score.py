from turtle import Turtle
FONT = ('Courier', 50, 'normal')

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.ht()
        self.color("white")
        self.up()
        self.goto(position)
        self.write(self.score, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write(self.score, font=FONT)
