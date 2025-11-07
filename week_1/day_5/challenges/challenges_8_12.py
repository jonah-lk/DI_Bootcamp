import math
# Exercise 8
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list
def l2(list_ex8):
    l2_norm = 0
    square_sum = 0
    try:
        for num in list_ex8:
            square_sum += (int(num) ** 2)
    except:
        print('Something is wrong with your input!')
    l2_norm = round(math.sqrt(square_sum), 4)
    return l2_norm
list_8 = [1, 2, 3 , 4, 5, 7, 6]
l2_norm = l2(list_8)

# Exercise 9
# Write a function to find if an array is monotonic (sorted either ascending of descending)
def is_monotonic_list(list_ex9):
    is_monotonic = True
    order = 'asc'
    try:
        prev_item = list_ex9[0]
        for i in range(1, len(list_ex9)):
            if i == 1 and prev_item > list_ex9[i]:
                order = 'desc'
            elif (order == 'asc' and prev_item > list_ex9[i]) or (order == 'desc' and prev_item < list_ex9[i]):
                is_monotonic = False
                break
            prev_item = list_ex9[i]
    except:
        print('Something is wrong with your input!')
    return is_monotonic
list_9 = [1, 2, 3, 3 ,5, 6]
is_list_monotonic = is_monotonic_list(list_9)

# Exercise 10
# Write a function that prints the longest word in a list.
def longest_word_in_list(list_ex10):
    longest_word = ''
    try:
        longest_word = list_ex10[list_ex10.index(max(list_ex10, key = len))]
    except:
        print('Something is wrong with your input!')
    return longest_word
list_10 = ['head', 'body', 'left arm', 'right arm', 'left leg', 'right leg']
longest_word_list = longest_word_in_list(list_10)

# Exercise 11
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.
def split_list_to_int_str(list_ex11):
    int_list = []
    str_list = []
    try:
        for item in list_ex11:
            if isinstance(item, int) and not isinstance(item, bool):
                int_list.append(item)
            elif isinstance(item, str):
                str_list.append(item)
    except:
        print('Something is wrong with your input!')
    return (int_list, str_list)
mixed_list = [42, 3.14, "hello", True, False, None, "world", 7]
int_list, str_list = split_list_to_int_str(mixed_list)

# Exercise 12
# Write a function to check if a string is a palindrome
def is_palindrome(string):
    it_is = True
    try:
        for i in range(int(len(string) / 2)):
            if string[i] != string[len(string) - 1 - i]:
                it_is = False
                break
    except:
        print('Something is wrong with your input!')
    return it_is
word = 'abba'
is_it_palindrome = is_palindrome(word)