from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_move_distance = STARTING_MOVE_DISTANCE
        self.cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle(shape='square')
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=3)
            car.setheading(180)
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def move_cars(self):
        for c in self.cars:
            c.goto(c.xcor() - self.car_move_distance, c.ycor())

    def level_up(self):
        self.car_move_distance += MOVE_INCREMENT
