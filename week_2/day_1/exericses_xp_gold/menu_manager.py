class MenuManager:
    def __init__(self):
        self.menu = [
            {
                'name': 'Soup',
                'price': 10,
                'spice_level': 'B',
                'gluten_index': False
            },
            {
                'name': 'Hamburger',
                'price': 15,
                'spice_level': 'A',
                'gluten_index': True
            },
            {
                'name': 'Salad',
                'price': 18,
                'spice_level': 'A',
                'gluten_index': False
            },
            {
                'name': 'French Fries',
                'price': 5,
                'spice_level': 'C',
                'gluten_index': False
            },
            {
                'name': 'Beef bourguignon',
                'price': 25,
                'spice_level': 'B',
                'gluten_index': True
            }
        ]

    def add_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish['name'] == name:
                return False
        
        if (
                isinstance(name, str) 
                and (isinstance(price, float) or isinstance(price, int)) 
                and (isinstance(spice, str) and len(spice) == 1)
                and isinstance(gluten, bool)
            ):
            self.menu.append(
                {
                    'name': name,
                    'price': price,
                    'spice_level': spice,
                    'gluten_index': gluten
                }
            )
            return True
        else:
            return False
        
    def update_item(self, name, price, spice, gluten):
        found = False
        for dish in self.menu:
            if dish['name'] == name:
                found = True
                if isinstance(price, float) or isinstance(price, int):
                    dish['price'] = price

                if isinstance(spice, str) and len(spice) == 1:
                    dish['spice_level'] = spice

                if isinstance(gluten, bool):
                    dish['gluten_index'] = gluten
                    
                break

        return found
    
    def remove_item(self, name):
        found = False
        for dish in self.menu:
            if dish['name'] == name:
                found = True
                self.menu.remove(dish)
                print(self.menu)
                    
                break

        return found