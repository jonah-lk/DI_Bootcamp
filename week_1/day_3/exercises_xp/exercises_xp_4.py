# Exercise 4: Disney Characters
# You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# Create a dictionary that maps characters to their indices:
enumerated = [item for item in enumerate(users)]
users_dict_1 = {item[1]: item[0] for item in enumerated}
# Create a dictionary that maps indices to characters:
users_dict_2 = {item[0]: item[1] for item in enumerated}
# Create a dictionary where characters are sorted alphabetically and mapped to their indices:
users.sort()
enumerated = [item for item in enumerate(users)]
users_dict_3 = {item[1]: item[0] for item in enumerated}