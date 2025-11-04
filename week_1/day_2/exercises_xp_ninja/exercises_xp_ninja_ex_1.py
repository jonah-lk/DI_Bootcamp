# Exercise 1: Formula
import math

# Write a program that calculates and prints a value according to this given formula:
# Q = Square root of [(2 * C * D)/H]
# C is 50.
C = 50
# H is 30.
H = 30
def formula(digit):
    return int(math.sqrt((2 * C * digit) / H))
# Following are the fixed values of C and H:
# Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
numbers = input('List of numbers comma separated\t')
for num in numbers.split(','):
    Q = formula(int(num))
    print(f'Number: {num}. Q: {Q}')