# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020B
# Assignment: 1
# Author: Tran Minh Duc (s3855825)
# Created date: 23/07/2020
# Last modified date: 28/07/2020

import turtle


def show_option():
    """
    Show user options
    """
    print('***************************')
    print('1. Draw UK flag')
    print('2. Draw Australia flag')
    print('3. Exit')


def draw_union_jack(width=100, height=100, shift=0):
    """
    Draw an union jack on a canvas of size (width, height)
    """
    working_screen = turtle.Screen()
    working_screen.bgcolor("white")

    # draw center cross
    turtle.fillcolor("red")


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
    user_input = input('Enter an option (1/2/3): ')
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
