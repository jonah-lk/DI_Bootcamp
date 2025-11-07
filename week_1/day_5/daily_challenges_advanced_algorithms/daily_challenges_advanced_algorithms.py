# Here is a python code that generates a list of 20000 random numbers, called list_of_numbers, and a target number.
import random
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number   = 3728
# Copy this code, and create a program that finds, within list_of_numbers all the pairs of number that sum to the target number
found = []
for num in list_of_numbers:
    try:
        pair = list_of_numbers.index(target_number - num)
        if num <= target_number and num not in found and list_of_numbers[pair]:
            print(f'The pair {num} and {list_of_numbers[pair]} sum to {target_number}')
            found.append(num)
            found.append(list_of_numbers[pair])
    except:
        continue