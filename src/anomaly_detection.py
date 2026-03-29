import numpy as np

def detect_anomaly(data, threshold=2):

    if not data or len(data) < 2:
        return False

    mean = np.mean(data)
    std = np.std(data)

    if std == 0:
        return False

    # Adaptive threshold for small datasets
    if len(data) <= 5:
        threshold = 2.2

    for value in data:
        z_score = abs((value - mean) / std)

        if z_score > threshold:
            return True

    return False
