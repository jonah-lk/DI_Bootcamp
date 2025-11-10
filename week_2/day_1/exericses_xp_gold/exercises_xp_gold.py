import math, random

# Ex 1:
class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def calculate_area(self):
        self.area = (self.radius ** 2) * math.pi
        print(f'Circle area: {self.area}')

    def calculate_perimeter(self):
        self.perimeter = 2 * self.radius * math.pi
        print(f'Circle perimeter: {self.perimeter}')

    def definition(self):
        print('A circle is the set of all points in a plane that are equidistant from a fixed point.')

# Ex 2:
class MyList:
    def __init__(self, letters_list):
        self.letters_list = []
        for letter in letters_list:
            self.letters_list.append(letter[0])

    def reverse_letters(self):
        reversed_list = self.letters_list
        reversed_list.reverse()
        return reversed_list
    
    def sorted_letters(self):
        sorted_list = self.letters_list
        sorted_list.sort()
        return sorted_list
    
    def random_list(self):
        random_list = [random.randint(1, 10) for i in range(len(self.letters_list))]
        return random_list