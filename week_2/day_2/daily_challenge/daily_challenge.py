import math

class Pagination:
    def __init__(self, items = None, page_size = 10):
        if items == None:
            self.items = []
        else:
            self.items = items
        try:
            self.page_size = int(page_size)
        except:
            self.page_size = 10
        self.current_index = 0
        self.page_count = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        start = self.current_index
        end = self.current_index + self.page_size
        if end > len(self.items):
            end = len(self.items)
        return self.items[start:end]
    
    def got_to_page(self, page_number):
        try:
            if page_number < 1 or page_number > self.page_count:
                raise ValueError
            self.current_index =  self.page_size * (page_number - 1)
            return self.get_visible_items()
        except ValueError:
            print('Value error!')

    def first_page(self):
        self.current_index = 0
        return self
    
    def last_page(self):
        self.current_index = (self.page_count - 1) * self.page_size
        return self
    
    def next_page(self):
        if self.current_index + self.page_size < len(self.items):
            self.current_index += self.page_size
        return self
    
    def prev_page(self):
        if self.current_index - self.page_size >= 0:
            self.current_index -= self.page_size
        return self
    
    def __str__(self):
        string = ''
        for i in range(self.current_index, self.current_index + self.page_size):
            string += f'{self.items[i]}\n'
        return string
    
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(p.get_visible_items())
print(p.next_page().get_visible_items())
print(p.last_page().get_visible_items())
p.got_to_page(12)
print(p.get_visible_items())
print(p.current_index + 1)
p.got_to_page(0)
p.got_to_page(1)
print(p.next_page().next_page().next_page().get_visible_items())