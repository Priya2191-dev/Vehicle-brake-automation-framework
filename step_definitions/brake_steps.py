from simulation.brake_simulator import BrakeSimulator

def test_brake():

    sim = BrakeSimulator(100)

    new_speed = sim.apply_brake(20)

    assert new_speed < 100
