import numpy as np

def detect_anomaly(data, threshold=1.5):  

    if not data:
        return False

    if len(data) < 2:
        return False

    mean = np.mean(data)
    std = np.std(data)

    if std == 0:
        return False

    for value in data:
        z_score = abs((value - mean) / std)

        if z_score > threshold:
            return True

    return False
