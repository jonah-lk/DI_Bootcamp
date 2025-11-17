class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []
    
    def add_family_member(self, person):
        if person not in self.family:
            self.family.append(person)
        if self not in person.family:
            person.family.append(self)

class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        if person.priority or person.age > 60:
            self.humans = [person] + self.humans
        else:
            self.humans += [person]

    def find_in_queue(self, person):
        for i in range(len(self.humans)):
            if self.humans[i] == person:
                return i
        return -1
    
    def swap(self, person1, person2):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        if index1 != -1 and index2 != -1:
            self.humans[index1], self.humans[index2] = self.humans[index2], self.humans[index1]

    def get_next(self):
        if len(self.humans) == 0:
            return None
        person = self.humans[0]
        self.humans = self.humans[1:]
        return person
    
    def get_next_blood_type(self, blood_type):
        for i in range(len(self.humans)):
            if self.humans[i].blood_type == blood_type:
                person = self.humans[i]
                self.humans = self.humans[:i] + self.humans[i+1:]
                return person
        return None
    
    def sort_by_age(self):
        n = len(self.humans)
        for i in range(n):
            max_index = i
            for j in range(i+1, n):
                if self.humans[j].priority and not self.humans[max_index].priority:
                    max_index = j
                elif (self.humans[j].priority == self.humans[max_index].priority and
                      self.humans[j].age > self.humans[max_index].age):
                    max_index = j
            self.humans[i], self.humans[max_index] = self.humans[max_index], self.humans[i]

    def rearrange_queue(self):
        new_queue = []
        temp_list = self.humans.copy()

        while temp_list:
            placed = False
            for i, person in enumerate(temp_list):
                if not new_queue or new_queue[-1] not in person.family:
                    new_queue.append(person)
                    temp_list.pop(i)
                    placed = True
                    break
            if not placed:
                new_queue.append(temp_list.pop(0))

        self.humans = new_queue