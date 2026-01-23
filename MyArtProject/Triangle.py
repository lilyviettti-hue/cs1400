###

#File: Triangle.py

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
# This program uses a turtle to draw an equilateral triangle.

###

import turtle

window = turtle.Screen()
window.title("Equilateral Triangle")
my_turtle = turtle.Turtle()
my_turtle.width(5)

# Draw an equilateral triangle with side length 200
for side in range(3):
    my_turtle.forward(200)
    my_turtle.right(120)

window.exitonclick()
