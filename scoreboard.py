from turtle import Turtle

with open("data.txt", mode="r") as file:
    high_score = int(file.read())


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = high_score
        self.hideturtle()
        self.setpos(0, 270)
        self.color("white")

    def update_score(self):
        self.clear()
        if self.score > self.high_score:
            with open("data.txt", mode="w") as f:
                f.write(str(self.score))
            self.high_score = self.score
        self.write(f"Score = {self.score} | High Score = {self.high_score}", False, align="center", font=("Arial", 16, "normal"))
        self.score += 1

    def reset(self):
        self.score = 0
        self.update_score()
