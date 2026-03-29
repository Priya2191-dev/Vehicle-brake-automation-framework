import numpy as np

def detect_anomaly(data, threshold=2):

    if not data or len(data) < 2:
        return False

    mean = np.mean(data)
    std = np.std(data)

    for value in data:
        deviation = abs(value - mean)

        # Absolute deviation (strong anomaly detection)
        if deviation > 30:
            return True

        # Z-score (statistical detection)
        if std != 0:
            z_score = abs((value - mean) / std)
            if z_score > threshold:
                return True

    return False
