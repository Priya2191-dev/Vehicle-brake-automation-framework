import numpy as np

def detect_anomaly(speed_values, threshold=2):
    mean = np.mean(speed_values)
    std = np.std(speed_values)

    if std == 0:
        return False

    return any(abs(v - mean) > threshold * std for v in speed_values)
