from turtle import Turtle

SCOREBOARD_POSITION = (-10, 270)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0  # Initial score is 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.goto(SCOREBOARD_POSITION)
        self.refresh(self.score)

    def refresh(self, score):
        self.clear()
        self.write(f"Score: {score}", False,
                   align='center', font=('Arial', 16, 'normal'))
