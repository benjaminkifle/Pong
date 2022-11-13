from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pad_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(pad_pos)

    def p1_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def p1_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
