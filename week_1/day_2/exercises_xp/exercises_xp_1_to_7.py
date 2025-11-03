# Exercise 1: Favorite Numbers
# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
my_fav_numbers = {1, 2, 3, 4, 5}
my_fav_numbers.update({7, 8})
my_fav_numbers.remove(8)
friend_fav_numbers = {9, 10}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

# Exercise 2: Tuple
# Given a tuple of integers, try to add more integers to the tuple.
my_tuple = (1, 2, 3)
try:
    my_tuple.append(4)
except:
    print('Tuples are immutable!')

# Exercise 3: List Manipulation
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.
basket = ['Banana', 'Apples', 'Oranges', 'Blueberries']
basket.remove('Banana')
basket.remove('Blueberries')
basket.append('Kiwi')
basket.insert(0, 'Apples')
apples_count = basket.count('Apples')
basket.clear()
print(basket)

# Exercise 4: Floats
# Create a list containing the following sequence of mixed types: floats and integers: 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
num_list = []
for n in range(2, 6):
    num_list.append(n - 0.5)
    num_list.append(n)

# Exercise 5: For Loop
# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.
for i in range(1, 21):
    print(i)
for i in range(2, 21, 2):
    print(i)
    
# Exercise 6: While Loop
# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
while True:
    proper_name = input('What\'s your name? (No digits and at least 3 letters long)\t')
    if len(proper_name) < 3 or proper_name.isdigit() or any(chr in proper_name for chr in numbers):
        continue
    else:
        print('thank you')
        break

# Exercise 7: Favorite Fruits
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print: "You chose one of your favorite fruits! Enjoy!"
# If not, print: "You chose a new fruit. I hope you enjoy it!"
fav_fruits = input('What are your favorite fruits? (List them here space separated)\t')
fav_fruits = fav_fruits.split(' ')
random_fruit = input('Now give us a random fruit.\t')
if random_fruit in fav_fruits:
    print('You chose one of your fav fruits. Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy!')
