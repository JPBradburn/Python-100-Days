import random
import time
from turtle import Turtle
from scoreboard import Scoreboard

scoreboard = Scoreboard()


class Ball(Turtle):

    score_left = 0
    score_right = 0

    def __init__(self, left, right, paddle_two):
        directions = [random.randint(-10, 10), random.randint(170, 190)]
        self.score_left = left
        self.score_right = right
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        vector = random.choice(directions)

        self.setheading(vector)
        paddle_two.catch_ball(self)

        time.sleep(2)

        if 10 >= vector >= -10:
            paddle_two.catch_ball(self)

    def move(self, paddle_one, paddle_two):
        if abs(self.ycor() - paddle_one.ycor()) <= 50 and (-290 >= self.xcor() >= -310):
            self.setheading(180 - self.heading())
            paddle_two.catch_ball(self)
        elif abs(self.ycor() - paddle_two.ycor()) <= 50 and (290 <= self.xcor() <= 310):
            self.setheading(180 - self.heading())

        if self.ycor() <= -290 or self.ycor() >= 290:
            self.setheading(-self.heading())

        self.forward(10)

    def check_for_out(self):
        if self.xcor() <= -400:
            self.score_right += 1
            scoreboard.write_score(self.score_left, self.score_right)
            self.hideturtle()
            return True
        elif self.xcor() >= 400:
            self.score_left += 1
            scoreboard.write_score(self.score_left, self.score_right)
            self.hideturtle()
            return True
        else:
            return False
