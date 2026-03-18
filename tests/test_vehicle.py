from vehicle import Vehicle

def test_braking():
    v = Vehicle()
    v.accelerate(100)
    speed = v.apply_brake(20)
    assert speed < 100
