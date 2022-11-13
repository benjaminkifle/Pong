from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 50, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.start_pos = 270
        self.lines = []
        self.score_p1 = 0
        self.score_p2 = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()
        self.line()

    def line(self):
        for line in range(14):
            new_line = Turtle("square")
            new_line.color("white")
            new_line.shapesize(stretch_wid=1, stretch_len=0.2)
            new_line.penup()
            new_line.goto(0, self.start_pos)
            self.lines.append(new_line)
            self.start_pos -= 41

    def update_scoreboard(self):
        self.write(f"{self.score_p1}    {self.score_p2}", align=ALIGNMENT, font=FONT)

    def increase_score_p1(self):
        self.score_p1 += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_p2(self):
        self.score_p2 += 1
        self.clear()
        self.update_scoreboard()
