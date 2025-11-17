import re, json, os

name = input("Enter the name of the Valentine item: ")
price = input("Enter the price (format XX,14): ")

def is_valid_name(name):
    if not name[0] == "V":
        return False
    if sum(1 for c in name.lower() if c == "e") < 2:
        return False
    if any(c.isdigit() for c in name):
        return False

    words = name.split()
    connection_words = ["of", "and", "the", "a"]
    for i, word in enumerate(words):
        if i == 0:
            if not word[0].isupper():
                return False
        elif word.lower() in connection_words:
            if not word.islower():
                return False
        else:
            if not word[0].isupper():
                return False
    return True


def is_valid_price(price):
    return re.fullmatch(r"\d{2},14", price) is not None

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "menu.json")

with open(file_path, "r") as file:
    menu = json.load(file)

menu.setdefault("valentine_items", [])

if is_valid_name(name) and is_valid_price(price):
    menu["valentine_items"].append({"name": name, "price": price})
    with open(file_path, "w") as file:
        json.dump(menu, file, indent=4)
    print(f"{name} added to the Valentine menu!")
else:
    print("Invalid item or price. Try again.")

def print_heart():
    for row in range(6):
        for col in range(7):
            if ((row == 0 and col % 3 != 0) or
                (row == 1 and col % 3 == 0) or
                (row - col == 2) or
                (row + col == 8)):
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_heart()