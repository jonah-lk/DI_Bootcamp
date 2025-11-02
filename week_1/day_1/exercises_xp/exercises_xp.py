#Exercise 1: Hello World
#Print the following output using one line of code:
#Hello world
#Hello world
#Hello world
#Hello world
print('Hello world\n' * 4)

# Exercise 2: Some Math
# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).
result = (99 ** 3) * 8
print(f'99 cubed x 8 = {result}\n')

#Exercise 3: What is the output?
#Predict the output of the following code snippets: Comment what is your guess, then run the code and compare
try:
    5 < 3 #False
    3 == 3 #True
    3 == "3" #False
    "3" > 3 #Type error
    "Hello" == "hello" #False
except:
    print('Type errors!\n')

# Exercise 4: Your computer brand
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable, print a sentence that states the following: "I have a <computer_brand> computer."
computer_brand = 'Lenovo Ideapad 5'
print(f'I have a {computer_brand} computer\n')

# Exercise 5: Your information
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
# Have your code print the info message.
name = 'Younes'
age = 25
shoe_size = 40
info = f'My name is {name} and I\'m {age}. Funny fact about me is I\'m a history nerd. My shoe size is {shoe_size}.'
print(info + '\n')

# Exercise 6: A & B
# Create two variables, a and b. Each variable’s value should be a number. If a is bigger than b, have your code print "Hello World".
a = 5
b = 2
if a > b:
    print('Hello world\n')

# Exercise 7: Odd or Even
# Write code that asks the user for a number and determines whether this number is odd or even.
number = input('Type a number:\t')
try:
    if int(number) % 2 == 0:
        print(f'The number {number} is even\n')
    else:
        print(f'The number {number} is odd\n')
except:
    print('Input was not a number!\n')

# Exercise 8: What’s your name?
# Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.
my_name = 'Younes'
user_name = input('What\'s your name?\t')
if my_name.lower() == user_name.lower():
    print('You might be me!\n')
else:
    print('Hello stranger!\n')

# Exercise 9: Tall enough to ride a roller coaster
# Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride. If they are not tall enough, print a message that says they need to grow some more to ride.
height = input('What\'s your height? (in cm)\t')
try:
    if int(height) > 145:
        print('You are allowed to go for a ride.\n')
    else:
        print('Too short!\n')
except:
    print('Height must be a number!\n')