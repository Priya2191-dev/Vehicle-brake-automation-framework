from telemetry_monitor import TelemetryMonitor   

def test_record_telemetry():
    monitor = TelemetryMonitor()

    monitor.record(80, 40)

    assert len(monitor.logs) == 1
    log = monitor.logs[0]

    assert log["speed"] == 80
    assert log["pressure"] == 40
