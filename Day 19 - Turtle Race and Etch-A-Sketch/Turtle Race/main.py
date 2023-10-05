import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=400, width=500)
screen.title("Welcome to the turtle race!")
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a colour. ")

colours = ["red", "orange", "yellow", "green", "blue", "pink"]
turtles = []
winner = None

for colour in colours:
    turtles.append(Turtle(shape="turtle"))
    turtles[-1].pu()
    turtles[-1].color(colour)
    turtles[-1].setposition(x=-225, y=175 - len(turtles) * 50)

while not winner:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 215:
            winner = turtle
            break
print(type(user_bet))
print(user_bet)
if user_bet == winner.fillcolor():
    print("You win!")
else:
    print(f"Sorry, {user_bet} didn't win, {winner.fillcolor()} won.")

screen.exitonclick()
