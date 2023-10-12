from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.speed("fastest")
        self.penup()
        self.setheading(90)
        self.hideturtle()
        self.write_score(0, 0)

    def write_score(self, left, right):
        self.clear()
        self.goto(-200, 200)
        self.write(str(left), False, align=ALIGNMENT, font=FONT)
        self.goto(200, 200)
        self.write(str(right), False, align=ALIGNMENT, font=FONT)
        self.goto(0, -280)
        for i in range(11):
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)

