import turtle as t
import random
import colorgram
timmy = t.Turtle()
t.colormode(255)
timmy.color('white')
timmy.hideturtle()
timmy.shape(None)
# timmy.speed('fastest')
timmy.pensize(2)


def draw_square(size, turtle):
    for i in range(4):
        for d in range(10):
            if (d + 1) % 2 == 0:
                turtle.pendown()
                turtle.forward(10)
                turtle.penup()
            else:
                turtle.penup()
                turtle.forward(10)
                turtle.pendown()
        turtle.right(90)


def draw_multishape(size, turtle):
    color_set = ["CornflowerBlue", "DarkOrchid", "IndianRed",
                 "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    for side_nb in range(3, 10):
        turtle.pencolor(color_set[side_nb])
        actual_side_nb = side_nb + 1
        for edge_nb in range(actual_side_nb):
            turtle.forward(size)
            turtle.right(360 / actual_side_nb)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def random_walk(total_segments, size, turtle):
    colors = ["CornflowerBlue", "DarkOrchid", "IndianRed",
              "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    for s in range(total_segments):
        turtle.color(random_color())
        turtle.forward(size)
        turtle.right(random.randint(0, 4) * 90)


def draw_spirograph(size, turtle):
    for d in range(0, 360, 5):
        turtle.setheading(d)
        turtle.color(random_color())
        turtle.circle(size)


def paint_spots(turtle):
    hirst_colors = [(194, 166, 108), (135, 167, 193), (49, 102, 145), (145, 90, 43), (10, 21, 54), (188, 156, 34), (224, 208, 115), (62,
                                                                                                                                     23, 10), (184, 141, 165), (69, 119, 79), (59, 13, 24), (138, 180, 149), (135, 28, 13), (129, 77, 104), (14, 41, 25), (19, 53, 135)]
    turtle.pensize(10)
    for row in range(10):
        for i in range(10):
            turtle.color(random.choice(hirst_colors))
            turtle.pendown()
            turtle.dot(20)
            turtle.penup()
            if i < 9:
                turtle.forward(50)
        if row % 2 == 0:
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
        else:
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)


paint_spots(timmy)
# draw_multishape(100, timmy)
# random_walk(500, 20, timmy)
# draw_spirograph(100, timmy)
screen = t.Screen()
screen.exitonclick()
