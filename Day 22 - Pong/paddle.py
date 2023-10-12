import math
from turtle import Turtle


class Paddle(Turtle):
    target_y = 0

    def __init__(self, xpos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.setposition(xpos, 0)

    def up(self):
        if self.ycor() < 250:
            self.forward(10)

    def down(self):
        if self.ycor() > -250:
            self.backward(10)

    def catch_ball(self, ball):
        self.speed(1)
        x = ball.xcor()
        y = ball.ycor()
        m = math.tan(math.radians(ball.heading()))
        b = y - m * x
        self.target_y = 5 * round((m * 300 + b)/5)
        while self.target_y > 300 or self.target_y < -300:
            if self.target_y > 300:
                self.target_y = 600 - self.target_y
            if self.target_y < -300:
                self.target_y = -600 - self.target_y
        print(self.target_y)
