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
# This program uses the turtle graphics library to draw an equilateral triangle.

###
import turtle

window = turtle.Screen()
window.setup(width=800, height=600)
window.title("Equilateral Triangle")

a_turtle = turtle.Turtle()
a_turtle.speed(0)

# Draw an equilateral triangle
side_length = 200
angle = 120  # exterior angle for equilateral triangle

for side in range(3):
    a_turtle.forward(side_length)
    a_turtle.right(angle)

a_turtle.hideturtle()
window.exitonclick()
