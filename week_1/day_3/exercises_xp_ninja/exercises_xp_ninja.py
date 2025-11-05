# Exercise 1 : Cars
# Copy the following string into your code: 
string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
# Convert it into a list using Python (don’t do it by hand!).
string_to_list = string.split(', ')
# Print out a message saying how many manufacturers/companies are in the list.
print(f'There are {len(string_to_list)} manufactureres in the list.')
# Print the list of manufacturers in reverse/descending order (Z-A).
string_to_list.sort(reverse = True)
print(f'{string_to_list}')
# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
# Find out how many manufacturers’ names do not have the letter ‘i’ in them.
item_has_o = 0
item_has_no_i = 0
for item in string_to_list:
    if 'o' in item:
        item_has_o += 1
    if 'i' not in item:
        item_has_no_i += 1
# Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
# Remove these programmatically. (Hint: you can use set to help you).
string_to_list = set(string_to_list)
# Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.
print(f'{', '.join(string_to_list)}')
print(f'There are {len(string_to_list)} manufactureres now in the list.')
# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.
string_to_list = list(string_to_list)
string_to_list.sort()
for i in range(len(string_to_list)):
    string_to_list[i] = string_to_list[i][::-1]
print(f'{', '.join(string_to_list)}')