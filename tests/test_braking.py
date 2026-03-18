from src.braking import automated_braking

def test_auto_brake():
    assert automated_braking(80, 5) == 40
