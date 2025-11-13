# Ex 1
class Pets:
    def __init__(self, all_cats):
        self.all_cats = all_cats

    def walk(self):
        for cat in self.all_cats:
            print(f'{cat.name} is one of the cats walking here!')

class Cat():
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age
    
    def walk(self):
        print(f'{self.name} is walking here!')

class Siamese(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def walk(self):
        print(f'{self.name} is walking here!')

class Bengal(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def walk(self):
        print(f'{self.name} is walking here!')

class Chartreux(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def walk(self):
        print(f'{self.name} is walking here!')

siamese_obj = Siamese('Mimi', 9)
bengal_obj = Bengal('Lulu', 5)
chartreux_obj = Chartreux('Luki', 4)

all_cats = [siamese_obj, bengal_obj, chartreux_obj]

sara_pets = Pets(all_cats)

sara_pets.walk()
siamese_obj.walk()
chartreux_obj.walk()
bengal_obj.walk()