from turtle import Screen
from paddle import Paddle
from ball import Ball

game_is_running = True

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

paddle_one = Paddle(-300)
paddle_two = Paddle(300)

screen.tracer(1)

ball = Ball(0, 0, paddle_two)

screen.listen()
screen.onkeypress(paddle_one.up, "Up")
screen.onkeypress(paddle_one.down, "Down")

while game_is_running:
    ball.move(paddle_one, paddle_two)
    if ball.check_for_out():
        ball = Ball(ball.score_left, ball.score_right, paddle_two)
    if (paddle_two.target_y - paddle_two.ycor()) > 0:
        paddle_two.forward(5)
    elif (paddle_two.target_y - paddle_two.ycor()) < 0:
        paddle_two.backward(5)




screen.exitonclick()
