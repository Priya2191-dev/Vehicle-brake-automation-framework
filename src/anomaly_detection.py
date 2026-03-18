import numpy as np

def detect_anomaly(speed_values):
    mean = np.mean(speed_values)
    return any(abs(v - mean) > 30 for v in speed_value)
