from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.up()
        self.goto(-0, 270)
        self.write_score()

    def display_game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False,
                   align="center", font=('courier', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score = {self.score}", move=False,
                   align="center", font=('courier', 14, 'normal'))