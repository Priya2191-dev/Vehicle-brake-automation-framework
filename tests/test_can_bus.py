import pytest
from can_bus import CANBusSimulator

def test_send_message():
    sim = CANBusSimulator()

    sim.send_message("ECU1", "ECU2", "speed", 80, 0x101)

    assert len(sim.messages) == 1
    msg = sim.messages[0]

    assert msg["sender"] == "ECU1"
    assert msg["receiver"] == "ECU2"
    assert msg["signal"] == "speed"
    assert msg["value"] == 80
    assert msg["id"] == hex(0x101)

def test_filter_by_sender():
    sim = CANBusSimulator()

    sim.send_message("ECU1", "ECU2", "speed", 80, 0x101)
    sim.send_message("ECU2", "ECU3", "temp", 90, 0x102)

    ecu1_msgs = sim.get_messages_by_sender("ECU1")

    assert len(ecu1_msgs) == 1
    assert ecu1_msgs[0]["sender"] == "ECU1"

def test_invalid_sender():
    sim = CANBusSimulator()

    with pytest.raises(ValueError):
        sim.send_message("", "ECU2", "speed", 80, 0x101)

def test_invalid_can_id():
    sim = CANBusSimulator()

    with pytest.raises(ValueError):
        sim.send_message("ECU1", "ECU2", "speed", 80, -1)
