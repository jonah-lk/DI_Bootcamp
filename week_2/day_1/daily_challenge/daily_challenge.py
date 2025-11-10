class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count = 1):
        if animal_type.lower() in self.animals.keys():
            self.animals[animal_type] += count
        else:
            self.animals[animal_type.lower()] = count
        
    def get_info(self):
        info = f'{self.name} farm\n\n'
        column_width = len(max(self.animals.keys()))
        for animal, count in self.animals.items():
            info += f'{animal}{' ' * (column_width - len(animal))} : {count}\n'
        info += '\n\tE-I-E-I-0!'
        return info
    
    def get_animal_types(self):
        types = []
        for animal in self.animals.keys():
            types.append(animal)
        types = list(sorted(types))
        return types
    
    def get_short_info(self):
        info = f'{self.name} farm has '
        types = self.get_animal_types()
        for type in types:
            if self.animals[type] > 1:
                types[types.index(type)] += 's'
        info += ', '.join(types)
        return info
    
    def add_animals(self, **kwargs):
        for kwarg, count in kwargs.items():
            if kwarg.lower() in self.animals.keys():
                self.animals[kwarg] += count
            else:
                self.animals[kwarg.lower()] = count

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
macdonald.add_animals(cow = 5, sheep = 2, goat = 12)
print(macdonald.get_info())