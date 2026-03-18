from can_bus import CANBusSimulator  

def test_send_message():
    sim = CANBusSimulator()

    sim.send_message("ECU1", "ECU2", "speed", 80)

    assert len(sim.messages) == 1
    msg = sim.messages[0]

    assert msg["sender"] == "ECU1"
    assert msg["receiver"] == "ECU2"
    assert msg["signal"] == "speed"
    assert msg["value"] == 80
