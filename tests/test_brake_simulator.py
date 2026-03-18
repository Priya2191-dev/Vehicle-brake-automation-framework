from brake_simulator import BrakeSimulator  

def test_apply_brake_reduces_speed():
    sim = BrakeSimulator(100)
    new_speed = sim.apply_brake(20)

    assert round(new_speed, 2) == 97  # 100 - (20 * 0.15)

def test_speed_not_negative():
    sim = BrakeSimulator(10)
    new_speed = sim.apply_brake(100)

    assert new_speed == 0
