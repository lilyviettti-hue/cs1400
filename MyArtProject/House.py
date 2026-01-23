###

#File: House.py

# Author:    Lily Vietti, u1411969
# Date:      2026-01-21
# Course:    CS 1400-001, University of Utah, Kahlert School of Computing
# Instructor: H. James de St. Germain
# Copyright: CS 1400 and Lily Vietti - This work may not
#            be copied for use in Academic Coursework.

# I, Lily Vietti, certify that I wrote this code from scratch and did not
# copy it in part or whole from any other source. Any references used in 
# the completion of the assignment are cited in my CS1400 file.

# Program Purpose:
# This program uses the turtle graphics library to draw a simple house

###

import turtle

window = turtle.Screen()
window.title("House")
my_turtle = turtle.Turtle()

# Main building dimensions
building_width = 150
building_height = 100

# Position turtle to start drawing the building
my_turtle.penup()
my_turtle.goto(-75, 50)
my_turtle.pendown()

# Draw a rectangle
for side in range(2):
    my_turtle.forward(building_width)
    my_turtle.right(90)
    my_turtle.forward(building_height)
    my_turtle.right(90)

# Draw the roof (triangle on top)
my_turtle.penup()
my_turtle.goto(-75, 50)
my_turtle.pendown()
my_turtle.left(45)
my_turtle.forward(106)  # length of roof side
my_turtle.right(90)
my_turtle.forward(106)
my_turtle.right(135)
my_turtle.forward(building_width)

# Draw the window in the roof
my_turtle.penup()
my_turtle.goto(10, 65)
my_turtle.pendown()
for i in range(4):
    my_turtle.forward(20)
    my_turtle.right(90)

window.exitonclick()
