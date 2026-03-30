import pytest
from anomaly_detection import detect_anomaly

def test_absolute_anomaly():
    data = [50, 55, 60, 120]  # deviation > 30
    assert detect_anomaly(data) == True


def test_zscore_anomaly():
    data = [50, 52, 53, 80]  # smaller deviation but high z-score
    assert detect_anomaly(data, threshold=1.5) == True


def test_no_anomaly():
    data = [50, 52, 53, 54]
    assert detect_anomaly(data) == False


def test_empty_data():
    assert detect_anomaly([]) == False


def test_single_value():
    assert detect_anomaly([50]) == False


def test_zero_std():
    data = [50, 50, 50, 50]
    assert detect_anomaly(data) == False
