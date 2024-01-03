from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.ht()
        self.goto(-200, 250)
        self.level = 1
        self.write(f"Level: {self.level}", move=False,
                   align='center', font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", move=False,
                   align='center', font=FONT)

    def show_game_over_message(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align='center', font=FONT)
