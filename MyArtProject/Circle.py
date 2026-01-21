###

#File: Circle.py

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
# This program uses the turtle graphics library to draw a circle
# with a gradient color effect.

###

import turtle

window = turtle.Screen()
window.setup(width=800, height=600)
window.title("Circle")

a_turtle = turtle.Turtle()
a_turtle.speed(0)
a_turtle.pensize(5)

# Draw a circle using 360 segments with gradually increasing purple
segment_length = 1
num_segments = 360
angle_per_segment = 360 / num_segments

for segment in range(num_segments):
    # Calculate purple color - gradually increase from dark to light purple
    purple_intensity = segment / num_segments
    a_turtle.pencolor(purple_intensity * 0.5, 0, purple_intensity)
    a_turtle.forward(segment_length)
    a_turtle.right(angle_per_segment)
    
a_turtle.hideturtle()
window.exitonclick()
