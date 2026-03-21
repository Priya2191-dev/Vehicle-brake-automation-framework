def validate_brake(speed, pressure):
    # Check length mismatch
    if len(speed) != len(pressure):
        return False

    for s, p in zip(speed, pressure):
        # Negative values check
        if s < 0 or p < 0:
            return False
        
        # Zero speed condition
        if s == 0 and p == 0:
            continue
        
        # Threshold validation
        if p < s * 0.3:
            return False

    return True
