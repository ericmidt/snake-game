from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_score(0)

    def update_score(self, increment):
        self.clear()
        self.score += increment
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)