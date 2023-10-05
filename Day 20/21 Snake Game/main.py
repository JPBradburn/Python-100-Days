import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=610, height=610)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_running = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_running:
    time.sleep(0.1)
    screen.update()

    if snake.segments[0].distance(food) <= 20:
        food.refresh()
        scoreboard.increase()
        snake.grow()
    else:
        snake.move()

    if snake.segments[0].xcor() >= 300 or snake.segments[0].xcor() <= -300 or \
            snake.segments[0].ycor() >= 300 or snake.segments[0].ycor() <= -300:
        game_running = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) <= 10:
            game_running = False
            scoreboard.game_over()


screen.exitonclick()
