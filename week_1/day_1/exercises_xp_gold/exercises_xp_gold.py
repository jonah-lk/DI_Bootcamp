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
try:
    # Ask the user to input a month (1 to 12).
    month = input('What is the month? (1 for Jan, 12 for Dec)\t')
    month = int(month)
    # Display the season of the month received :
    # Spring runs from March (3) to May (5)
    if month in [3, 4, 5]:
        print('It\'s spring.\n')
    # Summer runs from June (6) to August (8)
    elif month in [6, 7, 8]:
        print('It\'s summer.\n')
    # Autumn runs from September (9) to November (11)
    elif month in [9, 10, 11]:
        print('It\'s autumn.\n')
    # Winter runs from December (12) to February (2)
    elif month in [12, 1, 2]:
        print('It\'s winter.\n')
    else:
        print('Months are between 1 an 12.\n')
except:
    print('Month must be a number!\n')