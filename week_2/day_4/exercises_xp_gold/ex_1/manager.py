import os, json

class Manager:
    def __init__(self):
        self.menu = {}
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(base_dir, "menu.json")
        with open(self.file_path, 'r') as file:
            self.menu = json.load(file)
    
    def __str__(self):
        menu = ''
        for item in self.menu['items']:
            menu += f'{item['name']}: {item['price']}$\n'
        return menu
    
    def add_item(self, name: str, price: float):
        self.menu['items'].append({'name': name, 'price': price})

    def remove_item(self, name: str):
        for i, item in enumerate(self.menu['items']):
            if name == item['name']:
                del self.menu['items'][i]
                return True
        return False
    
    def save_to_file(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.menu, file, indent=4)

manager = Manager()
print(manager)
manager.add_item('Stake', 50)
print(manager)
manager.save_to_file()
print(manager.remove_item('Stake'))
print(manager)
manager.save_to_file()