import time
import logging

logging.basicConfig(level=logging.INFO)

class TelemetryMonitor:

    def __init__(self):
        self.logs = []

    def record(self, speed, pressure):
        # Validation
        if speed < 0 or pressure < 0:
            raise ValueError("Invalid values")

        log = {
            "timestamp": time.time(),
            "speed": speed,
            "pressure": pressure
        }

        self.logs.append(log)

        logging.info(f"Recorded: {log}")

    def average_speed(self):
        if not self.logs:
            return 0
        return sum(log["speed"] for log in self.logs) / len(self.logs)
