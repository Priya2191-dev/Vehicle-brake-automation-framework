import pytest
from brake_simulator import apply_brake


#  Positive Test Cases

def test_stationary_when_speed_zero():
    result = apply_brake(0, 50)
    assert result == "Stationary"


def test_decelerating_when_valid_inputs():
    result = apply_brake(60, 30)
    assert result == "Decelerating"


#  Negative Test Cases

def test_invalid_negative_speed():
    with pytest.raises(ValueError, match="Invalid speed"):
        apply_brake(-10, 50)


def test_pressure_exceeds_limit():
    with pytest.raises(ValueError, match="Pressure exceeds limit"):
        apply_brake(60, 150)


#  Edge Cases

def test_boundary_pressure_100():
    result = apply_brake(80, 100)
    assert result == "Decelerating"


def test_minimum_valid_speed():
    result = apply_brake(1, 10)
    assert result == "Decelerating"
