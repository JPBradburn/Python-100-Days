# import colorgram
#
# colours = colorgram.extract("download.png", 100)
# colours_rgb = []
#
# for colour in colours:
#     colours_rgb.append((colour.rgb.r, colour.rgb.g, colour.rgb.b))
#
# print((colours_rgb))

import random
import turtle
from turtle import *
import time

tim = Turtle()
screen = Screen()
turtle.colormode(255)
screen.setup(625, 625)

colours = [(224, 213, 86), (148, 59, 99), (147, 73, 50), (52, 97, 139), (243, 226, 232), (187, 165, 100), (225, 238, 229), (111, 156, 186), (219, 228, 238), (195, 145, 161), (62, 127, 99), (52, 50, 108), (86, 154, 96), (174, 89, 125), (131, 177, 158), (141, 37, 56), (167, 151, 63), (42, 35, 65), (26, 51, 41), (77, 145, 171), (122, 43, 39), (52, 32, 29), (65, 39, 45), (186, 88, 77), (111, 119, 171), (179, 190, 216), (220, 178, 172), (217, 177, 191), (173, 203, 188), (35, 81, 87), (167, 201, 208), (230, 210, 23), (40, 76, 67), (80, 75, 40)]
Screen().bgcolor(240, 234, 225)

n = 15
tim.penup()
tim.speed("fastest")

for i in range(n):
    for j in range(i, n):
        tim.setpos(j * 40 - 275, i * 40 - 275)
        tim.dot(20, random.choice(colours))

tim.hideturtle()

screen.exitonclick()
