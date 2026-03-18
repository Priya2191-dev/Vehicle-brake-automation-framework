def automated_braking(speed, obstacle_distance):
    if obstacle_distance < 10 and speed > 30:
        return 40
    return 0
