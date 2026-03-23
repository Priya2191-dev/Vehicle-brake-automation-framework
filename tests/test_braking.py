from braking import automated_braking

def test_auto_brake():
    assert automated_braking(80, 5) == 40

def test_no_brake_when_safe_distance():
    assert automated_braking(80, 20) == 0

def test_no_brake_when_low_speed():
    assert automated_braking(20, 5) == 0
