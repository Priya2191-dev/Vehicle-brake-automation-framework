def apply_brake(speed, pressure):
    if speed < 0:
        raise ValueError("Invalid speed")

    if pressure > 100:
        raise ValueError("Pressure exceeds limit")

    if speed == 0:
        return "Stationary"

    return "Decelerating"
