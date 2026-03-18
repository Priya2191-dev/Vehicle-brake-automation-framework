class Vehicle:
    def __init__(self):
        self.speed = 0
        self.brake_pressure = 0

    def accelerate(self, value):
        self.speed += value

    def apply_brake(self, pressure):
        self.brake_pressure = pressure
        self.speed -= pressure * 0.2
        return max(self.speed, 0)
