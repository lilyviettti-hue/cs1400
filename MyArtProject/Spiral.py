###

#File: Spiral.py

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
# This program uses the turtle graphics library to draw a spiral pattern.

###

import turtle

window = turtle.Screen()
window.title("Spiral")
my_turtle = turtle.Turtle()

# Draw a spiral with increasing segment lengths
segment_length = 5
angle_turn = 90
num_segments = 20
for segment in range(num_segments):
    my_turtle.forward(segment_length)
    my_turtle.right(angle_turn)
    segment_length += 5

window.exitonclick()
