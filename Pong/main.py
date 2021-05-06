from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
paddle_right = Paddle('R')
paddle_left = Paddle('L')
scoreboard = Scoreboard()
ball = Ball()
screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")

screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision on top wall:
    if ball.ycor() > 280:
        #
        ball.bounce_y()

    # Detect collision on bottom wall:
    if ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle :
    if (ball.distance(paddle_right) < 50 and ball.xcor() > 320) or (ball.distance(paddle_left) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        ball.reset_position()
        print(f"new speed : {ball.speed()}")
    if ball.xcor() < - 380:
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        ball.reset_position()
        print(f"new speed : {ball.speed()}")


screen.exitonclick()
