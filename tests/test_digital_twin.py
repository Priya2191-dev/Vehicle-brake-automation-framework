from digital_twin import Vehicle

def test_braking():
    v = Vehicle()
    v.accelerate(100)
    speed = v.apply_brake(20)
    assert speed == 96

def test_brake_not_negative():
    v = Vehicle()
    v.accelerate(10)
    speed = v.apply_brake(100)
    assert speed == 0

def test_brake_not_apply():
     v = Vehicle()
     v.accelerate(100)
     speed = v.apply_brake(0)
     assert speed == 100
