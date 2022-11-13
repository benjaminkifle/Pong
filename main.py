from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Game controls
screen.listen()
screen.onkey(r_paddle.p1_up, "Up")
screen.onkey(r_paddle.p1_down, "Down")
screen.onkey(l_paddle.p1_up, "w")
screen.onkey(l_paddle.p1_down, "s")

ball_speed = 0.09

game_is_on = True
while game_is_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move_ball()

    # Checks if player 1 misses the ball
    if ball.xcor() > 400:
        ball.goto(0, random.randint(-250, 250))
        ball.new_heading()
        ball.move_ball()
        scoreboard.increase_score_p1()
        ball_speed = 0.09

    # Checks if player 2 misses the ball
    elif ball.xcor() < -400:
        ball.goto(0, random.randint(-250, 250))
        ball.new_heading()
        ball.move_ball()
        scoreboard.increase_score_p2()
        ball_speed = 0.09

    # Bouncing the ball of the top and bottom wall
    if ball.ycor() >= 280:
        new_heading = (360 - ball.heading())
        ball.setheading(new_heading)
    elif ball.ycor() <= -280:
        new_heading = (360 - ball.heading())
        ball.setheading(new_heading)

    # Bounce the ball of the paddles
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320:
        new_heading = (180 - ball.heading())
        ball.setheading(new_heading)
        if not ball_speed <= 0.01:
            ball_speed -= 0.01
    elif ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        new_heading = (180 - ball.heading())
        ball.setheading(new_heading)
        if not ball_speed <= 0.01:
            ball_speed -= 0.01

screen.exitonclick()
