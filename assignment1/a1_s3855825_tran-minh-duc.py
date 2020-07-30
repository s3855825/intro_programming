# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020B
# Assignment: 1
# Author: Tran Minh Duc (s3855825)
# Created date: 23/07/2020
# Last modified date: 30/07/2020

import turtle


def show_option():
    """
    Show user options
    """
    print('***************************')
    print('1. Draw UK flag')
    print('2. Draw Australia flag')
    print('3. Exit')


def draw_union_jack(width=400, height=200, shift=0):
    """
    Draw an union jack on a canvas of size (width, height)
    Ratio taken from this photo: https://i.stack.imgur.com/lHE1z.png
    """
    turtle.speed("slow")
    turtle.getscreen().colormode(255)

    # draw canvas border
    turtle.penup()
    turtle.goto(-width/2, -height/2)
    turtle.pendown()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)

    center_cross_width = 0.1*width
    red_diagonal_width = 0.1*height
    white_diagonal_width = 0.1*width

    # draw center cross
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-width/2 + center_cross_width/2, height/2)
    turtle.pendown()
    for i in range(4):
        if i % 2 == 0:
            turtle.forward(width)
        else:
            turtle.forward(center_cross_width)
        turtle.right(90)

    turtle.penup()
    turtle.goto(width/2, -height/2)
    turtle.pendown()
    for i in range(4):
        if i % 2 == 0:
            turtle.forward(center_cross_width)
        else:
            turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

    turtle.exitonclick()


def draw_aussie(width=100, height=100):
    """
    Draw an Australian flag on a canvas of size (width, height)
    """
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
