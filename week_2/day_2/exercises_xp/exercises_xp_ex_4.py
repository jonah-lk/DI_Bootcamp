class Person:
    def __init__(self, first_name, age, last_name = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def is_18(self):
        return self.age >= 18

class Family:
    def __init__(self, last_name, members = []):
        self.last_name = last_name
        self.members = members

    def born(self, first_name, age):
        new_person = Person(first_name = first_name, last_name = self.last_name, age = age)
        self.members.append(new_person)

    def check_majority(self, first_name):
        all_with_name = filter(lambda person: person.first_name == first_name, self.members)
        print(first_name)
        for member in all_with_name:
            if member.is_18():
                print('You are over 18, your parents Jane and John accept that you will go out with your friends')
            else:
                print('Sorry, you are not allowed to go out with your friends.')
        
    def family_presentation(self):
        print(self.last_name)
        for member in self.members:
            print(f" - {member.first_name}, age {member.age}")


smith_family = Family("Smith")
smith_family.born("Alice", 10)
smith_family.born("Bob", 20)
smith_family.born("Charlie", 17)
smith_family.check_majority("Alice")
smith_family.check_majority("Bob")
smith_family.check_majority("Charlie")
smith_family.family_presentation()