# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020B
# Assignment: 1
# Author: Tran Minh Duc (s3855825)
# Created date: 23/07/2020
# Last modified date: 04/08/2020

import turtle
from random import random


def show_option():
    """
    Show user options
    """
    print('***************************')
    print('1. Draw UK flag')
    print('2. Draw Australia flag')
    print('3. Exit')


def draw_diagonal(color="white", left=True):
    turtle.fillcolor(color)
    turtle.begin_fill()
    # left diagonal
    if left:
        turtle.penup()
        turtle.goto(-300, 150)
        turtle.pendown()
        turtle.forward(60)
        turtle.goto(300, -130)
        turtle.goto(300, -150)
        turtle.goto(240, -150)
        turtle.goto(-300, 130)
        turtle.right(90)
        turtle.forward(20)
        turtle.penup()
    else:
        turtle.penup()
        turtle.goto(300, 150)
        turtle.pendown()
        turtle.left(-90)
        turtle.forward(60)
        turtle.goto(-300, -130)
        turtle.goto(-300, -150)
        turtle.goto(-240, -150)
        turtle.goto(300, 130)
        turtle.right(90)
        turtle.forward(20)
        turtle.penup()
    turtle.end_fill()


def draw_stripe(color, vertical=True):
    turtle.penup()
    turtle.goto()
    turtle.pendown()


def draw_union_jack():
    """
    Draw an union jack on a canvas of size (width, height)
    Ratio taken from this image: https://i.stack.imgur.com/lHE1z.png
    """
    turtle.speed("slow")
    turtle.getscreen().colormode(255)

    # draw blue background
    turtle.penup()
    turtle.goto(-300, 150)
    turtle.pendown()

    turtle.fillcolor("blue")
    turtle.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            turtle.forward(600)
        else:
            turtle.forward(300)
        turtle.right(90)
    turtle.end_fill()

    # draw white diagonal
    draw_diagonal(color="red", left=True)
    draw_diagonal(color="red", left=False)

    # draw white vertical
    turtle.exitonclick()


def draw_aussie(width=100, height=100):
    """
    Draw an Australian flag on a canvas of size (width, height)
    """
    # TODO


def calculate_fractions(numbers):
    total = sum(numbers)
    fractions = []
    for i in numbers:
        fractions.append(round(i / total, 3))
    print(fractions)
    return fractions


def draw_arc(color, fraction, radius):
    turtle.fillcolor(color[0], color[1], color[2])
    turtle.begin_fill()
    turtle.circle(radius, round(fraction * 360, 1))
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


def problem1():
    """
    Start a menu allowing user to choose to draw the British or Australian flag.
    Press 3 to exit.
    """
    show_option()
    # user_input = input('Enter an option (1/2/3): ')
    user_input = '1'
    while user_input != '1' and user_input != '2' and user_input != '3':
        print('Invalid option. Please choose again.\n')
        show_option()
        user_input = input('Enter an option (1/2/3): ')
    if user_input == '1':
        print('Drawing UK flag.')
        draw_union_jack()
    elif user_input == '2':
        print('Drawing Aussie flag.')
        draw_aussie()
    elif user_input == '3':
        print('Program exits. Have a nice day!')


def problem2():
    # numbers = [247.39, 260.4, 171.83, 51.96]
    numbers = []
    user_input = input("Please enter a number to add to the list, or 'q' to stop: ")
    while user_input != 'q' and user_input.isnumeric():
        if user_input != 'q':
            numbers.append(float(user_input))
        user_input = input("Please enter the next number to add to the list, or 'q' to stop: ")

    # print(numbers)
    draw_pie_chart(numbers)


problem1()
