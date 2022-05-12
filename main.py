from turtle import Turtle, Screen, colormode
import random

turtle = Turtle()
screen = Screen()

turtle.shape('turtle')


# print square in dashed line
def square_dashed_line():
    for i in range(4):
        for j in range(5):
            turtle.forward(10)
            turtle.penup()
            turtle.forward(10)
            turtle.pendown()
        turtle.right(90)


# square_dashed_line()

# print triangle (3 sides) to decagon (10 sides)
def shapes(start_side, end_side):
    colormode(255)

    for i in range(start_side, end_side+1):
        turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for _ in range(i):
            turtle.forward(100)
            turtle.right(360 / i)

# shapes(3,10)

# Random walk
def random_walk():
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
               "SeaGreen"]

    directions = [0, 90, 180, 270]
    turtle.pensize(15)
    turtle.speed('fastest')

    for _ in range(200):
        turtle.pencolor(random.choice(colours))
        turtle.forward(30)
        turtle.setheading(random.choice(directions))


# random_walk()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)

    return color


# Spirograph
colormode(255)
turtle.speed("fastest")


def spirograph(degree_of_turn):
    for _ in range(int(360 / degree_of_turn)):
        turtle.pencolor(random_color())
        turtle.circle(100)
        # turtle.right(degree_of_turn)
        turtle.setheading(turtle.heading() + degree_of_turn)


# spirograph(5)

screen.exitonclick()
