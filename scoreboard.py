from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_score(0)

    def update_score(self, increment):
        self.clear()
        self.score += increment
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score(1)

