import math

class Circle:
    circles = []

    def __init__(self, radius = None, diameter = None):
        """
        Initialize circle instance by providing either a radius or diameter
        """
        if radius:
            self.radius = float(radius)
            self.diameter = self.radius * 2
        elif diameter:
            self.diameter = float(diameter)
            self.radius = self.diameter / 2
        else:
            raise Exception('Provide construtor params!')
        Circle.circles.append(self)
        Circle.circles.sort(key = lambda instance: instance.radius)
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def __add__(self, circle):
        if isinstance(circle, Circle):
            radius = self.radius + circle.radius
            return Circle(radius = radius)
        else:
            raise Exception('Provide a circle as param!')
        
    def __gt__(circle1, circle2):
        if isinstance(circle1, Circle) and isinstance(circle2, Circle):
            return circle1.radius > circle2.radius
        else:
            raise Exception('Provide a circle as param!')
        
    def __eq__(circle1, circle2):
        if isinstance(circle1, Circle) and isinstance(circle2, Circle):
            return circle1.radius == circle2.radius
        else:
            raise Exception('Provide a circle as param!')
    
    def __str__(self):
        return f'r = {self.radius}.\nd = {self.diameter}.\na = {self.area()}'