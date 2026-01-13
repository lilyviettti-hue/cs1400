# Author:    Lily
# Partner:   None
# Date:      2026-01-13
# Course:    CS 1400, University of Utah, Kahlert School of Computing
# Copyright: CS 1400 and Lily - This work may not
#            be copied for use in Academic Coursework.
#
# I, Lily, certify that I wrote this code from scratch and
# did not copy it in part or whole from another source.
#
# File Contents/Program Purpose
#
#    A simple grader program that asks the user for their
#    name and expected averages for Programming Assignments,
#    Quizzes, and Labs, then hypothesizes course percentages
#    for possible midterm averages (0,20,...,100).

def main():
    # Prompt for user's first name
    users_name = input("Enter your first name: ")

    # Prompt for category scores in the required order
    programming_assignments = float(input("Enter your Programming Assignments average (0-100): "))
    quizzes = float(input("Enter your Quizzes average (0-100): "))
    labs = float(input("Enter your Labs average (0-100): "))

    # Category weights (as percentages)
    weight_programming = 10
    weight_quizzes = 25
    weight_labs = 10
    weight_midterms = 55

    # Possible midterm averages to hypothesize
    for midterm_avg in [0, 20, 40, 60, 80, 100]:
        total = (
            weight_programming * programming_assignments
            + weight_quizzes * quizzes
            + weight_labs * labs
            + weight_midterms * midterm_avg
        )
        # Convert to percentage
        course_percentage = total / 100.0

        # Print the nicely formatted result with two decimal places
        print(f"{users_name}, if your average midterm exam score is {midterm_avg} your course percentage for CS 1400 will be {course_percentage:.2f}.")


if __name__ == "__main__":
    main()
