from exercises_xp_ex_2 import Dog
from random import randint

class PetDog(Dog):
    tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]

    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        if len(args) == 0:
            print(f'{self.name} is playing by himself!')
        else:
            dog_names = []
            for dog in args:
                dog_names.append(dog.name)
            sentence = ', '.join(dog_names)
            sentence += ' all play together.' if len(dog_names) >= 1 else 'No dogs here!'
            print(sentence)

    def do_a_trick(self):
        if self.trained:
            print(f'{self.name} {PetDog.tricks[randint(0, len(PetDog.tricks))]}')
        else:
            print(f'{self.name} is not trained!')

my_pet_dog = PetDog('Rex', 10, 40, True)
my_pet_dog.train()
my_pet_dog.play()
my_pet_dog.do_a_trick()