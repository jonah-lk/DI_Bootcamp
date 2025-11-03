# Exercise 2 : List of integers
# Given a list of 10 integers to analyze.
# 1. Store the list of numbers in a variable.
# 2. Print the following information:
#     a. The list of numbers – printed in a single line
#     b. The list of numbers – sorted in descending order (largest to smallest)
#     c. The sum of all the numbers
# 3. A list containing the first and the last numbers.
# 4. A list of all the numbers greater than 50.
# 5. A list of all the numbers smaller than 10.
# 6. A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
# 7. The numbers without any duplicates – also print how many numbers are in the new list.
# 8. The average of all the numbers.
# 9. The largest number.
# 10.The smallest number.
# 11. Bonus: Find the sum, average, largest and smallest number without using built in functions.
# 12. Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Repeat this question 10 times. Each number should be added into a variable that you created earlier.
# 13. Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
# 14. Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
# 15. Bonus: Will the code work when the number of random numbers is not equal to 10?
import random
# 1
num_list = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
# 2
print(num_list)
print(num_list.sort(reverse = True))
print(sum(num_list))
# 3
first_last_list = [num_list[0], num_list[len(num_list) - 1]]
# 4
greater_than_50 = []
for item in num_list:
    if item > 50:
        greater_than_50.append(item)
# 5
lesser_than_10 = []
for item in num_list:
    if item < 10:
        lesser_than_10.append(item)
# 6
for item in num_list:
    print(item ** 2)
# 7
print(len(num_list))
unique_only = set(num_list)
print(len(unique_only))
# 8
total = 0
for item in num_list:
    total += item
average = total / len(num_list)
# 9
max_num = max(num_list)
# 10
min_number = min(num_list)
# 11
list_sum = 0
list_max = 0
list_min = 0
print(list_max)
for item in num_list:
    list_sum += item
    if list_max < item:
        list_max = item
    if list_min > item:
        list_min = item
list_average = list_sum / len(num_list)
# 12
user_input_numbers = []
for i in range(10):
    num = int(input('Give number between -100 and 100\t'))
    if  num < -100 or num > 100:
        print('Why won\'t you listen')
        num = random.randint(-100, 100)
    user_input_numbers.append(num)
# 13
random_numbers = []
for i in range(10):
    num = random.randint(-100, 100)
    random_numbers.append(num)
# 14
iterations = random.randint(0, 50)
double_random_numbers = []
for i in range(0, iterations):
    num = random.randint(-100, 100)
    double_random_numbers.append(num)
# 15 
# Yes