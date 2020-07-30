import turtle
import random


def calculate_fractions(numbers):
    total = sum(numbers)
    fractions = []
    for i in numbers:
        fractions.append(round(i/total, 3))
    print(fractions)
    return fractions


def draw_arc(color, fraction, radius):
    turtle.fillcolor(color[0], color[1], color[2])
    turtle.begin_fill()
    turtle.circle(radius, round(fraction*360, 1))
    position = turtle.position()  # get current point on the chart circumference to resume on next loop
    turtle.goto(0, 0)
    turtle.end_fill()
    # after finishing a "fraction" of the pie chart, return to the circumference to draw another fraction
    turtle.setposition(position)


def draw_pie_chart(numbers, radius=200):
    # set color mode to use random color format
    turtle.speed(10)
    turtle.getscreen().colormode(255)

    # move start position down, since turtle draw upward
    # move_mouse_position(0, -radius)
    turtle.goto(0, -radius)

    # draw arcs
    fractions = calculate_fractions(numbers)
    for i in fractions:
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw_arc(random_color, i, radius)
    turtle.exitonclick()


numbers = [247.39, 260.4, 171.83, 51.96]
draw_pie_chart(numbers)
