import random

# Exercise 1: What Are You Learning?
# Goal: Create a function that displays a message about what you’re learning.
def display_message():
    print('I am learning about functions in Python.')
display_message()

# Exercise 2: What’s Your Favorite Book?
# Goal: Create a function that displays a message about a favorite book.
def favorite_book(title):
    print(f'One of my favorite books is {title}.')
favorite_book('Blood Meridian')

# Exercise 3: Some Geography
# Goal: Create a function that describes a city and its country.
def describe_city(city, country = 'Unknown'):
    print(f'{city} is in {country}')
describe_city('Rabat', 'Morocco')
describe_city('New York')

# Exercise 4: Random
# Goal: Create a function that generates random numbers and compares them.
def random_compare(number):
    random_number = random.randint(1, 100)
    print(f'{'Success!' if number == random_number else f'Fail! Your number: {number}, Random number: {random_number}'}')
random_compare(1)

# Exercise 5: Let’s Create Some Personalized Shirts!
# Goal: Create a function to describe a shirt’s size and message, with default values.
def make_shirt(size = 'large', text = 'I love python'):
    print(f'The size of the shirt is {size} and the text is {text}.')
make_shirt('large')
make_shirt('medium')
make_shirt('small', 'I hate javascript!')
make_shirt(size = 'extra-large', text = 'Hello world!')

# Exercise 6: Magicians…
# Goal: Modify a list of magician names and display them in different ways.
magicians = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# Step 2: Create a Function to Display Magicians
def show_magicians(magicians_list):
    for magician in magicians_list:
        print(magician)
# Step 3: Create a Function to Modify the List
def make_great(magicians_list):
    for i in range(len(magicians_list)):
        magicians_list[i] += ' the Great.'
# Step 4: Call the Functions
make_great(magicians)
show_magicians(magicians)

# Exercise 7: Temperature Advice
# Goal: Generate a random temperature and provide advice based on the temperature range.
def get_random_temp():
    return round(random.uniform(-10, 41), 2)
# Modify get_random_temp() to return temperatures specific to each season.
def get_random_temp_month(month = 1):
    min_temp = -10
    max_temp = 10
    if month in ['9', '10', '11']: # Fall
        print('It\'s Fall')
        min_temp = 10
        max_temp = 20
    elif month in ['3', '4', '5']: # Spring
        print('It\'s Spring')
        min_temp = 20
        max_temp = 25
    elif month in ['6', '7', '8']: # Summer
        print('It\'s summer')
        min_temp = 23
        max_temp = 41
    else:
        print('It\'s winter')
    return round(random.uniform(min_temp, max_temp), 2)
def main():
    temp = get_random_temp()
    print(f'The temp right now is {temp}.')
    if temp < 0:
        print('Brrr, that’s freezing! Wear some extra layers today.')
    elif temp < 16:
        print('Quite chilly! Don’t forget your coat.')
    elif temp < 23:
        print('Nice weather.')
    elif temp < 32:
        print('A bit warm, stay hydrated.')
    else:
        print('It’s really hot! Stay cool.')
    month = input('Give a month (1 to 12)\t')
    if month not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
        month = str(random.randint(1, 13))
    temp_month = get_random_temp_month(month)
    print(f'The temp of month {month} right now is {temp_month}.')
    if temp_month < 0:
        print('Brrr, that’s freezing! Wear some extra layers today.')
    elif temp_month < 16:
        print('Quite chilly! Don’t forget your coat.')
    elif temp_month < 23:
        print('Nice weather.')
    elif temp_month < 32:
        print('A bit warm, stay hydrated.')
    else:
        print('It’s really hot! Stay cool.')
main()