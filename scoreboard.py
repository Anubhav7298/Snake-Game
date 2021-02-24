from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.setpos(0, 270)
        self.color("white")

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", False, align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", False, align="center", font=("Arial", 16, "normal"))
