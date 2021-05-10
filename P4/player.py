from turtle import Turtle


class Player(Turtle):
    def __init__(self, side):
        super().__init__()
        self.penup()
        self.setheading(270)
        self.shape('turtle')
        self.init_position(side)
        self.init_color(side)
        self.speed('fastest')
        self.nb_chips = 0
        self.active_chips = []
        self.active_chips_movement_status = []

    def init_color(self, side):
        if side == 'R':
            self.color('red')

        elif side == 'L':
            self.color('blue')

    def init_position(self, side):
        if side == 'R':
            self.goto(280, 280)
        elif side == 'L':
            self.goto(-280, 280)

    def move_left(self):
        if self.xcor() > -280:
            self.goto(self.xcor() - 20, self.ycor())

    def move_right(self):
        if self.xcor() < 280:
            self.goto(self.xcor() + 20, self.ycor())

    def drop_chip_left(self):
        chip = Turtle('circle')
        chip.setheading(270)
        chip.penup()
        chip.color('blue')
        chip.goto(self.xcor(), self.ycor() - 30)
        self.active_chips.append(chip)
        self.active_chips_movement_status.append(True)

    def drop_chip_right(self):
        chip = Turtle('circle')
        chip.setheading(270)
        chip.penup()
        chip.color('red')
        chip.goto(self.xcor(), self.ycor() - 30)
        self.active_chips.append(chip)
        self.active_chips_movement_status.append(True)

    def move_chip(self):
        if self.active_chips_movement_status[self.nb_chips - 1]:
            self.active_chips[-1].forward(20)
