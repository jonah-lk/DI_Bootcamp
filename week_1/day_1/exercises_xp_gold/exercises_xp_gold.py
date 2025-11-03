# Exercise 1 : Hello World-I love Python
# Print the following output in one line of code:
# Hello world
# Hello world
# Hello world
# Hello world
# I love python
# I love python
# I love python
# I love python
print('Hello world\n' * 4 + 'I love Python\n' * 4)

# Exercise 2 : What is the Season ?
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)
try:
    month = input('What is the month? (1 for Jan, 12 for Dec)\t')
    month = int(month)
    if month in [3, 4, 5]:
        print('It\'s spring.\n')
    elif month in [6, 7, 8]:
        print('It\'s summer.\n')
    elif month in [9, 10, 11]:
        print('It\'s autumn.\n')
    elif month in [12, 1, 2]:
        print('It\'s winter.\n')
    else:
        print('Months are between 1 an 12.\n')
except:
    print('Month must be a number!\n')