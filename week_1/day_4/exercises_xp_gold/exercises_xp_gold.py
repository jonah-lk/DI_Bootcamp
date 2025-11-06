import re
import random
# Exercise 1 : When will I retire ?
current_year = 2025
pattern = r'^(\d{4})/(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])$'
def get_age(current_year, birthday):
    year, month, day = re.match(pattern, birthday).groups()
    return current_year - int(year)
def can_retire(gender, birthday):
    age = get_age(current_year, birthday)
    if (gender.lower() == 'm' and age < 67) or (gender.lower() == 'f' and age < 62):
        return False
    else:
        return True

a_birthday = ''
a_gender = ''
while True:
    a_birthday = input('What is your birthday! (YYYY/MM/DD) \t')
    a_gender = input('What is your gender? (m or f)\t')
    if not re.match(pattern, a_birthday.strip()) or a_gender.lower() not in ['m', 'f']:
        print('Invalid input! Respect the formats.')
        continue
    else:
        break
retire_now = can_retire(a_gender, a_birthday)
print(f'You {'can' if retire_now else 'can\'t'} retire now.')

# Exercise 2 : Sum
def weird_sum(num):
    return num + (num * 11) + (num * 111) + (num * 1111)
sum_res = weird_sum(5)
print(sum_res)

# Exercise 3 : Double Dice
def throw_dice():
    return random.randint(1, 7)
def throw_2_dice():
    count = 0
    dice_1, dice_2 = (throw_dice(), throw_dice())
    count += 1
    while dice_1 != dice_2:
        dice_1, dice_2 = (throw_dice(), throw_dice())
        count += 1
    return count
def main():
    total_count = 0
    attempts_list = []
    for i in range(100):
        count = throw_2_dice()
        total_count += count
        attempts_list.append(count)
    average_throws = round(total_count / 100, 2)
    print(f'Total throws: {total_count}')
    print(f'Average throws for double: {average_throws}')
    return attempts_list
attempts = main()