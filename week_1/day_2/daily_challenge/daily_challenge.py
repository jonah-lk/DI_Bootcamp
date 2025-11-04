# Challenge 1: Multiples of a Number
try:
    # 1. Ask the user for two inputs:
    # A number (integer).
    # A length (integer).
    number = int(input('Give an integer:\t'))
    length = int(input('Give a length:\t'))
    # 2. Create a program that generates a list of multiples of the given number.
    # 3. The list should stop when it reaches the length specified by the user.
    print(f'Multiples of {number}')
    for factor in range(1, length + 1):
        print(f'{number} x {factor} = {number * factor}')
except:
    print('Inputs must be integers!')

# Challenge 2: Remove Consecutive Duplicate Letters
# 1. Ask the user for a string.
string = input('Give a random string:\t')
# 2. Write a program that processes the string to remove consecutive duplicate letters.
# The new string should only contain unique consecutive letters.
no_dups = []
for i in range(1, len(string)):
    if string[i - 1] == string[i] and i != 1:
        continue
    no_dups.append(string[i])
no_dups_string = ''.join(no_dups)
# 3. The program should print the modified string.
print(no_dups_string)