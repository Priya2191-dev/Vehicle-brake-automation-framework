import numpy as np

def detect_anomaly(data, threshold=2):

    # Handle empty input
    if not data:
        return False

    # If only one value → no anomaly
    if len(data) < 2:
        return False

    mean = np.mean(data)
    std = np.std(data)

    # Avoid division by zero
    if std == 0:
        return False

    for value in data:
        z_score = abs((value - mean) / std)

        if z_score > threshold:
            return True

    return False
