import pytest
from anomaly_detection import detect_anomaly

def test_detect_anomaly_true():
    # Large deviation → anomaly
    speeds = [50, 55, 60, 120]
    assert detect_anomaly(speeds) == True


def test_detect_anomaly_false():
    # Normal variation → no anomaly
    speeds = [50, 55, 60, 58]
    assert detect_anomaly(speeds) == False


def test_no_variation():
    # All values same → std = 0 → no anomaly
    speeds = [50, 50, 50, 50]
    assert detect_anomaly(speeds) == False


def test_custom_threshold():
    # Lower threshold → more sensitive
    speeds = [50, 55, 60, 70]
    assert detect_anomaly(speeds, threshold=1) == True


def test_empty_input():
    # Edge case
    speeds = []
    assert detect_anomaly(speeds) == False
