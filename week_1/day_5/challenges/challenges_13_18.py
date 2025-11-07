import re
# Exercise 13
# Write a function that returns the amount of words in a sentence with length > k
def count_words_longer_than(string, length = 3):
    count = 0
    try:
        for word in re.split(r'[^A-Za-z]+', string):
            if len(word) > length:
                count += 1
    except:
        print('Something is wrong with your input!')
    return count
sentence = 'Hello, world! 123 Nice-day.'
length = 3
sentence_count = count_words_longer_than(sentence, length)

# Exercise 14
# Write a function that returns the average value in a dictionary (assume the values are numeric)
def average_value(numeric_list):
    list_sum = 0
    try:
        list_sum = sum(numeric_list)
    except:
        print('None numeric value in list!')
    average = round(list_sum / len(numeric_list), 2)
    return average
num_list = [1, 2, 3, 4, 5, 6, 7 ,8 ,9]
average = average_value(num_list)

# Exercise 15
# Write a function that returns common divisors of 2 numbers
def common_factors(num_1, num_2):
    factors = []
    try:
        min_num = int(min(num_1, num_2))
        max_num = int(max(num_1, num_2))
        for num in range(1, int((min_num) / 2) + 1):
            if num_1 % num == 0 and num_2 % num == 0:
                factors.append(num)
        if max_num % min_num == 0:
            factors.append(min_num)
    except:
        print('Give two integer values!')
    return factors
num_1 = 20
num_2 = 25
num_1_2_factors = common_factors(num_1, num_2)

# Exercise 16
# Write a function that test if a number is prime
def is_prime(number):
    result = True
    for num in range(2, int(int((number) / 2) + 1)):
        if int(number) % num == 0:
            result = False
            break
    return result
number = 4
is_it_prime = is_prime(number)

# Exercise 17
# Write a function that prints elements of a list if the index and the value are even
def print_if_index_value_even(num_list):
    try:
        for i in range(len(num_list)):
            if i % 2 == 0 and int(num_list[i]) % 2 == 0:
                print(f'Index: {i}, value: {num_list[i]}')
    except:
        print('None numeric value in list!')
num_list = [1,2,2,3,4,5, 6, 6]
print_if_index_value_even(num_list)

# Exercise 18
# Write a function that accepts an undefined number of keyworded arguments and return the count of different types
def useless_function(**kwargs):
    type_count = {}
    for kwarg in kwargs.values():
        try:
            type_count[type(kwarg).__name__] += 1
        except:
            type_count[type(kwarg).__name__] = 1
    return type_count
types_object = useless_function(num_1 = 42, num_2 = 3.14, string_1 = "hello", bool_1 = True, bool_2 = False, none = None, string_3 = "world", num_3 = 7)