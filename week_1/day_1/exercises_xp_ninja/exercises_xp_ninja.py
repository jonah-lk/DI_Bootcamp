# Exercise 3 : Outputs
# Predict the output of the following code snippets:
3 <= 3 < 9 #True
3 == 3 == 3 #True
bool(0) #False
bool(5 == "5") #False
bool(4 == 4) == bool("4" == "4")  #True
bool(bool(None)) # False
x = (1 == True) #True
y = (1 == False) #False
a = True + 4 #5
b = False + 10 #10

# Exercise 4 : How many characters in a sentence ?
# Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).
my_text = """   Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                Ut enim ad minim veniam, quis nostrud exercitation ullamco 
                laboris nisi ut aliquip ex ea commodo consequat. 
                Duis aute irure dolor in reprehenderit in voluptate velit 
                esse cillum dolore eu fugiat nulla pariatur. 
                Excepteur sint occaecat cupidatat non proident, 
                sunt in culpa qui officia deserunt mollit anim id est laborum."""
print(f'my_text variable holds {len(my_text)} characters.')

# Exercise 5: Longest word without a specific character
# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.
record = 0
while True:
    user_input = input('Give the longest sentence you can write without A. (If you want to quit type 0)\t')
    if user_input == '0':
        break
    elif 'A'.lower() in user_input.lower():
        print('Your sentence includes the char A/a! Try again.\n')
    elif len(user_input.split('.')) > record:
        record = len(user_input.split('.'))
        print('You beat your previous record! Congrats\n')
    else:
        print('Your sentence is valid. But you couldn\'t beat your old record!\n')

print(f'Good game. Your record is {record}')