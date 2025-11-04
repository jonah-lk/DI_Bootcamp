import re

# Exercise 1: Converting Lists into Dictionaries
# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.
keys = ['first_name', 'last_name', 'age']
values = ['Jonah', 'Lakhdar', '25']
my_dict = {key: value for key in keys for value in values}

# Exercise 2: Cinemax #2
# Write a program that calculates the total cost of movie tickets for a family based on their ages.
# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# Loop through the family dictionary to calculate the total cost.
total_cost = 0
for item in family.items():
    # Print the ticket price for each family member.
    if item[1] < 3:
        print(f'{item[0]} - {0}$')
        continue
    print(f'{item[0]} - {10 if item[1] <= 12 else 15}$')
    total_cost += 10 if item[1] <= 12 else 15
# Print the total cost at the end.
print(f'Total: {total_cost}$')
# Bonus: Allow the user to input family members’ names and ages, then calculate the total ticket cost.
family = {}
total_cost = 0
pattern = r'^([A-Za-z]+)\s(\d+)$'
print('Insert buyers detail. Type quit if done.')
while True:
    family_member = input('Name and age please. (space searated)\t')
    if family_member == 'quit':
        break
    if not re.match(pattern, family_member.strip()):
        print('Invalid input! Try again')
        continue
    name, age = re.findall(pattern, family_member.strip())[0]
    family[name] = int(age)
    if int(age) < 3:
        print(f'{name} - {0}$')
        continue
    print(f'{name} - {10 if int(age) <= 12 else 15}$')
    total_cost += 10 if int(age) <= 12 else 15
print(f'Total: {total_cost}$')

# Exercise 3: Zara
# Create and manipulate a dictionary that contains information about the Zara brand.
# Create a dictionary called brand with the provided data.
brand = {'name': 'Zara', 'creation_date': '1975', 'creator_name': 'Amancio Ortega Gaona', 'number_stores': 7000,
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'mojor_color': {'France': 'blue', 'Spain': 'red', 'Us': ['pink', 'green']}}
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
brand['number_stores'] = 2
# Print a sentence describing Zara’s clients using the type_of_clothes key.
print(f'{brand['name']}\'s target clients are: {', '.join(brand['type_of_clothes'])}')
# Add a new key country_creation with the value Spain.
brand['country_creation'] = 'Spain'
# Check if international_competitors exists and, if so, add “Desigual” to the list.
if 'international_competitors' in brand.keys():
    brand['international_competitors'].append('Desigual')
# Delete the creation_date key.
del brand['creation_date']
# Print the last item in international_competitors.
print(f'{brand['international_competitors'][len(brand['international_competitors']) - 1]}')
# Print the major colors in the US.
print(f'Major colors in the US: {', '.join(brand['mojor_color']['Us'])}')
# Print the number of keys in the dictionary.
print(f'Keys count in dic: {len(brand.keys())}')
# Print all keys of the dictionary.
print(f'Keys in dic: {', '.join(brand.keys())}')
# Bonus:
# Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.
more_on_zara = {'creation_date': '1975', 'number_stores': 0}
brand.update(more_on_zara)
print(brand)