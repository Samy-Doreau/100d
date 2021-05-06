from turtle import Turtle

SCOREBOARD_POSITION = (0, 270)
ALIGNMENT = 'center'
FONT = ('Courier', 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0  # Initial score is 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.goto(SCOREBOARD_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False,
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False,
                   align=ALIGNMENT, font=FONT)
