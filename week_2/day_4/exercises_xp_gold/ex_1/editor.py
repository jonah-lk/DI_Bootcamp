from manager import Manager

def load_manager():
    return Manager()

def show_user_menu():
    print("1. Show restaurant menu")
    print("2. Add item to menu")
    print("3. Remove item from menu")
    print("4. Exit")

    choice = input("Choose an option: ")
    
    if choice in ['1', '2', '3', '4']:
        return choice
    else:
        raise Exception('Invalid input!')
    
def add_item_to_menu(manager: Manager):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    
    manager.add_item(name, price)
    print(f"Item '{name}' added successfully.")
    
def remove_item_from_menu(manager: Manager):
    name = input("Enter item name to remove: ")
    
    success = manager.remove_item(name)
    if success:
        print(f"Item '{name}' removed successfully.")
    else:
        print(f"Error: item '{name}' not found.")
    
def show_restaurant_menu(manager: Manager):
    print(manager)

def main():
    manager = load_manager()
    
    while True:
        choice = show_user_menu()
        if choice == "1":
            show_restaurant_menu(manager)
        elif choice == "2":
            add_item_to_menu(manager)
        elif choice == "3":
            remove_item_from_menu(manager)
        elif choice == "4":
            manager.save_to_file()
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__": # his ensures that main() runs only when you run this file directly, not if it’s imported somewhere else.
    main()