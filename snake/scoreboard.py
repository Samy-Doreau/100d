from turtle import Turtle

SCOREBOARD_POSITION = (0, 270)
ALIGNMENT = 'center'
FONT = ('Courier', 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open('data/data.txt') as score_file:
            self.high_score = int(score_file.read())
        self.score = 0  # Initial score is 0
        self.hideturtle()
        self.color('white')
        self.penup()

        self.speed('fastest')
        self.goto(SCOREBOARD_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", False,
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data/data.txt', 'w') as score_file:
                score_file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", False,
    #                align=ALIGNMENT, font=FONT)
