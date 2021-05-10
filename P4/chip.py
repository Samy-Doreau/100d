from turtle import Turtle


class Chip(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.setheading(270)

    def init_color(self, side):
        if side == 'R':
            self.color = 'red'
        elif side == 'L':
            self.color = 'blue'

    def move(self):
        self.forward(20)
