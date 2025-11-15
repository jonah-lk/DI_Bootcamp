class Temperature:
    def __init__(self, temp, unit):
        self.temp = temp
        self.unit = unit

    def convert(from_unit, to_unit, formula):
        return formula(from_unit, to_unit)

class Celsius(Temperature):
    def __init__(self, temp):
        super().__init__(temp, unit = 'C')

    def convert(self, to_unit):
        if isinstance(to_unit, Kelvin):
            return self.to_kelvin_formula()
        elif isinstance(to_unit, Fahrenheit):
            return self.to_fah_formula()
    
    def to_kelvin_formula(self):
        return self.temp + 273.15
    
    def to_fah_formula(self):
        return (self.temp * (9/5)) + 32
    
class Kelvin(Temperature):
    def __init__(self, temp):
        super().__init__(temp, unit = 'K')

    def convert(self, to_unit):
        if isinstance(to_unit, Celsius):
            return self.to_celsius_formula()
        elif isinstance(to_unit, Fahrenheit):
            return self.to_fah_formula()
    
    def to_celsius_formula(self):
        return self.temp - 273.15
    
    def to_fah_formula(self):
        return self.to_celsius_formula() * (9/5) + 32

class Fahrenheit(Temperature):
    def __init__(self, temp):
        super().__init__(temp, unit = 'F')

    def convert(self, to_unit):
        if isinstance(to_unit, Celsius):
            return self.to_celsius_formula()
        elif isinstance(to_unit, Kelvin):
            return self.to_kelvin_formula()
    
    def to_celsius_formula(self):
        return (self.temp - 32) * (5/9)
    
    def to_kelvin_formula(self):
        return self.to_celsius_formula() + 273.15
    
c = Celsius(25)
k = Kelvin(400)
f = Fahrenheit(90)

print(c.convert(k), k.unit)
print(c.convert(f), f.unit)