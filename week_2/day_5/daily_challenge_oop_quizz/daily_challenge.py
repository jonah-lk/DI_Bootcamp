# 1. What is a class?
# A blueprint for creating objects, defining attributes and methods.
# 2. What is an instance?
# A specific object created from a class with its own data.
# 3. What is encapsulation?
# Hiding a class’s internal data and controlling access to it.
# 4. What is abstraction?
# Showing only the essential features of an object while hiding details.
# 5. What is inheritance?
# A way for a class to use attributes and methods from another class.
# 6. What is multiple inheritance?
# A class inheriting from more than one parent class.
# 7. What is polymorphism?
# The same method or operator acting differently depending on the object.
# 8. What is Method Resolution Order (MRO)?
# The order Python follows to look for methods in a class hierarchy.

# ex 2
import random

class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"
    
class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = []

    def shuffle(self):
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return "No more cards to deal."
        return self.cards.pop()