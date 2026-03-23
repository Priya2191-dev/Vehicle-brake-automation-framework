import logging

logging.basicConfig(level=logging.INFO)

def automated_braking(speed, distance):
    """
    Determines brake pressure based on speed and obstacle distance.
    """

    # Input validation
    if speed < 0 or distance < 0:
        raise ValueError("Speed and distance must be non-negative")

    logging.info(f"Evaluating braking | Speed: {speed}, Distance: {distance}")

    # Advanced braking logic
    if speed == 0:
        return 0

    if distance < 5:
        pressure = 80   # Full brake (critical)
    elif distance < 10:
        pressure = 40   # Medium brake
    elif distance < 20:
        pressure = 20   # Mild brake
    else:
        pressure = 0    # Safe distance

    logging.info(f"Brake pressure applied: {pressure}")
    return pressure
