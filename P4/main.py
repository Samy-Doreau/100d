import time
from turtle import Screen
from chip import Chip

from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
# screen.tracer(0)
R_player = Player('R')
L_player = Player('L')

grid = []
current_player = ""


def R_chip_drop():
    current_player = 'R'
    R_player.drop_chip_right()
    grid.append(R_player.active_chips[-1])


def L_chip_drop():
    current_player = 'L'
    L_player.drop_chip_left()
    grid.append(L_player.active_chips[-1])


def manual_stop_chip():
    R_player.active_chips_movement_status[0] = False


screen.listen()
screen.onkey(R_player.move_left, 'Left')
screen.onkey(L_player.move_left, 'a')
screen.onkey(R_player.move_right, 'Right')
screen.onkey(L_player.move_right, 'd')
screen.onkey(manual_stop_chip, '5')
screen.onkey(L_chip_drop, 's')


screen.onkey(R_chip_drop, 'Down')


game_over = False
while game_over is False:
    screen.update()
    # time.sleep(0.1)

    # Detect collision with bottom wall or other chip
    if len(R_player.active_chips) > 0:

        if len(grid) > 1:
            actual_grid = grid[:-1]
            for c in actual_grid:
                if c.xcor() == R_player.active_chips[-1].xcor() and R_player.active_chips[-1].ycor() - c.ycor() <= 30:
                    is_chip_ahead_R = True
                    break
                else:
                    is_chip_ahead_R = False
        else:
            is_chip_ahead_R = False
        if R_player.active_chips[-1].ycor() <= -270 or is_chip_ahead_R:
            R_player.active_chips_movement_status[R_player.nb_chips - 1] = False

        R_player.move_chip()

    if len(L_player.active_chips) > 0:

        if len(grid) > 1:
            actual_grid = grid[:-1]
            for c in actual_grid:
                if c.xcor() == L_player.active_chips[-1].xcor() and L_player.active_chips[-1].ycor() - c.ycor() <= 30:
                    is_chip_ahead_L = True
                    break
                else:
                    is_chip_ahead_L = False
        else:
            is_chip_ahead_L = False
        if L_player.active_chips[-1].ycor() <= -270 or is_chip_ahead_L:
            L_player.active_chips_movement_status[L_player.nb_chips - 1] = False

        L_player.move_chip()

    # Detect a win
    if len(grid) >= 4:
        for c in grid:
            c_color = c.color()
            c_x = c.xcor()
            c_y = c.ycor()
            other_chips_V_up = [c for c in grid if c.color() == c_color and (
                c.xcor() == c_x and (c.ycor() == c_y - 20 or c.ycor() == c_y - 40 or c.ycor() == c_y - 60))]
            other_chips_V_down = [c for c in grid if c.color() == c_color and (
                c.xcor() == c_x and (c.ycor() == c_y + 20 or c.ycor() == c_y + 40 or c.ycor() == c_y + 60))]

            other_chips_H_left = [c for c in grid if c.color() == c_color and (
                c.ycor() == c_y and (c.xcor() == c_x - 20 or c.xcor() == c_x - 40 or c.xcor() == c_x - 60))]
            other_chips_H_right = [c for c in grid if c.color() == c_color and (
                c.ycor() == c_y and (c.xcor() == c_x + 20 or c.xcor() == c_x + 40 or c.xcor() == c_x + 60))]

            if len(other_chips_V_up) == 3 or len(other_chips_V_down) == 3 or len(other_chips_H_left) == 3 or len(other_chips_H_right) == 3:
                game_over = True
                break


screen.exitonclick()
