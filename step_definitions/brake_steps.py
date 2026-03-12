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


@given('obstacle distance is {distance:d} meters')
def step_obstacle(context, distance):

    context.distance = distance


@when('automated braking system activates')
def step_auto_brake(context):

    if context.distance < 10:
        context.brake_pressure = 40
        context.new_speed = context.initial_speed - 20
    else:
        context.brake_pressure = 0
        context.new_speed = context.initial_speed


@then('brake pressure should increase')
def step_pressure(context):

    assert context.brake_pressure > 0


@then('brake pressure should remain zero')
def step_no_pressure(context):

    assert context.brake_pressure == 0
