from turtle import Turtle


class Snake:
    segments = []

    def __init__(self):

        for segment in range(3):
            current_segment = Turtle(shape="square")
            current_segment.color("white")
            current_segment.penup()
            current_segment.setposition((segment - 1) * -20 + 5, -5)
            self.segments.append(current_segment)

    def move(self):
        for segment in reversed(range(1, len(self.segments))):
            self.segments[segment].setposition(self.segments[segment - 1].position())
        self.segments[0].forward(20)

    def grow(self):
        new_segment_position = self.segments[-1].position()

        for segment in reversed(range(1, len(self.segments))):
            self.segments[segment].setposition(self.segments[segment - 1].position())
        self.segments[0].forward(20)

        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(new_segment_position)
        self.segments.append(new_segment)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
