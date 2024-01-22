import turtle
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    score = 0
    try:
        with open("highscore_tracker.txt", mode="r") as tracker:
            highscore = int(tracker.read())
    except:
        highscore = 0
    scoring_turtle = Turtle()
    scoring_turtle.pencolor("white")
    scoring_turtle.hideturtle()
    scoring_turtle.penup()
    scoring_turtle.setposition(0, 260)

    def __init__(self):
        self.display()

    def increase(self):
        self.score += 1
        self.display()

    def display(self):
        self.scoring_turtle.clear()
        self.scoring_turtle.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.scoring_turtle.setposition(0, 230)
        self.scoring_turtle.write(f"High Score: {self.highscore}", False, align=ALIGNMENT, font=FONT)
        self.scoring_turtle.setposition(0, 260)

    # def game_over(self):
    #     self.scoring_turtle.setposition(0, 0)
    #     self.scoring_turtle.write("GAME OVER!", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore_tracker.txt", mode="w") as tracker:
                tracker.write(str(self.highscore))
        self.score = 0
        self.display()
