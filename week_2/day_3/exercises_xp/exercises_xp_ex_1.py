class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = int(amount)

    def __str__(self):
        return f'{self.amount} {self.currency}'
    
    def __int__(self):
        return int(self.amount)
    
    def __repr__(self):
        return f'{self.amount} {self.currency}'
    
    def __add__(self, amount):
        if isinstance(amount, Currency) and amount.currency != self.currency:
            raise Exception('Invalid operation! Must be of same currency.')
        return int(self.amount) + int(amount)
    
    def __iadd__(self, amount):
        if isinstance(amount, Currency) and amount.currency != self.currency:
            raise Exception('Invalid operation! Must be of same currency.')
        self.amount += int(amount)
        return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
print(c1 + c3)