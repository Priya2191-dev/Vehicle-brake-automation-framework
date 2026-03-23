from braking import automated_braking

def test_emergency_brake():
    assert automated_braking(80, 5) == 40

def test_full_brake():
    assert automated_braking(100, 3) == 80

def test_mild_brake():
    assert automated_braking(60, 15) == 20

def test_no_brake_safe_distance():
    assert automated_braking(80, 30) == 0

def test_no_brake_zero_speed():
    assert automated_braking(0, 5) == 0

def test_invalid_input():
    with pytest.raises(ValueError):
        automated_braking(-10, 5)
