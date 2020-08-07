# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020B
# Assignment: 1
# Author: Tran Minh Duc (s3855825)
# Created date: 23/07/2020
# Last modified date: 05/08/2020

import turtle
import math
from random import random


def show_option():
    """
    Show user options
    """
    print('***************************')
    print('1. Draw UK flag')
    print('2. Draw Australia flag')
    print('3. Exit')


def draw_blue_background(width, height):
    turtle.penup()
    turtle.goto(-width, height)
    turtle.pendown()

    turtle.fillcolor("blue")
    turtle.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            turtle.forward(width * 2)
        else:
            turtle.forward(height * 2)
        turtle.right(90)
    turtle.end_fill()


def draw_diagonal(width, height, color, left=True):
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()

    coefficient = pow(-1, int(left))  # switch coordinates between left and right diagonals

    # calculate turning points' coordinates
    if color == "red":
        diagonal_w = round(2/30 * width)
        diagonal_h = round(2/15 * height)
    else:
        diagonal_w = round(3/30 * width)
        diagonal_h = round(3/15 * height)

    turtle.penup()
    turtle.goto(coefficient * width, height)
    turtle.pendown()
    turtle.setheading(0)  # reset current turtle angle, make sure turtle is heading in guided direction
    if not left:
        turtle.left(180)
    turtle.forward(diagonal_w)
    turtle.goto(-coefficient * width, -height + diagonal_h)
    turtle.goto(-coefficient * width, -height)
    turtle.goto(-coefficient * (width - diagonal_w), -height)
    turtle.goto(coefficient * width, height - diagonal_h)
    if left:
        turtle.left(90)
    else:
        turtle.right(90)
    turtle.forward(diagonal_h)
    turtle.end_fill()
    turtle.penup()


def draw_stripe(width, height, color, orientation):
    turtle.pencolor(color)
    if color == "red":
        stripe_width = 6/30 * width
    else:
        stripe_width = 10/30 * width

    turtle.fillcolor(color)

    turtle.begin_fill()
    turtle.penup()
    if orientation == "vertical":
        if color == "white":
            turtle.goto(-5/30*width, height)
        else:
            turtle.goto(-3 / 30 * width, height)
    else:
        if color == "white":
            turtle.goto(-width, 5/30*height)
        else:
            turtle.goto(-width, 5/30*height)
    turtle.pendown()
    turtle.setheading(0)
    for i in range(4):
        if i % 2 == 0:
            if orientation == "vertical":
                turtle.forward(stripe_width)
            else:
                turtle.forward(width*2)
        else:
            if orientation == "vertical":
                turtle.forward(height*2)
            else:
                turtle.forward(stripe_width)
        turtle.right(90)
    turtle.end_fill()


def draw_stars(size, offset=(0, 0)):
    # TODO
    return


def draw_union_jack(width=300, height=150):
    """
    Draw the union jack on a canvas of size (width*2, height*2)
    Ratio taken from this image: https://i.stack.imgur.com/lHE1z.png
    """
    turtle.speed("fastest")
    turtle.getscreen().colormode(255)

    # draw blue background
    draw_blue_background(width, height)

    # draw white diagonals
    draw_diagonal(width=width, height=height, color="white", left=True)
    draw_diagonal(width=width, height=height, color="white", left=False)

    # draw red diagonals
    draw_diagonal(width=width, height=height, color="red", left=True)
    draw_diagonal(width=width, height=height, color="red", left=False)

    # draw white vertical and horizontal stripes
    draw_stripe(width=width, height=height * 2, color="white", orientation="vertical")
    draw_stripe(width=width, height=height * 2, color="white", orientation="horizontal")

    # draw red vertical and horizontal stripes
    draw_stripe(width=width, height=height, color="red", orientation="vertical")
    draw_stripe(width=width, height=height, color="red", orientation="horizontal")

    turtle.exitonclick()


def draw_aussie(width=100, height=100):
    """
    Draw an Australian flag on a canvas of size (width*2, height*2)
    """
    stars_position = []  # list of sizes and positions for 7 stars on the flag
    draw_union_jack()
    # TODO


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


problem1()
