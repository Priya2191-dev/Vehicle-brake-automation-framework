class Vehicle:

    def __init__(self, mass=1500):
        self.mass = mass
        self.speed = 0
        self.brake_pressure = 0

    def accelerate(self, value):
        self.speed += value

    def apply_brake(self, pressure):

        self.brake_pressure = pressure
        self.speed -= pressure * 0.2

        if self.speed < 0:
            self.speed = 0

        return self.speed
