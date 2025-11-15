import random

class QuantumParticle:
    def __init__(self, position = random.randint(1, 10_000), momentum = random.random(), spin = random.choice([1/2, -1/2])):
        self.x = position
        self.y = momentum
        self.p = spin
        self.entangled = None

    def position(self):
        self.x = random.randint(1, 10_000)
        self.disturbence()

    def momentum(self):
        self.y = random.random()
        self.disturbence()

    def spin(self):
        self.p = random.choice([1/2, -1/2])
        self.disturbence()
        if self.entangled:
            self.entangled.p = self.p * -1

    def disturbence(self):
        self.x = random.randint(1, 10_000)
        self.y = random.random()
        print('Quantum Interferences!')

    def entangle(self, particle):
        self.entangled = particle
        particle.entangled = self
        self.spin()
        print('Spooky Action at a Distance!')

    def __repr__(self):
        return f'(x: {self.x}, y: {self.y}) spin[{self.p}]'
    
p1 = QuantumParticle()
p2 = QuantumParticle()
p1.entangle(p2)