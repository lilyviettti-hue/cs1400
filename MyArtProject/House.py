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
window.setup(width=800, height=600)
window.title("House")

a_turtle = turtle.Turtle()
a_turtle.speed(0)

# Draw the main building (rectangle)
building_width = 150
building_height = 100

a_turtle.penup()
a_turtle.goto(-75, 50)
a_turtle.pendown()

# Draw rectangle: top-left to top-right to bottom-right to bottom-left
a_turtle.forward(building_width)
a_turtle.right(90)
a_turtle.forward(building_height)
a_turtle.right(90)
a_turtle.forward(building_width)
a_turtle.right(90)
a_turtle.forward(building_height)
a_turtle.right(90)

# Draw the roof (triangle on top)
a_turtle.penup()
a_turtle.goto(-75, 50)
a_turtle.pendown()

a_turtle.goto(0, 110)
a_turtle.goto(75, 50)
a_turtle.goto(-75, 50)

# Draw the window in the roof
window_size = 20
a_turtle.penup()
a_turtle.goto(-20, 70)
a_turtle.pendown()

for i in range(4):
    a_turtle.forward(window_size)
    a_turtle.right(90)

a_turtle.hideturtle()
window.exitonclick()
