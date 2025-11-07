# Exercise 1
# Write a script that inserts an item at a defined index in a list.
def insert_at_index(list_ex1, item, index):
    try:
        list_ex1.insert(index, item)
    except:
        print('Something is wrong with your input!')
list_1 = [10, 20, 25, 30, 40]
insert_at_index(list_1, 50, 0)

# Exercise 2
# Write a script that counts the number of spaces in a string.
def spaces_count(string):
    count = 0
    try:
        count = string.count(' ')
    except:
        print('Something is wrong with your input!')
    return count
count_2 = spaces_count(' Hello  World! ')

# Exercise 3
# Write a script that calculates the number of upper case letters and lower case letters in a string.
def upper_lower_count(text):
    upper_count = 0
    lower_count = 0
    try:
        for ch in text:
            if ch.isupper():
                upper_count += 1
            elif ch.islower():
                lower_count += 1
    except:
        print('Something is wrong with your input!')
    return (upper_count, lower_count)
upper_count, lower_count = upper_lower_count('Hello World!')

# Exercise 4
# Write a function to find the sum of an array without using the built in function
def my_sum(list_ex4):
    list_sum = 0
    try:
        for number in list_ex4:
            list_sum += float(number)
    except:
        print('Something is wrong with your input!')
    return round(list_sum, 2)
list_4 = [1, 2, 3, 4, 5, 6]
sum_list_4 = my_sum(list_4)

# Exercise 6
# Write a function that returns factorial of a number
def factorial(number):
    factorial = 1
    try:
        for i in range(1, int(number) + 1):
            factorial *= i
    except:
        print('Something is wrong with your input!')
    return factorial
number = 5
factorial_of_number = factorial(number)

# Exercise 7
# Write a function that counts an element in a list (without using the count method)
def my_count(list_ex7, value):
    count = 0
    try:
        for item in list_ex7:
            if item == value:
                count += 1
    except:
        print('Something is wrong with your input!')
    return count
list_7 = [1, 2, 3, 4, 5, 6, 7 , 8, 9]
list_count = my_count(list_7, 1)