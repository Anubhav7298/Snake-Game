from turtle import Turtle

position = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.size = 3
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in position:
            self.add_segment(pos)

    def add_segment(self, x):
        tim = Turtle("square")
        tim.fillcolor("white")
        tim.pencolor("white")
        tim.up()
        tim.goto(x)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
              self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
