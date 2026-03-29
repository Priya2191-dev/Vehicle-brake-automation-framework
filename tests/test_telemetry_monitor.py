import pytest
from telemetry_monitor import TelemetryMonitor

def test_record_telemetry():
    monitor = TelemetryMonitor()

    monitor.record(80, 40)

    assert len(monitor.logs) == 1
    log = monitor.logs[0]

    assert log["speed"] == 80
    assert log["pressure"] == 40
    assert "timestamp" in log


def test_multiple_records():
    monitor = TelemetryMonitor()

    monitor.record(100, 20)
    monitor.record(80, 40)

    assert len(monitor.logs) == 2


def test_average_speed():
    monitor = TelemetryMonitor()

    monitor.record(100, 20)
    monitor.record(50, 10)

    assert monitor.average_speed() == 75


def test_average_speed_empty():
    monitor = TelemetryMonitor()

    assert monitor.average_speed() == 0


def test_invalid_input():
    monitor = TelemetryMonitor()

    with pytest.raises(ValueError):
        monitor.record(-10, 20)

    with pytest.raises(ValueError):
        monitor.record(50, -5)
