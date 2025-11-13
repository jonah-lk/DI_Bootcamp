class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking!'

    def run_speed(self):
        return float(self.weight) / int(self.age) * 10

    def fight(self, other_dog):
        strength = self.run_speed() * float(self.weight)
        other_dog_strength = other_dog.run_speed() * float(self.weight)

        if strength > other_dog_strength:
            print(f'{self.name} wins!')
        elif strength < other_dog_strength:
            print(f'{other_dog.name} wins')
        else:
            print('Draw')

muh_dog = Dog('Rex', 10, 90)
muh_other_dog = Dog('Caesar', 14, 94)
some_dog = Dog('Peep', 8, 87)

print(muh_dog.bark())
print(muh_dog.run_speed())
print(some_dog.bark())
muh_other_dog.fight(some_dog)