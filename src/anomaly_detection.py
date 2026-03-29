import numpy as np

def detect_anomaly(data):

    if len(data) == 0:
        return False

    mean = np.mean(data)
    std = np.std(data)

    for value in data:
        if abs(value - mean) > 2 * std:
            return True

    return False
