# Exercise 1 : What’s your name ?
# Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name 3: last_name.
def get_full_name(first, last, middle = None):
    print(f'{first}{' ' + middle if middle else ''}{' ' + last}')
get_full_name('Younes', 'Lakhdar')
get_full_name('Lionel', 'Messi', 'Andres')
get_full_name(first = 'Lionel', middle = 'Andres', last = 'Messi')

# Exercise 2 : From English to Morse
# Write a function that converts English text to morse code and another one that does the opposite.
english_to_morse = {
    # Letters
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    
    # Numbers
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    
    # Punctuation
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.",
    "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
    "&": ".-...",  ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.",  "-": "-....-", "_": "..--.-", '"': ".-..-.",
    "$": "...-..-", "@": ".--.-.", ' ': '/'
}
def en_to_morse(text):
    encoded = ''
    for ch in text:
        encoded += english_to_morse[ch.upper()] + ' '
    return encoded
text = input('Give some text!\t')
print(en_to_morse(text))

# Exercise 3 : Box of stars
# Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
def box_printer(*args):
    max_width = 0
    for arg in args:
        if len(arg) > max_width:
            max_width = len(arg)
    print(f'# **{'*' * max_width}*')
    for arg in args:
        print(f'# * {arg}{' ' * (max_width - len(arg))}*')
    print(f'# **{'*' * max_width}*')    
box_printer("Hello", "World", "in", "reallylongword", "a", "frame")

# Exercise 4 : What is the purpose of this code?
# Analyse this code before executing it. What is the purpose of this code?

# This function sorts a list
# We go through the list with indeces
# we store the value of the index we are currently in
# we skip the first index to not compare with end of the list
# we compare the value with the preceding value
# if it's superior we set the lesser (current index value) to the precedding
# we set the index to the preceding index
# we put the original index' value that we stored in the new index (preceding)
# else we set the value to it's same value (nothing changed)
# in the end the list is sorted in ascending order
def insertion_sort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1

        alist[position] = currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)