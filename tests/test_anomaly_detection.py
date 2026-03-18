from anomaly_detection import detect_anomaly

def test_detect_anomaly_true():
    speeds = [50, 55, 60, 120]
    assert detect_anomaly(speeds) is True

def test_detect_anomaly_false():
    speeds = [50, 55, 60, 58]
    assert detect_anomaly(speeds) is False
