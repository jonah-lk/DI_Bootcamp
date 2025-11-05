import math
# Perfect number
# A perfect number is a positive integer that is equal to the sum of its divisors.
# However, the number itself is not included in the sum.
# Ask the user for a number and print whether or not it is a perfect number. If yes, print True else False.
# Hint: Google perfect numbers
# Example
# Input -- Enter the number:6
# Output -- True
# Input -- Enter the number:10
# Output --  False
try:
    number = int(input('Give a number.\t'))
    factors = []
    for num in range(1, math.floor(number / 2) + 1):
        if number % num == 0:
            factors.append(num)
    is_perfect_number = True if sum(factors) == number else False
    print(is_perfect_number)
except:
    print('Not a number!')