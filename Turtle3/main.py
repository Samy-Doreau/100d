from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet.",
                            "Which turtle will win the race ? Enter a color : ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


def create_turtle(i):
    turtle = Turtle(shape='turtle')
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=i * -50 + 150)
    all_turtles.append(turtle)


for i in range(6):
    create_turtle(i)

if user_bet:
    is_race_on = True

while is_race_on:

    for t in all_turtles:
        if t.xcor() > 230:
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You've won, {winning_color} has won.")
            else:
                print(f"You've lost, {winning_color} has won.")
            is_race_on = False
        random_distance = random.randint(0, 10)
        t.forward(random_distance)


screen.exitonclick()


# Event listener stuff

# def move_fwd():
#     tim.forward(10)


# def move_bkw():
#     tim.back(10)


# def clockwise():
#     tim.setheading(tim.heading() + 15)


# def counter_clockwise():
#     tim.setheading(tim.heading() - 15)


# def clear():
#     tim.clear()
#     tim.home()


# screen.listen()
# screen.onkey(key="D", fun=move_fwd)
# screen.onkey(key="A", fun=move_bkw)
# screen.onkey(key="W", fun=clockwise)
# screen.onkey(key="S", fun=counter_clockwise)
# screen.onkey(key="C", fun=clear)
