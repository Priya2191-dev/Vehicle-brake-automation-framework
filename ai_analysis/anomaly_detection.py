import numpy as np

def detect_anomaly(speed_values):

    mean_speed = np.mean(speed_values)

    for value in speed_values:

        if abs(value - mean_speed) > 30:
            return True

    return False
