# Exercise 1: Concatenate lists
# Write code that concatenates two lists together without using the + sign.
sub_string_1 = 'Hello my name is Jonah.'
sub_string_2 = 'I\'m 25 years old.'
concat_strings = f"{sub_string_1} {sub_string_2}"

# Exercise 2: Range of numbers
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
print('Multiples of 5 and 7 in the range 1500 2500')
for n in range(1500, 2501):
    if n % 5 == 0 or n % 7 == 0:
        print(n)

# Exercise 3: Check the index
# Using this variable: names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name. 
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_input = input('What\'s your name?\t')
try:
    index = names.index(user_input.capitalize())
    print(index)
except:
    print('Your name is not in the list.')

# Exercise 4: Greatest Number
# Ask the user for 3 numbers and print the greatest number.
count = 0
numbers = []
while count < 3:
    try:
        number = int(input('Give a number:\t'))
        numbers.append(number)
        count += 1
    except:
        print('Invalid number. Try again.')
print(f'The max is {max(numbers)}')
print(numbers)

# Exercise 5: The Alphabet
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.
vowels = ['a', 'e', 'o', 'i', 'y', 'u']
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for alpha in alphabets:
    if alpha in vowels:
        print(f'{alpha} is a vowel.')
    else:
        print(f'{alpha} in not a vowel.')

# Exercise 6: Words and letters
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.
words = []
for i in range(7):
    word = input('Give a word.\t')
    words.append(word)
character = input('Give a character. \t')
if len(character) != 1:
    print('Invalid! Your character is a.')
    character = 'a'
for word in words:
    try:
        print(f'Index of {character} in {word} is: {word.index(character)}')
    except:
        print('The character is not in this word buddy!')

# Exercise 7: Min, Max, Sum
# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.
numbers = []
for n in range(1, 1_000_001):
    numbers.append(n)
print(f'Min: {min(numbers)}. Max: {max(numbers)}.')
print(sum(numbers))
