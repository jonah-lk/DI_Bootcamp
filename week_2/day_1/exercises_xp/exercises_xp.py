# Exercise 1: Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat_1 = Cat('Tom', 2)
cat_2 = Cat('Marcus Aurelius', 10)
cat_3 = Cat('Achilles', 2)

def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    if cat2.age > oldest.age:
        oldest = cat2
    elif cat3.age > oldest.age:
        oldest = cat3
    return oldest

oldy = find_oldest_cat(cat_1, cat_2, cat_3)
print(f'The oldest cat is {oldy.name}, it\'s age is {oldy.age}')

# Exercise 2: Dogs
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = round(float(height), 2)

    def bark(self):
        print(f'{self.name} woof woof!')

    def jump(self):
        print(f'{self.name} jumps {self.height * 2} cm heigh!')

davids_dog = Dog('Max', 33)
sarahs_dog = Dog('Alexander The Great', 40)

print(f'{davids_dog.name} is {davids_dog.height} cm tall!')
davids_dog.bark()
davids_dog.jump()
print(f'{sarahs_dog.name} is {sarahs_dog.height} cm tall!')

print(f'The talest dog is {davids_dog.name if davids_dog.height > sarahs_dog.height else sarahs_dog.name}.')

# Exercise 3 : Who’s the song producer?
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics if isinstance(lyrics, list) else []

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# Exercise 4 : Afternoon at the Zoo
class Zoo:
    def __init__(self, zoo_name, animals):
        self.zoo_name = animals
        self.animals = animals if isinstance(animals, list) else []

    def add_animal(self, new_animal):
        if new_animal.lower() not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        self.animals_grouped = {}
        for animal in self.animals:
            first_letter = animal[0]
            if first_letter in self.animals_grouped.keys():
                self.animals_grouped[first_letter].append(animal)
            else:
                self.animals_grouped[first_letter] = [animal]

    def get_groups(self):
        for animal_group_key, animal_group_value in self.animals_grouped.items():
            print(f'{animal_group_key}: {animal_group_value}')

my_zoo = Zoo('Bioparco di Roma', ['Ostrich', 'Giraffe', 'Gorilla', 'Zebra', 'Tiger', 'Lion'])
my_zoo.add_animal('Elephant')
my_zoo.get_animals()
my_zoo.sell_animal('Ostrich')
my_zoo.sort_animals()
my_zoo.get_groups()