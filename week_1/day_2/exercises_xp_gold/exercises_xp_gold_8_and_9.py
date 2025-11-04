# Exercise 8 : List and Tuple
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
user_input = input('Give a sequence of numbers. (Integers coma separated)\t')
user_input = user_input.split(',')
print(user_input)

# Exercise 9 : Random number
import random

# Ask the user to input a number from 1 to 9 (including).
try:
    # Get a random number between 1 and 9. Hint: random module.
    user_number = int(input('Give number between 1 and 9:\t'))
    random_number = random.randint(1, 9)
    # If the user guesses the correct number print a message that says Winner.
    if user_input == str(random_number):
        print('Winner!')
    # If the user guesses the wrong number print a message that says better luck next time.
    else:
        print('Better luck next time!')

    # Bonus: use a loop that allows the user to keep guessing until they want to quit.
    while True:
        user_number = input('Give number between 1 and 9: (Type 0 to quit)\t')
        if user_number == '0':
            break
        random_number = random.randint(1, 9)
        if user_number == str(random_number):
            print('Winner!')
        else:
            print('Better luck next time!')
except:
    print('Invalid integer!')

# Bonus 2: on exiting the loop tally up and display total games won and lost.
won = 0
lost = 0
while True:
    user_number = input('Give number between 1 and 9: (Type 0 to quit)\t')
    if user_number == '0':
        break
    random_number = random.randint(1, 9)
    if user_number == str(random_number):
        print('Winner!')
        won += 1
    else:
        print('Better luck next time!')
        lost += 1
print(f'You won {won} and lost {lost} games in total!')