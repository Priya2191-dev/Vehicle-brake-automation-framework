from behave import given, when, then
from simulation.brake_simulator import BrakeSimulator


@given('vehicle speed is {speed:d} km/h')
def step_vehicle_speed(context, speed):

    context.simulator = BrakeSimulator(speed)
    context.initial_speed = speed


@when('brake pedal is pressed with pressure {pressure:d}')
def step_apply_brake(context, pressure):

    context.new_speed = context.simulator.apply_brake(pressure)


@then('vehicle speed should decrease')
def step_verify_speed(context):

    assert context.new_speed < context.initial_speed
