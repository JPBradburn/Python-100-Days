import turtle
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    score = 0
    scoring_turtle = Turtle()
    scoring_turtle.pencolor("white")
    scoring_turtle.hideturtle()
    scoring_turtle.penup()
    scoring_turtle.setposition(0, 260)

    def __init__(self):
        self.scoring_turtle.write("Score: 0", False, align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.scoring_turtle.clear()
        self.scoring_turtle.write("Score: " + str(self.score), False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.scoring_turtle.setposition(0, 0)
        self.scoring_turtle.write("GAME OVER!", False, align=ALIGNMENT, font=FONT)
