from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.L_score = 0
        self.R_score = 0
        self.update_scoreboard()

    def l_point(self):
        self.L_score += 1

    def r_point(self):
        self.R_score += 1

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.L_score, align='center',
                   font=('Courrier', 80, 'normal'))

        self.goto(100, 200)
        self.write(self.R_score, align='center',
                   font=('Courrier', 80, 'normal'))
