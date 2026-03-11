class TelemetryMonitor:

    def __init__(self):
        self.logs = []

    def record(self, speed, pressure):

        data = {
            "speed": speed,
            "brake_pressure": pressure
        }

        self.logs.append(data)

    def display(self):

        for log in self.logs:
            print(log)
