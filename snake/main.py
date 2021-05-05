from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')


t1 = Turtle(shape='square')
t1.color('white')


t2 = Turtle(shape='square')
t2.color('white')
t2.setx(t1.xcor() - 20)

t3 = Turtle(shape='square')
t3.color('white')
t3.setx(t2.xcor() - 20)


screen.exitonclick()
