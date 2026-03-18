class BrakeSimulator:
    def __init__(self, speed):
        self.speed = speed

    def apply_brake(self, pressure):
        self.speed -= pressure * 0.15
        return max(self.speed, 0)
