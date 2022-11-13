from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.make_ball()
        self.new_heading()

    def make_ball(self):
        self.shape("square")
        self.color("white")
        self.penup()

    def move_ball(self):
        self.speed(1)
        self.forward(10)

    def new_heading(self):
        new_heading = [
            random.randint(0, 45),
            random.randint(315, 360),
            random.randint(135, 180),
            random.randint(180, 225)
        ]
        self.setheading(random.choice(new_heading))
