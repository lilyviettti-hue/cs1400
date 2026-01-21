# Author:    Lily Vietti, u1411969
# Date:      2026-01-13
# Course:    CS 1400-001, University of Utah, Kahlert School of Computing
# Instructor: H. James de St. Germain
# Copyright: CS 1400 and [Your Name(s)] - This work may not
#            be copied for use in Academic Coursework.
#
# I, Lily Vietti, certify that I wrote this code from scratch and did not
# copy it in part or whole from any other source. Any references used in 
# the completion of the assignment are cited in my README file.
#
# File Contents/Program Purpose:
#    This program predicts a student's final grade based
#    on the scores the input for their programming assignments, 
#    quizzes, and labs. The program will then calculate the final 
#    grade for the course based on the possible midterm averages 
#    of 0, 20, 40, 60, 80, and 100.


def main():

    # Ask the user for their name.
    users_name = input("Enter your first name: ")

    # Ask the user's average scores for their programming
    # assignments, quizzes, and labs.
    avg_programming_assignments = float(input("Enter your Programming Assignments average (0-100): "))
    avg_quizzes = float(input("Enter your Quizzes average (0-100): "))
    avg_labs = float(input("Enter your Labs average (0-100): "))

    # Weight of categories (as percentages)
    weight_programming = 10
    weight_quizzes = 25
    weight_labs = 10
    weight_midterms = 55

    # Multiplying each of the users average scores for their assignments 
    # and possible midterm averages they might recieve (0, 20, 40, 60, 
    # 80, and 100 via a for loop) by the weight of each category, 
    # then calculating the sum of those weighted scores to get the total 
    # percentage forthe course.
    for midterm_avg in [0, 20, 40, 60, 80, 100]:
        total = (weight_programming * avg_programming_assignments
            + weight_quizzes * avg_quizzes
            + weight_labs * avg_labs
            + weight_midterms * midterm_avg)
        
        # Convert final course score to a percentage.
        course_percentage = total / 100.0

        # Print results.
        print(f"{users_name}, if your average midterm exam score is {midterm_avg} your course percentage for CS 1400 will be {course_percentage:.2f}.")


if __name__ == "__main__":
    main()
