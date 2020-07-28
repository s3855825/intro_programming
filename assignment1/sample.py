import turtle
import random


def calculate_fractions(numbers):
    total = sum(numbers)
    fractions = []
    for i in numbers:
        fractions.append(round(i/total, 3))
    print(fractions)
    return fractions


def move_mouse_position(position_x, position_y):
    turtle.penup()
    turtle.goto(position_x, position_y)
    turtle.pendown()


def draw_arc(color, fraction, radius):
    turtle.fillcolor(color[0], color[1], color[2])
    turtle.begin_fill()
    turtle.circle(radius, round(fraction*360, 1))
    move_mouse_position(0, 0)
    turtle.end_fill()


def draw_pie_chart(numbers, radius=200):
    # set color mode to use random color format
    turtle.speed(10)
    turtle.getscreen().colormode(255)

    # draw circle and first arm
    move_mouse_position(0, -radius)
    turtle.circle(radius)
    move_mouse_position(0, 0)
    turtle.forward(radius)

    # draw arcs
    fractions = calculate_fractions(numbers)
    for i in fractions:
        move_mouse_position(0, 0)
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw_arc(random_color, i, radius)
    turtle.exitonclick()


numbers = [247.39, 260.4, 171.83, 51.96]
draw_pie_chart(numbers)
