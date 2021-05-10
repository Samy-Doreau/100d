from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.listen()
snake = Snake()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.setup(width=600, height=600)

food = Food()
scoreboard = Scoreboard()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    # If head collides with any segment in the tail
    for seg in snake.segments[1:]:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            scoreboard.reset()


screen.exitonclick()
