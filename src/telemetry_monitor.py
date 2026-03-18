class TelemetryMonitor:
    def __init__(self):
        self.logs = []

    def record(self, speed, pressure):
        self.logs.append({"speed": speed, "pressure": pressure})
