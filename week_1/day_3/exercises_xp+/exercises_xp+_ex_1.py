# Exercise 1 : Student Grade Summary
# You are given a dictionary containing student names as keys and lists of their grades as values. Your task is to create a summary report that calculates the average grade for each student, assigns a letter grade, and determines the class average.
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}
# Requirements:
# Calculate the average grade for each student and store the results in a new dictionary called student_averages.
student_averages = {key: round(sum(value) / len(value), 2) for key, value in student_grades.items()}
# Assign each student a letter grade (A, B, C, D, F) based on their average grade according to the following scale, and store the results in a dictionary called student_letter_grades:
# A: 90 and above
# B: 80 to 89
# C: 70 to 79
# D: 60 to 69
# F: Below 60
student_letter_grades = {}
for student, grade in student_averages.items():
    if grade < 60:
        student_letter_grades[student] = 'F'
    elif grade < 70:
        student_letter_grades[student] = 'D'
    elif grade < 80:
        student_letter_grades[student] = 'C'
    elif grade < 90:
        student_letter_grades[student] = 'B'
    else:
        student_letter_grades[student] = 'A'
# Calculate the class average (the average of all students’ averages) and print it.
class_sum = round(sum(student_averages.values()), 2)
class_average = round(class_sum / len(student_averages), 0)
print(class_average)
# Print the name of each student, their average grade, and their letter grade.
for student, grade in student_averages.items():
    print(f'Student: {student}, Average grade: {grade}, Letter grade: {student_letter_grades[student]}')