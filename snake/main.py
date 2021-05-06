from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
score = 0
import time
snake = Snake()
food = Food()
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        score += 1
        scoreboard.refresh(score)


screen.exitonclick()
