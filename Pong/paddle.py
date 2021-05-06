from turtle import Turtle

PADDLE_LENGTH = 4


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed('fastest')
        self.color('white')
        self.init(side)

    def init(self, side):
        if side == 'R':
            self.goto(350, 0)
        elif side == 'L':
            self.goto(-350, 0)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
