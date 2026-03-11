class BrakeSimulator:

    def __init__(self, speed):
        self.speed = speed

    def apply_brake(self, pressure):

        deceleration = pressure * 0.15
        self.speed -= deceleration

        if self.speed < 0:
            self.speed = 0

        return self.speed
